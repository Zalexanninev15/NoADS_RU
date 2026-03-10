# NoADS_RU | [Подключить](https://codeberg.org/Zalexanninev15/NoADS_RU#инструкция-по-настройке-некоторых-расширений-и-браузеров-для-работы-со-списком)

<img src="./assets/Logo.png" width="100" height="100"/>

**Ура! Репозиторию NoADS_RU исполнилось 6 лет 🏆 и [![](https://img.shields.io/github/stars/Zalexanninev15/NoADS_RU)](https://github.com/Zalexanninev15/NoADS_RU/stargazers) на GitHub**

[![](https://img.shields.io/badge/platform-AdBlocking_Extensions-F40D12.svg?logo=adblock)](https://codeberg.com/Zalexanninev15/NoADS_RU)
[![](https://img.shields.io/badge/scripts-Python-%233776AB.svg?logo=python)](https://codeberg.org/Zalexanninev15/NoADS_RU/src/branch/main/scripts)
[![](https://img.shields.io/github/last-commit/Zalexanninev15/NoADS_RU)](https://github.com/Zalexanninev15/NoADS_RU/commits/main)
[![](https://img.shields.io/github/forks/Zalexanninev15/NoADS_RU)](https://github.com/Zalexanninev15/NoADS_RU/network/members)
[![](https://img.shields.io/gitea/stars/Zalexanninev15/NoADS_RU.svg?gitea_url=https%3A%2F%2Fcodeberg.org)](https://codeberg.org/Zalexanninev15/NoADS_RU/stars)
[![](https://img.shields.io/gitea/forks/Zalexanninev15/NoADS_RU.svg?gitea_url=https%3A%2F%2Fcodeberg.org)](https://codeberg.org/Zalexanninev15/NoADS_RU/forks)
[![](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![](https://img.shields.io/badge/Donate-FFDD00.svg?logo=buymeacoffee&logoColor=black)](https://z15.neocities.org/donate)

## Текущие задачи

- 🔨 Разработка генератора обновляемых списков фильтров с использованием add-on'ов под любые запросы пользователей, чтобы предотвратить проблемы, которые происходят при использовании заранее созданных в рамках NoADS_RU списков фильтров. Также это позволит учесть все предпочтения каждого пользователя и заметно уменьшить размер итоговых списков фильтров.
Upd. Начался процесс распределения фильтров на разные списки, чтобы уменьшить размер списков и ускорить процесс обновления.
Upd 10 марта: Первая версия вышла, хотя получилось не совсем то, что я хотел видеть изначально, но относительно близко.
- [ ] Переработка и актуализация информации касаемо NoADS_RU Web Unlimited.
- [ ] Новый логотип для NoADS_RU.
- [ ] Автоматическая генерация списков фильтров и хостов без участия автора раз в 1-2 недели (для поддержания актуальности)
Upd. Временно отложено, т.к. слишком много новых задач "посыплется" на голову автора репозитория.
- [ ] Улучшение README, уменьшение... "подгорания 5 точки в описаниях"

> [!NOTE]
> NoADS_RU в 2026 году переехал на Codeberg ([новый репозиторий](https://codeberg.org/Zalexanninev15/NoADS_RU)), однако, чтобы обеспечить совместимость и удобство, репозиторий на Github останется и будет автоматически обновляться в соответствии с новым репозиторием в формате зеркала. Ссылки на списки фильтров, хостов и другие файлы будут использовать GitHub для обеспечения совместимости, удобства и снижения возможной нагрузки на сервера Codeberg. По-сути для обычного пользователя ничего не меняется, однако, если вы захотите [создать задачу (Issue)](https://codeberg.org/Zalexanninev15/NoADS_RU#обратная-связь), то это нужно делать на Codeberg.

## Описание

Список фильтров для блокировки элементов на русскоязычных, и не только, сайтах. Список составляю вручную, блокируется и то, что не может заблокировать никакое расширение (upd. под конец 2025 года уже не уверен, особенно если прикрутить крутую нейронку). Автор старается охватить как можно большее число сайтов. При большом желании ВЫ (да, 🫵) можете самостоятельно добавить новые элементы для блокировки и попросить добавить их в основной список. [Правила создания задач (Issue)](https://codeberg.org/Zalexanninev15/NoADS_RU#обратная-связь).

> [!NOTE]
> Также проектом **NoADS_RU** развивается список для гарантированной работы 🇷🇺💩 сервисов (**NoADS_RU RWS**), расширенные списки фильтров (**NoADS_RU Extended** и **NoADS_RU Extended Plus**), add-on списки фильтров, списки хостов (**NoADS_RU Hosts**), блокировка рекламы на Android (**NoADS_RU Android Project**) и списки "заражённых" Telegram каналов (**NoADS_RU TGCL**).

Имеется небольшой [генератор ссылок](https://z15.neocities.org/apps/noads_ru) для удобства и возможности быстро сориентироваться.

<details>
    <summary>
        Полный список проектов в рамках NoADS_RU (откройте таблицы кликом по тексту)
    </summary>

#### Фильтры

> Для блокировщиков рекламы в браузере.

| Название | Тип списка фильтров | Описание |
| --- | --- | --- |
| 👍 **[NoADS_RU](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list.txt)** | Full | Основной проект репозитория. |
| ⚡ **[NoADS_RU Extended](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list_extended.txt)** | Full | Расширенный список фильтров на базе NoADS_RU. |
| 💪 **[NoADS_RU Extended Plus](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list_extended_plus.txt)** | Full | Расширенный список фильтров на базе NoADS_RU Extended. |
| 🇷🇺 **[NoADS_RU RWS](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list_rws.txt)** | Full | Список фильтров для 100% работы Я*, MAX, ВКонтакте (и, возможно, других русскоязычных сервисов) на базе NoADS_RU. |
| 📹 **[NoADS_RU YouTube](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/filters/youtube.txt)** | Add-on | Дополнительные фильтры конкретно для YouTube и других видеохостингов. |
| 🤖🖼️❌ **[NoADS_RU AI Slop Killer](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/filters/ai_slop_killer.txt)** | Add-on | Блокировка ИИ и сгенерированного низкокачественного контента. |
| 🌳🐥 **[NoADS_RU WebHosts Lite](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/filters/webhosts_lite.txt)** | Add-on | Фильтры на базе NoADS_RU Hosts Blocker. |
| 🌳 **[NoADS_RU WebHosts](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/filters/webhosts.txt)** | Add-on | Фильтры на базе NoADS_RU Hosts BlockerFL. |
| 👨‍💻 **[NoADS_RU Faust](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/filters/faust.txt)** | Add-on | Фильтры от Faust'а. |

> [!NOTE]
> Отличие Add-on от Full списков фильтров лишь три:
> 1. Add-on списки фильтров содержат фильтры только для конкретных задач, поэтому такие списки намного меньше по размеру и количеству фильтров.
> 2. Add-on списки фильтров необходимо подключать только совместно с подключенными Full-списками фильтров NoADS_RU, чтобы гарантировать большую стабильность и возможности по блокировкам.
> 3. Add-on списки фильтров обновляются реже, чем Full-списки фильтров. Данное отличие актуально на данный момент, но возможно в будущем скрипт будет доработан.

#### Хосты

> Для hosts-файлов/роутеров/расширений/программ.

| Название | Описание |
| --- | --- |
| **[NoADS_RU Hosts Blocker](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/hosts/blocker.txt)** | Блокировка доменов. |
| **[NoADS_RU Hosts BlockerFL](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/hosts/blockerFL.txt)** | Расширенная блокировка доменов. |
| **[NoADS_RU Hosts Bypass](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/hosts/bypass.txt)** | Обход региональных ограничений. |
| **[NoADS_RU Hosts Bypass2](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/hosts/bypass.txt)** | Альтернативный обход региональных ограничений. |

А также:
- Блокировка аналитики, рекламы, сбора данных на вашем смартфоне - **NoADS_RU Android Project**.
- "Ускорение" Интернета в наше смутное время и альтернативы привычным сервисам - **NoADS_RU Web Unlimited**.
- Информация по "гнилым" каналам - **NoADS_RU TGCL**.

> Более подробно про все представленные выше проекты смотрите чуть ниже в разделе **Альтернативные фильтры, прочие списки и сторонние проекты в рамках NoADS_RU**
</details>

**Сделаем сайты чище, а просмотр удобнее и безопаснее!**

👍 Ссылка для подключения основного списка:
```
https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list.txt
```

👉️ [Подробные инструкции по подключению](https://codeberg.org/Zalexanninev15/NoADS_RU#инструкция-по-настройке-некоторых-расширений-и-браузеров-для-работы-со-списком)

> [!TIP]
> [Обратная связь](https://codeberg.org/Zalexanninev15/NoADS_RU#обратная-связь)

> [!IMPORTANT]
> Если какой-то сайт не открывается и явно блокируется при помощи списка: https://github.com/Zalexanninev15/NoADS_RU/pull/24#issuecomment-3262847701 (обычно помогает список **NoADS_RU RWS**)

### Альтернативные фильтры, прочие списки и сторонние проекты в рамках NoADS_RU

#### 🇷🇺 NoADS_RU RWS

Список фильтров на базе стандартного **NoADS_RU**, в котором автор сделал значительные послабления в плане блокировки доменов, аргументов для сайтов, блокировки куки, скриптов отслеживания и сбора метрик (доступен тот же *max.ru*, выполнение скриптов VK API и Yandex API), также в данном списке, как и в **NoADS_RU**, работают панели в Google сервисах (выбор сервисов гугла и смена/управление аккаунтом). В данном списке **планируется** гарантированная работоспособность ру-сервисов (Я*, ВКонтакте, Mail.ru и прочее) для тех категорий людей, которые по своим, или иным причинам (принуждение со стороны), пользуются этим 💩 и хотят чтобы оно ещё и работало без рекламы (про блокировку сбора информации я промолчу, это почти невозможно реализовать без урезания функционала сервисов, т.к. ру-сервисы обожают её собирать даже там, где это совершенно не нужно)

🔗 Ссылка для подключения: 
```
https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list_rws.txt
```

#### ⚡ NoADS_RU Extended

Для сторонников более обширной блокировки вредных элементов рекомендуется использовать **[NoADS_RU Extended](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list_extended.txt)**. Данный список также включает в себя тестовые фильтры и ещё больше улучшает блокировку рекламы, трекеров, скриптов для сбора информации, информации о сборе куки. Из-за этого сервисы *некоторых* компаний (в основном, ру, одной большой Я), которые особенно хорошо собирают данные о пользователях (кто знает, что с ними потом делают) работают очень странно и не так, как вы можете ожидать от них. Автор рекомендует всеми правдами и неправдами избегать данные сервисы и удалять с них аккаунты, а лучше – развернуть в облаке свои self-hosted альтернативы. Я Поиск легко заменяется на 4get с поисковым движком той же компании (что в разы безопаснее и лучше, чем простой поиск через сайт компании напрямую), Я.Диск → Nextcloud/Seafiles/FileBrowser Quantum, VK → Sharkey/Mastodon/Misskey, Telegram → Delta Chat/SimpleX/Session/Matrix и т.д.. Всё можно заменить либо на своё, либо на надёжные сервисы ЗА ПРЕДЕЛАМИ страны! (что-то занесло меня немного, ну, вы поняли 😉)

🔗 Ссылка для подключения: 
```
https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list_extended.txt
```

#### 💪 NoADS_RU Extended Plus

Для хардкорных ценителей __чистого Интернета__ был создан новый список **[NoADS_RU Extended Plus](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list_extended.txt)**, который основан на NoADS_RU Extended (что логично) и включает в себя какое-то немыслимое количество фильтров. Данный список автор рекомендует только, если совсем "достала" реклама или как средство для тотальной блокировки всего что движется или мешает вашему времяпрепровождению в Интернете.

🔗 Ссылка для подключения:
```
https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list_extended_plus.txt
```

#### 📹 NoADS_RU YouTube

> [!NOTE]
> ⚠️ Важно! Это не Full список фильтров, как остальные, которые развиваются в рамках NoADS_RU. Данный список фильтров как-бы "наслаивается" на другие списки. Такой подход позволяет не выбирать какой-то один список фильтров в качестве основы и планируется использовать для всех списков фильтров, чтобы вас было удобнее кастомизировать списки фильтров под свои нужды.

Дополнительный список фильтров для YouTube и других видеохостингов.

🔗 Ссылка для подключения:
```
https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/filters/youtube.txt
```

#### 🤖🖼️❌ NoADS_RU AI Slop Killer

> [!NOTE]
> ⚠️ Важно! Это не Full список фильтров, как остальные, которые развиваются в рамках NoADS_RU. Данный список фильтров как-бы "наслаивается" на другие списки. Такой подход позволяет не выбирать какой-то один список фильтров в качестве основы и планируется использовать для всех списков фильтров, чтобы вас было удобнее кастомизировать списки фильтров под свои нужды.

Если вас уже бесит вездесущий ИИ и низкокачетсвенный контент, который им генерируется (всё чаще и чаще попадается в Интернете), то этот дополнительный список фильтров для вас.

🔗 Ссылка для подключения:
```
https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/filters/ai_slop_killer.txt
```

#### 🌳🐥 NoADS_RU WebHosts Lite

> [!NOTE]
> ⚠️ Важно! Это не Full список фильтров, как остальные, которые развиваются в рамках NoADS_RU. Данный список фильтров как-бы "наслаивается" на другие списки. Такой подход позволяет не выбирать какой-то один список фильтров в качестве основы и планируется использовать для всех списков фильтров, чтобы вас было удобнее кастомизировать списки фильтров под свои нужды.

Список фильтров для браузера на базе **NoADS_RU Hosts Blocker**.

🔗 Ссылка для подключения:
```
https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/filters/webhosts_lite.txt
```

#### 🌳 NoADS_RU WebHosts

> [!NOTE]
> ⚠️ Важно! Это не Full список фильтров, как остальные, которые развиваются в рамках NoADS_RU. Данный список фильтров как-бы "наслаивается" на другие списки. Такой подход позволяет не выбирать какой-то один список фильтров в качестве основы и планируется использовать для всех списков фильтров, чтобы вас было удобнее кастомизировать списки фильтров под свои нужды.

Список фильтров для браузера на базе **NoADS_RU Hosts BlockerFL**.

🔗 Ссылка для подключения:
```
https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/filters/webhosts.txt
```

#### 👨‍💻 NoADS_RU Faust's Lists

> [!NOTE]
> ⚠️ Важно! Это не Full списки фильтров, как остальные, которые развиваются в рамках NoADS_RU. Данный список фильтров как-бы "наслаивается" на другие списки. Такой подход позволяет не выбирать какой-то один список фильтров в качестве основы и планируется использовать для всех списков фильтров, чтобы вас было удобнее кастомизировать списки фильтров под свои нужды.

Списки фильтров от Faust'а. Собраны в одном файле.

🔗 Ссылка для подключения:
```
https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/filters/faust.txt
```

#### 🪄 NoADS_RU Hosts

Для сторонников хостов подготовлен другой тип правил — **[NoADS_RU Hosts](https://github.com/Zalexanninev15/NoADS_RU/tree/main/hosts)**. Включает в себя домены с рекламой, аналитикой, трекерами, сборами информации об ошибках, Android OEM, специфичные для Windows хосты (Microsoft, Adobe) и многие другие, а также сайты, которые по каким-либо причинам недоступны в одной *небольшой* стране с кучей блокировок 🤫.

> [!NOTE]
> Блокировка рекламных доменов, сбора данных о вас, аналитика и многое другое. Bypass - обход ограничений различных сервисов, если вы находитесь в недружественных странах.

> [!TIP]
> [Использование Blocker и BlockerFL на устройствах с OpenWRT](https://github.com/Zalexanninev15/NoADS_RU/discussions/22).

Типы host-файлов: 
- Блокировщик ([Blocker](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/hosts/blocker.txt))
- Расширенный блокировщик ([BlockerFL](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/hosts/blockerFL.txt))
- Анлокер сайтов ([Bypass](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/hosts/bypass.txt)) или [Bypass2](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/hosts/bypass2.txt) (альтернативный).

#### 📱 NoADS_RU Android Project

Блокировка рекламы и сбора данных на Android.

[Перейти в Android Project](https://codeberg.org/Zalexanninev15/NoADS_RU/src/branch/main/android_project.md)

#### 🌐 NoADS_RU Web Unlimited 

Просто кое-что интересное. Обязательно передайте своё СПАСИБО другим людям, которые создали данные проекты.

🩷 Также буду признателен, если воспользуйтесь: философией [r/DeGoogle](https://www.reddit.com/r/degoogle/), Self-hosted и, конечно же, Fediverse 🥳 (передаю 👋 sol4r1s: [Децентрализованная Сеть](https://4pda.to/forum/index.php?showtopic=1021622))

Касаемо self-hosted решений, мои инстанты:
- [Клиент Phanpy](https://apps.cloyder.mooo.com/phanpy) (очень классный веб-клиент для Mastodon)
- [IT-Tools](https://apps.cloyder.mooo.com/tools) ("404" - это норма, после входа используйте инструменты через меню или через клик на логотип)
- [CyberChef](https://apps.cloyder.mooo.com/kit) ("цепочки из инструментов") (как раз обновил до свежей версии)
- [AniX](https://anixart.netlify.app/) (удобно смотрим аниме вне приложения Anixart)

💡 [Моя настройка кастомных поисковиков на примере браузера Vivaldi](https://shitpost.poridge.club/notes/ab27s6de5p) (+ замена Я*)

> [!TIP]
> Если приведенный инстант 4get заблокирован для поиска по Я* — используйте любой другой из [списка](https://4get.ca/instances). В планах у меня идея создать свой инстант (ранее уже создавал, но он был закрыт в связи с заменой VPS).

😊 [Симпатичный тестер блокировщиков рекламы](https://obfusgated.com/tools/ad-block-test)

<details>
    <summary>
        Открыть обходняк (обновлённый материал собирается...)
    </summary>


> [!WARNING]
> ⚠️ **Материал временно убран на время обновления и "от греха подальше"!**
</details>

#### 📟 NoADS_RU TGCL

[Точка входа](https://codeberg.org/Zalexanninev15/NoADS_RU/src/branch/main/tgcl)

Описание:
Списки небезопасных русскоязычных Telegram каналов по категориям, от которых лучше отписаться, либо пустить в RSS (имеются примеры ссылок).

## Особенности списка

* Заблокирована реклама, её упоминания, баннеры и возможность её покупки (*давайте не будем переходить на тёмную сторону*)
* Заблокированы сообщения о подписках, покупках, донатах (только навязывающие)
* Заблокированы кнопки некоторых *Evil-based* социальных сетей и мессенджеров.
* Заблокированы уведомления о куки, т.к. такие есть на очень многих сайтах и крайне раздражают.
* Заблокированы сообщения, типа: "Используйте наше мобильное приложение", "Скачать в Google Play", "Мобильная версия сайта" и многие другие.
* Заблокированы некоторые элементы, которые собирают о вас дополнительную информацию или "помогают" предоставить другие услуги, о которых вы бы никогда не попросили, но вас застявили это использовать.
* Заблокированы ссылки для рекламодателей, компаний и прочих, которые ведут на страницы сайтов, которые позволяют создать больше рекламы и заработать на этом.
* Заблокированы 🍪
* Заблокированы скрипты для отслеживания пользователей и сбора метрик.
* Заблокированы сайты-майнеры и другие сайты от *недоброжелателей*.
* Всё, что заблокировано выше, я также стараюсь блокировать и в мобильных версиях сайтов (происходит крайне редко, т.к. данный список нацелен, в первую очередь, на десктоп-версии сайтов)
* Заблокированы другие элементы с использованием регулярных выражений (частично доступно в обычном варианте списка, но упор всё же сделан в [NoADS_RU Extended](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list_extended.txt) и [NoADS_RU Extended Plus](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list_extended_plus.txt))
* В хостах заблокированы вредоностные и рекламные домены. Список включает в себя домены с рекламой, аналитикой, трекерами, сборами информации об ошибках, Android OEM, специфичные для Windows хосты (Microsoft, Adobe) и многие другие. Некоторые домены также добавлены в фильтры.
* Некоторые другие вещи, которые уже описали в похожих репозиториях: https://github.com/mtxadmin/ublock/blob/master/docs/policy_ru.md

## Совместимость списка

!! **СПИСОКИ ФИЛЬТРОВ НЕЛЬЗЯ ИСПОЛЬЗОВАТЬ НА МАРШРУТИЗАТОРАХ (РОУТЕРАХ) И В HOST(S)-ФАЙЛАХ** !!

> [!NOTE]
> Это связано с тем что список содержит не записи/домены/IP-адреса сайтов, а лишь указывает на элементы на самом сайте, грубо говоря, "косметическая блокировка контента".

🪄 Для этих целей создан список правил [NoADS_RU Hosts](https://codeberg.org/Zalexanninev15/NoADS_RU#noads_ru-hosts).

### Совместимость списка фильтров

Список на 100% совместим с [uBlock Origin](https://github.com/gorhill/uBlock), т.к. это лучшая [лучшая баннерорезка](https://github.com/mtxadmin/ublock/?tab=readme-ov-file#%D0%BA%D0%B0%D0%BA-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%82%D1%8C-%D1%8D%D1%82%D0%BE%D1%82-%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA).

#### Рекомендуемые браузеры на пекарне (PC):

* Mozilla Firefox (и браузеры на его основе, рекомендую использовать его сборки: Floorp или Zen Browser)
* Vivaldi 🦖
* Brave 🦖
* Браузеры, которые имеют встроенный AdBlock с поддержкой пользовательских списков (проверено в Brave, Vivaldi)

> [!IMPORTANT]
> Для Chromium подобных браузеров рекомендуется ставить расширение через файл, а не через Магазин расширений, т.к. это позволит сохранить доступ к расширению в случае его удаления в будущем (что точно произойдёт). Использование uBlock Origin **Lite** автор не одобряет, да и режет рекламу он хуже, но если альтернатив нет - можете использовать.

🦖 – данные браузеры имеют встроенные блокировщики реклам, которые могут лишь частично заменить uBlock Origin, но этого рядовому пользователю будет более чем достаточно.

#### Рекомендуемые браузеры на Android:

На смартфоне используйте расширение в Mozilla Firefox (или в любом другом браузере на базе Firefox). Использование в Chromium-браузерах не рекомендуется в связи с урезанием функционала расширений в будущем, либо можно использовать установку из файла, но как долго проработает расширение гарантий нет. Из Chromium подобных могу порекомендовать лишь Brave 🦖, Vivaldi 🦖. С поддержкой расширений: Lemur Browser и Quetta.

> [!IMPORTANT]
> Для Chromium подобных браузеров рекомендуется ставить расширение uBlock Origin через файл (ищите `chromium` в [релизах](https://github.com/gorhill/uBlock/releases/latest)), а не через Магазин расширений, т.к. это позволит сохранить доступ к расширению в случае его удаления в будущем (что точно произойдёт). Использование uBlock Origin **Lite** автор не одобряет, да и режет рекламу он хуже, но если альтернатив нет - можете использовать.

🦖 – данные браузеры имеют встроенные блокировщики реклам, которые могут лишь частично заменить uBlock Origin, но этого рядовому пользователю будет более чем достаточно.

#### Другие AdBlock-подобные расширения для браузера:

Также список протестирован и работает в: AdGuard Антибаннер, Adblock Plus ([имеются некоторые особенности в работе](https://codeberg.org/Zalexanninev15/NoADS_RU#adblock-plus)), AdGuard Content Blocker.

#### К установке также рекомендую расширения

> [!TIP]
> Для дополнительной защиты будет не лишним установить... (особенно, если пользуетесь Firefox, что-то на Vivaldi)

- [Port Authority](https://github.com/ACK-J/Port_Authority)
- [Censor Tracker](https://censortracker.org) (только для выявления сайтов, которые следят за вами)
- [JustDeleteMe](https://justdeleteme.xyz/ru#extension_browser)
- [DuckDuckGo Search & Tracker Protection](https://addons.mozilla.org/ru/firefox/addon/duckduckgo-for-firefox/)
- [LocalCDN](https://www.localcdn.org/)
- [User Agent Switcher and Manager](https://webextension.org/listing/useragent-switcher.html)
- [LibRedirect](https://libredirect.github.io/)
- [FoxyProxy](https://github.com/foxyproxy/browser-extension) (я использую "по работе", но вариантов использования много 🤫). Версия для Chromium-браузеров имеется, а также рекомендую рассмотреть иные расширения с похожим функционалом: [Proxy SwitchyOmega 3 (ZeroOmega)](https://chromewebstore.google.com/detail/proxy-switchyomega-3-zero/pfnededegaaopdmhkdmcofjmoldfiped) и [ProxyControl](https://chromewebstore.google.com/detail/proxycontrol/hjocpjdeacglfchomobaagbmipeggnjg)
- [ClearURLs](https://github.com/ClearURLs/Addon)

> [!WARNING]
> - Расширение **LocalCDN** может поломать отображение изображений на некоторых сайтах, такие сайты нужно добавить в исключения.
> - Включение "Фильтра" в расширении **ClearURLs** может сломать работу некоторых функций на сайтов. В частности, перестаёт работать "AI Mode" в поиске Google.

## Инструкция по настройке некоторых расширений и браузеров для работы со списком

*Возможно придётся немного подождать прогрузки GIF*

> [!NOTE]
> ℹ️ В приведённых ниже гайдах демонстрируется подключение обычного списка **NoADS_RU**, если же вам нужен **NoADS_RU Extended** / **NoADS_RU Extended Plus** / **NoADS_RU RWS** — используйте [актуальные ссылки из раздела](https://codeberg.org/Zalexanninev15/NoADS_RU#альтернативные-фильтры-прочие-списки-и-сторонние-проекты-в-рамках-noads_ru). Также по данной сети э ссылке доступны другие проекты в рамках NoADS_RU (Хосты, Android Project, Web Unlimited, TGCL)

### uBlock Origin

> [!TIP]
> Методы могут быть частично актуальны и для других браузерных расширений.

🦸 Рекомендуется к использованию: **Авторский конфиг для uBlock Origin**

- 👍 Лучшие настройки и отличная оптимизация!
- 👍 Подписка на список **NoADS_RU** активирована!
- 👍 Доступны для активации списки **NoADS_RU Extended**, **NoADS_RU Extended Plus** и **NoADS_RU RWS**!

![image](https://github.com/Zalexanninev15/NoADS_RU/blob/main/assets/All_in_uBlock_Origin.png?raw=true)

Просто скачай, импортируй и пользуйся! Никакой мороки с настройками, без СМС и регистрации.

Лежит здесь → https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/refs/heads/main/my-ublock-origin-settings-backup.json (Сохранить как / Save as)

> [!IMPORTANT]
> Если же вы желаете всё настроить вручную, или у вас уже подключены другие списки, которые не хотелось бы потерять - читайте инструкцию ниже.
> [Принудительное обновление списка с фильтрами](https://github.com/Zalexanninev15/NoADS_RU/discussions/26#discussioncomment-14496899).

#### Подготовка

После установки uBlock Origin проверьте настройки:

1. Выберите вкладку **Списки фильтров**
2. Убедитесь, что поставлены галочки:

* Автообновление списков фильтров
* Приостановить сетевую активность, пока не запустятся все списки фильтров (необходимо для работы списка на некоторых сайтах)
* Парсить и применять косметические фильтры
* Игнорировать общие косметические фильтры

#### Подключение списка

Нажмите [сюда](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list.txt&title=NoADS_RU). Откроется вкладка с возможностью подписаться на список. Смело нажимайте на кнопку "Подписаться".

![image](https://github.com/Zalexanninev15/NoADS_RU/blob/main/assets/Subscribe-in-uBlock-Origin.png?raw=true)

<details>
    <summary>
        К сожалению, этот метод подписки в один клик может не работать. Можно использовать другие методы, они работают всегда и во всех расширениях и браузерах с AdBlock. (Нажмите на эту строку, чтобы развернуть описание)
    </summary>

#### Добавление вручную с автообновлением списка (аналог подписки, если не получилось автоматически)

1. Зайдите в настройки расширения (в данном расширении "Открыть панель управления")
2. Следуйте данной гифке

![](https://github.com/Zalexanninev15/NoADS_RU/blob/main/assets/How-to-subscribe-in-uBlock-Origin.gif)

🔗 Ссылка, которую нужно вставить: 
```
https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list.txt
```

#### Добавление вручную без автообновления списка (метод устарел)

> [!WARNING]
> Данный способ рекомендуется использовать только, если остальные способы не заработали. Обновления списка придётся производить **вручную**, что не очень эффективно и удобно.

1. Перейдите по [ссылке](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list.txt) и нажмите в любое место правой кнопкой мыши
2. Выберите пункт "Сохранить как" и сохраните в нужное вам место
3. Зайдите в настройки расширения (в данном расширении "Открыть панель управления")
4. Следуйте данной гифке, после импорта файл можно удалить

![](https://github.com/Zalexanninev15/NoADS_RU/blob/main/assets/How-to-from-file-in-uBlock-Origin.gif)

</details>

### Adblock Plus

[Старое обсуждение](https://github.com/Zalexanninev15/NoADS_RU/issues/10)

> [!IMPORTANT]
> Необходимо открыть саму [raw-ссылку на список](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list.txt) и с помощью Ctrl+A выделить всё и скопировать в это поле. Далее необходимо нажать Enter и подождать немного (может быть нагрузка на CPU). Потом могут появляться предупреждения из-за большого количества фильтров, не останавливаем работу расширения и пытаемся перейти в другие разделы слева, а потом обновляем страницу с настройками. Теперь браузер должен отвиснуть и все фильтры будут добавлены.

### Браузер уже имеет встроенный AdBlock

**Такими браузерами являются**

[![Vivaldi](https://img.shields.io/badge/Vivaldi-EF3939?style=for-the-badge&logo=Vivaldi&logoColor=white)](https://vivaldi.com/ru) [![Brave](https://img.shields.io/badge/Brave-FB542B?style=for-the-badge&logo=Brave&logoColor=white)](https://brave.com/ru/)

#### Как настроить?

Для всех браузеров необходимо просто вставить ссылку (см. ниже) в "Списки блокировки рекламы"/"Списки фильтров" (или что-то подобное) в настройках браузера.

```
https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list.txt
``` 

<details>
    <summary>
        Гайд для браузера Vivaldi (Нажмите на эту строку, чтобы развернуть описание)
    </summary>

### Подключение списка

1. Перейдите по ссылке (см. ниже) и пролистайте до раздела "БЛОКИРОВКА СЛЕЖКИ И РЕКЛАМЫ"
```
vivaldi://settings/privacy/
``` 
2. Следуйте стрелкам, показанным на скриншоте

![image](https://github.com/Zalexanninev15/NoADS_RU/blob/main/assets/Subscribe-in-Vivaldi.png?raw=true)

3. В текстовое поле всплывающего окна вставьте ссылку
```
https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list.txt
```
4. Согласитесь на добавление списка

</details>

<details>
    <summary>
        Гайд для браузера Brave (Нажмите на эту строку, чтобы развернуть описание)
    </summary>

### Подключение списка

1. Перейдите по одной из ссылок ниже и пролистайте до настройки "Списки фильтров"

```
brave://settings/shields/filters
```
или
```
brave://adblock/
```

2. Вставьте ссылку в поле "Введите URL списка фильтров"
```
https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list.txt
```

3. Нажмите кнопку "Добавить" и обновите страницу настроек

</details>

## Обратная связь

Что-то не работает? Чего-то не хватает? Пожалуйста, напишите об этом [здесь](https://codeberg.org/Zalexanninev15/NoADS_RU/issues/new) или через [другие каналы связи](https://z15.neocities.org/contacts) (email, беседа в Delta Chat).

### Правила создания задач с проблемой

> [!WARNING]
> Несоблюдение правил гарантирует высокую вероятность удаления задачи! (у меня нет времени догадываться, что вы имели в виду указывая на какую-то там ошибку, а также это потребует дополнительных вопросов, что, если быть честным, никому из нас не надо)

1. Перед отправкой задачи убедитесь, что никто ранее не создавал такую же задачу.
2. При написании задачи не используйте матерные выражения (неполный список [матерных слов ru](https://github.com/nickname76/russian-swears) 🤡) в сторону автора и его творений. Проявите уважение к автору списка и его труду! (за который, вообще-то, на протяжении 6 лет никто от вас не требовал ни рубля, или другой валюты) Если что-то не нравится — расспишите минусы, чтобы я смог улучшить свои проекты. Использование мата (на любом языке) или чрезмерное проявление эмоций при написании задачи будет караться удалением этой самой задачи! Только конструктивная критика. Прошу также обратить внимание на [данный пункт](https://codeberg.org/Zalexanninev15/NoADS_RU#альтернативные-фильтры-прочие-списки-и-сторонние-проекты-в-рамках-noads_ru), где подробно расписана информация по проектам NoADS_RU.
3. При написании задачи обязательно точно укажите в каком списке фильтров или в списке хостов произошла проблема! Созданные задачи без указания точного NoADS_RU не будут рассматриваться и будут удалены!
> [!TIP]
> Можно использовать сокращённые названия (если создаёте задачу на Codeberg):
> - `UB` - NoADS_RU
> - `UBE` - NoADS_RU Extended
> - `UBE+` - NoADS_RU Extended Plus
> - `UBRU` - NoADS_RU RWS
> - `HOSTS` - NoADS_RU Hosts Blocker
> - `HOSTSFL` - NoADS_RU Hosts BlockerFL
> - `HOSTSFIX` - NoADS_RU Hosts Bypass
> - `HOSTSFIX2` - NoADS_RU Hosts Bypass2
> - `ANDROID` - NoADS_RU Android Project
> - `WU` - NoADS_RU Web Unlimited
> - `TGCL` - NoADS_RU TGCL
4. При написании задачи обязательно точно укажите полную ссылку на проблемный сайт! (если проблема на сайте). Созданные задачи без указания точного URL могут не рассматриваться и, возможно, будут удалены!
5. Перед созданием задачи крайне рекомендуется (но не обязательно) самостоятельно идентифицировать причину поломки (приложите конкретный фильтр или домен, который ломает работу сайта), чтобы автору было проще внедрить исправление.
В этом вам поможет мини-гайд: https://github.com/Zalexanninev15/NoADS_RU/issues/35#issuecomment-3526988530
> [!IMPORTANT]
> Если вы всё ещё не можете идентифицировать проблему самостоятельно - попросите ChatGPT или своего друга. У автора может не быть времени на поиск проблемы, поэтому исправление может занять до 2 недель, даже если ошибка была совсем несложной в исправлении.
6. Если что-то не работает, то также может помочь [принудительное обновление списка с фильтрами](https://github.com/Zalexanninev15/NoADS_RU/discussions/26#discussioncomment-14496899) или выбор более простого варианта списка (НЕ Extended). Если это хосты, то подойдёт более простой [Блокировщик](https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/hosts/blocker.txt).
7. Если какой-то сайт не открывается и явно блокируется при помощи списка: https://github.com/Zalexanninev15/NoADS_RU/pull/24#issuecomment-3262847701
