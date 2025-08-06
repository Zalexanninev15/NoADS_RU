import os
import shutil
import re
from collections import OrderedDict

def extract_base_domain(line):
    match = re.search(r'([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', line)
    if not match:
        return None
    
    domain_str = match.group(1).lower().lstrip('-.')
    parts = domain_str.split('.')
    if len(parts) > 2 and parts[-2] in ('co', 'com', 'org', 'net', 'gov', 'edu'):
        return '.'.join(parts[-3:])
    if len(parts) > 1:
        return '.'.join(parts[-2:])
    return domain_str

def process_file_robustly(input_file):
    if not os.path.exists(input_file):
        print(f"Ошибка: Файл {input_file} не найден.")
        return

    backup_file = input_file + '.bak'
    print(f"Создание резервной копии: {backup_file}")
    try:
        shutil.copy2(input_file, backup_file)
    except Exception as e:
        print(f"Не удалось создать резервную копию: {e}")
        return

    with open(backup_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    header_lines = []
    comment_to_rules = OrderedDict()
    domain_to_comment_map = {}
    rule_to_parent_map = {}
    true_orphans = []
    
    is_header = True
    current_comment = None

    for line in lines:
        stripped = line.strip()

        if is_header and stripped and not stripped.startswith('!'):
            is_header = False

        if is_header:
            header_lines.append(line)
            continue
        
        if stripped.startswith('! ') and not stripped.startswith('!!'):
            current_comment = line
            comment_to_rules.setdefault(current_comment, [])
            domain = extract_base_domain(stripped)
            if domain:
                domain_to_comment_map.setdefault(domain, current_comment)
        
        elif stripped and not stripped.startswith('!'):
            parent = None
            if current_comment:
                parent = current_comment
            else:
                domain = extract_base_domain(stripped)
                if domain:
                    parent = domain_to_comment_map.get(domain)
            
            if parent:
                rule_to_parent_map.setdefault(line, parent)
            else:
                true_orphans.append(line)

    for rule, parent in rule_to_parent_map.items():
        if rule not in comment_to_rules[parent]:
            comment_to_rules[parent].append(rule)

    final_lines = []
    final_lines.extend(header_lines)

    for comment, rules in comment_to_rules.items():
        if not rules: continue
        
        final_lines.append(comment)
        final_lines.extend(rules)
        final_lines.append('\n')

    if true_orphans:
        final_lines.append("! Orphaned rules (no parent comment found)\n")
        unique_orphans = list(dict.fromkeys(true_orphans))
        final_lines.extend(unique_orphans)

    try:
        with open(input_file, 'w', encoding='utf-8') as file:
            file.writelines(final_lines)

        print("\n--- Отчет ---")
        print(f"Файл успешно обработан: {input_file}")
        print(f"Исходное количество строк: {len(lines)}")
        print(f"Итоговое количество строк: {len(final_lines)}")
        if true_orphans:
            print(f"Обнаружено 'настоящих сирот' (правил без родителя): {len(unique_orphans)}")
        print(f"Результат сохранен в {input_file}")
        print("-------------\n")

    except Exception as e:
        print(f"Произошла ошибка при записи файла: {e}")
        shutil.copy2(backup_file, input_file)
        print(f"Файл восстановлен из резервной копии {backup_file}.")


def main():
    base_path = '../' 
    files = {
        '1': 'ads_list.txt',
        '2': 'ads_list_extended.txt',
        '3': 'ads_list_extended_plus.txt'
    }
    while True:
        print("Выберите файл для обработки:")
        for key, value in files.items():
            print(f"{key}: {value}")
        print("4: Выход")
        choice = input("Введите номер (1-4): ")

        if choice in files:
            file_to_process = os.path.join(base_path, files[choice])
            process_file_robustly(file_to_process)
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите номер из списка.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter для выхода...")