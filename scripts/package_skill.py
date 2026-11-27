"""Build a shareable zip of the skill folder.

Usage: python3 scripts/package_skill.py skills/ux-writing-vi dist/ux-writing-vi.zip
       python3 scripts/package_skill.py --all skills dist
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


def package_all(skills_root: Path, out_dir: Path) -> list[Path]:
    skills_root, out_dir = Path(skills_root), Path(out_dir)
    dirs = sorted(d for d in skills_root.iterdir() if (d / "SKILL.md").is_file()) if skills_root.is_dir() else []
    return [package_skill(d, out_dir / f"{d.name}.zip") for d in dirs]


def main(argv: list[str]) -> int:
    try:
        if len(argv) == 3 and argv[0] == "--all":
            outs = package_all(Path(argv[1]), Path(argv[2]))
        elif len(argv) == 2 and argv[0] != "--all":
            outs = [package_skill(Path(argv[0]), Path(argv[1]))]
        else:
            print("usage: package_skill.py <skill_dir> <out.zip> | --all <skills_root> <out_dir>", file=sys.stderr)
            return 2
    except ValueError as e:
        print(e, file=sys.stderr)
        return 1
    for o in outs:
        print(o)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
