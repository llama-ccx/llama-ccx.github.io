from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Dict, List, Tuple


SECTION_CONFIG: Dict[str, str] = {
    "basics": "Core concepts and components to build, solve, and inspect models in Llama.",
    "examples": "Choose an example workflow:",
    "references": "Reference material for solver details, licensing, and purchase.",
}


@dataclass
class PageInfo:
    title: str
    description: str
    rel_path: str


def _humanize(stem: str) -> str:
    return stem.replace("-", " ").replace("_", " ").strip().title()


def _extract_title_and_description(md_path: Path) -> Tuple[str, str]:
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    title = _humanize(md_path.stem)
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# "):
            title = stripped[2:].strip()
            break

    description = "Open this page to view details."
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        if stripped.startswith(("-", "*", ">", "!!!", "```", "1.", "2.", "3.")):
            continue

        stripped = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", stripped)
        description = stripped
        break

    if len(description) > 120:
        description = description[:117].rstrip() + "..."

    return title, description


def _discover_section_pages(docs_dir: Path, section_name: str) -> List[PageInfo]:
    section_dir = docs_dir / section_name
    if not section_dir.exists():
        return []

    pages: List[PageInfo] = []
    for md_path in sorted(section_dir.glob("*.md")):
        if md_path.name.lower() == "index.md":
            continue

        title, description = _extract_title_and_description(md_path)
        rel_path = f"{section_name}/{md_path.name}"
        pages.append(PageInfo(title=title, description=description, rel_path=rel_path))

    return pages


def _write_section_index(docs_dir: Path, section_name: str, intro: str, pages: List[PageInfo]) -> None:
    section_title = _humanize(section_name)
    lines = [f"# {section_title}", "", intro, "", '<div class="category-grid">', ""]

    for page in pages:
        href = Path(page.rel_path).name.replace(".md", "/")
        lines.extend(
            [
                f'<a class="category-card" href="{href}">',
                f'  <div class="category-card__title">{page.title}</div>',
                f'  <div class="category-card__desc">{page.description}</div>',
                "</a>",
                "",
            ]
        )

    lines.append("</div>")
    lines.append("")

    (docs_dir / section_name / "index.md").write_text("\n".join(lines), encoding="utf-8")


def _build_section_nav(section_name: str, pages: List[PageInfo]) -> List[object]:
    children: List[object] = [f"{section_name}/index.md"]
    for page in pages:
        children.append({page.title: page.rel_path})
    return children


def on_config(config, **kwargs):
    docs_dir = Path(config["docs_dir"]).resolve()

    section_pages: Dict[str, List[PageInfo]] = {}
    for section_name, intro in SECTION_CONFIG.items():
        pages = _discover_section_pages(docs_dir, section_name)
        section_pages[section_name] = pages
        _write_section_index(docs_dir, section_name, intro, pages)

    nav = config.get("nav")
    if isinstance(nav, list):
        for item in nav:
            if not isinstance(item, dict):
                continue
            for key in list(item.keys()):
                section_key = key.lower()
                if section_key in section_pages:
                    item[key] = _build_section_nav(section_key, section_pages[section_key])

    return config