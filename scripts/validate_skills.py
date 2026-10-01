"""Validate the lightweight skill pack structure.

This script intentionally uses only the Python standard library so GitHub
Actions can run it without installing package dependencies.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"


FRONTMATTER_RE = re.compile(r"\A---\r?\n(?P<body>.*?)\r?\n---\r?\n", re.DOTALL)
FIELD_RE = re.compile(r"^(?P<key>[A-Za-z0-9_-]+):\s*(?P<value>.+?)\s*$")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("missing YAML frontmatter delimited by ---")

    fields: dict[str, str] = {}
    for line in match.group("body").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        field = FIELD_RE.match(line)
        if not field:
            raise ValueError(f"unsupported frontmatter line: {line!r}")
        fields[field.group("key")] = field.group("value").strip().strip('"').strip("'")
    return fields


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"

    if not skill_file.exists():
        return [f"{skill_dir.relative_to(ROOT)} is missing SKILL.md"]

    try:
        fields = parse_frontmatter(skill_file)
    except ValueError as exc:
        return [f"{skill_file.relative_to(ROOT)}: {exc}"]

    name = fields.get("name", "")
    description = fields.get("description", "")

    if not name:
        errors.append(f"{skill_file.relative_to(ROOT)}: missing name")
    elif not NAME_RE.fullmatch(name):
        errors.append(f"{skill_file.relative_to(ROOT)}: invalid skill name {name!r}")
    elif name != skill_dir.name:
        errors.append(
            f"{skill_file.relative_to(ROOT)}: name {name!r} does not match folder {skill_dir.name!r}"
        )

    if not description:
        errors.append(f"{skill_file.relative_to(ROOT)}: missing description")
    elif len(description) < 40:
        errors.append(f"{skill_file.relative_to(ROOT)}: description is too short")

    text = skill_file.read_text(encoding="utf-8")
    if "TODO" in text or "[TODO]" in text:
        errors.append(f"{skill_file.relative_to(ROOT)}: contains TODO placeholder")

    return errors


def main() -> int:
    if not SKILLS_DIR.exists():
        print("skills/ directory not found", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        print("no skill directories found", file=sys.stderr)
        return 1

    errors: list[str] = []
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
