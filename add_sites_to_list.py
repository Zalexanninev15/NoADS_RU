import re

regex = r" https:\/\/[a-z]\w+(.+)$"
with open('ads_list.txt', 'r') as file:
    content = file.read()
matches = re.finditer(regex, content, re.MULTILINE)
links = []
for matchNum, match in enumerate(matches, start=1):
    match = match.group()
    link = f"-{match}"
    links.append(link)
    print(link)
with open('SITES.md', 'w', encoding="utf8") as file:
    file.write('\n# Сайты, которые имеются в списке NoADS_RU:\n')
    for i in links:
        file.write(f"\n{i}")
print('Список пополнился новыми сайтами!')
