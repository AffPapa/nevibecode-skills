# Agent skills for Claude Code, Codex and Cursor, by topic

По-русски: [README.md](README.md)

248 skills in 25 topics from the [NeVibeCode](https://affpapa.org/en/nevibecode) catalog on affpapa.org. Each topic lists the most popular skills that raised no warnings in the automated security check of 2026-11-16. Every entry has an install command, a link to its catalog card and a link to the source.

Method and numbers: [affpapa.org/en/nevibecode/research](https://affpapa.org/en/nevibecode/research).

## Marks

- **installs ✓ 2026-11-16** — the listed command was run in a sandbox on 2026-11-16: the skill installed, SKILL.md is in place and passes the format check. We ran it for the 150 most popular skills in the catalog; 144 worked. 92 skills here carry the mark; the rest were not install-tested.
- **A/B 2026-11-16** — the skill was in the “with skill vs without” test (3 models, 5 topics, blind judges). The number is the mean score difference on a 1–10 scale; the method’s own noise is 0.70, so anything smaller is not a result.
- Security: on 2026-11-16 the catalog check covered 45,138 items and 20,101 executable files and found nothing malicious. It is static analysis and may miss malware written to evade it. Skills with warnings (mostly `curl | sh` installers) are left out.

## What the test showed

On average, a skill in the system prompt gave no measurable gain: −0.20 points against 0.70 noise. Strong models handle these tasks at 7–9 out of 10 without a skill. Narrow skills that encode norms — DB migrations, animation, bug diagnosis — were positive by sign. Of two popular TDD skills, one made answers significantly worse and is left out; the other broke GPT answers and is marked. A skill costs up to 10k tokens per request; answers with it were 15–26% longer.

Limits: whole skill in the system prompt, single turn, 6 answers per skill. Process-style skills are at a disadvantage in this setup.

## Topics

- [Agent setup: memory, context, orchestration](#topic-agent-tooling) — 10
- [Frontend and UI](#topic-frontend) — 10
- [Backend and APIs](#topic-backend) — 10
- [Design](#topic-design) — 10
- [Testing and QA](#topic-testing) — 10
- [Code review and refactoring](#topic-code-review) — 10
- [Security](#topic-security) — 10
- [DevOps and infrastructure](#topic-devops) — 10
- [Cloud: AWS, Azure, GCP](#topic-cloud) — 10
- [Data and databases](#topic-data) — 10
- [AI and ML](#topic-ai-ml) — 10
- [Automation and no-code: n8n, Zapier, Make](#topic-automation) — 10
- [Writing and docs](#topic-docs) — 10
- [Office documents](#topic-office) — 10
- [SEO and GEO](#topic-seo) — 10
- [Marketing and content](#topic-marketing) — 10
- [Browser and scraping](#topic-browser) — 10
- [Mobile](#topic-mobile) — 10
- [Game dev and 3D: Unity, Unreal, Godot, Blender](#topic-gamedev) — 10
- [Science and research](#topic-science) — 10
- [Git and GitHub](#topic-git) — 10
- [Notes, tasks and projects](#topic-productivity) — 10
- [Finance and business](#topic-finance) — 10
- [Programming languages](#topic-languages) — 10
- [Telegram bots](#topic-telegram) — 8

## Installing

Commands target Claude Code (`-a claude-code`) and run from the project folder; Node.js is required. The same CLI installs skills for other agents — see [vercel-labs/skills](https://github.com/vercel-labs/skills). You can also paste the prompt from the [catalog page](https://affpapa.org/en/nevibecode) and let the agent install them.

<a name="topic-agent-tooling"></a>
## Agent setup: memory, context, orchestration

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/agent-tooling](https://affpapa.org/en/nevibecode/topic/agent-tooling)

- **[setup-matt-pocock-skills](https://affpapa.org/en/nevibecode/skills/setup-matt-pocock-skills)** — This skill configures a repository for Matt Pocock's engineering skills by setting its issue tracker, triage labels, and domain docs layout. Run it before using the other skills.
  `npx skills add mattpocock/skills --skill setup-matt-pocock-skills -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/setup-matt-pocock-skills/SKILL.md) · 1,052,851 installs · installs ✓ 2026-11-16
- **[ask-matt](https://affpapa.org/en/nevibecode/skills/ask-matt)** — Routes you to the right Matt Pocock skill or flow for the task at hand. Use it when you need a starting point for a feature, prototype, incoming issue, or hard bug.
  `npx skills add mattpocock/skills --skill ask-matt -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/ask-matt/SKILL.md) · 766,587 installs · installs ✓ 2026-11-16
- **[to-tickets](https://affpapa.org/en/nevibecode/skills/to-tickets)** — Turns a plan, spec, or conversation into small end-to-end tickets with explicit blockers. Use it to agree on the work breakdown before tickets go to a tracker.
  `npx skills add mattpocock/skills --skill to-tickets -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/to-tickets/SKILL.md) · 711,230 installs · installs ✓ 2026-11-16
- **[hyperframes](https://affpapa.org/en/nevibecode/skills/heygen-com-hyperframes)** — Claude Code skill that renders video from HTML by seeking a paused timeline frame by frame.
  `npx skills add heygen-com/hyperframes --skill hyperframes -a claude-code` · [source: heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/blob/95e4e7f880f5005211412e926b307f4a53f47246/skills/hyperframes/SKILL.md) · 1,600,000 installs · installs ✓ 2026-11-16
- **[impeccable](https://affpapa.org/en/nevibecode/skills/impeccable)** — A skill for Claude Code that automates UI auditing, design, and improvement. Use it for redesigns, UI refactoring, or building design systems.
  `npx skills add pbakaus/impeccable --skill impeccable -a claude-code` · [source: pbakaus/impeccable](https://github.com/pbakaus/impeccable/blob/d41d9860b0094dcb68030657da63461212835aaa/cursor-plugin/skills/impeccable/SKILL.md) · 413,300 installs
- **[brainstorming](https://affpapa.org/en/nevibecode/skills/brainstorming)** — The skill runs a design discussion before implementation, clarifies requirements and writes a design doc. Triggered automatically when a request contains ambiguity or implies new functionality.
  `npx skills add obra/superpowers --skill brainstorming -a claude-code` · [source: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/brainstorming/SKILL.md) · 404,045 installs · installs ✓ 2026-11-16
- **[systematic-debugging](https://affpapa.org/en/nevibecode/skills/systematic-debugging)** — A skill for Claude Code and Codex that prevents the agent from proposing fixes before root cause analysis is complete. It activates on any test failure, bug, or unexpected behavior — before the agent reaches for a quick patch.
  `npx skills add obra/superpowers --skill systematic-debugging -a claude-code` · [source: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/systematic-debugging/SKILL.md) · 306,118 installs · installs ✓ 2026-11-16
- **[writing-plans](https://affpapa.org/en/nevibecode/skills/writing-plans)** — Claude Code and Codex skill that writes a detailed implementation plan for multi-step tasks before touching code. Triggered when the agent has a spec or requirements for a feature.
  `npx skills add obra/superpowers --skill writing-plans -a claude-code` · [source: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-plans/SKILL.md) · 282,859 installs · installs ✓ 2026-11-16
- **[mcp-builder](https://affpapa.org/en/nevibecode/skills/mcp-builder)** — Guides the agent through building Model Context Protocol servers in TypeScript or Python. It helps design tool schemas, integrate external APIs, and test transports.
  `npx skills add anthropics/skills --skill mcp-builder -a claude-code` · [source: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/mcp-builder/SKILL.md) · 130,949 installs · installs ✓ 2026-11-16
- **[orca-cli](https://affpapa.org/en/nevibecode/skills/orca-cli)** — This Claude Code skill controls Orca worktrees, terminals, and its built-in browser. The agent can use it to hand work to another agent or inspect a page inside Orca.
  `npx skills add stablyai/orca --skill orca-cli -a claude-code` · [source: stablyai/orca](https://github.com/stablyai/orca/blob/b30d12992e702724fffb426759c907d9b4450586/skills/orca-cli/SKILL.md) · 363,100 installs · installs ✓ 2026-11-16

<a name="topic-frontend"></a>
## Frontend and UI

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/frontend](https://affpapa.org/en/nevibecode/topic/frontend)

- **[design-taste-frontend](https://affpapa.org/en/nevibecode/skills/design-taste-frontend)** — This Claude Code skill sets design rules and checks for websites. It activates for new pages, redesigns, and requests to fix a generic-looking site.
  `npx skills add Leonxlnx/taste-skill --skill design-taste-frontend -a claude-code` · [source: leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/blob/f6b76575f949707b4e3c37cd86cb44b0b98643e8/skills/taste-skill/SKILL.md) · 786,200 installs · A/B 2026-11-16: -0.04 — no effect, ~10k tokens per request
- **[prototype](https://affpapa.org/en/nevibecode/skills/prototype)** — Creates throwaway prototypes for checking state logic or exploring UI before committing the decision to the main codebase.
  `npx skills add mattpocock/skills --skill prototype -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/prototype/SKILL.md) · 986,201 installs · installs ✓ 2026-11-16
- **[webapp-testing](https://affpapa.org/en/nevibecode/skills/webapp-testing)** — This skill tests local web apps with Playwright, helping agents debug UI behavior, capture screenshots, and inspect browser logs.
  `npx skills add anthropics/skills --skill webapp-testing -a claude-code` · [source: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/webapp-testing/SKILL.md) · 186,758 installs · installs ✓ 2026-11-16
- **[ui-ux-pro-max](https://affpapa.org/en/nevibecode/skills/ui-ux-pro-max)** — The ui-ux-pro-max skill for Claude Code and Cursor evaluates interface accessibility, styling, and layouts.
  `npx skills add nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max -a claude-code` · [source: nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/e59ff376a41f7ca47b7541ad5c116495cbade3ee/.claude/skills/ui-ux-pro-max/SKILL.md) · 455,900 installs · installs ✓ 2026-11-16
- **[web-artifacts-builder](https://affpapa.org/en/nevibecode/skills/web-artifacts-builder)** — Skill for Claude Code and Claude.ai builds multi-component HTML artifacts with React, TypeScript, Tailwind CSS and shadcn/ui.
  `npx skills add anthropics/skills --skill web-artifacts-builder -a claude-code` · [source: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/web-artifacts-builder/SKILL.md) · 112,122 installs · installs ✓ 2026-11-16
- **[remotion-to-hyperframes](https://affpapa.org/en/nevibecode/skills/remotion-to-hyperframes)** — Ports video code from Remotion, Motion Canvas, Lottie, or 3D renders into HyperFrames. Runs automated frame-by-frame diffs against the original video file to catch visual drifts.
  `npx skills add heygen-com/hyperframes --skill remotion-to-hyperframes -a claude-code` · [source: heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/blob/95e4e7f880f5005211412e926b307f4a53f47246/skills/remotion-to-hyperframes/SKILL.md) · 627,200 installs · installs ✓ 2026-11-16
- **[shadcn](https://affpapa.org/en/nevibecode/skills/shadcn-ui-shadcn)** — A skill that keeps your agent on the rails with shadcn/ui: adds components, searches registries, fixes markup and builds a design system from your spec.
  `npx skills add shadcn-ui/ui --skill shadcn -a claude-code` · [source: shadcn-ui/ui](https://github.com/shadcn-ui/ui/blob/e62c9435fff729a175f38983dee73b2cb4f6a069/skills/shadcn/SKILL.md) · 150,100 installs · installs ✓ 2026-11-16
- **[vercel-composition-patterns](https://affpapa.org/en/nevibecode/skills/vercel-composition-patterns)** — A rule set that pushes your agent away from boolean props and toward compound components, shared context and state lifted into providers.
  `npx skills add vercel-labs/agent-skills --skill vercel-composition-patterns -a claude-code` · [source: vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/composition-patterns/SKILL.md) · 457,600 installs
- **[emil-design-eng](https://affpapa.org/en/nevibecode/skills/emil-design-eng)** — This skill for Claude Code guides UI component design and review, including interaction details and animation choices. It activates when an agent builds or reviews a component and no narrower skill applies.
  `npx skills add emilkowalski/skills --skill emil-design-eng -a claude-code` · [source: emilkowalski/skills](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills/emil-design-eng/SKILL.md) · 453,900 installs · installs ✓ 2026-11-16 · A/B 2026-11-16: +0.46 — helped with animation and accessibility
- **[review-animations](https://affpapa.org/en/nevibecode/skills/review-animations)** — This Claude Code skill reviews animation and motion code against Emil Kowalski’s design engineering standards. Request an animation review to get a table of findings and suggested changes.
  `npx skills add emilkowalski/skills --skill review-animations -a claude-code` · [source: emilkowalski/skills](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills/review-animations/SKILL.md) · 313,500 installs · installs ✓ 2026-11-16

<a name="topic-backend"></a>
## Backend and APIs

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/backend](https://affpapa.org/en/nevibecode/topic/backend)

- **[lark-im](https://affpapa.org/en/nevibecode/skills/lark-im)** — This skill lets an agent work with Lark IM messages, chats, files, and interactive cards. Use it when coding tasks need access to team conversations.
  `npx skills add larksuite/cli --skill lark-im -a claude-code` · [source: larksuite/cli](https://github.com/larksuite/cli/blob/3d82c85419ad7560ad017db7a3972a596b5fbeb1/skills/lark-im/SKILL.md) · 490,400 installs · installs ✓ 2026-11-16
- **[api-and-interface-design](https://affpapa.org/en/nevibecode/skills/api-and-interface-design)** — Guides API and module-boundary design with explicit contracts, validation, and consistent errors. Use it for REST, GraphQL, or public interfaces.
  `npx skills add addyosmani/agent-skills --skill api-and-interface-design -a claude-code` · [source: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/api-and-interface-design/SKILL.md) · 77,000 installs
- **[observability-and-instrumentation](https://affpapa.org/en/nevibecode/skills/observability-and-instrumentation)** — Skill for Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI and OpenCode that teaches the AI to write instrumentation: structured logging, metrics, traces, and correlation IDs.
  `npx skills add addyosmani/agent-skills --skill observability-and-instrumentation -a claude-code` · [source: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/observability-and-instrumentation/SKILL.md) · 68,100 installs
- **[gws-gmail-watch](https://affpapa.org/en/nevibecode/skills/gws-gmail-watch)** — Watches Gmail for new emails and streams events as NDJSON. Use it when an agent needs incoming mail as a live input.
  `npx skills add googleworkspace/cli --skill gws-gmail-watch -a claude-code` · [source: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-gmail-watch/SKILL.md) · 38,600 installs
- **[api-security-testing](https://affpapa.org/en/nevibecode/skills/usestrix-api-security-testing)** — This skill guides Strix through REST, GraphQL, or gRPC API security tests, then provides a request to reproduce each finding.
  `npx skills add usestrix/strix --skill api-security-testing -a claude-code` · [source: usestrix/strix](https://github.com/usestrix/strix/blob/fc44d80b3e8f85d91be7a6ba66db85fa84d3840b/skills/api-security-testing/SKILL.md) · 17,500 installs
- **[mcporter](https://affpapa.org/en/nevibecode/skills/mcporter)** — This skill lets an agent list, configure, authenticate, inspect, and call MCP servers over HTTP or stdio. Use it when MCP tools need direct CLI access.
  `npx skills add openclaw/openclaw --skill mcporter -a claude-code` · [source: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/mcporter/SKILL.md) · 6,300 installs
- **[goplaces](https://affpapa.org/en/nevibecode/skills/goplaces)** — This skill runs goplaces to search Google Places, look up place details, and fetch reviews. Use it when an agent needs information about a place or area.
  `npx skills add openclaw/openclaw --skill goplaces -a claude-code` · [source: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/goplaces/SKILL.md) · 5,400 installs
- **[xurl](https://affpapa.org/en/nevibecode/skills/xurl)** — Skill for the xurl CLI tool. It lets your coding agent publish posts, inspect feeds, upload media files, and send raw X API requests directly from chat.
  `npx skills add openclaw/openclaw --skill xurl -a claude-code` · [source: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/xurl/SKILL.md) · 4,900 installs
- **[wrangler](https://affpapa.org/en/nevibecode/skills/cloudflare-wrangler)** — Runs and troubleshoots Wrangler CLI commands for Cloudflare Workers projects that use wrangler configuration files.
  `npx skills add cloudflare/skills --skill wrangler -a claude-code` · [source: cloudflare/skills](https://github.com/cloudflare/skills/blob/cbf893b954222276bf1af57e5f23379231e0efb9/skills/wrangler/SKILL.md) · 149,600 installs
- **[backend-patterns](https://affpapa.org/en/nevibecode/skills/backend-patterns)** — A skill with backend patterns for Node.js, Express and Next.js API routes: layering, caching, transactions, error handling.
  `npx skills add affaan-m/ECC --skill backend-patterns -a claude-code` · [source: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/backend-patterns/SKILL.md) · 7,700 installs

<a name="topic-design"></a>
## Design

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/design](https://affpapa.org/en/nevibecode/topic/design)

- **[frontend-design](https://affpapa.org/en/nevibecode/skills/frontend-design)** — This skill guides intentional visual design for new interfaces and redesigns. Use it when a generic generated UI is not enough.
  `npx skills add anthropics/skills --skill frontend-design -a claude-code` · [source: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/frontend-design/SKILL.md) · 1,025,790 installs · installs ✓ 2026-11-16 · A/B 2026-11-16: +0.08 — within noise
- **[codebase-design](https://affpapa.org/en/nevibecode/skills/codebase-design)** — This skill helps design modules with small interfaces and hidden complexity. Use it when refactoring code, choosing a seam, or making tests easier to write.
  `npx skills add mattpocock/skills --skill codebase-design -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/codebase-design/SKILL.md) · 850,344 installs · installs ✓ 2026-11-16
- **[hyperframes-cli](https://affpapa.org/en/nevibecode/skills/heygen-com-hyperframes-cli)** — This Claude Code skill controls HyperFrames projects through the CLI, from project setup to timeline edits. It runs checks, previews and video renders.
  `npx skills add heygen-com/hyperframes --skill hyperframes-cli -a claude-code` · [source: heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/blob/95e4e7f880f5005211412e926b307f4a53f47246/skills/hyperframes-cli/SKILL.md) · 1,600,000 installs · installs ✓ 2026-11-16
- **[hyperframes-registry](https://affpapa.org/en/nevibecode/skills/heygen-com-hyperframes-registry)** — Search and add editable HyperFrames blocks for transitions, titles, captions, charts, maps, and 3D scenes. The skill starts with catalog search before you build an effect by hand.
  `npx skills add heygen-com/hyperframes --skill hyperframes-registry -a claude-code` · [source: heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/blob/95e4e7f880f5005211412e926b307f4a53f47246/skills/hyperframes-registry/SKILL.md) · 1,300,000 installs · installs ✓ 2026-11-16
- **[canvas-design](https://affpapa.org/en/nevibecode/skills/canvas-design)** — A skill for Claude Code and Claude.ai that produces static visual art as .png or .pdf files. It kicks in when you ask for a poster, a graphic piece, or a design that has no existing layout.
  `npx skills add anthropics/skills --skill canvas-design -a claude-code` · [source: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/canvas-design/SKILL.md) · 121,543 installs · installs ✓ 2026-11-16
- **[brand-guidelines](https://affpapa.org/en/nevibecode/skills/brand-guidelines)** — Applies Anthropic's official brand colors and fonts to documents, slides and other artifacts. Useful whenever something needs to match the company look.
  `npx skills add anthropics/skills --skill brand-guidelines -a claude-code` · [source: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/brand-guidelines/SKILL.md) · 109,043 installs · installs ✓ 2026-11-16
- **[hallmark](https://affpapa.org/en/nevibecode/skills/hallmark)** — A design skill for AI coding that keeps generated UIs from looking generated. Useful when you ask an agent to build a new page or site.
  `npx skills add Nutlope/hallmark --skill hallmark -a claude-code` · [source: nutlope/hallmark](https://github.com/Nutlope/hallmark/blob/04977e15f3dfd6ee4b74c887dac3eb52665d6c92/skills/hallmark/SKILL.md) · 109,000 installs · installs ✓ 2026-11-16
- **[apple-design](https://affpapa.org/en/nevibecode/skills/apple-design)** — Translates Apple's fluid interface principles from WWDC talks into web code with Pointer Events and spring physics. Essential for gesture-driven sheets, drags, and sliders.
  `npx skills add emilkowalski/skills --skill apple-design -a claude-code` · [source: emilkowalski/skills](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills/apple-design/SKILL.md) · 305,400 installs · installs ✓ 2026-11-16
- **[design](https://affpapa.org/en/nevibecode/skills/design)** — This Claude Code skill handles brand identity, interface styling, logos, banners, presentations, and social graphics. Ask for a design system, corporate identity mockups, or assets for a social platform.
  `npx skills add nextlevelbuilder/ui-ux-pro-max-skill --skill design -a claude-code` · [source: nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/e59ff376a41f7ca47b7541ad5c116495cbade3ee/cli/assets/skills/design/SKILL.md) · 52,700 installs
- **[brand](https://affpapa.org/en/nevibecode/skills/brand)** — Keeps brand voice, visual rules and design tokens in one markdown file, then feeds them to your agent's prompts and to your CSS variables.
  `npx skills add nextlevelbuilder/ui-ux-pro-max-skill --skill brand -a claude-code` · [source: nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/e59ff376a41f7ca47b7541ad5c116495cbade3ee/cli/assets/skills/brand/SKILL.md) · 51,100 installs

<a name="topic-testing"></a>
## Testing and QA

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/testing](https://affpapa.org/en/nevibecode/topic/testing)

- **[tdd](https://affpapa.org/en/nevibecode/skills/tdd)** — Guides the red-green TDD loop: ensures tests are written first, keep them at public interfaces, and avoid coupling to implementation details.
  `npx skills add mattpocock/skills --skill tdd -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/tdd/SKILL.md) · 1,141,062 installs · installs ✓ 2026-11-16 · A/B 2026-11-16: -1.33 — broke GPT answers
- **[diagnosing-bugs](https://affpapa.org/en/nevibecode/skills/diagnosing-bugs)** — This skill guides agents through reproducing hard bugs and performance regressions with a focused feedback loop. Use it when code fails, behaves incorrectly, or runs slowly.
  `npx skills add mattpocock/skills --skill diagnosing-bugs -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/diagnosing-bugs/SKILL.md) · 834,802 installs · installs ✓ 2026-11-16 · A/B 2026-11-16: +0.31 — helped Claude
- **[implement](https://affpapa.org/en/nevibecode/skills/implement)** — Implements work from a specification or tickets, following a test-driven flow and ending with review and a commit. Use it when a coding task needs a defined delivery routine.
  `npx skills add mattpocock/skills --skill implement -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/implement/SKILL.md) · 774,700 installs · installs ✓ 2026-11-16
- **[verification-before-completion](https://affpapa.org/en/nevibecode/skills/verification-before-completion)** — This skill blocks completion claims until the agent runs a fresh check and reads the result. Use it before commits or PRs when an agent report is not enough.
  `npx skills add obra/superpowers --skill verification-before-completion -a claude-code` · [source: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/verification-before-completion/SKILL.md) · 251,313 installs · installs ✓ 2026-11-16
- **[executing-plans](https://affpapa.org/en/nevibecode/skills/executing-plans)** — Runs an implementation plan in the current session instead of assigning each task to a subagent. Use it for inline work with TDD, a decision ledger, and a final branch review.
  `npx skills add obra/superpowers --skill executing-plans -a claude-code` · [source: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/executing-plans/SKILL.md) · 242,988 installs · installs ✓ 2026-11-16
- **[dispatching-parallel-agents](https://affpapa.org/en/nevibecode/skills/dispatching-parallel-agents)** — Dispatches independent tasks to separate subagents so they can investigate them in parallel. Use it for unrelated test failures and separate broken subsystems.
  `npx skills add obra/superpowers --skill dispatching-parallel-agents -a claude-code` · [source: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/dispatching-parallel-agents/SKILL.md) · 218,235 installs · installs ✓ 2026-11-16
- **[google-agents-cli-eval](https://affpapa.org/en/nevibecode/skills/google-agents-cli-eval)** — Runs agent evaluation pipelines, grades responses with LLM judges, and tracks metric failures. Activates during dataset authoring and benchmark runs in agents-cli.
  `npx skills add google/agents-cli --skill google-agents-cli-eval -a claude-code` · [source: google/agents-cli](https://github.com/google/agents-cli/blob/6eedbdc2f44c388cbfc5f305eb83b9924cfefebb/skills/google-agents-cli-eval/SKILL.md) · 574,900 installs · installs ✓ 2026-11-16
- **[verify-and-stop](https://affpapa.org/en/nevibecode/skills/verify-and-stop)** — Proves existing work meets acceptance criteria without expanding scope. Useful for validation tasks and last-mile checks.
  `npx skills add JuliusBrussee/caveman --skill verify-and-stop -a claude-code` · [source: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/9b243662ff98d392bc0a95b865a554583d71be75/skills/verify-and-stop/SKILL.md) · 126,300 installs · installs ✓ 2026-11-16
- **[surgical-patch](https://affpapa.org/en/nevibecode/skills/surgical-patch)** — The skill constrains AI coding agents to the narrowest layer responsible for a bug. It prevents unwanted refactoring and demands focused regression checks.
  `npx skills add JuliusBrussee/caveman --skill surgical-patch -a claude-code` · [source: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/9b243662ff98d392bc0a95b865a554583d71be75/skills/surgical-patch/SKILL.md) · 126,100 installs · installs ✓ 2026-11-16
- **[debugging-and-error-recovery](https://affpapa.org/en/nevibecode/skills/debugging-and-error-recovery)** — This Claude Code skill traces failures to their root cause and checks the fix. It activates for failing tests, broken builds, unexpected errors, or behavior that no longer matches expectations.
  `npx skills add addyosmani/agent-skills --skill debugging-and-error-recovery -a claude-code` · [source: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/debugging-and-error-recovery/SKILL.md) · 76,900 installs

<a name="topic-code-review"></a>
## Code review and refactoring

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/code-review](https://affpapa.org/en/nevibecode/topic/code-review)

- **[improve-codebase-architecture](https://affpapa.org/en/nevibecode/skills/improve-codebase-architecture)** — This skill scans a codebase for architectural friction, then builds a visual HTML report with refactoring candidates. Use it before a deeper architecture review.
  `npx skills add mattpocock/skills --skill improve-codebase-architecture -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/improve-codebase-architecture/SKILL.md) · 1,163,035 installs · installs ✓ 2026-11-16
- **[code-review](https://affpapa.org/en/nevibecode/skills/code-review)** — Evaluates code diffs along two parallel tracks: project standards and issue specifications. Uses isolated sub-agents to keep findings clean.
  `npx skills add mattpocock/skills --skill code-review -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/code-review/SKILL.md) · 789,521 installs · installs ✓ 2026-11-16 · A/B 2026-11-16: -0.29 — no effect
- **[requesting-code-review](https://affpapa.org/en/nevibecode/skills/requesting-code-review)** — Sends completed work to a reviewer subagent after a task, major feature, or before merging to main. It keeps the review focused on the change and its requirements.
  `npx skills add obra/superpowers --skill requesting-code-review -a claude-code` · [source: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/requesting-code-review/SKILL.md) · 262,135 installs · installs ✓ 2026-11-16
- **[receiving-code-review](https://affpapa.org/en/nevibecode/skills/receiving-code-review)** — Reviews code review feedback before changes: it clarifies unclear points, checks the repository, and supports reasoned pushback. Use it before acting on review comments.
  `npx skills add obra/superpowers --skill receiving-code-review -a claude-code` · [source: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/receiving-code-review/SKILL.md) · 221,216 installs · installs ✓ 2026-11-16
- **[retro](https://affpapa.org/en/nevibecode/skills/retro)** — Reviews a coding session and suggests changes to the agent environment for later runs. Use it after mistakes, slow repository navigation, or costly tool calls.
  `npx skills add mattpocock/skills --skill retro -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/retro/SKILL.md) · 276,027 installs · installs ✓ 2026-11-16
- **[caveman-review](https://affpapa.org/en/nevibecode/skills/caveman-review)** — Turns code review comments into one line per finding: location, problem, fix. Useful when a diff or PR needs a fast pass without the filler.
  `npx skills add JuliusBrussee/caveman --skill caveman-review -a claude-code` · [source: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/9b243662ff98d392bc0a95b865a554583d71be75/skills/caveman-review/SKILL.md) · 434,700 installs · installs ✓ 2026-11-16 · A/B 2026-11-16: -0.21 — compression drops details
- **[ponytail](https://affpapa.org/en/nevibecode/skills/ponytail)** — ponytail puts an agent into a senior-dev mode focused on the smallest complete change. Use it when you want clear replies and less code added to a project.
  `npx skills add DietrichGebert/ponytail --skill ponytail -a claude-code` · [source: dietrichgebert/ponytail](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail/SKILL.md) · 132,500 installs · installs ✓ 2026-11-16
- **[ponytail-review](https://affpapa.org/en/nevibecode/skills/ponytail-review)** — ponytail-review reviews a change beyond the diff, checking connected code, bugs, risks, load, tests, speed, and unnecessary code. Use it for PRs and commits.
  `npx skills add DietrichGebert/ponytail --skill ponytail-review -a claude-code` · [source: dietrichgebert/ponytail](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail-review/SKILL.md) · 72,100 installs · installs ✓ 2026-11-16
- **[ponytail-audit](https://affpapa.org/en/nevibecode/skills/ponytail-audit)** — It audits a repository and ranks bugs, risks, and redundant code in a one-shot report. Use it when you need a review without code changes.
  `npx skills add DietrichGebert/ponytail --skill ponytail-audit -a claude-code` · [source: dietrichgebert/ponytail](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail-audit/SKILL.md) · 59,700 installs · installs ✓ 2026-11-16
- **[caveman-explore](https://affpapa.org/en/nevibecode/skills/caveman-explore)** — A read-only skill locates relevant files and line ranges in a repository. Use it for cold-start orientation or broad searches.
  `npx skills add JuliusBrussee/caveman --skill caveman-explore -a claude-code` · [source: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/9b243662ff98d392bc0a95b865a554583d71be75/skills/caveman-explore/SKILL.md) · 129,100 installs · installs ✓ 2026-11-16

<a name="topic-security"></a>
## Security

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/security](https://affpapa.org/en/nevibecode/topic/security)

- **[security-audit](https://affpapa.org/en/nevibecode/skills/cloudflare-security-audit)** — Reviews codebases and APIs for vulnerabilities using safe sandboxing. Fits pre-release security reviews, pen-test triage, and architecture checks.
  `npx skills add cloudflare/security-audit-skill --skill security-audit -a claude-code` · [source: cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/SKILL.md) · 111,000 installs · installs ✓ 2026-11-16
- **[security-and-hardening](https://affpapa.org/en/nevibecode/skills/security-and-hardening)** — This skill checks code that handles untrusted input, authentication, sessions, and external services. It also covers dependency audits and privacy-related data risks.
  `npx skills add addyosmani/agent-skills --skill security-and-hardening -a claude-code` · [source: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/security-and-hardening/SKILL.md) · 86,400 installs · installs ✓ 2026-11-16
- **[fix-security-vulnerabilities-with-strix](https://affpapa.org/en/nevibecode/skills/fix-security-vulnerabilities-with-strix)** — This skill triages validated Strix findings, fixes their root causes, and runs Strix again to verify the result. Use it after a CLI or cloud scan.
  `npx skills add usestrix/strix --skill fix-security-vulnerabilities-with-strix -a claude-code` · [source: usestrix/strix](https://github.com/usestrix/strix/blob/fc44d80b3e8f85d91be7a6ba66db85fa84d3840b/skills/fix-security-vulnerabilities-with-strix/SKILL.md) · 20,300 installs
- **[web-app-penetration-testing](https://affpapa.org/en/nevibecode/skills/web-app-penetration-testing)** — Runs a black-box web app pentest through Strix and validates findings with working PoCs. Use it for staging sites, live URLs, or local development servers.
  `npx skills add usestrix/strix --skill web-app-penetration-testing -a claude-code` · [source: usestrix/strix](https://github.com/usestrix/strix/blob/fc44d80b3e8f85d91be7a6ba66db85fa84d3840b/skills/web-app-penetration-testing/SKILL.md) · 17,600 installs
- **[owasp-top-10-testing](https://affpapa.org/en/nevibecode/skills/owasp-top-10-testing)** — Runs Strix AI agents to execute exploits across OWASP Top 10:2025 categories. Useful for verifying attack paths with concrete proofs-of-concept before audits.
  `npx skills add usestrix/strix --skill owasp-top-10-testing -a claude-code` · [source: usestrix/strix](https://github.com/usestrix/strix/blob/fc44d80b3e8f85d91be7a6ba66db85fa84d3840b/skills/owasp-top-10-testing/SKILL.md) · 17,500 installs
- **[persona-it-admin](https://affpapa.org/en/nevibecode/skills/persona-it-admin)** — A persona skill for IT admins: watches for suspicious logins, sets Drive sharing policies, and works through requests with gws.
  `npx skills add googleworkspace/cli --skill persona-it-admin -a claude-code` · [source: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/persona-it-admin/SKILL.md) · 31,000 installs
- **[gws-modelarmor](https://affpapa.org/en/nevibecode/skills/gws-modelarmor)** — Filters user prompts and model responses for safety using Google Model Armor templates. Useful for automated content sanitization via the gws CLI.
  `npx skills add googleworkspace/cli --skill gws-modelarmor -a claude-code` · [source: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-modelarmor/SKILL.md) · 30,900 installs
- **[gws-modelarmor-create-template](https://affpapa.org/en/nevibecode/skills/gws-modelarmor-create-template)** — Creates Google Model Armor templates in GCP to filter user-generated content. Useful when configuring jailbreak defenses via the gws CLI.
  `npx skills add googleworkspace/cli --skill gws-modelarmor-create-template -a claude-code` · [source: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-modelarmor-create-template/SKILL.md) · 30,800 installs
- **[1password](https://affpapa.org/en/nevibecode/skills/1password)** — Configures 1Password CLI, handles authentication modes, and safely injects secrets into commands without leaking credentials into chat.
  `npx skills add openclaw/openclaw --skill 1password -a claude-code` · [source: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/1password/SKILL.md) · 6,400 installs
- **[security-best-practices](https://affpapa.org/en/nevibecode/skills/githubcomopenaiskills-security-best-practices)** — A skill that reviews code against security best practices for Python, JavaScript/TypeScript and Go, then suggests fixes.
  `npx skills add tech-leads-club/agent-skills --skill security-best-practices -a claude-code` · [source: tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills/blob/e74dc8a7e8d59bb36f267afd089580e0858e224a/packages/skills-catalog/skills/(security)/security-best-practices/SKILL.md) · 390 installs

<a name="topic-devops"></a>
## DevOps and infrastructure

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/devops](https://affpapa.org/en/nevibecode/topic/devops)

- **[wizard](https://affpapa.org/en/nevibecode/skills/wizard)** — This skill creates an interactive bash wizard for manual setup steps, CI secrets, third-party dashboards, and one-off migrations.
  `npx skills add mattpocock/skills --skill wizard -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/wizard/SKILL.md) · 553,369 installs · installs ✓ 2026-11-16
- **[setup-pre-commit](https://affpapa.org/en/nevibecode/skills/setup-pre-commit)** — This skill configures pre-commit checks for a JavaScript repository, running Prettier, type checking, and tests before each commit.
  `npx skills add mattpocock/skills --skill setup-pre-commit -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/setup-pre-commit/SKILL.md) · 489,289 installs · installs ✓ 2026-11-16
- **[google-agents-cli-observability](https://affpapa.org/en/nevibecode/skills/google-agents-cli-observability)** — This skill guides you through tracing and monitoring agents, including ADK projects. Use it to investigate errors or track an agent after deployment.
  `npx skills add google/agents-cli --skill google-agents-cli-observability -a claude-code` · [source: google/agents-cli](https://github.com/google/agents-cli/blob/6eedbdc2f44c388cbfc5f305eb83b9924cfefebb/skills/google-agents-cli-observability/SKILL.md) · 574,700 installs · installs ✓ 2026-11-16
- **[herdr](https://affpapa.org/en/nevibecode/skills/herdr)** — A skill that lets your agent drive Herdr, the terminal multiplexer for coding agents: panes, tabs, workspaces and command runs.
  `npx skills add herdrdev/herdr --skill herdr -a claude-code` · [source: herdrdev/herdr](https://github.com/herdrdev/herdr/blob/ee5bfb5041bb3e4a49d591c72308aae3c81ecdde/skills/herdr/SKILL.md) · 84,800 installs · installs ✓ 2026-11-16
- **[vercel-cli-with-tokens](https://affpapa.org/en/nevibecode/skills/vercel-cli-with-tokens)** — Lets your agent drive the Vercel CLI with an access token instead of an interactive login: find the token, link the project, ship a preview, edit env vars.
  `npx skills add vercel-labs/agent-skills --skill vercel-cli-with-tokens -a claude-code` · [source: vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/vercel-cli-with-tokens/SKILL.md) · 156,700 installs
- **[turborepo](https://affpapa.org/en/nevibecode/skills/vercel-turborepo)** — Configures Turborepo monorepos and troubleshoots task pipelines. Useful when editing turbo.json, setting up caching, or fixing CI builds.
  `npx skills add vercel/turborepo --skill turborepo -a claude-code` · [source: vercel/turborepo](https://github.com/vercel/turborepo/blob/67484391f9090c51a888221998b042a31a93e49d/skills/turborepo/SKILL.md) · 90,700 installs · installs ✓ 2026-11-16
- **[vercel-optimize](https://affpapa.org/en/nevibecode/skills/vercel-optimize)** — A skill for Claude Code, Codex, Cursor, GitHub Copilot, and Gemini CLI that audits cost and performance on deployed Vercel projects. It collects platform signals first, then produces ranked recommendations tied to specific routes.
  `npx skills add vercel-labs/agent-skills --skill vercel-optimize -a claude-code` · [source: vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/vercel-optimize/SKILL.md) · 132,700 installs
- **[shipping-and-launch](https://affpapa.org/en/nevibecode/skills/shipping-and-launch)** — Walks your agent through a production launch: pre-launch checklist, monitoring, staged rollout and a rollback plan. Useful when a feature reaches real users.
  `npx skills add addyosmani/agent-skills --skill shipping-and-launch -a claude-code` · [source: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/shipping-and-launch/SKILL.md) · 71,600 installs
- **[ci-cd-and-automation](https://affpapa.org/en/nevibecode/skills/ci-cd-and-automation)** — Builds a GitHub Actions CI/CD pipeline for a repo: lint, type check, tests, build and dependency audit chained as gates on every pull request.
  `npx skills add addyosmani/agent-skills --skill ci-cd-and-automation -a claude-code` · [source: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/ci-cd-and-automation/SKILL.md) · 71,500 installs
- **[orca-per-workspace-env](https://affpapa.org/en/nevibecode/skills/orca-per-workspace-env)** — This Claude Code skill sets up and checks Orca environment recipes for individual workspaces. It applies to environmentRecipes in orca.yaml, provider scripts, and orca vm recipe doctor failures.
  `npx skills add stablyai/orca --skill orca-per-workspace-env -a claude-code` · [source: stablyai/orca](https://github.com/stablyai/orca/blob/b30d12992e702724fffb426759c907d9b4450586/skills/orca-per-workspace-env/SKILL.md) · 12,600 installs

<a name="topic-cloud"></a>
## Cloud: AWS, Azure, GCP

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/cloud](https://affpapa.org/en/nevibecode/topic/cloud)

- **[google-agents-cli-deploy](https://affpapa.org/en/nevibecode/skills/google-agents-cli-deploy)** — Guides coding agents through deploying AI agents to Google Cloud targets via agents-cli. Configures pipelines, secrets, and environments across Agent Runtime, Cloud Run, or GKE.
  `npx skills add google/agents-cli --skill google-agents-cli-deploy -a claude-code` · [source: google/agents-cli](https://github.com/google/agents-cli/blob/6eedbdc2f44c388cbfc5f305eb83b9924cfefebb/skills/google-agents-cli-deploy/SKILL.md) · 576,100 installs · installs ✓ 2026-11-16
- **[gws-drive-upload](https://affpapa.org/en/nevibecode/skills/gws-drive-upload)** — A skill for Claude Code, Codex, Cursor and other IDEs that uploads files to Google Drive directly from the editor with automatic type detection. Run via gws drive +upload with a file path.
  `npx skills add googleworkspace/cli --skill gws-drive-upload -a claude-code` · [source: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-drive-upload/SKILL.md) · 51,200 installs
- **[gws-events-subscribe](https://affpapa.org/en/nevibecode/skills/gws-events-subscribe)** — A skill for Claude Code, Cursor, and other IDEs that lets you subscribe to Google Workspace events (Chat messages, document changes) and stream them as NDJSON. Use the gws events +subscribe command to pick event types and target resources.
  `npx skills add googleworkspace/cli --skill gws-events-subscribe -a claude-code` · [source: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-events-subscribe/SKILL.md) · 31,700 installs
- **[cloudflare](https://affpapa.org/en/nevibecode/skills/cloudflare-cloudflare)** — Skill for Claude Code and Codex helps choose Cloudflare products for applications, storage, and APIs. Diagnoses 52x status codes and Cloudflare 403 errors across origin servers.
  `npx skills add cloudflare/skills --skill cloudflare -a claude-code` · [source: cloudflare/skills](https://github.com/cloudflare/skills/blob/cbf893b954222276bf1af57e5f23379231e0efb9/skills/cloudflare/SKILL.md) · 159,200 installs
- **[google-cloud-waf-cost-optimization](https://affpapa.org/en/nevibecode/skills/google-cloud-waf-cost-optimization)** — A skill for Claude Code, Gemini CLI, and Codex that audits Google Cloud workloads against the Well-Architected Framework Cost Optimization pillar.
  `npx skills add google/skills --skill google-cloud-waf-cost-optimization -a claude-code` · [source: google/skills](https://github.com/google/skills/blob/e5250c8a02c28097b11a0c22d77143f4a0e5a408/skills/cloud/google-cloud-waf-cost-optimization/SKILL.md) · 14,266 installs
- **[firebase-basics](https://affpapa.org/en/nevibecode/skills/firebase-basics)** — This skill sets up the Firebase CLI, handles sign-in, creates or switches projects, and downloads Android or iOS app configuration files.
  `npx skills add google/skills --skill firebase-basics -a claude-code` · [source: google/skills](https://github.com/google/skills/blob/e5250c8a02c28097b11a0c22d77143f4a0e5a408/skills/cloud/firebase-basics/SKILL.md) · 14,100 installs
- **[google-cloud-networking-observability](https://affpapa.org/en/nevibecode/skills/google-cloud-networking-observability)** — Investigate Google Cloud network logs, metrics, and connectivity paths. Use it to trace packet drops, firewall blocks, or routing problems.
  `npx skills add google/skills --skill google-cloud-networking-observability -a claude-code` · [source: google/skills](https://github.com/google/skills/blob/e5250c8a02c28097b11a0c22d77143f4a0e5a408/skills/cloud/google-cloud-networking-observability/SKILL.md) · 11,856 installs
- **[firebase-app-hosting-basics](https://affpapa.org/en/nevibecode/skills/firebase-app-hosting-basics)** — Deploys Next.js and Angular applications with SSR through Firebase App Hosting. Use it to configure backends, secrets, GitHub rollouts, and local emulation.
  `npx skills add firebase/agent-skills --skill firebase-app-hosting-basics -a claude-code` · [source: firebase/agent-skills](https://github.com/firebase/agent-skills/blob/99954a30898bb5ddc8152ee10e124dc3b4106bf7/skills/firebase-app-hosting-basics/SKILL.md) · 180,100 installs
- **[firebase-crashlytics](https://affpapa.org/en/nevibecode/skills/firebase-crashlytics)** — Skill for Claude Code that guides Firebase Crashlytics provisioning and SDK setup. It covers crash reporting for Android, iOS, and Web apps.
  `npx skills add firebase/agent-skills --skill firebase-crashlytics -a claude-code` · [source: firebase/agent-skills](https://github.com/firebase/agent-skills/blob/99954a30898bb5ddc8152ee10e124dc3b4106bf7/skills/firebase-crashlytics/SKILL.md) · 142,100 installs
- **[prisma-compute](https://affpapa.org/en/nevibecode/skills/prisma-compute)** — Skill for Claude Code that guides deploying and running apps on Prisma Compute via Prisma 8 CLI. Covers Prisma Composer setups, rolling back versions, and reading service logs.
  `npx skills add prisma/skills --skill prisma-compute -a claude-code` · [source: prisma/skills](https://github.com/prisma/skills/blob/a6f192959cf43b08aa330fe1ffca090267215812/prisma-compute/SKILL.md) · 410,600 installs

<a name="topic-data"></a>
## Data and databases

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/data](https://affpapa.org/en/nevibecode/topic/data)

- **[migration](https://affpapa.org/en/nevibecode/skills/migration)** — Enforces reversible, compatibility-safe transitions for schema, data, and API updates. Useful whenever data loss or rollout downtime is unacceptable.
  `npx skills add JuliusBrussee/caveman --skill migration -a claude-code` · [source: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/9b243662ff98d392bc0a95b865a554583d71be75/skills/migration/SKILL.md) · 125,000 installs · installs ✓ 2026-11-16 · A/B 2026-11-16: +0.43 — best by sign, 5 of 6 scores positive
- **[notion](https://affpapa.org/en/nevibecode/skills/notion)** — This skill connects an agent to Notion through the ntn CLI and API, for reading and editing pages, querying data sources, and uploading files.
  `npx skills add openclaw/openclaw --skill notion -a claude-code` · [source: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/notion/SKILL.md) · 5,700 installs
- **[data-visualization](https://affpapa.org/en/nevibecode/skills/anthropics-data-visualization)** — Selects chart types based on data structure and produces Python visualization code in matplotlib, seaborn, and plotly. Useful for reports and research figures.
  `npx skills add anthropics/knowledge-work-plugins --skill data-visualization -a claude-code` · [source: anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/data/skills/data-visualization/SKILL.md) · 14,800 installs
- **[database-migrations](https://affpapa.org/en/nevibecode/skills/database-migrations)** — A skill that spells out safe, reversible schema changes: expand-contract renames, concurrent indexes, batched backfills, plus workflows for PostgreSQL, Prisma, Drizzle, Kysely, Django and golang-migrate.
  `npx skills add affaan-m/ECC --skill database-migrations -a claude-code` · [source: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/database-migrations/SKILL.md) · 6,900 installs
- **[postgres-patterns](https://affpapa.org/en/nevibecode/skills/postgres-patterns)** — PostgreSQL best practice reference based on Supabase guidelines. Covers indexing patterns, data type choices, RLS policies, and slow query diagnosis.
  `npx skills add affaan-m/ECC --skill postgres-patterns -a claude-code` · [source: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/postgres-patterns/SKILL.md) · 6,800 installs
- **[bigquery-basics](https://affpapa.org/en/nevibecode/skills/bigquery-basics)** — Manages BigQuery resources and runs SQL queries. Use it to create datasets, tables and views, or handle basic data ingestion and analysis.
  `npx skills add google/skills --skill bigquery-basics -a claude-code` · [source: google/skills](https://github.com/google/skills/blob/e5250c8a02c28097b11a0c22d77143f4a0e5a408/skills/cloud/bigquery-basics/SKILL.md) · 17,678 installs
- **[mysql-patterns](https://affpapa.org/en/nevibecode/skills/mysql-patterns)** — Production patterns for MySQL and MariaDB schema design, indexing, transactions, and slow query diagnostics in AI coding agents.
  `npx skills add affaan-m/ECC --skill mysql-patterns -a claude-code` · [source: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/mysql-patterns/SKILL.md) · 6,100 installs
- **[alloydb-basics](https://affpapa.org/en/nevibecode/skills/alloydb-basics)** — Use this skill to create and configure AlloyDB for PostgreSQL clusters and instances, manage backups, and work with AlloyDB MCP tools. It is for AlloyDB administration.
  `npx skills add google/skills --skill alloydb-basics -a claude-code` · [source: google/skills](https://github.com/google/skills/blob/e5250c8a02c28097b11a0c22d77143f4a0e5a408/skills/cloud/alloydb-basics/SKILL.md) · 12,991 installs
- **[postgresql-table-design](https://affpapa.org/en/nevibecode/skills/postgresql-table-design)** — Helps design and review PostgreSQL schemas with guidance on data types, keys, constraints, indexes, and table partitioning.
  `npx skills add wshobson/agents --skill postgresql-table-design -a claude-code` · [source: wshobson/agents](https://github.com/wshobson/agents/blob/4bde3168b43c0655c4d00ea2726e631719908a6d/plugins/database-design/skills/postgresql-table-design/SKILL.md) · 27,780 installs
- **[data-analysis](https://affpapa.org/en/nevibecode/skills/bytedance-data-analysis)** — A skill for Claude Code, Codex, Cursor and other environments to inspect structured data. Runs DuckDB SQL queries and statistical calculations on Excel and CSV files.
  `npx skills add bytedance/deer-flow --skill data-analysis -a claude-code` · [source: bytedance/deer-flow](https://github.com/bytedance/deer-flow/blob/4a27b133f81dfa621bf17635f2659bef2eebb7fd/skills/public/data-analysis/SKILL.md) · 3,700 installs

<a name="topic-ai-ml"></a>
## AI and ML

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/ai-ml](https://affpapa.org/en/nevibecode/topic/ai-ml)

- **[skill-creator](https://affpapa.org/en/nevibecode/skills/skill-creator)** — Creates and refines skills, then tests them with prompts, evaluations, and performance checks.
  `npx skills add anthropics/skills --skill skill-creator -a claude-code` · [source: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/skill-creator/SKILL.md) · 414,180 installs · installs ✓ 2026-11-16
- **[media-use](https://affpapa.org/en/nevibecode/skills/media-use)** — Finds and generates media assets for HyperFrames video projects and saves them directly to assets. Handles HeyGen catalog search, voice generation, background audio, and footage grading.
  `npx skills add heygen-com/hyperframes --skill media-use -a claude-code` · [source: heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/blob/95e4e7f880f5005211412e926b307f4a53f47246/skills/media-use/SKILL.md) · 1,500,000 installs · installs ✓ 2026-11-16
- **[subagent-driven-development](https://affpapa.org/en/nevibecode/skills/subagent-driven-development)** — This skill runs an implementation plan through fresh subagents for independent tasks and reviews each result. Use it for multi-step work in one session.
  `npx skills add obra/superpowers --skill subagent-driven-development -a claude-code` · [source: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/subagent-driven-development/SKILL.md) · 237,746 installs · installs ✓ 2026-11-16
- **[caveman-stats](https://affpapa.org/en/nevibecode/skills/caveman-stats)** — Displays recorded output and cache-read tokens for Claude Code sessions or points to host native usage stats. Useful for tracking raw token consumption.
  `npx skills add JuliusBrussee/caveman --skill caveman-stats -a claude-code` · [source: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/9b243662ff98d392bc0a95b865a554583d71be75/skills/caveman-stats/SKILL.md) · 381,900 installs · installs ✓ 2026-11-16
- **[claude-api](https://affpapa.org/en/nevibecode/skills/claude-api)** — Reference skill for the Claude API and Anthropic SDK that enforces valid model IDs, adaptive thinking, and streaming.
  `npx skills add anthropics/skills --skill claude-api -a claude-code` · [source: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/claude-api/SKILL.md) · 74,198 installs · installs ✓ 2026-11-16
- **[karpathy-guidelines](https://affpapa.org/en/nevibecode/skills/karpathy-guidelines)** — Guidelines that cut typical LLM coding mistakes: less overcomplication, surgical edits, verifiable outcomes.
  `npx skills add multica-ai/andrej-karpathy-skills --skill karpathy-guidelines -a claude-code` · [source: multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/skills/karpathy-guidelines/SKILL.md) · 47,100 installs · installs ✓ 2026-11-16
- **[google-agents-cli-publish](https://affpapa.org/en/nevibecode/skills/google-agents-cli-publish)** — Walks a coding agent through agents-cli publish gemini: ADK and A2A registration modes, flags, metadata auto-detection and Agent Registry entries.
  `npx skills add google/agents-cli --skill google-agents-cli-publish -a claude-code` · [source: google/agents-cli](https://github.com/google/agents-cli/blob/6eedbdc2f44c388cbfc5f305eb83b9924cfefebb/skills/google-agents-cli-publish/SKILL.md) · 575,900 installs · installs ✓ 2026-11-16
- **[caveman-optimize](https://affpapa.org/en/nevibecode/skills/caveman-optimize)** — This skill turns a Caveman report observation into an operator-selected candidate and a paired baseline evaluation. Approval is required before code changes.
  `npx skills add JuliusBrussee/caveman --skill caveman-optimize -a claude-code` · [source: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/9b243662ff98d392bc0a95b865a554583d71be75/skills/caveman-optimize/SKILL.md) · 127,200 installs · installs ✓ 2026-11-16
- **[caveman-evidence-review](https://affpapa.org/en/nevibecode/skills/caveman-evidence-review)** — A read-only skill reviews Caveman Cloud evidence on LLM spend, traces, and routing. Use it to see where a project’s model budget goes.
  `npx skills add JuliusBrussee/caveman --skill caveman-evidence-review -a claude-code` · [source: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/9b243662ff98d392bc0a95b865a554583d71be75/skills/caveman-evidence-review/SKILL.md) · 125,700 installs · installs ✓ 2026-11-16
- **[context-engineering](https://affpapa.org/en/nevibecode/skills/context-engineering)** — Helps you set up agent context: which rules, specs and files to feed the agent, and when. Use it at the start of a session, when output quality drops, or when switching tasks.
  `npx skills add addyosmani/agent-skills --skill context-engineering -a claude-code` · [source: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/context-engineering/SKILL.md) · 75,400 installs

<a name="topic-automation"></a>
## Automation and no-code: n8n, Zapier, Make

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/automation](https://affpapa.org/en/nevibecode/topic/automation)

- **[gws-gmail-send](https://affpapa.org/en/nevibecode/skills/gws-gmail-send)** — A skill for Claude Code, Codex, Cursor, GitHub Copilot and Gemini CLI that exposes gws gmail +send to the agent. Sends Gmail messages with attachments, CC/BCC, HTML body and sender aliases.
  `npx skills add googleworkspace/cli --skill gws-gmail-send -a claude-code` · [source: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-gmail-send/SKILL.md) · 76,600 installs
- **[recipe-email-drive-link](https://affpapa.org/en/nevibecode/skills/recipe-email-drive-link)** — A skill for Claude Code, Codex, Cursor and other AI editors that strings together three tasks: find a file in Google Drive, grant access, and email the link. Works across six platforms and chains commands into one workflow.
  `npx skills add googleworkspace/cli --skill recipe-email-drive-link -a claude-code` · [source: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/recipe-email-drive-link/SKILL.md) · 32,400 installs
- **[recipe-label-and-archive-emails](https://affpapa.org/en/nevibecode/skills/recipe-label-and-archive-emails)** — A skill for six AI coding platforms that organizes your inbox by finding emails based on criteria, applying labels, and archiving them. Requires the gws-gmail skill and runs through Google Workspace CLI.
  `npx skills add googleworkspace/cli --skill recipe-label-and-archive-emails -a claude-code` · [source: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/recipe-label-and-archive-emails/SKILL.md) · 31,400 installs
- **[openhue](https://affpapa.org/en/nevibecode/skills/openhue)** — A skill for Claude Code, Codex, Cursor and other AI agents that controls Philips Hue lights and scenes through the OpenHue CLI.
  `npx skills add openclaw/openclaw --skill openhue -a claude-code` · [source: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/openhue/SKILL.md) · 5,200 installs
- **[baoyu-post-to-x](https://affpapa.org/en/nevibecode/skills/baoyu-post-to-x)** — Posts text, images, videos and long articles to X via Chrome. Works through Codex plugin, Computer Use or CDP scripts.
  `npx skills add JimLiu/baoyu-skills --skill baoyu-post-to-x -a claude-code` · [source: jimliu/baoyu-skills](https://github.com/JimLiu/baoyu-skills/blob/ca703c2d7c2c4399a1dc0cf82224f8551e05a96d/skills/baoyu-post-to-x/SKILL.md) · 29,400 installs
- **[baoyu-youtube-transcript](https://affpapa.org/en/nevibecode/skills/baoyu-youtube-transcript)** — Pulls YouTube transcripts and cover images from a URL or video ID. Handy when you want the text of a video without copying it by hand.
  `npx skills add JimLiu/baoyu-skills --skill baoyu-youtube-transcript -a claude-code` · [source: jimliu/baoyu-skills](https://github.com/JimLiu/baoyu-skills/blob/ca703c2d7c2c4399a1dc0cf82224f8551e05a96d/skills/baoyu-youtube-transcript/SKILL.md) · 22,800 installs
- **[wacli](https://affpapa.org/en/nevibecode/skills/wacli)** — Enables your coding agent to send WhatsApp messages to third parties, search conversation history, and backfill chat archives using the wacli tool.
  `npx skills add openclaw/openclaw --skill wacli -a claude-code` · [source: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/extensions/whatsapp/skills/wacli/SKILL.md) · 3,300 installs
- **[just](https://affpapa.org/en/nevibecode/skills/just)** — Reference skill for just, a command runner that executes tasks from a justfile. Use when your project has a justfile or you need syntax help for recipes and commands.
  `npx skills add casey/just --skill just -a claude-code` · [source: casey/just](https://github.com/casey/just/blob/168c8e288dc8a591ca851b4ef070cada64f43c35/skills/just/SKILL.md) · 1,200 installs
- **[create-an-asset](https://affpapa.org/en/nevibecode/skills/create-an-asset)** — This skill assembles decks, one-pagers and leave-behinds from account data, call notes and approved materials without invented numbers. Works in Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI and OpenCode.
  `npx skills add anthropics/knowledge-work-plugins --skill create-an-asset -a claude-code` · [source: anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/sales/skills/create-an-asset/SKILL.md) · 3,100 installs
- **[iros-registry-automation](https://affpapa.org/en/nevibecode/skills/iros-registry-automation)** — Prepares Korean IROS real estate and corporate registry requests inside a browser session. Helps stage document issuance without touching payments.
  `npx skills add NomaDamas/k-skill --skill iros-registry-automation -a claude-code` · [source: nomadamas/k-skill](https://github.com/NomaDamas/k-skill/blob/9766d20fb1fe1a5eb1d10ef5ff9872c8d6fc4985/iros-registry-automation/SKILL.md) · 11,000 installs

<a name="topic-docs"></a>
## Writing and docs

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/docs](https://affpapa.org/en/nevibecode/topic/docs)

- **[grill-with-docs](https://affpapa.org/en/nevibecode/skills/grill-with-docs)** — This skill interviews you about a plan or design and creates ADRs and a glossary along the way. Use it when decisions need sharper definition.
  `npx skills add mattpocock/skills --skill grill-with-docs -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/grill-with-docs/SKILL.md) · 1,219,756 installs · installs ✓ 2026-11-16
- **[domain-modeling](https://affpapa.org/en/nevibecode/skills/domain-modeling)** — This skill sharpens project terminology, maintains GLOSSARY.md, and records selected architecture decisions in ADRs. Use it while the domain model is changing.
  `npx skills add mattpocock/skills --skill domain-modeling -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/domain-modeling/SKILL.md) · 876,391 installs · installs ✓ 2026-11-16
- **[to-spec](https://affpapa.org/en/nevibecode/skills/to-spec)** — Turns the current conversation and repository context into a spec, then publishes it to the project issue tracker. Use it when a feature discussion is ready to hand off to an agent.
  `npx skills add mattpocock/skills --skill to-spec -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/to-spec/SKILL.md) · 715,388 installs · installs ✓ 2026-11-16
- **[pdf](https://affpapa.org/en/nevibecode/skills/pdf)** — This skill lets an agent read, create, and edit PDF files, including forms and scanned documents. Use it when PDF work is part of the task.
  `npx skills add anthropics/skills --skill pdf -a claude-code` · [source: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/pdf/SKILL.md) · 216,041 installs
- **[doc-coauthoring](https://affpapa.org/en/nevibecode/skills/doc-coauthoring)** — Guides document drafting through context collection, section work, and a reader check. Use it for specs, RFCs, proposals, and decision documents.
  `npx skills add anthropics/skills --skill doc-coauthoring -a claude-code` · [source: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/doc-coauthoring/SKILL.md) · 93,900 installs
- **[caveman-help](https://affpapa.org/en/nevibecode/skills/caveman-help)** — A quick reference for Caveman modes and commands in Claude Code and other supported hosts. Use it when you need to control response style or find related skills.
  `npx skills add JuliusBrussee/caveman --skill caveman-help -a claude-code` · [source: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/9b243662ff98d392bc0a95b865a554583d71be75/skills/caveman-help/SKILL.md) · 425,100 installs · installs ✓ 2026-11-16
- **[internal-comms](https://affpapa.org/en/nevibecode/skills/internal-comms)** — internal-comms helps Claude write internal communications in the formats your company uses, from status reports to FAQs and incident reports.
  `npx skills add anthropics/skills --skill internal-comms -a claude-code` · [source: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/internal-comms/SKILL.md) · 79,929 installs · installs ✓ 2026-11-16
- **[archify](https://affpapa.org/en/nevibecode/skills/archify)** — Creates checked diagrams and one-page explainers as standalone HTML. Use it to show a system’s structure, data flow, or database schema.
  `npx skills add tt-a1i/archify --skill archify -a claude-code` · [source: tt-a1i/archify](https://github.com/tt-a1i/archify/blob/a7ed6fd6657da90414831d1d42cf95987188750c/archify/SKILL.md) · 192,900 installs · installs ✓ 2026-11-16
- **[writing-guidelines](https://affpapa.org/en/nevibecode/skills/writing-guidelines)** — A skill that reviews docs and prose against a written style guide. You get findings with line numbers instead of hunting through the file yourself.
  `npx skills add vercel-labs/agent-skills --skill writing-guidelines -a claude-code` · [source: vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/writing-guidelines/SKILL.md) · 129,300 installs
- **[spec-driven-development](https://affpapa.org/en/nevibecode/skills/spec-driven-development)** — This Claude Code skill drafts a specification before coding begins. It activates for vague requirements, new features, project plans, and changes to an existing spec.
  `npx skills add addyosmani/agent-skills --skill spec-driven-development -a claude-code` · [source: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/spec-driven-development/SKILL.md) · 79,100 installs · installs ✓ 2026-11-16

<a name="topic-office"></a>
## Office documents

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/office](https://affpapa.org/en/nevibecode/topic/office)

- **[pptx](https://affpapa.org/en/nevibecode/skills/pptx)** — Skill for Claude Code creates, parses, and edits .pptx and .potx files. It activates whenever a prompt involves slides, slide decks, or presentation templates.
  `npx skills add anthropics/skills --skill pptx -a claude-code` · [source: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/pptx/SKILL.md) · 241,433 installs
- **[docx](https://affpapa.org/en/nevibecode/skills/docx)** — A skill for Claude Code and Claude.ai that creates, reads, and edits Word documents. It activates for requests involving .docx files or .dotx templates.
  `npx skills add anthropics/skills --skill docx -a claude-code` · [source: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/docx/SKILL.md) · 206,304 installs
- **[xlsx](https://affpapa.org/en/nevibecode/skills/xlsx)** — Skill for Claude Code and Claude.ai that generates, modifies, and validates spreadsheets. Triggers whenever tasks involve xlsx, xlsm, csv, or tsv files.
  `npx skills add anthropics/skills --skill xlsx -a claude-code` · [source: anthropics/skills](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/xlsx/SKILL.md) · 187,223 installs
- **[gws-sheets](https://affpapa.org/en/nevibecode/skills/gws-sheets)** — This skill lets an agent read and edit Google Sheets through the CLI. Use it when a coding workflow needs spreadsheet data or table updates.
  `npx skills add googleworkspace/cli --skill gws-sheets -a claude-code` · [source: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-sheets/SKILL.md) · 61,600 installs
- **[gws-sheets-read](https://affpapa.org/en/nevibecode/skills/gws-sheets-read)** — Reads cell values and sheets from Google Spreadsheets via CLI. Useful when an agent needs spreadsheet data without risk of altering it.
  `npx skills add googleworkspace/cli --skill gws-sheets-read -a claude-code` · [source: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-sheets-read/SKILL.md) · 52,600 installs
- **[gws-slides](https://affpapa.org/en/nevibecode/skills/gws-slides)** — Skill for Claude Code and other AI code editors that adds commands to read and modify Google Slides presentations from code. Runs on Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI, and OpenCode.
  `npx skills add googleworkspace/cli --skill gws-slides -a claude-code` · [source: googleworkspace/cli](https://github.com/googleworkspace/cli/blob/cd3697e07eb520056dcf142d0c7439bbb9ba32e9/skills/gws-slides/SKILL.md) · 43,600 installs
- **[gog](https://affpapa.org/en/nevibecode/skills/gog)** — Guides an agent using the gog CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs. Use it when Google Workspace tasks need to run from a terminal.
  `npx skills add openclaw/openclaw --skill gog -a claude-code` · [source: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/gog/SKILL.md) · 8,500 installs
- **[nano-pdf](https://affpapa.org/en/nevibecode/skills/nano-pdf)** — A skill for editing PDF pages using natural-language instructions through the nano-pdf CLI. Runs in Claude Code, Codex, Cursor, and other AI editors — change headings, fix typos, or rebuild layouts from code without opening manual tools.
  `npx skills add openclaw/openclaw --skill nano-pdf -a claude-code` · [source: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/nano-pdf/SKILL.md) · 7,200 installs
- **[convert-documents-to-markdown](https://affpapa.org/en/nevibecode/skills/convert-documents-to-markdown)** — Converts office documents, spreadsheets, and PDFs into GitHub-Flavored Markdown via anydoc. Useful when an agent must read DOCX or XLSX files without manual copy-pasting.
  `npx skills add firecrawl/anydoc --skill convert-documents-to-markdown -a claude-code` · [source: firecrawl/anydoc](https://github.com/firecrawl/anydoc/blob/e56a49bf3062c55e8d258346de4a36f4cfb59f70/skills/convert-documents-to-markdown/SKILL.md) · 13,700 installs
- **[nature-paper2ppt](https://affpapa.org/en/nevibecode/skills/nature-paper2ppt)** — Builds a Chinese academic .pptx from a scientific paper or reading notes, with figures from the source and speaker notes.
  `npx skills add Yuan1z0825/nature-skills --skill nature-paper2ppt -a claude-code` · [source: yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills/blob/14ca69710cae192325395a380e9cdd4ae5d9d0c8/skills/nature-paper2ppt/SKILL.md) · 17,500 installs

<a name="topic-seo"></a>
## SEO and GEO

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/seo](https://affpapa.org/en/nevibecode/topic/seo)

- **[seo-audit](https://affpapa.org/en/nevibecode/skills/coreyhaines31-seo-audit)** — A skill for Claude Code, Codex, and Cursor that guides technical SEO audits. Diagnoses traffic drops, indexing issues, canonical tags, and multilingual setups.
  `npx skills add coreyhaines31/marketingskills --skill seo-audit -a claude-code` · [source: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/seo-audit/SKILL.md) · 257,200 installs · installs ✓ 2026-11-16 · A/B 2026-11-16: +0.00 — no effect
- **[marketing-psychology](https://affpapa.org/en/nevibecode/skills/coreyhaines31-marketing-psychology)** — This Claude Code skill applies psychology to marketing decisions. It explains buyer behavior and assesses whether persuasion tactics are ethical.
  `npx skills add coreyhaines31/marketingskills --skill marketing-psychology -a claude-code` · [source: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/marketing-psychology/SKILL.md) · 179,700 installs
- **[ai-seo](https://affpapa.org/en/nevibecode/skills/ai-seo)** — This skill helps your content get cited in ChatGPT, Perplexity, Google AI Overviews and other LLM-generated answers. It shows how to format pages, structure content, and position information so AI systems select you as a source.
  `npx skills add coreyhaines31/marketingskills --skill ai-seo -a claude-code` · [source: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/ai-seo/SKILL.md) · 166,900 installs · A/B 2026-11-16: -0.21 — no effect, ~9k tokens
- **[seo](https://affpapa.org/en/nevibecode/skills/affaan-m-seo)** — A skill that walks your coding agent through technical SEO, on-page fixes, structured data and Core Web Vitals, with page-level recommendations.
  `npx skills add affaan-m/ECC --skill seo -a claude-code` · [source: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/seo/SKILL.md) · 6,500 installs
- **[content-engine](https://affpapa.org/en/nevibecode/skills/content-engine)** — This skill turns articles, notes, and demos into content for X, LinkedIn, TikTok, YouTube, and newsletters. Use it for posts, scripts, or content calendars.
  `npx skills add affaan-m/ECC --skill content-engine -a claude-code` · [source: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/content-engine/SKILL.md) · 6,200 installs
- **[marketing-campaign](https://affpapa.org/en/nevibecode/skills/marketing-campaign)** — Plans and runs multi-channel marketing launches. It handles audience research, campaign angles, landing page copy, email sequences, and social posts.
  `npx skills add affaan-m/ECC --skill marketing-campaign -a claude-code` · [source: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/marketing-campaign/SKILL.md) · 6,100 installs
- **[fixing-metadata](https://affpapa.org/en/nevibecode/skills/fixing-metadata)** — Audits page metadata and fixes what's broken: titles, descriptions, canonical URLs, Open Graph, Twitter cards, icons and JSON-LD.
  `npx skills add ibelick/ui-skills --skill fixing-metadata -a claude-code` · [source: ibelick/ui-skills](https://github.com/ibelick/ui-skills/blob/f511eae41c996e3953fbeabf95d38e4077d40711/skills/fixing-metadata/SKILL.md) · 20,000 installs
- **[keyword-research](https://affpapa.org/en/nevibecode/skills/every-app-keyword-research)** — Finds search query opportunities via OpenSEO MCP tools, evaluates SERP metrics, and saves vetted keywords to the project.
  `npx skills add every-app/open-seo --skill keyword-research -a claude-code` · [source: every-app/open-seo](https://github.com/every-app/open-seo/blob/46b815be34723e46ceeefe9b2b907bb62b62fd76/plugins/openseo/skills/keyword-research/SKILL.md) · 7,800 installs
- **[competitor-analysis](https://affpapa.org/en/nevibecode/skills/competitor-analysis)** — A skill for Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI, and OpenCode that maps one competitor's organic footprint — ranking keywords, content themes, backlinks, and gaps. Point it at a domain and get an actionable plan.
  `npx skills add every-app/open-seo --skill competitor-analysis -a claude-code` · [source: every-app/open-seo](https://github.com/every-app/open-seo/blob/46b815be34723e46ceeefe9b2b907bb62b62fd76/plugins/openseo/skills/competitor-analysis/SKILL.md) · 7,500 installs
- **[seo-project-setup](https://affpapa.org/en/nevibecode/skills/seo-project-setup)** — Collects a site's SEO context, goals, positioning, competitors, and key pages. Use it before running other OpenSEO skills.
  `npx skills add every-app/open-seo --skill seo-project-setup -a claude-code` · [source: every-app/open-seo](https://github.com/every-app/open-seo/blob/46b815be34723e46ceeefe9b2b907bb62b62fd76/plugins/openseo/skills/seo-project-setup/SKILL.md) · 7,500 installs

<a name="topic-marketing"></a>
## Marketing and content

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/marketing](https://affpapa.org/en/nevibecode/topic/marketing)

- **[copywriting](https://affpapa.org/en/nevibecode/skills/coreyhaines31-copywriting)** — A skill for Claude Code, Codex, Cursor and other platforms that helps write and rewrite page text—homepage, landing, pricing, feature descriptions.
  `npx skills add coreyhaines31/marketingskills --skill copywriting -a claude-code` · [source: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/copywriting/SKILL.md) · 257,800 installs · installs ✓ 2026-11-16 · A/B 2026-11-16: -0.33 — bloats meta descriptions
- **[content-strategy](https://affpapa.org/en/nevibecode/skills/coreyhaines31-content-strategy)** — Skill for Claude Code and Codex that turns customer questions and search intent into an actionable editorial plan. Evaluates topic ideas before production starts.
  `npx skills add coreyhaines31/marketingskills --skill content-strategy -a claude-code` · [source: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/content-strategy/SKILL.md) · 179,600 installs
- **[copy-editing](https://affpapa.org/en/nevibecode/skills/coreyhaines31-copy-editing)** — A skill for editing marketing copy, emails, and descriptions without full rewrite.
  `npx skills add coreyhaines31/marketingskills --skill copy-editing -a claude-code` · [source: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/copy-editing/SKILL.md) · 163,900 installs
- **[brag](https://affpapa.org/en/nevibecode/skills/brag)** — A skill for Claude Code that turns project code into a short, polished launch video. It triggers when you ask to create a video or showcase your build.
  `npx skills add latent-spaces/brag --skill brag -a claude-code` · [source: latent-spaces/brag](https://github.com/latent-spaces/brag/blob/06379432a9243c951dfcc051153be18d2d261044/skills/brag/SKILL.md) · 24,600 installs
- **[baoyu-post-to-wechat](https://affpapa.org/en/nevibecode/skills/baoyu-post-to-wechat)** — Publishes articles and multi-image posts to WeChat Official Accounts using the official API or Chrome CDP.
  `npx skills add JimLiu/baoyu-skills --skill baoyu-post-to-wechat -a claude-code` · [source: jimliu/baoyu-skills](https://github.com/JimLiu/baoyu-skills/blob/ca703c2d7c2c4399a1dc0cf82224f8551e05a96d/skills/baoyu-post-to-wechat/SKILL.md) · 35,000 installs
- **[higgsfield-video-explainer](https://affpapa.org/en/nevibecode/skills/higgsfield-video-explainer)** — This Claude Code skill routes the legacy video-explainer workflow to Higgsfield’s illustrated process. It activates when explicitly invoked or when continuing that existing workflow.
  `npx skills add higgsfield-ai/skills --skill higgsfield-video-explainer -a claude-code` · [source: higgsfield-ai/skills](https://github.com/higgsfield-ai/skills/blob/27000402070db19d958789d05b3b52b6f4718d7c/higgsfield-video-explainer/SKILL.md) · 154,400 installs
- **[baoyu-post-to-weibo](https://affpapa.org/en/nevibecode/skills/baoyu-post-to-weibo)** — Prepare Weibo posts with text, images, or video, or turn a Markdown file into a headline article. The skill fills the page in Chrome; you review and publish it yourself.
  `npx skills add JimLiu/baoyu-skills --skill baoyu-post-to-weibo -a claude-code` · [source: jimliu/baoyu-skills](https://github.com/JimLiu/baoyu-skills/blob/ca703c2d7c2c4399a1dc0cf82224f8551e05a96d/skills/baoyu-post-to-weibo/SKILL.md) · 22,100 installs
- **[crosspost](https://affpapa.org/en/nevibecode/skills/crosspost)** — Skill for distributing content to X, LinkedIn, Threads, and Bluesky with platform-specific adaptation. Creates separate versions tailored to each network's constraints and audience instead of posting identical copy everywhere.
  `npx skills add affaan-m/ECC --skill crosspost -a claude-code` · [source: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/crosspost/SKILL.md) · 5,900 installs
- **[investor-outreach](https://affpapa.org/en/nevibecode/skills/investor-outreach)** — Skill for crafting investor emails, warm intro requests, and fund updates. Produces personalized outreach with explicit asks, no generic phrases or vague praise.
  `npx skills add affaan-m/ECC --skill investor-outreach -a claude-code` · [source: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/investor-outreach/SKILL.md) · 5,900 installs
- **[reddit-automation](https://affpapa.org/en/nevibecode/skills/reddit-automation)** — Finds Reddit threads where people actually need what you sell, then drafts short helpful replies that disclose your affiliation.
  `npx skills add flowkit-labs/skills --skill reddit-automation -a claude-code` · [source: flowkit-labs/skills](https://github.com/flowkit-labs/skills/blob/0c9e2b63f504a296a86e45ed3a60a426dd979ca6/reddit-automation/SKILL.md) · 1,400,000 installs

<a name="topic-browser"></a>
## Browser and scraping

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/browser](https://affpapa.org/en/nevibecode/topic/browser)

- **[agent-browser](https://affpapa.org/en/nevibecode/skills/vercel-labs-agent-browser)** — This Claude Code skill automates browser interaction for tasks like navigating sites, filling forms, and testing web apps. It also supports exploratory QA and Electron app automation.
  `npx skills add vercel-labs/agent-browser --skill agent-browser -a claude-code` · [source: vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/blob/9f62847e89712164a6d5ea823e8c700d5fd911cd/skills/agent-browser/SKILL.md) · 1,500,000 installs · installs ✓ 2026-11-16
- **[browser-use](https://affpapa.org/en/nevibecode/skills/browser-use)** — A Claude Code skill for controlling Chrome or Chromium instances through the Chrome DevTools Protocol. Handles clicks, form inputs, screenshots, and scraping on dynamic web pages.
  `npx skills add browser-use/browser-use --skill browser-use -a claude-code` · [source: browser-use/browser-use](https://github.com/browser-use/browser-use/blob/4b5b1b0aa0ab45a1d6a2a31984d37d3e748c0134/skills/browser-use/SKILL.md) · 99,800 installs · installs ✓ 2026-11-16
- **[playwright-cli](https://affpapa.org/en/nevibecode/skills/playwright-cli)** — A skill that hands your agent a browser: open a page, click elements, grab a snapshot, and work with Playwright tests.
  `npx skills add microsoft/playwright-cli --skill playwright-cli -a claude-code` · [source: microsoft/playwright-cli](https://github.com/microsoft/playwright-cli/blob/b21724888b8100b05ef8dee3a92f2bb03bf4dcde/skills/playwright-cli/SKILL.md) · 218,400 installs · installs ✓ 2026-11-16
- **[scrapling-official](https://affpapa.org/en/nevibecode/skills/scrapling-official)** — A skill that gets your agent writing Scrapling code: HTTP requests, stealth browsers, Cloudflare bypass, spiders and adaptive parsing.
  `npx skills add D4Vinci/Scrapling --skill scrapling-official -a claude-code` · [source: d4vinci/scrapling](https://github.com/D4Vinci/Scrapling/blob/bb223f2f5fc8f743772751a5ce283ef7851ca6be/agent-skill/Scrapling-Skill/SKILL.md) · 6,900 installs
- **[ego-browser](https://affpapa.org/en/nevibecode/skills/ego-browser)** — Controls the ego-lite Chromium browser to click buttons, fill forms, take screenshots, and test web apps. Runs when agents need your existing browser sessions to inspect UI flows.
  `npx skills add citrolabs/ego-lite --skill ego-browser -a claude-code` · [source: citrolabs/ego-lite](https://github.com/citrolabs/ego-lite/blob/f499162d1b911ba9b320ed31b741dba7ebc2e4d6/skills/ego-browser/SKILL.md) · 17,500 installs
- **[opencli-browser](https://affpapa.org/en/nevibecode/skills/opencli-browser)** — This skill drives Chrome through OpenCLI to inspect pages, use logged-in sites, capture API evidence, and manage native tabs and windows.
  `npx skills add jackwener/OpenCLI --skill opencli-browser -a claude-code` · [source: jackwener/opencli](https://github.com/jackwener/OpenCLI/blob/9bc5f5ca132ec4d4e48d7ee517d4303bf159e8e8/skills/opencli-browser/SKILL.md) · 20,800 installs
- **[browser-act](https://affpapa.org/en/nevibecode/skills/browser-act)** — A skill that hands your agent a browser CLI: navigate, wait for JavaScript, pull data, fill forms, take screenshots. Useful when plain fetch falls short.
  `npx skills add browser-act/skills --skill browser-act -a claude-code` · [source: browser-act/skills](https://github.com/browser-act/skills/blob/593316aa0f8ccd88bdf745c92b24a50641701973/browser-act/SKILL.md) · 108,500 installs
- **[opencli-autofix](https://affpapa.org/en/nevibecode/skills/opencli-autofix)** — Repairs broken OpenCLI adapters when websites alter their DOM or APIs. The agent inspects trace logs, explores live pages, and applies targeted patches.
  `npx skills add jackwener/OpenCLI --skill opencli-autofix -a claude-code` · [source: jackwener/opencli](https://github.com/jackwener/OpenCLI/blob/9bc5f5ca132ec4d4e48d7ee517d4303bf159e8e8/skills/opencli-autofix/SKILL.md) · 18,100 installs
- **[browser-act-skill-forge](https://affpapa.org/en/nevibecode/skills/browser-act-skill-forge)** — Explores a website through browser-act and forges a skill package with SKILL.md and Python scripts. Later runs skip the exploration step.
  `npx skills add browser-act/skills --skill browser-act-skill-forge -a claude-code` · [source: browser-act/skills](https://github.com/browser-act/skills/blob/593316aa0f8ccd88bdf745c92b24a50641701973/browser-act-skill-forge/SKILL.md) · 85,200 installs
- **[baoyu-url-to-markdown](https://affpapa.org/en/nevibecode/skills/baoyu-url-to-markdown)** — Fetches webpages via Chrome CDP and converts their content into Markdown. Runs when an agent needs to archive articles, social threads, or video transcripts.
  `npx skills add JimLiu/baoyu-skills --skill baoyu-url-to-markdown -a claude-code` · [source: jimliu/baoyu-skills](https://github.com/JimLiu/baoyu-skills/blob/ca703c2d7c2c4399a1dc0cf82224f8551e05a96d/skills/baoyu-url-to-markdown/SKILL.md) · 30,900 installs

<a name="topic-mobile"></a>
## Mobile

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/mobile](https://affpapa.org/en/nevibecode/topic/mobile)

- **[vercel-react-native-skills](https://affpapa.org/en/nevibecode/skills/vercel-react-native-skills)** — A rules pack for React Native and Expo work: lists, animations, navigation, native modules. Load it so your agent makes mobile changes the same way every time.
  `npx skills add vercel-labs/agent-skills --skill vercel-react-native-skills -a claude-code` · [source: vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/react-native-skills/SKILL.md) · 279,400 installs
- **[write-swift](https://affpapa.org/en/nevibecode/skills/write-swift)** — A Swift skill for Claude Code guides code writing and review. It activates for Swift changes, migrations, and fixes involving concurrency, hangs, memory, or performance.
  `npx skills add emilkowalski/skills --skill write-swift -a claude-code` · [source: emilkowalski/skills](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills/write-swift/SKILL.md) · 165,900 installs · installs ✓ 2026-11-16
- **[aso](https://affpapa.org/en/nevibecode/skills/aso)** — Skill for Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI, and OpenCode that audits mobile store listings. Evaluates App Store and Google Play assets against ranking factors.
  `npx skills add coreyhaines31/marketingskills --skill aso -a claude-code` · [source: coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/aso/SKILL.md) · 87,100 installs
- **[swiftui-pro](https://affpapa.org/en/nevibecode/skills/swiftui-pro)** — Reviews SwiftUI code for deprecated APIs, data-flow issues, accessibility gaps, and performance concerns. Use it during feature work or code review.
  `npx skills add twostraws/SwiftUI-Agent-Skill --skill swiftui-pro -a claude-code` · [source: twostraws/swiftui-agent-skill](https://github.com/twostraws/SwiftUI-Agent-Skill/blob/f2920b63995263f57b3e198674e89a602efba6d2/swiftui-pro/SKILL.md) · 38,300 installs
- **[orca-emulator](https://affpapa.org/en/nevibecode/skills/orca-emulator)** — This Claude Code skill controls a booted iOS Simulator on macOS through Orca. It can tap, type, rotate the device, and inspect the accessibility tree.
  `npx skills add stablyai/orca --skill orca-emulator -a claude-code` · [source: stablyai/orca](https://github.com/stablyai/orca/blob/b30d12992e702724fffb426759c907d9b4450586/skills/orca-emulator/SKILL.md) · 6,300 installs
- **[orca-emulator-android](https://affpapa.org/en/nevibecode/skills/orca-emulator-android)** — This Claude Code skill controls an Android device or emulator through adb. It handles app interactions and runtime checks.
  `npx skills add stablyai/orca --skill orca-emulator-android -a claude-code` · [source: stablyai/orca](https://github.com/stablyai/orca/blob/b30d12992e702724fffb426759c907d9b4450586/skills/orca-emulator-android/SKILL.md) · 6,000 installs
- **[swiftui-expert-skill](https://affpapa.org/en/nevibecode/skills/swiftui-expert-skill)** — Skill for Claude Code, Codex, and Cursor. Guides assistants through writing, reviewing, and diagnosing SwiftUI interfaces on iOS and macOS alongside Instruments trace analysis.
  `npx skills add AvdLee/SwiftUI-Agent-Skill --skill swiftui-expert-skill -a claude-code` · [source: avdlee/swiftui-agent-skill](https://github.com/AvdLee/SwiftUI-Agent-Skill/blob/62bd760f005093d1e2e4de5db156e456a5f96400/skills/swiftui-expert-skill/SKILL.md) · 36,700 installs
- **[android-clean-architecture](https://affpapa.org/en/nevibecode/skills/android-clean-architecture)** — Tells the agent how to split an Android or KMP project into layers: modules, dependency rules, UseCases, repositories, plus Room, SQLDelight and Ktor patterns.
  `npx skills add affaan-m/ECC --skill android-clean-architecture -a claude-code` · [source: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/android-clean-architecture/SKILL.md) · 6,900 installs
- **[liquid-glass-design](https://affpapa.org/en/nevibecode/skills/liquid-glass-design)** — A skill that feeds your coding agent the iOS 26 Liquid Glass patterns for SwiftUI, UIKit and WidgetKit. Useful when you're building or porting an app to iOS 26+.
  `npx skills add affaan-m/ECC --skill liquid-glass-design -a claude-code` · [source: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/liquid-glass-design/SKILL.md) · 6,900 installs
- **[kotlin-coroutines-flows](https://affpapa.org/en/nevibecode/skills/kotlin-coroutines-flows)** — This skill covers Kotlin Coroutines and Flow patterns for Android and KMP. Use it when handling cancellation, concurrent work, reactive state, or tests.
  `npx skills add affaan-m/ECC --skill kotlin-coroutines-flows -a claude-code` · [source: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/kotlin-coroutines-flows/SKILL.md) · 6,400 installs

<a name="topic-gamedev"></a>
## Game dev and 3D: Unity, Unreal, Godot, Blender

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/gamedev](https://affpapa.org/en/nevibecode/topic/gamedev)

- **[gcode](https://affpapa.org/en/nevibecode/skills/gcode)** — Slices .stl, .3mf, and .obj files into .gcode or .gcode.3mf through OrcaSlicer. It never connects to a printer.
  `npx skills add earthtojake/text-to-cad --skill gcode -a claude-code` · [source: earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad/blob/4d42cb0bd9a61b46254bc8cf9bd9ae1f45c3295b/skills/gcode/SKILL.md) · 10,500 installs
- **[bambu-labs](https://affpapa.org/en/nevibecode/skills/bambu-labs)** — Hands print files off to Bambu Lab printers via Bambu Connect or Bambu Studio. The agent opens the file in the app; you pick the printer and press Print.
  `npx skills add earthtojake/text-to-cad --skill bambu-labs -a claude-code` · [source: earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad/blob/4d42cb0bd9a61b46254bc8cf9bd9ae1f45c3295b/skills/bambu-labs/SKILL.md) · 10,200 installs
- **[img2threejs](https://affpapa.org/en/nevibecode/skills/img2threejs)** — Builds a procedural Three.js model from an object or character image. Use it for code-based reconstruction, animation preparation, and staged model generation.
  `npx skills add img2threejs/img2threejs --skill img2threejs -a claude-code` · [source: img2threejs/img2threejs](https://github.com/img2threejs/img2threejs/blob/0c0c49bc168e648dbaf9c8c080474de0b3a941b6/SKILL.md) · 3,100 installs
- **[dfam-check](https://affpapa.org/en/nevibecode/skills/dfam-check)** — Validates 3D mesh files against additive manufacturing design rules before printing. Inspects wall thickness, overhangs, and build orientation for FDM, SLS, SLA, PBF, and MJF.
  `npx skills add earthtojake/text-to-cad --skill dfam-check -a claude-code` · [source: earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad/blob/4d42cb0bd9a61b46254bc8cf9bd9ae1f45c3295b/skills/dfam-check/SKILL.md) · 5,200 installs
- **[threejs-geometry](https://affpapa.org/en/nevibecode/skills/threejs-geometry)** — Teaches your coding agent how to build standard geometries, generate 3D text, and construct custom vertex buffers in three.js.
  `npx skills add CloudAI-X/threejs-skills --skill threejs-geometry -a claude-code` · [source: cloudai-x/threejs-skills](https://github.com/CloudAI-X/threejs-skills/blob/0e181866f095b5f06d005133876e926515390d95/skills/threejs-geometry/SKILL.md) · 20,600 installs
- **[threejs-lighting](https://affpapa.org/en/nevibecode/skills/threejs-lighting)** — Three.js r186 lighting skill for WebGL and WebGPU. It guides physical light units, cascaded shadow maps, and RectAreaLight setup.
  `npx skills add CloudAI-X/threejs-skills --skill threejs-lighting -a claude-code` · [source: cloudai-x/threejs-skills](https://github.com/CloudAI-X/threejs-skills/blob/0e181866f095b5f06d005133876e926515390d95/skills/threejs-lighting/SKILL.md) · 19,400 installs
- **[fal-3d](https://affpapa.org/en/nevibecode/skills/fal-3d)** — Skill for creating 3D models from text or images via fal.ai. Useful for game assets, AR previews, product mockups, and concept sculpting.
  `npx skills add nexu-io/open-design --skill fal-3d -a claude-code` · [source: nexu-io/open-design](https://github.com/nexu-io/open-design/blob/59e4f2ae85de7e7318a5e6bdcf3a34584c4b7582/skills/fal-3d/SKILL.md) · 3,000 installs
- **[game-feel](https://affpapa.org/en/nevibecode/skills/game-feel)** — Adds juice to game mechanics like trauma-based screen shake, hit-stop, and squash and stretch. Runs when hits and jumps feel flat or weightless.
  `npx skills add gamedev-skills/awesome-gamedev-agent-skills --skill game-feel -a claude-code` · [source: gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/disciplines/game-feel/SKILL.md) · 17,800 installs
- **[game-ui-ux](https://affpapa.org/en/nevibecode/skills/game-ui-ux)** — This Claude Code skill sets rules for game menus and HUDs. It comes into play when building screens or fixing layout and gamepad navigation across resolutions.
  `npx skills add gamedev-skills/awesome-gamedev-agent-skills --skill game-ui-ux -a claude-code` · [source: gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/disciplines/game-ui-ux/SKILL.md) · 17,700 installs
- **[shader-dev](https://affpapa.org/en/nevibecode/skills/minimax-ai-shader-dev)** — GLSL reference skill covering 36 real-time shader techniques for ShaderToy and WebGL2. Helpful for ray marching, SDF scenes, fluids, and visual effects.
  `npx skills add MiniMax-AI/skills --skill shader-dev -a claude-code` · [source: minimax-ai/skills](https://github.com/MiniMax-AI/skills/blob/02853d885acb1abc157477ce00c4d98a8ed14a71/skills/shader-dev/SKILL.md) · 2,700 installs

<a name="topic-science"></a>
## Science and research

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/science](https://affpapa.org/en/nevibecode/topic/science)

- **[academic-paper](https://affpapa.org/en/nevibecode/skills/academic-paper)** — This skill runs a 12-agent pipeline for academic paper writing in Claude Code.
  `npx skills add Imbad0202/academic-research-skills --skill academic-paper -a claude-code` · [source: imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills/blob/23bd688bbc121da6ae98ec3c4d4a7675cefc4c83/academic-paper/SKILL.md) · 11,600 installs
- **[nature-figure](https://affpapa.org/en/nevibecode/skills/nature-figure)** — A skill that builds, revises and audits scientific figures for manuscripts in Python or R. Useful when plots go to submission, not to a report.
  `npx skills add Yuan1z0825/nature-skills --skill nature-figure -a claude-code` · [source: yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills/blob/14ca69710cae192325395a380e9cdd4ae5d9d0c8/skills/nature-figure/SKILL.md) · 20,300 installs
- **[academic-paper-reviewer](https://affpapa.org/en/nevibecode/skills/academic-paper-reviewer)** — This skill reviews an academic paper through five role-based perspectives. Use it for peer review, revision checks, or a focused methodology assessment.
  `npx skills add Imbad0202/academic-research-skills --skill academic-paper-reviewer -a claude-code` · [source: imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills/blob/23bd688bbc121da6ae98ec3c4d4a7675cefc4c83/academic-paper-reviewer/SKILL.md) · 10,600 installs
- **[nature-citation](https://affpapa.org/en/nevibecode/skills/nature-citation)** — Finds Nature and CNS-family papers for manuscript claims, maps claims to sources, and prepares a reference-manager export. Use it when the journal scope matters.
  `npx skills add Yuan1z0825/nature-skills --skill nature-citation -a claude-code` · [source: yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills/blob/14ca69710cae192325395a380e9cdd4ae5d9d0c8/skills/nature-citation/SKILL.md) · 16,900 installs
- **[nature-academic-search](https://affpapa.org/en/nevibecode/skills/nature-academic-search)** — Searches research literature, checks citations, and builds MeSH strategies. Useful for source discovery, bibliography work, and citation audits.
  `npx skills add Yuan1z0825/nature-skills --skill nature-academic-search -a claude-code` · [source: yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills/blob/14ca69710cae192325395a380e9cdd4ae5d9d0c8/skills/nature-academic-search/SKILL.md) · 16,700 installs
- **[deep-research](https://affpapa.org/en/nevibecode/skills/imbad0202-deep-research)** — Runs a team of 13 agents through academic research on any topic, from framing the question to an APA 7.0 report.
  `npx skills add Imbad0202/academic-research-skills --skill deep-research -a claude-code` · [source: imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills/blob/23bd688bbc121da6ae98ec3c4d4a7675cefc4c83/deep-research/SKILL.md) · 8,200 installs
- **[paper-context-resolver](https://affpapa.org/en/nevibecode/skills/paper-context-resolver)** — Looks up one specific missing detail in a paper's primary sources, such as a dataset split or eval protocol, when a repo's README can't answer it.
  `npx skills add lllllllama/RigorPilot-Skills --skill paper-context-resolver -a claude-code` · [source: lllllllama/rigorpilot-skills](https://github.com/lllllllama/RigorPilot-Skills/blob/fb3ccdf5aa64b1fa5b1d0463e666a8bc8bc26e01/skills/paper-context-resolver/SKILL.md) · 499,800 installs
- **[read-arxiv-paper](https://affpapa.org/en/nevibecode/skills/read-arxiv-paper)** — This skill reads an arXiv paper from its source files and writes a Markdown report. It is useful when research needs to be connected to nanochat.
  `npx skills add karpathy/nanochat --skill read-arxiv-paper -a claude-code` · [source: karpathy/nanochat](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/.claude/skills/read-arxiv-paper/SKILL.md) · 2,900 installs
- **[ai-research-reproduction](https://affpapa.org/en/nevibecode/skills/ai-research-reproduction)** — This skill guides a repository-grounded reproduction run from its README to an evidence bundle. Use it to test a documented model run without quietly changing the experiment.
  `npx skills add lllllllama/RigorPilot-Skills --skill ai-research-reproduction -a claude-code` · [source: lllllllama/rigorpilot-skills](https://github.com/lllllllama/RigorPilot-Skills/blob/fb3ccdf5aa64b1fa5b1d0463e666a8bc8bc26e01/skills/ai-research-reproduction/SKILL.md) · 359,800 installs
- **[start](https://affpapa.org/en/nevibecode/skills/anthropics-start)** — Checks connected MCP servers and surveys bio-research tools. Helps researchers get oriented with the plugin before starting a project.
  `npx skills add anthropics/knowledge-work-plugins --skill start -a claude-code` · [source: anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/bio-research/skills/start/SKILL.md) · 5,000 installs

<a name="topic-git"></a>
## Git and GitHub

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/git](https://affpapa.org/en/nevibecode/topic/git)

- **[triage](https://affpapa.org/en/nevibecode/skills/triage)** — This skill moves issues and external PRs through triage states, verification, and agent briefs. It fits maintainers managing an issue queue.
  `npx skills add mattpocock/skills --skill triage -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/triage/SKILL.md) · 990,453 installs · installs ✓ 2026-11-16
- **[git-guardrails-claude-code](https://affpapa.org/en/nevibecode/skills/git-guardrails-claude-code)** — This skill adds a Claude Code hook that stops risky Git commands before they run. Use it when an agent must not push or discard working-tree changes.
  `npx skills add mattpocock/skills --skill git-guardrails-claude-code -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/misc/git-guardrails-claude-code/SKILL.md) · 499,069 installs · installs ✓ 2026-11-16
- **[using-git-worktrees](https://affpapa.org/en/nevibecode/skills/using-git-worktrees)** — Prepares an isolated workspace before feature work or plan execution. It checks the repository first, then uses native worktree support or Git.
  `npx skills add obra/superpowers --skill using-git-worktrees -a claude-code` · [source: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-git-worktrees/SKILL.md) · 217,153 installs · installs ✓ 2026-11-16
- **[finishing-a-development-branch](https://affpapa.org/en/nevibecode/skills/finishing-a-development-branch)** — This skill checks the test suite and guides branch completion: merge locally, open a Pull Request, or leave the work in place.
  `npx skills add obra/superpowers --skill finishing-a-development-branch -a claude-code` · [source: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/finishing-a-development-branch/SKILL.md) · 214,439 installs · installs ✓ 2026-11-16
- **[caveman-commit](https://affpapa.org/en/nevibecode/skills/caveman-commit)** — Generates terse Conventional Commits messages focused strictly on intent. Ideal for keeping git history clean without boilerplate or AI signatures.
  `npx skills add JuliusBrussee/caveman --skill caveman-commit -a claude-code` · [source: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/9b243662ff98d392bc0a95b865a554583d71be75/skills/caveman-commit/SKILL.md) · 438,700 installs · installs ✓ 2026-11-16
- **[pr](https://affpapa.org/en/nevibecode/skills/pr)** — Helps Claude Code structure a PR body with a change summary, before-and-after evidence, and a clear account of merge risk.
  `npx skills add mattpocock/skills --skill pr -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/pr/SKILL.md) · 167,125 installs · installs ✓ 2026-11-16
- **[git-workflow-and-versioning](https://affpapa.org/en/nevibecode/skills/git-workflow-and-versioning)** — A skill that structures git discipline: atomic commits, short-lived branches, messages that explain why. It activates whenever the agent prepares any code change for commit.
  `npx skills add addyosmani/agent-skills --skill git-workflow-and-versioning -a claude-code` · [source: addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/39b723ceebf81474d0557c1fecd01eddab585563/skills/git-workflow-and-versioning/SKILL.md) · 73,100 installs
- **[gh-fix-ci](https://affpapa.org/en/nevibecode/skills/openai-gh-fix-ci)** — Finds failing GitHub Actions checks on a pull request, inspects logs, and drafts a fix plan. The skill modifies code only after explicit approval.
  `npx skills add openai/skills --skill gh-fix-ci -a claude-code` · [source: openai/skills](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/gh-fix-ci/SKILL.md) · 12,000 installs
- **[github](https://affpapa.org/en/nevibecode/skills/github)** — Skill for GitHub through CLI: view and create pull requests, manage issues, check CI status, handle reviews and releases. Works on Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI, and OpenCode.
  `npx skills add openclaw/openclaw --skill github -a claude-code` · [source: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/github/SKILL.md) · 6,100 installs
- **[gh-issues](https://affpapa.org/en/nevibecode/skills/gh-issues)** — This skill finds GitHub issues, starts background fix agents, and opens PRs. Use it when you want an issue-to-PR workflow with optional review handling.
  `npx skills add openclaw/openclaw --skill gh-issues -a claude-code` · [source: openclaw/openclaw](https://github.com/openclaw/openclaw/blob/2014d1afbfeac3b88851491ea9753bb9f82ad520/skills/gh-issues/SKILL.md) · 5,000 installs

<a name="topic-productivity"></a>
## Notes, tasks and projects

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/productivity](https://affpapa.org/en/nevibecode/topic/productivity)

- **[find-skills](https://affpapa.org/en/nevibecode/skills/find-skills)** — Discovers and installs agent skills from skills.sh directly inside your coding assistant. Handy when you need domain-specific workflows for a project.
  `npx skills add vercel-labs/skills --skill find-skills -a claude-code` · [source: vercel-labs/skills](https://github.com/vercel-labs/skills/blob/50894c1d98bc45ca1ab127213e59d6525065b5e7/skills/find-skills/SKILL.md) · 4,400,000 installs · installs ✓ 2026-11-16
- **[grill-me](https://affpapa.org/en/nevibecode/skills/grill-me)** — grill-me interviews you about a plan or design to expose gaps and sharpen decisions. Use it before implementation starts.
  `npx skills add mattpocock/skills --skill grill-me -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/grill-me/SKILL.md) · 1,424,476 installs · installs ✓ 2026-11-16
- **[handoff](https://affpapa.org/en/nevibecode/skills/handoff)** — Creates a handoff document from the current conversation so another agent can continue the work. Use it when a task moves to a new session or agent.
  `npx skills add mattpocock/skills --skill handoff -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/handoff/SKILL.md) · 1,038,491 installs · installs ✓ 2026-11-16
- **[grilling](https://affpapa.org/en/nevibecode/skills/grilling)** — Stress-test a plan, decision, or idea through structured rounds of questions. Use it when you need to expose assumptions before acting.
  `npx skills add mattpocock/skills --skill grilling -a claude-code` · [source: mattpocock/skills](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/grilling/SKILL.md) · 979,543 installs · installs ✓ 2026-11-16
- **[using-superpowers](https://affpapa.org/en/nevibecode/skills/using-superpowers)** — Checks for relevant skills before an agent responds or takes action. Use it when you want a fixed workflow for handling tasks.
  `npx skills add obra/superpowers --skill using-superpowers -a claude-code` · [source: obra/superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-superpowers/SKILL.md) · 270,479 installs · installs ✓ 2026-11-16
- **[caveman](https://affpapa.org/en/nevibecode/skills/juliusbrussee-caveman)** — Cuts filler and polite greetings from agent responses while keeping technical facts and code exact. Stays active until turned off.
  `npx skills add JuliusBrussee/caveman --skill caveman -a claude-code` · [source: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/9b243662ff98d392bc0a95b865a554583d71be75/skills/caveman/SKILL.md) · 630,200 installs · installs ✓ 2026-11-16
- **[ponytail-help](https://affpapa.org/en/nevibecode/skills/ponytail-help)** — Shows a quick reference card for ponytail levels, skills, and configuration inside the chat. Useful when you need command triggers without leaving your editor.
  `npx skills add DietrichGebert/ponytail --skill ponytail-help -a claude-code` · [source: dietrichgebert/ponytail](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail-help/SKILL.md) · 56,400 installs · installs ✓ 2026-11-16
- **[ponytail-gain](https://affpapa.org/en/nevibecode/skills/ponytail-gain)** — Displays measured benchmark savings across code volume, token spend, and execution time for Ponytail. Useful when evaluating the toolset.
  `npx skills add DietrichGebert/ponytail --skill ponytail-gain -a claude-code` · [source: dietrichgebert/ponytail](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail-gain/SKILL.md) · 54,200 installs · installs ✓ 2026-11-16
- **[caveman-learn](https://affpapa.org/en/nevibecode/skills/caveman-learn)** — This skill reads Caveman learn reports, proposes token-cost reductions, and asks for consent before each edit. Use it for heavy CLAUDE.md files or repeated context.
  `npx skills add JuliusBrussee/caveman --skill caveman-learn -a claude-code` · [source: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/9b243662ff98d392bc0a95b865a554583d71be75/skills/caveman-learn/SKILL.md) · 128,200 installs · installs ✓ 2026-11-16
- **[lean-build](https://affpapa.org/en/nevibecode/skills/lean-build)** — Prevents overbuilding when adding new features or integrations. It sets strict acceptance bounds, cuts speculative abstractions, and stops immediately once proof passes.
  `npx skills add JuliusBrussee/caveman --skill lean-build -a claude-code` · [source: juliusbrussee/caveman](https://github.com/JuliusBrussee/caveman/blob/9b243662ff98d392bc0a95b865a554583d71be75/skills/lean-build/SKILL.md) · 125,800 installs · installs ✓ 2026-11-16

<a name="topic-finance"></a>
## Finance and business

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/finance](https://affpapa.org/en/nevibecode/topic/finance)

- **[market-research](https://affpapa.org/en/nevibecode/skills/affaan-m-market-research)** — A skill for market research, competitor comparisons and investor diligence. Useful when you need a decision backed by evidence, not a tidy report.
  `npx skills add affaan-m/ECC --skill market-research -a claude-code` · [source: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/market-research/SKILL.md) · 7,600 installs
- **[investor-materials](https://affpapa.org/en/nevibecode/skills/investor-materials)** — Creates and aligns pitch decks, one-pagers, financial models, and accelerator applications. Keeps all numbers and assumptions consistent across fundraising documents.
  `npx skills add affaan-m/ECC --skill investor-materials -a claude-code` · [source: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/investor-materials/SKILL.md) · 6,200 installs
- **[customs-trade-compliance](https://affpapa.org/en/nevibecode/skills/customs-trade-compliance)** — Classifies goods under HS/HTS codes, checks denied-party lists, and verifies trade documents across US, EU, UK, and APAC jurisdictions.
  `npx skills add affaan-m/ECC --skill customs-trade-compliance -a claude-code` · [source: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/customs-trade-compliance/SKILL.md) · 5,900 installs
- **[earnings-analysis](https://affpapa.org/en/nevibecode/skills/earnings-analysis)** — A skill for Claude Code, Codex, Cursor, Copilot, Gemini CLI and OpenCode that builds quarterly earnings update reports: 8–12 pages, tables, charts, beat/miss analysis.
  `npx skills add anthropics/financial-services --skill earnings-analysis -a claude-code` · [source: anthropics/financial-services](https://github.com/anthropics/financial-services/blob/60565064557ca77b12f62aa7877f365d111c129d/plugins/agent-plugins/earnings-reviewer/skills/earnings-analysis/SKILL.md) · 3,700 installs
- **[equity-research](https://affpapa.org/en/nevibecode/skills/equity-research)** — A skill for Claude Code, Codex, Cursor and other IDEs that chains five MCP tool calls into a structured equity research snapshot.
  `npx skills add anthropics/financial-services --skill equity-research -a claude-code` · [source: anthropics/financial-services](https://github.com/anthropics/financial-services/blob/60565064557ca77b12f62aa7877f365d111c129d/plugins/partner-built/lseg/skills/equity-research/SKILL.md) · 3,400 installs
- **[consulting-analysis](https://affpapa.org/en/nevibecode/skills/consulting-analysis)** — A skill for Claude Code and Codex that writes consulting reports in Markdown in two phases. It builds an analysis framework first, then turns collected data and charts into the final report.
  `npx skills add bytedance/deer-flow --skill consulting-analysis -a claude-code` · [source: bytedance/deer-flow](https://github.com/bytedance/deer-flow/blob/4a27b133f81dfa621bf17635f2659bef2eebb7fd/skills/public/consulting-analysis/SKILL.md) · 3,100 installs
- **[financial-statements](https://affpapa.org/en/nevibecode/skills/financial-statements)** — Generates financial statements with period comparisons and variance analysis. Use it for P&L preparation, period close, budget checks, and leadership summaries.
  `npx skills add anthropics/knowledge-work-plugins --skill financial-statements -a claude-code` · [source: anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/finance/skills/financial-statements/SKILL.md) · 4,800 installs
- **[backtesting-frameworks](https://affpapa.org/en/nevibecode/skills/backtesting-frameworks)** — Helps build trading strategy backtests that account for look-ahead and survivorship bias, plus transaction costs. Use it when developing or validating a trading algorithm.
  `npx skills add wshobson/agents --skill backtesting-frameworks -a claude-code` · [source: wshobson/agents](https://github.com/wshobson/agents/blob/4bde3168b43c0655c4d00ea2726e631719908a6d/plugins/quantitative-trading/skills/backtesting-frameworks/SKILL.md) · 16,710 installs
- **[dcf-model](https://affpapa.org/en/nevibecode/skills/dcf-model)** — Builds an institutional-grade DCF valuation model: pulls data from SEC filings and analyst reports, computes WACC and cash flows, and outputs an Excel model with sensitivity analysis.
  `npx skills add anthropics/financial-services --skill dcf-model -a claude-code` · [source: anthropics/financial-services](https://github.com/anthropics/financial-services/blob/60565064557ca77b12f62aa7877f365d111c129d/plugins/agent-plugins/model-builder/skills/dcf-model/SKILL.md) · 2,600 installs
- **[reconciliation](https://affpapa.org/en/nevibecode/skills/reconciliation)** — Compares GL balances with subledgers, bank statements, or third-party data. Useful for finding and classifying reconciliation differences.
  `npx skills add anthropics/knowledge-work-plugins --skill reconciliation -a claude-code` · [source: anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/finance/skills/reconciliation/SKILL.md) · 3,700 installs

<a name="topic-languages"></a>
## Programming languages

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/languages](https://affpapa.org/en/nevibecode/topic/languages)

- **[typescript-advanced-types](https://affpapa.org/en/nevibecode/skills/typescript-advanced-types)** — Guides an agent through advanced TypeScript types, from generics to conditional and mapped types. Use it for typed libraries, API clients, or strict configuration objects.
  `npx skills add wshobson/agents --skill typescript-advanced-types -a claude-code` · [source: wshobson/agents](https://github.com/wshobson/agents/blob/9c61ab243def98f72da12abd41cfcf5bcd91af9d/plugins/javascript-typescript/skills/typescript-advanced-types/SKILL.md) · 92,169 installs
- **[python-patterns](https://affpapa.org/en/nevibecode/skills/affaan-m-python-patterns)** — Tells the agent how to write and review Python: idioms, type hints, exception handling, context managers.
  `npx skills add affaan-m/ECC --skill python-patterns -a claude-code` · [source: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/python-patterns/SKILL.md) · 7,200 installs
- **[golang-patterns](https://affpapa.org/en/nevibecode/skills/golang-patterns)** — This skill guides Go coding, reviews, and refactors with idiomatic patterns. Use it when package structure, errors, or concurrency need a closer check.
  `npx skills add affaan-m/ECC --skill golang-patterns -a claude-code` · [source: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/golang-patterns/SKILL.md) · 6,900 installs
- **[cpp-coding-standards](https://affpapa.org/en/nevibecode/skills/cpp-coding-standards)** — A skill that pushes your AI agent toward C++ Core Guidelines when it writes, reviews or refactors C++: RAII, immutability, strong typing.
  `npx skills add affaan-m/ECC --skill cpp-coding-standards -a claude-code` · [source: affaan-m/ecc](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/cpp-coding-standards/SKILL.md) · 6,700 installs
- **[python-performance-optimization](https://affpapa.org/en/nevibecode/skills/python-performance-optimization)** — This skill profiles Python code to locate CPU and memory bottlenecks. Use it when an application responds slowly or consumes too many resources.
  `npx skills add wshobson/agents --skill python-performance-optimization -a claude-code` · [source: wshobson/agents](https://github.com/wshobson/agents/blob/4bde3168b43c0655c4d00ea2726e631719908a6d/plugins/python-development/skills/python-performance-optimization/SKILL.md) · 35,675 installs
- **[design-patterns](https://affpapa.org/en/nevibecode/skills/design-patterns)** — Provides Rust architectural patterns for RTK CLI filter modules. Helps select Newtype, Builder, State Machine, and RAII during module design and refactoring.
  `npx skills add rtk-ai/rtk --skill design-patterns -a claude-code` · [source: rtk-ai/rtk](https://github.com/rtk-ai/rtk/blob/2a786dca60fa4759f4f8381262a6a3b98256667a/.claude/skills/design-patterns/SKILL.md) · 2,000 installs
- **[python-design-patterns](https://affpapa.org/en/nevibecode/skills/python-design-patterns)** — Use it to shape Python components, separate responsibilities, and decide when repeated code deserves an abstraction. It fits design and refactoring work.
  `npx skills add wshobson/agents --skill python-design-patterns -a claude-code` · [source: wshobson/agents](https://github.com/wshobson/agents/blob/4bde3168b43c0655c4d00ea2726e631719908a6d/plugins/python-development/skills/python-design-patterns/SKILL.md) · 22,842 installs
- **[typescript-expert](https://affpapa.org/en/nevibecode/skills/typescript-expert)** — A skill for TypeScript and JavaScript work: it reads your project setup, fixes type errors and speeds up type checking. Useful once a TS codebase gets big.
  `npx skills add sickn33/agentic-awesome-skills --skill typescript-expert -a claude-code` · [source: sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills/blob/560b762c309d6b96315855d7968727d3bca7df20/skills/typescript-expert/SKILL.md) · 12,800 installs
- **[cardputer-buddy](https://affpapa.org/en/nevibecode/skills/cardputer-buddy)** — Iterate on Cardputer-Adv MicroPython apps without re-flashing. The skill pushes individual files over serial, streams device logs, and runs one-shot REPL commands.
  `npx skills add anthropics/claude-plugins-official --skill cardputer-buddy -a claude-code` · [source: anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official/blob/b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6/plugins/cwc-makers/skills/cardputer-buddy/SKILL.md) · 2,897 installs
- **[swift-concurrency](https://affpapa.org/en/nevibecode/skills/swift-concurrency)** — Diagnoses Swift Concurrency issues, refactors callback code to async/await, and guides Swift 6 migration. Useful when isolation, Sendable, or compiler warnings block a change.
  `npx skills add AvdLee/Swift-Concurrency-Agent-Skill --skill swift-concurrency -a claude-code` · [source: avdlee/swift-concurrency-agent-skill](https://github.com/AvdLee/Swift-Concurrency-Agent-Skill/blob/3b1580d8398e0b5408b3bf0bada0e941a1cfc642/skills/swift-concurrency/SKILL.md) · 17,700 installs

<a name="topic-telegram"></a>
## Telegram bots

Whole topic in the catalog: [https://affpapa.org/en/nevibecode/topic/telegram](https://affpapa.org/en/nevibecode/topic/telegram)

- **[telegram-bot-builder](https://affpapa.org/en/nevibecode/skills/sickn33-telegram-bot-builder)** — Plan a Telegram bot’s architecture, menus, payments, and webhook setup with this skill. It’s useful when starting a bot or preparing one for production.
  `npx skills add sickn33/agentic-awesome-skills --skill telegram-bot-builder -a claude-code` · [source: sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills/blob/560b762c309d6b96315855d7968727d3bca7df20/skills/telegram-bot-builder/SKILL.md) · 3,800 installs
- **[telegram-bot](https://affpapa.org/en/nevibecode/skills/telegram-bot)** — A skill for building Telegram bots: chatbots, notifications, AI assistants and group automation. Useful when you need message handlers and workflows fast.
  `npx skills add claude-office-skills/skills --skill telegram-bot -a claude-code` · [source: claude-office-skills/skills](https://github.com/claude-office-skills/skills/blob/9c4c7d5cd2813a8936bf2c9fdb174ea883b85a11/telegram-bot/SKILL.md) · 6,500 installs
- **[tg-bot-binding](https://affpapa.org/en/nevibecode/skills/tg-bot-binding)** — Guides the AI through linking a Telegram bot to Starchild via QR code or manual BotFather tokens, plus resolving pairing errors.
  `npx skills add Starchild-ai-agent/official-skills --skill tg-bot-binding -a claude-code` · [source: starchild-ai-agent/official-skills](https://github.com/Starchild-ai-agent/official-skills/blob/0996b6d9872e0513160d4436e8f615b8097bcf59/tg-bot-binding/SKILL.md) · 2,200 installs
- **[meta](https://affpapa.org/en/nevibecode/skills/meta)** — Registers a /meta handler to run Claude Code Agent SDK sessions inside the telegram_agent directory and edit the bot from chat.
  `npx skills add glebis/claude-skills --skill meta -a claude-code` · [source: glebis/claude-skills](https://github.com/glebis/claude-skills/blob/4d37d3b0af1f98cb4ac820d9abbce95e38e909fb/meta/SKILL.md) · 228 installs
- **[tg-ws-proxy-telegram-socks5](https://affpapa.org/en/nevibecode/skills/tg-ws-proxy-telegram-socks5)** — Guides the setup of a local SOCKS5 proxy routing Telegram Desktop traffic to data centers over WebSockets. Useful for bypassing connection blocks without remote servers.
  `npx skills add reason-machines/trending-skills --skill tg-ws-proxy-telegram-socks5 -a claude-code` · [source: reason-machines/trending-skills](https://github.com/reason-machines/trending-skills/blob/c61b1a456af4015e9a367e0245292281bb3c87d9/skills/tg-ws-proxy-telegram-socks5/SKILL.md) · 889 installs
- **[telegram-group-analytics-bot](https://affpapa.org/en/nevibecode/skills/telegram-group-analytics-bot)** — This skill tracks Telegram group activity: member growth, message counts, hourly heatmaps and scheduled reports you can export.
  `npx skills add reason-machines/data-skills --skill telegram-group-analytics-bot -a claude-code` · [source: reason-machines/data-skills](https://github.com/reason-machines/data-skills/blob/25d6ee79eea935ef4be1ee375a5777b2ad259f0a/skills/telegram-group-analytics-bot/SKILL.md) · 614 installs
- **[telegram-group-statistics-analytics-bot](https://affpapa.org/en/nevibecode/skills/telegram-group-statistics-analytics-bot)** — Tracks Telegram group member changes, counts messages by participant, and exports periodic activity summaries. Designed for community managers monitoring chat health.
  `npx skills add reason-machines/data-skills --skill telegram-group-statistics-analytics-bot -a claude-code` · [source: reason-machines/data-skills](https://github.com/reason-machines/data-skills/blob/25d6ee79eea935ef4be1ee375a5777b2ad259f0a/skills/telegram-group-statistics-analytics-bot/SKILL.md) · 609 installs
- **[interactive-bot](https://affpapa.org/en/nevibecode/skills/interactive-bot)** — Skill documents the Gmail Commander Telegram bot: slash commands for email, AI routing of free-text through MCP, compose/reply sessions.
  `npx skills add terrylica/cc-skills --skill interactive-bot -a claude-code` · [source: terrylica/cc-skills](https://github.com/terrylica/cc-skills/blob/0ca36f7260a3eb5de13a1b684509c4ecd5fe819b/plugins/gmail-commander/skills/interactive-bot/SKILL.md) · 114 installs

## Updates and license

The list is built by `scripts/build.py` from the catalog database; checks snapshot: `data/checks-2026-11-16.json`. Built on 2026-11-17. Install counts come from the source the card was imported from. Descriptions were written for the affpapa.org catalog. The list and descriptions are [CC0 1.0](LICENSE). Each skill keeps its author’s license — check the source.
