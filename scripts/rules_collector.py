import os
import requests
from urllib.parse import urlparse

def download_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.RequestException as e:
        print(f"Ошибка при загрузке {url}: {e}")
        return []

def read_file(file_path):
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
    line = line.strip()
    if not line:
        return True
    return (line.startswith('!') or 
            line.startswith('!!') or 
            (line.startswith('#') and not line.startswith('##') and not line.startswith('#?')))

def clean_rule(line):
    line = line.encode('utf-8').decode('utf-8-sig').lstrip().rstrip()
    if not line:
        return None
    if line.lower().startswith('[adblock plus 2.0]'):
        return None
    if is_comment(line):
        return None
    if '  # ' in line:
        return line.split('  # ', 1)[0].rstrip()
    return line

def clean_rules(lines):
    return [rule for line in lines if (rule := clean_rule(line))]

def process_files(input_file, output_file):
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
    process_files(input_file, output_file)
    print(f"Очищенные правила сохранены в {output_file}")

if __name__ == "__main__":
    main()