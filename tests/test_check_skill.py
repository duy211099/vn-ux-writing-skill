import contextlib
import io
import tempfile
import unicodedata
import unittest
from pathlib import Path

from scripts.check_skill import check_skill, main

VALID_SKILL = """---
name: ux-writing-vi
description: Use when writing Vietnamese UI text.
---

# Skill

See [rules](references/a.md).
"""


def make_skill(root: Path, skill_md: str = VALID_SKILL, files: dict | None = None) -> Path:
    (root / "SKILL.md").write_text(skill_md, encoding="utf-8")
    files = {"references/a.md": "# A\n"} if files is None else files
    for rel, text in files.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    return root


class CheckSkillTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def test_valid_skill_passes(self):
        self.assertEqual(check_skill(make_skill(self.root)), [])

    def test_missing_frontmatter_name(self):
        md = VALID_SKILL.replace("name: ux-writing-vi\n", "")
        errors = check_skill(make_skill(self.root, md))
        self.assertEqual(len(errors), 1)
        self.assertIn("name", errors[0])

    def test_skill_md_too_long(self):
        md = VALID_SKILL + "line\n" * 201
        errors = check_skill(make_skill(self.root, md))
        self.assertTrue(any("200" in e for e in errors), errors)

    def test_unreferenced_reference_file(self):
        files = {"references/a.md": "# A\n", "references/x.md": "# X\n"}
        errors = check_skill(make_skill(self.root, files=files))
        self.assertTrue(any("references/x.md" in e for e in errors), errors)

    def test_broken_relative_link(self):
        files = {"references/a.md": "[a](nope.md)\n"}
        errors = check_skill(make_skill(self.root, files=files))
        self.assertTrue(any("nope.md" in e for e in errors), errors)

    def test_nfd_text_rejected(self):
        files = {"references/a.md": unicodedata.normalize("NFD", "Xóa tài khoản\n")}
        errors = check_skill(make_skill(self.root, files=files))
        self.assertTrue(any("NFC" in e and "a.md" in e for e in errors), errors)

    def test_tbd_rejected(self):
        files = {"references/a.md": "# A\nTBD\n"}
        errors = check_skill(make_skill(self.root, files=files))
        self.assertTrue(any("TBD" in e for e in errors), errors)

    def test_main_exit_codes(self):
        valid = self.root / "ok"
        valid.mkdir()
        make_skill(valid)
        bad = self.root / "bad"
        bad.mkdir()
        make_skill(bad, VALID_SKILL.replace("name: ux-writing-vi\n", ""))
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(main([str(valid)]), 0)
            self.assertEqual(main([str(bad)]), 1)


if __name__ == "__main__":
    unittest.main()
