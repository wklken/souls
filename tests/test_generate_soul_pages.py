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

    def test_home_stats_use_data_count(self):
        home_layout = (self.repo_root / "_layouts" / "home.html").read_text(encoding="utf-8")
        self.assertIn('data-count="{{ site.stats.total }}"', home_layout)
        self.assertIn('data-count="{{ site.stats.real_world }}"', home_layout)
        self.assertIn('data-count="{{ site.stats.virtual_world }}"', home_layout)
        self.assertIn('data-count="{{ site.stats.personas }}"', home_layout)


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


if __name__ == "__main__":
    unittest.main()
