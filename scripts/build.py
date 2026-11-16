#!/usr/bin/env python3
"""Собирает README.md, README.en.md и data/skills.json из базы каталога NeVibeCode (affpapa.org).

Нужны переменные окружения Postgres (PGHOST, PGUSER, PGDATABASE, PGPASSWORD) с доступом к таблице vibe_items,
файл тем data/topics.json (выгрузка config('nevibe.topics')) и снимок проверок data/checks-*.json.

Отбор: тип skill, опубликован на affpapa.org, не склеен с другой карточкой, не в архиве,
автоматическая проверка безопасности — без предупреждений (clean), есть команда установки,
которая проходит белый список символов. Дубли по имени схлопываются в самый популярный.
Тема — первая тема карточки. В теме — до PER_TOPIC самых популярных, не больше PER_REPO из одного репозитория;
тема с числом меньше MIN_TOPIC пропускается.
"""
import glob, json, os, re, subprocess, sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PER_TOPIC, MIN_TOPIC, PER_REPO = 10, 5, 3
SITE = 'https://affpapa.org'

SQL = r"""
select coalesce(json_agg(d order by d.popularity desc, d.id), '[]') from (
  select distinct on (lower(name)) id, slug, name, lede_ru, lede_en, source_url, gh_repo, install,
         frontmatter->>'name' as fm_name, installs, stars, popularity, topics->>0 as topic
  from vibe_items
  where type = 'skill' and is_public and gen_status = 'done' and not is_archived and merged_into_id is null
    and security_status = 'clean' and topics->>0 is not null
  order by lower(name), popularity desc, id
) d
"""

SAFE_NPX = re.compile(r'^npx skills add [A-Za-z0-9._-]+/[A-Za-z0-9._-]+ --skill ([A-Za-z0-9._:-]+) -a claude-code$')
SAFE_NAME = re.compile(r'^[a-z0-9][a-z0-9-]{0,63}$')


def rows():
    out = subprocess.run(['psql', '-X', '-At', '-v', 'ON_ERROR_STOP=1', '-c', SQL],
                         check=True, capture_output=True, text=True).stdout
    return json.loads(out)


def install_cmd(item):
    """Команда `npx skills add` с карточки. CLI ищет скил по name из frontmatter, а не по папке:
    если они расходятся, подставляем name (так ставится; см. отчёт B 16.11)."""
    inst = item['install']
    cmds = []
    if isinstance(inst, dict):
        for v in inst.values():
            cmds += v if isinstance(v, list) else [v]
    elif isinstance(inst, list):
        cmds = inst
    for c in cmds:
        if not isinstance(c, str):
            continue
        m = SAFE_NPX.match(c.strip())
        if not m:
            continue
        fm = (item.get('fm_name') or '').strip()
        if fm and fm != m.group(1) and SAFE_NAME.match(fm):
            return c.strip().replace('--skill ' + m.group(1) + ' ', '--skill ' + fm + ' '), True
        return c.strip(), False
    return None, False


def num_ru(n):
    return f'{n:,}'.replace(',', ' ')


def plural_ru(n, one, few, many):
    n10, n100 = n % 10, n % 100
    if n10 == 1 and n100 != 11:
        return one
    if 2 <= n10 <= 4 and not 12 <= n100 <= 14:
        return few
    return many


def num_en(n):
    return f'{n:,}'


def fmt_delta(d, ru):
    s = f'{d:+.2f}'
    return s.replace('.', ',') if ru else s


def clean(text):
    return re.sub(r'\s+', ' ', (text or '').replace('<', '‹').replace('>', '›')).strip()


def main():
    topics = json.load(open(os.path.join(ROOT, 'data', 'topics.json'), encoding='utf-8'))
    checks_file = sorted(glob.glob(os.path.join(ROOT, 'data', 'checks-*.json')))[-1]
    checks = json.load(open(checks_file, encoding='utf-8'))
    ok_ids = set(checks['install']['ok_ids'])
    ab = checks['ab']['items']
    exclude = checks.get('exclude', {})
    cdate = checks['date']
    cdate_ru = '.'.join(reversed(cdate.split('-')[1:]))  # 16.11

    by_topic = {k: [] for k in topics}
    for it in rows():
        if str(it['id']) in exclude or it['topic'] not in by_topic:
            continue
        if len(by_topic[it['topic']]) >= PER_TOPIC:
            continue
        if it['gh_repo'] and sum(1 for x in by_topic[it['topic']] if x['gh_repo'] == it['gh_repo']) >= PER_REPO:
            continue
        cmd, renamed = install_cmd(it)
        if not cmd:
            continue
        it['cmd'], it['cmd_renamed'] = cmd, renamed
        it['install_ok'] = it['id'] in ok_ids and not renamed
        it['ab'] = ab.get(str(it['id']))
        by_topic[it['topic']].append(it)
    by_topic = {k: v for k, v in by_topic.items() if len(v) >= MIN_TOPIC}
    total = sum(len(v) for v in by_topic.values())
    n_ok = sum(1 for v in by_topic.values() for i in v if i['install_ok'])
    n_ab = sum(1 for v in by_topic.values() for i in v if i['ab'])

    for lang in ('ru', 'en'):
        ru = lang == 'ru'
        L = []
        w = L.append
        if ru:
            w('# Скиллы для Claude Code, Codex и Cursor по темам')
            w('')
            w('English: [README.en.md](README.en.md)')
            w('')
            w(f'{total} скиллов в {len(by_topic)} темах из каталога [NeVibeCode]({SITE}/nevibecode) на affpapa.org. '
              f'В каждой теме — самые популярные скиллы, у которых автоматическая проверка безопасности {cdate_ru} не нашла предупреждений. '
              'У каждого скилла здесь команда установки, ссылка на карточку с описанием по-русски и ссылка на исходник.')
            w('')
            w(f'Методика и цифры проверки — [affpapa.org/nevibecode/research]({SITE}/nevibecode/research).')
        else:
            w('# Agent skills for Claude Code, Codex and Cursor, by topic')
            w('')
            w('По-русски: [README.md](README.md)')
            w('')
            w(f'{total} skills in {len(by_topic)} topics from the [NeVibeCode]({SITE}/en/nevibecode) catalog on affpapa.org. '
              f'Each topic lists the most popular skills that raised no warnings in the automated security check of {cdate}. '
              'Every entry has an install command, a link to its catalog card and a link to the source.')
            w('')
            w(f'Method and numbers: [affpapa.org/en/nevibecode/research]({SITE}/en/nevibecode/research).')
        w('')
        w('## Отметки' if ru else '## Marks')
        w('')
        if ru:
            w(f'- **ставится ✓ {cdate_ru}** — команду из списка запустили в песочнице {cdate_ru}: скилл установился, SKILL.md на месте и проходит проверку формата. '
              f'Проверяли 150 самых популярных скиллов каталога, рабочими по команде оказались 144. Здесь отметка стоит у {n_ok} скиллов; у остальных установку не запускали.')
            w(f'- **A/B {cdate_ru}** — скилл участвовал в тесте «ответ со скиллом против ответа без него» (3 модели, 5 тем, слепые судьи). '
              'Число — средняя разница оценок по шкале 1–10; шум самого метода 0,70, так что разница меньше этого — не результат.')
            w('- Безопасность: в каталоге 16.11 проверены 45 138 единиц и 20 101 исполняемый файл, вредоносного не нашли. '
              'Это статический разбор: переписанный под обход вредонос он может не увидеть. Скиллы с предупреждениями (чаще всего `curl | sh` в установке) в список не берём.')
        else:
            w(f'- **installs ✓ {cdate}** — the listed command was run in a sandbox on {cdate}: the skill installed, SKILL.md is in place and passes the format check. '
              f'We ran it for the 150 most popular skills in the catalog; 144 worked. {n_ok} skills here carry the mark; the rest were not install-tested.')
            w(f'- **A/B {cdate}** — the skill was in the “with skill vs without” test (3 models, 5 topics, blind judges). '
              'The number is the mean score difference on a 1–10 scale; the method’s own noise is 0.70, so anything smaller is not a result.')
            w('- Security: on 2026-11-16 the catalog check covered 45,138 items and 20,101 executable files and found nothing malicious. '
              'It is static analysis and may miss malware written to evade it. Skills with warnings (mostly `curl | sh` installers) are left out.')
        w('')
        w('## Что показал тест' if ru else '## What the test showed')
        w('')
        if ru:
            w('В среднем скилл в системном промпте измеримого выигрыша не дал: −0,20 балла при шуме 0,70. '
              'Сильные модели и без скилла решают такие задачи на 7–9 из 10. Плюс по знаку дали узкие скиллы с нормами — миграции БД, анимация, диагностика багов. '
              'Из двух популярных TDD-скиллов один значимо ухудшал ответы, в списке его нет; второй ломал ответ GPT, у него стоит пометка. Скилл стоит до 10 тыс. токенов на каждый запрос, а ответы с ним длиннее на 15–26 %.')
            w('')
            w('Тест ограничен: скилл целиком в системном промпте, один ход, по 6 ответов на скилл. Процессным скиллам такой формат невыгоден.')
        else:
            w('On average, a skill in the system prompt gave no measurable gain: −0.20 points against 0.70 noise. '
              'Strong models handle these tasks at 7–9 out of 10 without a skill. Narrow skills that encode norms — DB migrations, animation, bug diagnosis — were positive by sign. '
              'Of two popular TDD skills, one made answers significantly worse and is left out; the other broke GPT answers and is marked. A skill costs up to 10k tokens per request; answers with it were 15–26% longer.')
            w('')
            w('Limits: whole skill in the system prompt, single turn, 6 answers per skill. Process-style skills are at a disadvantage in this setup.')
        w('')
        w('## Темы' if ru else '## Topics')
        w('')
        for k, items in by_topic.items():
            label = topics[k]['ru' if ru else 'en']
            anchor = 'topic-' + k
            w(f'- [{label}](#{anchor}) — {len(items)}')
        w('')
        w('## Как ставить' if ru else '## Installing')
        w('')
        if ru:
            w('Команды рассчитаны на Claude Code (`-a claude-code`) и запускаются из папки проекта; нужен Node.js. '
              'Тот же CLI ставит скиллы и другим агентам — список в [vercel-labs/skills](https://github.com/vercel-labs/skills). '
              'Можно не запускать руками: на [странице раздела](' + SITE + '/nevibecode) есть промпт, который ставит скиллы через самого агента.')
        else:
            w('Commands target Claude Code (`-a claude-code`) and run from the project folder; Node.js is required. '
              'The same CLI installs skills for other agents — see [vercel-labs/skills](https://github.com/vercel-labs/skills). '
              'You can also paste the prompt from the [catalog page](' + SITE + '/en/nevibecode) and let the agent install them.')
        w('')
        for k, items in by_topic.items():
            label = topics[k]['ru' if ru else 'en']
            w(f'<a name="topic-{k}"></a>')
            w(f'## {label}')
            w('')
            w(f'Вся тема в каталоге: [{SITE}/nevibecode/topic/{k}]({SITE}/nevibecode/topic/{k})' if ru else
              f'Whole topic in the catalog: [{SITE}/en/nevibecode/topic/{k}]({SITE}/en/nevibecode/topic/{k})')
            w('')
            for it in items:
                card = f'{SITE}{"" if ru else "/en"}/nevibecode/skills/{it["slug"]}'
                lede = clean(it['lede_ru'] if ru else it['lede_en']) or ''
                head = f'- **[{it["name"]}]({card})**'
                w(head + (f' — {lede}' if lede else ''))
                meta = [f'`{it["cmd"]}`']
                if it['source_url']:
                    meta.append(f'[{"исходник" if ru else "source"}: {it["gh_repo"] or "GitHub"}]({it["source_url"]})')
                if it['installs']:
                    meta.append((f'{num_ru(it["installs"])} {plural_ru(it["installs"], "установка", "установки", "установок")}' if ru else f'{num_en(it["installs"])} installs'))
                if it['install_ok']:
                    meta.append(f'ставится ✓ {cdate_ru}' if ru else f'installs ✓ {cdate}')
                if it['ab']:
                    a = it['ab']
                    meta.append(f'A/B {cdate_ru if ru else cdate}: {fmt_delta(a["delta"], ru)} — {a["ru" if ru else "en"]}')
                w('  ' + ' · '.join(meta))
            w('')
        w('## Обновление и лицензия' if ru else '## Updates and license')
        w('')
        if ru:
            w(f'Список собирает `scripts/build.py` из базы каталога; снимок проверок — `{os.path.relpath(checks_file, ROOT)}`. '
              f'Сборка от {date.today().isoformat()}. Число установок — по данным источника, из которого карточка пришла в каталог. '
              'Описания скиллов написаны для каталога affpapa.org. Список и описания — [CC0 1.0](LICENSE). '
              'Сами скиллы — под лицензиями своих авторов, смотрите исходник.')
        else:
            w(f'The list is built by `scripts/build.py` from the catalog database; checks snapshot: `{os.path.relpath(checks_file, ROOT)}`. '
              f'Built on {date.today().isoformat()}. Install counts come from the source the card was imported from. '
              'Descriptions were written for the affpapa.org catalog. The list and descriptions are [CC0 1.0](LICENSE). '
              'Each skill keeps its author’s license — check the source.')
        w('')
        open(os.path.join(ROOT, 'README.md' if ru else 'README.en.md'), 'w', encoding='utf-8').write('\n'.join(L))

    slim = {k: [{f: i[f] for f in ('id', 'slug', 'name', 'cmd', 'source_url', 'installs', 'install_ok')} | {'ab': i['ab']}
                for i in v] for k, v in by_topic.items()}
    json.dump({'built': date.today().isoformat(), 'topics': slim}, open(os.path.join(ROOT, 'data', 'skills.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(f'topics={len(by_topic)} skills={total} install_ok={n_ok} ab={n_ab}', file=sys.stderr)


if __name__ == '__main__':
    main()
