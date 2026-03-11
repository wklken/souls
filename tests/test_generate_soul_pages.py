import importlib.util
import os
import re
import subprocess
import tempfile
import unittest
from pathlib import Path


def load_module():
    module_path = Path(__file__).resolve().parents[1] / "scripts" / "generate_soul_pages.py"
    spec = importlib.util.spec_from_file_location("generate_soul_pages", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class GenerateSoulPagesBilingualTest(unittest.TestCase):
    def setUp(self):
        self.module = load_module()
        self.tmpdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tmpdir.name)

        persona_dir = self.root / "personas" / "er_doctor"
        persona_dir.mkdir(parents=True)
        persona_dir.joinpath("SOUL.md").write_text(
            "# 急诊室医生\n\n中文内容。\n\n## 标签\ncategory: 专家角色 tags: 医疗, 急诊\n",
            encoding="utf-8",
        )
        persona_dir.joinpath("SOUL.en.md").write_text(
            "# ER Doctor\n\nEnglish content.\n\n## Tags\ncategory: Expert Persona tags: medicine, emergency\n",
            encoding="utf-8",
        )
        persona_dir.joinpath("README.md").write_text(
            "# 急诊室医生\n\n## 基本信息\n- **英文名**: ER Doctor\n",
            encoding="utf-8",
        )

        self.previous_root = self.module.ROOT
        self.module.ROOT = self.root

    def tearDown(self):
        self.module.ROOT = self.previous_root
        self.tmpdir.cleanup()

    def test_generated_page_references_zh_and_en_sources(self):
        created = self.module.generate_for_category("personas", "专家角色")
        self.assertEqual(created, 1)

        page = (self.root / "personas" / "er_doctor.md").read_text(encoding="utf-8")
        self.assertIn('title_zh: "急诊室医生"', page)
        self.assertIn('title_en: "ER Doctor"', page)
        self.assertIn('category_name_zh: "专家角色"', page)
        self.assertIn('category_name_en: "Personas"', page)
        self.assertIn('  - "医疗"', page)
        self.assertIn('  - "急诊"', page)
        self.assertIn('  - "medicine"', page)
        self.assertIn('  - "emergency"', page)
        self.assertIn('{% include_relative er_doctor/SOUL.md %}', page)
        self.assertIn('{% include_relative er_doctor/SOUL.en.md %}', page)
        self.assertIn('download_url_en: "/personas/er_doctor/SOUL.en.md"', page)
        self.assertIn(
            'edit_url_en: "https://github.com/wklken/souls/edit/master/personas/er_doctor/SOUL.en.md"',
            page,
        )

    def test_generated_page_contains_seo_description_and_image_metadata(self):
        self.module.generate_for_category("personas", "专家角色")
        page = (self.root / "personas" / "er_doctor.md").read_text(encoding="utf-8")

        self.assertIn('description: "中文内容。"', page)
        self.assertIn('description_zh: "中文内容。"', page)
        self.assertIn('description_en: "English content."', page)
        self.assertIn(
            'image: "https://robohash.org/souls-personas-er_doctor.png?size=1200x630&set=set4&bgset=bg1"',
            page,
        )


class PersonaReadmeNameLocalizationRegressionTest(unittest.TestCase):
    def setUp(self):
        self.module = load_module()
        self.tmpdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tmpdir.name)

        persona_dir = self.root / "personas" / "translation_consultant"
        persona_dir.mkdir(parents=True)
        persona_dir.joinpath("SOUL.md").write_text(
            "# 翻译顾问 (Translation Consultant)\n\n中文内容。\n", encoding="utf-8"
        )
        persona_dir.joinpath("SOUL.en.md").write_text(
            "# Translation Consultant (翻译顾问)\n\nEnglish content.\n", encoding="utf-8"
        )
        persona_dir.joinpath("README.md").write_text(
            (
                "# 翻译顾问\n\n"
                "## 基本信息\n"
                "- **中文名**: 翻译顾问\n"
                "- **英文名**: Translation Consultant\n"
            ),
            encoding="utf-8",
        )

        self.previous_root = self.module.ROOT
        self.module.ROOT = self.root

    def tearDown(self):
        self.module.ROOT = self.previous_root
        self.tmpdir.cleanup()

    def test_generated_titles_prefer_readme_names_over_bilingual_headings(self):
        created = self.module.generate_for_category("personas", "专家角色")
        self.assertEqual(created, 1)

        page = (self.root / "personas" / "translation_consultant.md").read_text(encoding="utf-8")
        self.assertIn('title_zh: "翻译顾问"', page)
        self.assertIn('title_en: "Translation Consultant"', page)
        self.assertIn('english_name: "Translation Consultant"', page)
        self.assertNotIn('title_zh: "翻译顾问 (Translation Consultant)"', page)
        self.assertNotIn('title_en: "Translation Consultant (翻译顾问)"', page)


class SiteTemplateLocalizationRegressionTest(unittest.TestCase):
    def setUp(self):
        self.repo_root = Path(__file__).resolve().parents[1]

    def test_search_template_has_bilingual_fields(self):
        template = (self.repo_root / "search.json").read_text(encoding="utf-8")
        self.assertIn('"name_zh"', template)
        self.assertIn('"name_en"', template)
        self.assertIn('"category_zh"', template)
        self.assertIn('"category_en"', template)
        self.assertIn('"tags_zh"', template)
        self.assertIn('"tags_en"', template)

    def test_home_stats_use_dynamic_directory_counts(self):
        home_layout = (self.repo_root / "_layouts" / "home.html").read_text(encoding="utf-8")
        self.assertIn("site.static_files", home_layout)
        self.assertIn("file.name == 'SOUL.md'", home_layout)
        self.assertIn("file.path contains '/real_world/'", home_layout)
        self.assertIn("file.path contains '/virtual_world/'", home_layout)
        self.assertIn("file.path contains '/personas/'", home_layout)
        self.assertIn('data-count="{{ total_count }}"', home_layout)
        self.assertIn('data-count="{{ real_world_count }}"', home_layout)
        self.assertIn('data-count="{{ virtual_world_count }}"', home_layout)
        self.assertIn('data-count="{{ personas_count }}"', home_layout)
        self.assertNotIn("site.stats.total", home_layout)

    def test_default_layout_includes_json_ld(self):
        default_layout = (self.repo_root / "_layouts" / "default.html").read_text(encoding="utf-8")
        self.assertIn("{% include json_ld.html %}", default_layout)

    def test_json_ld_include_contains_required_schema_types(self):
        json_ld_include = (self.repo_root / "_includes" / "json_ld.html").read_text(encoding="utf-8")
        self.assertIn("SearchAction", json_ld_include)
        self.assertIn("BreadcrumbList", json_ld_include)
        self.assertIn("ProfilePage", json_ld_include)
        self.assertIn('"@type": "Person"', json_ld_include)

    def test_soul_layout_contains_related_souls_section(self):
        soul_layout = (self.repo_root / "_layouts" / "soul.html").read_text(encoding="utf-8")
        self.assertIn('class="related-souls"', soul_layout)
        self.assertIn('data-i18n="soul.related"', soul_layout)

    def test_category_pages_include_local_search_bar(self):
        include = (self.repo_root / "_includes" / "category_search.html").read_text(encoding="utf-8")
        self.assertIn('id="category-search-input"', include)
        self.assertIn("data-search-input", include)
        self.assertIn("/assets/js/category-search.js", include)

        for page_name in ("real_world.md", "virtual_world.md", "personas.md"):
            page = (self.repo_root / page_name).read_text(encoding="utf-8")
            self.assertIn("{% include category_search.html %}", page)
            self.assertNotIn("{% include search.html %}", page)

    def test_i18n_updates_all_search_input_placeholders(self):
        i18n_script = (self.repo_root / "assets" / "js" / "i18n.js").read_text(encoding="utf-8")
        self.assertIn("querySelectorAll('[data-search-input]')", i18n_script)

    def test_category_cards_use_single_localized_title_without_subtitle(self):
        for page_name in ("real_world.md", "virtual_world.md", "personas.md"):
            page = (self.repo_root / page_name).read_text(encoding="utf-8")
            self.assertIn('class="soul-name"', page)
            self.assertIn('data-localized-en="{{ soul_name_en | escape }}"', page)
            self.assertNotIn('class="soul-english"', page)

    def test_soul_layout_removes_secondary_name_lines(self):
        soul_layout = (self.repo_root / "_layouts" / "soul.html").read_text(encoding="utf-8")
        self.assertNotIn('class="english-name"', soul_layout)
        self.assertNotIn('class="related-soul-english"', soul_layout)

    def test_soul_styles_hide_duplicate_heading_in_content(self):
        style = (self.repo_root / "assets" / "css" / "style.scss").read_text(encoding="utf-8")
        self.assertIn("> h1:first-child {", style)

    def test_team_download_config_exports_single_language_fields(self):
        team_layout = (self.repo_root / "_layouts" / "team.html").read_text(encoding="utf-8")

        self.assertIn("const activeLang =", team_layout)
        self.assertIn("const pickLocalized =", team_layout)
        self.assertIn("team_name: pickLocalized(", team_layout)
        self.assertIn("team_description: pickLocalized(", team_layout)
        self.assertIn("name: pickLocalized(", team_layout)
        self.assertIn("description: pickLocalized(", team_layout)
        self.assertNotIn("team_name: {", team_layout)
        self.assertNotIn("team_description: {", team_layout)
        self.assertNotIn("name: {", team_layout)
        self.assertNotIn("description: {", team_layout)

    def test_teams_pages_use_single_localized_titles_without_subtitles(self):
        teams_page = (self.repo_root / "teams.md").read_text(encoding="utf-8")
        team_layout = (self.repo_root / "_layouts" / "team.html").read_text(encoding="utf-8")

        self.assertIn('class="team-name"', teams_page)
        self.assertIn('data-localized-en="{{ team_name_en | escape }}"', teams_page)
        self.assertNotIn('class="team-english"', teams_page)

        self.assertIn('class="member-name"', team_layout)
        self.assertIn('data-localized-en="{{ member.name_en | escape }}"', team_layout)
        self.assertNotIn('class="team-english-name"', team_layout)
        self.assertNotIn('class="member-name-en"', team_layout)

    def test_category_search_script_has_normalized_matching(self):
        script = (self.repo_root / "assets" / "js" / "category-search.js").read_text(
            encoding="utf-8"
        )
        self.assertIn("normalizeForSearch", script)
        self.assertIn("rebuildSearchCache", script)
        self.assertIn("searchInput.addEventListener('search', filterCards)", script)

    def test_default_layout_has_prompt_focused_soul_meta(self):
        default_layout = (self.repo_root / "_layouts" / "default.html").read_text(encoding="utf-8")

        self.assertIn("Prompts - Agent Souls", default_layout)
        self.assertIn("AI character prompt", default_layout)
        self.assertIn('<link rel="canonical"', default_layout)
        self.assertNotIn("{% seo %}", default_layout)

    def test_prompts_landing_page_targets_requested_keywords(self):
        prompts_page = (self.repo_root / "prompts.md").read_text(encoding="utf-8")

        self.assertIn(
            'title: "AI Character Prompts - Historical Figures & Virtual Characters"',
            prompts_page,
        )
        self.assertIn("Laozi prompts", prompts_page)
        self.assertIn("Sherlock Holmes prompts", prompts_page)
        self.assertIn("AI character prompts", prompts_page)

    def test_homepage_description_mentions_ai_character_prompts(self):
        index_page = (self.repo_root / "index.md").read_text(encoding="utf-8")

        self.assertIn("description:", index_page)
        self.assertIn("AI character prompts", index_page)
        self.assertIn("prompts", index_page)

    def test_config_avoids_underscore_directories_in_sitemap_output(self):
        config = (self.repo_root / "_config.yml").read_text(encoding="utf-8")

        self.assertIn("Character Prompts", config)
        self.assertNotIn("  - _layouts", config)
        self.assertNotIn("  - _includes", config)
        self.assertNotIn("  - _sass", config)


class DeployWorkflowBaseurlRegressionTest(unittest.TestCase):
    def setUp(self):
        self.repo_root = Path(__file__).resolve().parents[1]

    def test_deploy_workflow_does_not_force_souls_baseurl(self):
        deploy_workflow = (self.repo_root / ".github" / "workflows" / "deploy.yml").read_text(
            encoding="utf-8"
        )
        self.assertNotIn('BASE_PATH="/souls"', deploy_workflow)


class GenerateSoulPagesCleanupTest(unittest.TestCase):
    def setUp(self):
        self.module = load_module()
        self.tmpdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tmpdir.name)

        category_dir = self.root / "real_world"
        category_dir.mkdir(parents=True)

        ada_dir = category_dir / "ada_lovelace"
        ada_dir.mkdir(parents=True)
        ada_dir.joinpath("SOUL.md").write_text("# 阿达·洛夫莱斯\n\n内容。", encoding="utf-8")
        ada_dir.joinpath("SOUL.en.md").write_text("# Ada Lovelace\n\nContent.", encoding="utf-8")
        ada_dir.joinpath("README.md").write_text(
            "# 阿达·洛夫莱斯\n\n## 基本信息\n- **英文名**: Ada Lovelace\n",
            encoding="utf-8",
        )

        # Simulate stale generated page from an old folder name.
        category_dir.joinpath("old_name.md").write_text("stale", encoding="utf-8")

        self.previous_root = self.module.ROOT
        self.module.ROOT = self.root

    def tearDown(self):
        self.module.ROOT = self.previous_root
        self.tmpdir.cleanup()

    def test_stale_generated_pages_are_removed(self):
        self.module.generate_for_category("real_world", "真实世界")
        self.assertFalse((self.root / "real_world" / "old_name.md").exists())
        self.assertTrue((self.root / "real_world" / "ada_lovelace.md").exists())


class SoulMarkdownTableSpacingRegressionTest(unittest.TestCase):
    def setUp(self):
        self.repo_root = Path(__file__).resolve().parents[1]

    def assert_heading_has_blank_line_before_table(
        self,
        markdown_text: str,
        heading: str,
        table_header: str,
    ):
        marker = f"{heading}\n\n{table_header}"
        self.assertIn(
            marker,
            markdown_text,
            f"Expected a blank line between '{heading}' and '{table_header}'.",
        )

    def test_hamlet_tables_have_required_blank_line(self):
        zh = (self.repo_root / "virtual_world" / "hamlet" / "SOUL.md").read_text(
            encoding="utf-8"
        )
        en = (self.repo_root / "virtual_world" / "hamlet" / "SOUL.en.md").read_text(
            encoding="utf-8"
        )

        self.assert_heading_has_blank_line_before_table(zh, "### 典型回应模式", "| 情境 | 反应方式 |")
        self.assert_heading_has_blank_line_before_table(
            en, "### Typical Response Patterns", "| Situation | Response |"
        )

    def test_all_category_souls_have_blank_line_before_table(self):
        import re

        heading_then_table = re.compile(r"^(#{1,6}\s+.+)\n(\|[^\n]*\|\s*)$", re.M)
        categories = ["real_world", "virtual_world", "personas"]
        offenders: list[str] = []

        for category in categories:
            for soul_file in sorted((self.repo_root / category).rglob("SOUL*.md")):
                text = soul_file.read_text(encoding="utf-8")
                if heading_then_table.search(text):
                    offenders.append(str(soul_file.relative_to(self.repo_root)))

        self.assertEqual(
            offenders,
            [],
            "Expected a blank line between heading and table header in soul files. "
            f"Found {len(offenders)} offenders: {offenders[:20]}",
        )


class PersonaTitleNormalizationRegressionTest(unittest.TestCase):
    TARGET_PERSONAS = [
        "historian",
        "video_editor",
        "financial_planner",
        "fitness_coach",
        "economist",
        "yoga_instructor",
        "relationship_consultant",
        "colorist",
        "psychologist",
        "sleep_consultant",
        "sociologist",
        "photography_mentor",
        "psychological_counselor",
        "sound_designer",
        "mindfulness_mentor",
        "political_analyst",
        "painting_coach",
        "game_designer",
        "environmental_expert",
        "organization_consultant",
        "music_theorist",
        "animator",
        "medical_expert",
        "time_management_coach",
        "instrument_coach",
        "legal_scholar",
        "scientist",
        "film_director_consultant",
        "philosopher",
    ]

    def setUp(self):
        self.repo_root = Path(__file__).resolve().parents[1]

    @staticmethod
    def parse_readme_names(readme_text: str) -> tuple[str, str]:
        zh_match = re.search(r"\*\*中文名\*\*:\s*(.+)", readme_text)
        en_match = re.search(r"\*\*英文名\*\*:\s*(.+)", readme_text)
        if not zh_match or not en_match:
            return "", ""
        return zh_match.group(1).strip(), en_match.group(1).strip()

    def test_recent_persona_titles_use_expert_names_not_person_names(self):
        offenders: list[str] = []

        for slug in self.TARGET_PERSONAS:
            folder = self.repo_root / "personas" / slug
            readme_text = (folder / "README.md").read_text(encoding="utf-8")
            zh_name, en_name = self.parse_readme_names(readme_text)

            zh_heading = (folder / "SOUL.md").read_text(encoding="utf-8").splitlines()[0].strip()
            en_heading = (
                folder / "SOUL.en.md"
            ).read_text(encoding="utf-8").splitlines()[0].strip()

            expected_zh_heading = f"# {zh_name} ({en_name})"
            expected_en_heading = f"# {en_name} ({zh_name})"

            if zh_heading != expected_zh_heading or en_heading != expected_en_heading:
                offenders.append(
                    f"{slug}: zh='{zh_heading}' expected='{expected_zh_heading}'; "
                    f"en='{en_heading}' expected='{expected_en_heading}'"
                )

        self.assertEqual(
            offenders,
            [],
            "Expected recent persona titles to match expert names in README. "
            f"Found {len(offenders)} offenders: {offenders}",
        )


class SiteBuildSeoRegressionTest(unittest.TestCase):
    @staticmethod
    def read_optional_text(*paths: Path) -> str:
        for path in paths:
            if path.exists():
                return path.read_text(encoding="utf-8")
        return ""

    @classmethod
    def setUpClass(cls):
        cls.repo_root = Path(__file__).resolve().parents[1]
        env = dict(os.environ, JEKYLL_ENV="production", PYTHONDONTWRITEBYTECODE="1")

        subprocess.run(
            ["python3", "scripts/generate_soul_pages.py"],
            cwd=cls.repo_root,
            check=True,
            env=env,
        )
        subprocess.run(
            ["bundle", "exec", "jekyll", "build", "--baseurl", ""],
            cwd=cls.repo_root,
            check=True,
            env=env,
        )

        cls.site_root = cls.repo_root / "_site"
        cls.index_html = (cls.site_root / "index.html").read_text(encoding="utf-8")
        cls.real_world_html = cls.read_optional_text(
            cls.site_root / "real_world" / "index.html",
            cls.site_root / "real_world.html",
        )
        cls.virtual_world_html = cls.read_optional_text(
            cls.site_root / "virtual_world" / "index.html",
            cls.site_root / "virtual_world.html",
        )
        cls.personas_html = cls.read_optional_text(
            cls.site_root / "personas" / "index.html",
            cls.site_root / "personas.html",
        )
        cls.zhuge_liang_html = (
            cls.site_root / "real_world" / "zhuge_liang" / "index.html"
        ).read_text(encoding="utf-8")
        cls.sitemap_xml = (cls.site_root / "sitemap.xml").read_text(encoding="utf-8")
        cls.robots_txt = (cls.site_root / "robots.txt").read_text(encoding="utf-8")

    def test_homepage_renders_single_optimized_title_and_description(self):
        self.assertEqual(self.index_html.count("<title>"), 1)
        self.assertIn("Agent Souls", self.index_html)
        self.assertNotIn("<title>Souls - Souls</title>", self.index_html)
        self.assertIn("200+历史人物", self.index_html)

    def test_category_pages_use_pretty_urls_and_specific_descriptions(self):
        self.assertTrue((self.site_root / "real_world" / "index.html").exists())
        self.assertTrue((self.site_root / "virtual_world" / "index.html").exists())
        self.assertTrue((self.site_root / "personas" / "index.html").exists())

        self.assertIn(
            '<link rel="canonical" href="https://agent-souls.com/real_world/" />',
            self.real_world_html,
        )
        self.assertIn("历史人物AI灵魂库", self.real_world_html)
        self.assertIn("经典虚拟角色AI人格设定", self.virtual_world_html)
        self.assertIn("专家角色AI人格设定", self.personas_html)

    def test_detail_pages_render_ai_focused_metadata_and_clean_schema(self):
        self.assertIn("诸葛亮 AI 灵魂设定", self.zhuge_liang_html)
        self.assertIn("twitter:description", self.zhuge_liang_html)
        self.assertIn('"@type": "CreativeWork"', self.zhuge_liang_html)
        self.assertNotIn('"sameAs": ["", ""]', self.zhuge_liang_html)

    def test_built_html_uses_chinese_source_locale(self):
        self.assertIn('<html\n  lang="zh-CN"', self.index_html)
        self.assertIn('meta property="og:locale" content="zh_CN"', self.index_html)

    def test_sitemap_excludes_internal_template_paths(self):
        self.assertNotIn("/_layouts/", self.sitemap_xml)
        self.assertNotIn("/_includes/", self.sitemap_xml)

    def test_robots_has_explicit_crawler_rules(self):
        self.assertIn("User-agent: *", self.robots_txt)
        self.assertIn("Allow: /", self.robots_txt)
        self.assertIn("Disallow: /_layouts/", self.robots_txt)
        self.assertIn("Disallow: /_includes/", self.robots_txt)
        self.assertIn("Sitemap: https://agent-souls.com/sitemap.xml", self.robots_txt)


if __name__ == "__main__":
    unittest.main()
