from itertools import groupby
import re

regex = r" https:\/\/[a-z]\w+(.+)$"
with open('ads_list.txt', 'r') as file:
    content = file.read()
matches = re.finditer(regex, content, re.MULTILINE)
links = []
for matchNum, match in enumerate(matches, start=1):
    match = match.group()
    lk = f"\n- [{match.replace(' ', '')}]({match.replace(' ', '')})"
    links.append(lk)
links_a = list(set(links))
with open('SITES.md', 'w', encoding="utf8") as file: 
    file.write("\n# Сайты, которые имеются в списке NoADS_RU:\n\n") 
    for line in links_a: 
        file.write(line)
    file.write('\n- И другие сайты (при использовании [расширенного варианта](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list_extended.txt) списка)')
print('Список пополнился новыми сайтами!')