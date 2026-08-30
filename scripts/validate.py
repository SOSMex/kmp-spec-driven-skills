#!/usr/bin/env python3
"""Validate repository structure, skill metadata, links, evals, and secrets."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = (
    "kmp-spec-driven-design",
    "kmp-proof-of-parity",
)
REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "evals/cases.json",
    "templates/spec.md",
    "templates/rfc.md",
    "templates/adr.md",
    "templates/plan.md",
    "templates/tasks.md",
    "templates/verification-report.md",
    "templates/handoff.md",
)
FRONTMATTER_PATTERN = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
NAME_PATTERN = re.compile(r"^[a-z0-9-]{1,64}$")
PLACEHOLDER_PATTERN = re.compile(r"\b(?:TODO|TBD|FIXME|CHANGE_ME)\b")
SECRET_PATTERNS = (
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]+"),
    re.compile(r"\bghp_[A-Za-z0-9]+"),
    re.compile(r"\bAIza[0-9A-Za-z_-]{20,}"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"),
)


def parse_frontmatter(path: Path) -> dict[str, str]:
    match = FRONTMATTER_PATTERN.match(path.read_text(encoding="utf-8"))
    if not match:
        raise ValueError("missing YAML frontmatter")
    metadata: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()
    return metadata


def markdown_files() -> list[Path]:
    return sorted(ROOT.rglob("*.md"))


def validate_links(path: Path) -> list[str]:
    errors: list[str] = []
    for raw_target in LINK_PATTERN.findall(path.read_text(encoding="utf-8")):
        target = raw_target.strip().split()[0].strip("<>")
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        local_part = target.split("#", 1)[0]
        if not local_part:
            continue
        resolved = (path.parent / local_part).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken link {raw_target}")
    return errors


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).exists():
            errors.append(f"missing required file: {relative}")

    for skill in SKILLS:
        path = ROOT / "skills" / skill / "SKILL.md"
        if not path.exists():
            errors.append(f"missing skill: {path.relative_to(ROOT)}")
            continue
        try:
            metadata = parse_frontmatter(path)
        except ValueError as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
            continue
        if metadata.get("name") != skill:
            errors.append(f"{path.relative_to(ROOT)}: name must match directory")
        if not NAME_PATTERN.fullmatch(metadata.get("name", "")):
            errors.append(f"{path.relative_to(ROOT)}: invalid skill name")
        description = metadata.get("description", "")
        if not description or len(description) > 1024:
            errors.append(f"{path.relative_to(ROOT)}: invalid description length")
        if len(path.read_text(encoding="utf-8").splitlines()) > 500:
            errors.append(f"{path.relative_to(ROOT)}: SKILL.md exceeds 500 lines")

    eval_path = ROOT / "evals" / "cases.json"
    if eval_path.exists():
        try:
            payload = json.loads(eval_path.read_text(encoding="utf-8"))
            cases = payload.get("cases", [])
            if len(cases) < 3:
                errors.append("evals/cases.json: at least three cases are required")
            ids: set[str] = set()
            for case in cases:
                case_id = case.get("id", "")
                if not case_id or case_id in ids:
                    errors.append(f"evals/cases.json: invalid or duplicate id {case_id!r}")
                ids.add(case_id)
                if case.get("skill") not in SKILLS:
                    errors.append(f"evals/cases.json: unknown skill for {case_id}")
                if not case.get("prompt") or not case.get("expected_invariants"):
                    errors.append(f"evals/cases.json: incomplete case {case_id}")
        except (json.JSONDecodeError, AttributeError) as exc:
            errors.append(f"evals/cases.json: {exc}")

    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        if PLACEHOLDER_PATTERN.search(text):
            errors.append(f"{relative}: unresolved placeholder marker")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"{relative}: possible secret pattern")
        errors.extend(validate_links(path))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Validation passed: {len(SKILLS)} skills, "
        f"{len(json.loads(eval_path.read_text(encoding='utf-8'))['cases'])} eval cases, "
        f"{len(markdown_files())} Markdown files."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
