from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

# Repo root (learn-python/)  ← two levels up from website/scripts/
ROOT = Path(__file__).resolve().parent.parent.parent
# VuePress app folder (website/)
WEBSITE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = WEBSITE_DIR / 'docs'
VUEPRESS_DIR = DOCS_DIR / '.vuepress'
PUBLIC_FILES_DIR = VUEPRESS_DIR / 'public' / 'files'
SIDEBAR_FILE = VUEPRESS_DIR / 'sidebar.ts'

README_PATH = ROOT / 'README.md'
CONTRIBUTION_PATH = ROOT / 'CONTRIBUTION.md'
NOTEBOOK_PATH = ROOT / 'learn-python.ipynb'
SOURCE_DOCS_DIR = ROOT / 'docs'
DOCS_README_PATH = DOCS_DIR / 'README.md'
DOCS_CONTRIBUTION_PATH = DOCS_DIR / 'contribution.md'

# Directories inside docs/ that are internal tooling — skip when syncing to VuePress
SKIP_DIRS = {'.vitepress', '.vuepress'}

# ---------------------------------------------------------------------------
# Sidebar structure — mirrors docs/.vitepress/config.ts
# ---------------------------------------------------------------------------
SIDEBAR_STRUCTURE = [
    {
        'text': 'Getting Started',
        'link': '/getting-started/',
    },
    {
        'text': 'I — The Basics',
        'collapsed': False,
        'link': '/01-the-basics/',
        'items': [
            {'text': 'Hello World',       'link': '/01-the-basics/hello-world'},
            {'text': 'Variables',         'link': '/01-the-basics/variables'},
            {'text': 'Built-in Data Types','link': '/01-the-basics/built-in-data-types'},
            {'text': 'String Formatting', 'link': '/01-the-basics/string-formatting'},
            {'text': 'Operators',         'link': '/01-the-basics/operators'},
            {'text': 'Falsy Values',      'link': '/01-the-basics/falsy-values'},
        ],
    },
    {
        'text': 'II — Data Structures',
        'collapsed': False,
        'link': '/02-data-structures/',
        'items': [
            {'text': 'Lists',             'link': '/02-data-structures/lists'},
            {'text': 'Tuples',            'link': '/02-data-structures/tuples'},
            {'text': 'Dictionaries',      'link': '/02-data-structures/dictionaries'},
            {'text': 'Sets',              'link': '/02-data-structures/sets'},
            {'text': 'Collections Module','link': '/02-data-structures/collections-module'},
            {'text': 'Comprehensions',    'link': '/02-data-structures/comprehensions'},
            {'text': 'Type Conversion',   'link': '/02-data-structures/type-conversion'},
        ],
    },
    {
        'text': 'III — Control Flow',
        'collapsed': False,
        'link': '/03-control-flow/',
        'items': [
            {'text': 'If / Else',   'link': '/03-control-flow/if-else'},
            {'text': 'Match / Case','link': '/03-control-flow/match-case'},
            {'text': 'Loops',       'link': '/03-control-flow/loops'},
        ],
    },
    {
        'text': 'IV — Functions',
        'collapsed': False,
        'link': '/04-functions/',
        'items': [
            {'text': 'Defining Functions',     'link': '/04-functions/defining-functions'},
            {'text': 'Parameters & Arguments', 'link': '/04-functions/parameters-arguments'},
            {'text': 'Lambda Functions',       'link': '/04-functions/lambda-functions'},
            {'text': 'Scoping Rules',          'link': '/04-functions/scoping-rules'},
            {'text': 'Type Hints',             'link': '/04-functions/type-hints'},
        ],
    },
    {
        'text': 'V — OOP',
        'collapsed': False,
        'link': '/05-oop/',
        'items': [
            {'text': 'Classes',               'link': '/05-oop/classes'},
            {'text': 'Inheritance',           'link': '/05-oop/inheritance'},
            {'text': 'Abstract Base Classes', 'link': '/05-oop/abstract-base-classes'},
            {'text': 'Magic Methods',         'link': '/05-oop/magic-methods'},
            {'text': 'Dataclasses',           'link': '/05-oop/dataclasses'},
        ],
    },
    {
        'text': 'VI — Advanced Python Techniques',
        'collapsed': False,
        'link': '/06-advanced-python-techniques/',
        'items': [
            {'text': 'Iterators & Generators','link': '/06-advanced-python-techniques/iterators-generators'},
            {'text': 'itertools & functools',  'link': '/06-advanced-python-techniques/itertools-functools'},
            {'text': 'Decorators',            'link': '/06-advanced-python-techniques/decorators'},
            {'text': 'Context Managers',      'link': '/06-advanced-python-techniques/context-managers'},
            {'text': 'Pattern Matching',      'link': '/06-advanced-python-techniques/pattern-matching'},
        ],
    },
    {
        'text': 'VII — Modules & Packaging',
        'collapsed': False,
        'link': '/07-modules/',
        'items': [
            {'text': 'Modules',              'link': '/07-modules/modules'},
            {'text': 'File I/O & JSON',      'link': '/07-modules/file-io-json'},
            {'text': 'Packages',             'link': '/07-modules/packages'},
            {'text': 'Virtual Environments', 'link': '/07-modules/virtual-environments'},
            {'text': 'Useful Commands',      'link': '/07-modules/useful-commands'},
            {'text': 'Build & Packaging',    'link': '/07-modules/build-packaging'},
        ],
    },
    {
        'text': 'VIII — Errors & Exceptions',
        'link': '/08-errors-exceptions/',
    },
    {
        'text': 'IX — Concurrency',
        'collapsed': False,
        'link': '/09-concurrency/',
        'items': [
            {'text': 'The GIL',         'link': '/09-concurrency/the-gil'},
            {'text': 'Async / Await',   'link': '/09-concurrency/async-await'},
            {'text': 'Threading',       'link': '/09-concurrency/threading'},
            {'text': 'Multiprocessing', 'link': '/09-concurrency/multiprocessing'},
            {'text': 'Free-Threading',  'link': '/09-concurrency/free-threading'},
            {'text': 'Decision Matrix', 'link': '/09-concurrency/decision-matrix'},
        ],
    },
    {
        'text': 'Appendix',
        'collapsed': False,
        'link': '/appendix/',
        'items': [
            {'text': 'AI & Data Science', 'link': '/appendix/ai-data-science'},
            {'text': 'Web Development',   'link': '/appendix/web-development'},
        ],
    },
]



# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def to_ts(value: object, indent: int = 0) -> str:
    space = '  ' * indent
    next_space = '  ' * (indent + 1)

    if isinstance(value, dict):
        lines = ['{']
        for key, val in value.items():
            lines.append(f"{next_space}{key}: {to_ts(val, indent + 1)},")
        lines.append(f'{space}}}')
        return '\n'.join(lines)

    if isinstance(value, list):
        if not value:
            return '[]'
        lines = ['[']
        for item in value:
            rendered = to_ts(item, indent + 1)
            lines.append(f'{next_space}{rendered},')
        lines.append(f'{space}]')
        return '\n'.join(lines)

    return json.dumps(value, ensure_ascii=False)


def _doc_rel_from_sidebar_link(link: str) -> str:
    normalized = link.strip('/')
    if not normalized:
        raise ValueError('Sidebar link cannot be empty')
    if link.endswith('/'):
        return f'{normalized}/index.md'
    return f'{normalized}.md'


def _first_heading_text(path: Path) -> str | None:
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.startswith('# '):
            return line[2:].strip()
    return None


def _anchor_id(text: str) -> str:
    slug = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
    return slug or 'section'


def _anchor_for_doc(rel_path: str) -> str | None:
    path = SOURCE_DOCS_DIR / rel_path
    if not path.exists():
        return None
    heading = _first_heading_text(path)
    if not heading:
        return None
    return _anchor_id(heading)


def _inject_anchor(md_text: str, anchor: str | None) -> str:
    if not anchor:
        return md_text
    return f'<a id="{anchor}"></a>\n\n{md_text}'


# ---------------------------------------------------------------------------
# Sync steps
# ---------------------------------------------------------------------------

def sync_chapter_dirs() -> None:
    """Copy every chapter folder from docs/ into website/docs/, skipping tooling dirs."""
    for src in sorted(SOURCE_DOCS_DIR.iterdir()):
        if not src.is_dir() or src.name in SKIP_DIRS or src.name.startswith('.'):
            continue
        dst = DOCS_DIR / src.name
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print(f'  synced {src.name}/')

    # Write the site home from docs/index.md
    src_index = SOURCE_DOCS_DIR / 'index.md'
    if src_index.exists():
        content = src_index.read_text(encoding='utf-8')
        DOCS_README_PATH.write_text(
            '---\ntitle: Learn Python\n---\n\n' + content,
            encoding='utf-8',
        )
        print('  wrote README.md (home page)')


def write_contribution() -> None:
    contribution = CONTRIBUTION_PATH.read_text(encoding='utf-8')
    DOCS_CONTRIBUTION_PATH.write_text(
        '---\ntitle: Contribution\n---\n\n' + contribution,
        encoding='utf-8',
    )


def copy_notebook() -> None:
    PUBLIC_FILES_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(NOTEBOOK_PATH, PUBLIC_FILES_DIR / NOTEBOOK_PATH.name)


# Ordered list of doc files to concatenate for the root README.md
README_DOCS_ORDER = [
    'getting-started/index.md',
    '01-the-basics/index.md',
    '01-the-basics/hello-world.md',
    '01-the-basics/variables.md',
    '01-the-basics/built-in-data-types.md',
    '01-the-basics/string-formatting.md',
    '01-the-basics/operators.md',
    '01-the-basics/falsy-values.md',
    '02-data-structures/index.md',
    '02-data-structures/lists.md',
    '02-data-structures/tuples.md',
    '02-data-structures/dictionaries.md',
    '02-data-structures/sets.md',
    '02-data-structures/collections-module.md',
    '02-data-structures/comprehensions.md',
    '02-data-structures/type-conversion.md',
    '03-control-flow/index.md',
    '03-control-flow/if-else.md',
    '03-control-flow/match-case.md',
    '03-control-flow/loops.md',
    '04-functions/index.md',
    '04-functions/defining-functions.md',
    '04-functions/parameters-arguments.md',
    '04-functions/lambda-functions.md',
    '04-functions/scoping-rules.md',
    '04-functions/type-hints.md',
    '05-oop/index.md',
    '05-oop/classes.md',
    '05-oop/inheritance.md',
    '05-oop/abstract-base-classes.md',
    '05-oop/magic-methods.md',
    '05-oop/dataclasses.md',
    '06-advanced-python-techniques/index.md',
    '06-advanced-python-techniques/iterators-generators.md',
    '06-advanced-python-techniques/itertools-functools.md',
    '06-advanced-python-techniques/decorators.md',
    '06-advanced-python-techniques/context-managers.md',
    '06-advanced-python-techniques/pattern-matching.md',
    '07-modules/index.md',
    '07-modules/modules.md',
    '07-modules/file-io-json.md',
    '07-modules/packages.md',
    '07-modules/virtual-environments.md',
    '07-modules/useful-commands.md',
    '07-modules/build-packaging.md',
    '08-errors-exceptions/index.md',
    '09-concurrency/index.md',
    '09-concurrency/the-gil.md',
    '09-concurrency/async-await.md',
    '09-concurrency/threading.md',
    '09-concurrency/multiprocessing.md',
    '09-concurrency/free-threading.md',
    '09-concurrency/decision-matrix.md',
    'appendix/index.md',
    'appendix/ai-data-science.md',
    'appendix/web-development.md',
]

def build_course_toc() -> str:
    lines = ['## Table of Contents', '']
    for section in SIDEBAR_STRUCTURE:
        section_rel = _doc_rel_from_sidebar_link(section['link'])
        section_anchor = _anchor_for_doc(section_rel)
        if section_anchor:
            lines.append(f"- [{section['text']}](#{section_anchor})")
        else:
            lines.append(f"- {section['text']}")
        for item in section.get('items', []):
            item_rel = _doc_rel_from_sidebar_link(item['link'])
            item_anchor = _anchor_for_doc(item_rel)
            if item_anchor:
                lines.append(f"  - [{item['text']}](#{item_anchor})")
            else:
                lines.append(f"  - {item['text']}")
    return '\n'.join(lines)


README_HEADER = """\
# Learn Python

> Learn Python from scratch with short lessons, clear explanations, and runnable examples.

- :page_facing_up: **Documentation site** — the full content is published at **[learn-python-dev.netlify.app](https://learn-python-dev.netlify.app/)** with a sidebar, search, and per-chapter navigation.

- :notebook: **Interactive notebook** — [learn-python.ipynb](learn-python.ipynb) in VS Code lets you run and edit every code block inline.

> [!NOTE]
> After editing any file in `docs/`, run this to update the website content:
> ```bash
> python website/scripts/sync_docs.py
> ```

{toc}

---

"""


def _bump_headings(text: str) -> str:
    """Shift all headings down one level (# → ##, ## → ###, etc.)."""
    lines = []
    for line in text.splitlines(keepends=True):
        if line.startswith('#'):
            line = '#' + line
        lines.append(line)
    return ''.join(lines)


def write_root_readme() -> None:
    """Regenerate the root README.md from docs/ files in sidebar order."""
    parts = [README_HEADER.format(toc=build_course_toc())]
    for rel in README_DOCS_ORDER:
        path = SOURCE_DOCS_DIR / rel
        if not path.exists():
            continue
        content = _bump_headings(path.read_text(encoding='utf-8').strip())
        content = _inject_anchor(content, _anchor_for_doc(rel))
        parts.append(content + '\n\n---\n\n')
    README_PATH.write_text(''.join(parts), encoding='utf-8')
    print('  wrote root README.md')


def _parse_md_to_cells(md_text: str) -> list[dict]:
    """Split a markdown file into alternating text/code sections."""
    cells: list[dict] = []
    current_text: list[str] = []
    current_code: list[str] = []
    in_code = False
    code_lang = ''

    for line in md_text.split('\n'):
        if not in_code:
            m = re.match(r'^```(\w*)', line)
            if m:
                text = '\n'.join(current_text).strip()
                if text:
                    cells.append({'type': 'markdown', 'source': text})
                current_text = []
                in_code = True
                code_lang = m.group(1)
                current_code = []
            else:
                current_text.append(line)
        else:
            if line.strip() == '```':
                code = '\n'.join(current_code)
                if code_lang == 'python' and code.strip():
                    cells.append({'type': 'code', 'source': code})
                in_code = False
                current_code = []
                code_lang = ''
            else:
                current_code.append(line)

    text = '\n'.join(current_text).strip()
    if text:
        cells.append({'type': 'markdown', 'source': text})
    return cells


def _nb_cell(cell_type: str, source: str) -> dict:
    lines = source.splitlines(keepends=True)
    # ensure last line has no trailing newline
    if lines and lines[-1].endswith('\n'):
        lines[-1] = lines[-1][:-1]
    if cell_type == 'markdown':
        return {'cell_type': 'markdown', 'metadata': {}, 'source': lines}
    return {
        'cell_type': 'code',
        'execution_count': None,
        'metadata': {},
        'outputs': [],
        'source': lines,
    }


def write_notebook() -> None:
    """Regenerate learn-python.ipynb from docs/ files in sidebar order."""
    cells = [
        _nb_cell('markdown', (
            '# Learn Python\n\n'
            '> 💡 Learn Python from scratch with short lessons, clear explanations, and runnable examples.\n\n'
            '- :page_facing_up: **Documentation site** — the full content is published at **[learn-python-dev.netlify.app](https://learn-python-dev.netlify.app/)** with a sidebar, search, and per-chapter navigation.\n\n'
            '- :notebook: **Interactive notebook** — [learn-python.ipynb](learn-python.ipynb) in VS Code lets you run and edit every code block inline.\n\n'
            '> [!NOTE]\n'
            '> After editing any file in `docs/`, run `python website/scripts/sync_docs.py` to regenerate this notebook.'
        )),
        _nb_cell('markdown', build_course_toc()),
    ]

    for rel in README_DOCS_ORDER:
        path = SOURCE_DOCS_DIR / rel
        if not path.exists():
            continue
        md_text = _inject_anchor(path.read_text(encoding='utf-8'), _anchor_for_doc(rel))
        for c in _parse_md_to_cells(md_text):
            cells.append(_nb_cell(c['type'], c['source']))

    notebook = {
        'cells': cells,
        'metadata': {
            'kernelspec': {
                'display_name': 'Python 3',
                'language': 'python',
                'name': 'python3',
            },
            'language_info': {
                'name': 'python',
                'version': '3.13.0',
            },
        },
        'nbformat': 4,
        'nbformat_minor': 5,
    }
    NOTEBOOK_PATH.write_text(
        json.dumps(notebook, indent=1, ensure_ascii=False),
        encoding='utf-8',
    )
    print('  wrote learn-python.ipynb')


def write_sidebar_file() -> None:
    contribution_sidebar = [
        {'text': 'Contribution', 'link': '/contribution/'},
        {'text': 'Course Home',  'link': '/'},
    ]

    content = (
        '// This file is auto-generated by scripts/sync_docs.py.\n'
        '// Do not edit it manually.\n\n'
        f'export const courseSidebar = {to_ts(SIDEBAR_STRUCTURE)};\n\n'
        f'export const contributionSidebar = {to_ts(contribution_sidebar)};\n'
    )
    SIDEBAR_FILE.write_text(content, encoding='utf-8')


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    DOCS_DIR.mkdir(exist_ok=True)
    print('Syncing docs/ → website/docs/ ...')
    sync_chapter_dirs()
    write_contribution()
    write_sidebar_file()
    write_root_readme()
    write_notebook()
    copy_notebook()
    print('Done.')


