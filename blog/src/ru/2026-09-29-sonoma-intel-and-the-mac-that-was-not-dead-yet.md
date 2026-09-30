---
title: Sonoma, Intel и Mac, который ещё рано списывать
description: Agent! для Mac теперь работает на macOS Sonoma 14.6 и новее, на Apple Silicon и Intel. Многие из вас просили версию для систем до macOS 26. Вот она.
tags: Заметки о выпуске, За кулисами
---
Давайте честно. Когда у Agent! стояло «требуется macOS 26», за бортом осталось много хороших Mac.

Сидите на Sonoma — не повезло. На Sequoia — то же самое. А если у вас Mac с Intel, вас даже в разговор не звали.

Меня это всегда задевало. Эти Mac по-прежнему работают. Люди пользуются ими каждый день. Пишут на них код, ведут на них бизнес и держат на них слишком много открытых вкладок. Они ничего плохого не сделали. Просто стоят не на самой новой системе.

Больше нет. **Agent! для Mac теперь работает на macOS Sonoma 14.6 и новее, на Apple Silicon и на Intel.**

Многие из вас ждали версию для систем до macOS 26. Эта — для вас.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img" aria-labelledby="macs-title macs-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="macs-title">Два счастливых Mac и новая табличка</title>
<desc id="macs-desc">Mac с Intel и Mac с Apple Silicon стоят на столе, оба улыбаются. Между ними табличка, на которой «только macOS 26» зачёркнуто и заменено на «macOS 14.6+, Apple Silicon и Intel».</desc>
<rect width="760" height="340" rx="20" fill="#eef6ff"/>
<rect x="182" y="215" width="16" height="50" fill="#8a97a8"/><rect x="150" y="263" width="80" height="12" rx="4" fill="#8a97a8"/>
<rect x="562" y="215" width="16" height="50" fill="#8a97a8"/><rect x="530" y="263" width="80" height="12" rx="4" fill="#8a97a8"/>
<rect x="374" y="170" width="12" height="105" fill="#8b684c"/>
<path d="M30 280H730" stroke="#8b684c" stroke-width="10" stroke-linecap="round"/>
<rect x="90" y="100" width="200" height="125" rx="14" fill="#c9d3df" stroke="#173452" stroke-width="4"/>
<rect x="104" y="114" width="172" height="97" rx="6" fill="#559ef5"/>
<circle cx="160" cy="150" r="9" fill="#fff"/><circle cx="220" cy="150" r="9" fill="#fff"/>
<circle cx="162" cy="151" r="4" fill="#173452"/><circle cx="222" cy="151" r="4" fill="#173452"/>
<path d="M165 178Q190 196 215 178" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<rect x="470" y="100" width="200" height="125" rx="14" fill="#e7e2f7" stroke="#173452" stroke-width="4"/>
<rect x="484" y="114" width="172" height="97" rx="6" fill="#7b6ad6"/>
<circle cx="540" cy="150" r="9" fill="#fff"/><circle cx="600" cy="150" r="9" fill="#fff"/>
<circle cx="542" cy="151" r="4" fill="#173452"/><circle cx="602" cy="151" r="4" fill="#173452"/>
<path d="M545 178Q570 196 595 178" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<rect x="303" y="60" width="154" height="115" rx="10" fill="#fff" stroke="#8b684c" stroke-width="4"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="380" y="88" font-size="15" fill="#8a97a8">только macOS 26</text>
<text x="380" y="118" font-size="19" font-weight="700">macOS 14.6+</text>
<text x="380" y="141" font-size="16">Apple Silicon</text>
<text x="380" y="162" font-size="16">и Intel</text>
<text x="190" y="315" font-size="20">Mac с Intel</text>
<text x="570" y="315" font-size="20">Mac с Apple Silicon</text>
</g>
<path d="M318 83H442" stroke="#d94877" stroke-width="3" stroke-linecap="round"/>
</svg>
<figcaption>Тот же стол. Те же Mac. Новая табличка.</figcaption>
</figure>

## Почему вообще была только 26-я

Agent! использует локальную модель Apple через фреймворк FoundationModels. Это не главный мозг. Всю тяжёлую работу делает выбранный вами провайдер. Но локальная модель помогает с задачами поменьше: делает сводки при сжатии контекста, считает токены и прогревает сессию при запуске приложения.

И вот загвоздка. FoundationModels существует только в macOS 26. Если код хотя бы упоминает один из его типов, под старый Mac он не соберётся. Компилятор просто говорит «нет».

Так что проще всего было потребовать macOS 26 и забыть. Проще для меня, во всяком случае. Для всех остальных — не очень.

И, честно говоря, это было немного глупо. Локальная модель — помощник. Приятный бонус. Agent! работает вовсе не благодаря ей. Отрезать все старые Mac из-за помощника — всё равно что отказаться готовить ужин, потому что кончилась петрушка.

## И как это исправить?

Сначала спросить. Прежде чем трогать локальную модель, Agent! проверяет: я на macOS 26? Если да — отлично, используем. Если нет — этот код просто не запускается, а провайдер продолжает делать настоящую работу.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 300" role="img" aria-labelledby="fork-title fork-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="fork-title">Спроси, прежде чем использовать</title>
<desc id="fork-desc">Блок-схема. Agent! хочет обратиться к локальной модели. Он спрашивает: это macOS 26? «Да» ведёт к использованию локальных помощников. «Нет» — к их пропуску, пока провайдер продолжает работать.</desc>
<defs><marker id="fork-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0L10 5 0 10Z" fill="#4b617e"/></marker></defs>
<rect width="760" height="300" rx="20" fill="#f0f5fb"/>
<g fill="none" stroke="#4b617e" stroke-width="4"><path d="M380 90V113" marker-end="url(#fork-arrow)"/><path d="M320 150H170V206" marker-end="url(#fork-arrow)"/><path d="M440 150H590V206" marker-end="url(#fork-arrow)"/></g>
<rect x="230" y="30" width="300" height="60" rx="18" fill="#d7eaff" stroke="#3377b9" stroke-width="3"/>
<path d="M380 115L440 150 380 185 320 150Z" fill="#fce9b6" stroke="#9a701b" stroke-width="3"/>
<rect x="40" y="210" width="260" height="66" rx="18" fill="#cff3e4" stroke="#29836a" stroke-width="3"/>
<rect x="460" y="210" width="260" height="66" rx="18" fill="#dfd9ff" stroke="#7760b5" stroke-width="3"/>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="380" y="67" font-size="17" font-weight="700">Нужна локальная модель?</text>
<text x="380" y="156" font-size="16" font-weight="700">macOS 26?</text>
<text x="245" y="140" font-size="17">Да</text>
<text x="515" y="140" font-size="17">Нет</text>
<text x="170" y="238" font-size="18" font-weight="700">Используем.</text>
<text x="170" y="262" font-size="15">Сводки, подсчёт токенов</text>
<text x="590" y="238" font-size="18" font-weight="700">Пропускаем.</text>
<text x="590" y="262" font-size="14">Провайдер продолжает работу</text>
</g>
</svg>
<figcaption>Вот и весь фокус. Спроси, прежде чем использовать.</figcaption>
</figure>

Есть ещё один нюанс. Swift не даёт классу хранить свойство, тип которого не существует в запущенной ОС. Поэтому сессия хранится как обычный `AnyObject` и приводится обратно только внутри кода для macOS 26. Некрасиво. Работает отлично.

## Коммиты

Всё случилось 27 сентября 2026 года. Четыре коммита, один день, и всё это есть в Git.

<figure style="margin:2rem 0">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 260" role="img" aria-labelledby="day-title day-desc" style="display:block;width:100%;height:auto;border-radius:20px">
<title id="day-title">27 сентября 2026 года, коммит за коммитом</title>
<desc id="day-desc">Временная шкала с полудня до 20:00. Коммит ea5ce624 в 12:46, 4d7fca86 в 12:57, 3a993205 в 19:14 и 81079e2a в 19:32.</desc>
<rect width="760" height="260" rx="20" fill="#f0f5fb"/>
<g stroke="#4b617e" stroke-width="2"><path d="M121 104V130M136 130V148M639 104V130M663 130V148"/></g>
<path d="M60 130H700" stroke="#4b617e" stroke-width="4" stroke-linecap="round"/>
<g fill="#227657" stroke="#fff" stroke-width="3"><circle cx="121" cy="130" r="8"/><circle cx="136" cy="130" r="8"/><circle cx="639" cy="130" r="8"/><circle cx="663" cy="130" r="8"/></g>
<g font-family="system-ui,sans-serif" text-anchor="middle" fill="#173452">
<text x="121" y="56" font-size="16" font-weight="700">проверки</text><text x="121" y="76" font-size="15">ea5ce624</text><text x="121" y="96" font-size="15">12:46</text>
<text x="136" y="166" font-size="15">12:57</text><text x="136" y="186" font-size="15">4d7fca86</text><text x="136" y="206" font-size="16" font-weight="700">обновить пакеты</text>
<text x="639" y="56" font-size="16" font-weight="700">документация</text><text x="639" y="76" font-size="15">3a993205</text><text x="639" y="96" font-size="15">19:14</text>
<text x="663" y="166" font-size="15">19:32</text><text x="663" y="186" font-size="15">81079e2a</text><text x="663" y="206" font-size="16" font-weight="700">1.1.76</text>
<g font-size="14" fill="#4b617e"><text x="60" y="244">полдень</text><text x="380" y="244">16:00</text><text x="700" y="244">20:00</text></g>
</g>
</svg>
<figcaption>Время коммитов из Git, восточное время США.</figcaption>
</figure>

**[`ea5ce624`](https://github.com/AgentiLoop/Agent/commit/ea5ce62493aef5ca74e694a8ec85b16621ec6388)**: каждое использование FoundationModels спрятано за проверкой на macOS 26. Это сервис модели, посредник Apple Intelligence, прогрев при запуске в `AgentApp`, сводки и подсчёт токенов в `Compression.swift`, а также `AboutSelf`. На старых системах теперь просто выводится «требуется macOS 26 или новее», вместо того чтобы отказываться собираться. Если вы уже на 26, ничего не меняется.

**[`4d7fca86`](https://github.com/AgentiLoop/Agent/commit/4d7fca863a15d91d8e3734f991fabfcb90da734c)**: все десять Swift-пакетов AgentiLoop обновлены до версий с поддержкой macOS 14. AgentAccess, AgentAudit, AgentColorSyntax, AgentD1F, AgentEventBridges, AgentLLM, AgentMCP, AgentSwift, AgentTerminalNeo, AgentTools. Все десять. Это была самая нудная часть. Нельзя просто поменять одну цифру в Xcode и пойти домой. Всё, от чего зависит приложение, должно поехать вместе с ним. В том же коммите выяснилось, что одному вызову подсчёта токенов нужна macOS 26.4, а не 26.0, так что эту проверку ужесточили.

**[`3a993205`](https://github.com/AgentiLoop/Agent/commit/3a9932053630a21ec9df481c8f137cea30ff87a0)**: документация. В README и FAQ теперь написано **Apple Silicon или Intel, macOS 14.6+**. Два слова: «или Intel». Пришлось потрудиться, чтобы их заслужить.

**[`81079e2a`](https://github.com/AgentiLoop/Agent/commit/81079e2a937f62d2d68389a3c124214f80cb3bc3)**: версия 1.1.76, сборка 276, минимальная система 14.6. Выпускаем.

Вот и всё. Никакой магии. Просто проверки `#available`, обновления пакетов и сборка за сборкой, пока компилятор не перестал на меня орать.

## Мелкий шрифт (честный)

На Sonoma или Sequoia вы не получите функции Apple Intelligence, потому что Apple их туда не поставляет. Agent! просто обходится без них. Вы мало что потеряете. Настоящую работу всё равно делал ваш провайдер.

Mac с Intel — это всё ещё Mac с Intel. С облачным провайдером Agent! на нём работает нормально. Большие локальные модели — другая история. В FAQ уже сказано про 64 ГБ+ для локальных моделей на 30B, и это верно для любого Mac, а не только для старых.

И 14.6 — это нижняя планка. Если ваш Mac не тянет Sonoma, тут я бессилен. Я хорош, но не настолько.

## Друзья с Intel, это для вас

Я знаю, многие из вас держатся за Mac с Intel, потому что они всё ещё справляются. Они оплачены. Всё настроено как надо. Вы знаете, где что лежит. Не хочется покупать новую машину только ради того, чтобы попробовать приложение.

Абсолютно справедливо. И не нужно.

То же касается владельцев Apple Silicon, которые пока не готовы прыгать на macOS 26. Может, вы ждёте минорного обновления. Может, нужный инструмент ещё не готов. Может, просто не хочется. Никаких претензий. Сидите на Sonoma сколько угодно.

## Забирайте

**Agent! для Mac. macOS Sonoma 14.6 и новее. Apple Silicon и Intel.**

Если вы ждали — ожидание закончилось. Попробуйте и расскажите, как он работает на вашей машине. Особенно вы, народ с Intel. Очень хочу услышать.

Ваш Mac ещё рано списывать. Оказывается, его просто нужно было пригласить.

Хотите подробный разбор с кодом? Загляните в [инженерный разбор](/blog/agent-now-runs-on-macos-14-6-and-intel/).
