import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class SeoMetadataTest(unittest.TestCase):
    def test_default_layout_uses_prompts_title_for_soul_pages(self):
        template = (REPO_ROOT / "_layouts" / "default.html").read_text(encoding="utf-8")

        self.assertIn("page.layout == 'soul'", template)
        self.assertIn("page.english_name | default: page.title", template)
        self.assertIn("Prompts - Agent Souls", template)

    def test_config_sets_prompt_library_site_metadata(self):
        config = (REPO_ROOT / "_config.yml").read_text(encoding="utf-8")

        self.assertIn('title: "Agent Souls - AI Character Prompts Library"', config)
        self.assertIn("AI prompts and character prompts", config)
        self.assertIn("historical figures", config)
        self.assertIn("expert personas", config)

    def test_homepage_front_matter_targets_agent_souls(self):
        index_page = (REPO_ROOT / "index.md").read_text(encoding="utf-8")

        self.assertIn("title: Agent Souls", index_page)
        self.assertIn(
            'description: "AI Character Prompts for Historical Figures. Download 200+ AI souls like Laozi, Confucius, Socrates. Free prompts for ChatGPT, Claude."',
            index_page,
        )

    def test_prompts_landing_page_exists_with_prompt_keywords(self):
        prompts_page = (REPO_ROOT / "prompts.md").read_text(encoding="utf-8")
        prompts_text = prompts_page.lower()

        self.assertIn("AI Character Prompts - Historical Figures & Virtual Characters", prompts_page)
        self.assertIn("ai prompts", prompts_text)
        self.assertIn("character prompts", prompts_text)
        self.assertIn("historical figure prompts", prompts_text)
        for url in [
            "/real_world/laozi/",
            "/real_world/confucius/",
            "/real_world/socrates/",
            "/virtual_world/sherlock_holmes/",
            "/personas/silicon_valley_cto/",
        ]:
            self.assertIn(url, prompts_page)

    def test_robots_txt_exists_with_sitemap(self):
        robots_txt = (REPO_ROOT / "robots.txt").read_text(encoding="utf-8")

        self.assertIn("User-agent: *", robots_txt)
        self.assertIn("Sitemap:", robots_txt)


if __name__ == "__main__":
    unittest.main()
