import os
import re
import requests
from urllib.parse import urlparse



def load_exceptions(exc_file="exceptions_hosts.txt"):
    """Загружает исключения для хостов."""
    exceptions = {"exact": set(), "regex": []}
    if not os.path.exists(exc_file):
        return exceptions
    try:
        with open(exc_file, 'r', encoding='utf-8-sig') as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith('#'):
                    continue
                # regex style: r/.../
                if line.startswith('r/') and line.endswith('/'):
                    try:
                        pattern = re.compile(line[2:-1])
                        exceptions["regex"].append(pattern)
                    except re.error:
                        continue
                else:
                    exceptions["exact"].add(line)
    except Exception:
        return exceptions
    return exceptions

def is_exception(host, exceptions):
    """Проверяет хост на попадание в исключения."""
    if not host or not exceptions:
        return False
    if host in exceptions.get("exact", ()):
        return True
    for pat in exceptions.get("regex", ()):
        if pat.search(host):
            return True
    return False

def download_file(url):
    """Загружает содержимое файла по URL."""
    try:
        response = requests.get(url, timeout=30)
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
        print(f"⚠️  Файл не найден: {file_path}")
        return []
    except Exception as e:
        print(f"Ошибка при чтении {file_path}: {e}")
        return []

def is_valid_domain(domain):
    """Проверяет, является ли строка валидным доменом."""
    if not domain or len(domain) > 253:
        return False
    # Базовая проверка домена
    domain_pattern = re.compile(
        r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)*[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$'
    )
    return bool(domain_pattern.match(domain))

def parse_hosts_line(line):
    """Парсит строку hosts файла и возвращает кортеж (ip, [domains]).
    Формат: IP domain [domain2 domain3 ...]
    """
    line = line.strip()
    
    # Пропускаем комментарии и пустые строки
    if not line or line.startswith('#'):
        return None, []
    
    # Убираем комментарии в конце строки
    if '#' in line:
        line = line.split('#', 1)[0].strip()
    
    # Разбиваем строку на части
    parts = line.split()
    if len(parts) < 2:
        return None, []
    
    # Первая часть — IP адрес
    ip = parts[0]
    
    # Проверяем, что первая часть похожа на IP
    if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}

def extract_hosts(lines, exceptions=None):
    """Извлекает хосты из списка строк и разделяет их по IP.
    Возвращает два множества: blocker_hosts (0.0.0.0, 127.0.0.1) и bypass_hosts (остальные).
    """
    exceptions = exceptions or {"exact": set(), "regex": []}
    blocker_hosts = set()
    bypass_hosts = set()
    
    for line in lines:
        ip, domains = parse_hosts_line(line)
        if ip is None:
            continue
        
        for domain in domains:
            # Проверяем исключения
            if is_exception(domain, exceptions):
                continue
            
            # Распределяем по категориям в зависимости от IP
            if ip in ('0.0.0.0', '127.0.0.1'):
                blocker_hosts.add(domain)
            else:
                bypass_hosts.add(domain)
    
    return sorted(blocker_hosts), sorted(bypass_hosts)

def process_hosts_files(input_file, exceptions=None):
    """Обрабатывает файлы из списка и возвращает два списка хостов: blocker и bypass."""
    exceptions = exceptions or {"exact": set(), "regex": []}
    
    try:
        with open(input_file, 'r', encoding='utf-8-sig') as f:
            file_list = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]
    except FileNotFoundError:
        print(f"Файл {input_file} не найден")
        return set(), set()
    except Exception as e:
        print(f"Ошибка при чтении {input_file}: {e}")
        return set(), set()
    
    all_blocker = set()
    all_bypass = set()
    
    for file_source in file_list:
        file_source = file_source.strip()
        
        print(f"📥 Обработка: {file_source}")
        
        if file_source.startswith(('http://', 'https://')):
            lines = download_file(file_source)
        else:
            lines = read_file(file_source)
        
        blocker_hosts, bypass_hosts = extract_hosts(lines, exceptions=exceptions)
        all_blocker.update(blocker_hosts)
        all_bypass.update(bypass_hosts)
        print(f"   Blocker: {len(blocker_hosts)}, Bypass: {len(bypass_hosts)}")
    
    return all_blocker, all_bypass

def save_hosts_file(output_file, hosts, default_ip):
    """Сохраняет хосты в файл."""
    sorted_hosts = sorted(hosts)
    
    try:
        with open(output_file, 'w', encoding='utf-8') as out:
            # Записываем заголовок
            out.write(f"# Total hosts: {len(sorted_hosts)}\n")
            out.write("#\n\n")
            
            # Записываем хосты
            for host in sorted_hosts:
                out.write(f"{default_ip} {host}\n")
        
        print(f"💾 Сохранено {len(sorted_hosts)} уникальных хостов в {output_file}")
    except Exception as e:
        print(f"Ошибка при записи {output_file}: {e}")

def main():
    print("=" * 60)
    print("HOST FILES GENERATOR")
    print("=" * 60)
    
    exceptions_file = "exceptions_hosts.txt"
    exceptions = load_exceptions(exceptions_file)
    print(f"\n⏳ Шаг 1: Загрузка исключений...")
    print(f"👍 Загружено исключений: {len(exceptions.get('exact', ()))} доменов, {len(exceptions.get('regex', ()))} regex\n")
    
    # Список всех источников
    input_file = "hosts_sources.txt"
    
    print("⏳ Шаг 2: Обработка всех источников...")
    print("-" * 60)
    blocker_hosts, bypass_hosts = process_hosts_files(input_file, exceptions=exceptions)
    
    print("\n" + "=" * 60)
    print("⏳ Шаг 3: Сохранение результатов...")
    print("-" * 60)
    
    # Сохраняем blocker.txt (0.0.0.0)
    save_hosts_file("blocker.txt", blocker_hosts, "0.0.0.0")
    
    # Сохраняем bypass.txt (127.0.0.1)
    save_hosts_file("bypass.txt", bypass_hosts, "127.0.0.1")
    
    print("\n" + "=" * 60)
    print("🥳 Готово!")
    print(f"📊 Статистика:")
    print(f"   Blocker (0.0.0.0): {len(blocker_hosts)} хостов")
    print(f"   Bypass (127.0.0.1): {len(bypass_hosts)} хостов")
    print("=" * 60)

if __name__ == "__main__":
    main()
, ip):
        return None, []
    
    # Остальные части — домены
    domains = []
    for domain in parts[1:]:
        domain = domain.strip().lower()
        if domain and is_valid_domain(domain):
            domains.append(domain)
    
    return ip, domains

def extract_hosts(lines, exceptions=None):
    """Извлекает уникальные хосты из списка строк."""
    exceptions = exceptions or {"exact": set(), "regex": []}
    hosts = set()
    
    for line in lines:
        domains = parse_hosts_line(line)
        for domain in domains:
            # Проверяем исключения
            if is_exception(domain, exceptions):
                continue
            hosts.add(domain)
    
    return sorted(hosts)

def process_hosts_files(input_file, output_file, default_ip="0.0.0.0", exceptions=None):
    """Обрабатывает файлы из списка и сохраняет хосты в output_file."""
    exceptions = exceptions or {"exact": set(), "regex": []}
    
    try:
        with open(input_file, 'r', encoding='utf-8-sig') as f:
            file_list = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]
    except FileNotFoundError:
        print(f"Файл {input_file} не найден")
        return
    except Exception as e:
        print(f"Ошибка при чтении {input_file}: {e}")
        return
    
    all_hosts = set()
    
    for file_source in file_list:
        file_source = file_source.strip()
        
        print(f"📥 Обработка: {file_source}")
        
        if file_source.startswith(('http://', 'https://')):
            lines = download_file(file_source)
        else:
            lines = read_file(file_source)
        
        hosts = extract_hosts(lines, exceptions=exceptions)
        all_hosts.update(hosts)
        print(f"   Найдено хостов: {len(hosts)}")
    
    # Сортируем и записываем результат
    sorted_hosts = sorted(all_hosts)
    
    try:
        with open(output_file, 'w', encoding='utf-8') as out:
            # Записываем заголовок
            out.write(last_modified_line())
            out.write(f"# Total hosts: {len(sorted_hosts)}\n")
            out.write("#\n\n")
            
            # Записываем хосты
            for host in sorted_hosts:
                out.write(f"{default_ip} {host}\n")
        
        print(f"\n💾 Сохранено {len(sorted_hosts)} уникальных хостов в {output_file}")
    except Exception as e:
        print(f"Ошибка при записи {output_file}: {e}")

def main():
    print("=" * 60)
    print("HOST FILES GENERATOR")
    print("=" * 60)
    
    exceptions_file = "exceptions_hosts.txt"
    exceptions = load_exceptions(exceptions_file)
    print(f"\n⏳ Шаг 1: Загрузка исключений...")
    print(f"👍 Загружено исключений: {len(exceptions.get('exact', ()))} доменов, {len(exceptions.get('regex', ()))} regex\n")
    
    # Обработка blocker.txt (0.0.0.0)
    print("⏳ Шаг 2: Генерация blocker.txt...")
    print("-" * 60)
    process_hosts_files("hosts0.txt", "blocker.txt", "0.0.0.0", exceptions=exceptions)
    
    print("\n" + "=" * 60)
    
    # Обработка bypass.txt (с IP из исходных файлов или 127.0.0.1)
    print("⏳ Шаг 3: Генерация bypass.txt...")
    print("-" * 60)
    process_hosts_files("hosts_ip.txt", "bypass.txt", "127.0.0.1", exceptions=exceptions)
    
    print("\n" + "=" * 60)
    print("🥳 Готово!")
    print("=" * 60)

if __name__ == "__main__":
    main()