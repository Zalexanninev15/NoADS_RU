import os
import re
import tempfile

import requests


def load_exceptions(exc_file="exceptions_hosts.txt"):
    """Загружает исключения для хостов."""
    exceptions = {"exact": set(), "regex": []}
    if not os.path.exists(exc_file):
        return exceptions
    try:
        with open(exc_file, "r", encoding="utf-8-sig") as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith("#"):
                    continue
                # regex style: r/.../
                if line.startswith("r/") and line.endswith("/"):
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


def is_valid_domain(domain):
    """Проверяет, является ли строка валидным доменом."""
    if not domain or len(domain) > 253:
        return False
    # Базовая проверка домена
    domain_pattern = re.compile(
        r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)*[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$"
    )
    if domain == "0.0.0.0" or domain == "localhost":
        return False
    return bool(domain_pattern.match(domain))


def parse_hosts_line(line):
    """Парсит строку hosts файла и возвращает кортеж (ip, [domains]).
    Формат: IP domain [domain2 domain3 ...]
    """
    line = line.strip()
    # Пропускаем комментарии и пустые строки
    if not line or line.startswith("#"):
        return None, []
    # Убираем комментарии в конце строки
    if "#" in line:
        line = line.split("#", 1)[0].strip()
    # Разбиваем строку на части
    parts = line.split()
    if len(parts) < 2:
        return None, []
    # Первая часть — IP адрес
    ip = parts[0]
    # Проверяем, что первая часть похожа на IP
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        return None, []
    # Остальные части — домены
    domains = []
    for domain in parts[1:]:
        domain = domain.strip().lower()
        if domain and is_valid_domain(domain):
            domains.append(domain)
    return ip, domains


def process_hosts_from_list(file_list, exceptions=None, proxies=None):
    """Обрабатывает список источников и возвращает два списка хостов: blocker и bypass."""
    exceptions = exceptions or {"exact": set(), "regex": []}
    all_blocker = set()
    all_bypass = {}
    for file_source in file_list:
        file_source = file_source.strip()
        print(f"📥 Обработка: {file_source}")
        blocker_hosts = set()
        bypass_hosts = {}
        if file_source.startswith(("http://", "https://")):
            temp_path = tempfile.mktemp()
            success = False
            for attempt in range(3):
                try:
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
                    }
                    response = requests.get(
                        file_source,
                        headers=headers,
                        proxies=proxies,
                        stream=True,
                        timeout=60,
                    )
                    response.raise_for_status()
                    with open(temp_path, "wb") as out_file:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                out_file.write(chunk)
                    with open(temp_path, "r", encoding="utf-8", errors="ignore") as f:
                        for line in f:
                            line = line.rstrip()
                            ip, domains = parse_hosts_line(line)
                            if ip is None:
                                continue
                            for domain in domains:
                                if is_exception(domain, exceptions):
                                    continue
                                if ip in ("0.0.0.0", "127.0.0.1", "0.0.0.1"):
                                    blocker_hosts.add(domain)
                                else:
                                    bypass_hosts[domain] = ip
                    success = True
                    break
                except requests.exceptions.Timeout:
                    print(f"⚠️ Попытка {attempt + 1} таймаут для {file_source}")
                except requests.exceptions.RequestException as e:
                    print(f"⚠️ Попытка {attempt + 1} не удалась для {file_source}: {e}")
                    break
            if not success:
                print(f"❌ Ошибка скачивания {file_source} после 3 попыток.")
                blocker_hosts = set()
                bypass_hosts = {}
            if os.path.exists(temp_path):
                os.remove(temp_path)
        else:
            try:
                with open(file_source, "r", encoding="utf-8-sig") as f:
                    for line in f:
                        ip, domains = parse_hosts_line(line.strip())
                        if ip is None:
                            continue
                        for domain in domains:
                            if is_exception(domain, exceptions):
                                continue
                            if ip in ("0.0.0.0", "127.0.0.1", "0.0.0.1"):
                                blocker_hosts.add(domain)
                            else:
                                bypass_hosts[domain] = ip
            except FileNotFoundError:
                print(f"⚠️ Файл не найден: {file_source}")
                continue
            except Exception as e:
                print(f"⚠️ Ошибка при чтении {file_source}: {e}")
                continue
        print(f"🔪 Блокировки: {len(blocker_hosts)}\n🦙 Обходы: {len(bypass_hosts)}")
        all_blocker.update(blocker_hosts)
        all_bypass.update(bypass_hosts)
    return all_blocker, all_bypass


def save_hosts_file(output_file, hosts, default_ip=None):
    """Сохраняет хосты в файл."""
    try:
        with open(output_file, "w", encoding="utf-8") as out:
            # Записываем заголовок
            out.write(f"# Total hosts: {len(hosts)}\n")
            if default_ip is not None:
                sorted_hosts = sorted(hosts)
                for host in sorted_hosts:
                    out.write(f"{default_ip} {host}\n")
            else:
                sorted_hosts = sorted(hosts.keys())
                for host in sorted_hosts:
                    ip = hosts[host]
                    out.write(f"{ip} {host}\n")
        print(f"💾 Сохранено {len(hosts)} уникальных хостов в {output_file}")
    except Exception as e:
        print(f"Ошибка при записи {output_file}: {e}")


def main():
    exceptions_file = "exceptions_hosts.txt"
    exceptions = load_exceptions(exceptions_file)
    print("\n⏳ Шаг 1: Загрузка исключений...")
    print(
        f"👍 Загружено исключений: {len(exceptions.get('exact', ()))} доменов, {len(exceptions.get('regex', ()))} regex\n"
    )
    input_file = "hosts_sources.txt"
    standard_list = []
    two_list = []
    fl_list = []
    try:
        with open(input_file, "r", encoding="utf-8-sig") as f:
            for raw_line in f:
                line = raw_line.strip()
                if not line or line.startswith("#"):
                    continue
                prefix_match = re.match(r"^\[(\w+)\]\s*(.+)$", line)
                if prefix_match:
                    prefix = prefix_match.group(1)
                    source = prefix_match.group(2).strip()
                    if prefix == "2":
                        two_list.append(source)
                    elif prefix == "FL":
                        fl_list.append(source)
                    else:
                        standard_list.append(line)
                else:
                    standard_list.append(line)
    except FileNotFoundError:
        print(f"Файл {input_file} не найден")
        return
    except Exception as e:
        print(f"Ошибка при чтении {input_file}: {e}")
        return
    proxies = None
    use_proxy = input("🌐 Использовать прокси SOCKS5? (y/n): ")
    if use_proxy.lower() == "y":
        proxy_address = input(
            "⚙️ Введите адрес прокси-сервера SOCKS5 (например, 127.0.0.1:3401): "
        )
        proxies = {
            "http": f"socks5h://{proxy_address}",
            "https": f"socks5h://{proxy_address}",
        }
        print("🌐5 Использую SOCKS5-прокси!")
    print("⏳ Шаг 2: Обработка стандартных источников...")
    print("-" * 60)
    blocker_hosts, bypass_hosts = process_hosts_from_list(
        standard_list, exceptions=exceptions, proxies=proxies
    )
    print("\n" + "=" * 60)
    print("⏳ Шаг 3: Сохранение стандартных результатов...")
    print("-" * 60)
    # Сохраняем blocker.txt
    save_hosts_file("../hosts/blocker.txt", blocker_hosts, "0.0.0.0")
    # Сохраняем bypass.txt
    save_hosts_file("../hosts/bypass.txt", bypass_hosts)
    # Обработка bypass2.txt
    if two_list:
        print("\n" + "=" * 60)
        print("⏳ Шаг 4: Обработка источников с [2]...")
        print("-" * 60)
        two_blocker, two_bypass = process_hosts_from_list(
            two_list, exceptions=exceptions, proxies=proxies
        )
        bypass2_hosts = bypass_hosts.copy()
        bypass2_hosts.update(two_bypass)
        save_hosts_file("../hosts/bypass2.txt", bypass2_hosts)
    # Обработка blockerFL.txt
    if fl_list:
        print("\n" + "=" * 60)
        print("⏳ Шаг 4: Обработка источников с [FL]...")
        print("-" * 60)
        fl_blocker, fl_bypass = process_hosts_from_list(
            fl_list, exceptions=exceptions, proxies=proxies
        )
        blockerFL_hosts = blocker_hosts.copy()
        blockerFL_hosts.update(fl_blocker)
        save_hosts_file("../hosts/blockerFL.txt", blockerFL_hosts, "0.0.0.0")
    print("\n" + "=" * 60)
    print("🥳 Готово!")
    print("📊 Статистика:")
    print(f"🔪 Blocker: {len(blocker_hosts)} хостов")
    print(f"🦙 Bypass: {len(bypass_hosts)} хостов")
    if two_list:
        print(f"🦙2️⃣ Bypass2: {len(bypass2_hosts)} хостов")
    if fl_list:
        print(f"🔪FL BlockerFL: {len(blockerFL_hosts)} хостов")
    print("=" * 60)


if __name__ == "__main__":
    main()
