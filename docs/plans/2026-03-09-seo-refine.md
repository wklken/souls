# SEO Refine Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement the high-impact sitewide SEO fixes from `seo-01.md` and `seo-02.md` for the Jekyll site without changing the content model of the soul entries.

**Architecture:** Keep SEO logic centralized in Jekyll front matter, the default layout, and shared includes. Use the page generator for soul-detail metadata, page front matter for homepage/category metadata, and build-output regression tests to verify the rendered HTML, sitemap, and robots behavior.

**Tech Stack:** Jekyll, Liquid templates, `jekyll-seo-tag`, Python `unittest`, `scripts/generate_soul_pages.py`

---

### Task 1: Add failing SEO regression coverage

**Files:**
- Modify: `tests/test_generate_soul_pages.py`

**Step 1: Write the failing tests**

Add build-output tests that assert:
- the rendered homepage has exactly one `<title>` and it is not `Souls - Souls`
- homepage/category/detail pages render page-specific descriptions
- category pages render pretty URLs instead of `.html` canonicals
- the sitemap excludes `_layouts/` and `_includes/`
- `robots.txt` contains explicit crawler rules and the sitemap URL

**Step 2: Run the targeted tests to verify they fail**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_generate_soul_pages.SiteBuildSeoRegressionTest -v`
Expected: FAIL on duplicate titles, generic metadata, sitemap pollution, and robots output.

### Task 2: Implement centralized SEO metadata

**Files:**
- Modify: `_config.yml`
- Modify: `_layouts/default.html`
- Modify: `_includes/json_ld.html`
- Modify: `index.md`
- Modify: `real_world.md`
- Modify: `virtual_world.md`
- Modify: `personas.md`
- Create: `robots.txt`

**Step 1: Fix site defaults and metadata sources**

Set the site language/locale defaults to Chinese for the source HTML, stop publishing underscored include/layout folders, and add reusable site-level SEO strings.

**Step 2: Fix layout-level SEO rendering**

Remove the duplicate manual `<title>`, keep `jekyll-seo-tag` as the canonical metadata renderer, and expose page SEO titles to the client-side language switcher through data attributes.

**Step 3: Add page-specific metadata**

Add explicit SEO titles, descriptions, images, and pretty permalinks for the homepage and category pages. Add a real `robots.txt` source file with allow/disallow rules and the sitemap entry.

**Step 4: Tighten schema output**

Ensure the JSON-LD include avoids empty `sameAs` values and adds a generic creative-work schema for all soul pages alongside the existing breadcrumb/profile data.

### Task 3: Align generated soul pages with the SEO templates

**Files:**
- Modify: `scripts/generate_soul_pages.py`

**Step 1: Write minimal generator changes**

Emit any missing SEO front-matter fields that the templates need, while preserving existing description/image generation.

**Step 2: Regenerate pages**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 scripts/generate_soul_pages.py`
Expected: 212 generated pages with updated front matter.

### Task 4: Verify the full deploy path

**Files:**
- Verify: `_site/index.html`
- Verify: `_site/real_world/index.html`
- Verify: `_site/real_world/zhuge_liang/index.html`
- Verify: `_site/sitemap.xml`
- Verify: `_site/robots.txt`

**Step 1: Run the targeted tests**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests/test_generate_soul_pages.py`
Expected: PASS

**Step 2: Run the deploy-equivalent build**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 scripts/generate_soul_pages.py && JEKYLL_ENV=production bundle exec jekyll build --baseurl ""`
Expected: build succeeds and the rendered files match the new SEO assertions.
