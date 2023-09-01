import requests
import json
import re
import os

print('NoADS_RU Updater v3.1')
print('Что я умею?')
print('- Запись фильтров из файла uBlock Origin в ads_list.txt и ads_list_extended.txt')
print('- Удаление дублей фильтров')
print('- Формирование файла SITES.md')
print('- Обновление фильтров от Faust для ads_list_extended.txt\n')

txt_files = [file for file in os.listdir() if file.endswith(".txt")]
ads_list_file = "ads_list.txt"

for file in txt_files:
    if file.startswith('my-ublock-static-filters_'):
        ads_list_file = file
        if os.path.exists('ads_list.txt'):
            os.remove('ads_list.txt')
        os.rename(ads_list_file, 'ads_list.txt')
        ads_list_file = 'ads_list.txt'
        break
    
print('[!] Файл списка обновлён! (1/4)')

extended_list_url = 'https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list_extended.txt'
response = requests.get(extended_list_url)
extended_list = response.text

with open(ads_list_file, 'r') as file:
    ads_list = file.read()
    
extended_list = extended_list.replace(extended_list.split('! [List from Faust (https://gist.github.com/dymitr-ua): https://gist.github.com/dymitr-ua/ab19ebfa6b6027daf07a995e420d4613]')[0], ads_list.replace('NoADS_RU (2020-2023)', 'NoADS_RU Extended (2023)'))

with open('ads_list_extended.txt', 'w') as file:
    file.write(extended_list)

print('[!] Файл расширенного варианта списка обновлён! (2/4)')

regex = r"[0-9] https:\/\/[a-z]\w+(.+)$"

with open(ads_list_file, 'r') as file:
    content = file.read()

matches = re.finditer(regex, content, re.MULTILINE)
links = []

for matchNum, match in enumerate(matches, start=1):
    match = match.group()
    lk = f"\n- [{match.replace(' ', '')}]({match.replace(' ', '')})"
    links.append(lk)

links_a = list(set(links))

with open('SITES.md', 'w', encoding="utf8") as file: 
    file.write('\n# Сайты, которые имеются в списке NoADS_RU:\n\n') 
    for line in links_a: 
        file.write(line)
    file.write('\n- И другие сайты (при использовании [расширенного варианта](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list_extended.txt) списка)')

print('[!] Список сайтов с поддержкой фильтров NoADS_RU пополнился новыми сайтами! (3/4)')

url_gists = 'https://api.github.com/users/dymitr-ua/gists'
response = requests.get(url_gists)
data = json.loads(response.text)
url_file = data[0]['files']['brave_adblock_additions.txt']['raw_url']

response = requests.get(url_file)

with open('ads_list_extended.txt', 'r') as file:
    lines = file.readlines()

for i in range(len(lines)):
    if lines[i].strip().startswith('! [List from Faust'):
        j = i
        while j < len(lines) and lines[j].strip() != '':
            j += 1
        lines[i + 1:j] = [line + "\n" for line in response.text.splitlines()]
        break

with open('ads_list_extended.txt', 'w') as file:
    file.writelines(lines)

print('[!] Обновлены фильтры от Faust для файла расширенного варианта списка! (4/4)')

print('[!] Работа скрипта завершена успешно!')
