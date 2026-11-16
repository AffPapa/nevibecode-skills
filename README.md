# Скиллы для Claude Code, Codex и Cursor по темам

English: [README.en.md](README.en.md)

248 скиллов в 25 темах из каталога [NeVibeCode](https://affpapa.org/nevibecode) на affpapa.org. В каждой теме — самые популярные скиллы, у которых автоматическая проверка безопасности 16.11 не нашла предупреждений. У каждого скилла здесь команда установки, ссылка на карточку с описанием по-русски и ссылка на исходник.

Методика и цифры проверки — [affpapa.org/nevibecode/research](https://affpapa.org/nevibecode/research).

## Отметки

- **ставится ✓ 16.11** — команду из списка запустили в песочнице 16.11: скилл установился, SKILL.md на месте и проходит проверку формата. Проверяли 150 самых популярных скиллов каталога, рабочими по команде оказались 144. Здесь отметка стоит у 94 скиллов; у остальных установку не запускали.
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

- **[setup-matt-pocock-skills](https://affpapa.org/nevibecode/skills/setup-matt-pocock-skills)** — Скилл настраивает репозиторий для инженерных скиллов Matt Pocock: задаёт трекер задач, метки триажа и расположение доменной документации. Запустите его перед первым использованием остальных скиллов.
  `npx skills add mattpocock/skills --skill setup-matt-pocock-skills -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/setup-matt-pocock-skills/SKILL.md) · 1 052 851 установка · ставится ✓ 16.11
- **[ask-matt](https://affpapa.org/nevibecode/skills/ask-matt)** — Скилл для Claude Code, маршрутизирует задачу к нужному скиллу или рабочему потоку из набора Matt Pocock. Направляет от сырой идеи до разбора бага.
  `npx skills add mattpocock/skills --skill ask-matt -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/ask-matt/SKILL.md) · 766 587 установок · ставится ✓ 16.11
- **[to-tickets](https://affpapa.org/nevibecode/skills/to-tickets)** — Скилл для Claude Code разбивает план, спецификацию или переписку на небольшие сквозные задачи и помечает блокирующие зависимости. Запускается до публикации задач в трекере.
  `npx skills add mattpocock/skills --skill to-tickets -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/to-tickets/SKILL.md) · 711 230 установок · ставится ✓ 16.11
- **[brainstorming](https://affpapa.org/nevibecode/skills/brainstorming)** — Скилл проводит обсуждение с разработчиком перед началом реализации, уточняет требования и формирует дизайн-док. Запускается автоматически, когда запрос содержит неопределённость или предполагает новую функциональность.
  `npx skills add obra/superpowers --skill brainstorming -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/brainstorming/SKILL.md) · 404 045 установок · ставится ✓ 16.11
- **[systematic-debugging](https://affpapa.org/nevibecode/skills/systematic-debugging)** — Скилл для Claude Code и Codex, который запрещает агенту предлагать исправления до завершения анализа первопричины. Включается при любом падении теста, баге или неожиданном поведении — до того, как агент потянется к «быстрому фиксу».
  `npx skills add obra/superpowers --skill systematic-debugging -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/systematic-debugging/SKILL.md) · 306 118 установок · ставится ✓ 16.11
- **[writing-plans](https://affpapa.org/nevibecode/skills/writing-plans)** — Скилл для Claude Code и Codex создаёт детальный план реализации многошаговой задачи перед первой правкой кода. Запускается, когда у агента есть спецификация фичи или требования.
  `npx skills add obra/superpowers --skill writing-plans -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-plans/SKILL.md) · 282 859 установок · ставится ✓ 16.11
- **[mcp-builder](https://affpapa.org/nevibecode/skills/mcp-builder)** — Пошагово направляет агента при разработке серверов Model Context Protocol на TypeScript или Python. Помогает проектировать схемы инструментов, подключать API и тестировать транспорт.
  `npx skills add anthropics/skills --skill mcp-builder -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/mcp-builder/SKILL.md) · 130 949 установок · ставится ✓ 16.11
- **[orca-cli](https://affpapa.org/nevibecode/skills/orca-cli)** — Скилл для Claude Code, Codex и Cursor управляет контекстами Orca. Помогает запускать субагентов в отдельных worktree, читать терминалы и тестировать веб-страницы во встроенном браузере.
  `npx skills add stablyai/orca --skill orca-cli -a claude-code` · [исходник: stablyai/orca](https://github.com/stablyai/orca/blob/457c602b4f737d95dbdcf2f176f0beac8d9909b6/skills/orca-cli/SKILL.md) · 363 000 установок · ставится ✓ 16.11
- **[orchestration](https://affpapa.org/nevibecode/skills/orchestration)** — Скилл для Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI и OpenCode — запускает задачи в отдельных агентах Orca и возвращает результат обратно.
  `npx skills add stablyai/orca --skill orchestration -a claude-code` · [исходник: stablyai/orca](https://github.com/stablyai/orca/blob/457c602b4f737d95dbdcf2f176f0beac8d9909b6/skills/orchestration/SKILL.md) · 359 500 установок · ставится ✓ 16.11
- **[slideshow](https://affpapa.org/nevibecode/skills/slideshow)** — Скилл собирает в HyperFrames презентацию для показа в браузере: слайды, раскрытие фрагментов и переходы по интерактивным точкам. Он также помогает перенести существующую страницу в формат слайдов.
  `npx skills add heygen-com/hyperframes --skill slideshow -a claude-code` · [исходник: heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/blob/f207f612f1fba902d5c1480ea98a90c1469752e5/skills/slideshow/SKILL.md) · 532 000 установок · ставится ✓ 16.11

<a name="topic-frontend"></a>
## Фронтенд и UI

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/frontend](https://affpapa.org/nevibecode/topic/frontend)

- **[design-taste-frontend](https://affpapa.org/nevibecode/skills/design-taste-frontend)** — Скилл для Claude Code задаёт правила оформления и проверки сайтов. Подключается при создании или переделке страницы, а также при просьбе убрать шаблонный вид.
  `npx skills add Leonxlnx/taste-skill --skill design-taste-frontend -a claude-code` · [исходник: leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/blob/f6b76575f949707b4e3c37cd86cb44b0b98643e8/skills/taste-skill/SKILL.md) · 786 200 установок · A/B 16.11: -0,04 — эффекта нет, ~10 тыс. токенов на запрос
- **[prototype](https://affpapa.org/nevibecode/skills/prototype)** — Создаёт временный прототип, чтобы проверить логику, модель состояния или вид интерфейса до работы над основным кодом.
  `npx skills add mattpocock/skills --skill prototype -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/prototype/SKILL.md) · 986 201 установка · ставится ✓ 16.11
- **[hyperframes](https://affpapa.org/nevibecode/skills/heygen-com-hyperframes)** — Скилл для Claude Code управляет созданием, правкой и рендерингом видео из HTML через CLI HyperFrames. Задаёт контракт разметки, правила таймлайна и алгоритм сборки проекта.
  `npx skills add heygen-com/hyperframes --skill hyperframes -a claude-code` · [исходник: heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/blob/f207f612f1fba902d5c1480ea98a90c1469752e5/skills/hyperframes/SKILL.md) · 1 600 000 установок · ставится ✓ 16.11
- **[webapp-testing](https://affpapa.org/nevibecode/skills/webapp-testing)** — Скилл запускает проверки локальных веб-приложений через Playwright: помогает отлаживать UI, делать скриншоты и смотреть логи браузера.
  `npx skills add anthropics/skills --skill webapp-testing -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/webapp-testing/SKILL.md) · 186 758 установок · ставится ✓ 16.11
- **[web-artifacts-builder](https://affpapa.org/nevibecode/skills/web-artifacts-builder)** — Скилл для Claude Code и Claude.ai создаёт многокомпонентные HTML-артефакты на React, TypeScript, Tailwind CSS и shadcn/ui. Инициализирует проект через init-artifact.sh, собирает всё в один файл bundle.html скриптом bundle-artifact.sh.
  `npx skills add anthropics/skills --skill web-artifacts-builder -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/web-artifacts-builder/SKILL.md) · 112 122 установки · ставится ✓ 16.11
- **[remotion-to-hyperframes](https://affpapa.org/nevibecode/skills/remotion-to-hyperframes)** — Переносит анимации и видеокод из Remotion, Motion Canvas или Lottie в проект HyperFrames. Позволяет проверить результат покадровым сравнением с оригиналом через diff.
  `npx skills add heygen-com/hyperframes --skill remotion-to-hyperframes -a claude-code` · [исходник: heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/blob/f207f612f1fba902d5c1480ea98a90c1469752e5/skills/remotion-to-hyperframes/SKILL.md) · 627 200 установок · ставится ✓ 16.11
- **[shadcn](https://affpapa.org/nevibecode/skills/shadcn-ui-shadcn)** — Скилл ведёт агента по работе с shadcn/ui: добавляет компоненты, ищет в реестрах, чинит верстку и собирает дизайн-систему по вашему описанию.
  `npx skills add shadcn-ui/ui --skill shadcn -a claude-code` · [исходник: shadcn-ui/ui](https://github.com/shadcn-ui/ui/blob/e62c9435fff729a175f38983dee73b2cb4f6a069/skills/shadcn/SKILL.md) · 150 100 установок · ставится ✓ 16.11
- **[vercel-composition-patterns](https://affpapa.org/nevibecode/skills/vercel-composition-patterns)** — Свод правил, по которым агент переводит React-компоненты с Boolean props на compound components и общий контекст.
  `npx skills add vercel-labs/agent-skills --skill vercel-composition-patterns -a claude-code` · [исходник: vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/composition-patterns/SKILL.md) · 457 600 установок
- **[emil-design-eng](https://affpapa.org/nevibecode/skills/emil-design-eng)** — Скилл задаёт правила для полировки интерфейсов, компонентов и анимаций. Пригодится, когда UI работает, но требует более точных состояний и переходов.
  `npx skills add emilkowalski/skills --skill emil-design-eng -a claude-code` · [исходник: emilkowalski/skills](https://github.com/emilkowalski/skills/blob/715c1807e08c497cfd1dc4feb450a2a3300ef2a9/skills/emil-design-eng/SKILL.md) · 453 900 установок · ставится ✓ 16.11 · A/B 16.11: +0,46 — плюс на анимации и доступности
- **[review-animations](https://affpapa.org/nevibecode/skills/review-animations)** — Проверяет код интерфейсных анимаций по стандартам Эмила Ковальски. Находит проблемы с производительностью, плавностью и физикой переходов.
  `npx skills add emilkowalski/skills --skill review-animations -a claude-code` · [исходник: emilkowalski/skills](https://github.com/emilkowalski/skills/blob/715c1807e08c497cfd1dc4feb450a2a3300ef2a9/skills/review-animations/SKILL.md) · 313 500 установок · ставится ✓ 16.11

<a name="topic-backend"></a>
## Бэкенд и API

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/backend](https://affpapa.org/nevibecode/topic/backend)

- **[lark-im](https://affpapa.org/nevibecode/skills/lark-im)** — Скилл подключает Lark IM к агенту: он отправляет сообщения, ищет историю, управляет чатами и файлами. Подойдёт для задач вокруг командных коммуникаций.
  `npx skills add larksuite/cli --skill lark-im -a claude-code` · [исходник: larksuite/cli](https://github.com/larksuite/cli/blob/3d82c85419ad7560ad017db7a3972a596b5fbeb1/skills/lark-im/SKILL.md) · 490 400 установок · ставится ✓ 16.11
- **[api-and-interface-design](https://affpapa.org/nevibecode/skills/api-and-interface-design)** — Помогает проектировать API и границы модулей так, чтобы их было проще использовать и менять. Подходит для REST, GraphQL и публичных интерфейсов.
  `npx skills add addyosmani/agent-skills --skill api-and-interface-design -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/301b02b12bff98e4688e6984af6556802322bbde/skills/api-and-interface-design/SKILL.md) · 77 000 установок
- **[observability-and-instrumentation](https://affpapa.org/nevibecode/skills/observability-and-instrumentation)** — Скилл для Claude Code и других IDE, который учит ИИ писать инструментацию в код: структурированное логирование, метрики, трейсинг и корреляционные ID. Запускается при добавлении фич в продакшн, когда нужна видимость поведения системы.
  `npx skills add addyosmani/agent-skills --skill observability-and-instrumentation -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/301b02b12bff98e4688e6984af6556802322bbde/skills/observability-and-instrumentation/SKILL.md) · 68 100 установок
- **[gws-gmail-watch](https://affpapa.org/nevibecode/skills/gws-gmail-watch)** — Следит за новыми письмами Gmail и отдаёт события потоком NDJSON. Подходит для обработки входящей почты в агентных сценариях.
  `npx skills add googleworkspace/cli --skill gws-gmail-watch -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-gmail-watch/SKILL.md) · 38 600 установок
- **[api-security-testing](https://affpapa.org/nevibecode/skills/usestrix-api-security-testing)** — Скилл помогает проверить REST, GraphQL и gRPC API с помощью Strix: агенты ищут уязвимости и прикладывают запрос для проверки находки.
  `npx skills add usestrix/strix --skill api-security-testing -a claude-code` · [исходник: usestrix/strix](https://github.com/usestrix/strix/blob/4719329d1c3eb0db796714397551945c514a2301/skills/api-security-testing/SKILL.md) · 17 500 установок
- **[mcporter](https://affpapa.org/nevibecode/skills/mcporter)** — Скилл даёт агенту команды для работы с MCP-серверами и их инструментами через HTTP или stdio. Подойдёт для настройки, авторизации и вызова MCP.
  `npx skills add openclaw/openclaw --skill mcporter -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/f683d5ffd214c84d2b75d91b82cde3aabc05fab2/skills/mcporter/SKILL.md) · 6 300 установок
- **[goplaces](https://affpapa.org/nevibecode/skills/goplaces)** — Скилл для Claude Code запускает goplaces и ищет места через Google Places API, возвращает карточки и отзывы.
  `npx skills add openclaw/openclaw --skill goplaces -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/f683d5ffd214c84d2b75d91b82cde3aabc05fab2/skills/goplaces/SKILL.md) · 5 400 установок
- **[xurl](https://affpapa.org/nevibecode/skills/xurl)** — Скилл для работы с CLI-утилитой xurl. Позволяет публиковать посты, читать ленту, загружать медиа и отправлять запросы к API X прямо из сессии агента.
  `npx skills add openclaw/openclaw --skill xurl -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/f683d5ffd214c84d2b75d91b82cde3aabc05fab2/skills/xurl/SKILL.md) · 4 900 установок
- **[wrangler](https://affpapa.org/nevibecode/skills/cloudflare-wrangler)** — Помогает запускать команды Wrangler CLI, настраивать конфигурации и отлаживать деплой Cloudflare Workers в существующих проектах.
  `npx skills add cloudflare/skills --skill wrangler -a claude-code` · [исходник: cloudflare/skills](https://github.com/cloudflare/skills/blob/cbf893b954222276bf1af57e5f23379231e0efb9/skills/wrangler/SKILL.md) · 149 600 установок
- **[backend-patterns](https://affpapa.org/nevibecode/skills/backend-patterns)** — Скилл с паттернами бэкенда для Node.js, Express и Next.js API routes: слои, кэш, транзакции, обработка ошибок.
  `npx skills add affaan-m/ECC --skill backend-patterns -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/backend-patterns/SKILL.md) · 7 700 установок

<a name="topic-design"></a>
## Дизайн

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/design](https://affpapa.org/nevibecode/topic/design)

- **[frontend-design](https://affpapa.org/nevibecode/skills/frontend-design)** — Скилл задаёт осмысленное визуальное направление для новых интерфейсов и редизайна. Подойдёт, когда стандартный шаблонный UI не устраивает.
  `npx skills add anthropics/skills --skill frontend-design -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/frontend-design/SKILL.md) · 1 025 790 установок · ставится ✓ 16.11 · A/B 16.11: +0,08 — в пределах шума
- **[codebase-design](https://affpapa.org/nevibecode/skills/codebase-design)** — Скилл помогает проектировать модули с небольшим интерфейсом и скрытой внутри сложностью. Подходит для рефакторинга, тестируемости и поиска чистого seam.
  `npx skills add mattpocock/skills --skill codebase-design -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/codebase-design/SKILL.md) · 850 344 установки · ставится ✓ 16.11
- **[hyperframes-cli](https://affpapa.org/nevibecode/skills/heygen-com-hyperframes-cli)** — Скилл для Claude Code управляет проектами HyperFrames через CLI: проверяет кадры, меняет таймлайн и рендерит видео. Запускается на задачах по созданию и правке роликов в HyperFrames.
  `npx skills add heygen-com/hyperframes --skill hyperframes-cli -a claude-code` · [исходник: heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/blob/f207f612f1fba902d5c1480ea98a90c1469752e5/skills/hyperframes-cli/SKILL.md) · 1 600 000 установок · ставится ✓ 16.11
- **[hyperframes-registry](https://affpapa.org/nevibecode/skills/heygen-com-hyperframes-registry)** — Скилл ищет и добавляет редактируемые HyperFrames-блоки для переходов, титров, субтитров, графиков и 3D-сцен. Поиск запускается перед ручной сборкой визуального эффекта.
  `npx skills add heygen-com/hyperframes --skill hyperframes-registry -a claude-code` · [исходник: heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/blob/f207f612f1fba902d5c1480ea98a90c1469752e5/skills/hyperframes-registry/SKILL.md) · 1 300 000 установок · ставится ✓ 16.11
- **[impeccable](https://affpapa.org/nevibecode/skills/impeccable)** — Скилл для Claude Code и других агентов: проектирует и переделывает интерфейсы — лендинги, дашборды, формы, экраны iOS и Android. Приводит вёрстку в порядок по правилам дизайна.
  `npx skills add pbakaus/impeccable --skill impeccable -a claude-code` · [исходник: pbakaus/impeccable](https://github.com/pbakaus/impeccable/blob/ec229b48547f24685ffb22aa51c462c5ae27908c/cursor-plugin/skills/impeccable/SKILL.md) · 412 300 установок
- **[ui-ux-pro-max](https://affpapa.org/nevibecode/skills/ui-ux-pro-max)** — Скилл для Claude Code и ещё пяти платформ: подключает к агенту локальную базу UX-правил, цветовых палитр и пар шрифтов для проектирования интерфейсов. Поиск идёт через Python-скрипт.
  `npx skills add nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max -a claude-code` · [исходник: nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/4f2dbb67e64969a9a30ab00742f2d55d66ddec2b/.claude/skills/ui-ux-pro-max/SKILL.md) · 455 100 установок · ставится ✓ 16.11
- **[canvas-design](https://affpapa.org/nevibecode/skills/canvas-design)** — Скилл для Claude Code и Claude.ai, который создаёт визуальный арт в .png и .pdf. Включается, когда нужен постер, графический дизайн или статичная работа без готового макета.
  `npx skills add anthropics/skills --skill canvas-design -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/canvas-design/SKILL.md) · 121 543 установки · ставится ✓ 16.11
- **[brand-guidelines](https://affpapa.org/nevibecode/skills/brand-guidelines)** — Скилл для Claude Code применяет фирменные цвета и шрифты Anthropic к документам, презентациям и другим артефактам.
  `npx skills add anthropics/skills --skill brand-guidelines -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/brand-guidelines/SKILL.md) · 109 043 установки · ставится ✓ 16.11
- **[hallmark](https://affpapa.org/nevibecode/skills/hallmark)** — Скилл для Claude Code и других агентов: заставляет сгенерированные интерфейсы выглядеть сделанными, а не сгенерированными. Собирает новые страницы и сайты по жёстким правилам вёрстки.
  `npx skills add Nutlope/hallmark --skill hallmark -a claude-code` · [исходник: nutlope/hallmark](https://github.com/Nutlope/hallmark/blob/04977e15f3dfd6ee4b74c887dac3eb52665d6c92/skills/hallmark/SKILL.md) · 109 000 установок · ставится ✓ 16.11
- **[apple-design](https://affpapa.org/nevibecode/skills/apple-design)** — Переносит принципы физического интерфейса Apple с докладов WWDC в веб на CSS, Pointer Events и Motion. Пригодится при верстке жестов, шторки и прерываемых пружин.
  `npx skills add emilkowalski/skills --skill apple-design -a claude-code` · [исходник: emilkowalski/skills](https://github.com/emilkowalski/skills/blob/715c1807e08c497cfd1dc4feb450a2a3300ef2a9/skills/apple-design/SKILL.md) · 305 400 установок · ставится ✓ 16.11

<a name="topic-testing"></a>
## Тесты и QA

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/testing](https://affpapa.org/nevibecode/topic/testing)

- **[tdd](https://affpapa.org/nevibecode/skills/tdd)** — Скилл управляет циклом красный-зелёный в TDD: проверяет, что тесты пишутся до кода, держит их на уровне публичных интерфейсов и не завязывает на внутреннюю структуру.
  `npx skills add mattpocock/skills --skill tdd -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/tdd/SKILL.md) · 1 141 062 установки · ставится ✓ 16.11 · A/B 16.11: -1,33 — у GPT ломал ответ
- **[diagnosing-bugs](https://affpapa.org/nevibecode/skills/diagnosing-bugs)** — Скилл Claude Code строит воспроизводимый тестовый цикл для разбора сложных ошибок и просадок производительности. Разбирает падения, неверный вывод и медленную работу проекта.
  `npx skills add mattpocock/skills --skill diagnosing-bugs -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/diagnosing-bugs/SKILL.md) · 834 802 установки · ставится ✓ 16.11 · A/B 16.11: +0,31 — помог Claude
- **[implement](https://affpapa.org/nevibecode/skills/implement)** — Выполняет задачу по спецификации или тикетам, ведёт работу через тесты и завершает её ревью с коммитом. Подходит для задач, где нужен дисциплинированный цикл разработки.
  `npx skills add mattpocock/skills --skill implement -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/implement/SKILL.md) · 774 700 установок · ставится ✓ 16.11
- **[verification-before-completion](https://affpapa.org/nevibecode/skills/verification-before-completion)** — Скилл запрещает объявлять задачу готовой без свежего запуска проверки и разбора вывода. Нужен перед коммитом или PR, когда словам агента нельзя верить на слово.
  `npx skills add obra/superpowers --skill verification-before-completion -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/verification-before-completion/SKILL.md) · 251 313 установок · ставится ✓ 16.11
- **[executing-plans](https://affpapa.org/nevibecode/skills/executing-plans)** — Выполняет готовый план задач в текущей сессии без субагента на каждую задачу. Нужен для inline-разработки с TDD, журналом решений и финальным ревью ветки.
  `npx skills add obra/superpowers --skill executing-plans -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/executing-plans/SKILL.md) · 242 988 установок · ставится ✓ 16.11
- **[dispatching-parallel-agents](https://affpapa.org/nevibecode/skills/dispatching-parallel-agents)** — Распределяет независимые задачи между субагентами, чтобы они разбирали их параллельно. Подходит для разных сбоев в тестах и несвязанных подсистемах.
  `npx skills add obra/superpowers --skill dispatching-parallel-agents -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/dispatching-parallel-agents/SKILL.md) · 218 235 установок · ставится ✓ 16.11
- **[google-agents-cli-eval](https://affpapa.org/nevibecode/skills/google-agents-cli-eval)** — Оценивает качество ИИ-агентов через agents-cli, находит ошибки и сравнивает прогоны. Включается при отладке датасетов и проверке метрик в проектах на базе Gemini.
  `npx skills add google/agents-cli --skill google-agents-cli-eval -a claude-code` · [исходник: google/agents-cli](https://github.com/google/agents-cli/blob/6eedbdc2f44c388cbfc5f305eb83b9924cfefebb/skills/google-agents-cli-eval/SKILL.md) · 574 900 установок · ставится ✓ 16.11
- **[verify-and-stop](https://affpapa.org/nevibecode/skills/verify-and-stop)** — Подтверждает выполнение условий сдачи без раздувания правок. Помогает при финальной проверке тикета и точечном прогоне проверок.
  `npx skills add JuliusBrussee/caveman --skill verify-and-stop -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/3dc497a7f858c774d6e15b25e8c6120ef3a0eda8/skills/verify-and-stop/SKILL.md) · 126 300 установок · ставится ✓ 16.11
- **[surgical-patch](https://affpapa.org/nevibecode/skills/surgical-patch)** — Скилл удерживает ассистента от лишнего рефакторинга при исправлении ошибок. Модель меняет только ответственный слой кода и пишет точечный тест.
  `npx skills add JuliusBrussee/caveman --skill surgical-patch -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/3dc497a7f858c774d6e15b25e8c6120ef3a0eda8/skills/surgical-patch/SKILL.md) · 126 100 установок · ставится ✓ 16.11
- **[debugging-and-error-recovery](https://affpapa.org/nevibecode/skills/debugging-and-error-recovery)** — Скилл ведёт агента по шагам от воспроизведения ошибки до проверки исправления. Подойдёт, когда падают тесты, ломается сборка или поведение не совпадает с ожиданиями.
  `npx skills add addyosmani/agent-skills --skill debugging-and-error-recovery -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/301b02b12bff98e4688e6984af6556802322bbde/skills/debugging-and-error-recovery/SKILL.md) · 76 900 установок

<a name="topic-code-review"></a>
## Код-ревью и рефакторинг

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/code-review](https://affpapa.org/nevibecode/topic/code-review)

- **[improve-codebase-architecture](https://affpapa.org/nevibecode/skills/improve-codebase-architecture)** — Скилл ищет архитектурные узкие места в кодовой базе и показывает варианты углубления модулей в HTML-отчёте. Подойдёт для ревью перед рефакторингом.
  `npx skills add mattpocock/skills --skill improve-codebase-architecture -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/improve-codebase-architecture/SKILL.md) · 1 163 035 установок · ставится ✓ 16.11
- **[code-review](https://affpapa.org/nevibecode/skills/code-review)** — Проверяет ветку или коммиты по двум осям: соответствие стандартам кода и выполнение требований спеки. Запускает субагентов параллельно.
  `npx skills add mattpocock/skills --skill code-review -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/code-review/SKILL.md) · 789 521 установка · ставится ✓ 16.11 · A/B 16.11: -0,29 — эффекта нет
- **[requesting-code-review](https://affpapa.org/nevibecode/skills/requesting-code-review)** — Запрашивает ревью у субагента после задачи, крупной функции или перед слиянием в main. Помогает проверить изменения по требованиям, не перегружая основной контекст.
  `npx skills add obra/superpowers --skill requesting-code-review -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/requesting-code-review/SKILL.md) · 262 135 установок · ставится ✓ 16.11
- **[receiving-code-review](https://affpapa.org/nevibecode/skills/receiving-code-review)** — Помогает разбирать замечания к коду до правок: уточнять неясное, сверяться с кодовой базой и аргументированно возражать. Нужен перед обработкой ревью.
  `npx skills add obra/superpowers --skill receiving-code-review -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/receiving-code-review/SKILL.md) · 221 216 установок · ставится ✓ 16.11
- **[retro](https://affpapa.org/nevibecode/skills/retro)** — Проводит ретроспективу сессии кодинга и предлагает правки окружения агента. Нужен после ошибок, долгой навигации по репозиторию или лишних вызовов инструментов.
  `npx skills add mattpocock/skills --skill retro -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/retro/SKILL.md) · 276 027 установок · ставится ✓ 16.11
- **[caveman-review](https://affpapa.org/nevibecode/skills/caveman-review)** — Скилл для Claude Code и других агентов: пишет замечания к коду одной строкой — место, проблема, исправление. Ускоряет ревью диффа или PR без воды.
  `npx skills add JuliusBrussee/caveman --skill caveman-review -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/3dc497a7f858c774d6e15b25e8c6120ef3a0eda8/skills/caveman-review/SKILL.md) · 434 700 установок · ставится ✓ 16.11 · A/B 16.11: -0,21 — сжатие теряет детали
- **[ponytail](https://affpapa.org/nevibecode/skills/ponytail)** — ponytail переводит агента в режим старшего разработчика: он ищет самое короткое полное решение без лишних абстракций и функций. Подходит для задач, где важны ясный дифф и проверка рисков.
  `npx skills add DietrichGebert/ponytail --skill ponytail -a claude-code` · [исходник: dietrichgebert/ponytail](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail/SKILL.md) · 132 500 установок · ставится ✓ 16.11
- **[ponytail-review](https://affpapa.org/nevibecode/skills/ponytail-review)** — Скилл проверяет изменения глубже обычного diff: читает связанный код, ищет ошибки, риски, проблемы нагрузки и недостающие тесты. Пригодится для ревью PR и коммитов.
  `npx skills add DietrichGebert/ponytail --skill ponytail-review -a claude-code` · [исходник: dietrichgebert/ponytail](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail-review/SKILL.md) · 72 100 установок · ставится ✓ 16.11
- **[ponytail-audit](https://affpapa.org/nevibecode/skills/ponytail-audit)** — Проверяет репозиторий и ранжирует ошибки, риски и лишний код. Подойдёт, если нужен разовый разбор без автоматических правок.
  `npx skills add DietrichGebert/ponytail --skill ponytail-audit -a claude-code` · [исходник: dietrichgebert/ponytail](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail-audit/SKILL.md) · 59 700 установок · ставится ✓ 16.11
- **[caveman-explore](https://affpapa.org/nevibecode/skills/caveman-explore)** — Read-only скилл ищет нужные места в репозитории и возвращает ссылки на файлы со строками. Подходит для первого знакомства с кодовой базой.
  `npx skills add JuliusBrussee/caveman --skill caveman-explore -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/3dc497a7f858c774d6e15b25e8c6120ef3a0eda8/skills/caveman-explore/SKILL.md) · 129 100 установок · ставится ✓ 16.11

<a name="topic-security"></a>
## Безопасность

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/security](https://affpapa.org/nevibecode/topic/security)

- **[security-audit](https://affpapa.org/nevibecode/skills/cloudflare-security-audit)** — Проверяет кодовую базу на уязвимости и ищет нарушения границ доверия. Пригодится перед релизом или для точечного разбора опасных участков кода.
  `npx skills add cloudflare/security-audit-skill --skill security-audit -a claude-code` · [исходник: cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/SKILL.md) · 111 000 установок · ставится ✓ 16.11
- **[security-and-hardening](https://affpapa.org/nevibecode/skills/security-and-hardening)** — Скилл проверяет код на уязвимости в обработчиках ввода, авторизации, сессиях и интеграциях. Помогает разбирать зависимости и риски утечки данных.
  `npx skills add addyosmani/agent-skills --skill security-and-hardening -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/301b02b12bff98e4688e6984af6556802322bbde/skills/security-and-hardening/SKILL.md) · 86 400 установок · ставится ✓ 16.11
- **[fix-security-vulnerabilities-with-strix](https://affpapa.org/nevibecode/skills/fix-security-vulnerabilities-with-strix)** — Скилл разбирает подтверждённые Strix-уязвимости, исправляет их причину и повторно запускает проверку. Подойдёт после CLI- или cloud-сканирования.
  `npx skills add usestrix/strix --skill fix-security-vulnerabilities-with-strix -a claude-code` · [исходник: usestrix/strix](https://github.com/usestrix/strix/blob/4719329d1c3eb0db796714397551945c514a2301/skills/fix-security-vulnerabilities-with-strix/SKILL.md) · 20 300 установок
- **[web-app-penetration-testing](https://affpapa.org/nevibecode/skills/web-app-penetration-testing)** — Проводит чёрный ящик-пентест веб-приложения через Strix и подтверждает найденные уязвимости рабочим PoC. Нужен для проверки staging и dev-сервера.
  `npx skills add usestrix/strix --skill web-app-penetration-testing -a claude-code` · [исходник: usestrix/strix](https://github.com/usestrix/strix/blob/4719329d1c3eb0db796714397551945c514a2301/skills/web-app-penetration-testing/SKILL.md) · 17 600 установок
- **[owasp-top-10-testing](https://affpapa.org/nevibecode/skills/owasp-top-10-testing)** — Запускает агентов Strix для поиска реальных эксплойтов по стандарту OWASP Top 10:2025. Пригодится перед релизом или аудитом безопасности веб-приложения.
  `npx skills add usestrix/strix --skill owasp-top-10-testing -a claude-code` · [исходник: usestrix/strix](https://github.com/usestrix/strix/blob/4719329d1c3eb0db796714397551945c514a2301/skills/owasp-top-10-testing/SKILL.md) · 17 500 установок
- **[persona-it-admin](https://affpapa.org/nevibecode/skills/persona-it-admin)** — Скилл-персона для админа: следит за подозрительными входами, настраивает политики Drive и разбирает заявки через gws.
  `npx skills add googleworkspace/cli --skill persona-it-admin -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/persona-it-admin/SKILL.md) · 31 000 установок
- **[gws-modelarmor](https://affpapa.org/nevibecode/skills/gws-modelarmor)** — Фильтрует пользовательский контент и ответы ИИ через Google Model Armor. Пригодится для проверки безопасности промптов и работы с шаблонами фильтрации.
  `npx skills add googleworkspace/cli --skill gws-modelarmor -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-modelarmor/SKILL.md) · 30 900 установок
- **[gws-modelarmor-create-template](https://affpapa.org/nevibecode/skills/gws-modelarmor-create-template)** — Создаёт шаблоны Google Model Armor в GCP для фильтрации контента. Пригодится при настройке защиты от джейлбрейков через утилиту gws.
  `npx skills add googleworkspace/cli --skill gws-modelarmor-create-template -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-modelarmor-create-template/SKILL.md) · 30 800 установок
- **[1password](https://affpapa.org/nevibecode/skills/1password)** — Настраивает 1Password CLI, подключает авторизацию и помогает безопасно внедрять секреты в команды без утечки паролей в чат.
  `npx skills add openclaw/openclaw --skill 1password -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/f683d5ffd214c84d2b75d91b82cde3aabc05fab2/skills/1password/SKILL.md) · 6 400 установок
- **[healthcheck](https://affpapa.org/nevibecode/skills/healthcheck)** — Проверяет безопасность хоста OpenClaw, открытые порты, фаервол и SSH. Помогает найти риски и поэтапно усилить защиту без опасности потерять доступ.
  `npx skills add openclaw/openclaw --skill healthcheck -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/f683d5ffd214c84d2b75d91b82cde3aabc05fab2/skills/healthcheck/SKILL.md) · 5 600 установок

<a name="topic-devops"></a>
## DevOps и инфраструктура

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/devops](https://affpapa.org/nevibecode/topic/devops)

- **[wizard](https://affpapa.org/nevibecode/skills/wizard)** — Скилл создаёт интерактивный bash-скрипт для ручных шагов: настройки сервисов, секретов CI и разовых миграций.
  `npx skills add mattpocock/skills --skill wizard -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/wizard/SKILL.md) · 553 369 установок · ставится ✓ 16.11
- **[setup-pre-commit](https://affpapa.org/nevibecode/skills/setup-pre-commit)** — Скилл настраивает pre-commit для JavaScript-репозитория: Husky запускает форматирование, проверку типов и тесты перед коммитом.
  `npx skills add mattpocock/skills --skill setup-pre-commit -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/misc/setup-pre-commit/SKILL.md) · 489 289 установок · ставится ✓ 16.11
- **[google-agents-cli-observability](https://affpapa.org/nevibecode/skills/google-agents-cli-observability)** — Скилл помогает настроить трассировку и сбор данных о работе агентов, включая ADK. Пригодится для разбора ошибок и наблюдения за агентом после развёртывания.
  `npx skills add google/agents-cli --skill google-agents-cli-observability -a claude-code` · [исходник: google/agents-cli](https://github.com/google/agents-cli/blob/6eedbdc2f44c388cbfc5f305eb83b9924cfefebb/skills/google-agents-cli-observability/SKILL.md) · 574 700 установок · ставится ✓ 16.11
- **[herdr](https://affpapa.org/nevibecode/skills/herdr)** — Скилл даёт агенту доступ к Herdr — терминальному мультиплексору для кодинг-агентов: панели, вкладки, воркспейсы и запуск команд.
  `npx skills add herdrdev/herdr --skill herdr -a claude-code` · [исходник: herdrdev/herdr](https://github.com/herdrdev/herdr/blob/ee5bfb5041bb3e4a49d591c72308aae3c81ecdde/skills/herdr/SKILL.md) · 84 800 установок · ставится ✓ 16.11
- **[vercel-cli-with-tokens](https://affpapa.org/nevibecode/skills/vercel-cli-with-tokens)** — Агент работает с Vercel CLI по access-токену, без vercel login: находит VERCEL_TOKEN, связывает проект, катит preview-деплой и правит переменные окружения.
  `npx skills add vercel-labs/agent-skills --skill vercel-cli-with-tokens -a claude-code` · [исходник: vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/vercel-cli-with-tokens/SKILL.md) · 156 700 установок
- **[turborepo](https://affpapa.org/nevibecode/skills/vercel-turborepo)** — Настраивает монорепозитории с Turborepo и чинит пайплайны задач. Пригодится при правках turbo.json, кеширования или сборки в CI.
  `npx skills add vercel/turborepo --skill turborepo -a claude-code` · [исходник: vercel/turborepo](https://github.com/vercel/turborepo/blob/ef00d80db2f08d610582dbcd592064c2c4247d45/skills/turborepo/SKILL.md) · 90 700 установок · ставится ✓ 16.11
- **[vercel-optimize](https://affpapa.org/nevibecode/skills/vercel-optimize)** — Скилл для Claude Code, Codex, Cursor, GitHub Copilot и Gemini CLI, который проводит аудит стоимости и производительности задеплоенных проектов на Vercel.
  `npx skills add vercel-labs/agent-skills --skill vercel-optimize -a claude-code` · [исходник: vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/vercel-optimize/SKILL.md) · 132 700 установок
- **[shipping-and-launch](https://affpapa.org/nevibecode/skills/shipping-and-launch)** — Скилл для Claude Code: чек-лист перед деплоем в прод, поэтапный роллаут и план отката. Запускается, когда фича уходит к реальным пользователям.
  `npx skills add addyosmani/agent-skills --skill shipping-and-launch -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/301b02b12bff98e4688e6984af6556802322bbde/skills/shipping-and-launch/SKILL.md) · 71 600 установок
- **[ci-cd-and-automation](https://affpapa.org/nevibecode/skills/ci-cd-and-automation)** — Скилл собирает пайплайн CI/CD на GitHub Actions: линт, типы, тесты, сборка и аудит зависимостей идут по порядку с фиксированным набором гейтов на каждый PR.
  `npx skills add addyosmani/agent-skills --skill ci-cd-and-automation -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/301b02b12bff98e4688e6984af6556802322bbde/skills/ci-cd-and-automation/SKILL.md) · 71 500 установок
- **[orca-per-workspace-env](https://affpapa.org/nevibecode/skills/orca-per-workspace-env)** — Настраивает и проверяет рецепты изолированных окружений Orca под каждый воркспейс. Помогает при отладке cloud sandbox, VM или контейнеров в orca.yaml.
  `npx skills add stablyai/orca --skill orca-per-workspace-env -a claude-code` · [исходник: stablyai/orca](https://github.com/stablyai/orca/blob/457c602b4f737d95dbdcf2f176f0beac8d9909b6/skills/orca-per-workspace-env/SKILL.md) · 12 600 установок

<a name="topic-cloud"></a>
## Облака: AWS, Azure, GCP

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/cloud](https://affpapa.org/nevibecode/topic/cloud)

- **[google-agents-cli-deploy](https://affpapa.org/nevibecode/skills/google-agents-cli-deploy)** — Инструктирует агента по деплою ИИ-агентов в Google Cloud через утилиту agents-cli. Помогает настроить запуск в Agent Runtime, Cloud Run или GKE с учётом CI/CD и секретов.
  `npx skills add google/agents-cli --skill google-agents-cli-deploy -a claude-code` · [исходник: google/agents-cli](https://github.com/google/agents-cli/blob/6eedbdc2f44c388cbfc5f305eb83b9924cfefebb/skills/google-agents-cli-deploy/SKILL.md) · 576 100 установок · ставится ✓ 16.11
- **[gws-drive-upload](https://affpapa.org/nevibecode/skills/gws-drive-upload)** — Скилл для Claude Code, Codex, Cursor и других IDE позволяет загружать файлы в Google Drive прямо из редактора с автоматическим определением типа и имени. Запускается командой gws drive +upload с указанием пути к файлу.
  `npx skills add googleworkspace/cli --skill gws-drive-upload -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-drive-upload/SKILL.md) · 51 200 установок
- **[gws-events-subscribe](https://affpapa.org/nevibecode/skills/gws-events-subscribe)** — Скилл для Claude Code, Cursor и других IDE позволяет подписаться на события Google Workspace (сообщения в Chat, изменения документов) и получать их потоком в формате NDJSON.
  `npx skills add googleworkspace/cli --skill gws-events-subscribe -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-events-subscribe/SKILL.md) · 31 700 установок
- **[cloudflare](https://affpapa.org/nevibecode/skills/cloudflare-cloudflare)** — Скилл для Claude Code и Codex подбирает продукты Cloudflare под архитектуру проекта и диагностирует ошибки 52x или 403. Включается при создании сайтов, настройке API и отладке проксирования.
  `npx skills add cloudflare/skills --skill cloudflare -a claude-code` · [исходник: cloudflare/skills](https://github.com/cloudflare/skills/blob/cbf893b954222276bf1af57e5f23379231e0efb9/skills/cloudflare/SKILL.md) · 159 200 установок
- **[google-cloud-waf-cost-optimization](https://affpapa.org/nevibecode/skills/google-cloud-waf-cost-optimization)** — Скилл для Claude Code, Gemini CLI и Codex, который оценивает рабочие нагрузки Google Cloud по столпу Cost Optimization фреймворка Well-Architected.
  `npx skills add google/skills --skill google-cloud-waf-cost-optimization -a claude-code` · [исходник: google/skills](https://github.com/google/skills/blob/e5250c8a02c28097b11a0c22d77143f4a0e5a408/skills/cloud/google-cloud-waf-cost-optimization/SKILL.md) · 14 266 установок
- **[firebase-basics](https://affpapa.org/nevibecode/skills/firebase-basics)** — Скилл настраивает Firebase CLI, помогает войти в аккаунт, создать или выбрать проект и скачать конфигурацию Android или iOS.
  `npx skills add google/skills --skill firebase-basics -a claude-code` · [исходник: google/skills](https://github.com/google/skills/blob/e5250c8a02c28097b11a0c22d77143f4a0e5a408/skills/cloud/firebase-basics/SKILL.md) · 14 100 установок
- **[google-cloud-networking-observability](https://affpapa.org/nevibecode/skills/google-cloud-networking-observability)** — Скилл разбирает сетевые логи, метрики и диагностику Google Cloud. Подойдёт, когда нужно найти причину потерь пакетов или проверить сетевой путь.
  `npx skills add google/skills --skill google-cloud-networking-observability -a claude-code` · [исходник: google/skills](https://github.com/google/skills/blob/e5250c8a02c28097b11a0c22d77143f4a0e5a408/skills/cloud/google-cloud-networking-observability/SKILL.md) · 11 856 установок
- **[firebase-app-hosting-basics](https://affpapa.org/nevibecode/skills/firebase-app-hosting-basics)** — Скилл помогает разворачивать Next.js и Angular с SSR через Firebase App Hosting. Пригодится для настройки бэкенда, секретов и деплоя из GitHub.
  `npx skills add firebase/agent-skills --skill firebase-app-hosting-basics -a claude-code` · [исходник: firebase/agent-skills](https://github.com/firebase/agent-skills/blob/99954a30898bb5ddc8152ee10e124dc3b4106bf7/skills/firebase-app-hosting-basics/SKILL.md) · 180 100 установок
- **[firebase-crashlytics](https://affpapa.org/nevibecode/skills/firebase-crashlytics)** — Скилл для Claude Code, который помогает настроить Firebase Crashlytics и SDK для отчётов о сбоях. Запускается при добавлении Crashlytics в Android, iOS или Web-приложение.
  `npx skills add firebase/agent-skills --skill firebase-crashlytics -a claude-code` · [исходник: firebase/agent-skills](https://github.com/firebase/agent-skills/blob/99954a30898bb5ddc8152ee10e124dc3b4106bf7/skills/firebase-crashlytics/SKILL.md) · 142 100 установок
- **[prisma-compute](https://affpapa.org/nevibecode/skills/prisma-compute)** — Скилл для Claude Code управляет развёртыванием и обслуживанием приложений на Prisma Compute через CLI Prisma 8. Помогает настроить Prisma Composer, откатить релизы и проверить логи сервисов.
  `npx skills add prisma/skills --skill prisma-compute -a claude-code` · [исходник: prisma/skills](https://github.com/prisma/skills/blob/a6f192959cf43b08aa330fe1ffca090267215812/prisma-compute/SKILL.md) · 410 600 установок

<a name="topic-data"></a>
## Данные и базы

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/data](https://affpapa.org/nevibecode/topic/data)

- **[migration](https://affpapa.org/nevibecode/skills/migration)** — Скилл задаёт правила безопасных миграций схем, данных и API с обязательным откатом. Пригодится при изменениях, где нельзя терять данные или ломать совместимость.
  `npx skills add JuliusBrussee/caveman --skill migration -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/3dc497a7f858c774d6e15b25e8c6120ef3a0eda8/skills/migration/SKILL.md) · 125 000 установок · ставится ✓ 16.11 · A/B 16.11: +0,43 — лучший по знаку, 5 из 6 оценок в плюс
- **[notion](https://affpapa.org/nevibecode/skills/notion)** — Скилл связывает агента с Notion через ntn CLI и API: он помогает читать и менять страницы, запрашивать data sources и загружать файлы.
  `npx skills add openclaw/openclaw --skill notion -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/f683d5ffd214c84d2b75d91b82cde3aabc05fab2/skills/notion/SKILL.md) · 5 700 установок
- **[data-visualization](https://affpapa.org/nevibecode/skills/anthropics-data-visualization)** — Подбирает подходящие типы графиков под структуру данных и генерирует код на Python с matplotlib, seaborn и plotly. Пригодится при подготовке отчётов.
  `npx skills add anthropics/knowledge-work-plugins --skill data-visualization -a claude-code` · [исходник: anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/data/skills/data-visualization/SKILL.md) · 14 800 установок
- **[database-migrations](https://affpapa.org/nevibecode/skills/database-migrations)** — Скилл описывает безопасные и обратимые миграции схемы: expand-contract, индексы CONCURRENTLY, батч-бэкфиллы и рабочие процессы для PostgreSQL, Prisma, Drizzle, Kysely, Django и golang-migrate.
  `npx skills add affaan-m/ECC --skill database-migrations -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/database-migrations/SKILL.md) · 6 900 установок
- **[postgres-patterns](https://affpapa.org/nevibecode/skills/postgres-patterns)** — Шпаргалка по лучшим практикам PostgreSQL на базе Supabase: выбор индексов, типов данных, оптимизация RLS и поиск медленных запросов.
  `npx skills add affaan-m/ECC --skill postgres-patterns -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/postgres-patterns/SKILL.md) · 6 800 установок
- **[bigquery-basics](https://affpapa.org/nevibecode/skills/bigquery-basics)** — Управляет ресурсами BigQuery и запускает SQL-запросы. Подходит для создания датасетов, таблиц, представлений и базовой загрузки данных.
  `npx skills add google/skills --skill bigquery-basics -a claude-code` · [исходник: google/skills](https://github.com/google/skills/blob/e5250c8a02c28097b11a0c22d77143f4a0e5a408/skills/cloud/bigquery-basics/SKILL.md) · 17 678 установок
- **[mysql-patterns](https://affpapa.org/nevibecode/skills/mysql-patterns)** — Скилл с проверенными шаблонами для MySQL и MariaDB. Помогает проектировать схемы, настраивать индексы и ускорять медленные транзакции.
  `npx skills add affaan-m/ECC --skill mysql-patterns -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/mysql-patterns/SKILL.md) · 6 100 установок
- **[alloydb-basics](https://affpapa.org/nevibecode/skills/alloydb-basics)** — Помогает создавать и настраивать кластеры и экземпляры AlloyDB for PostgreSQL, управлять резервными копиями и использовать инструменты AlloyDB MCP. Подходит для администрирования AlloyDB.
  `npx skills add google/skills --skill alloydb-basics -a claude-code` · [исходник: google/skills](https://github.com/google/skills/blob/e5250c8a02c28097b11a0c22d77143f4a0e5a408/skills/cloud/alloydb-basics/SKILL.md) · 12 991 установка
- **[postgresql-table-design](https://affpapa.org/nevibecode/skills/postgresql-table-design)** — Помогает проектировать и проверять схемы PostgreSQL: типы, ключи, ограничения, индексы и разбиение таблиц.
  `npx skills add wshobson/agents --skill postgresql-table-design -a claude-code` · [исходник: wshobson/agents](https://github.com/wshobson/agents/blob/4bde3168b43c0655c4d00ea2726e631719908a6d/plugins/database-design/skills/postgresql-table-design/SKILL.md) · 27 780 установок
- **[data-analysis](https://affpapa.org/nevibecode/skills/bytedance-data-analysis)** — Скилл для Claude Code, Codex, Cursor и других платформ обрабатывает таблицы через DuckDB. Выполняет SQL-запросы к загруженным файлам Excel и CSV без отдельной СУБД.
  `npx skills add bytedance/deer-flow --skill data-analysis -a claude-code` · [исходник: bytedance/deer-flow](https://github.com/bytedance/deer-flow/blob/4a27b133f81dfa621bf17635f2659bef2eebb7fd/skills/public/data-analysis/SKILL.md) · 3 700 установок

<a name="topic-ai-ml"></a>
## ИИ и ML

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/ai-ml](https://affpapa.org/nevibecode/topic/ai-ml)

- **[skill-creator](https://affpapa.org/nevibecode/skills/skill-creator)** — Помогает создать новый скилл, доработать существующий и проверить результат через тестовые промпты и оценки.
  `npx skills add anthropics/skills --skill skill-creator -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/skill-creator/SKILL.md) · 414 180 установок · ставится ✓ 16.11
- **[media-use](https://affpapa.org/nevibecode/skills/media-use)** — Ищет и генерирует медиафайлы для видеопроектов HyperFrames, сохраняя их локально в папку assets. Подключает каталог HeyGen, озвучку, фоновую музыку и цветовую коррекцию видео.
  `npx skills add heygen-com/hyperframes --skill media-use -a claude-code` · [исходник: heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/blob/f207f612f1fba902d5c1480ea98a90c1469752e5/skills/media-use/SKILL.md) · 1 500 000 установок · ставится ✓ 16.11
- **[subagent-driven-development](https://affpapa.org/nevibecode/skills/subagent-driven-development)** — Скилл выполняет план через отдельных субагентов для каждой задачи и проверяет результат после каждого шага. Подходит для независимых задач в одной сессии.
  `npx skills add obra/superpowers --skill subagent-driven-development -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/subagent-driven-development/SKILL.md) · 237 746 установок · ставится ✓ 16.11
- **[caveman-stats](https://affpapa.org/nevibecode/skills/caveman-stats)** — Выводит статистику токенов и активный режим сессии или направляет к штатным отчётам хоста. Полезен для контроля расхода токенов вывода и кэша.
  `npx skills add JuliusBrussee/caveman --skill caveman-stats -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/3dc497a7f858c774d6e15b25e8c6120ef3a0eda8/skills/caveman-stats/SKILL.md) · 381 900 установок · ставится ✓ 16.11
- **[claude-api](https://affpapa.org/nevibecode/skills/claude-api)** — Справочник по Anthropic SDK и API Claude для генерации кода без устаревших параметров и выдуманных методов.
  `npx skills add anthropics/skills --skill claude-api -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/claude-api/SKILL.md) · 74 198 установок · ставится ✓ 16.11
- **[karpathy-guidelines](https://affpapa.org/nevibecode/skills/karpathy-guidelines)** — Правила, которые уменьшают типовые ошибки LLM в коде: меньше лишних абстракций, точечные правки, проверяемый результат.
  `npx skills add multica-ai/andrej-karpathy-skills --skill karpathy-guidelines -a claude-code` · [исходник: multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/skills/karpathy-guidelines/SKILL.md) · 47 100 установок · ставится ✓ 16.11
- **[google-agents-cli-publish](https://affpapa.org/nevibecode/skills/google-agents-cli-publish)** — Проводит задеплоенного агента через agents-cli publish gemini: режимы ADK и A2A, флаги, автодетект по метаданным и регистрация в Agent Registry.
  `npx skills add google/agents-cli --skill google-agents-cli-publish -a claude-code` · [исходник: google/agents-cli](https://github.com/google/agents-cli/blob/6eedbdc2f44c388cbfc5f305eb83b9924cfefebb/skills/google-agents-cli-publish/SKILL.md) · 575 900 установок · ставится ✓ 16.11
- **[caveman-optimize](https://affpapa.org/nevibecode/skills/caveman-optimize)** — Скилл помогает разобрать наблюдение Caveman, выбрать кандидата оператором и проверить его парным сравнением с базовой версией. Изменения требуют явного одобрения.
  `npx skills add JuliusBrussee/caveman --skill caveman-optimize -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/3dc497a7f858c774d6e15b25e8c6120ef3a0eda8/skills/caveman-optimize/SKILL.md) · 127 200 установок · ставится ✓ 16.11
- **[caveman-evidence-review](https://affpapa.org/nevibecode/skills/caveman-evidence-review)** — Скилл читает данные Caveman Cloud о расходах LLM, трассах и маршрутизации. Подходит для проверки того, куда уходит бюджет проекта.
  `npx skills add JuliusBrussee/caveman --skill caveman-evidence-review -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/3dc497a7f858c774d6e15b25e8c6120ef3a0eda8/skills/caveman-evidence-review/SKILL.md) · 125 700 установок · ставится ✓ 16.11
- **[context-engineering](https://affpapa.org/nevibecode/skills/context-engineering)** — Помогает настроить контекст ИИ-агента: какие правила, спецификации и файлы отдать агенту и когда. Пригодится в начале сессии, при падении качества ответов и при смене задач.
  `npx skills add addyosmani/agent-skills --skill context-engineering -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/301b02b12bff98e4688e6984af6556802322bbde/skills/context-engineering/SKILL.md) · 75 400 установок

<a name="topic-automation"></a>
## Автоматизация и no-code: n8n, Zapier, Make

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/automation](https://affpapa.org/nevibecode/topic/automation)

- **[gws-gmail-send](https://affpapa.org/nevibecode/skills/gws-gmail-send)** — Скилл для Claude Code, Codex, Cursor, GitHub Copilot и Gemini CLI, который даёт агенту команду gws gmail +send. Отправляет письма через Gmail с вложениями, CC/BCC, HTML-телом и алиасами отправителя.
  `npx skills add googleworkspace/cli --skill gws-gmail-send -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-gmail-send/SKILL.md) · 76 600 установок
- **[recipe-email-drive-link](https://affpapa.org/nevibecode/skills/recipe-email-drive-link)** — Скилл для Claude Code, Codex, Cursor и других ИИ-редакторов автоматизирует отправку ссылок на файлы Google Drive по почте. Находит файл, открывает доступ и отправляет письмо с сообщением — всё в одной цепочке команд.
  `npx skills add googleworkspace/cli --skill recipe-email-drive-link -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/recipe-email-drive-link/SKILL.md) · 32 400 установок
- **[recipe-label-and-archive-emails](https://affpapa.org/nevibecode/skills/recipe-label-and-archive-emails)** — Скилл для Claude Code и ещё пяти платформ ИИ-кодинга: организует почту через поиск писем по условию, добавление меток и архивирование. Работает через Google Workspace CLI с предварительной загрузкой скилла gws-gmail.
  `npx skills add googleworkspace/cli --skill recipe-label-and-archive-emails -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/recipe-label-and-archive-emails/SKILL.md) · 31 400 установок
- **[openhue](https://affpapa.org/nevibecode/skills/openhue)** — Скилл для Claude Code, Codex, Cursor и других AI-агентов, который управляет лампами и сценами Philips Hue через CLI. Работает через локальный Hue Bridge — агент включает свет, меняет яркость и цвет прямо из чата.
  `npx skills add openclaw/openclaw --skill openhue -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/f683d5ffd214c84d2b75d91b82cde3aabc05fab2/skills/openhue/SKILL.md) · 5 200 установок
- **[baoyu-post-to-x](https://affpapa.org/nevibecode/skills/baoyu-post-to-x)** — Публикует текст, картинки, видео и длинные статьи в X через браузер Chrome. Работает через плагин Codex, Computer Use или CDP-скрипты.
  `npx skills add JimLiu/baoyu-skills --skill baoyu-post-to-x -a claude-code` · [исходник: jimliu/baoyu-skills](https://github.com/JimLiu/baoyu-skills/blob/ca703c2d7c2c4399a1dc0cf82224f8551e05a96d/skills/baoyu-post-to-x/SKILL.md) · 29 400 установок
- **[baoyu-youtube-transcript](https://affpapa.org/nevibecode/skills/baoyu-youtube-transcript)** — Скилл для Claude Code и Codex: скачивает субтитры и обложку YouTube-видео по ссылке или ID — без ручного копирования текста ролика.
  `npx skills add JimLiu/baoyu-skills --skill baoyu-youtube-transcript -a claude-code` · [исходник: jimliu/baoyu-skills](https://github.com/JimLiu/baoyu-skills/blob/ca703c2d7c2c4399a1dc0cf82224f8551e05a96d/skills/baoyu-youtube-transcript/SKILL.md) · 22 800 установок
- **[wacli](https://affpapa.org/nevibecode/skills/wacli)** — Скилл подключает консольную утилиту wacli для отправки сообщений в WhatsApp третьим лицам, поиска переписок и скачивания истории чатов.
  `npx skills add openclaw/openclaw --skill wacli -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/f683d5ffd214c84d2b75d91b82cde3aabc05fab2/extensions/whatsapp/skills/wacli/SKILL.md) · 3 300 установок
- **[just](https://affpapa.org/nevibecode/skills/just)** — Скилл для Claude Code и других агентов: справочник по just с синтаксисом justfile, рецептами и командами просмотра — чтобы читать и запускать задачи в проекте.
  `npx skills add casey/just --skill just -a claude-code` · [исходник: casey/just](https://github.com/casey/just/blob/168c8e288dc8a591ca851b4ef070cada64f43c35/skills/just/SKILL.md) · 1 200 установок
- **[create-an-asset](https://affpapa.org/nevibecode/skills/create-an-asset)** — Скилл собирает презентации, одностраничники и раздаточные материалы из данных аккаунта, заметок с созвонов и утверждённого контента без выдуманных цифр. Работает в Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI и OpenCode.
  `npx skills add anthropics/knowledge-work-plugins --skill create-an-asset -a claude-code` · [исходник: anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/sales/skills/create-an-asset/SKILL.md) · 3 100 установок
- **[iros-registry-automation](https://affpapa.org/nevibecode/skills/iros-registry-automation)** — Готовит выписки из корейского реестра IROS и помогает вести сессию в браузере. Нужен при работе с выписками по недвижимости и юрлицам.
  `npx skills add NomaDamas/k-skill --skill iros-registry-automation -a claude-code` · [исходник: nomadamas/k-skill](https://github.com/NomaDamas/k-skill/blob/9766d20fb1fe1a5eb1d10ef5ff9872c8d6fc4985/iros-registry-automation/SKILL.md) · 11 000 установок

<a name="topic-docs"></a>
## Тексты и документация

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/docs](https://affpapa.org/nevibecode/topic/docs)

- **[grill-with-docs](https://affpapa.org/nevibecode/skills/grill-with-docs)** — Скилл проводит жёсткое интервью по плану или дизайну и по ходу создаёт ADR и глоссарий. Подойдёт перед началом сложной разработки.
  `npx skills add mattpocock/skills --skill grill-with-docs -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/grill-with-docs/SKILL.md) · 1 219 756 установок · ставится ✓ 16.11
- **[domain-modeling](https://affpapa.org/nevibecode/skills/domain-modeling)** — Скилл помогает уточнять термины проекта, вести GLOSSARY.md и фиксировать архитектурные решения в ADR. Нужен, когда модель предметной области меняется.
  `npx skills add mattpocock/skills --skill domain-modeling -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/domain-modeling/SKILL.md) · 876 391 установка · ставится ✓ 16.11
- **[to-spec](https://affpapa.org/nevibecode/skills/to-spec)** — Собирает из текущего диалога и контекста репозитория спецификацию, затем публикует её в трекере задач. Нужен после обсуждения фичи, когда пора передать работу агенту.
  `npx skills add mattpocock/skills --skill to-spec -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/to-spec/SKILL.md) · 715 388 установок · ставится ✓ 16.11
- **[pdf](https://affpapa.org/nevibecode/skills/pdf)** — Скилл читает, создаёт и меняет PDF-файлы, включая формы и сканы. Подойдёт, когда агенту нужно работать с PDF в проекте.
  `npx skills add anthropics/skills --skill pdf -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/pdf/SKILL.md) · 216 041 установка
- **[doc-coauthoring](https://affpapa.org/nevibecode/skills/doc-coauthoring)** — Ведёт автора через сбор контекста, подготовку разделов и проверку документа глазами нового читателя. Подходит для спецификаций, RFC, предложений и decision docs.
  `npx skills add anthropics/skills --skill doc-coauthoring -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/doc-coauthoring/SKILL.md) · 93 900 установок
- **[caveman-help](https://affpapa.org/nevibecode/skills/caveman-help)** — Справка по режимам и командам Caveman для Claude Code и других поддерживаемых платформ. Нужна, когда вы настраиваете стиль ответов и связанные скиллы.
  `npx skills add JuliusBrussee/caveman --skill caveman-help -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/3dc497a7f858c774d6e15b25e8c6120ef3a0eda8/skills/caveman-help/SKILL.md) · 425 100 установок · ставится ✓ 16.11
- **[internal-comms](https://affpapa.org/nevibecode/skills/internal-comms)** — Скилл помогает Claude писать внутренние коммуникации в форматах вашей компании: от статусных отчётов до FAQ и отчётов об инцидентах.
  `npx skills add anthropics/skills --skill internal-comms -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/internal-comms/SKILL.md) · 79 929 установок · ставится ✓ 16.11
- **[archify](https://affpapa.org/nevibecode/skills/archify)** — Создаёт проверенные диаграммы и одностраничные объяснения в виде HTML-файлов. Подойдёт, когда нужно показать устройство системы, поток данных или схему базы.
  `npx skills add tt-a1i/archify --skill archify -a claude-code` · [исходник: tt-a1i/archify](https://github.com/tt-a1i/archify/blob/7e45f36c66de1254d5ad6ba1d878f6499ea269fd/archify/SKILL.md) · 192 900 установок · ставится ✓ 16.11
- **[writing-guidelines](https://affpapa.org/nevibecode/skills/writing-guidelines)** — Скилл для ревью документации и прозы по письменному гайдлайну. Возвращает замечания с номерами строк, чтобы правки не искать по всему файлу вручную.
  `npx skills add vercel-labs/agent-skills --skill writing-guidelines -a claude-code` · [исходник: vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/writing-guidelines/SKILL.md) · 129 300 установок
- **[documentation-and-adrs](https://affpapa.org/nevibecode/skills/documentation-and-adrs)** — Скилл помогает фиксировать архитектурные решения (ADR), причины выбора технологий и контекст для будущих разработчиков или агентов в репозитории.
  `npx skills add addyosmani/agent-skills --skill documentation-and-adrs -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/301b02b12bff98e4688e6984af6556802322bbde/skills/documentation-and-adrs/SKILL.md) · 77 900 установок

<a name="topic-office"></a>
## Документы и офис

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/office](https://affpapa.org/nevibecode/topic/office)

- **[pptx](https://affpapa.org/nevibecode/skills/pptx)** — Скилл для Claude Code создаёт, разбирает и редактирует файлы .pptx и .potx. Срабатывает при любых задачах со слайдами, шаблонами или презентациями.
  `npx skills add anthropics/skills --skill pptx -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/pptx/SKILL.md) · 241 433 установки
- **[docx](https://affpapa.org/nevibecode/skills/docx)** — Скилл для Claude Code помогает создавать, читать и редактировать документы Word и шаблоны. Включается по запросу на работу с .docx или .dotx, в том числе на подготовку оформленного отчёта или письма.
  `npx skills add anthropics/skills --skill docx -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/docx/SKILL.md) · 206 304 установки
- **[xlsx](https://affpapa.org/nevibecode/skills/xlsx)** — Скилл для Claude Code и Claude.ai создаёт, правит и проверяет электронные таблицы. Запускается при работе с файлами xlsx, xlsm, csv или tsv.
  `npx skills add anthropics/skills --skill xlsx -a claude-code` · [исходник: anthropics/skills](https://github.com/anthropics/skills/blob/1780c5e5a552fd4d1c9d6a7b0cab26b0c2bef064/skills/xlsx/SKILL.md) · 187 223 установки
- **[gws-sheets](https://affpapa.org/nevibecode/skills/gws-sheets)** — Скилл позволяет агенту читать и изменять таблицы Google Sheets через CLI. Подойдёт для работы с данными из проекта и автоматизации операций с таблицами.
  `npx skills add googleworkspace/cli --skill gws-sheets -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-sheets/SKILL.md) · 61 600 установок
- **[gws-sheets-read](https://affpapa.org/nevibecode/skills/gws-sheets-read)** — Скилл для Claude Code читает значения ячеек и листов из Google Таблиц через CLI. Получает данные таблицы без их изменения.
  `npx skills add googleworkspace/cli --skill gws-sheets-read -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-sheets-read/SKILL.md) · 52 600 установок
- **[gws-slides](https://affpapa.org/nevibecode/skills/gws-slides)** — Скилл для Claude Code и других AI-редакторов, который добавляет команды для чтения и редактирования презентаций Google Slides прямо из кода. Работает на Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI и OpenCode.
  `npx skills add googleworkspace/cli --skill gws-slides -a claude-code` · [исходник: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-slides/SKILL.md) · 43 600 установок
- **[gog](https://affpapa.org/nevibecode/skills/gog)** — Даёт агенту правила работы с CLI gog для Gmail, Calendar, Drive, Contacts, Sheets и Docs. Нужен, когда действия в Google Workspace надо выполнять из терминала.
  `npx skills add openclaw/openclaw --skill gog -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/f683d5ffd214c84d2b75d91b82cde3aabc05fab2/skills/gog/SKILL.md) · 8 500 установок
- **[nano-pdf](https://affpapa.org/nevibecode/skills/nano-pdf)** — Скилл для Claude Code и Codex. Редактирует PDF-страницы по текстовым инструкциям через CLI nano-pdf.
  `npx skills add openclaw/openclaw --skill nano-pdf -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/f683d5ffd214c84d2b75d91b82cde3aabc05fab2/skills/nano-pdf/SKILL.md) · 7 200 установок
- **[convert-documents-to-markdown](https://affpapa.org/nevibecode/skills/convert-documents-to-markdown)** — Скилл для Claude Code конвертирует офисные документы, таблицы и PDF в GitHub-Flavored Markdown через утилиту anydoc. Извлекает данные из DOCX и XLSX без ручной вычитки.
  `npx skills add firecrawl/anydoc --skill convert-documents-to-markdown -a claude-code` · [исходник: firecrawl/anydoc](https://github.com/firecrawl/anydoc/blob/e7178e099b6bf9171e2c52b832cbdb4134b69112/skills/convert-documents-to-markdown/SKILL.md) · 13 700 установок
- **[nature-paper2ppt](https://affpapa.org/nevibecode/skills/nature-paper2ppt)** — Собирает китайскую академическую презентацию .pptx из научной статьи или заметок: слайды, рисунки из источника и заметки докладчика.
  `npx skills add Yuan1z0825/nature-skills --skill nature-paper2ppt -a claude-code` · [исходник: yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills/blob/7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8/skills/nature-paper2ppt/SKILL.md) · 17 500 установок

<a name="topic-seo"></a>
## SEO и GEO

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/seo](https://affpapa.org/nevibecode/topic/seo)

- **[seo-audit](https://affpapa.org/nevibecode/skills/coreyhaines31-seo-audit)** — Скилл для Claude Code, Codex, Cursor и других платформ. Находит технические ошибки поисковой оптимизации, проблемы индексации и сбои в разметке сайта.
  `npx skills add coreyhaines31/marketingskills --skill seo-audit -a claude-code` · [исходник: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/8a3bde8083bd121971f61cba4bdbe5fd8c0eee7d/skills/seo-audit/SKILL.md) · 256 600 установок · ставится ✓ 16.11 · A/B 16.11: +0,00 — эффекта нет
- **[marketing-psychology](https://affpapa.org/nevibecode/skills/coreyhaines31-marketing-psychology)** — Скилл для Claude Code помогает применять психологические модели в маркетинге. Разбирает поведение покупателей и оценивает, насколько честно работает приём убеждения.
  `npx skills add coreyhaines31/marketingskills --skill marketing-psychology -a claude-code` · [исходник: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/8a3bde8083bd121971f61cba4bdbe5fd8c0eee7d/skills/marketing-psychology/SKILL.md) · 179 300 установок
- **[ai-seo](https://affpapa.org/nevibecode/skills/ai-seo)** — Скилл для Claude Code помогает попасть в ответы ChatGPT, Perplexity, Google AI Overviews и других LLM. Настраивает контент, структуру и формат страниц, чтобы AI-системы выбирали ваши источники.
  `npx skills add coreyhaines31/marketingskills --skill ai-seo -a claude-code` · [исходник: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/8a3bde8083bd121971f61cba4bdbe5fd8c0eee7d/skills/ai-seo/SKILL.md) · 166 500 установок · A/B 16.11: -0,21 — эффекта нет, ~9 тыс. токенов
- **[seo](https://affpapa.org/nevibecode/skills/affaan-m-seo)** — Скилл для ИИ-агента: проверяет техническое SEO, разметку и Core Web Vitals, а потом предлагает конкретные правки по страницам.
  `npx skills add affaan-m/ECC --skill seo -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/seo/SKILL.md) · 6 500 установок
- **[content-engine](https://affpapa.org/nevibecode/skills/content-engine)** — Скилл превращает статьи, заметки и демо в контент для X, LinkedIn, TikTok, YouTube и рассылок. Подойдёт для постов, сценариев и контент-планов.
  `npx skills add affaan-m/ECC --skill content-engine -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/content-engine/SKILL.md) · 6 200 установок
- **[marketing-campaign](https://affpapa.org/nevibecode/skills/marketing-campaign)** — Планирует многоканальный запуск продукта: от анализа аудитории и позиционирования до текстов для лендинга, писем и соцсетей. Помогает собрать материалы запуска по единой структуре.
  `npx skills add affaan-m/ECC --skill marketing-campaign -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/marketing-campaign/SKILL.md) · 6 100 установок
- **[fixing-metadata](https://affpapa.org/nevibecode/skills/fixing-metadata)** — Проверяет и приводит в порядок метаданные страниц: заголовки, описания, canonical, Open Graph, карточки Twitter, иконки и JSON-LD.
  `npx skills add ibelick/ui-skills --skill fixing-metadata -a claude-code` · [исходник: ibelick/ui-skills](https://github.com/ibelick/ui-skills/blob/f511eae41c996e3953fbeabf95d38e4077d40711/skills/fixing-metadata/SKILL.md) · 20 000 установок
- **[keyword-research](https://affpapa.org/nevibecode/skills/every-app-keyword-research)** — Подбирает поисковые запросы через MCP-инструменты OpenSEO, оценивает метрики выдачи и сохраняет перспективные фразы в проект.
  `npx skills add every-app/open-seo --skill keyword-research -a claude-code` · [исходник: every-app/open-seo](https://github.com/every-app/open-seo/blob/46b815be34723e46ceeefe9b2b907bb62b62fd76/plugins/openseo/skills/keyword-research/SKILL.md) · 7 800 установок
- **[competitor-analysis](https://affpapa.org/nevibecode/skills/competitor-analysis)** — Скилл для Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI и OpenCode разбирает органический след одного конкурента: ключевые слова, бэклинки, темы контента и слабые места. Запускается по домену и выдаёт план действий.
  `npx skills add every-app/open-seo --skill competitor-analysis -a claude-code` · [исходник: every-app/open-seo](https://github.com/every-app/open-seo/blob/46b815be34723e46ceeefe9b2b907bb62b62fd76/plugins/openseo/skills/competitor-analysis/SKILL.md) · 7 500 установок
- **[seo-project-setup](https://affpapa.org/nevibecode/skills/seo-project-setup)** — Собирает контекст SEO-проекта: сайт, цели, позиционирование, конкурентов и важные страницы. Нужен перед работой других SEO-скиллов.
  `npx skills add every-app/open-seo --skill seo-project-setup -a claude-code` · [исходник: every-app/open-seo](https://github.com/every-app/open-seo/blob/46b815be34723e46ceeefe9b2b907bb62b62fd76/plugins/openseo/skills/seo-project-setup/SKILL.md) · 7 500 установок

<a name="topic-marketing"></a>
## Маркетинг и контент

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/marketing](https://affpapa.org/nevibecode/topic/marketing)

- **[copywriting](https://affpapa.org/nevibecode/skills/coreyhaines31-copywriting)** — Скилл для Claude Code, Codex, Cursor и других платформ помогает писать и переделывать текст страниц (главная, лендинг, прайсинг, описание фич).
  `npx skills add coreyhaines31/marketingskills --skill copywriting -a claude-code` · [исходник: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/8a3bde8083bd121971f61cba4bdbe5fd8c0eee7d/skills/copywriting/SKILL.md) · 257 200 установок · ставится ✓ 16.11 · A/B 16.11: -0,33 — раздувает meta description
- **[content-strategy](https://affpapa.org/nevibecode/skills/coreyhaines31-content-strategy)** — Скилл для Claude Code и Codex выстраивает редакционный план вокруг поискового спроса и задач клиентов. Помогает отобрать темы, которые приводят лиды или цитируются в сети.
  `npx skills add coreyhaines31/marketingskills --skill content-strategy -a claude-code` · [исходник: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/8a3bde8083bd121971f61cba4bdbe5fd8c0eee7d/skills/content-strategy/SKILL.md) · 179 200 установок
- **[copy-editing](https://affpapa.org/nevibecode/skills/coreyhaines31-copy-editing)** — Скилл для Claude Code и Codex: редактирует маркетинговые тексты, письма и описания без полной переписки.
  `npx skills add coreyhaines31/marketingskills --skill copy-editing -a claude-code` · [исходник: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/8a3bde8083bd121971f61cba4bdbe5fd8c0eee7d/skills/copy-editing/SKILL.md) · 163 500 установок
- **[brag](https://affpapa.org/nevibecode/skills/brag)** — Делает короткий проморолик о проекте по его исходному коду с помощью Hyperframes. Без развёрнутого сайта и скриншотов.
  `npx skills add latent-spaces/brag --skill brag -a claude-code` · [исходник: latent-spaces/brag](https://github.com/latent-spaces/brag/blob/669ab9286aa28b6c3ee30e75f181ee74319d012a/skills/brag/SKILL.md) · 24 600 установок
- **[baoyu-post-to-wechat](https://affpapa.org/nevibecode/skills/baoyu-post-to-wechat)** — Публикует статьи и графические посты в WeChat Official Account через API платформы или браузерный профиль Chrome.
  `npx skills add JimLiu/baoyu-skills --skill baoyu-post-to-wechat -a claude-code` · [исходник: jimliu/baoyu-skills](https://github.com/JimLiu/baoyu-skills/blob/ca703c2d7c2c4399a1dc0cf82224f8551e05a96d/skills/baoyu-post-to-wechat/SKILL.md) · 35 000 установок
- **[baoyu-post-to-weibo](https://affpapa.org/nevibecode/skills/baoyu-post-to-weibo)** — Скилл готовит обычные публикации и статьи для Weibo через Chrome. После заполнения формы пользователь сам проверяет запись и публикует её.
  `npx skills add JimLiu/baoyu-skills --skill baoyu-post-to-weibo -a claude-code` · [исходник: jimliu/baoyu-skills](https://github.com/JimLiu/baoyu-skills/blob/ca703c2d7c2c4399a1dc0cf82224f8551e05a96d/skills/baoyu-post-to-weibo/SKILL.md) · 22 100 установок
- **[crosspost](https://affpapa.org/nevibecode/skills/crosspost)** — Скилл для Claude Code и Codex, распределяет контент по X, LinkedIn, Threads и Bluesky с адаптацией под каждую платформу. Не публикует одинаковый текст везде — переделывает содержание под ограничения и аудиторию каждой сети.
  `npx skills add affaan-m/ECC --skill crosspost -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/crosspost/SKILL.md) · 5 900 установок
- **[investor-outreach](https://affpapa.org/nevibecode/skills/investor-outreach)** — Скилл для Claude Code и Codex, который составляет письма инвесторам, запросы на тёплые интро и апдейты по раунду. Генерирует персонализированные письма с конкретными просьбами, без общих фраз и размытых комплиментов.
  `npx skills add affaan-m/ECC --skill investor-outreach -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/investor-outreach/SKILL.md) · 5 900 установок
- **[reddit-automation](https://affpapa.org/nevibecode/skills/reddit-automation)** — Находит треды на Reddit, где людям нужен ваш продукт, и пишет короткие полезные ответы с раскрытием, что вы связаны с продуктом.
  `npx skills add flowkit-labs/skills --skill reddit-automation -a claude-code` · [исходник: flowkit-labs/skills](https://github.com/flowkit-labs/skills/blob/0c9e2b63f504a296a86e45ed3a60a426dd979ca6/reddit-automation/SKILL.md) · 1 400 000 установок
- **[google-ads-api-mcp-setup](https://affpapa.org/nevibecode/skills/google-ads-api-mcp-setup)** — Скилл помогает установить официальный Google Ads MCP Server и подключить ассистента к аккаунту для запросов о кампаниях и отчётности.
  `npx skills add google/skills --skill google-ads-api-mcp-setup -a claude-code` · [исходник: google/skills](https://github.com/google/skills/blob/e5250c8a02c28097b11a0c22d77143f4a0e5a408/skills/ads/google-ads-api-mcp-setup/SKILL.md) · 6 910 установок

<a name="topic-browser"></a>
## Браузер и парсинг

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/browser](https://affpapa.org/nevibecode/topic/browser)

- **[agent-browser](https://affpapa.org/nevibecode/skills/vercel-labs-agent-browser)** — Скилл для Claude Code управляет браузером по запросам на навигацию, заполнение форм и проверку веб-приложений. Агент также может запускать через него исследовательское тестирование и автоматизировать Electron-приложения.
  `npx skills add vercel-labs/agent-browser --skill agent-browser -a claude-code` · [исходник: vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/blob/f18b8bb5275ea2be22fca5e6856886827468f41e/skills/agent-browser/SKILL.md) · 1 500 000 установок · ставится ✓ 16.11
- **[browser-use](https://affpapa.org/nevibecode/skills/browser-use)** — Скилл для Claude Code управляет браузером через Chrome DevTools Protocol. Автоматизирует клики, заполнение форм, снятие скриншотов и сбор данных со страниц с JavaScript.
  `npx skills add browser-use/browser-use --skill browser-use -a claude-code` · [исходник: browser-use/browser-use](https://github.com/browser-use/browser-use/blob/480d0bd508ce10dcf27a4716f2f87355a08e8372/skills/browser-use/SKILL.md) · 99 800 установок · ставится ✓ 16.11
- **[playwright-cli](https://affpapa.org/nevibecode/skills/playwright-cli)** — Скилл, который даёт агенту браузер: открыть страницу, кликнуть по элементу, снять снимок и разобрать тесты Playwright.
  `npx skills add microsoft/playwright-cli --skill playwright-cli -a claude-code` · [исходник: microsoft/playwright-cli](https://github.com/microsoft/playwright-cli/blob/b21724888b8100b05ef8dee3a92f2bb03bf4dcde/skills/playwright-cli/SKILL.md) · 218 400 установок · ставится ✓ 16.11
- **[defuddle](https://affpapa.org/nevibecode/skills/defuddle)** — Скилл для Claude Code и других агентов преобразует веб-страницы в Markdown через Defuddle CLI, убирая навигацию и рекламу.
  `npx skills add kepano/obsidian-skills --skill defuddle -a claude-code` · [исходник: kepano/obsidian-skills](https://github.com/kepano/obsidian-skills/blob/3ccff5338ea700537839b21900aa5358a0402c98/skills/defuddle/SKILL.md) · 76 500 установок
- **[scrapling-official](https://affpapa.org/nevibecode/skills/scrapling-official)** — Скилл учит агента писать код на Scrapling: HTTP-запросы, stealth-браузер, обход Cloudflare, пауки и адаптивный парсер.
  `npx skills add D4Vinci/Scrapling --skill scrapling-official -a claude-code` · [исходник: d4vinci/scrapling](https://github.com/D4Vinci/Scrapling/blob/c5121c7c06a8595ed3a0a9b7b7dcd6802b5ebfc5/agent-skill/Scrapling-Skill/SKILL.md) · 6 900 установок
- **[ego-browser](https://affpapa.org/nevibecode/skills/ego-browser)** — Управляет браузером ego-lite для тестирования веб-приложений, кликов, ввода данных и снятия скриншотов. Включается при проверке сценариев в интерфейсе с авторизацией пользователя.
  `npx skills add citrolabs/ego-lite --skill ego-browser -a claude-code` · [исходник: citrolabs/ego-lite](https://github.com/citrolabs/ego-lite/blob/bacaece43900e8ca68eea3b6f1663835ea38df9e/skills/ego-browser/SKILL.md) · 17 500 установок
- **[opencli-browser](https://affpapa.org/nevibecode/skills/opencli-browser)** — Скилл управляет Chrome через OpenCLI: читает страницы, работает с авторизованными сайтами и собирает данные о сетевых запросах.
  `npx skills add jackwener/OpenCLI --skill opencli-browser -a claude-code` · [исходник: jackwener/opencli](https://github.com/jackwener/OpenCLI/blob/9bc5f5ca132ec4d4e48d7ee517d4303bf159e8e8/skills/opencli-browser/SKILL.md) · 20 800 установок
- **[browser-act](https://affpapa.org/nevibecode/skills/browser-act)** — Скилл подключает к агенту браузерный CLI: открыть страницу, дождаться JavaScript, вытащить данные, заполнить форму, снять скриншот. Пригодится там, где обычного fetch не хватает.
  `npx skills add browser-act/skills --skill browser-act -a claude-code` · [исходник: browser-act/skills](https://github.com/browser-act/skills/blob/593316aa0f8ccd88bdf745c92b24a50641701973/browser-act/SKILL.md) · 108 500 установок
- **[opencli-autofix](https://affpapa.org/nevibecode/skills/opencli-autofix)** — Чинит упавшие адаптеры OpenCLI при смене DOM или API сайтов. Агент собирает трейс ошибки, находит новые селекторы через браузер и патчит код.
  `npx skills add jackwener/OpenCLI --skill opencli-autofix -a claude-code` · [исходник: jackwener/opencli](https://github.com/jackwener/OpenCLI/blob/9bc5f5ca132ec4d4e48d7ee517d4303bf159e8e8/skills/opencli-autofix/SKILL.md) · 18 100 установок
- **[browser-act-skill-forge](https://affpapa.org/nevibecode/skills/browser-act-skill-forge)** — Разбирает сайт через browser-act и собирает готовый скилл с SKILL.md и Python-скриптами. Дальше сбор данных идёт без повторного исследования.
  `npx skills add browser-act/skills --skill browser-act-skill-forge -a claude-code` · [исходник: browser-act/skills](https://github.com/browser-act/skills/blob/593316aa0f8ccd88bdf745c92b24a50641701973/browser-act-skill-forge/SKILL.md) · 85 200 установок

<a name="topic-mobile"></a>
## Мобильная разработка

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/mobile](https://affpapa.org/nevibecode/topic/mobile)

- **[vercel-react-native-skills](https://affpapa.org/nevibecode/skills/vercel-react-native-skills)** — Скилл для Claude Code и других агентов: правила React Native и Expo по спискам, анимациям и навигации. Держит правки мобильного кода в одном стиле.
  `npx skills add vercel-labs/agent-skills --skill vercel-react-native-skills -a claude-code` · [исходник: vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/react-native-skills/SKILL.md) · 279 400 установок
- **[animate-expo](https://affpapa.org/nevibecode/skills/animate-expo)** — Создаёт мобильные анимации для React Native и Expo на базе Reanimated и Gesture Handler. Помогает избежать просадок кадров на реальных устройствах.
  `npx skills add emilkowalski/skills --skill animate-expo -a claude-code` · [исходник: emilkowalski/skills](https://github.com/emilkowalski/skills/blob/715c1807e08c497cfd1dc4feb450a2a3300ef2a9/skills/animate-expo/SKILL.md) · 185 800 установок · ставится ✓ 16.11
- **[aso](https://affpapa.org/nevibecode/skills/aso)** — Скилл для Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI и OpenCode анализирует карточки мобильных приложений. Помогает подготовить аудит страницы в App Store и Google Play.
  `npx skills add coreyhaines31/marketingskills --skill aso -a claude-code` · [исходник: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/8a3bde8083bd121971f61cba4bdbe5fd8c0eee7d/skills/aso/SKILL.md) · 86 800 установок
- **[swiftui-pro](https://affpapa.org/nevibecode/skills/swiftui-pro)** — Проверяет SwiftUI-код на устаревшие API, ошибки в структуре и проблемы доступности. Пригодится для ревью и доработки проектов на SwiftUI.
  `npx skills add twostraws/SwiftUI-Agent-Skill --skill swiftui-pro -a claude-code` · [исходник: twostraws/swiftui-agent-skill](https://github.com/twostraws/SwiftUI-Agent-Skill/blob/f2920b63995263f57b3e198674e89a602efba6d2/swiftui-pro/SKILL.md) · 38 300 установок
- **[orca-emulator-android](https://affpapa.org/nevibecode/skills/orca-emulator-android)** — Скилл для Claude Code, Codex, Cursor и других агентов управляет Android-устройством или эмулятором через adb прямо из сессии. Запускает AVD, отправляет тапы, свайпы, текст, устанавливает APK и читает дерево доступности.
  `npx skills add stablyai/orca --skill orca-emulator-android -a claude-code` · [исходник: stablyai/orca](https://github.com/stablyai/orca/blob/457c602b4f737d95dbdcf2f176f0beac8d9909b6/skills/orca-emulator-android/SKILL.md) · 6 000 установок
- **[swiftui-expert-skill](https://affpapa.org/nevibecode/skills/swiftui-expert-skill)** — Скилл для Claude Code, Codex, Cursor и других ИИ-ассистентов. Подключает правила ревью, оптимизации верстки и анализа трейсов Instruments при разработке на SwiftUI под iOS и macOS.
  `npx skills add AvdLee/SwiftUI-Agent-Skill --skill swiftui-expert-skill -a claude-code` · [исходник: avdlee/swiftui-agent-skill](https://github.com/AvdLee/SwiftUI-Agent-Skill/blob/62bd760f005093d1e2e4de5db156e456a5f96400/skills/swiftui-expert-skill/SKILL.md) · 36 700 установок
- **[android-clean-architecture](https://affpapa.org/nevibecode/skills/android-clean-architecture)** — Подсказывает агенту, как раскладывать Android- и KMP-проект по слоям: модули, зависимости, UseCase, репозитории, работа с Room, SQLDelight и Ktor.
  `npx skills add affaan-m/ECC --skill android-clean-architecture -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/android-clean-architecture/SKILL.md) · 6 900 установок
- **[liquid-glass-design](https://affpapa.org/nevibecode/skills/liquid-glass-design)** — Скилл для Claude и других ИИ-редакторов: подсказывает агенту, как собрать интерфейс в стиле Liquid Glass из iOS 26. Пригодится, если вы пишете SwiftUI, UIKit или WidgetKit под iOS 26+.
  `npx skills add affaan-m/ECC --skill liquid-glass-design -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/liquid-glass-design/SKILL.md) · 6 900 установок
- **[kotlin-coroutines-flows](https://affpapa.org/nevibecode/skills/kotlin-coroutines-flows)** — Скилл подсказывает паттерны Kotlin Coroutines и Flow для Android и KMP. Пригодится при отладке отмены, параллельных задач и тестов.
  `npx skills add affaan-m/ECC --skill kotlin-coroutines-flows -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/kotlin-coroutines-flows/SKILL.md) · 6 400 установок
- **[app-store-screenshots](https://affpapa.org/nevibecode/skills/parthjadhav-app-store-screenshots)** — Собирает редактор на Next.js и ShadCN, в котором вы верстаете и выгружаете скриншоты для App Store и Google Play.
  `npx skills add ParthJadhav/app-store-screenshots --skill app-store-screenshots -a claude-code` · [исходник: parthjadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots/blob/e889033b68f418952cc65ba897fe2b1ec63d1564/skills/app-store-screenshots/SKILL.md) · 16 200 установок

<a name="topic-gamedev"></a>
## Геймдев и 3D: Unity, Unreal, Godot, Blender

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/gamedev](https://affpapa.org/nevibecode/topic/gamedev)

- **[gcode](https://affpapa.org/nevibecode/skills/gcode)** — Слайсит модели .stl, .3mf и .obj в .gcode или .gcode.3mf через OrcaSlicer. Принтер скилл не подключает.
  `npx skills add earthtojake/text-to-cad --skill gcode -a claude-code` · [исходник: earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad/blob/4d42cb0bd9a61b46254bc8cf9bd9ae1f45c3295b/skills/gcode/SKILL.md) · 10 500 установок
- **[bambu-labs](https://affpapa.org/nevibecode/skills/bambu-labs)** — Передаёт файл на печать в принтеры Bambu Lab через Bambu Connect или Bambu Studio. Агент открывает файл в приложении, а принтер и запуск печати выбирает уже человек.
  `npx skills add earthtojake/text-to-cad --skill bambu-labs -a claude-code` · [исходник: earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad/blob/4d42cb0bd9a61b46254bc8cf9bd9ae1f45c3295b/skills/bambu-labs/SKILL.md) · 10 200 установок
- **[img2threejs](https://affpapa.org/nevibecode/skills/img2threejs)** — Собирает процедурную модель Three.js по изображению объекта или персонажа. Нужен для реконструкции, подготовки к анимации и генерации кода.
  `npx skills add img2threejs/img2threejs --skill img2threejs -a claude-code` · [исходник: img2threejs/img2threejs](https://github.com/img2threejs/img2threejs/blob/0c0c49bc168e648dbaf9c8c080474de0b3a941b6/SKILL.md) · 3 100 установок
- **[dfam-check](https://affpapa.org/nevibecode/skills/dfam-check)** — Проверяет 3D-сетки на соответствие правилам аддитивного производства перед печатью. Анализирует толщину стенок, свесы и ориентацию деталей для FDM, SLS, SLA, PBF и MJF.
  `npx skills add earthtojake/text-to-cad --skill dfam-check -a claude-code` · [исходник: earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad/blob/4d42cb0bd9a61b46254bc8cf9bd9ae1f45c3295b/skills/dfam-check/SKILL.md) · 5 200 установок
- **[threejs-geometry](https://affpapa.org/nevibecode/skills/threejs-geometry)** — Скилл учит ИИ-агента создавать стандартные и процедурные геометрии three.js, настраивать буферные атрибуты и генерировать 3D-текст.
  `npx skills add CloudAI-X/threejs-skills --skill threejs-geometry -a claude-code` · [исходник: cloudai-x/threejs-skills](https://github.com/CloudAI-X/threejs-skills/blob/0e181866f095b5f06d005133876e926515390d95/skills/threejs-geometry/SKILL.md) · 20 600 установок
- **[threejs-lighting](https://affpapa.org/nevibecode/skills/threejs-lighting)** — Скилл содержит правила настройки света, теней и физических единиц в Three.js r186. Он помогает выставить параметры для WebGLRenderer или WebGPURenderer.
  `npx skills add CloudAI-X/threejs-skills --skill threejs-lighting -a claude-code` · [исходник: cloudai-x/threejs-skills](https://github.com/CloudAI-X/threejs-skills/blob/0e181866f095b5f06d005133876e926515390d95/skills/threejs-lighting/SKILL.md) · 19 400 установок
- **[fal-3d](https://affpapa.org/nevibecode/skills/fal-3d)** — Скилл для создания 3D-моделей из текста или изображений через fal.ai. Пригодится для игровых ассетов, AR-превью, прототипов товаров и концептов.
  `npx skills add nexu-io/open-design --skill fal-3d -a claude-code` · [исходник: nexu-io/open-design](https://github.com/nexu-io/open-design/blob/59e4f2ae85de7e7318a5e6bdcf3a34584c4b7582/skills/fal-3d/SKILL.md) · 3 000 установок
- **[game-feel](https://affpapa.org/nevibecode/skills/game-feel)** — Скилл учит агента добавлять отклик к игровым действиям: тряску камеры, стоп-кадр, твины с easing, сквош и отброс. Для случаев, когда механика работает, но ощущается ватной.
  `npx skills add gamedev-skills/awesome-gamedev-agent-skills --skill game-feel -a claude-code` · [исходник: gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/4cce500ce1a779b12fdd824be581c7d2ab4e7ba2/skills/disciplines/game-feel/SKILL.md) · 17 600 установок
- **[game-ui-ux](https://affpapa.org/nevibecode/skills/game-ui-ux)** — Архитектурный скилл для создания адаптивных игровых интерфейсов, стека экранов и навигации с геймпада без покадрового опроса состояния.
  `npx skills add gamedev-skills/awesome-gamedev-agent-skills --skill game-ui-ux -a claude-code` · [исходник: gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/4cce500ce1a779b12fdd824be581c7d2ab4e7ba2/skills/disciplines/game-ui-ux/SKILL.md) · 17 500 установок
- **[level-design](https://affpapa.org/nevibecode/skills/level-design)** — Скилл для Claude Code помогает спланировать и собрать игровой уровень: от серого блокинга до проверки маршрутов, темпа и боевых сцен. Включается при работе над планировкой, критическим путём или встречами с противниками.
  `npx skills add gamedev-skills/awesome-gamedev-agent-skills --skill level-design -a claude-code` · [исходник: gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/4cce500ce1a779b12fdd824be581c7d2ab4e7ba2/skills/disciplines/level-design/SKILL.md) · 14 700 установок

<a name="topic-science"></a>
## Наука и исследования

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/science](https://affpapa.org/nevibecode/topic/science)

- **[academic-paper](https://affpapa.org/nevibecode/skills/academic-paper)** — Скилл разворачивает конвейер из 12 агентов для подготовки научных статей в 11 режимах. Помогает пройти путь от поиска литературы и плана до проверки цитат и ответа рецензентам.
  `npx skills add Imbad0202/academic-research-skills --skill academic-paper -a claude-code` · [исходник: imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills/blob/6d9388674de1ad0437ad95db3d52f92b92204d84/academic-paper/SKILL.md) · 11 600 установок
- **[nature-figure](https://affpapa.org/nevibecode/skills/nature-figure)** — Скилл для Claude Code и Codex собирает, правит и проверяет научные рисунки на Python или R. Готовит графики для submission в журнал, а не для отчёта.
  `npx skills add Yuan1z0825/nature-skills --skill nature-figure -a claude-code` · [исходник: yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills/blob/7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8/skills/nature-figure/SKILL.md) · 20 300 установок
- **[academic-paper-reviewer](https://affpapa.org/nevibecode/skills/academic-paper-reviewer)** — Скилл имитирует коллегиальную проверку научной статьи через пять ролей. Пригодится для рецензии, повторной проверки правок и оценки методологии.
  `npx skills add Imbad0202/academic-research-skills --skill academic-paper-reviewer -a claude-code` · [исходник: imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills/blob/6d9388674de1ad0437ad95db3d52f92b92204d84/academic-paper-reviewer/SKILL.md) · 10 500 установок
- **[nature-citation](https://affpapa.org/nevibecode/skills/nature-citation)** — Скилл для Claude Code и Codex ищет статьи из Nature и семейства CNS, связывает утверждения рукописи с источниками и готовит экспорт для менеджера ссылок. Работает в границах этих журналов.
  `npx skills add Yuan1z0825/nature-skills --skill nature-citation -a claude-code` · [исходник: yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills/blob/7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8/skills/nature-citation/SKILL.md) · 16 900 установок
- **[nature-academic-search](https://affpapa.org/nevibecode/skills/nature-academic-search)** — Ищет научные публикации, проверяет ссылки и собирает стратегии MeSH. Пригодится для работы с источниками и файлами библиографии.
  `npx skills add Yuan1z0825/nature-skills --skill nature-academic-search -a claude-code` · [исходник: yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills/blob/7bff1d0539c0dfad6c30178bb93ce6dd8a5cebf8/skills/nature-academic-search/SKILL.md) · 16 700 установок
- **[deep-research](https://affpapa.org/nevibecode/skills/imbad0202-deep-research)** — Скилл запускает команду из 13 агентов для академического исследования по любой теме: от формулировки вопроса до готового отчёта в APA 7.0.
  `npx skills add Imbad0202/academic-research-skills --skill deep-research -a claude-code` · [исходник: imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills/blob/6d9388674de1ad0437ad95db3d52f92b92204d84/deep-research/SKILL.md) · 8 200 установок
- **[paper-context-resolver](https://affpapa.org/nevibecode/skills/paper-context-resolver)** — Скилл ищет в первоисточниках статьи один недостающий для воспроизведения факт: сплит датасета, предобработку, протокол оценки. Нужен, когда README молчит.
  `npx skills add lllllllama/RigorPilot-Skills --skill paper-context-resolver -a claude-code` · [исходник: lllllllama/rigorpilot-skills](https://github.com/lllllllama/RigorPilot-Skills/blob/fb3ccdf5aa64b1fa5b1d0463e666a8bc8bc26e01/skills/paper-context-resolver/SKILL.md) · 499 800 установок
- **[read-arxiv-paper](https://affpapa.org/nevibecode/skills/read-arxiv-paper)** — Скилл читает исходники статьи arXiv и готовит её разбор в Markdown. Пригодится для разбора научной работы в контексте nanochat.
  `npx skills add karpathy/nanochat --skill read-arxiv-paper -a claude-code` · [исходник: karpathy/nanochat](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/.claude/skills/read-arxiv-paper/SKILL.md) · 2 900 установок
- **[ai-research-reproduction](https://affpapa.org/nevibecode/skills/ai-research-reproduction)** — Скилл ведёт от чтения README до проверяемого запуска модели и собирает отчёт с командами, логами и отклонениями. Пригодится для воспроизведения эксперимента в конкретном репозитории.
  `npx skills add lllllllama/RigorPilot-Skills --skill ai-research-reproduction -a claude-code` · [исходник: lllllllama/rigorpilot-skills](https://github.com/lllllllama/RigorPilot-Skills/blob/fb3ccdf5aa64b1fa5b1d0463e666a8bc8bc26e01/skills/ai-research-reproduction/SKILL.md) · 359 800 установок
- **[start](https://affpapa.org/nevibecode/skills/anthropics-start)** — Проверяет подключённые MCP-серверы и доступные инструменты биоисследований. Помогает сориентироваться в окружении плагина перед началом проекта.
  `npx skills add anthropics/knowledge-work-plugins --skill start -a claude-code` · [исходник: anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/bio-research/skills/start/SKILL.md) · 5 000 установок

<a name="topic-git"></a>
## Git и GitHub

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/git](https://affpapa.org/nevibecode/topic/git)

- **[triage](https://affpapa.org/nevibecode/skills/triage)** — Скилл проводит issue и внешние PR через роли триажа, проверку и подготовку брифа для агента. Подойдёт мейнтейнеру, который разбирает очередь задач.
  `npx skills add mattpocock/skills --skill triage -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/triage/SKILL.md) · 990 453 установки · ставится ✓ 16.11
- **[git-guardrails-claude-code](https://affpapa.org/nevibecode/skills/git-guardrails-claude-code)** — Скилл ставит хук Claude Code, который останавливает опасные Git-команды до их запуска. Нужен, если агент не должен делать push или удалять изменения.
  `npx skills add mattpocock/skills --skill git-guardrails-claude-code -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/misc/git-guardrails-claude-code/SKILL.md) · 499 069 установок · ставится ✓ 16.11
- **[using-git-worktrees](https://affpapa.org/nevibecode/skills/using-git-worktrees)** — Готовит изолированное рабочее дерево перед доработкой или выполнением плана. Проверяет текущий репозиторий, выбирает нативные средства платформы либо Git.
  `npx skills add obra/superpowers --skill using-git-worktrees -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-git-worktrees/SKILL.md) · 217 153 установки · ставится ✓ 16.11
- **[finishing-a-development-branch](https://affpapa.org/nevibecode/skills/finishing-a-development-branch)** — Скилл проверяет тесты и помогает выбрать, как завершить работу в ветке: слить её, открыть Pull Request или оставить как есть.
  `npx skills add obra/superpowers --skill finishing-a-development-branch -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/finishing-a-development-branch/SKILL.md) · 214 439 установок · ставится ✓ 16.11
- **[caveman-commit](https://affpapa.org/nevibecode/skills/caveman-commit)** — Скилл для Claude Code и Codex формирует краткие коммит-сообщения по стандарту Conventional Commits. Держит суть изменений без лишних слов.
  `npx skills add JuliusBrussee/caveman --skill caveman-commit -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/3dc497a7f858c774d6e15b25e8c6120ef3a0eda8/skills/caveman-commit/SKILL.md) · 438 700 установок · ставится ✓ 16.11
- **[pr](https://affpapa.org/nevibecode/skills/pr)** — Помогает Claude Code собирать тело PR по заданной структуре: краткое резюме, доказательства и оценка риска слияния.
  `npx skills add mattpocock/skills --skill pr -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/pr/SKILL.md) · 167 125 установок · ставится ✓ 16.11
- **[git-workflow-and-versioning](https://affpapa.org/nevibecode/skills/git-workflow-and-versioning)** — Скилл, который наводит порядок в git-процессе: атомарные коммиты, короткоживущие ветки, сообщения, объясняющие зачем, а не что. Включается при любом изменении кода, которое агент готовит к коммиту.
  `npx skills add addyosmani/agent-skills --skill git-workflow-and-versioning -a claude-code` · [исходник: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/301b02b12bff98e4688e6984af6556802322bbde/skills/git-workflow-and-versioning/SKILL.md) · 73 100 установок
- **[gh-fix-ci](https://affpapa.org/nevibecode/skills/openai-gh-fix-ci)** — Находит упавшие проверки GitHub Actions в пулл-реквесте, собирает логи ошибок и готовит план исправлений. Скилл применяет правки только после подтверждения.
  `npx skills add openai/skills --skill gh-fix-ci -a claude-code` · [исходник: openai/skills](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/gh-fix-ci/SKILL.md) · 12 000 установок
- **[github](https://affpapa.org/nevibecode/skills/github)** — Скилл для работы с GitHub через CLI на Claude Code: просмотр и создание PR, управление issues, проверка статуса CI. Доступен также на Codex, Cursor, GitHub Copilot, Gemini CLI и OpenCode.
  `npx skills add openclaw/openclaw --skill github -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/f683d5ffd214c84d2b75d91b82cde3aabc05fab2/skills/github/SKILL.md) · 6 100 установок
- **[gh-issues](https://affpapa.org/nevibecode/skills/gh-issues)** — Скилл находит GitHub issues, запускает фоновых агентов для исправлений и открывает PR. Подходит для потока от issue до готового pull request.
  `npx skills add openclaw/openclaw --skill gh-issues -a claude-code` · [исходник: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/f683d5ffd214c84d2b75d91b82cde3aabc05fab2/skills/gh-issues/SKILL.md) · 5 000 установок

<a name="topic-productivity"></a>
## Заметки, задачи и проекты

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/productivity](https://affpapa.org/nevibecode/topic/productivity)

- **[find-skills](https://affpapa.org/nevibecode/skills/find-skills)** — Скилл для Claude Code и других агентов: ищет и устанавливает готовые скиллы через каталог skills.sh. Находит специализированный воркфлоу под рабочую задачу.
  `npx skills add vercel-labs/skills --skill find-skills -a claude-code` · [исходник: vercel-labs/skills](https://github.com/vercel-labs/skills/blob/cef06daf8efac89fbeefb2f53ddb0795d73bf10b/skills/find-skills/SKILL.md) · 4 400 000 установок · ставится ✓ 16.11
- **[grill-me](https://affpapa.org/nevibecode/skills/grill-me)** — Скилл проводит жёсткое интервью по плану или дизайну, чтобы найти пробелы и уточнить решения. Подойдёт перед началом разработки.
  `npx skills add mattpocock/skills --skill grill-me -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/grill-me/SKILL.md) · 1 424 476 установок · ставится ✓ 16.11
- **[handoff](https://affpapa.org/nevibecode/skills/handoff)** — Собирает текущий диалог в документ передачи, чтобы другой агент продолжил работу с нужным контекстом. Нужен при смене сессии или исполнителя.
  `npx skills add mattpocock/skills --skill handoff -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/handoff/SKILL.md) · 1 038 491 установка · ставится ✓ 16.11
- **[grilling](https://affpapa.org/nevibecode/skills/grilling)** — Стресс-тестирует план, решение или идею сериями уточняющих вопросов. Подходит, когда нужно вскрыть допущения до начала работы.
  `npx skills add mattpocock/skills --skill grilling -a claude-code` · [исходник: mattpocock/skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/grilling/SKILL.md) · 979 543 установки · ставится ✓ 16.11
- **[using-superpowers](https://affpapa.org/nevibecode/skills/using-superpowers)** — Проверяет подходящие скиллы до любого ответа или действия агента. Нужен, когда хотите задать единый порядок работы с задачами.
  `npx skills add obra/superpowers --skill using-superpowers -a claude-code` · [исходник: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-superpowers/SKILL.md) · 270 479 установок · ставится ✓ 16.11
- **[caveman](https://affpapa.org/nevibecode/skills/juliusbrussee-caveman)** — Убирает вежливые фразы и лишние слова из ответов ИИ-агента, сохраняя код и факты. Включается командой /caveman и действует всю сессию.
  `npx skills add JuliusBrussee/caveman --skill caveman -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/3dc497a7f858c774d6e15b25e8c6120ef3a0eda8/skills/caveman/SKILL.md) · 630 200 установок · ставится ✓ 16.11
- **[ponytail-help](https://affpapa.org/nevibecode/skills/ponytail-help)** — Скилл для Claude Code: выводит справку по режимам, командам и скиллам ponytail прямо в диалоге с ассистентом. Подсказывает синтаксис без перехода в браузер.
  `npx skills add DietrichGebert/ponytail --skill ponytail-help -a claude-code` · [исходник: dietrichgebert/ponytail](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail-help/SKILL.md) · 56 400 установок · ставится ✓ 16.11
- **[ponytail-gain](https://affpapa.org/nevibecode/skills/ponytail-gain)** — Выводит бенчмарк экономии строк кода, токенов, денег и времени в Ponytail. Помогает оценить результаты тестов перед использованием набора скиллов.
  `npx skills add DietrichGebert/ponytail --skill ponytail-gain -a claude-code` · [исходник: dietrichgebert/ponytail](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail-gain/SKILL.md) · 54 200 установок · ставится ✓ 16.11
- **[caveman-learn](https://affpapa.org/nevibecode/skills/caveman-learn)** — Скилл разбирает отчёт Caveman, предлагает сокращение затрат на токены и просит согласие перед каждым изменением. Подходит для тяжёлого CLAUDE.md и повторяемого контекста.
  `npx skills add JuliusBrussee/caveman --skill caveman-learn -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/3dc497a7f858c774d6e15b25e8c6120ef3a0eda8/skills/caveman-learn/SKILL.md) · 128 200 установок · ставится ✓ 16.11
- **[lean-build](https://affpapa.org/nevibecode/skills/lean-build)** — Удерживает агента от усложнения архитектуры при создании новых фич и интеграций. Скилл формулирует критерии приёмки, убирает лишний код и останавливает работу по факту проверки.
  `npx skills add JuliusBrussee/caveman --skill lean-build -a claude-code` · [исходник: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/3dc497a7f858c774d6e15b25e8c6120ef3a0eda8/skills/lean-build/SKILL.md) · 125 800 установок · ставится ✓ 16.11

<a name="topic-finance"></a>
## Финансы и бизнес

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/finance](https://affpapa.org/nevibecode/topic/finance)

- **[market-research](https://affpapa.org/nevibecode/skills/affaan-m-market-research)** — Скилл для Claude Code и Codex: задаёт рамки рыночных исследований, сравнения конкурентов и проверки инвесторов. Обосновывает решение, а не собирает отчёт.
  `npx skills add affaan-m/ECC --skill market-research -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/market-research/SKILL.md) · 7 600 установок
- **[investor-materials](https://affpapa.org/nevibecode/skills/investor-materials)** — Помогает готовить питч-деки, ванпейджеры, финмодели и заявки в акселераторы. Следит за тем, чтобы метрики и суммы сходились во всех документах раунда.
  `npx skills add affaan-m/ECC --skill investor-materials -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/investor-materials/SKILL.md) · 6 200 установок
- **[customs-trade-compliance](https://affpapa.org/nevibecode/skills/customs-trade-compliance)** — Классифицирует товары по кодам ТН ВЭД (HS/HTS), проверяет санкционные списки и готовит таможенные документы для США, ЕС и Великобритании.
  `npx skills add affaan-m/ECC --skill customs-trade-compliance -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/customs-trade-compliance/SKILL.md) · 5 900 установок
- **[earnings-analysis](https://affpapa.org/nevibecode/skills/earnings-analysis)** — Скилл для Claude Code, Codex, Cursor, Copilot, Gemini CLI и OpenCode создаёт отчёты по квартальным результатам компаний из equity research: 8–12 страниц, таблицы, графики, анализ beat/miss.
  `npx skills add anthropics/financial-services --skill earnings-analysis -a claude-code` · [исходник: anthropics/financial-services](https://github.com/anthropics/financial-services/blob/60565064557ca77b12f62aa7877f365d111c129d/plugins/agent-plugins/earnings-reviewer/skills/earnings-analysis/SKILL.md) · 3 700 установок
- **[equity-research](https://affpapa.org/nevibecode/skills/equity-research)** — Скилл для Claude Code, Codex, Cursor и других IDE берёт данные из MCP-инструментов и собирает структурированный инвестиционный снапшот по акции.
  `npx skills add anthropics/financial-services --skill equity-research -a claude-code` · [исходник: anthropics/financial-services](https://github.com/anthropics/financial-services/blob/60565064557ca77b12f62aa7877f365d111c129d/plugins/partner-built/lseg/skills/equity-research/SKILL.md) · 3 400 установок
- **[consulting-analysis](https://affpapa.org/nevibecode/skills/consulting-analysis)** — Скилл для Claude Code и Codex, который готовит консалтинговые отчёты в Markdown в два этапа. Сначала строит план исследования и список данных, потом сводит собранные факты и графики в текст.
  `npx skills add bytedance/deer-flow --skill consulting-analysis -a claude-code` · [исходник: bytedance/deer-flow](https://github.com/bytedance/deer-flow/blob/4a27b133f81dfa621bf17635f2659bef2eebb7fd/skills/public/consulting-analysis/SKILL.md) · 3 100 установок
- **[financial-statements](https://affpapa.org/nevibecode/skills/financial-statements)** — Формирует финансовые отчёты с сопоставлением периодов и анализом отклонений. Нужен для P&L, закрытия периода и сравнения факта с бюджетом.
  `npx skills add anthropics/knowledge-work-plugins --skill financial-statements -a claude-code` · [исходник: anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/finance/skills/financial-statements/SKILL.md) · 4 800 установок
- **[backtesting-frameworks](https://affpapa.org/nevibecode/skills/backtesting-frameworks)** — Помогает строить бэктесты торговых стратегий с учётом смещения заглядывания в будущее, выживших активов и торговых издержек. Пригодится для проверки стратегии на исторических данных.
  `npx skills add wshobson/agents --skill backtesting-frameworks -a claude-code` · [исходник: wshobson/agents](https://github.com/wshobson/agents/blob/4bde3168b43c0655c4d00ea2726e631719908a6d/plugins/quantitative-trading/skills/backtesting-frameworks/SKILL.md) · 16 710 установок
- **[dcf-model](https://affpapa.org/nevibecode/skills/dcf-model)** — Строит институциональную DCF-модель для оценки компании: берёт данные из отчётности SEC и аналитических отчётов, считает WACC и денежные потоки, выдаёт Excel с анализом чувствительности.
  `npx skills add anthropics/financial-services --skill dcf-model -a claude-code` · [исходник: anthropics/financial-services](https://github.com/anthropics/financial-services/blob/60565064557ca77b12f62aa7877f365d111c129d/plugins/agent-plugins/model-builder/skills/dcf-model/SKILL.md) · 2 600 установок
- **[reconciliation](https://affpapa.org/nevibecode/skills/reconciliation)** — Сверяет остатки GL с субледжером, банковской выпиской или данными третьей стороны. Нужен для поиска расхождений.
  `npx skills add anthropics/knowledge-work-plugins --skill reconciliation -a claude-code` · [исходник: anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/finance/skills/reconciliation/SKILL.md) · 3 700 установок

<a name="topic-languages"></a>
## Языки программирования

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/languages](https://affpapa.org/nevibecode/topic/languages)

- **[write-swift](https://affpapa.org/nevibecode/skills/write-swift)** — Скилл помогает писать, проверять и переносить код на Swift с учётом модели языка. Подойдёт, когда нужно разобраться с конкурентностью, ошибкой или циклом удержания объектов.
  `npx skills add emilkowalski/skills --skill write-swift -a claude-code` · [исходник: emilkowalski/skills](https://github.com/emilkowalski/skills/blob/715c1807e08c497cfd1dc4feb450a2a3300ef2a9/skills/write-swift/SKILL.md) · 165 900 установок · ставится ✓ 16.11
- **[typescript-advanced-types](https://affpapa.org/nevibecode/skills/typescript-advanced-types)** — Помогает агенту писать сложную типизацию TypeScript: generics, conditional types и преобразования типов. Нужен для библиотек, API-клиентов и строгих конфигураций.
  `npx skills add wshobson/agents --skill typescript-advanced-types -a claude-code` · [исходник: wshobson/agents](https://github.com/wshobson/agents/blob/4bde3168b43c0655c4d00ea2726e631719908a6d/plugins/javascript-typescript/skills/typescript-advanced-types/SKILL.md) · 92 169 установок
- **[python-patterns](https://affpapa.org/nevibecode/skills/affaan-m-python-patterns)** — Подсказывает агенту, как писать и ревьюить Python: идиомы, аннотации типов, обработка исключений, контекстные менеджеры.
  `npx skills add affaan-m/ECC --skill python-patterns -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/python-patterns/SKILL.md) · 7 200 установок
- **[golang-patterns](https://affpapa.org/nevibecode/skills/golang-patterns)** — Скилл для Claude Code и других платформ подсказывает идиоматичные паттерны Go при написании, ревью и рефакторинге кода. Проверяет структуру пакета и обработку ошибок.
  `npx skills add affaan-m/ECC --skill golang-patterns -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/golang-patterns/SKILL.md) · 6 900 установок
- **[cpp-coding-standards](https://affpapa.org/nevibecode/skills/cpp-coding-standards)** — Скилл для ИИ-агентов, который подтягивает написание и ревью C++ к C++ Core Guidelines: RAII, иммутабельность, строгая типизация.
  `npx skills add affaan-m/ECC --skill cpp-coding-standards -a claude-code` · [исходник: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/cpp-coding-standards/SKILL.md) · 6 700 установок
- **[python-performance-optimization](https://affpapa.org/nevibecode/skills/python-performance-optimization)** — Скилл помогает профилировать Python-код, находить узкие места CPU и памяти. Подходит, когда приложение медленно отвечает или тратит слишком много ресурсов.
  `npx skills add wshobson/agents --skill python-performance-optimization -a claude-code` · [исходник: wshobson/agents](https://github.com/wshobson/agents/blob/4bde3168b43c0655c4d00ea2726e631719908a6d/plugins/python-development/skills/python-performance-optimization/SKILL.md) · 35 675 установок
- **[design-patterns](https://affpapa.org/nevibecode/skills/design-patterns)** — Подбирает архитектурные паттерны Rust для CLI-модулей фильтрации RTK. Помогает структурировать парсеры вывода, конфигурации и работу с ресурсами.
  `npx skills add rtk-ai/rtk --skill design-patterns -a claude-code` · [исходник: rtk-ai/rtk](https://github.com/rtk-ai/rtk/blob/2a786dca60fa4759f4f8381262a6a3b98256667a/.claude/skills/design-patterns/SKILL.md) · 2 000 установок
- **[python-design-patterns](https://affpapa.org/nevibecode/skills/python-design-patterns)** — Помогает выбирать структуру Python-кода, разделять обязанности и решать, когда выносить повторяющуюся логику в абстракцию. Пригодится при проектировании и рефакторинге.
  `npx skills add wshobson/agents --skill python-design-patterns -a claude-code` · [исходник: wshobson/agents](https://github.com/wshobson/agents/blob/4bde3168b43c0655c4d00ea2726e631719908a6d/plugins/python-development/skills/python-design-patterns/SKILL.md) · 22 842 установки
- **[typescript-expert](https://affpapa.org/nevibecode/skills/typescript-expert)** — Скилл для Claude Code и других IDE: разбирает типы TypeScript, ускоряет проверку и помогает с миграциями. Запускается на каждом PR, диагностирует медленную компиляцию и разрешает ошибки вроде «The inferred type cannot be named».
  `npx skills add sickn33/agentic-awesome-skills --skill typescript-expert -a claude-code` · [исходник: sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills/blob/560b762c309d6b96315855d7968727d3bca7df20/skills/typescript-expert/SKILL.md) · 12 800 установок
- **[cardputer-buddy](https://affpapa.org/nevibecode/skills/cardputer-buddy)** — Помогает разрабатывать MicroPython-приложения для Cardputer-Adv. Скилл обновляет отдельные скрипты по кабелю, читает логи и запускает команды в REPL без перепрошивки платы.
  `npx skills add anthropics/claude-plugins-official --skill cardputer-buddy -a claude-code` · [исходник: anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official/blob/b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6/plugins/cwc-makers/skills/cardputer-buddy/SKILL.md) · 2 897 установок

<a name="topic-telegram"></a>
## Telegram-боты

Вся тема в каталоге: [https://affpapa.org/nevibecode/topic/telegram](https://affpapa.org/nevibecode/topic/telegram)

- **[telegram-bot-builder](https://affpapa.org/nevibecode/skills/sickn33-telegram-bot-builder)** — Скилл помогает спроектировать Telegram-бота: от структуры проекта и кнопок до платежей и вебхуков. Пригодится при запуске нового бота или подготовке его к продакшену.
  `npx skills add sickn33/agentic-awesome-skills --skill telegram-bot-builder -a claude-code` · [исходник: sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills/blob/560b762c309d6b96315855d7968727d3bca7df20/skills/telegram-bot-builder/SKILL.md) · 3 800 установок
- **[telegram-bot](https://affpapa.org/nevibecode/skills/telegram-bot)** — Скилл для Claude Code и других платформ: чат-боты, уведомления, ИИ-ассистенты и автоматизация групп. Собирает обработчики сообщений и сценарии.
  `npx skills add claude-office-skills/skills --skill telegram-bot -a claude-code` · [исходник: claude-office-skills/skills](https://github.com/claude-office-skills/skills/blob/9c4c7d5cd2813a8936bf2c9fdb174ea883b85a11/telegram-bot/SKILL.md) · 6 500 установок
- **[tg-bot-binding](https://affpapa.org/nevibecode/skills/tg-bot-binding)** — Скилл помогает подключить Telegram-бота к Starchild, подтвердить владение и наладить отправку сообщений через сканирование QR-кода или токен BotFather.
  `npx skills add Starchild-ai-agent/official-skills --skill tg-bot-binding -a claude-code` · [исходник: starchild-ai-agent/official-skills](https://github.com/Starchild-ai-agent/official-skills/blob/0996b6d9872e0513160d4436e8f615b8097bcf59/tg-bot-binding/SKILL.md) · 2 200 установок
- **[meta](https://affpapa.org/nevibecode/skills/meta)** — Регистрирует обработчик команды /meta, чтобы запускать Claude Code Agent SDK прямо в каталоге бота telegram_agent и править его код из чата.
  `npx skills add glebis/claude-skills --skill meta -a claude-code` · [исходник: glebis/claude-skills](https://github.com/glebis/claude-skills/blob/4d37d3b0af1f98cb4ac820d9abbce95e38e909fb/meta/SKILL.md) · 228 установок
- **[tg-ws-proxy-telegram-socks5](https://affpapa.org/nevibecode/skills/tg-ws-proxy-telegram-socks5)** — Помогает настроить локальный SOCKS5-прокси для Telegram Desktop с туннелированием трафика в дата-центры через WebSocket. Пригодится при сетевых блокировках мессенджера.
  `npx skills add reason-machines/trending-skills --skill tg-ws-proxy-telegram-socks5 -a claude-code` · [исходник: reason-machines/trending-skills](https://github.com/reason-machines/trending-skills/blob/c61b1a456af4015e9a367e0245292281bb3c87d9/skills/tg-ws-proxy-telegram-socks5/SKILL.md) · 889 установок
- **[telegram-group-analytics-bot](https://affpapa.org/nevibecode/skills/telegram-group-analytics-bot)** — Скилл собирает статистику Telegram-группы: прирост участников, сообщения, активность по часам и автоматические отчёты.
  `npx skills add reason-machines/data-skills --skill telegram-group-analytics-bot -a claude-code` · [исходник: reason-machines/data-skills](https://github.com/reason-machines/data-skills/blob/25d6ee79eea935ef4be1ee375a5777b2ad259f0a/skills/telegram-group-analytics-bot/SKILL.md) · 614 установок
- **[telegram-group-statistics-analytics-bot](https://affpapa.org/nevibecode/skills/telegram-group-statistics-analytics-bot)** — Скилл настраивает бота для сбора метрик в группах Telegram, учёта активности участников и рассылки отчётов. Пригодится администраторам чатов для контроля вовлечённости.
  `npx skills add reason-machines/data-skills --skill telegram-group-statistics-analytics-bot -a claude-code` · [исходник: reason-machines/data-skills](https://github.com/reason-machines/data-skills/blob/25d6ee79eea935ef4be1ee375a5777b2ad259f0a/skills/telegram-group-statistics-analytics-bot/SKILL.md) · 609 установок
- **[interactive-bot](https://affpapa.org/nevibecode/skills/interactive-bot)** — Скилл объясняет устройство Telegram-бота Gmail Commander: слэш-команды для почты, ИИ-роутинг свободного текста через MCP, сессии compose/reply.
  `npx skills add terrylica/cc-skills --skill interactive-bot -a claude-code` · [исходник: terrylica/cc-skills](https://github.com/terrylica/cc-skills/blob/0ca36f7260a3eb5de13a1b684509c4ecd5fe819b/plugins/gmail-commander/skills/interactive-bot/SKILL.md) · 114 установок

## Обновление и лицензия

Список собирает `scripts/build.py` из базы каталога; снимок проверок — `data/checks-2026-11-16.json`. Сборка от 2026-11-16. Число установок — по данным источника, из которого карточка пришла в каталог. Описания скиллов написаны для каталога affpapa.org. Список и описания — [CC0 1.0](LICENSE). Сами скиллы — под лицензиями своих авторов, смотрите исходник.
