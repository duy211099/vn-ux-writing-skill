import unicodedata
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTROLS = ROOT / "evals" / "humanizer-vi" / "controls"
SKILLS = ROOT / "skills"

FIELDS = ("source", "revision", "date", "author", "license", "register")
LICENSES = {
    "CC BY-SA 4.0",
    "CC BY-SA 3.0",
    "CC BY 2.0 FR",
    "public domain (Luật SHTT Điều 15)",
}
REGISTERS = {"formal", "personal", "casual"}


def parse(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---\n", 2)
    assert parts[0] == "" and len(parts) == 3, f"{path.name}: bad front matter"
    meta = {}
    for line in parts[1].splitlines():
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip().strip('"')
    return meta, parts[2].strip()


def controls() -> list[tuple[Path, dict, str]]:
    return [(p, *parse(p)) for p in sorted(CONTROLS.glob("*.md")) if p.name != "NOTICE.md"]


class ControlsTest(unittest.TestCase):
    def test_controls_exist(self):
        self.assertGreaterEqual(len(controls()), 10)

    def test_controls_have_metadata(self):
        for p, meta, _ in controls():
            for f in FIELDS:
                self.assertTrue(meta.get(f), f"{p.name}: missing {f}")
            self.assertIn(meta["license"], LICENSES, p.name)
            self.assertIn(meta["register"], REGISTERS, p.name)
            self.assertLess(meta["date"], "2022-06-01", p.name)

    def test_controls_nfc_and_length(self):
        for p, meta, body in controls():
            self.assertEqual(body, unicodedata.normalize("NFC", body), p.name)
            n = len(body.split())
            self.assertLessEqual(n, 300, p.name)
            if "tatoeba.org" not in meta["source"]:
                self.assertGreaterEqual(n, 50, p.name)

    def test_registers_covered(self):
        regs = [m["register"] for _, m, _ in controls()]
        for r in REGISTERS:
            self.assertGreaterEqual(regs.count(r), 3, r)

    def test_controls_not_in_skills(self):
        skill_text = "\n".join(
            f.read_text(encoding="utf-8", errors="ignore")
            for f in SKILLS.rglob("*") if f.is_file()
        )
        skill_text = unicodedata.normalize("NFC", skill_text)
        for p, _, body in controls():
            self.assertNotIn(body[:40], skill_text, p.name)


if __name__ == "__main__":
    unittest.main()
