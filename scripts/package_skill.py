"""Build a shareable zip of the skill folder.

Usage: python3 scripts/package_skill.py ux-writing-vi dist/ux-writing-vi.zip
"""

import sys
import zipfile
from pathlib import Path

try:
    from scripts.check_skill import check_skill
except ModuleNotFoundError:  # run as a script: scripts/ is on sys.path
    from check_skill import check_skill


def package_skill(skill_dir: Path, out_path: Path) -> Path:
    skill_dir = Path(skill_dir)
    out_path = Path(out_path)
    errors = check_skill(skill_dir)
    if errors:
        raise ValueError("skill check failed:\n" + "\n".join(errors))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(skill_dir.rglob("*")):
            rel = p.relative_to(skill_dir)
            if p.is_dir() or any(part.startswith(".") for part in rel.parts):
                continue
            zf.write(p, (Path(skill_dir.name) / rel).as_posix())
    return out_path


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: package_skill.py <skill_dir> <out.zip>", file=sys.stderr)
        return 2
    try:
        out = package_skill(Path(argv[0]), Path(argv[1]))
    except ValueError as e:
        print(e, file=sys.stderr)
        return 1
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
