#!/usr/bin/env python3
"""Generate a simple catalog from Markdown front matter."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "CATALOG.md"
ENTRY_DIRS = ["skills", "plugins", "tools", "prompts", "workflows", "automations", "examples", "docs"]
FRONT_MATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_front_matter(path: Path) -> dict[str, str]:
    text = path.read_text()
    match = FRONT_MATTER.match(text)
    data: dict[str, str] = {}
    if not match:
        return data
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def iter_entries() -> list[tuple[str, Path, dict[str, str]]]:
    entries: list[tuple[str, Path, dict[str, str]]] = []
    for dirname in ENTRY_DIRS:
        base = ROOT / dirname
        if not base.exists():
            continue
        for path in sorted(base.glob("*.md")):
            if path.name == "README.md":
                continue
            meta = parse_front_matter(path)
            if not meta:
                continue
            entries.append((dirname, path, meta))
    return entries


def render() -> str:
    lines = [
        "# Catalog",
        "",
        "Generated from note front matter.",
        "",
    ]
    current = None
    for dirname, path, meta in iter_entries():
        if dirname != current:
            current = dirname
            lines.extend([f"## {dirname.title()}", ""])
        rel = path.relative_to(ROOT).as_posix()
        title = meta.get("title", path.stem)
        status = meta.get("status", "unknown")
        updated = meta.get("updated", "unknown")
        lines.append(f"- [{title}]({rel}) - `{status}`, updated `{updated}`")
    if len(lines) == 4:
        lines.append("No cataloged entries yet.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if CATALOG.md is stale")
    args = parser.parse_args()

    content = render()
    if args.check:
        if not CATALOG.exists() or CATALOG.read_text() != content:
            raise SystemExit("CATALOG.md is stale; run `make catalog`")
        return 0
    CATALOG.write_text(content)
    print(CATALOG.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
