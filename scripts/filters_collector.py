import os
import re
from datetime import datetime
from urllib.parse import urlparse

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
    return f"! Last modified: {today.day} {months[today.month-1]} {today.year} года\n"


def count_rules(lines):
    return sum(
        1
        for ln in lines
        if ln.strip() and not ln.strip().startswith("!") and not ln.startswith(" ")
    )


def load_exceptions(exc_file="filters_exceptions.dat"):
    exceptions = {"exact": set(), "regex": []}
    if not os.path.exists(exc_file):
        return exceptions
    try:
        with open(exc_file, "r", encoding="utf-8-sig") as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith("#") or line.startswith("!"):
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
        pass
    return exceptions


def is_exception(rule, exceptions):
    if not rule or not exceptions:
        return False
    if rule in exceptions.get("exact", ()):
        return True
    for pat in exceptions.get("regex", ()):
        if pat.search(rule):
            return True
    return False


def fetch_and_clean_filters(input_file, output_file, exceptions, proxies):
    cleaned_filters = {}
    try:
        with open(input_file, "r", encoding="utf-8-sig") as f:
            file_list = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"❌ Файл {input_file} не найден")
        return cleaned_filters

    for src in file_list:
        if "=" in src:
            url, name = src.split("=", 1)
        else:
            url = src
            name = os.path.basename(urlparse(url).path)

        url = url.strip()
        name = name.strip()
        print(f"⏳ Получаю источник: {name}")

        lines = []
        if url.startswith(("http://", "https://")):
            try:
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                }
                resp = requests.get(url, headers=headers, proxies=proxies, timeout=60)
                resp.raise_for_status()
                lines = resp.text.splitlines()
            except Exception as e:
                print(f"❌ Ошибка скачивания {url}: {e}")
        else:
            if os.path.exists(url):
                try:
                    with open(url, "r", encoding="utf-8-sig") as f:
                        lines = f.read().splitlines()
                except Exception as e:
                    print(f"⚠️ Ошибка чтения {url}: {e}")
            else:
                print(f"⚠️ Источник не найден: {url}")

        rules = []
        for line in lines:
            rule = line.encode("utf-8").decode("utf-8-sig").strip()
            if not rule or rule.lower().startswith("[adblock plus"):
                continue
            if rule.startswith("!") or rule.startswith("!!"):
                continue
            if (
                rule.startswith("#")
                and not rule.startswith("##")
                and not rule.startswith("#?")
            ):
                continue
            if "  # " in rule:
                rule = rule.split("  # ", 1)[0].rstrip()

            if rule and not is_exception(rule, exceptions):
                rules.append(rule)

        if rules:
            cleaned_filters[name] = rules

    try:
        with open(output_file, "w", encoding="utf-8") as out:
            for name, rules in cleaned_filters.items():
                out.write(f"! {name}\n")
                for rule in rules:
                    out.write(f"{rule}\n")
                out.write("\n")
        print(f"✅ Очищенные фильтры сохранены: {output_file}")
    except Exception as e:
        print(f"❌ Ошибка записи {output_file}: {e}")

    return cleaned_filters


def update_target_file(target_file, cleaned_filters, exceptions):
    if not os.path.exists(target_file):
        print(f"⚠️ Пропуск {target_file} (не найден)")
        return

    try:
        with open(target_file, "r", encoding="utf-8-sig") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"❌ Ошибка чтения {target_file}: {e}")
        return

    updated_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]
        s = line.strip()

        if s.startswith("! Last modified:"):
            updated_lines.append(get_last_modified_line())
            i += 1
            continue

        if s.startswith("! Total:"):
            updated_lines.append("! Total: PLACEHOLDER\n")
            i += 1
            continue

        if s.startswith("!") and not s.startswith("!!"):
            name = s[1:].strip()
            if name in cleaned_filters:
                updated_lines.append(line)
                i += 1

                header_buffer = []
                found_empty = False
                for offset in range(3):
                    if i + offset >= len(lines):
                        break
                    hl = lines[i + offset]
                    header_buffer.append(hl)
                    if not hl.strip():
                        found_empty = True
                        break

                if found_empty:
                    updated_lines.extend(header_buffer)
                    i += len(header_buffer)

                for rule in cleaned_filters[name]:
                    updated_lines.append(f"{rule}\n")

                print(f"👍 Категория обновлена: {name}")
                while i < len(lines) and lines[i].strip():
                    i += 1
                continue

        if s and not s.startswith("!") and not s.startswith("!!"):
            if is_exception(s, exceptions):
                i += 1
                continue

        updated_lines.append(line)
        i += 1

    if not any(l.startswith("! Last modified:") for l in updated_lines):
        updated_lines.insert(0, get_last_modified_line())

    compact_lines = []
    prev_empty = False
    for ln in updated_lines:
        if not ln.strip():
            if not prev_empty:
                compact_lines.append(ln)
            prev_empty = True
        else:
            compact_lines.append(ln)
            prev_empty = False

    total = count_rules(compact_lines)
    total_line = f"! Total: {total}\n"

    placeholder_idx = next(
        (idx for idx, ln in enumerate(compact_lines) if "! Total: PLACEHOLDER" in ln),
        None,
    )
    if placeholder_idx is not None:
        compact_lines[placeholder_idx] = total_line
    else:
        insert_pos = min(2, len(compact_lines))
        compact_lines.insert(insert_pos, total_line)

    try:
        with open(target_file, "w", encoding="utf-8") as f:
            f.writelines(compact_lines)
        print(f"🔌 Файл {os.path.basename(target_file)} обновился! ({total})\n")
    except Exception as e:
        print(f"❌ Ошибка записи {target_file}: {e}")


def main():
    exceptions = load_exceptions("filters_exceptions.dat")
    print(
        f"⏳ Загружено исключений: {len(exceptions['exact'])} точных, {len(exceptions['regex'])} regex"
    )

    proxies = None
    if input("🌐 Использовать SOCKS5? (y/n): ").lower() == "y":
        addr = input("⚙️  Адрес (например: 127.0.0.1:3401): ").strip()
        if not addr:
            addr = "127.0.0.1:3401"
        proxies = {"http": f"socks5h://{addr}", "https": f"socks5h://{addr}"}

    print("\n[1/2] Получение и очистка фильтров...")
    cleaned_filters = fetch_and_clean_filters(
        "file_list.txt", "cleaned_filters.txt", exceptions, proxies
    )

    if not cleaned_filters:
        print("⚠️ Нет фильтров для обновления.")
        return

    print("\n[2/2] Обновление списков фильтров")
    target_files = [
        "ads_list.txt",
        "ads_list_extended.txt",
        "ads_list_extended_plus.txt",
        "ads_list_rws.txt",
    ]

    for target_file in target_files:
        update_target_file(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)), f"../{target_file}"
            ),
            cleaned_filters,
            exceptions,
        )

    if os.path.exists("cleaned_filters.txt"):
        os.remove("cleaned_filters.txt")
    print("🥳 Готово!")


if __name__ == "__main__":
    main()
