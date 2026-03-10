# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Souls is a bilingual (Chinese/English) static website serving as an AI persona library — 332+ historical figures, fictional characters, and expert personas. Each "soul" is a SOUL.md prompt file. Site: https://agent-souls.com

## Build & Development Commands

```bash
# Install dependencies
bundle install

# Generate Jekyll pages from SOUL.md source files (required before build)
python3 scripts/generate_soul_pages.py

# Build static site
bundle exec jekyll build --baseurl ""

# Local dev server (http://localhost:4000)
bundle exec jekyll serve

# Run tests
python3 -m pytest tests/ -v

# Run a single test class
python3 -m pytest tests/test_generate_soul_pages.py::SiteBuildSeoRegressionTest -v
```

## Architecture

**Three-layer pipeline: Source → Generation → Static Site**

1. **Source content** lives in category folders (`real_world/`, `virtual_world/`, `personas/`), each soul in its own subfolder:
   ```
   real_world/confucius/
   ├── SOUL.md        # Chinese prompt
   ├── SOUL.en.md     # English prompt
   └── README.md      # Metadata (English name, Wikipedia links)
   ```

2. **`scripts/generate_soul_pages.py`** reads source folders and generates Jekyll-compatible `.md` entry pages (e.g., `real_world/confucius.md`) with YAML front matter. These generated pages are gitignored.

3. **Jekyll** renders the generated pages using layouts in `_layouts/` (soul.html for detail pages, home.html for index) into `_site/`.

## Key Conventions

- **Bilingual-first**: Every soul needs both `SOUL.md` (Chinese) and `SOUL.en.md` (English). Templates use `data-i18n` attributes; `assets/js/i18n.js` handles language switching.
- **Generated files are gitignored**: `/{real_world,virtual_world,personas}/*.md` entry pages are generated, not committed. Only the source folders with SOUL.md files are tracked.
- **Deployment**: Push to `shipped` branch triggers GitHub Actions (`.github/workflows/deploy.yml`) which runs generation → Jekyll build → GitHub Pages deploy.
- **SEO**: JSON-LD structured data (`_includes/json_ld.html`), jekyll-seo-tag plugin, dynamic OpenGraph images via Robohash.

## Adding a New Soul

1. Create folder: `{category}/{slug}/`
2. Write `SOUL.md` (Chinese), `SOUL.en.md` (English), `README.md` (metadata)
3. Run `python3 scripts/generate_soul_pages.py` to generate the entry page
4. Update `stats` counts in `_config.yml`

## Tech Stack

- **Static site generator**: Jekyll 4.3+ (Ruby)
- **Content pipeline**: Python 3
- **Frontend**: Vanilla JS, SCSS (no framework)
- **Tests**: pytest
