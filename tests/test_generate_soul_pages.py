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
        persona_dir.joinpath("SOUL.md").write_text("# 急诊室医生\n\n中文内容。", encoding="utf-8")
        persona_dir.joinpath("SOUL.en.md").write_text("# ER Doctor\n\nEnglish content.", encoding="utf-8")
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
        self.assertIn('{% include_relative er_doctor/SOUL.md %}', page)
        self.assertIn('{% include_relative er_doctor/SOUL.en.md %}', page)
        self.assertIn('download_url_en: "/personas/er_doctor/SOUL.en.md"', page)
        self.assertIn(
            'edit_url_en: "https://github.com/wklken/souls/edit/master/personas/er_doctor/SOUL.en.md"',
            page,
        )


if __name__ == "__main__":
    unittest.main()
