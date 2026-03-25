#!/bin/bash

# 1. Извлекаем хеши и даты из вашего файла в удобный формат (ХЕШ ДАТА)
# Временный файл будет сохранен в абсолютном пути, чтобы filter-branch его нашел
MAPPING_FILE="/tmp/git_date_mapping.txt"
sed -n 's/.*\[\([0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}\)\] - \([a-f0-9]*\)/\2 \1/p' commits_list.txt > "$MAPPING_FILE"

echo "Подготовлен файл маппинга. Начинаем перезапись истории Git..."

# 2. Запускаем перезапись истории
git filter-branch -f --env-filter '
    # Ищем хеш текущего обрабатываемого коммита в нашем файле
    NEW_DATE=$(grep "^$GIT_COMMIT" /tmp/git_date_mapping.txt | awk "{print \$2}")
    
    if [ -n "$NEW_DATE" ]; then
        # Если дата найдена, меняем дату создания и дату коммита
        # Устанавливаем время по умолчанию на 12:00:00, так как в списке его нет
        export GIT_AUTHOR_DATE="${NEW_DATE}T12:00:00"
        export GIT_COMMITTER_DATE="${NEW_DATE}T12:00:00"
    fi
' -- --all

echo "Готово! Даты изменены."
