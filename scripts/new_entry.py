#!/usr/bin/env python3
"""Create a new note from a template."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TYPE_TO_DIR = {
    "skill": "skills",
    "plugin": "plugins",
    "tool": "tools",
    "prompt": "prompts",
    "workflow": "workflows",
    "automation": "automations",
    "case-study": "examples",
    "reference": "docs",
}


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def load_template(entry_type: str) -> str:
    specific = ROOT / "templates" / f"{entry_type}.md"
    fallback = ROOT / "templates" / "entry.md"
    return (specific if specific.exists() else fallback).read_text()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", required=True, choices=sorted(TYPE_TO_DIR))
    parser.add_argument("--slug", required=True)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()

    slug = slugify(args.slug)
    if not slug:
        raise SystemExit("slug must contain at least one ASCII letter or digit")

    target_dir = ROOT / TYPE_TO_DIR[args.type]
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f"{slug}.md"
    if target.exists():
        raise SystemExit(f"entry already exists: {target}")

    today = dt.date.today().isoformat()
    content = load_template(args.type)
    content = content.replace("{{TITLE}}", args.title.strip())
    content = content.replace("{{TYPE}}", args.type)
    content = content.replace("{{DATE}}", today)
    target.write_text(content)
    print(target.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
