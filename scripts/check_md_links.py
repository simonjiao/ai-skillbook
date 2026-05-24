#!/usr/bin/env python3
"""Check local Markdown links without external dependencies."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def normalize_target(raw: str) -> str:
    target = raw.strip()
    if " " in target and not target.startswith("<"):
        target = target.split()[0]
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return unquote(target)


def is_external(target: str) -> bool:
    parsed = urlparse(target)
    return parsed.scheme in {"http", "https", "mailto"}


def target_exists(source: Path, target: str) -> bool:
    target = target.split("#", 1)[0]
    if not target or is_external(target):
        return True
    if target.startswith("/"):
        path = ROOT / target.lstrip("/")
    else:
        path = source.parent / target
    return path.exists()


def main() -> int:
    failures: list[str] = []
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text()
        for match in LINK_RE.finditer(text):
            target = normalize_target(match.group(1))
            if not target_exists(path, target):
                rel = path.relative_to(ROOT)
                failures.append(f"{rel}: broken link: {target}")
    if failures:
        for failure in failures:
            print(failure)
        return 1
    print("Markdown links OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
