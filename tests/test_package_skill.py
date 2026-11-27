import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.package_skill import package_skill

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "ux-writing-vi"


class PackageSkillTest(unittest.TestCase):
    def test_zip_contains_skill_md(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = package_skill(SKILL_DIR, Path(tmp) / "ux-writing-vi.zip")
            names = set(zipfile.ZipFile(out).namelist())
        self.assertIn("ux-writing-vi/SKILL.md", names)
        for ref in (SKILL_DIR / "references").glob("*.md"):
            self.assertIn(f"ux-writing-vi/references/{ref.name}", names)
        self.assertFalse(any("/." in n for n in names), names)

    def test_refuses_invalid_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "bad"
            bad.mkdir()
            (bad / "SKILL.md").write_text("no front matter\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                package_skill(bad, Path(tmp) / "out.zip")


if __name__ == "__main__":
    unittest.main()
