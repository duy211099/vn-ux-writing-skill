"""Mechanical checks for skill folders.

Usage: python3 scripts/check_skill.py <skill_dir>
       python3 scripts/check_skill.py --all [root]
"""

import re
import sys
import unicodedata
from pathlib import Path

MAX_SKILL_LINES = 200
MAX_DESCRIPTION = 1024
NAME_RE = re.compile(r"^[a-z0-9-]+$")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
PLACEHOLDER_RE = re.compile(r"\b(TBD|TODO)\b")
INDEXED_DIRS = ("references", "templates", "examples")
# (source of truth, copy that must stay byte-identical), relative to the repo root.
SYNCED_FILES: list[tuple[str, str]] = [
    ("skills/style-vi/templates/giong-van.md", "skills/ux-writing-vi/templates/giong-van.md"),
]


def _frontmatter(text: str) -> dict[str, str] | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip()
    return None


def _check_frontmatter(text: str) -> list[str]:
    fm = _frontmatter(text)
    if fm is None:
        return ["SKILL.md: missing YAML front matter"]
    errors = []
    name = fm.get("name", "")
    if not NAME_RE.match(name):
        errors.append("SKILL.md: front matter 'name' missing or not [a-z0-9-]")
    desc = fm.get("description", "")
    if not desc:
        errors.append("SKILL.md: front matter 'description' missing")
    elif len(desc) > MAX_DESCRIPTION:
        errors.append(f"SKILL.md: description longer than {MAX_DESCRIPTION} chars")
    return errors


def _is_relative_link(target: str) -> bool:
    return not re.match(r"^[a-z]+:", target) and not target.startswith("#")


def check_skill(skill_dir: Path) -> list[str]:
    skill_dir = Path(skill_dir)
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return ["SKILL.md: not found"]

    skill_text = skill_md.read_text(encoding="utf-8")
    errors = _check_frontmatter(skill_text)

    if len(skill_text.splitlines()) > MAX_SKILL_LINES:
        errors.append(f"SKILL.md: more than {MAX_SKILL_LINES} lines")

    for d in INDEXED_DIRS:
        for p in sorted((skill_dir / d).rglob("*.md")):
            rel = p.relative_to(skill_dir).as_posix()
            if rel not in skill_text:
                errors.append(f"SKILL.md: does not reference {rel}")

    for p in sorted(skill_dir.rglob("*.md")):
        rel = p.relative_to(skill_dir).as_posix()
        text = p.read_text(encoding="utf-8")
        if unicodedata.normalize("NFC", text) != text:
            errors.append(f"{rel}: text is not Unicode NFC")
        if m := PLACEHOLDER_RE.search(text):
            errors.append(f"{rel}: contains placeholder {m.group(1)}")
        for target in LINK_RE.findall(text):
            if not _is_relative_link(target):
                continue
            path = target.split("#", 1)[0]
            if path and not (p.parent / path).exists():
                errors.append(f"{rel}: broken link {target}")
    return errors


def skill_dirs(root: Path) -> list[Path]:
    """Every directory under root/skills/ that contains a SKILL.md, sorted."""
    skills = Path(root) / "skills"
    if not skills.is_dir():
        return []
    return sorted(d for d in skills.iterdir() if (d / "SKILL.md").is_file())


def _check_synced(root: Path) -> list[str]:
    errors = []
    for source, copy in SYNCED_FILES:
        src, dst = Path(root) / source, Path(root) / copy
        if not src.is_file() and not dst.is_file():
            continue
        if not src.is_file():
            errors.append(f"{source}: missing (source of {copy})")
        elif not dst.is_file():
            errors.append(f"{copy}: missing (copy of {source})")
        elif src.read_bytes() != dst.read_bytes():
            errors.append(f"{copy} differs from {source}")
    return errors


def check_repo(root: Path) -> list[str]:
    """Run check_skill on every skill under root/skills/, then repo-wide checks."""
    errors: list[str] = _check_synced(root)
    for d in skill_dirs(root):
        prefix = f"skills/{d.name}"
        errors += [f"{prefix}/{e}" for e in check_skill(d)]
        fm = _frontmatter((d / "SKILL.md").read_text(encoding="utf-8")) or {}
        name = fm.get("name", "")
        if name and name != d.name:
            errors.append(f"{prefix}: front matter name '{name}' does not match folder")
    return errors


def main(argv: list[str]) -> int:
    if argv and argv[0] == "--all" and len(argv) <= 2:
        errors = check_repo(Path(argv[1]) if len(argv) == 2 else Path("."))
    elif len(argv) == 1 and argv[0] != "--all":
        errors = check_skill(Path(argv[0]))
    else:
        print("usage: check_skill.py <skill_dir> | --all [root]", file=sys.stderr)
        return 2
    for e in errors:
        print(e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
