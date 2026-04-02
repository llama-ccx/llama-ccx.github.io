# Llama Docs Maintenance Guide

This repository contains the documentation website for Llama, built with MkDocs + Material.

## Quick Start

Run all commands from the repository root:

```bash
cd /Users/mp/Documents/GitHub/Llama/llama-ccx.github.io
```

Install dependencies (if needed):

```bash
pip install mkdocs-material
```

Serve locally:

```bash
mkdocs serve -f mkdocs.yml
```

Build static site:

```bash
mkdocs build -f mkdocs.yml
```

## Important Configuration (Do Not Forget)

The MkDocs config is now at repository root:

- `mkdocs.yml`
- `docs_dir: docs`
- `site_dir: site`

## Navigation + Cards Autogeneration

A build hook auto-generates section index pages and section nav items:

- Hook file: `docs/scripts/autogen_sections.py`
- Enabled in: `mkdocs.yml` (`hooks:`)

### What is auto-generated

At build/serve time, these index pages are rewritten:

- `docs/basics/index.md`
- `docs/examples/index.md`
- `docs/references/index.md`

Each page gets one card per markdown file in its folder.

### What this means in practice

If you add:

- `docs/examples/new-topic.md`

it will automatically appear:

- as a card in `Examples`
- as an item in the `Examples` navigation section

## Content Rules to Remember

- Put normal docs pages under `docs/`.
- Keep section content in folder-based structure:
  - `docs/basics/*.md`
  - `docs/examples/*.md`
  - `docs/references/*.md`
- Avoid manual edits to generated section index pages if you expect persistence; the hook rewrites them.

## Styling and UI Customization

Main custom stylesheet:

- `docs/stylesheets/extra.css`

Custom JS (header title clickable):

- `docs/javascripts/header-clickable-title.js`

Configured in:

- `mkdocs.yml` (`extra_css`, `extra_javascript`)

## Deployment

GitHub Actions workflow:

- `.github/workflows/deploy-docs.yml`

Current behavior:

- Triggers on push to `main` for `docs/**` and `mkdocs.yml`
- Runs `mkdocs gh-deploy --force -f mkdocs.yml`

## One-Year Reminder Checklist

When you come back after a long time, verify these first:

1. `mkdocs.yml` still lives at repo root.
2. `docs/scripts/autogen_sections.py` is still referenced under `hooks:`.
3. Build succeeds with `mkdocs build -f mkdocs.yml`.
4. Deploy workflow still points to `-f mkdocs.yml`.
5. New files in `docs/examples/` appear automatically as cards.

If all five checks pass, the docs system is healthy.
