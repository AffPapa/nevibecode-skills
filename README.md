# Скиллы для Claude Code, Codex и Cursor по темам

English: [README.en.md](README.en.md)

248 скиллов в 25 темах из каталога [NeVibeCode](https://affpapa.org/nevibecode) на affpapa.org. В каждой теме — самые популярные скиллы, у которых автоматическая проверка безопасности 16.11 не нашла предупреждений. У каждого скилла здесь команда установки, ссылка на карточку с описанием по-русски и ссылка на исходник.

Методика и цифры проверки — [affpapa.org/nevibecode/research](https://affpapa.org/nevibecode/research).

## Отметки

- **ставится ✓ 16.11** — команду из списка запустили в песочнице 16.11: скилл установился, SKILL.md на месте и проходит проверку формата. Проверяли 150 самых популярных скиллов каталога, рабочими по команде оказались 144. Здесь отметка стоит у 89 скиллов; у остальных установку не запускали.
- **A/B 16.11** — скилл участвовал в тесте «ответ со скиллом против ответа без него» (3 модели, 5 тем, слепые судьи). Число — средняя разница оценок по шкале 1–10; шум самого метода 0,70, так что разница меньше этого — не результат.
- Безопасность: в каталоге 16.11 проверены 45 138 единиц и 20 101 исполняемый файл, вредоносного не нашли. Это статический разбор: переписанный под обход вредонос он может не увидеть. Скиллы с предупреждениями (чаще всего `curl | sh` в установке) в список не берём.

## Что показал тест

В среднем скилл в системном промпте измеримого выигрыша не дал: −0,20 балла при шуме 0,70. Сильные модели и без скилла решают такие задачи на 7–9 из 10. Плюс по знаку дали узкие скиллы с нормами — миграции БД, анимация, диагностика багов. Из двух популярных TDD-скиллов один значимо ухудшал ответы, в списке его нет; второй ломал ответ GPT, у него стоит пометка. Скилл стоит до 10 тыс. токенов на каждый запрос, а ответы с ним длиннее на 15–26 %.

Тест ограничен: скилл целиком в системном промпте, один ход, по 6 ответов на скилл. Процессным скиллам такой формат невыгоден.

## Темы

- [Настройка агента: память, контекст, субагенты](#topic-agent-tooling) — 10
- [Фронтенд и UI](#topic-frontend) — 10
- [Бэкенд и API](#topic-backend) — 10
- [Дизайн](#topic-design) — 10
- [Тесты и QA](#topic-testing) — 10
- [Код-ревью и рефакторинг](#topic-code-review) — 10
- [Безопасность](#topic-security) — 10
- [DevOps и инфраструктура](#topic-devops) — 10
- [Облака: AWS, Azure, GCP](#topic-cloud) — 10
- [Данные и базы](#topic-data) — 10
- [ИИ и ML](#topic-ai-ml) — 10
- [Автоматизация и no-code: n8n, Zapier, Make](#topic-automation) — 10
- [Тексты и документация](#topic-docs) — 10
- [Документы и офис](#topic-office) — 10
- [SEO и GEO](#topic-seo) — 10
- [Маркетинг и контент](#topic-marketing) — 10
- [Браузер и парсинг](#topic-browser) — 10
- [Мобильная разработка](#topic-mobile) — 10
- [Геймдев и 3D: Unity, Unreal, Godot, Blender](#topic-gamedev) — 10
- [Наука и исследования](#topic-science) — 10
- [Git и GitHub](#topic-git) — 10
- [Заметки, задачи и проекты](#topic-productivity) — 10
- [Финансы и бизнес](#topic-finance) — 10
- [Языки программирования](#topic-languages) — 10
- [Telegram-боты](#topic-telegram) — 8

## Как ставить

Команды рассчитаны на Claude Code (`-a claude-code`) и запускаются из папки проекта; нужен Node.js. Тот же CLI ставит скиллы и другим агентам — список в [vercel-labs/skills](https://github.com/vercel-labs/skills). Можно не запускать руками: на [странице раздела](https://affpapa.org/nevibecode) есть промпт, который ставит скиллы через самого агента.

<a name="topic-agent-tooling"></a>
## Настройка агента: память, контекст, субагенты

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/agent-tooling](https://affpapa.org/nevibecode/topic/agent-tooling)

- **[find-skills](https://affpapa.org/nevibecode/skills/find-skills)** — Скилл find-skills для Claude Code ищет скиллы по задаче и помогает выбрать, что установить. Он включается, когда нужно найти готовую возможность для агента.
  `npx skills add vercel-labs/skills --skill find-skills -a claude-code` · [исходник: vercel-labs/skills](https://github.com/vercel-labs/skills/blob/50894c1d98bc45ca1ab127213e59d6525065b5e7/skills/find-skills/SKILL.md) · 4 400 000 установок · ставится ✓ 16.11
- **[setup-matt-pocock-skills](https://affpapa.org/nevibecode/skills/setup-matt-pocock-skills)** — Скилл setup-matt-pocock-skills настраивает репозиторий для инженерных скиллов Matt Pocock: задаёт трекер задач, метки триажа и расположение доменной документации. Запустите его перед первым использованием остальных скиллов.
  `npx skills add mattpocock/skills --skill setup-matt-pocock-skills -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/setup-matt-pocock-skills/SKILL.md) · 1 052 851 установка · ставится ✓ 16.11
- **[ask-matt](https://affpapa.org/nevibecode/skills/ask-matt)** — Скилл ask-matt для Claude Code, маршрутизирует задачу к нужному скиллу или рабочему потоку из набора Matt Pocock. Направляет от сырой идеи до разбора бага.
  `npx skills add mattpocock/skills --skill ask-matt -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/ask-matt/SKILL.md) · 766 587 установок · ставится ✓ 16.11
- **[to-tickets](https://affpapa.org/nevibecode/skills/to-tickets)** — Скилл to-tickets для Claude Code разбивает план, спецификацию или переписку на небольшие сквозные задачи и помечает блокирующие зависимости. Запускается до публикации задач в трекере.
  `npx skills add mattpocock/skills --skill to-tickets -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/to-tickets/SKILL.md) · 711 230 установок · ставится ✓ 16.11
- **[hyperframes](https://affpapa.org/nevibecode/skills/heygen-com-hyperframes)** — Скилл hyperframes для Claude Code рендерит видео на основе HTML через покадровый обход временной шкалы.
  `npx skills add heygen-com/hyperframes --skill hyperframes -a claude-code` · [исходник: heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/blob/95e4e7f880f5005211412e926b307f4a53f47246/skills/hyperframes/SKILL.md) · 1 600 000 установок · ставится ✓ 16.11
- **[impeccable](https://affpapa.org/nevibecode/skills/impeccable)** — Скилл impeccable для Claude Code, который автоматизирует аудит, проектирование и улучшение интерфейсов. Запускается при задачах на редизайн, рефакторинг UI или создание дизайн-систем.
  `npx skills add pbakaus/impeccable --skill impeccable -a claude-code` · [исходник: pbakaus/impeccable](https://github.com/pbakaus/impeccable/blob/d41d9860b0094dcb68030657da63461212835aaa/cursor-plugin/skills/impeccable/SKILL.md) · 413 300 установок
- **[brainstorming](https://affpapa.org/nevibecode/skills/brainstorming)** — Скилл brainstorming проводит обсуждение с разработчиком перед началом реализации, уточняет требования и формирует дизайн-док. Запускается автоматически, когда запрос содержит неопределённость или предполагает новую функциональность.
  `npx skills add obra/superpowers --skill brainstorming -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/brainstorming/SKILL.md) · 404 045 установок · ставится ✓ 16.11
- **[systematic-debugging](https://affpapa.org/nevibecode/skills/systematic-debugging)** — Скилл systematic-debugging для Claude Code и Codex блокирует фиксы до завершения анализа первопричины. Включается при падении тестов, баге или неожиданном поведении.
  `npx skills add obra/superpowers --skill systematic-debugging -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/systematic-debugging/SKILL.md) · 306 118 установок · ставится ✓ 16.11
- **[writing-plans](https://affpapa.org/nevibecode/skills/writing-plans)** — Скилл writing-plans для Claude Code и Codex создаёт детальный план реализации многошаговой задачи перед первой правкой кода. Запускается, когда у агента есть спецификация фичи или требования.
  `npx skills add obra/superpowers --skill writing-plans -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-plans/SKILL.md) · 282 859 установок · ставится ✓ 16.11
- **[mcp-builder](https://affpapa.org/nevibecode/skills/mcp-builder)** — Скилл mcp-builder для Claude Code пошагово направляет агента при разработке серверов Model Context Protocol на TypeScript или Python. Помогает проектировать схемы инструментов, подключать API и тестировать транспорт.
  `npx skills add anthropics/skills --skill mcp-builder -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/mcp-builder/SKILL.md) · 130 949 установок · ставится ✓ 16.11

<a name="topic-frontend"></a>
## Фронтенд и UI

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/frontend](https://affpapa.org/nevibecode/topic/frontend)

- **[design-taste-frontend](https://affpapa.org/nevibecode/skills/design-taste-frontend)** — Скилл design-taste-frontend для Claude Code задаёт правила оформления и проверки сайтов. Подключается при создании или переделке страницы, а также при просьбе убрать шаблонный вид.
  `npx skills add Leonxlnx/taste-skill --skill design-taste-frontend -a claude-code` · [исходник: leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/blob/f6b76575f949707b4e3c37cd86cb44b0b98643e8/skills/taste-skill/SKILL.md) · 802 600 установок · A/B 16.11: -0,04 — эффекта нет, ~10 тыс. токенов на запрос
- **[prototype](https://affpapa.org/nevibecode/skills/prototype)** — Скилл prototype создаёт временный прототип, чтобы проверить логику, модель состояния или вид интерфейса до работы над основным кодом.
  `npx skills add mattpocock/skills --skill prototype -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/prototype/SKILL.md) · 986 201 установка · ставится ✓ 16.11
- **[webapp-testing](https://affpapa.org/nevibecode/skills/webapp-testing)** — Скилл webapp-testing запускает проверки локальных веб-приложений через Playwright: помогает отлаживать UI, делать скриншоты и смотреть логи браузера.
  `npx skills add anthropics/skills --skill webapp-testing -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/webapp-testing/SKILL.md) · 186 758 установок · ставится ✓ 16.11
- **[ui-ux-pro-max](https://affpapa.org/nevibecode/skills/ui-ux-pro-max)** — Скилл ui-ux-pro-max для Claude Code и Cursor проверяет доступность, гайды и верстку интерфейсов.
  `npx skills add nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max -a claude-code` · [исходник: nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/e59ff376a41f7ca47b7541ad5c116495cbade3ee/.claude/skills/ui-ux-pro-max/SKILL.md) · 455 900 установок · ставится ✓ 16.11
- **[web-artifacts-builder](https://affpapa.org/nevibecode/skills/web-artifacts-builder)** — Скилл web-artifacts-builder для Claude Code и Claude.ai создаёт многокомпонентные HTML-артефакты на React, TypeScript, Tailwind CSS и shadcn/ui.
  `npx skills add anthropics/skills --skill web-artifacts-builder -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/web-artifacts-builder/SKILL.md) · 112 122 установки · ставится ✓ 16.11
- **[remotion-to-hyperframes](https://affpapa.org/nevibecode/skills/remotion-to-hyperframes)** — Скилл remotion-to-hyperframes переносит анимации и видеокод из Remotion, Motion Canvas или Lottie в проект HyperFrames. Позволяет проверить результат покадровым сравнением с оригиналом через diff.
  `npx skills add heygen-com/hyperframes --skill remotion-to-hyperframes -a claude-code` · [исходник: heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/blob/95e4e7f880f5005211412e926b307f4a53f47246/skills/remotion-to-hyperframes/SKILL.md) · 627 200 установок · ставится ✓ 16.11
- **[shadcn](https://affpapa.org/nevibecode/skills/shadcn-ui-shadcn)** — Скилл ведёт агента по работе с shadcn/ui: добавляет компоненты, ищет в реестрах, чинит верстку и собирает дизайн-систему по вашему описанию.
  `npx skills add shadcn-ui/ui --skill shadcn -a claude-code` · [исходник: shadcn-ui/ui](https://github.com/shadcn-ui/ui/blob/e62c9435fff729a175f38983dee73b2cb4f6a069/skills/shadcn/SKILL.md) · 150 100 установок · ставится ✓ 16.11
- **[vercel-composition-patterns](https://affpapa.org/nevibecode/skills/vercel-composition-patterns)** — Скилл vercel-composition-patterns для Claude Code задаёт правила перехода от Boolean props к compound components и общему контексту в React.
  `npx skills add vercel-labs/agent-skills --skill vercel-composition-patterns -a claude-code` · [исходник: vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/composition-patterns/SKILL.md) · 464 000 установок
- **[emil-design-eng](https://affpapa.org/nevibecode/skills/emil-design-eng)** — Скилл emil-design-eng для Claude Code помогает проектировать и проверять детали интерфейса: состояния кнопок, поповеры, подсказки и анимации. Агент подключает его при работе над UI-компонентом, если нет более узкого скилла.
  `npx skills add emilkowalski/skills --skill emil-design-eng -a claude-code` · [исходник: emilkowalski/skills](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills/emil-design-eng/SKILL.md) · 459 000 установок · ставится ✓ 16.11 · A/B 16.11: +0,46 — плюс на анимации и доступности
- **[review-animations](https://affpapa.org/nevibecode/skills/review-animations)** — Скилл review-animations для Claude Code проверяет код анимаций и движения по правилам дизайн-инженерии Emil Kowalski. Запускается по запросу на ревью анимаций и возвращает таблицу проблем с вариантами исправлений.
  `npx skills add emilkowalski/skills --skill review-animations -a claude-code` · [исходник: emilkowalski/skills](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills/review-animations/SKILL.md) · 317 800 установок · ставится ✓ 16.11

<a name="topic-backend"></a>
## Бэкенд и API

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/backend](https://affpapa.org/nevibecode/topic/backend)

- **[lark-im](https://affpapa.org/nevibecode/skills/lark-im)** — Скилл для Claude Code подключает Lark IM: отправляет сообщения, ищет историю, управляет чатами и файлами. Выполняет задачи командных коммуникаций.
  `npx skills add larksuite/cli --skill lark-im -a claude-code` · [исходник: larksuite/cli](https://github.com/larksuite/cli/blob/3d82c85419ad7560ad017db7a3972a596b5fbeb1/skills/lark-im/SKILL.md) · 490 400 установок · ставится ✓ 16.11
- **[api-and-interface-design](https://affpapa.org/nevibecode/skills/api-and-interface-design)** — Скилл api-and-interface-design помогает проектировать API и границы модулей так, чтобы их было проще использовать и менять. Подходит для REST, GraphQL и публичных интерфейсов.
  `npx skills add addyosmani/agent-skills --skill api-and-interface-design -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/api-and-interface-design/SKILL.md) · 77 000 установок
- **[deprecation-and-migration](https://affpapa.org/nevibecode/skills/deprecation-and-migration)** — Скилл deprecation-and-migration для Claude Code помогает выводить из эксплуатации старые системы и переносить пользователей на замену. Он подключается при миграции API, функций или схемы базы данных.
  `npx skills add addyosmani/agent-skills --skill deprecation-and-migration -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/deprecation-and-migration/SKILL.md) · 70 500 установок
- **[observability-and-instrumentation](https://affpapa.org/nevibecode/skills/observability-and-instrumentation)** — Скилл observability-and-instrumentation для Claude Code учит ИИ добавлять в код логи, метрики, трейсинг и корреляционные ID. Включается при добавлении фич в продакшн для наблюдения за поведением системы.
  `npx skills add addyosmani/agent-skills --skill observability-and-instrumentation -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/observability-and-instrumentation/SKILL.md) · 68 100 установок
- **[gws-gmail-watch](https://affpapa.org/nevibecode/skills/gws-gmail-watch)** — Скилл gws-gmail-watch следит за новыми письмами Gmail и отдаёт события потоком NDJSON. Подходит для обработки входящей почты в агентных сценариях.
  `npx skills add googleworkspace/cli --skill gws-gmail-watch -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-gmail-watch/SKILL.md) · 38 700 установок
- **[api-security-testing](https://affpapa.org/nevibecode/skills/usestrix-api-security-testing)** — Скилл api-security-testing помогает проверить REST, GraphQL и gRPC API с помощью Strix: агенты ищут уязвимости и прикладывают запрос для проверки находки.
  `npx skills add usestrix/strix --skill api-security-testing -a claude-code` · [исходник: usestrix/strix](https://github.com/usestrix/strix/blob/fc44d80b3e8f85d91be7a6ba66db85fa84d3840b/skills/api-security-testing/SKILL.md) · 17 500 установок
- **[mcporter](https://affpapa.org/nevibecode/skills/mcporter)** — Скилл mcporter для Claude Code даёт агенту команды для работы с MCP-серверами и инструментами через HTTP или stdio. Настраивает авторизацию и вызов MCP.
  `npx skills add openclaw/openclaw --skill mcporter -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/mcporter/SKILL.md) · 6 300 установок
- **[goplaces](https://affpapa.org/nevibecode/skills/goplaces)** — Скилл для Claude Code запускает goplaces и ищет места через Google Places API, возвращает карточки и отзывы.
  `npx skills add openclaw/openclaw --skill goplaces -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/goplaces/SKILL.md) · 5 400 установок
- **[xurl](https://affpapa.org/nevibecode/skills/xurl)** — Скилл для работы с CLI-утилитой xurl. Позволяет публиковать посты, читать ленту, загружать медиа и отправлять запросы к API X прямо из сессии агента.
  `npx skills add openclaw/openclaw --skill xurl -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/xurl/SKILL.md) · 4 900 установок
- **[wrangler](https://affpapa.org/nevibecode/skills/cloudflare-wrangler)** — Помогает запускать команды Wrangler CLI, настраивать конфигурации и отлаживать деплой Cloudflare Workers в существующих проектах.
  `npx skills add cloudflare/skills --skill wrangler -a claude-code` · [исходник: cloudflare/skills](https://github.com/cloudflare/skills/blob/cbf893b954222276bf1af57e5f23379231e0efb9/skills/wrangler/SKILL.md) · 149 600 установок

<a name="topic-design"></a>
## Дизайн

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/design](https://affpapa.org/nevibecode/topic/design)

- **[frontend-design](https://affpapa.org/nevibecode/skills/frontend-design)** — Скилл frontend-design для Claude Code задаёт осмысленное визуальное направление для новых интерфейсов и редизайна. Помогает уйти от шаблонного UI.
  `npx skills add anthropics/skills --skill frontend-design -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/frontend-design/SKILL.md) · 1 025 790 установок · ставится ✓ 16.11 · A/B 16.11: +0,08 — в пределах шума
- **[codebase-design](https://affpapa.org/nevibecode/skills/codebase-design)** — Скилл codebase-design помогает проектировать модули с небольшим интерфейсом и скрытой внутри сложностью. Подходит для рефакторинга, тестируемости и поиска чистого seam.
  `npx skills add mattpocock/skills --skill codebase-design -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/codebase-design/SKILL.md) · 850 344 установки · ставится ✓ 16.11
- **[hyperframes-cli](https://affpapa.org/nevibecode/skills/heygen-com-hyperframes-cli)** — Скилл hyperframes-cli для Claude Code управляет проектами HyperFrames через CLI: создаёт проект, проверяет кадры и редактирует таймлайн. Агент запускает команды для предпросмотра, рендера и публикации видео.
  `npx skills add heygen-com/hyperframes --skill hyperframes-cli -a claude-code` · [исходник: heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/blob/95e4e7f880f5005211412e926b307f4a53f47246/skills/hyperframes-cli/SKILL.md) · 1 600 000 установок · ставится ✓ 16.11
- **[hyperframes-registry](https://affpapa.org/nevibecode/skills/heygen-com-hyperframes-registry)** — Скилл hyperframes-registry ищет и добавляет редактируемые HyperFrames-блоки для переходов, титров, субтитров, графиков и 3D-сцен. Поиск запускается перед ручной сборкой визуального эффекта.
  `npx skills add heygen-com/hyperframes --skill hyperframes-registry -a claude-code` · [исходник: heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/blob/95e4e7f880f5005211412e926b307f4a53f47246/skills/hyperframes-registry/SKILL.md) · 1 300 000 установок · ставится ✓ 16.11
- **[canvas-design](https://affpapa.org/nevibecode/skills/canvas-design)** — Скилл canvas-design для Claude Code и Claude.ai, который создаёт визуальный арт в .png и .pdf. Включается, когда нужен постер, графический дизайн или статичная работа без готового макета.
  `npx skills add anthropics/skills --skill canvas-design -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/canvas-design/SKILL.md) · 121 543 установки · ставится ✓ 16.11
- **[brand-guidelines](https://affpapa.org/nevibecode/skills/brand-guidelines)** — Скилл brand-guidelines для Claude Code применяет фирменные цвета и шрифты Anthropic к документам, презентациям и другим артефактам.
  `npx skills add anthropics/skills --skill brand-guidelines -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/brand-guidelines/SKILL.md) · 109 043 установки · ставится ✓ 16.11
- **[hallmark](https://affpapa.org/nevibecode/skills/hallmark)** — Скилл hallmark для Claude Code и других агентов: заставляет сгенерированные интерфейсы выглядеть сделанными, а не сгенерированными. Собирает новые страницы и сайты по жёстким правилам вёрстки.
  `npx skills add Nutlope/hallmark --skill hallmark -a claude-code` · [исходник: nutlope/hallmark](https://github.com/Nutlope/hallmark/blob/04977e15f3dfd6ee4b74c887dac3eb52665d6c92/skills/hallmark/SKILL.md) · 115 000 установок · ставится ✓ 16.11
- **[apple-design](https://affpapa.org/nevibecode/skills/apple-design)** — Скилл apple-design переносит принципы физического интерфейса Apple с докладов WWDC в веб на CSS, Pointer Events и Motion. Пригодится при верстке жестов, шторки и прерываемых пружин.
  `npx skills add emilkowalski/skills --skill apple-design -a claude-code` · [исходник: emilkowalski/skills](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills/apple-design/SKILL.md) · 310 000 установок · ставится ✓ 16.11
- **[design](https://affpapa.org/nevibecode/skills/design)** — Скилл design для Claude Code помогает создавать фирменный стиль, логотипы, баннеры, презентации и элементы интерфейса. Запрашивайте дизайн-систему, макет корпоративной айдентики или графику для соцсетей.
  `npx skills add nextlevelbuilder/ui-ux-pro-max-skill --skill design -a claude-code` · [исходник: nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/e59ff376a41f7ca47b7541ad5c116495cbade3ee/cli/assets/skills/design/SKILL.md) · 52 700 установок
- **[brand](https://affpapa.org/nevibecode/skills/brand)** — Скилл brand держит голос бренда, визуальные правила и дизайн-токены в одном файле, а потом раздаёт их промптам агента и вашему CSS.
  `npx skills add nextlevelbuilder/ui-ux-pro-max-skill --skill brand -a claude-code` · [исходник: nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/e59ff376a41f7ca47b7541ad5c116495cbade3ee/cli/assets/skills/brand/SKILL.md) · 51 100 установок

<a name="topic-testing"></a>
## Тесты и QA

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/testing](https://affpapa.org/nevibecode/topic/testing)

- **[tdd](https://affpapa.org/nevibecode/skills/tdd)** — Скилл управляет циклом красный-зелёный в TDD: проверяет, что тесты пишутся до кода, держит их на уровне публичных интерфейсов и не завязывает на внутреннюю структуру.
  `npx skills add mattpocock/skills --skill tdd -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/tdd/SKILL.md) · 1 141 062 установки · ставится ✓ 16.11 · A/B 16.11: -1,33 — у GPT ломал ответ
- **[diagnosing-bugs](https://affpapa.org/nevibecode/skills/diagnosing-bugs)** — Скилл diagnosing-bugs для Claude Code помогает разбирать сложные ошибки и просадки производительности. Он включается по просьбе диагностировать сбой или когда код падает, выдаёт ошибку либо работает медленно.
  `npx skills add mattpocock/skills --skill diagnosing-bugs -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/diagnosing-bugs/SKILL.md) · 834 802 установки · ставится ✓ 16.11 · A/B 16.11: +0,31 — помог Claude
- **[implement](https://affpapa.org/nevibecode/skills/implement)** — Скилл implement выполняет задачу по спецификации или тикетам, ведёт работу через тесты и завершает её ревью с коммитом. Подходит для задач, где нужен дисциплинированный цикл разработки.
  `npx skills add mattpocock/skills --skill implement -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/implement/SKILL.md) · 774 700 установок · ставится ✓ 16.11
- **[verification-before-completion](https://affpapa.org/nevibecode/skills/verification-before-completion)** — Скилл verification-before-completion запрещает объявлять задачу готовой без свежего запуска проверки и разбора вывода. Нужен перед коммитом или PR, когда словам агента нельзя верить на слово.
  `npx skills add obra/superpowers --skill verification-before-completion -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/verification-before-completion/SKILL.md) · 251 313 установок · ставится ✓ 16.11
- **[executing-plans](https://affpapa.org/nevibecode/skills/executing-plans)** — Скилл executing-plans для Claude Code выполняет готовый план задач в текущей сессии без отдельного субагента на каждую задачу. Выполняет план в одном контексте с TDD, журналом решений и ревью ветки.
  `npx skills add obra/superpowers --skill executing-plans -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/executing-plans/SKILL.md) · 242 988 установок · ставится ✓ 16.11
- **[dispatching-parallel-agents](https://affpapa.org/nevibecode/skills/dispatching-parallel-agents)** — Скилл dispatching-parallel-agents распределяет независимые задачи между субагентами, чтобы они разбирали их параллельно. Подходит для разных сбоев в тестах и несвязанных подсистемах.
  `npx skills add obra/superpowers --skill dispatching-parallel-agents -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/dispatching-parallel-agents/SKILL.md) · 218 235 установок · ставится ✓ 16.11
- **[google-agents-cli-eval](https://affpapa.org/nevibecode/skills/google-agents-cli-eval)** — Скилл google-agents-cli-eval оценивает качество ИИ-агентов через agents-cli, находит ошибки и сравнивает прогоны. Включается при отладке датасетов и проверке метрик в проектах на базе Gemini.
  `npx skills add google/agents-cli --skill google-agents-cli-eval -a claude-code` · [исходник: google/agents-cli](https://github.com/google/agents-cli/blob/6eedbdc2f44c388cbfc5f305eb83b9924cfefebb/skills/google-agents-cli-eval/SKILL.md) · 574 900 установок · ставится ✓ 16.11
- **[verify-and-stop](https://affpapa.org/nevibecode/skills/verify-and-stop)** — Скилл verify-and-stop подтверждает выполнение условий сдачи без раздувания правок. Помогает при финальной проверке тикета и точечном прогоне проверок.
  `npx skills add JuliusBrussee/caveman --skill verify-and-stop -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/a192894723a8f47e7f504c7b5041967ff1f18e55/skills/verify-and-stop/SKILL.md) · 129 000 установок · ставится ✓ 16.11
- **[surgical-patch](https://affpapa.org/nevibecode/skills/surgical-patch)** — Скилл surgical-patch удерживает ассистента от лишнего рефакторинга при исправлении ошибок. Модель меняет только ответственный слой кода и пишет точечный тест.
  `npx skills add JuliusBrussee/caveman --skill surgical-patch -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/a192894723a8f47e7f504c7b5041967ff1f18e55/skills/surgical-patch/SKILL.md) · 128 900 установок · ставится ✓ 16.11
- **[debugging-and-error-recovery](https://affpapa.org/nevibecode/skills/debugging-and-error-recovery)** — Скилл debugging-and-error-recovery для Claude Code помогает найти первопричину сбоя и проверить исправление. Он включается при падении тестов, ошибках сборки и неожиданном поведении кода.
  `npx skills add addyosmani/agent-skills --skill debugging-and-error-recovery -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/debugging-and-error-recovery/SKILL.md) · 76 900 установок

<a name="topic-code-review"></a>
## Код-ревью и рефакторинг

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/code-review](https://affpapa.org/nevibecode/topic/code-review)

- **[improve-codebase-architecture](https://affpapa.org/nevibecode/skills/improve-codebase-architecture)** — Скилл improve-codebase-architecture для Claude Code ищет архитектурные узкие места в кодовой базе и показывает варианты углубления модулей в HTML-отчёте. Отчёт содержит материал для ревью перед рефакторингом.
  `npx skills add mattpocock/skills --skill improve-codebase-architecture -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/improve-codebase-architecture/SKILL.md) · 1 163 035 установок · ставится ✓ 16.11
- **[code-review](https://affpapa.org/nevibecode/skills/code-review)** — Скилл code-review проверяет ветку или коммиты по двум осям: соответствие стандартам кода и выполнение требований спеки. Запускает субагентов параллельно.
  `npx skills add mattpocock/skills --skill code-review -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/code-review/SKILL.md) · 789 521 установка · ставится ✓ 16.11 · A/B 16.11: -0,29 — эффекта нет
- **[requesting-code-review](https://affpapa.org/nevibecode/skills/requesting-code-review)** — Скилл requesting-code-review запрашивает ревью у субагента после задачи, крупной функции или перед слиянием в main. Помогает проверить изменения по требованиям, не перегружая основной контекст.
  `npx skills add obra/superpowers --skill requesting-code-review -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/requesting-code-review/SKILL.md) · 262 135 установок · ставится ✓ 16.11
- **[receiving-code-review](https://affpapa.org/nevibecode/skills/receiving-code-review)** — Скилл receiving-code-review помогает разбирать замечания к коду до правок: уточнять неясное, сверяться с кодовой базой и аргументированно возражать. Нужен перед обработкой ревью.
  `npx skills add obra/superpowers --skill receiving-code-review -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/receiving-code-review/SKILL.md) · 221 216 установок · ставится ✓ 16.11
- **[retro](https://affpapa.org/nevibecode/skills/retro)** — Скилл retro проводит ретроспективу сессии кодинга и предлагает правки окружения агента. Нужен после ошибок, долгой навигации по репозиторию или лишних вызовов инструментов.
  `npx skills add mattpocock/skills --skill retro -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/retro/SKILL.md) · 276 027 установок · ставится ✓ 16.11
- **[caveman-review](https://affpapa.org/nevibecode/skills/caveman-review)** — Скилл caveman-review для Claude Code и других агентов: пишет замечания к коду одной строкой — место, проблема, исправление. Ускоряет ревью диффа или PR без воды.
  `npx skills add JuliusBrussee/caveman --skill caveman-review -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/a192894723a8f47e7f504c7b5041967ff1f18e55/skills/caveman-review/SKILL.md) · 437 600 установок · ставится ✓ 16.11 · A/B 16.11: -0,21 — сжатие теряет детали
- **[ponytail](https://affpapa.org/nevibecode/skills/ponytail)** — ponytail переводит агента в режим старшего разработчика: он ищет самое короткое полное решение без лишних абстракций и функций. Подходит для задач, где важны ясный дифф и проверка рисков.
  `npx skills add DietrichGebert/ponytail --skill ponytail -a claude-code` · [исходник: dietrichgebert/ponytail](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail/SKILL.md) · 132 500 установок · ставится ✓ 16.11
- **[ponytail-review](https://affpapa.org/nevibecode/skills/ponytail-review)** — Скилл ponytail-review для Claude Code проверяет изменения в коде на ошибки, риски и лишнюю сложность. Запускается по запросам на ревью коммита, PR, ветки или файлов.
  `npx skills add DietrichGebert/ponytail --skill ponytail-review -a claude-code` · [исходник: dietrichgebert/ponytail](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail-review/SKILL.md) · 72 100 установок · ставится ✓ 16.11
- **[ponytail-audit](https://affpapa.org/nevibecode/skills/ponytail-audit)** — Скилл ponytail-audit для Claude Code и Codex проверяет репозиторий и ранжирует ошибки, риски и лишний код. Выполняет разовый аудит без автоматических правок.
  `npx skills add DietrichGebert/ponytail --skill ponytail-audit -a claude-code` · [исходник: dietrichgebert/ponytail](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail-audit/SKILL.md) · 59 700 установок · ставится ✓ 16.11
- **[caveman-explore](https://affpapa.org/nevibecode/skills/caveman-explore)** — Скилл caveman-explore ищет нужные файлы и строки в репозитории и возвращает ссылки на них. Помогает сориентироваться в незнакомой кодовой базе.
  `npx skills add JuliusBrussee/caveman --skill caveman-explore -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/a192894723a8f47e7f504c7b5041967ff1f18e55/skills/caveman-explore/SKILL.md) · 131 900 установок · ставится ✓ 16.11

<a name="topic-security"></a>
## Безопасность

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/security](https://affpapa.org/nevibecode/topic/security)

- **[security-audit](https://affpapa.org/nevibecode/skills/cloudflare-security-audit)** — Скилл security-audit проверяет кодовую базу на уязвимости и ищет нарушения границ доверия. Пригодится перед релизом или для точечного разбора опасных участков кода.
  `npx skills add cloudflare/security-audit-skill --skill security-audit -a claude-code` · [исходник: cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/SKILL.md) · 116 100 установок · ставится ✓ 16.11
- **[security-and-hardening](https://affpapa.org/nevibecode/skills/security-and-hardening)** — Скилл security-and-hardening проверяет код на уязвимости в обработчиках ввода, авторизации, сессиях и интеграциях. Помогает разбирать зависимости и риски утечки данных.
  `npx skills add addyosmani/agent-skills --skill security-and-hardening -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/security-and-hardening/SKILL.md) · 86 400 установок · ставится ✓ 16.11
- **[fix-security-vulnerabilities-with-strix](https://affpapa.org/nevibecode/skills/fix-security-vulnerabilities-with-strix)** — Скилл fix-security-vulnerabilities-with-strix разбирает подтверждённые Strix-уязвимости, исправляет их причину и повторно запускает проверку. Подойдёт после CLI- или cloud-сканирования.
  `npx skills add usestrix/strix --skill fix-security-vulnerabilities-with-strix -a claude-code` · [исходник: usestrix/strix](https://github.com/usestrix/strix/blob/fc44d80b3e8f85d91be7a6ba66db85fa84d3840b/skills/fix-security-vulnerabilities-with-strix/SKILL.md) · 20 300 установок
- **[web-app-penetration-testing](https://affpapa.org/nevibecode/skills/web-app-penetration-testing)** — Скилл web-app-penetration-testing для Claude Code проводит чёрный ящик-пентест веб-приложения через Strix и подтверждает уязвимости рабочим PoC. Проверяет staging и dev-сервер.
  `npx skills add usestrix/strix --skill web-app-penetration-testing -a claude-code` · [исходник: usestrix/strix](https://github.com/usestrix/strix/blob/fc44d80b3e8f85d91be7a6ba66db85fa84d3840b/skills/web-app-penetration-testing/SKILL.md) · 17 600 установок
- **[owasp-top-10-testing](https://affpapa.org/nevibecode/skills/owasp-top-10-testing)** — Скилл owasp-top-10-testing запускает агентов Strix для поиска реальных эксплойтов по стандарту OWASP Top 10:2025. Пригодится перед релизом или аудитом безопасности веб-приложения.
  `npx skills add usestrix/strix --skill owasp-top-10-testing -a claude-code` · [исходник: usestrix/strix](https://github.com/usestrix/strix/blob/fc44d80b3e8f85d91be7a6ba66db85fa84d3840b/skills/owasp-top-10-testing/SKILL.md) · 17 500 установок
- **[persona-it-admin](https://affpapa.org/nevibecode/skills/persona-it-admin)** — Скилл persona-it-admin задаёт агенту роль IT-администратора Google Workspace: проверяет подозрительные входы, настраивает политики Drive и разбирает заявки через gws.
  `npx skills add googleworkspace/cli --skill persona-it-admin -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/persona-it-admin/SKILL.md) · 31 100 установок
- **[gws-modelarmor](https://affpapa.org/nevibecode/skills/gws-modelarmor)** — Скилл gws-modelarmor для Claude Code фильтрует пользовательский контент и ответы ИИ через Google Model Armor. Проверяет безопасность промптов и работает с шаблонами фильтрации.
  `npx skills add googleworkspace/cli --skill gws-modelarmor -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-modelarmor/SKILL.md) · 31 000 установок
- **[gws-modelarmor-create-template](https://affpapa.org/nevibecode/skills/gws-modelarmor-create-template)** — Скилл gws-modelarmor-create-template создаёт шаблоны Google Model Armor в GCP для фильтрации контента. Пригодится при настройке защиты от джейлбрейков через утилиту gws.
  `npx skills add googleworkspace/cli --skill gws-modelarmor-create-template -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-modelarmor-create-template/SKILL.md) · 30 900 установок
- **[1password](https://affpapa.org/nevibecode/skills/1password)** — Настраивает 1Password CLI, подключает авторизацию и помогает безопасно внедрять секреты в команды без утечки паролей в чат.
  `npx skills add openclaw/openclaw --skill 1password -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/1password/SKILL.md) · 6 400 установок
- **[security-best-practices](https://affpapa.org/nevibecode/skills/githubcomopenaiskills-security-best-practices)** — Скилл security-best-practices проводит ревью кода на соответствие практикам безопасности для Python, JavaScript/TypeScript и Go и предлагает правки.
  `npx skills add tech-leads-club/agent-skills --skill security-best-practices -a claude-code` · [исходник: tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills/blob/e74dc8a7e8d59bb36f267afd089580e0858e224a/packages/skills-catalog/skills/(security)/security-best-practices/SKILL.md) · 390 установок

<a name="topic-devops"></a>
## DevOps и инфраструктура

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/devops](https://affpapa.org/nevibecode/topic/devops)

- **[wizard](https://affpapa.org/nevibecode/skills/wizard)** — Скилл wizard создаёт интерактивный bash-скрипт для ручных шагов: настройки сервисов, секретов CI и разовых миграций.
  `npx skills add mattpocock/skills --skill wizard -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/wizard/SKILL.md) · 553 369 установок · ставится ✓ 16.11
- **[setup-pre-commit](https://affpapa.org/nevibecode/skills/setup-pre-commit)** — Скилл setup-pre-commit настраивает pre-commit для JavaScript-репозитория: Husky запускает форматирование, проверку типов и тесты перед коммитом.
  `npx skills add mattpocock/skills --skill setup-pre-commit -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/setup-pre-commit/SKILL.md) · 489 289 установок · ставится ✓ 16.11
- **[google-agents-cli-observability](https://affpapa.org/nevibecode/skills/google-agents-cli-observability)** — Скилл google-agents-cli-observability для Claude Code настраивает наблюдаемость ИИ-агентов и помогает разбирать рабочие трассировки. Он включается при запросах о логировании, мониторинге или отладке трафика.
  `npx skills add google/agents-cli --skill google-agents-cli-observability -a claude-code` · [исходник: google/agents-cli](https://github.com/google/agents-cli/blob/6eedbdc2f44c388cbfc5f305eb83b9924cfefebb/skills/google-agents-cli-observability/SKILL.md) · 574 700 установок · ставится ✓ 16.11
- **[herdr](https://affpapa.org/nevibecode/skills/herdr)** — Скилл даёт агенту доступ к Herdr — терминальному мультиплексору для кодинг-агентов: панели, вкладки, воркспейсы и запуск команд.
  `npx skills add herdrdev/herdr --skill herdr -a claude-code` · [исходник: herdrdev/herdr](https://github.com/herdrdev/herdr/blob/ee5bfb5041bb3e4a49d591c72308aae3c81ecdde/skills/herdr/SKILL.md) · 84 800 установок · ставится ✓ 16.11
- **[vercel-cli-with-tokens](https://affpapa.org/nevibecode/skills/vercel-cli-with-tokens)** — Агент vercel-cli-with-tokens работает с Vercel CLI по access-токену, без vercel login: находит VERCEL_TOKEN, связывает проект, катит preview-деплой и правит переменные окружения.
  `npx skills add vercel-labs/agent-skills --skill vercel-cli-with-tokens -a claude-code` · [исходник: vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/vercel-cli-with-tokens/SKILL.md) · 160 500 установок
- **[turborepo](https://affpapa.org/nevibecode/skills/vercel-turborepo)** — Настраивает монорепозитории с Turborepo и чинит пайплайны задач. Пригодится при правках turbo.json, кеширования или сборки в CI.
  `npx skills add vercel/turborepo --skill turborepo -a claude-code` · [исходник: vercel/turborepo](https://github.com/vercel/turborepo/blob/67484391f9090c51a888221998b042a31a93e49d/skills/turborepo/SKILL.md) · 90 700 установок · ставится ✓ 16.11
- **[vercel-optimize](https://affpapa.org/nevibecode/skills/vercel-optimize)** — Скилл vercel-optimize для Claude Code, Codex, Cursor, GitHub Copilot и Gemini CLI, который проводит аудит стоимости и производительности задеплоенных проектов на Vercel.
  `npx skills add vercel-labs/agent-skills --skill vercel-optimize -a claude-code` · [исходник: vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/vercel-optimize/SKILL.md) · 136 600 установок
- **[shipping-and-launch](https://affpapa.org/nevibecode/skills/shipping-and-launch)** — Скилл shipping-and-launch для Claude Code готовит выпуск в продакшен: собирает предпусковой список, план мониторинга и отката. Включается при подготовке релиза или вопросе, что нужно до выкладки.
  `npx skills add addyosmani/agent-skills --skill shipping-and-launch -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/shipping-and-launch/SKILL.md) · 71 600 установок
- **[ci-cd-and-automation](https://affpapa.org/nevibecode/skills/ci-cd-and-automation)** — Скилл ci-cd-and-automation собирает пайплайн CI/CD на GitHub Actions: линт, типы, тесты, сборка и аудит зависимостей идут по порядку с фиксированным набором гейтов на каждый PR.
  `npx skills add addyosmani/agent-skills --skill ci-cd-and-automation -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/ci-cd-and-automation/SKILL.md) · 71 500 установок
- **[orca-per-workspace-env](https://affpapa.org/nevibecode/skills/orca-per-workspace-env)** — Скилл orca-per-workspace-env для Claude Code настраивает и проверяет рецепт окружения Orca для отдельного рабочего пространства. Он включается при работе с environmentRecipes в orca.yaml и ошибками orca vm recipe doctor.
  `npx skills add stablyai/orca --skill orca-per-workspace-env -a claude-code` · [исходник: stablyai/orca](https://github.com/stablyai/orca/blob/b30d12992e702724fffb426759c907d9b4450586/skills/orca-per-workspace-env/SKILL.md) · 12 600 установок

<a name="topic-cloud"></a>
## Облака: AWS, Azure, GCP

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/cloud](https://affpapa.org/nevibecode/topic/cloud)

- **[google-agents-cli-deploy](https://affpapa.org/nevibecode/skills/google-agents-cli-deploy)** — Скилл google-agents-cli-deploy инструктирует агента по деплою ИИ-агентов в Google Cloud через утилиту agents-cli. Помогает настроить запуск в Agent Runtime, Cloud Run или GKE с учётом CI/CD и секретов.
  `npx skills add google/agents-cli --skill google-agents-cli-deploy -a claude-code` · [исходник: google/agents-cli](https://github.com/google/agents-cli/blob/6eedbdc2f44c388cbfc5f305eb83b9924cfefebb/skills/google-agents-cli-deploy/SKILL.md) · 576 100 установок · ставится ✓ 16.11
- **[gws-drive-upload](https://affpapa.org/nevibecode/skills/gws-drive-upload)** — Скилл для Claude Code, Codex, Cursor и других IDE позволяет загружать файлы в Google Drive прямо из редактора с автоматическим определением типа и имени. Запускается командой gws drive +upload с указанием пути к файлу.
  `npx skills add googleworkspace/cli --skill gws-drive-upload -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-drive-upload/SKILL.md) · 51 400 установок
- **[gws-events-subscribe](https://affpapa.org/nevibecode/skills/gws-events-subscribe)** — Скилл gws-events-subscribe для Claude Code, Cursor и других IDE позволяет подписаться на события Google Workspace (сообщения в Chat, изменения документов) и получать их потоком в формате NDJSON.
  `npx skills add googleworkspace/cli --skill gws-events-subscribe -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-events-subscribe/SKILL.md) · 31 800 установок
- **[cloudflare](https://affpapa.org/nevibecode/skills/cloudflare-cloudflare)** — Скилл для Claude Code и Codex подбирает продукты Cloudflare под архитектуру проекта и диагностирует ошибки 52x или 403. Включается при создании сайтов, настройке API и отладке проксирования.
  `npx skills add cloudflare/skills --skill cloudflare -a claude-code` · [исходник: cloudflare/skills](https://github.com/cloudflare/skills/blob/cbf893b954222276bf1af57e5f23379231e0efb9/skills/cloudflare/SKILL.md) · 159 200 установок
- **[google-cloud-waf-cost-optimization](https://affpapa.org/nevibecode/skills/google-cloud-waf-cost-optimization)** — Скилл google-cloud-waf-cost-optimization для Claude Code, Gemini CLI и Codex, который оценивает рабочие нагрузки Google Cloud по столпу Cost Optimization фреймворка Well-Architected.
  `npx skills add google/skills --skill google-cloud-waf-cost-optimization -a claude-code` · [исходник: google/skills](https://github.com/google/skills/blob/06fff9e3edb7fc3c115a1769406047fcaf0a6289/skills/cloud/google-cloud-waf-cost-optimization/SKILL.md) · 14 266 установок
- **[firebase-basics](https://affpapa.org/nevibecode/skills/firebase-basics)** — Скилл firebase-basics настраивает Firebase CLI, помогает войти в аккаунт, создать или выбрать проект и скачать конфигурацию Android или iOS.
  `npx skills add google/skills --skill firebase-basics -a claude-code` · [исходник: google/skills](https://github.com/google/skills/blob/06fff9e3edb7fc3c115a1769406047fcaf0a6289/skills/cloud/firebase-basics/SKILL.md) · 14 100 установок
- **[gke-basics](https://affpapa.org/nevibecode/skills/gke-basics)** — Скилл gke-basics для Claude Code управляет развёртыванием кластеров GKE, выбором между Autopilot и Standard, получением доступов и деплоем нагрузок. Запускается при создании кластеров GKE и настройке параметров Kubernetes.
  `npx skills add google/skills --skill gke-basics -a claude-code` · [исходник: google/skills](https://github.com/google/skills/blob/06fff9e3edb7fc3c115a1769406047fcaf0a6289/skills/cloud/gke-basics/SKILL.md) · 13 953 установки
- **[firebase-app-hosting-basics](https://affpapa.org/nevibecode/skills/firebase-app-hosting-basics)** — Скилл firebase-app-hosting-basics для Claude Code помогает развёртывать Next.js и Angular с SSR через Firebase App Hosting. Настраивает бэкенд, секреты и деплой из GitHub.
  `npx skills add firebase/agent-skills --skill firebase-app-hosting-basics -a claude-code` · [исходник: firebase/agent-skills](https://github.com/firebase/agent-skills/blob/99954a30898bb5ddc8152ee10e124dc3b4106bf7/skills/firebase-app-hosting-basics/SKILL.md) · 180 900 установок
- **[firebase-crashlytics](https://affpapa.org/nevibecode/skills/firebase-crashlytics)** — Скилл для Claude Code, который помогает настроить Firebase Crashlytics и SDK для отчётов о сбоях. Запускается при добавлении Crashlytics в Android, iOS или Web-приложение.
  `npx skills add firebase/agent-skills --skill firebase-crashlytics -a claude-code` · [исходник: firebase/agent-skills](https://github.com/firebase/agent-skills/blob/99954a30898bb5ddc8152ee10e124dc3b4106bf7/skills/firebase-crashlytics/SKILL.md) · 142 900 установок
- **[prisma-compute](https://affpapa.org/nevibecode/skills/prisma-compute)** — Скилл для Claude Code управляет развёртыванием и обслуживанием приложений на Prisma Compute через CLI Prisma 8. Помогает настроить Prisma Composer, откатить релизы и проверить логи сервисов.
  `npx skills add prisma/skills --skill prisma-compute -a claude-code` · [исходник: prisma/skills](https://github.com/prisma/skills/blob/a6f192959cf43b08aa330fe1ffca090267215812/prisma-compute/SKILL.md) · 410 600 установок

<a name="topic-data"></a>
## Данные и базы

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/data](https://affpapa.org/nevibecode/topic/data)

- **[migration](https://affpapa.org/nevibecode/skills/migration)** — Скилл migration задаёт правила безопасных миграций схем, данных и API с обязательным откатом. Пригодится при изменениях, где нельзя терять данные или ломать совместимость.
  `npx skills add JuliusBrussee/caveman --skill migration -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/a192894723a8f47e7f504c7b5041967ff1f18e55/skills/migration/SKILL.md) · 127 700 установок · ставится ✓ 16.11 · A/B 16.11: +0,43 — лучший по знаку, 5 из 6 оценок в плюс
- **[recipe-compare-sheet-tabs](https://affpapa.org/nevibecode/skills/recipe-compare-sheet-tabs)** — Скилл recipe-compare-sheet-tabs для Claude Code сравнивает данные в двух вкладках Google Sheets. Он запускается по запросу найти различия между вкладками таблицы.
  `npx skills add googleworkspace/cli --skill recipe-compare-sheet-tabs -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/recipe-compare-sheet-tabs/SKILL.md) · 31 800 установок
- **[notion](https://affpapa.org/nevibecode/skills/notion)** — Скилл связывает агента с Notion через ntn CLI и API: он помогает читать и менять страницы, запрашивать data sources и загружать файлы.
  `npx skills add openclaw/openclaw --skill notion -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/notion/SKILL.md) · 5 700 установок
- **[data-visualization](https://affpapa.org/nevibecode/skills/anthropics-data-visualization)** — Скилл data-visualization подбирает подходящие типы графиков под структуру данных и генерирует код на Python с matplotlib, seaborn и plotly. Пригодится при подготовке отчётов.
  `npx skills add anthropics/knowledge-work-plugins --skill data-visualization -a claude-code` · [исходник: anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/data/skills/data-visualization/SKILL.md) · 14 800 установок
- **[database-migrations](https://affpapa.org/nevibecode/skills/database-migrations)** — Скилл database-migrations описывает безопасные и обратимые миграции схемы: expand-contract, индексы CONCURRENTLY, батч-бэкфиллы и рабочие процессы для PostgreSQL, Prisma, Drizzle, Kysely, Django и golang-migrate.
  `npx skills add affaan-m/ECC --skill database-migrations -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/database-migrations/SKILL.md) · 6 900 установок
- **[postgres-patterns](https://affpapa.org/nevibecode/skills/postgres-patterns)** — Скилл postgres-patterns для Claude Code собирает практики PostgreSQL для проектирования схем и настройки запросов: индексы, типы данных, RLS и диагностика медленных запросов.
  `npx skills add affaan-m/ECC --skill postgres-patterns -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/postgres-patterns/SKILL.md) · 6 800 установок
- **[bigquery-basics](https://affpapa.org/nevibecode/skills/bigquery-basics)** — Скилл bigquery-basics управляет ресурсами BigQuery и запускает SQL-запросы. Подходит для создания датасетов, таблиц, представлений и базовой загрузки данных.
  `npx skills add google/skills --skill bigquery-basics -a claude-code` · [исходник: google/skills](https://github.com/google/skills/blob/06fff9e3edb7fc3c115a1769406047fcaf0a6289/skills/cloud/bigquery-basics/SKILL.md) · 17 678 установок
- **[mysql-patterns](https://affpapa.org/nevibecode/skills/mysql-patterns)** — Скилл mysql-patterns с проверенными шаблонами для MySQL и MariaDB. Помогает проектировать схемы, настраивать индексы и ускорять медленные транзакции.
  `npx skills add affaan-m/ECC --skill mysql-patterns -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/mysql-patterns/SKILL.md) · 6 100 установок
- **[alloydb-basics](https://affpapa.org/nevibecode/skills/alloydb-basics)** — Скилл alloydb-basics помогает создавать и настраивать кластеры и экземпляры AlloyDB for PostgreSQL, управлять резервными копиями и использовать инструменты AlloyDB MCP. Подходит для администрирования AlloyDB.
  `npx skills add google/skills --skill alloydb-basics -a claude-code` · [исходник: google/skills](https://github.com/google/skills/blob/06fff9e3edb7fc3c115a1769406047fcaf0a6289/skills/cloud/alloydb-basics/SKILL.md) · 12 991 установка
- **[postgresql-table-design](https://affpapa.org/nevibecode/skills/postgresql-table-design)** — Скилл postgresql-table-design помогает проектировать и проверять схемы PostgreSQL: типы, ключи, ограничения, индексы и разбиение таблиц.
  `npx skills add wshobson/agents --skill postgresql-table-design -a claude-code` · [исходник: wshobson/agents](https://github.com/wshobson/agents/blob/4bde3168b43c0655c4d00ea2726e631719908a6d/plugins/database-design/skills/postgresql-table-design/SKILL.md) · 27 780 установок

<a name="topic-ai-ml"></a>
## ИИ и ML

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/ai-ml](https://affpapa.org/nevibecode/topic/ai-ml)

- **[skill-creator](https://affpapa.org/nevibecode/skills/skill-creator)** — Скилл skill-creator помогает создать новый скилл, доработать существующий и проверить результат через тестовые промпты и оценки.
  `npx skills add anthropics/skills --skill skill-creator -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/skill-creator/SKILL.md) · 414 180 установок · ставится ✓ 16.11
- **[media-use](https://affpapa.org/nevibecode/skills/media-use)** — Скилл media-use ищет и генерирует медиафайлы для видеопроектов HyperFrames, сохраняя их локально в папку assets. Подключает каталог HeyGen, озвучку, фоновую музыку и цветовую коррекцию видео.
  `npx skills add heygen-com/hyperframes --skill media-use -a claude-code` · [исходник: heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/blob/95e4e7f880f5005211412e926b307f4a53f47246/skills/media-use/SKILL.md) · 1 500 000 установок · ставится ✓ 16.11
- **[subagent-driven-development](https://affpapa.org/nevibecode/skills/subagent-driven-development)** — Скилл subagent-driven-development выполняет план через отдельных субагентов для каждой задачи и проверяет результат после каждого шага. Подходит для независимых задач в одной сессии.
  `npx skills add obra/superpowers --skill subagent-driven-development -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/subagent-driven-development/SKILL.md) · 237 746 установок · ставится ✓ 16.11
- **[caveman-stats](https://affpapa.org/nevibecode/skills/caveman-stats)** — Скилл caveman-stats выводит статистику токенов и активный режим сессии или направляет к штатным отчётам хоста. Полезен для контроля расхода токенов вывода и кэша.
  `npx skills add JuliusBrussee/caveman --skill caveman-stats -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/a192894723a8f47e7f504c7b5041967ff1f18e55/skills/caveman-stats/SKILL.md) · 385 600 установок · ставится ✓ 16.11
- **[claude-api](https://affpapa.org/nevibecode/skills/claude-api)** — Справочник по Anthropic SDK и API Claude для генерации кода без устаревших параметров и выдуманных методов.
  `npx skills add anthropics/skills --skill claude-api -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/claude-api/SKILL.md) · 74 198 установок · ставится ✓ 16.11
- **[karpathy-guidelines](https://affpapa.org/nevibecode/skills/karpathy-guidelines)** — Скилл karpathy-guidelines для Claude Code задаёт правила, снижающие типовые ошибки LLM при написании кода: явные допущения, минимальный код, точечные правки и проверка результата.
  `npx skills add multica-ai/andrej-karpathy-skills --skill karpathy-guidelines -a claude-code` · [исходник: multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/skills/karpathy-guidelines/SKILL.md) · 47 100 установок · ставится ✓ 16.11
- **[google-agents-cli-publish](https://affpapa.org/nevibecode/skills/google-agents-cli-publish)** — Скилл google-agents-cli-publish проводит задеплоенного агента через agents-cli publish gemini: режимы ADK и A2A, флаги, автодетект по метаданным и регистрация в Agent Registry.
  `npx skills add google/agents-cli --skill google-agents-cli-publish -a claude-code` · [исходник: google/agents-cli](https://github.com/google/agents-cli/blob/6eedbdc2f44c388cbfc5f305eb83b9924cfefebb/skills/google-agents-cli-publish/SKILL.md) · 575 900 установок · ставится ✓ 16.11
- **[caveman-optimize](https://affpapa.org/nevibecode/skills/caveman-optimize)** — Скилл caveman-optimize помогает разобрать наблюдение Caveman, выбрать кандидата оператором и проверить его парным сравнением с базовой версией. Изменения требуют явного одобрения.
  `npx skills add JuliusBrussee/caveman --skill caveman-optimize -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/a192894723a8f47e7f504c7b5041967ff1f18e55/skills/caveman-optimize/SKILL.md) · 129 900 установок · ставится ✓ 16.11
- **[caveman-evidence-review](https://affpapa.org/nevibecode/skills/caveman-evidence-review)** — Скилл caveman-evidence-review читает данные Caveman Cloud о расходах LLM, трассах и маршрутизации. Подходит для проверки того, куда уходит бюджет проекта.
  `npx skills add JuliusBrussee/caveman --skill caveman-evidence-review -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/a192894723a8f47e7f504c7b5041967ff1f18e55/skills/caveman-evidence-review/SKILL.md) · 128 400 установок · ставится ✓ 16.11
- **[context-engineering](https://affpapa.org/nevibecode/skills/context-engineering)** — Скилл context-engineering помогает настроить контекст ИИ-агента: какие правила, спецификации и файлы отдать агенту и когда. Пригодится в начале сессии, при падении качества ответов и при смене задач.
  `npx skills add addyosmani/agent-skills --skill context-engineering -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/context-engineering/SKILL.md) · 75 400 установок

<a name="topic-automation"></a>
## Автоматизация и no-code: n8n, Zapier, Make

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/automation](https://affpapa.org/nevibecode/topic/automation)

- **[lark-event](https://affpapa.org/nevibecode/skills/lark-event)** — Скилл lark-event для Claude Code запускает подписку на события Lark и передаёт их потоком NDJSON. Он включается для обработки сообщений, изменений задач и других событий в реальном времени.
  `npx skills add larksuite/cli --skill lark-event -a claude-code` · [исходник: larksuite/cli](https://github.com/larksuite/cli/blob/3d82c85419ad7560ad017db7a3972a596b5fbeb1/skills/lark-event/SKILL.md) · 484 000 установок · ставится ✓ 16.11
- **[gws-gmail-send](https://affpapa.org/nevibecode/skills/gws-gmail-send)** — Скилл для Claude Code, Codex, Cursor, GitHub Copilot и Gemini CLI, который даёт агенту команду gws gmail +send. Отправляет письма через Gmail с вложениями, CC/BCC, HTML-телом и алиасами отправителя.
  `npx skills add googleworkspace/cli --skill gws-gmail-send -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-gmail-send/SKILL.md) · 76 800 установок
- **[recipe-email-drive-link](https://affpapa.org/nevibecode/skills/recipe-email-drive-link)** — Скилл recipe-email-drive-link для Claude Code, Codex, Cursor и других ИИ-редакторов автоматизирует отправку ссылок на файлы Google Drive по почте. Находит файл, открывает доступ и отправляет письмо с сообщением — всё в одной цепочке команд.
  `npx skills add googleworkspace/cli --skill recipe-email-drive-link -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/recipe-email-drive-link/SKILL.md) · 32 500 установок
- **[recipe-label-and-archive-emails](https://affpapa.org/nevibecode/skills/recipe-label-and-archive-emails)** — Скилл recipe-label-and-archive-emails для Claude Code организует почту: ищет письма в Gmail по условию, добавляет метки и архивирует их через Google Workspace CLI.
  `npx skills add googleworkspace/cli --skill recipe-label-and-archive-emails -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/recipe-label-and-archive-emails/SKILL.md) · 31 500 установок
- **[openhue](https://affpapa.org/nevibecode/skills/openhue)** — Скилл openhue для Claude Code, Codex, Cursor и других AI-агентов, который управляет лампами и сценами Philips Hue через CLI. Работает через локальный Hue Bridge — агент включает свет, меняет яркость и цвет прямо из чата.
  `npx skills add openclaw/openclaw --skill openhue -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/openhue/SKILL.md) · 5 200 установок
- **[baoyu-post-to-x](https://affpapa.org/nevibecode/skills/baoyu-post-to-x)** — Скилл baoyu-post-to-x публикует текст, картинки, видео и длинные статьи в X через браузер Chrome. Работает через плагин Codex, Computer Use или CDP-скрипты.
  `npx skills add JimLiu/baoyu-skills --skill baoyu-post-to-x -a claude-code` · [исходник: jimliu/baoyu-skills](https://github.com/JimLiu/baoyu-skills/blob/ca703c2d7c2c4399a1dc0cf82224f8551e05a96d/skills/baoyu-post-to-x/SKILL.md) · 29 400 установок
- **[baoyu-youtube-transcript](https://affpapa.org/nevibecode/skills/baoyu-youtube-transcript)** — Скилл baoyu-youtube-transcript для Claude Code и Codex: скачивает субтитры и обложку YouTube-видео по ссылке или ID — без ручного копирования текста ролика.
  `npx skills add JimLiu/baoyu-skills --skill baoyu-youtube-transcript -a claude-code` · [исходник: jimliu/baoyu-skills](https://github.com/JimLiu/baoyu-skills/blob/ca703c2d7c2c4399a1dc0cf82224f8551e05a96d/skills/baoyu-youtube-transcript/SKILL.md) · 22 800 установок
- **[wacli](https://affpapa.org/nevibecode/skills/wacli)** — Скилл подключает консольную утилиту wacli для отправки сообщений в WhatsApp третьим лицам, поиска переписок и скачивания истории чатов.
  `npx skills add openclaw/openclaw --skill wacli -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/extensions/whatsapp/skills/wacli/SKILL.md) · 3 300 установок
- **[just](https://affpapa.org/nevibecode/skills/just)** — Скилл для Claude Code и других агентов: справочник по just с синтаксисом justfile, рецептами и командами просмотра — чтобы читать и запускать задачи в проекте.
  `npx skills add casey/just --skill just -a claude-code` · [исходник: casey/just](https://github.com/casey/just/blob/168c8e288dc8a591ca851b4ef070cada64f43c35/skills/just/SKILL.md) · 1 200 установок
- **[create-an-asset](https://affpapa.org/nevibecode/skills/create-an-asset)** — Скилл create-an-asset для Claude Code собирает презентации, одностраничники и раздаточные материалы из данных аккаунта, заметок с созвонов и утверждённого контента без выдуманных цифр.
  `npx skills add anthropics/knowledge-work-plugins --skill create-an-asset -a claude-code` · [исходник: anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/sales/skills/create-an-asset/SKILL.md) · 3 100 установок

<a name="topic-docs"></a>
## Тексты и документация

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/docs](https://affpapa.org/nevibecode/topic/docs)

- **[grill-with-docs](https://affpapa.org/nevibecode/skills/grill-with-docs)** — Скилл grill-with-docs проводит жёсткое интервью по плану или дизайну и по ходу создаёт ADR и глоссарий. Подойдёт перед началом сложной разработки.
  `npx skills add mattpocock/skills --skill grill-with-docs -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/grill-with-docs/SKILL.md) · 1 219 756 установок · ставится ✓ 16.11
- **[domain-modeling](https://affpapa.org/nevibecode/skills/domain-modeling)** — Скилл domain-modeling для Claude Code уточняет термины проекта, ведёт GLOSSARY.md и фиксирует архитектурные решения в ADR. Уточняет модель предметной области при её изменении.
  `npx skills add mattpocock/skills --skill domain-modeling -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/domain-modeling/SKILL.md) · 876 391 установка · ставится ✓ 16.11
- **[to-spec](https://affpapa.org/nevibecode/skills/to-spec)** — Скилл to-spec собирает из текущего диалога и контекста репозитория спецификацию, затем публикует её в трекере задач. Нужен после обсуждения фичи, когда пора передать работу агенту.
  `npx skills add mattpocock/skills --skill to-spec -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/to-spec/SKILL.md) · 715 388 установок · ставится ✓ 16.11
- **[pdf](https://affpapa.org/nevibecode/skills/pdf)** — Скилл для Claude Code читает, создаёт и меняет PDF-файлы, включая формы и сканы. Обрабатывает PDF в проекте.
  `npx skills add anthropics/skills --skill pdf -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/pdf/SKILL.md) · 216 041 установка
- **[doc-coauthoring](https://affpapa.org/nevibecode/skills/doc-coauthoring)** — Скилл doc-coauthoring ведёт автора через сбор контекста, подготовку разделов и проверку документа глазами нового читателя. Подходит для спецификаций, RFC, предложений и decision docs.
  `npx skills add anthropics/skills --skill doc-coauthoring -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/doc-coauthoring/SKILL.md) · 93 900 установок
- **[caveman-help](https://affpapa.org/nevibecode/skills/caveman-help)** — Скилл caveman-help для Claude Code и других поддерживаемых платформ показывает команды Caveman и описывает его режимы. Помогает настроить стиль ответов и связанные скиллы.
  `npx skills add JuliusBrussee/caveman --skill caveman-help -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/a192894723a8f47e7f504c7b5041967ff1f18e55/skills/caveman-help/SKILL.md) · 427 900 установок · ставится ✓ 16.11
- **[internal-comms](https://affpapa.org/nevibecode/skills/internal-comms)** — Скилл internal-comms помогает Claude писать внутренние коммуникации в форматах вашей компании: от статусных отчётов до FAQ и отчётов об инцидентах.
  `npx skills add anthropics/skills --skill internal-comms -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/internal-comms/SKILL.md) · 79 929 установок · ставится ✓ 16.11
- **[archify](https://affpapa.org/nevibecode/skills/archify)** — Скилл archify для Claude Code создаёт проверенные диаграммы и одностраничные объяснения в HTML. Показывает устройство системы, поток данных или схему базы.
  `npx skills add tt-a1i/archify --skill archify -a claude-code` · [исходник: tt-a1i/archify](https://github.com/tt-a1i/archify/blob/44781293f38728baf04dbad33ce1a0cef8c39cca/archify/SKILL.md) · 193 400 установок · ставится ✓ 16.11
- **[writing-guidelines](https://affpapa.org/nevibecode/skills/writing-guidelines)** — Скилл writing-guidelines для ревью документации и прозы по письменному гайдлайну. Возвращает замечания с номерами строк, чтобы правки не искать по всему файлу вручную.
  `npx skills add vercel-labs/agent-skills --skill writing-guidelines -a claude-code` · [исходник: vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/writing-guidelines/SKILL.md) · 133 400 установок
- **[spec-driven-development](https://affpapa.org/nevibecode/skills/spec-driven-development)** — Скилл spec-driven-development для Claude Code готовит спецификацию до начала разработки. Он включается, когда нужно разобрать расплывчатые требования, спланировать функцию или оформить изменения к уже выпущенной спецификации.
  `npx skills add addyosmani/agent-skills --skill spec-driven-development -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/spec-driven-development/SKILL.md) · 79 100 установок · ставится ✓ 16.11

<a name="topic-office"></a>
## Документы и офис

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/office](https://affpapa.org/nevibecode/topic/office)

- **[pptx](https://affpapa.org/nevibecode/skills/pptx)** — Скилл для Claude Code создаёт, разбирает и редактирует файлы .pptx и .potx. Срабатывает при любых задачах со слайдами, шаблонами или презентациями.
  `npx skills add anthropics/skills --skill pptx -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/pptx/SKILL.md) · 241 433 установки
- **[docx](https://affpapa.org/nevibecode/skills/docx)** — Скилл для Claude Code и Claude.ai создаёт, читает и редактирует документы Word. Включается по запросу на работу с .docx или шаблоном .dotx.
  `npx skills add anthropics/skills --skill docx -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/docx/SKILL.md) · 206 304 установки
- **[xlsx](https://affpapa.org/nevibecode/skills/xlsx)** — Скилл для Claude Code и Claude.ai создаёт, правит и проверяет электронные таблицы. Запускается при работе с файлами xlsx, xlsm, csv или tsv.
  `npx skills add anthropics/skills --skill xlsx -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/xlsx/SKILL.md) · 187 223 установки
- **[gws-sheets](https://affpapa.org/nevibecode/skills/gws-sheets)** — Скилл gws-sheets для Claude Code читает и изменяет таблицы Google Sheets через CLI. Автоматизирует операции с таблицами и работу с данными проекта.
  `npx skills add googleworkspace/cli --skill gws-sheets -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-sheets/SKILL.md) · 61 900 установок
- **[gws-sheets-read](https://affpapa.org/nevibecode/skills/gws-sheets-read)** — Скилл gws-sheets-read для Claude Code читает значения ячеек и листов из Google Таблиц через CLI. Получает данные таблицы без их изменения.
  `npx skills add googleworkspace/cli --skill gws-sheets-read -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-sheets-read/SKILL.md) · 52 800 установок
- **[gws-slides](https://affpapa.org/nevibecode/skills/gws-slides)** — Скилл gws-slides для Claude Code и других AI-редакторов, который добавляет команды для чтения и редактирования презентаций Google Slides прямо из кода. Работает на Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI и OpenCode.
  `npx skills add googleworkspace/cli --skill gws-slides -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-slides/SKILL.md) · 43 700 установок
- **[gog](https://affpapa.org/nevibecode/skills/gog)** — Скилл для Claude Code задаёт агенту правила работы с CLI gog в Gmail, Calendar, Drive, Contacts, Sheets и Docs. Агент выполняет действия в Google Workspace из терминала.
  `npx skills add openclaw/openclaw --skill gog -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/gog/SKILL.md) · 8 500 установок
- **[nano-pdf](https://affpapa.org/nevibecode/skills/nano-pdf)** — Скилл для Claude Code и Codex. Редактирует PDF-страницы по текстовым инструкциям через CLI nano-pdf.
  `npx skills add openclaw/openclaw --skill nano-pdf -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/nano-pdf/SKILL.md) · 7 200 установок
- **[convert-documents-to-markdown](https://affpapa.org/nevibecode/skills/convert-documents-to-markdown)** — Скилл convert-documents-to-markdown для Claude Code конвертирует офисные документы, таблицы и PDF в GitHub-Flavored Markdown через утилиту anydoc. Извлекает данные из DOCX и XLSX без ручной вычитки.
  `npx skills add firecrawl/anydoc --skill convert-documents-to-markdown -a claude-code` · [исходник: firecrawl/anydoc](https://github.com/firecrawl/anydoc/blob/e56a49bf3062c55e8d258346de4a36f4cfb59f70/skills/convert-documents-to-markdown/SKILL.md) · 13 700 установок
- **[nature-paper2ppt](https://affpapa.org/nevibecode/skills/nature-paper2ppt)** — Скилл nature-paper2ppt собирает китайскую академическую презентацию .pptx из научной статьи или заметок: слайды, рисунки из источника и заметки докладчика.
  `npx skills add Yuan1z0825/nature-skills --skill nature-paper2ppt -a claude-code` · [исходник: yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills/blob/14ca69710cae192325395a380e9cdd4ae5d9d0c8/skills/nature-paper2ppt/SKILL.md) · 17 500 установок

<a name="topic-seo"></a>
## SEO и GEO

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/seo](https://affpapa.org/nevibecode/topic/seo)

- **[seo-audit](https://affpapa.org/nevibecode/skills/coreyhaines31-seo-audit)** — Скилл seo-audit для Claude Code, Codex, Cursor и других платформ. Находит технические ошибки поисковой оптимизации, проблемы индексации и сбои в разметке сайта.
  `npx skills add coreyhaines31/marketingskills --skill seo-audit -a claude-code` · [исходник: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/seo-audit/SKILL.md) · 257 200 установок · ставится ✓ 16.11 · A/B 16.11: +0,00 — эффекта нет
- **[marketing-psychology](https://affpapa.org/nevibecode/skills/coreyhaines31-marketing-psychology)** — Скилл marketing-psychology для Claude Code помогает применять психологические модели в маркетинге. Разбирает поведение покупателей и оценивает, насколько честно работает приём убеждения.
  `npx skills add coreyhaines31/marketingskills --skill marketing-psychology -a claude-code` · [исходник: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/marketing-psychology/SKILL.md) · 179 700 установок
- **[ai-seo](https://affpapa.org/nevibecode/skills/ai-seo)** — Скилл ai-seo для Claude Code помогает попасть в ответы ChatGPT, Perplexity, Google AI Overviews и других LLM. Настраивает контент, структуру и формат страниц, чтобы AI-системы выбирали ваши источники.
  `npx skills add coreyhaines31/marketingskills --skill ai-seo -a claude-code` · [исходник: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/ai-seo/SKILL.md) · 166 900 установок · A/B 16.11: -0,21 — эффекта нет, ~9 тыс. токенов
- **[seo](https://affpapa.org/nevibecode/skills/affaan-m-seo)** — Скилл для ИИ-агента: проверяет техническое SEO, разметку и Core Web Vitals, а потом предлагает конкретные правки по страницам.
  `npx skills add affaan-m/ECC --skill seo -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/seo/SKILL.md) · 6 500 установок
- **[content-engine](https://affpapa.org/nevibecode/skills/content-engine)** — Скилл content-engine для Claude Code превращает статьи, заметки и демо в контент для X, LinkedIn, TikTok, YouTube и рассылок. Создаёт посты, сценарии и контент-планы.
  `npx skills add affaan-m/ECC --skill content-engine -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/content-engine/SKILL.md) · 6 200 установок
- **[marketing-campaign](https://affpapa.org/nevibecode/skills/marketing-campaign)** — Скилл marketing-campaign планирует многоканальный запуск продукта: от анализа аудитории и позиционирования до текстов для лендинга, писем и соцсетей. Помогает собрать материалы запуска по единой структуре.
  `npx skills add affaan-m/ECC --skill marketing-campaign -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/marketing-campaign/SKILL.md) · 6 100 установок
- **[fixing-metadata](https://affpapa.org/nevibecode/skills/fixing-metadata)** — Скилл fixing-metadata проверяет и приводит в порядок метаданные страниц: заголовки, описания, canonical, Open Graph, карточки Twitter, иконки и JSON-LD.
  `npx skills add ibelick/ui-skills --skill fixing-metadata -a claude-code` · [исходник: ibelick/ui-skills](https://github.com/ibelick/ui-skills/blob/347d3189830f8ec3c4c041421bce19182a79dc7a/skills/fixing-metadata/SKILL.md) · 20 200 установок
- **[keyword-research](https://affpapa.org/nevibecode/skills/every-app-keyword-research)** — Скилл keyword-research подбирает поисковые запросы через MCP-инструменты OpenSEO, оценивает метрики выдачи и сохраняет перспективные фразы в проект.
  `npx skills add every-app/open-seo --skill keyword-research -a claude-code` · [исходник: every-app/open-seo](https://github.com/every-app/open-seo/blob/14402bf60409e9024d6de8f008843a4c9bedca8a/plugins/openseo/skills/keyword-research/SKILL.md) · 7 800 установок
- **[competitor-analysis](https://affpapa.org/nevibecode/skills/competitor-analysis)** — Скилл competitor-analysis для Claude Code разбирает органический след одного конкурента: ключевые слова, бэклинки, темы контента и слабые места. Запускается по домену и выдаёт план действий.
  `npx skills add every-app/open-seo --skill competitor-analysis -a claude-code` · [исходник: every-app/open-seo](https://github.com/every-app/open-seo/blob/14402bf60409e9024d6de8f008843a4c9bedca8a/plugins/openseo/skills/competitor-analysis/SKILL.md) · 7 600 установок
- **[seo-project-setup](https://affpapa.org/nevibecode/skills/seo-project-setup)** — Скилл seo-project-setup собирает контекст SEO-проекта: сайт, цели, позиционирование, конкурентов и важные страницы. Нужен перед работой других SEO-скиллов.
  `npx skills add every-app/open-seo --skill seo-project-setup -a claude-code` · [исходник: every-app/open-seo](https://github.com/every-app/open-seo/blob/14402bf60409e9024d6de8f008843a4c9bedca8a/plugins/openseo/skills/seo-project-setup/SKILL.md) · 7 600 установок

<a name="topic-marketing"></a>
## Маркетинг и контент

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/marketing](https://affpapa.org/nevibecode/topic/marketing)

- **[copywriting](https://affpapa.org/nevibecode/skills/coreyhaines31-copywriting)** — Скилл copywriting для Claude Code, Codex, Cursor и других платформ помогает писать и переделывать текст страниц (главная, лендинг, прайсинг, описание фич).
  `npx skills add coreyhaines31/marketingskills --skill copywriting -a claude-code` · [исходник: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/copywriting/SKILL.md) · 257 800 установок · ставится ✓ 16.11 · A/B 16.11: -0,33 — раздувает meta description
- **[content-strategy](https://affpapa.org/nevibecode/skills/coreyhaines31-content-strategy)** — Скилл content-strategy для Claude Code и Codex выстраивает редакционный план вокруг поискового спроса и задач клиентов. Помогает отобрать темы, которые приводят лиды или цитируются в сети.
  `npx skills add coreyhaines31/marketingskills --skill content-strategy -a claude-code` · [исходник: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/content-strategy/SKILL.md) · 179 600 установок
- **[copy-editing](https://affpapa.org/nevibecode/skills/coreyhaines31-copy-editing)** — Скилл copy-editing для Claude Code и Codex: редактирует маркетинговые тексты, письма и описания без полной переписки.
  `npx skills add coreyhaines31/marketingskills --skill copy-editing -a claude-code` · [исходник: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/copy-editing/SKILL.md) · 163 900 установок
- **[brag](https://affpapa.org/nevibecode/skills/brag)** — Скилл brag для Claude Code, который превращает код проекта в короткий презентационный видеоролик. Запускается при запросе на создание видео или демонстрацию продукта.
  `npx skills add latent-spaces/brag --skill brag -a claude-code` · [исходник: latent-spaces/brag](https://github.com/latent-spaces/brag/blob/06379432a9243c951dfcc051153be18d2d261044/skills/brag/SKILL.md) · 25 000 установок
- **[higgsfield-video-explainer](https://affpapa.org/nevibecode/skills/higgsfield-video-explainer)** — Скилл higgsfield-video-explainer для Claude Code перенаправляет старый сценарий создания видео-объяснения в иллюстрированный процесс Higgsfield. Он включается при явном вызове или продолжении прежнего рабочего процесса.
  `npx skills add higgsfield-ai/skills --skill higgsfield-video-explainer -a claude-code` · [исходник: higgsfield-ai/skills](https://github.com/higgsfield-ai/skills/blob/27000402070db19d958789d05b3b52b6f4718d7c/higgsfield-video-explainer/SKILL.md) · 154 400 установок
- **[baoyu-post-to-wechat](https://affpapa.org/nevibecode/skills/baoyu-post-to-wechat)** — Скилл baoyu-post-to-wechat публикует статьи и графические посты в WeChat Official Account через API платформы или браузерный профиль Chrome.
  `npx skills add JimLiu/baoyu-skills --skill baoyu-post-to-wechat -a claude-code` · [исходник: jimliu/baoyu-skills](https://github.com/JimLiu/baoyu-skills/blob/ca703c2d7c2c4399a1dc0cf82224f8551e05a96d/skills/baoyu-post-to-wechat/SKILL.md) · 35 000 установок
- **[baoyu-post-to-weibo](https://affpapa.org/nevibecode/skills/baoyu-post-to-weibo)** — Скилл baoyu-post-to-weibo готовит обычные публикации и статьи для Weibo через Chrome. После заполнения формы пользователь сам проверяет запись и публикует её.
  `npx skills add JimLiu/baoyu-skills --skill baoyu-post-to-weibo -a claude-code` · [исходник: jimliu/baoyu-skills](https://github.com/JimLiu/baoyu-skills/blob/ca703c2d7c2c4399a1dc0cf82224f8551e05a96d/skills/baoyu-post-to-weibo/SKILL.md) · 22 100 установок
- **[crosspost](https://affpapa.org/nevibecode/skills/crosspost)** — Скилл crosspost для Claude Code и Codex, распределяет контент по X, LinkedIn, Threads и Bluesky с адаптацией под каждую платформу. Не публикует одинаковый текст везде — переделывает содержание под ограничения и аудиторию каждой сети.
  `npx skills add affaan-m/ECC --skill crosspost -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/crosspost/SKILL.md) · 5 900 установок
- **[investor-outreach](https://affpapa.org/nevibecode/skills/investor-outreach)** — Скилл investor-outreach для Claude Code и Codex, который составляет письма инвесторам, запросы на тёплые интро и апдейты по раунду. Генерирует персонализированные письма с конкретными просьбами, без общих фраз и размытых комплиментов.
  `npx skills add affaan-m/ECC --skill investor-outreach -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/investor-outreach/SKILL.md) · 5 900 установок
- **[reddit-automation](https://affpapa.org/nevibecode/skills/reddit-automation)** — Скилл reddit-automation находит треды на Reddit, где людям нужен ваш продукт, и пишет короткие полезные ответы с раскрытием, что вы связаны с продуктом.
  `npx skills add flowkit-labs/skills --skill reddit-automation -a claude-code` · [исходник: flowkit-labs/skills](https://github.com/flowkit-labs/skills/blob/0c9e2b63f504a296a86e45ed3a60a426dd979ca6/reddit-automation/SKILL.md) · 1 500 000 установок

<a name="topic-browser"></a>
## Браузер и парсинг

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/browser](https://affpapa.org/nevibecode/topic/browser)

- **[agent-browser](https://affpapa.org/nevibecode/skills/vercel-labs-agent-browser)** — Скилл agent-browser для Claude Code управляет браузером по запросам на навигацию, заполнение форм и проверку веб-приложений. Агент также может запускать через него исследовательское тестирование и автоматизировать Electron-приложения.
  `npx skills add vercel-labs/agent-browser --skill agent-browser -a claude-code` · [исходник: vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/blob/9f62847e89712164a6d5ea823e8c700d5fd911cd/skills/agent-browser/SKILL.md) · 1 500 000 установок · ставится ✓ 16.11
- **[browser-use](https://affpapa.org/nevibecode/skills/browser-use)** — Скилл browser-use для Claude Code управляет браузером через Chrome DevTools Protocol. Автоматизирует клики, заполнение форм, снятие скриншотов и сбор данных со страниц с JavaScript.
  `npx skills add browser-use/browser-use --skill browser-use -a claude-code` · [исходник: browser-use/browser-use](https://github.com/browser-use/browser-use/blob/4b5b1b0aa0ab45a1d6a2a31984d37d3e748c0134/skills/browser-use/SKILL.md) · 99 800 установок · ставится ✓ 16.11
- **[playwright-cli](https://affpapa.org/nevibecode/skills/playwright-cli)** — Скилл playwright-cli для Claude Code управляет браузером, проверяет веб-страницы и работает с тестами Playwright. Агент подключает его для действий на странице и запуска браузерных проверок.
  `npx skills add microsoft/playwright-cli --skill playwright-cli -a claude-code` · [исходник: microsoft/playwright-cli](https://github.com/microsoft/playwright-cli/blob/c872a33cec77fa03c28fa7c6d1ad99d15d04ce42/skills/playwright-cli/SKILL.md) · 221 700 установок · ставится ✓ 16.11
- **[scrapling-official](https://affpapa.org/nevibecode/skills/scrapling-official)** — Скилл scrapling-official учит агента писать код на Scrapling: HTTP-запросы, stealth-браузер, обход Cloudflare, пауки и адаптивный парсер.
  `npx skills add D4Vinci/Scrapling --skill scrapling-official -a claude-code` · [исходник: d4vinci/scrapling](https://github.com/D4Vinci/Scrapling/blob/bb223f2f5fc8f743772751a5ce283ef7851ca6be/agent-skill/Scrapling-Skill/SKILL.md) · 6 900 установок
- **[ego-browser](https://affpapa.org/nevibecode/skills/ego-browser)** — Скилл ego-browser управляет браузером ego-lite для тестирования веб-приложений, кликов, ввода данных и снятия скриншотов. Включается при проверке сценариев в интерфейсе с авторизацией пользователя.
  `npx skills add citrolabs/ego-lite --skill ego-browser -a claude-code` · [исходник: citrolabs/ego-lite](https://github.com/citrolabs/ego-lite/blob/f499162d1b911ba9b320ed31b741dba7ebc2e4d6/skills/ego-browser/SKILL.md) · 18 400 установок
- **[opencli-browser](https://affpapa.org/nevibecode/skills/opencli-browser)** — Скилл opencli-browser управляет Chrome через OpenCLI: читает страницы, работает с авторизованными сайтами и собирает данные о сетевых запросах.
  `npx skills add jackwener/OpenCLI --skill opencli-browser -a claude-code` · [исходник: jackwener/opencli](https://github.com/jackwener/OpenCLI/blob/9bc5f5ca132ec4d4e48d7ee517d4303bf159e8e8/skills/opencli-browser/SKILL.md) · 20 800 установок
- **[browser-act](https://affpapa.org/nevibecode/skills/browser-act)** — Скилл browser-act подключает к агенту браузерный CLI: открыть страницу, дождаться JavaScript, вытащить данные, заполнить форму, снять скриншот. Пригодится там, где обычного fetch не хватает.
  `npx skills add browser-act/skills --skill browser-act -a claude-code` · [исходник: browser-act/skills](https://github.com/browser-act/skills/blob/593316aa0f8ccd88bdf745c92b24a50641701973/browser-act/SKILL.md) · 108 500 установок
- **[opencli-autofix](https://affpapa.org/nevibecode/skills/opencli-autofix)** — Скилл opencli-autofix чинит упавшие адаптеры OpenCLI при смене DOM или API сайтов. Агент собирает трейс ошибки, находит новые селекторы через браузер и патчит код.
  `npx skills add jackwener/OpenCLI --skill opencli-autofix -a claude-code` · [исходник: jackwener/opencli](https://github.com/jackwener/OpenCLI/blob/9bc5f5ca132ec4d4e48d7ee517d4303bf159e8e8/skills/opencli-autofix/SKILL.md) · 18 100 установок
- **[browser-act-skill-forge](https://affpapa.org/nevibecode/skills/browser-act-skill-forge)** — Скилл browser-act-skill-forge разбирает сайт через browser-act и собирает готовый скилл с SKILL.md и Python-скриптами. Дальше сбор данных идёт без повторного исследования.
  `npx skills add browser-act/skills --skill browser-act-skill-forge -a claude-code` · [исходник: browser-act/skills](https://github.com/browser-act/skills/blob/593316aa0f8ccd88bdf745c92b24a50641701973/browser-act-skill-forge/SKILL.md) · 85 200 установок
- **[baoyu-url-to-markdown](https://affpapa.org/nevibecode/skills/baoyu-url-to-markdown)** — Скилл baoyu-url-to-markdown загружает веб-страницы через Chrome CDP и переводит контент в чистый Markdown. Включается при запросе на сохранение статей, веток обсуждений или расшифровок видео.
  `npx skills add JimLiu/baoyu-skills --skill baoyu-url-to-markdown -a claude-code` · [исходник: jimliu/baoyu-skills](https://github.com/JimLiu/baoyu-skills/blob/ca703c2d7c2c4399a1dc0cf82224f8551e05a96d/skills/baoyu-url-to-markdown/SKILL.md) · 30 900 установок

<a name="topic-mobile"></a>
## Мобильная разработка

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/mobile](https://affpapa.org/nevibecode/topic/mobile)

- **[vercel-react-native-skills](https://affpapa.org/nevibecode/skills/vercel-react-native-skills)** — Скилл vercel-react-native-skills для Claude Code и других агентов: правила React Native и Expo по спискам, анимациям и навигации. Держит правки мобильного кода в одном стиле.
  `npx skills add vercel-labs/agent-skills --skill vercel-react-native-skills -a claude-code` · [исходник: vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/react-native-skills/SKILL.md) · 283 800 установок
- **[write-swift](https://affpapa.org/nevibecode/skills/write-swift)** — Скилл write-swift для Claude Code помогает писать и разбирать современный Swift. Включается при создании, ревью или миграции Swift-кода, а также при поиске ошибок конкурентности и проблем с памятью.
  `npx skills add emilkowalski/skills --skill write-swift -a claude-code` · [исходник: emilkowalski/skills](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills/write-swift/SKILL.md) · 169 400 установок · ставится ✓ 16.11
- **[aso](https://affpapa.org/nevibecode/skills/aso)** — Скилл aso для Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI и OpenCode анализирует карточки мобильных приложений. Помогает подготовить аудит страницы в App Store и Google Play.
  `npx skills add coreyhaines31/marketingskills --skill aso -a claude-code` · [исходник: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/aso/SKILL.md) · 87 100 установок
- **[swiftui-pro](https://affpapa.org/nevibecode/skills/swiftui-pro)** — Скилл swiftui-pro для Claude Code проверяет код SwiftUI на ошибки, устаревшие API и проблемы с производительностью. Агент подключает его при чтении, написании или ревью проектов на SwiftUI.
  `npx skills add twostraws/SwiftUI-Agent-Skill --skill swiftui-pro -a claude-code` · [исходник: twostraws/swiftui-agent-skill](https://github.com/twostraws/SwiftUI-Agent-Skill/blob/f2920b63995263f57b3e198674e89a602efba6d2/swiftui-pro/SKILL.md) · 38 500 установок
- **[orca-emulator](https://affpapa.org/nevibecode/skills/orca-emulator)** — Скилл orca-emulator для Claude Code управляет запущенным iOS Simulator на macOS через Orca. Агент нажимает кнопки, вводит текст, меняет ориентацию и собирает данные дерева доступности.
  `npx skills add stablyai/orca --skill orca-emulator -a claude-code` · [исходник: stablyai/orca](https://github.com/stablyai/orca/blob/b30d12992e702724fffb426759c907d9b4450586/skills/orca-emulator/SKILL.md) · 6 300 установок
- **[orca-emulator-android](https://affpapa.org/nevibecode/skills/orca-emulator-android)** — Скилл orca-emulator-android для Claude Code управляет Android-устройством или эмулятором через adb. Запускается для действий в приложении и проверки его состояния.
  `npx skills add stablyai/orca --skill orca-emulator-android -a claude-code` · [исходник: stablyai/orca](https://github.com/stablyai/orca/blob/b30d12992e702724fffb426759c907d9b4450586/skills/orca-emulator-android/SKILL.md) · 6 000 установок
- **[swiftui-expert-skill](https://affpapa.org/nevibecode/skills/swiftui-expert-skill)** — Скилл swiftui-expert-skill для Claude Code, Codex, Cursor и других ИИ-ассистентов. Подключает правила ревью, оптимизации верстки и анализа трейсов Instruments при разработке на SwiftUI под iOS и macOS.
  `npx skills add AvdLee/SwiftUI-Agent-Skill --skill swiftui-expert-skill -a claude-code` · [исходник: avdlee/swiftui-agent-skill](https://github.com/AvdLee/SwiftUI-Agent-Skill/blob/62bd760f005093d1e2e4de5db156e456a5f96400/skills/swiftui-expert-skill/SKILL.md) · 36 800 установок
- **[android-clean-architecture](https://affpapa.org/nevibecode/skills/android-clean-architecture)** — Скилл android-clean-architecture подсказывает агенту, как раскладывать Android- и KMP-проект по слоям: модули, зависимости, UseCase, репозитории, работа с Room, SQLDelight и Ktor.
  `npx skills add affaan-m/ECC --skill android-clean-architecture -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/android-clean-architecture/SKILL.md) · 6 900 установок
- **[liquid-glass-design](https://affpapa.org/nevibecode/skills/liquid-glass-design)** — Скилл liquid-glass-design для Claude Code подсказывает, как собирать интерфейсы в стиле Liquid Glass из iOS 26. Описывает паттерны для SwiftUI, UIKit и WidgetKit под iOS 26+.
  `npx skills add affaan-m/ECC --skill liquid-glass-design -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/liquid-glass-design/SKILL.md) · 6 900 установок
- **[kotlin-coroutines-flows](https://affpapa.org/nevibecode/skills/kotlin-coroutines-flows)** — Скилл kotlin-coroutines-flows подсказывает паттерны Kotlin Coroutines и Flow для Android и KMP. Пригодится при отладке отмены, параллельных задач и тестов.
  `npx skills add affaan-m/ECC --skill kotlin-coroutines-flows -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/kotlin-coroutines-flows/SKILL.md) · 6 400 установок

<a name="topic-gamedev"></a>
## Геймдев и 3D: Unity, Unreal, Godot, Blender

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/gamedev](https://affpapa.org/nevibecode/topic/gamedev)

- **[gcode](https://affpapa.org/nevibecode/skills/gcode)** — Слайсит модели .stl, .3mf и .obj в .gcode или .gcode.3mf через OrcaSlicer. Принтер скилл не подключает.
  `npx skills add earthtojake/text-to-cad --skill gcode -a claude-code` · [исходник: earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad/blob/4d42cb0bd9a61b46254bc8cf9bd9ae1f45c3295b/skills/gcode/SKILL.md) · 10 500 установок
- **[bambu-labs](https://affpapa.org/nevibecode/skills/bambu-labs)** — Скилл bambu-labs передаёт файл на печать в принтеры Bambu Lab через Bambu Connect или Bambu Studio. Агент открывает файл в приложении, а принтер и запуск печати выбирает уже человек.
  `npx skills add earthtojake/text-to-cad --skill bambu-labs -a claude-code` · [исходник: earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad/blob/4d42cb0bd9a61b46254bc8cf9bd9ae1f45c3295b/skills/bambu-labs/SKILL.md) · 10 200 установок
- **[img2threejs](https://affpapa.org/nevibecode/skills/img2threejs)** — Скилл img2threejs для Claude Code собирает процедурную модель Three.js по изображению объекта или персонажа. Используется для реконструкции, подготовки модели к анимации и генерации кода.
  `npx skills add img2threejs/img2threejs --skill img2threejs -a claude-code` · [исходник: img2threejs/img2threejs](https://github.com/img2threejs/img2threejs/blob/0c0c49bc168e648dbaf9c8c080474de0b3a941b6/SKILL.md) · 3 100 установок
- **[dfam-check](https://affpapa.org/nevibecode/skills/dfam-check)** — Скилл dfam-check проверяет 3D-сетки на соответствие правилам аддитивного производства перед печатью. Анализирует толщину стенок, свесы и ориентацию деталей для FDM, SLS, SLA, PBF и MJF.
  `npx skills add earthtojake/text-to-cad --skill dfam-check -a claude-code` · [исходник: earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad/blob/4d42cb0bd9a61b46254bc8cf9bd9ae1f45c3295b/skills/dfam-check/SKILL.md) · 5 200 установок
- **[threejs-geometry](https://affpapa.org/nevibecode/skills/threejs-geometry)** — Скилл threejs-geometry учит ИИ-агента создавать стандартные и процедурные геометрии three.js, настраивать буферные атрибуты и генерировать 3D-текст.
  `npx skills add CloudAI-X/threejs-skills --skill threejs-geometry -a claude-code` · [исходник: cloudai-x/threejs-skills](https://github.com/CloudAI-X/threejs-skills/blob/0e181866f095b5f06d005133876e926515390d95/skills/threejs-geometry/SKILL.md) · 20 600 установок
- **[threejs-lighting](https://affpapa.org/nevibecode/skills/threejs-lighting)** — Скилл threejs-lighting для Claude Code помогает настроить освещение в Three.js. Он включается при добавлении источников света, настройке теней и работе с HDR-окружением.
  `npx skills add CloudAI-X/threejs-skills --skill threejs-lighting -a claude-code` · [исходник: cloudai-x/threejs-skills](https://github.com/CloudAI-X/threejs-skills/blob/0e181866f095b5f06d005133876e926515390d95/skills/threejs-lighting/SKILL.md) · 19 400 установок
- **[game-feel](https://affpapa.org/nevibecode/skills/game-feel)** — Скилл game-feel для Claude Code добавляет сочности игровая механика вроде покачивания камеры, хитстопа и деформации сплющиванием. Запускается, когда прыжки и удары кажутся вялыми.
  `npx skills add gamedev-skills/awesome-gamedev-agent-skills --skill game-feel -a claude-code` · [исходник: gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/disciplines/game-feel/SKILL.md) · 17 800 установок
- **[game-ui-ux](https://affpapa.org/nevibecode/skills/game-ui-ux)** — Скилл game-ui-ux для Claude Code задаёт правила компоновки игровых меню и HUD. Подключается при создании экранов или исправлении масштабирования и навигации с геймпада.
  `npx skills add gamedev-skills/awesome-gamedev-agent-skills --skill game-ui-ux -a claude-code` · [исходник: gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/disciplines/game-ui-ux/SKILL.md) · 17 700 установок
- **[fal-3d](https://affpapa.org/nevibecode/skills/fal-3d)** — Скилл fal-3d для Claude Code создаёт 3D-модели по тексту и изображениям через fal.ai. Создаёт игровые ассеты, AR-превью, прототипы товаров и концепты.
  `npx skills add nexu-io/open-design --skill fal-3d -a claude-code` · [исходник: nexu-io/open-design](https://github.com/nexu-io/open-design/blob/59e4f2ae85de7e7318a5e6bdcf3a34584c4b7582/skills/fal-3d/SKILL.md) · 3 000 установок
- **[shader-dev](https://affpapa.org/nevibecode/skills/minimax-ai-shader-dev)** — Скилл shader-dev для Claude Code содержит руководства по 36 техникам GLSL и генерирует шейдеры для ShaderToy и WebGL2. Техники охватывают процедурное 3D, рей-марчинг и визуальные эффекты в коде.
  `npx skills add MiniMax-AI/skills --skill shader-dev -a claude-code` · [исходник: minimax-ai/skills](https://github.com/MiniMax-AI/skills/blob/02853d885acb1abc157477ce00c4d98a8ed14a71/skills/shader-dev/SKILL.md) · 2 800 установок

<a name="topic-science"></a>
## Наука и исследования

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/science](https://affpapa.org/nevibecode/topic/science)

- **[academic-paper](https://affpapa.org/nevibecode/skills/academic-paper)** — Скилл academic-paper запускает конвейер из 12 субагентов для написания научных статей в Claude Code.
  `npx skills add Imbad0202/academic-research-skills --skill academic-paper -a claude-code` · [исходник: imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills/blob/23bd688bbc121da6ae98ec3c4d4a7675cefc4c83/academic-paper/SKILL.md) · 11 600 установок
- **[nature-figure](https://affpapa.org/nevibecode/skills/nature-figure)** — Скилл nature-figure для Claude Code создаёт, правит и проверяет научные рисунки на Python или R. Он подключается к задачам с графиками для рукописей, многочастными фигурами и схемами.
  `npx skills add Yuan1z0825/nature-skills --skill nature-figure -a claude-code` · [исходник: yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills/blob/14ca69710cae192325395a380e9cdd4ae5d9d0c8/skills/nature-figure/SKILL.md) · 20 300 установок
- **[academic-paper-reviewer](https://affpapa.org/nevibecode/skills/academic-paper-reviewer)** — Скилл academic-paper-reviewer для Claude Code имитирует коллегиальную проверку научной статьи через пять ролей. Выполняет рецензирование, повторную проверку правок и оценку методологии.
  `npx skills add Imbad0202/academic-research-skills --skill academic-paper-reviewer -a claude-code` · [исходник: imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills/blob/23bd688bbc121da6ae98ec3c4d4a7675cefc4c83/academic-paper-reviewer/SKILL.md) · 10 600 установок
- **[nature-citation](https://affpapa.org/nevibecode/skills/nature-citation)** — Скилл nature-citation для Claude Code ищет и проверяет статьи Nature и семейства CNS в поддержку утверждений рукописи. Он связывает тезисы с источниками и готовит файл для менеджера библиографии.
  `npx skills add Yuan1z0825/nature-skills --skill nature-citation -a claude-code` · [исходник: yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills/blob/14ca69710cae192325395a380e9cdd4ae5d9d0c8/skills/nature-citation/SKILL.md) · 16 900 установок
- **[nature-academic-search](https://affpapa.org/nevibecode/skills/nature-academic-search)** — Скилл nature-academic-search для Claude Code ищет научные публикации, проверяет ссылки и собирает стратегии MeSH. Работает с источниками и файлами библиографии.
  `npx skills add Yuan1z0825/nature-skills --skill nature-academic-search -a claude-code` · [исходник: yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills/blob/14ca69710cae192325395a380e9cdd4ae5d9d0c8/skills/nature-academic-search/SKILL.md) · 16 700 установок
- **[deep-research](https://affpapa.org/nevibecode/skills/imbad0202-deep-research)** — Скилл deep-research запускает команду из 13 агентов для академического исследования по любой теме: от формулировки вопроса до готового отчёта в APA 7.0.
  `npx skills add Imbad0202/academic-research-skills --skill deep-research -a claude-code` · [исходник: imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills/blob/23bd688bbc121da6ae98ec3c4d4a7675cefc4c83/deep-research/SKILL.md) · 8 200 установок
- **[paper-context-resolver](https://affpapa.org/nevibecode/skills/paper-context-resolver)** — Скилл paper-context-resolver для Claude Code ищет в первоисточниках статьи недостающий факт для воспроизведения модели. Уточняет сплит, предобработку или протокол оценки, если README молчит.
  `npx skills add lllllllama/RigorPilot-Skills --skill paper-context-resolver -a claude-code` · [исходник: lllllllama/rigorpilot-skills](https://github.com/lllllllama/RigorPilot-Skills/blob/fb3ccdf5aa64b1fa5b1d0463e666a8bc8bc26e01/skills/paper-context-resolver/SKILL.md) · 499 800 установок
- **[read-arxiv-paper](https://affpapa.org/nevibecode/skills/read-arxiv-paper)** — Скилл read-arxiv-paper для Claude Code читает исходники статьи arXiv и готовит разбор в Markdown. Разбирает научную работу в контексте nanochat.
  `npx skills add karpathy/nanochat --skill read-arxiv-paper -a claude-code` · [исходник: karpathy/nanochat](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/.claude/skills/read-arxiv-paper/SKILL.md) · 2 900 установок
- **[ai-research-reproduction](https://affpapa.org/nevibecode/skills/ai-research-reproduction)** — Скилл ai-research-reproduction для Claude Code помогает воспроизвести запуск глубокого обучения по README репозитория. Он выбирает минимальную проверяемую цель и собирает результаты в repro_outputs/.
  `npx skills add lllllllama/RigorPilot-Skills --skill ai-research-reproduction -a claude-code` · [исходник: lllllllama/rigorpilot-skills](https://github.com/lllllllama/RigorPilot-Skills/blob/fb3ccdf5aa64b1fa5b1d0463e666a8bc8bc26e01/skills/ai-research-reproduction/SKILL.md) · 359 800 установок
- **[math-olympiad](https://affpapa.org/nevibecode/skills/math-olympiad)** — Скилл math-olympiad для Claude Code решает олимпиадные задачи и проверяет доказательства отдельным агентом. Он включается для задач IMO, Putnam, USAMO, AIME и вопросов о контрпримерах.
  `npx skills add anthropics/claude-plugins-official --skill math-olympiad -a claude-code` · [исходник: anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official/blob/b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6/plugins/math-olympiad/skills/math-olympiad/SKILL.md) · 4 024 установки

<a name="topic-git"></a>
## Git и GitHub

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/git](https://affpapa.org/nevibecode/topic/git)

- **[triage](https://affpapa.org/nevibecode/skills/triage)** — Скилл triage проводит issue и внешние PR через роли триажа, проверку и подготовку брифа для агента. Подойдёт мейнтейнеру, который разбирает очередь задач.
  `npx skills add mattpocock/skills --skill triage -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/triage/SKILL.md) · 990 453 установки · ставится ✓ 16.11
- **[git-guardrails-claude-code](https://affpapa.org/nevibecode/skills/git-guardrails-claude-code)** — Скилл git-guardrails-claude-code для Claude Code устанавливает хук, который блокирует опасные Git-команды до запуска. Он оставляет push и удаление изменений под контролем человека.
  `npx skills add mattpocock/skills --skill git-guardrails-claude-code -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/git-guardrails-claude-code/SKILL.md) · 499 069 установок · ставится ✓ 16.11
- **[using-git-worktrees](https://affpapa.org/nevibecode/skills/using-git-worktrees)** — Скилл using-git-worktrees готовит изолированное рабочее дерево перед доработкой или выполнением плана. Проверяет текущий репозиторий, выбирает нативные средства платформы либо Git.
  `npx skills add obra/superpowers --skill using-git-worktrees -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-git-worktrees/SKILL.md) · 217 153 установки · ставится ✓ 16.11
- **[finishing-a-development-branch](https://affpapa.org/nevibecode/skills/finishing-a-development-branch)** — Скилл finishing-a-development-branch проверяет тесты и помогает выбрать, как завершить работу в ветке: слить её, открыть Pull Request или оставить как есть.
  `npx skills add obra/superpowers --skill finishing-a-development-branch -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/finishing-a-development-branch/SKILL.md) · 214 439 установок · ставится ✓ 16.11
- **[caveman-commit](https://affpapa.org/nevibecode/skills/caveman-commit)** — Скилл caveman-commit для Claude Code и Codex формирует краткие коммит-сообщения по стандарту Conventional Commits. Держит суть изменений без лишних слов.
  `npx skills add JuliusBrussee/caveman --skill caveman-commit -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/a192894723a8f47e7f504c7b5041967ff1f18e55/skills/caveman-commit/SKILL.md) · 441 600 установок · ставится ✓ 16.11
- **[pr](https://affpapa.org/nevibecode/skills/pr)** — Помогает Claude Code собирать тело PR по заданной структуре: краткое резюме, доказательства и оценка риска слияния.
  `npx skills add mattpocock/skills --skill pr -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/pr/SKILL.md) · 167 125 установок · ставится ✓ 16.11
- **[git-workflow-and-versioning](https://affpapa.org/nevibecode/skills/git-workflow-and-versioning)** — Скилл git-workflow-and-versioning, который наводит порядок в git-процессе: атомарные коммиты, короткоживущие ветки, сообщения, объясняющие зачем, а не что. Включается при любом изменении кода, которое агент готовит к коммиту.
  `npx skills add addyosmani/agent-skills --skill git-workflow-and-versioning -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/git-workflow-and-versioning/SKILL.md) · 73 100 установок
- **[gh-fix-ci](https://affpapa.org/nevibecode/skills/openai-gh-fix-ci)** — Скилл gh-fix-ci находит упавшие проверки GitHub Actions в пулл-реквесте, собирает логи ошибок и готовит план исправлений. Скилл применяет правки только после подтверждения.
  `npx skills add openai/skills --skill gh-fix-ci -a claude-code` · [исходник: openai/skills](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/gh-fix-ci/SKILL.md) · 12 000 установок
- **[github](https://affpapa.org/nevibecode/skills/github)** — Скилл для работы с GitHub через CLI на Claude Code: просмотр и создание PR, управление issues, проверка статуса CI. Доступен также на Codex, Cursor, GitHub Copilot, Gemini CLI и OpenCode.
  `npx skills add openclaw/openclaw --skill github -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/github/SKILL.md) · 6 100 установок
- **[gh-issues](https://affpapa.org/nevibecode/skills/gh-issues)** — Скилл gh-issues находит GitHub issues, запускает фоновых агентов для исправлений и открывает PR. Подходит для потока от issue до готового pull request.
  `npx skills add openclaw/openclaw --skill gh-issues -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/gh-issues/SKILL.md) · 5 000 установок

<a name="topic-productivity"></a>
## Заметки, задачи и проекты

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/productivity](https://affpapa.org/nevibecode/topic/productivity)

- **[grill-me](https://affpapa.org/nevibecode/skills/grill-me)** — Скилл grill-me проводит жёсткое интервью по плану или дизайну, чтобы найти пробелы и уточнить решения. Подойдёт перед началом разработки.
  `npx skills add mattpocock/skills --skill grill-me -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/grill-me/SKILL.md) · 1 424 476 установок · ставится ✓ 16.11
- **[handoff](https://affpapa.org/nevibecode/skills/handoff)** — Скилл handoff собирает текущий диалог в документ передачи, чтобы другой агент продолжил работу с нужным контекстом. Нужен при смене сессии или исполнителя.
  `npx skills add mattpocock/skills --skill handoff -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/handoff/SKILL.md) · 1 038 491 установка · ставится ✓ 16.11
- **[grilling](https://affpapa.org/nevibecode/skills/grilling)** — Скилл grilling для Claude Code стресс-тестирует план, решение или идею сериями уточняющих вопросов. Помогает выявить допущения до начала работы.
  `npx skills add mattpocock/skills --skill grilling -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/grilling/SKILL.md) · 979 543 установки · ставится ✓ 16.11
- **[using-superpowers](https://affpapa.org/nevibecode/skills/using-superpowers)** — Скилл using-superpowers для Claude Code и Codex проверяет релевантные скиллы до любого ответа или действия агента. Задаёт единый порядок работы с задачами.
  `npx skills add obra/superpowers --skill using-superpowers -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-superpowers/SKILL.md) · 270 479 установок · ставится ✓ 16.11
- **[caveman-learn](https://affpapa.org/nevibecode/skills/caveman-learn)** — Скилл caveman-learn разбирает отчёт Caveman, предлагает сокращение затрат на токены и просит согласие перед каждым изменением. Подходит для тяжёлого CLAUDE.md и повторяемого контекста.
  `npx skills add JuliusBrussee/caveman --skill caveman-learn -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/a192894723a8f47e7f504c7b5041967ff1f18e55/skills/caveman-learn/SKILL.md) · 130 900 установок · ставится ✓ 16.11
- **[lean-build](https://affpapa.org/nevibecode/skills/lean-build)** — Скилл lean-build удерживает агента от усложнения архитектуры при создании новых фич и интеграций. Скилл формулирует критерии приёмки, убирает лишний код и останавливает работу по факту проверки.
  `npx skills add JuliusBrussee/caveman --skill lean-build -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/a192894723a8f47e7f504c7b5041967ff1f18e55/skills/lean-build/SKILL.md) · 128 500 установок · ставится ✓ 16.11
- **[planning-and-task-breakdown](https://affpapa.org/nevibecode/skills/planning-and-task-breakdown)** — Скилл planning-and-task-breakdown разбивает спецификацию на небольшие проверяемые задачи с явными критериями приемки. Помогает агенту спланировать архитектуру до написания кода и избежать путаницы.
  `npx skills add addyosmani/agent-skills --skill planning-and-task-breakdown -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/planning-and-task-breakdown/SKILL.md) · 77 900 установок
- **[obsidian-cli](https://affpapa.org/nevibecode/skills/obsidian-cli)** — Скилл obsidian-cli для Claude Code управляет заметками и поиском в хранилище Obsidian через CLI. Также помогает разрабатывать и отлаживать плагины и темы.
  `npx skills add obsidianmd/obsidian-skills --skill obsidian-cli -a claude-code` · [исходник: obsidianmd/obsidian-skills](https://github.com/obsidianmd/obsidian-skills/blob/398127736bd4ba42d767b1419fee1a927508370b/plugins/obsidian/skills/obsidian-cli/SKILL.md) · 83 700 установок
- **[obsidian-bases](https://affpapa.org/nevibecode/skills/obsidianmd-obsidian-bases)** — Скилл obsidian-bases для Claude Code создаёт и редактирует файлы .base для Obsidian. Запускается при работе с базами заметок, таблицами, карточками, канбан-досками, фильтрами и формулами.
  `npx skills add obsidianmd/obsidian-skills --skill obsidian-bases -a claude-code` · [исходник: obsidianmd/obsidian-skills](https://github.com/obsidianmd/obsidian-skills/blob/398127736bd4ba42d767b1419fee1a927508370b/plugins/obsidian/skills/obsidian-bases/SKILL.md) · 83 600 установок
- **[incremental-implementation](https://affpapa.org/nevibecode/skills/incremental-implementation)** — Скилл incremental-implementation ограничивает работу агента небольшими проверяемыми шагами вместо одной массивной правки. Пригодится при изменениях в нескольких файлах или внедрении фич через feature flags.
  `npx skills add addyosmani/agent-skills --skill incremental-implementation -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/incremental-implementation/SKILL.md) · 75 300 установок

<a name="topic-finance"></a>
## Финансы и бизнес

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/finance](https://affpapa.org/nevibecode/topic/finance)

- **[market-research](https://affpapa.org/nevibecode/skills/affaan-m-market-research)** — Скилл market-research для Claude Code и Codex: задаёт рамки рыночных исследований, сравнения конкурентов и проверки инвесторов. Обосновывает решение, а не собирает отчёт.
  `npx skills add affaan-m/ECC --skill market-research -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/market-research/SKILL.md) · 7 600 установок
- **[investor-materials](https://affpapa.org/nevibecode/skills/investor-materials)** — Скилл investor-materials помогает готовить питч-деки, ванпейджеры, финмодели и заявки в акселераторы. Следит за тем, чтобы метрики и суммы сходились во всех документах раунда.
  `npx skills add affaan-m/ECC --skill investor-materials -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/investor-materials/SKILL.md) · 6 200 установок
- **[customs-trade-compliance](https://affpapa.org/nevibecode/skills/customs-trade-compliance)** — Скилл customs-trade-compliance классифицирует товары по кодам ТН ВЭД (HS/HTS), проверяет санкционные списки и готовит таможенные документы для США, ЕС и Великобритании.
  `npx skills add affaan-m/ECC --skill customs-trade-compliance -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/customs-trade-compliance/SKILL.md) · 5 900 установок
- **[earnings-analysis](https://affpapa.org/nevibecode/skills/earnings-analysis)** — Скилл earnings-analysis для Claude Code, Codex, Cursor, Copilot, Gemini CLI и OpenCode создаёт отчёты по квартальным результатам компаний из equity research: 8–12 страниц, таблицы, графики, анализ beat/miss.
  `npx skills add anthropics/financial-services --skill earnings-analysis -a claude-code` · [исходник: anthropics/financial-services](https://github.com/anthropics/financial-services/blob/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f/plugins/agent-plugins/earnings-reviewer/skills/earnings-analysis/SKILL.md) · 3 700 установок
- **[equity-research](https://affpapa.org/nevibecode/skills/equity-research)** — Скилл equity-research для Claude Code, Codex, Cursor и других IDE берёт данные из MCP-инструментов и собирает структурированный инвестиционный снапшот по акции.
  `npx skills add anthropics/financial-services --skill equity-research -a claude-code` · [исходник: anthropics/financial-services](https://github.com/anthropics/financial-services/blob/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f/plugins/partner-built/lseg/skills/equity-research/SKILL.md) · 3 400 установок
- **[consulting-analysis](https://affpapa.org/nevibecode/skills/consulting-analysis)** — Скилл consulting-analysis для Claude Code и Codex, который готовит консалтинговые отчёты в Markdown в два этапа. Сначала строит план исследования и список данных, потом сводит собранные факты и графики в текст.
  `npx skills add bytedance/deer-flow --skill consulting-analysis -a claude-code` · [исходник: bytedance/deer-flow](https://github.com/bytedance/deer-flow/blob/c18df580f61aa104d823ecbd0e7b362576eb7395/skills/public/consulting-analysis/SKILL.md) · 3 100 установок
- **[financial-statements](https://affpapa.org/nevibecode/skills/financial-statements)** — Скилл financial-statements для Claude Code формирует финансовые отчёты с сопоставлением периодов и анализом отклонений. Формирует P&L для закрытия периода и сравнения факта с бюджетом.
  `npx skills add anthropics/knowledge-work-plugins --skill financial-statements -a claude-code` · [исходник: anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/finance/skills/financial-statements/SKILL.md) · 4 800 установок
- **[backtesting-frameworks](https://affpapa.org/nevibecode/skills/backtesting-frameworks)** — Скилл backtesting-frameworks для Claude Code помогает строить бэктесты торговых стратегий с учётом смещения заглядывания в будущее, выживших активов и торговых издержек. Проверяет стратегии на исторических данных.
  `npx skills add wshobson/agents --skill backtesting-frameworks -a claude-code` · [исходник: wshobson/agents](https://github.com/wshobson/agents/blob/4bde3168b43c0655c4d00ea2726e631719908a6d/plugins/quantitative-trading/skills/backtesting-frameworks/SKILL.md) · 16 710 установок
- **[dcf-model](https://affpapa.org/nevibecode/skills/dcf-model)** — Скилл dcf-model строит институциональную DCF-модель для оценки компании: берёт данные из отчётности SEC и аналитических отчётов, считает WACC и денежные потоки, выдаёт Excel с анализом чувствительности.
  `npx skills add anthropics/financial-services --skill dcf-model -a claude-code` · [исходник: anthropics/financial-services](https://github.com/anthropics/financial-services/blob/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f/plugins/agent-plugins/model-builder/skills/dcf-model/SKILL.md) · 2 700 установок
- **[reconciliation](https://affpapa.org/nevibecode/skills/reconciliation)** — Скилл reconciliation для Claude Code сверяет остатки GL с субледжером, банковской выпиской или данными третьей стороны и помогает находить расхождения.
  `npx skills add anthropics/knowledge-work-plugins --skill reconciliation -a claude-code` · [исходник: anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/finance/skills/reconciliation/SKILL.md) · 3 700 установок

<a name="topic-languages"></a>
## Языки программирования

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/languages](https://affpapa.org/nevibecode/topic/languages)

- **[typescript-advanced-types](https://affpapa.org/nevibecode/skills/typescript-advanced-types)** — Скилл typescript-advanced-types для Claude Code помогает агенту писать сложную типизацию TypeScript: generics, conditional types и преобразования типов. Используется при работе над библиотеками, API-клиентами и строгими конфигурациями.
  `npx skills add wshobson/agents --skill typescript-advanced-types -a claude-code` · [исходник: wshobson/agents](https://github.com/wshobson/agents/blob/9c61ab243def98f72da12abd41cfcf5bcd91af9d/plugins/javascript-typescript/skills/typescript-advanced-types/SKILL.md) · 92 169 установок
- **[python-patterns](https://affpapa.org/nevibecode/skills/affaan-m-python-patterns)** — Скилл python-patterns подсказывает агенту, как писать и ревьюить Python: идиомы, аннотации типов, обработка исключений, контекстные менеджеры.
  `npx skills add affaan-m/ECC --skill python-patterns -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/python-patterns/SKILL.md) · 7 200 установок
- **[golang-patterns](https://affpapa.org/nevibecode/skills/golang-patterns)** — Скилл golang-patterns для Claude Code и других платформ подсказывает идиоматичные паттерны Go при написании, ревью и рефакторинге кода. Проверяет структуру пакета и обработку ошибок.
  `npx skills add affaan-m/ECC --skill golang-patterns -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/golang-patterns/SKILL.md) · 6 900 установок
- **[cpp-coding-standards](https://affpapa.org/nevibecode/skills/cpp-coding-standards)** — Скилл cpp-coding-standards для ИИ-агентов, который подтягивает написание и ревью C++ к C++ Core Guidelines: RAII, иммутабельность, строгая типизация.
  `npx skills add affaan-m/ECC --skill cpp-coding-standards -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/cpp-coding-standards/SKILL.md) · 6 700 установок
- **[python-performance-optimization](https://affpapa.org/nevibecode/skills/python-performance-optimization)** — Скилл python-performance-optimization помогает профилировать Python-код, находить узкие места CPU и памяти. Подходит, когда приложение медленно отвечает или тратит слишком много ресурсов.
  `npx skills add wshobson/agents --skill python-performance-optimization -a claude-code` · [исходник: wshobson/agents](https://github.com/wshobson/agents/blob/4bde3168b43c0655c4d00ea2726e631719908a6d/plugins/python-development/skills/python-performance-optimization/SKILL.md) · 35 675 установок
- **[design-patterns](https://affpapa.org/nevibecode/skills/design-patterns)** — Скилл design-patterns подбирает архитектурные паттерны Rust для CLI-модулей фильтрации RTK. Помогает структурировать парсеры вывода, конфигурации и работу с ресурсами.
  `npx skills add rtk-ai/rtk --skill design-patterns -a claude-code` · [исходник: rtk-ai/rtk](https://github.com/rtk-ai/rtk/blob/3ab08beca3f4d7a2d5b9f0f494e13ce1d5e81fb2/.claude/skills/design-patterns/SKILL.md) · 2 000 установок
- **[python-design-patterns](https://affpapa.org/nevibecode/skills/python-design-patterns)** — Скилл python-design-patterns помогает выбирать структуру Python-кода, разделять обязанности и решать, когда выносить повторяющуюся логику в абстракцию. Пригодится при проектировании и рефакторинге.
  `npx skills add wshobson/agents --skill python-design-patterns -a claude-code` · [исходник: wshobson/agents](https://github.com/wshobson/agents/blob/4bde3168b43c0655c4d00ea2726e631719908a6d/plugins/python-development/skills/python-design-patterns/SKILL.md) · 22 842 установки
- **[typescript-expert](https://affpapa.org/nevibecode/skills/typescript-expert)** — Скилл typescript-expert для Claude Code разбирает типы TypeScript, ускоряет проверку и помогает с миграциями; запускается на каждом PR и диагностирует медленную компиляцию.
  `npx skills add sickn33/agentic-awesome-skills --skill typescript-expert -a claude-code` · [исходник: sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills/blob/560b762c309d6b96315855d7968727d3bca7df20/skills/typescript-expert/SKILL.md) · 12 800 установок
- **[cardputer-buddy](https://affpapa.org/nevibecode/skills/cardputer-buddy)** — Скилл cardputer-buddy для Claude Code помогает менять MicroPython-приложения на Cardputer-Adv. Запускается при добавлении приложения, отправке файла на устройство или работе с его логами.
  `npx skills add anthropics/claude-plugins-official --skill cardputer-buddy -a claude-code` · [исходник: anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official/blob/b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6/plugins/cwc-makers/skills/cardputer-buddy/SKILL.md) · 2 897 установок
- **[swift-concurrency](https://affpapa.org/nevibecode/skills/swift-concurrency)** — Скилл swift-concurrency для Claude Code разбирает ошибки Swift Concurrency и предлагает безопасные исправления. Он включается при миграции на Swift 6 и работе с задачами, акторами и Sendable.
  `npx skills add AvdLee/Swift-Concurrency-Agent-Skill --skill swift-concurrency -a claude-code` · [исходник: avdlee/swift-concurrency-agent-skill](https://github.com/AvdLee/Swift-Concurrency-Agent-Skill/blob/3b1580d8398e0b5408b3bf0bada0e941a1cfc642/skills/swift-concurrency/SKILL.md) · 17 700 установок

<a name="topic-telegram"></a>
## Telegram-боты

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/telegram](https://affpapa.org/nevibecode/topic/telegram)

- **[telegram-bot-builder](https://affpapa.org/nevibecode/skills/sickn33-telegram-bot-builder)** — Скилл telegram-bot-builder помогает спроектировать Telegram-бота: от структуры проекта и кнопок до платежей и вебхуков. Пригодится при запуске нового бота или подготовке его к продакшену.
  `npx skills add sickn33/agentic-awesome-skills --skill telegram-bot-builder -a claude-code` · [исходник: sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills/blob/560b762c309d6b96315855d7968727d3bca7df20/skills/telegram-bot-builder/SKILL.md) · 3 800 установок
- **[telegram-bot](https://affpapa.org/nevibecode/skills/telegram-bot)** — Скилл telegram-bot для Claude Code и других платформ: чат-боты, уведомления, ИИ-ассистенты и автоматизация групп. Собирает обработчики сообщений и сценарии.
  `npx skills add claude-office-skills/skills --skill telegram-bot -a claude-code` · [исходник: claude-office-skills/skills](https://github.com/claude-office-skills/skills/blob/9c4c7d5cd2813a8936bf2c9fdb174ea883b85a11/telegram-bot/SKILL.md) · 6 500 установок
- **[tg-bot-binding](https://affpapa.org/nevibecode/skills/tg-bot-binding)** — Скилл tg-bot-binding помогает подключить Telegram-бота к Starchild, подтвердить владение и наладить отправку сообщений через сканирование QR-кода или токен BotFather.
  `npx skills add Starchild-ai-agent/official-skills --skill tg-bot-binding -a claude-code` · [исходник: starchild-ai-agent/official-skills](https://github.com/Starchild-ai-agent/official-skills/blob/d7df896c602f2f14b0c17d66727bc7510d84b48a/tg-bot-binding/SKILL.md) · 2 200 установок
- **[meta](https://affpapa.org/nevibecode/skills/meta)** — Регистрирует обработчик команды /meta, чтобы запускать Claude Code Agent SDK прямо в каталоге бота telegram_agent и править его код из чата.
  `npx skills add glebis/claude-skills --skill meta -a claude-code` · [исходник: glebis/claude-skills](https://github.com/glebis/claude-skills/blob/4d37d3b0af1f98cb4ac820d9abbce95e38e909fb/meta/SKILL.md) · 228 установок
- **[tg-ws-proxy-telegram-socks5](https://affpapa.org/nevibecode/skills/tg-ws-proxy-telegram-socks5)** — Скилл tg-ws-proxy-telegram-socks5 помогает настроить локальный SOCKS5-прокси для Telegram Desktop с туннелированием трафика в дата-центры через WebSocket. Пригодится при сетевых блокировках мессенджера.
  `npx skills add reason-machines/trending-skills --skill tg-ws-proxy-telegram-socks5 -a claude-code` · [исходник: reason-machines/trending-skills](https://github.com/reason-machines/trending-skills/blob/c61b1a456af4015e9a367e0245292281bb3c87d9/skills/tg-ws-proxy-telegram-socks5/SKILL.md) · 889 установок
- **[telegram-group-analytics-bot](https://affpapa.org/nevibecode/skills/telegram-group-analytics-bot)** — Скилл telegram-group-analytics-bot собирает статистику Telegram-группы: прирост участников, сообщения, активность по часам и автоматические отчёты.
  `npx skills add reason-machines/data-skills --skill telegram-group-analytics-bot -a claude-code` · [исходник: reason-machines/data-skills](https://github.com/reason-machines/data-skills/blob/25d6ee79eea935ef4be1ee375a5777b2ad259f0a/skills/telegram-group-analytics-bot/SKILL.md) · 615 установок
- **[telegram-group-statistics-analytics-bot](https://affpapa.org/nevibecode/skills/telegram-group-statistics-analytics-bot)** — Скилл telegram-group-statistics-analytics-bot настраивает бота для сбора метрик в группах Telegram, учёта активности участников и рассылки отчётов. Пригодится администраторам чатов для контроля вовлечённости.
  `npx skills add reason-machines/data-skills --skill telegram-group-statistics-analytics-bot -a claude-code` · [исходник: reason-machines/data-skills](https://github.com/reason-machines/data-skills/blob/25d6ee79eea935ef4be1ee375a5777b2ad259f0a/skills/telegram-group-statistics-analytics-bot/SKILL.md) · 610 установок
- **[interactive-bot](https://affpapa.org/nevibecode/skills/interactive-bot)** — Скилл interactive-bot объясняет устройство Telegram-бота Gmail Commander: слэш-команды для почты, ИИ-роутинг свободного текста через MCP, сессии compose/reply.
  `npx skills add terrylica/cc-skills --skill interactive-bot -a claude-code` · [исходник: terrylica/cc-skills](https://github.com/terrylica/cc-skills/blob/0ca36f7260a3eb5de13a1b684509c4ecd5fe819b/plugins/gmail-commander/skills/interactive-bot/SKILL.md) · 114 установок

## Обновление и лицензия

Список собирает `scripts/build.py` из базы каталога; снимок проверок — `data/checks-2026-11-16.json`. Сборка от 2026-11-20. Число установок — по данным источника, из которого карточка пришла в каталог. Описания скиллов написаны для каталога affpapa.org. Список и описания — [CC0 1.0](LICENSE). Сами скиллы — под лицензиями своих авторов, смотрите исходник.
