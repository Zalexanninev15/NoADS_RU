import os
import re
import requests
from urllib.parse import urlparse
from datetime import datetime

def last_modified_line():
    months = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля",
        5: "мая", 6: "июня", 7: "июля", 8: "августа",
        9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    }
    today = datetime.today()
    return f"! Last modified: {today.day} {months[today.month]} {today.year} года\n"

def load_exceptions(exc_file="exceptions.txt"):
    """Загружает исключения: каждая строка — точное правило или регулярное выражение.
    Формат: строка начинается с r/.../ или строка с правилом.
    """
    exceptions = {"exact": set(), "regex": []}
    if not os.path.exists(exc_file):
        return exceptions
    try:
        with open(exc_file, 'r', encoding='utf-8-sig') as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith('#') or line.startswith('!'):
                    continue
                # regex style: r/.../  (пример: r/ads\.\w+\.com/)
                if line.startswith('r/') and line.endswith('/'):
                    try:
                        pattern = re.compile(line[2:-1])
                        exceptions["regex"].append(pattern)
                    except re.error:
                        # пропустить некорректный шаблон
                        continue
                else:
                    exceptions["exact"].add(line)
    except Exception:
        return exceptions
    return exceptions

def is_exception(rule, exceptions):
    """Проверяет правило на попадание в исключения: строка с правилом или regex."""
    if not rule or not exceptions:
        return False
    if rule in exceptions.get("exact", ()):
        return True
    for pat in exceptions.get("regex", ()):
        if pat.search(rule):
            return True
    return False

def download_file(url):
    """Загружает содержимое файла по URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.RequestException as e:
        print(f"Ошибка при загрузке {url}: {e}")
        return []

def read_file(file_path):
    """Читает содержимое локального файла."""
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print(f"⚠️  {file_path}")
        return []
    except Exception as e:
        print(f"Ошибка при чтении {file_path}: {e}")
        return []

def is_comment(line):
    """Проверяет, является ли строка комментарием (начинается с !, !! или #, но не фильтром)."""
    line = line.strip()
    if not line:
        return True
    return (line.startswith('!') or 
            line.startswith('!!') or 
            (line.startswith('#') and not line.startswith('##') and not line.startswith('#?')))

def clean_rule(line):
    """Очищает строку от комментариев и лишних пробелов/табов."""
    line = line.encode('utf-8').decode('utf-8-sig').lstrip().rstrip()
    if not line:
        return None
    if line.lower().startswith('[adblock plus 2.0]'):  # убираем заголовок
        return None
    if is_comment(line):
        return None
    if '  # ' in line:  # удаляем комментарии вида "  # ..."
        return line.split('  # ', 1)[0].rstrip()
    return line

def clean_rules(lines, exceptions=None):
    """Удаляет комментарии из списка строк и очищает правила. Пропускает исключения."""
    exceptions = exceptions or {"exact": set(), "regex": []}
    cleaned = []
    for line in lines:
        rule = clean_rule(line)
        if not rule:
            continue
        if is_exception(rule, exceptions):
            # пропускаем правило, попавшее в исключения
            continue
        cleaned.append(rule)
    return cleaned

def parse_cleaned_rules(cleaned_file):
    """Парсит файл с очищенными правилами и возвращает словарь {название_фильтра: [правила]}."""
    filters = {}
    try:
        with open(cleaned_file, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Файл {cleaned_file} не найден")
        return filters
    
    current_filter = None
    current_rules = []
    
    for line in lines:
        line_stripped = line.strip()
        
        # Проверяем, является ли строка названием фильтра
        if line_stripped.startswith('!') and not line_stripped.startswith('!!'):
            # Сохраняем предыдущий фильтр
            if current_filter and current_rules:
                filters[current_filter] = current_rules
            
            # Начинаем новый фильтр
            current_filter = line_stripped[1:].strip()
            current_rules = []
        elif line_stripped and current_filter:
            # Добавляем правило к текущему фильтру
            current_rules.append(line_stripped)
    
    # Сохраняем последний фильтр
    if current_filter and current_rules:
        filters[current_filter] = current_rules
    
    return filters

def update_target_file(target_file, cleaned_filters, exceptions=None):
    """Обновляет целевой файл, заменяя правила фильтров на очищенные, с учётом исключений.
    Всегда объявляет updated_lines, корректно обрабатывает ранние выходы и вставляет/обновляет
    строку '! Last modified: ...'.
    """
    exceptions = exceptions or {"exact": set(), "regex": []}

    if not os.path.exists(target_file):
        print(f"Файл {target_file} не найден, пропускаем")
        return

    # Гарантируем, что updated_lines существует всегда
    updated_lines = []

    try:
        with open(target_file, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Ошибка при чтении {target_file}: {e}")
        return

    i = 0
    while i < len(lines):
        line = lines[i]
        line_stripped = line.strip()

        # Проверяем, является ли строка названием фильтра
        if line_stripped.startswith('!') and not line_stripped.startswith('!!'):
            filter_name = line_stripped[1:].strip()

            # Проверяем, есть ли этот фильтр в очищенных правилах
            if filter_name in cleaned_filters:
                print(f"🔃 Обновляем фильтр '{filter_name}'")

                # Добавляем строку с названием фильтра
                updated_lines.append(line)
                i += 1

                # Подсчитываем строки до первой пустой (1-3 строки заголовка)
                header_lines = []
                found_empty = False
                header_count = 0

                while i < len(lines) and header_count < 3:
                    if lines[i].strip() == '':
                        found_empty = True
                        header_lines.append(lines[i])
                        i += 1
                        break
                    header_lines.append(lines[i])
                    header_count += 1
                    i += 1

                # Если нашли пустую строку после заголовка (вариант 1)
                if found_empty and header_count > 0:
                    # Добавляем строки заголовка
                    updated_lines.extend(header_lines)

                    # Пропускаем старые правила до следующей пустой строки
                    while i < len(lines) and lines[i].strip() != '':
                        i += 1

                    # Добавляем новые очищенные правила (пропуская исключения)
                    for rule in cleaned_filters[filter_name]:
                        if is_exception(rule, exceptions):
                            continue
                        updated_lines.append(f"{rule}\n")

                    # Добавляем пустую строку в конце
                    if i < len(lines) and lines[i].strip() == '':
                        updated_lines.append(lines[i])
                        i += 1
                    else:
                        updated_lines.append("\n")
                else:
                    # Вариант 2: нет заголовка, правила сразу после названия
                    # Возвращаем индекс назад, если читали не-пустые строки
                    i -= len(header_lines)

                    while i < len(lines) and lines[i].strip() != '':
                        i += 1

                    # Добавляем новые очищенные правила (пропуская исключения)
                    for rule in cleaned_filters[filter_name]:
                        if is_exception(rule, exceptions):
                            continue
                        updated_lines.append(f"{rule}\n")

                    # Добавляем пустую строку в конце
                    if i < len(lines) and lines[i].strip() == '':
                        updated_lines.append(lines[i])
                        i += 1
                    else:
                        updated_lines.append("\n")
            else:
                updated_lines.append(line)
                i += 1
        else:
            # Обычная строка, не название фильтра
            updated_lines.append(line)
            i += 1

    # Вставляем/обновляем строку Last modified
    lm = last_modified_line()
    found = False
    for idx, l in enumerate(updated_lines):
        if l.startswith('! Last modified:'):
            updated_lines[idx] = lm
            found = True
            break
    if not found:
        # Вставляем в начало файла (можно настроить позицию при желании)
        updated_lines.insert(0, lm)

    # Записываем обновлённый файл
    try:
        with open(target_file, 'w', encoding='utf-8') as f:
            f.writelines(updated_lines)
        print(f"💾 Файл {target_file} успешно обновлён!\n===+++===")
    except Exception as e:
        print(f"Ошибка при записи {target_file}: {e}")

def process_files(input_file, output_file, exceptions=None):
    """Обрабатывает файлы из списка и сохраняет очищенные правила в output_file."""
    exceptions = exceptions or {"exact": set(), "regex": []}
    try:
        with open(input_file, 'r', encoding='utf-8-sig') as f:
            file_list = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Файл {input_file} не найден")
        return
    except Exception as e:
        print(f"Ошибка при чтении {input_file}: {e}")
        return

    with open(output_file, 'w', encoding='utf-8') as out:
        for file_source in file_list:
            if '=' in file_source:
                file_source, filter_name = file_source.split('=', 1)
            else:
                file_source = file_source.strip()
                filter_name = os.path.basename(urlparse(file_source).path)

            if file_source.startswith(('http://', 'https://')):
                lines = download_file(file_source)
            else:
                lines = read_file(file_source)

            cleaned_rules = clean_rules(lines, exceptions=exceptions)
            if cleaned_rules:
                out.write(f"! {filter_name.strip()}\n")
                for rule in cleaned_rules:
                    out.write(f"{rule}\n")
                out.write("\n")

def remove_exception_lines_after_update(target_file, exceptions=None):
    """После обновления файла удаляет строки, соответствующие исключениям, полностью (без пустых строк)."""
    exceptions = exceptions or {"exact": set(), "regex": []}
    try:
        with open(target_file, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Ошибка при чтении {target_file}: {e}")
        return

    new_lines = []
    for line in lines:
        s = line.strip()
        if not s:
            new_lines.append(line)
            continue

        # Пропускаем строчки-комментарии и заголовки
        if s.startswith('!') and not (s.startswith('!!')):
            new_lines.append(line)
            continue

        # Если строка совпадает с исключением — пропускаем её (не добавляем)
        if is_exception(s, exceptions):
            continue

        new_lines.append(line)

    # Удаляем подряд идущие пустые строки (сохраняем максимум одну подряд)
    compact_lines = []
    prev_empty = False
    for ln in new_lines:
        if ln.strip() == '':
            if not prev_empty:
                compact_lines.append(ln)
            prev_empty = True
        else:
            compact_lines.append(ln)
            prev_empty = False

    try:
        with open(target_file, 'w', encoding='utf-8') as f:
            f.writelines(compact_lines)
    except Exception as e:
        print(f"Ошибка при записи {target_file}: {e}")

def main():
    input_file = "file_list.txt"
    output_file = "cleaned_rules.txt"
    exceptions_file = "exceptions.txt"
    
    exceptions = load_exceptions(exceptions_file)
    print(f"⏳ Шаг 1: Загрузка исключений...")
    print(f"👍 Загружено исключений: {len(exceptions.get('exact',()))} строк(и) с правилами, {len(exceptions.get('regex',()))} regex\n")
    
    print("⏳ Шаг 2: Получение и очистка правил...")
    process_files(input_file, output_file, exceptions=exceptions)
    print(f"💾 Очищенные правила сохранены в {output_file}\n")
    
    print("⏳ Шаг 3: Парсинг очищенных правил...")
    cleaned_filters = parse_cleaned_rules(output_file)
    print(f"👍 Найдено {len(cleaned_filters)} фильтров для обновления\n")
    
    print("⏳ Шаг 4: Обновление файлов NoADS_RU...")
    target_files = [
        "../ads_list.txt",
        "../ads_list_extended.txt",
        "../ads_list_extended_plus.txt",
        "../ads_list_rws.txt"
    ]
    
    for target_file in target_files:
        update_target_file(target_file, cleaned_filters, exceptions=exceptions)
        remove_exception_lines_after_update(target_file, exceptions=exceptions)
    
    print("\n🥳 Готово!")

if __name__ == "__main__":
    main()

