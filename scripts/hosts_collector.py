import os
import re
from datetime import datetime

import requests


def get_last_modified_line():
    months = [
        "января",
        "февраля",
        "марта",
        "апреля",
        "мая",
        "июня",
        "июля",
        "августа",
        "сентября",
        "октября",
        "ноября",
        "декабря",
    ]
    today = datetime.today()
    return f"# Last modified: {today.day} {months[today.month-1]} {today.year} года\n"


def load_exceptions(exc_file="exceptions_hosts.dat"):
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
    domain_pattern = re.compile(
        r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)*[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$"
    )
    if domain in ("0.0.0.0", "localhost", "255.255.255.255"):
        return False
    return bool(domain_pattern.match(domain))


def parse_hosts_line(line):
    """Парсит строку hosts файла."""
    line = line.strip()
    if not line or line.startswith("#"):
        return None, []
    if "#" in line:
        line = line.split("#", 1)[0].strip()
    parts = line.split()
    if len(parts) < 2:
        return None, []
    ip = parts[0]
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        return None, []
    domains = []
    for domain in parts[1:]:
        domain = domain.strip().lower()
        if domain and is_valid_domain(domain):
            domains.append(domain)
    return ip, domains


def process_hosts_from_list(file_list, exceptions=None, proxies=None):
    """Обрабатывает список источников."""
    exceptions = exceptions or {"exact": set(), "regex": []}
    all_blocker = set()
    all_bypass = {}

    for file_source in file_list:
        file_source = file_source.strip()
        print(f"⏳ Источник: {file_source}")
        blocker_hosts = set()
        bypass_hosts = {}

        if file_source.startswith(("http://", "https://")):
            try:
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
                }
                response = requests.get(
                    file_source, headers=headers, proxies=proxies, timeout=60
                )
                response.raise_for_status()
                content = response.text.splitlines()
                for line in content:
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
            except Exception as e:
                print(f"❌ Ошибка скачивания {file_source}: {e}")
        else:
            try:
                if os.path.exists(file_source):
                    with open(file_source, "r", encoding="utf-8-sig") as f:
                        for line in f:
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
                else:
                    print(f"⚠️ Файл не найден: {file_source}")
            except Exception as e:
                print(f"⚠️ Ошибка чтения {file_source}: {e}")

        print(
            f"👍 Найдено: {len(blocker_hosts)} блокировок, {len(bypass_hosts)} обходов"
        )
        all_blocker.update(blocker_hosts)
        all_bypass.update(bypass_hosts)

    return all_blocker, all_bypass


def save_hosts_file(output_path, hosts, default_ip=None):
    """Сохраняет хосты в файл, создавая папки при необходимости."""
    try:
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as out:
            out.write(f"# Total hosts: {len(hosts)}\n")
            out.write(get_last_modified_line())
            if default_ip is not None:
                for host in sorted(hosts):
                    out.write(f"{default_ip} {host}\n")
            else:
                for host in sorted(hosts.keys()):
                    out.write(f"{hosts[host]} {host}\n")

        print(f"✅ Файл сохранен: {os.path.abspath(output_path)} (Всего: {len(hosts)})")
    except Exception as e:
        print(f"❌ Ошибка при записи {output_path}: {e}")


def main():
    exceptions = load_exceptions("exceptions_hosts.txt")
    print(
        f"⏳ Загружено исключений: {len(exceptions['exact'])} доменов, {len(exceptions['regex'])} regex"
    )

    standard_list, two_list, fl_list = [], [], []

    try:
        with open("hosts_sources.txt", "r", encoding="utf-8-sig") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                # Парсинг префиксов
                prefix_match = re.match(r"^\[(\w+)\]\s*(.+)$", line)
                if prefix_match:
                    prefix, source = (
                        prefix_match.group(1),
                        prefix_match.group(2).strip(),
                    )
                    if prefix == "2":
                        two_list.append(source)
                    elif prefix == "FL":
                        fl_list.append(source)
                    else:
                        standard_list.append(source)
                else:
                    standard_list.append(line)
    except FileNotFoundError:
        print("❌ Файл hosts_sources.txt не найден")
        return

    proxies = None
    proxy_file = ".s5proxy"
    use_proxy_auto = True
    if os.path.exists(proxy_file):
        try:
            with open(proxy_file, "r", encoding="utf-8") as pf:
                addr = pf.readline().strip()
                if not addr == "":
                    if addr == "0":
                        use_proxy_auto = False
                    else:
                        print(f"🌐 Прокси выбран автоматически: {addr}")
                        proxies = {"http": f"socks5h://{addr}", "https": f"socks5h://{addr}"}
        except:
            pass

    if not proxies:
        if input("🌐 Использовать SOCKS5? (y/n): ").lower() == "y" or use_proxy_auto:
            addr = input("⚙️  Адрес (например: 127.0.0.1:3401): ")
            if addr == "":
                addr = "127.0.0.1:3401"
            proxies = {"http": f"socks5h://{addr}", "https": f"socks5h://{addr}"}

    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../hosts")

    print("\n[1/2] Обработка стандартных источников...")
    blocker_hosts, bypass_hosts = process_hosts_from_list(
        standard_list, exceptions, proxies
    )
    save_hosts_file(f"{base_dir}/blocker.txt", blocker_hosts, "0.0.0.0")
    save_hosts_file(f"{base_dir}/bypass.txt", bypass_hosts)

    if two_list:
        print("\n[2/2] Обработка источников для ByPass2...")
        _, two_bypass = process_hosts_from_list(two_list, exceptions, proxies)
        bypass2_hosts = bypass_hosts.copy()
        bypass2_hosts.update(two_bypass)
        save_hosts_file(f"{base_dir}/bypass2.txt", bypass2_hosts)

    if fl_list:
        print("\n[3/3] Обработка расширенных источников для BlockerFL...")
        fl_blocker, _ = process_hosts_from_list(fl_list, exceptions, proxies)
        blockerFL_hosts = blocker_hosts.copy()
        blockerFL_hosts.update(fl_blocker)
        save_hosts_file(f"{base_dir}/blockerFL.txt", blockerFL_hosts, "0.0.0.0")

    print("\n" + "=" * 30)
    print("📊 Итоговая статистика:")
    print(f"🔪 Blocker: {len(blocker_hosts)}")
    print(f"🦙 Bypass: {len(bypass_hosts)}")
    if two_list:
        print(f"🦙2️⃣ Bypass2: {len(bypass2_hosts)}")
    if fl_list:
        print(f"🔪FL BlockerFL: {len(blockerFL_hosts)}")
    print("=" * 30)


if __name__ == "__main__":
    main()
