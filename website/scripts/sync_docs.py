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
DOCS_README_PATH = DOCS_DIR / 'README.md'
DOCS_CONTRIBUTION_PATH = DOCS_DIR / 'contribution.md'

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*)$')
FENCE_RE = re.compile(r'^(```|~~~)')
TOC_EXCLUDE = {'Learn Python', 'Table of Contents'}
MAX_SIDEBAR_LEVEL = 3
COLLAPSIBLE_TOP_LEVEL = {
    'Getting Started',
    'Chapter I: Core Python',
    'Chapter II: Advanced Features',
    'Chapter III: Concurrency',
    'Appendix',
}


def slugify(text: str, used: dict[str, int]) -> str:
    slug = text.strip().lower()
    slug = re.sub(r'\s+', '-', slug)
    slug = re.sub(r'[^\w\-]', '', slug)
    slug = slug.strip('-')
    if not slug:
        slug = 'section'

    count = used.get(slug, 0)
    used[slug] = count + 1
    if count:
        return f'{slug}-{count}'
    return slug


def extract_headings(markdown: str) -> list[dict[str, object]]:
    headings: list[dict[str, object]] = []
    used_slugs: dict[str, int] = {}
    in_fence = False

    for line in markdown.splitlines():
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        match = HEADING_RE.match(line)
        if not match:
            continue

        level = len(match.group(1))
        text = match.group(2).strip()
        text = re.sub(r'\s+#.*$', '', text).strip()
        text = re.sub(r'`([^`]*)`', r'\1', text)
        text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
        text = re.sub(r'[*_~]', '', text).strip()

        slug = slugify(text, used_slugs)
        headings.append({
            'level': level,
            'text': text,
            'slug': slug,
        })

    return headings


def build_sidebar_items(headings: list[dict[str, object]]) -> list[dict[str, object]]:
    sidebar: list[dict[str, object]] = [
        {
            'text': 'Course Home',
            'link': '/',
        }
    ]

    stack: list[tuple[int, dict[str, object]]] = []

    for heading in headings:
        level = int(heading['level'])
        text = str(heading['text'])
        slug = str(heading['slug'])

        if text in TOC_EXCLUDE or level > MAX_SIDEBAR_LEVEL:
            continue

        item: dict[str, object] = {
            'text': text,
            'link': f'/#{slug}',
        }

        while stack and stack[-1][0] >= level:
            stack.pop()

        if not stack:
            if level == 1:
                item['items'] = []
            sidebar.append(item)
            stack.append((level, item))
            continue

        parent = stack[-1][1]
        parent_items = parent.setdefault('items', [])
        if not isinstance(parent_items, list):
            parent_items = []
            parent['items'] = parent_items

        if level < MAX_SIDEBAR_LEVEL:
            item['items'] = []
        parent_items.append(item)
        stack.append((level, item))

    def prune(items: list[dict[str, object]]) -> list[dict[str, object]]:
        for item in items:
            children = item.get('items')
            if isinstance(children, list):
                prune(children)
                if not children:
                    item.pop('items', None)
                item.pop('collapsed', None)

        for item in items:
            children = item.get('items')
            if isinstance(children, list) and item.get('text') in COLLAPSIBLE_TOP_LEVEL:
                item['collapsed'] = False
        return items

    return prune(sidebar)


def write_markdown_docs() -> None:
    DOCS_DIR.mkdir(exist_ok=True)
    PUBLIC_FILES_DIR.mkdir(parents=True, exist_ok=True)

    readme = README_PATH.read_text(encoding='utf-8')
    readme = readme.replace('(learn-python.ipynb)', '(/files/learn-python.ipynb)')
    readme = readme.replace('(./CONTRIBUTION.md)', '(/contribution/)')
    DOCS_README_PATH.write_text('---\ntitle: Learn Python\n---\n\n' + readme, encoding='utf-8')

    contribution = CONTRIBUTION_PATH.read_text(encoding='utf-8')
    DOCS_CONTRIBUTION_PATH.write_text('---\ntitle: Contribution\n---\n\n' + contribution, encoding='utf-8')

    shutil.copy2(NOTEBOOK_PATH, PUBLIC_FILES_DIR / NOTEBOOK_PATH.name)


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


def write_sidebar_file() -> None:
    headings = extract_headings(README_PATH.read_text(encoding='utf-8'))
    course_sidebar = build_sidebar_items(headings)
    contribution_sidebar = [
        {'text': 'Contribution', 'link': '/contribution/'},
        {'text': 'Course Home', 'link': '/'},
    ]

    content = (
        '// This file is auto-generated by scripts/sync_docs.py.\n'
        '// Do not edit it manually.\n\n'
        f'export const courseSidebar = {to_ts(course_sidebar)}\n\n'
        f'export const contributionSidebar = {to_ts(contribution_sidebar)}\n'
    )
    SIDEBAR_FILE.write_text(content, encoding='utf-8')


if __name__ == '__main__':
    write_markdown_docs()
    write_sidebar_file()

