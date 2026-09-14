"""Unit tests for html_extra/robots.txt (SEO crawler entry point)."""
from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROBOTS = ROOT / "html_extra" / "robots.txt"


class RobotsTxtTest(unittest.TestCase):
    def test_robots_has_user_agent_allow_sitemap(self):
        self.assertTrue(ROBOTS.is_file(), f"missing {ROBOTS}")
        text = ROBOTS.read_text(encoding="utf-8")
        self.assertIn("User-agent: *", text)
        self.assertIn("Allow: /", text)
        self.assertIn("Sitemap: https://doc.eyssen.com/sitemap.xml", text)


if __name__ == "__main__":
    unittest.main()
