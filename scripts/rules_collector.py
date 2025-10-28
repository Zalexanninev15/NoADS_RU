import os
import re
import requests
from urllib.parse import urlparse

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
        print(f"Файл {file_path} не найден")
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

def clean_rules(lines):
    """Удаляет комментарии из списка строк и очищает правила."""
    return [rule for line in lines if (rule := clean_rule(line))]

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

def update_target_file(target_file, cleaned_filters):
    """Обновляет целевой файл, заменяя правила фильтров на очищенные."""
    if not os.path.exists(target_file):
        print(f"Файл {target_file} не найден, пропускаем")
        return
    
    try:
        with open(target_file, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Ошибка при чтении {target_file}: {e}")
        return
    
    updated_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        line_stripped = line.strip()
        
        # Проверяем, является ли строка названием фильтра
        if line_stripped.startswith('!') and not line_stripped.startswith('!!'):
            filter_name = line_stripped[1:].strip()
            
            # Проверяем, есть ли этот фильтр в очищенных правилах
            if filter_name in cleaned_filters:
                print(f"Обновляем фильтр '{filter_name}' в {target_file}")
                
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
                    
                    # Добавляем новые очищенные правила
                    for rule in cleaned_filters[filter_name]:
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
                    
                    # Добавляем новые очищенные правила
                    for rule in cleaned_filters[filter_name]:
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
    
    # Записываем обновленный файл
    try:
        with open(target_file, 'w', encoding='utf-8') as f:
            f.writelines(updated_lines)
        print(f"Файл {target_file} успешно обновлен")
    except Exception as e:
        print(f"Ошибка при записи {target_file}: {e}")

def process_files(input_file, output_file):
    """Обрабатывает файлы из списка и сохраняет очищенные правила в output_file."""
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

            cleaned_rules = clean_rules(lines)
            if cleaned_rules:
                out.write(f"! {filter_name.strip()}\n")
                for rule in cleaned_rules:
                    out.write(f"{rule}\n")
                out.write("\n")

def main():
    input_file = "file_list.txt"
    output_file = "cleaned_rules.txt"
    
    # Шаг 1: Создаем файл с очищенными правилами
    print("Шаг 1: Очистка правил из исходных файлов...")
    process_files(input_file, output_file)
    print(f"Очищенные правила сохранены в {output_file}\n")
    
    # Шаг 2: Парсим очищенные правила
    print("Шаг 2: Парсинг очищенных правил...")
    cleaned_filters = parse_cleaned_rules(output_file)
    print(f"Найдено {len(cleaned_filters)} фильтров для обновления\n")
    
    # Шаг 3: Обновляем целевые файлы
    print("Шаг 3: Обновление целевых файлов...")
    target_files = [
        "../ads_list.txt",
        "../ads_list_extended.txt",
        "../ads_list_extended_plus.txt",
        "../evil/ads_list.txt",
        "../evil/ads_list_extended.txt",
        "../evil/ads_list_extended_plus.txt"
    ]
    
    for target_file in target_files:
        update_target_file(target_file, cleaned_filters)
    
    print("\nГотово!")

if __name__ == "__main__":
    main()