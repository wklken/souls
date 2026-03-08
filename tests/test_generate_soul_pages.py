import importlib.util
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

    def test_i18n_updates_all_search_input_placeholders(self):
        i18n_script = (self.repo_root / "assets" / "js" / "i18n.js").read_text(encoding="utf-8")
        self.assertIn("querySelectorAll('[data-search-input]')", i18n_script)


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


if __name__ == "__main__":
    unittest.main()
