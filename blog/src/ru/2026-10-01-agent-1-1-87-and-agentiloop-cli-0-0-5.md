---
title: Выходит вся семья: Agent! 1.1.87 и AgentiLoop CLI 0.0.5
description: Agent! для Mac получает Auto-Pilot, шесть новых провайдеров, более строгого критика и поддержку macOS 14.6. CLI на Rust и Go получают расширенный набор инструментов: поиск, загрузку веб-страниц, списки задач, AGENTS.md, /undo, пользовательские команды и --json.
tags: Анонс, Релиз, Кроссплатформенность
---
<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" role="img" aria-labelledby="fam-title fam-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="fam-title">Семья AgentiLoop: одно приложение для Mac и два терминала</title>
<desc id="fam-desc">В центре стоит большое окно Mac с подписью Agent! 1.1.87. Слева от него окно терминала показывает маленького краба и подпись Rust 0.0.5; справа окно терминала показывает маленького гофера и подпись Go 0.0.5. Пунктирные линии соединяют все три окна с общим символом цикла наверху.</desc>
<rect width="760" height="380" rx="20" fill="#0f1724"/>
<g fill="#6fb6ff" opacity=".35"><circle cx="60" cy="50" r="2"/><circle cx="700" cy="70" r="2"/><circle cx="640" cy="330" r="2"/><circle cx="110" cy="320" r="2"/><circle cx="380" cy="350" r="2"/><circle cx="520" cy="40" r="2"/><circle cx="230" cy="36" r="2"/></g>
<g fill="none" stroke="#6fb6ff" stroke-width="3" stroke-dasharray="4 8" stroke-linecap="round"><path d="M380 80V112"/><path d="M350 62Q170 70 140 150"/><path d="M410 62Q590 70 620 150"/></g>
<g fill="none" stroke="#9fd2ff" stroke-width="5" stroke-linecap="round"><path d="M380 55C392 39 412 39 412 55C412 71 392 71 380 55C368 39 348 39 348 55C348 71 368 71 380 55Z"/></g>
<rect x="250" y="112" width="260" height="190" rx="16" fill="#1d2a3d" stroke="#6fb6ff" stroke-width="3"/>
<rect x="250" y="112" width="260" height="34" rx="16" fill="#26364d"/><rect x="250" y="130" width="260" height="16" fill="#26364d"/>
<circle cx="272" cy="129" r="6" fill="#ff5f57"/><circle cx="292" cy="129" r="6" fill="#febc2e"/><circle cx="312" cy="129" r="6" fill="#28c840"/>
<rect x="340" y="164" width="80" height="80" rx="20" fill="#2f7bf5"/>
<g fill="#fff"><circle cx="358" cy="186" r="5"/><circle cx="402" cy="186" r="5"/><circle cx="380" cy="204" r="5"/><circle cx="360" cy="226" r="5"/><circle cx="400" cy="226" r="5"/></g>
<g fill="none" stroke="#fff" stroke-width="2" opacity=".8"><path d="M358 186L380 204L402 186M380 204L360 226M380 204L400 226M360 226H400M358 186H402M358 186L360 226M402 186L400 226"/></g>
<text x="380" y="280" text-anchor="middle" font-family="system-ui,sans-serif" font-size="22" font-weight="700" fill="#e8f2ff">Agent! 1.1.87</text>
<rect x="40" y="150" width="190" height="150" rx="12" fill="#121c2a" stroke="#f08a4b" stroke-width="3"/>
<text x="56" y="178" font-family="ui-monospace,monospace" font-size="15" fill="#f08a4b">$ agentiloop</text>
<g fill="#f08a4b" stroke="#0f1724" stroke-width="2"><ellipse cx="135" cy="236" rx="34" ry="22"/><circle cx="92" cy="214" r="10"/><circle cx="178" cy="214" r="10"/></g>
<g stroke="#f08a4b" stroke-width="4" stroke-linecap="round"><path d="M110 256l-10 14M122 258l-6 14M148 258l6 14M160 256l10 14M100 222l8 6M170 222l-8 6"/></g>
<circle cx="124" cy="230" r="4" fill="#0f1724"/><circle cx="146" cy="230" r="4" fill="#0f1724"/>
<text x="135" y="292" text-anchor="middle" font-family="system-ui,sans-serif" font-size="17" font-weight="700" fill="#ffd2b5">Rust 0.0.5</text>
<rect x="530" y="150" width="190" height="150" rx="12" fill="#121c2a" stroke="#4fd1e8" stroke-width="3"/>
<text x="546" y="178" font-family="ui-monospace,monospace" font-size="15" fill="#4fd1e8">$ agentiloop</text>
<g stroke="#0f1724" stroke-width="2"><ellipse cx="625" cy="236" rx="30" ry="36" fill="#4fd1e8"/><circle cx="600" cy="204" r="7" fill="#4fd1e8"/><circle cx="650" cy="204" r="7" fill="#4fd1e8"/></g>
<circle cx="612" cy="222" r="9" fill="#fff"/><circle cx="638" cy="222" r="9" fill="#fff"/><circle cx="612" cy="222" r="4" fill="#0f1724"/><circle cx="638" cy="222" r="4" fill="#0f1724"/>
<text x="625" y="292" text-anchor="middle" font-family="system-ui,sans-serif" font-size="17" font-weight="700" fill="#c8f4fb">Go 0.0.5</text>
<text x="380" y="345" text-anchor="middle" font-family="system-ui,sans-serif" font-size="18" fill="#9fb6d4">Один цикл. Три способа его запустить.</text>
</svg>
<figcaption>Семья AgentiLoop 1 октября: Agent! для Mac, а также редакции для командной строки на Rust и Go.</figcaption>
</figure>

Сегодня вся семья выходит одновременно. **Agent! 1.1.87** — новый релиз приложения для Mac, а **AgentiLoop CLI 0.0.5** вышел сразу для [Rust](https://github.com/AgentiLoop/AgentiLoopCLI/releases/tag/v0.0.5) и [Go](https://github.com/AgentiLoop/AgentiLoopGo/releases/tag/v0.0.5). Это полноценный релиз, а не предварительная версия, и для всех троих это самый большой шаг на сегодняшний день.

Вот что нового — прямо из истории git.

## Agent! 1.1.87 для Mac

Последним полноценным релизом приложения для Mac была версия 1.1.33 от 12 сентября. С тех пор многое произошло: в 1.1.87 вошли 449 коммитов. Вот главное.

### 🤖 Auto-Pilot: `/auto <goal>`

Главная функция. Дайте Agent! цель, и `/auto` будет выполнять её серией автономных циклов в рамках бюджета времени. Каждый цикл продвигается к цели, проверяет, где он находится, и продолжает работу.

- Никаких ограничений на число циклов или итераций. Работает во вкладках LLM и хранит историю целей, так что `/auto last` и `/auto #N` возвращают одну из прошлых целей.
- Сессии переживают перезапуск приложения и продолжаются в той же вкладке.
- **Esc** останавливает только текущий цикл. **Stop All** (или `/auto stop all`) завершает сессию.

Это агентный цикл, в котором человек намеренно делает шаг назад: вы задаёте пункт назначения и бюджет, а Agent! ведёт.

### 🔌 Шесть новых провайдеров и меньше настроек, с которыми надо возиться

Новое в 1.1.87: **Sidrune AI** (с вариантами протокола OpenAI и Anthropic), **Muse Code** (использует вашу подписку `muse login`), **Requesty**, **A2Agent**, **OrcaRouter** и **Qwen Code** в рамках Coding Plan. Есть также экспериментальный провайдер **fm serve**, который открывает доступ к Apple Foundation Models через локальный API Chat Completions.

Поддержка зрения теперь определяется по метаданным каталога каждого провайдера, поэтому переключатель Force Vision больше не нужен. Под капотом все провайдеры теперь живут в одном реестре, `APIProvider`, вместо дюжины отдельных путей в коде.

### 🧐 Критик, которого не переубедить

В Agent! есть «шлюз критика»: вторая модель проверяет изменение, прежде чем задача будет признана выполненной. В 1.1.87 проверка стала **обязательной**. Неизменённый diff отклоняется, изменённый diff проверяется заново, а замечания нельзя отмести как «выходящие за рамки задачи». Критик теперь также работает с Codex и Apple Intelligence, а в журнале видно, какие проблемы он нашёл и изменился ли после этого код.

Рядом с ним работает **Jev** — слой принятия решений TypeSafe System One, который даёт советы циклу инструментов. Его настройки находятся в новом разделе LLM Common Settings.

### 🧠 Более умный контекст

Сжатие контекста было тщательно переработано. Пороги теперь рассчитываются по модели, которая *действительно используется* (модель вкладки или резервная), а полученные размеры контекстного окна Ollama запоминаются. Это исправляет ошибку, из-за которой некоторые модели сжимались уже на 16K. Сохраняемый хвост и microcompact ограничены числом токенов, а не количеством сообщений, слишком большие блоки урезаются в первую очередь, а ошибки переполнения контекста и `max_tokens` распознаются одинаково у всех провайдеров.

### 🖥️ Больше Mac, больше языков

- **macOS 14.6 Sonoma и новее**, на Apple Silicon и Intel. Для функций Apple Intelligence (Foundation Models) нужна macOS 26.
- Приложение локализовано на испанский, французский, немецкий, китайский (упрощённый), русский, корейский и японский языки.
- Новые действия Accessibility: `wait_until_actionable`, `select_text_range` и `observe_start/poll/stop/list`.
- Установка через Homebrew: `brew update && brew install --cask agentiloop-agent`.

### 🔒 Безопаснее по умолчанию

Рекурсивное удаление текущей папки проекта теперь блокируется. Охота на баги по всему приложению устранила обход режима только для чтения в ShellSafety через `&`, зависание стриминга Ollama и несколько сбоев. `task_complete` отклоняется, если итоговое резюме ссылается на вывод, который так и не был записан, а локальные модели, которым не хватает памяти, сразу останавливаются с понятной причиной, а не крутятся впустую.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 330" role="img" aria-labelledby="box-title box-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="box-title">Расширенный набор инструментов для CLI</title>
<desc id="box-desc">Открытый красный ящик с инструментами и подписью 0.0.5. Из него поднимаются инструменты на подписанных ярлыках: glob и grep с лупой, web_fetch с глобусом, todo_write с чек-листом, /undo с изогнутой стрелкой, AGENTS.md с документом и --json с фигурными скобками.</desc>
<rect width="760" height="330" rx="20" fill="#fff6ea"/>
<path d="M60 296H700" stroke="#c9a77f" stroke-width="10" stroke-linecap="round"/>
<path d="M240 178L270 140H490L520 178Z" fill="#b8323a" stroke="#5a1418" stroke-width="4" stroke-linejoin="round"/>
<rect x="240" y="178" width="280" height="112" rx="10" fill="#d9444d" stroke="#5a1418" stroke-width="4"/>
<path d="M340 140V120Q340 108 352 108H408Q420 108 420 120V140" fill="none" stroke="#5a1418" stroke-width="8"/>
<rect x="340" y="214" width="80" height="40" rx="8" fill="#fff" stroke="#5a1418" stroke-width="3"/>
<text x="380" y="241" text-anchor="middle" font-family="ui-monospace,monospace" font-size="20" font-weight="700" fill="#5a1418">0.0.5</text>
<g font-family="ui-monospace,monospace" font-size="17" font-weight="700" text-anchor="middle">
<g><rect x="60" y="40" width="150" height="44" rx="12" fill="#d7eaff" stroke="#3377b9" stroke-width="3"/><text x="135" y="68" fill="#173452">glob · grep</text><circle cx="232" cy="102" r="16" fill="none" stroke="#3377b9" stroke-width="5"/><path d="M244 114l14 14" stroke="#3377b9" stroke-width="6" stroke-linecap="round"/></g>
<g><rect x="60" y="120" width="140" height="44" rx="12" fill="#d9f5e4" stroke="#2f8f5b" stroke-width="3"/><text x="130" y="148" fill="#14432a">web_fetch</text><circle cx="222" cy="186" r="16" fill="#bfe9cf" stroke="#2f8f5b" stroke-width="3"/><path d="M206 186H238M222 170Q212 186 222 202Q232 186 222 170" fill="none" stroke="#2f8f5b" stroke-width="2.5"/></g>
<g><rect x="295" y="20" width="170" height="44" rx="12" fill="#fce9b6" stroke="#9a701b" stroke-width="3"/><text x="380" y="48" fill="#4a3608">todo_write</text><path d="M362 76l6 6 10-12M362 94l6 6 10-12" fill="none" stroke="#9a701b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><path d="M386 78H404M386 96H404" stroke="#9a701b" stroke-width="4" stroke-linecap="round"/></g>
<g><rect x="560" y="40" width="140" height="44" rx="12" fill="#efe1ff" stroke="#7a4bb8" stroke-width="3"/><text x="630" y="68" fill="#341a5a">/undo</text><path d="M548 128Q520 128 520 104Q520 84 546 84" fill="none" stroke="#7a4bb8" stroke-width="5" stroke-linecap="round"/><path d="M538 74l12 10-12 10" fill="none" stroke="#7a4bb8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></g>
<g><rect x="560" y="120" width="140" height="44" rx="12" fill="#ffe0e6" stroke="#b83a5a" stroke-width="3"/><text x="630" y="148" fill="#5a1426">AGENTS.md</text><path d="M528 172h20l8 8v26h-28z" fill="#fff" stroke="#b83a5a" stroke-width="3" stroke-linejoin="round"/></g>
<g><rect x="560" y="210" width="140" height="44" rx="12" fill="#e2e8f0" stroke="#4b617e" stroke-width="3"/><text x="630" y="238" fill="#173452">--json { }</text></g>
</g>
</svg>
<figcaption>AgentiLoop CLI 0.0.5: тот же цикл, но в ящике гораздо больше.</figcaption>
</figure>

## AgentiLoop CLI 0.0.5: расширенный набор инструментов

Когда мы [перенесли агентный цикл в терминал](/blog/the-terminal-strikes-back/), CLI начинал с пяти точных инструментов: чтение, просмотр папок, запись, редактирование и bash. Версия 0.0.4 научила его корректно останавливаться. Версия 0.0.5 даёт ему больше возможностей для работы. Всё это сначала появилось в Rust и было перенесено в Go коммит за коммитом, так что у обеих редакций абсолютно одинаковые функции.

### Новые инструменты

| Инструмент | Что делает | Спрашивает заранее? |
|---|---|---|
| `glob` | Находит файлы по шаблону | Нет |
| `grep` | Ищет по содержимому файлов, с 0–5 строками контекста | Нет |
| `web_fetch` | Загружает страницу по http(s) в виде текста, с ограничением размера | **Да** |
| `todo_write` | Ведёт чек-лист для многошаговой работы (посмотреть можно через `/todos`) | Нет |

`glob` и `grep` пропускают `.git`, `node_modules`, `target` и бинарные файлы и учитывают `.gitignore`, включая вложенные файлы, отрицание, привязку и правила только для каталогов. Поэтому они быстрее, чем вызов `find` в оболочке, и безопаснее, чем вываливать в контекст целое дерево каталогов.

### Он читает инструкции вашего проекта

Если в вашем репозитории есть **`AGENTS.md`** или **`CLAUDE.md`**, CLI загружает его в системный промпт вместе с файлом из `~/.agentiloop` с вашими личными настройками по умолчанию. Строки вида `@docs/style.md` импортируют другие файлы (с поддержкой вложенности и защитой от циклов). Файла ещё нет? **`/init`** создаст стартовый `AGENTS.md` с найденными командами сборки и тестирования.

### Отмена, diff и не только

- **`/undo`**: каждое изменение, сделанное `write_file`, `edit_file` и `apply_patch`, записывается в журнал для каждого запроса, так что можно откатить последний ход агента.
- **`/diff`** показывает git status и diff рабочего дерева.
- **`/export`** сохраняет разговор в формате Markdown.
- **`/usage`** показывает суммарное число токенов с момента запуска и степень заполнения контекста.

### Настройте под себя

- **Пользовательские слэш-команды**: положите Markdown-файл в `.agentiloop/commands/`, например `review.md` с текстом `Review $1 for bugs`, и `/review main.rs` его выполнит. Поддерживаются `$ARGUMENTS` и `$1`..`$9`, а `/commands` выводит их список.
- **MCP-промпты** с ваших серверов появляются в виде команд `/mcp__<server>__<prompt>`.

### Создан для скриптов и CI

- **`--json`** выводит разовый ответ одним JSON-объектом: result, is_error, session_id, provider, model и usage.
- **`--allow-tool` / `--deny-tool`** задают правила разрешений по имени инструмента или префиксу `mcp_*`. Запрет всегда побеждает, даже `--yes`.
- **`--append-system-prompt`** добавляет текст к системному промпту на один запуск.
- **Конвейеры просто работают**: одиночный `-` в запросе заменяется на stdin, так что `git diff | agentiloop "review this" -` делает ровно то, что написано.

Всё вместе даёт шаг CI, который проверяет pull request, не трогает оболочку и возвращает машиночитаемый вывод:

```
git diff origin/main | agentiloop --deny-tool bash --json "review this diff" -
```

## Зачем выпускать их вместе?

Потому что это одна и та же идея в трёх формах. Agent! для Mac — флагман: он управляет вашими приложениями, сборками Xcode и всем рабочим столом. CLI переносят тот же цикл в любой терминал на macOS, Windows и Linux. Отмена по Esc в CLI и Auto-Pilot в приложении для Mac с кнопкой Stop All отвечают на один и тот же вопрос с двух сторон: *как человеку сохранить контроль над циклом, который работает сам по себе?*

Именно это для нас важнее всего. Не милый аватар и не большая цифра в бенчмарке, а человек в цикле: вы задаёте цель, видите каждый шаг, и можете его остановить. В CLI команда `/undo` ещё и откатывает последние правки файлов, сделанные агентом. У Auto-Pilot отмены нет, поэтому запускайте его в проекте под git.

## Где их взять

- **Agent! 1.1.87 для Mac**: [скачать с GitHub](https://github.com/AgentiLoop/Agent/releases/tag/v1.1.87.287) или `brew update && brew install --cask agentiloop-agent`. macOS 14.6 или новее, Apple Silicon или Intel.
- **AgentiLoop CLI 0.0.5 (Rust)**: [релиз на GitHub](https://github.com/AgentiLoop/AgentiLoopCLI/releases/tag/v0.0.5).
- **AgentiLoopGo 0.0.5 (Go)**: [релиз на GitHub](https://github.com/AgentiLoop/AgentiLoopGo/releases/tag/v0.0.5).

Бинарники CLI для macOS подписаны и нотаризованы. Распакуйте, добавьте `agentiloop` в PATH и запустите — дальше всё сделает мастер настройки.

Тестировщикам мы очень рады. Попробуйте `/undo` после большой правки, натравите его на репозиторий с `AGENTS.md` или встройте `--json` в скрипт, а потом расскажите нам, что сломалось. Пожалуйста, укажите вашу ОС, провайдера и модель и никогда не прикладывайте API-ключи.
