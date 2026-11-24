#!/usr/bin/env python3
"""Scaffold a new architecture repository from the template tree.

Usage:
  scaffold.py --name "Project name" --dest DIR [--id 70] [--pages-url URL] [--dry-run]

Copies assets/template/ into DIR and replaces the placeholders. Never overwrites an existing file.
Standard library only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import shutil
import subprocess
import sys
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "assets" / "template"
TEXT_SUFFIXES = {".md", ".json", ".py", ".gitignore", ""}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name", required=True, help="Project name, e.g. 'OCP KubeVirt platform'")
    ap.add_argument("--dest", required=True, type=Path, help="Destination directory")
    ap.add_argument("--id", default="", help="Document ID used as the architecture title prefix, e.g. 70")
    ap.add_argument("--pages-url", default="", help="GitHub Pages base URL, e.g. https://owner.github.io/repo")
    ap.add_argument("--dry-run", action="store_true", help="List what would be written, write nothing")
    args = ap.parse_args()

    dest: Path = args.dest.expanduser().resolve()
    pages = args.pages_url.rstrip("/")
    subs = {
        "{{PROJECT_NAME}}": args.name,
        "{{TITLE_PREFIX}}": f"{args.id} :: " if args.id else "",
        # With no Pages URL, links fall back to repo-relative paths.
        "{{PAGES_BASE}}": pages if pages else ".",
        "{{DATE}}": dt.date.today().isoformat(),
    }

    written, skipped = [], []
    for src in sorted(TEMPLATE.rglob("*")):
        if src.is_dir() or src.name == ".DS_Store":
            continue
        rel = src.relative_to(TEMPLATE)
        out = dest / rel
        if out.exists():
            skipped.append(rel)
            continue
        written.append(rel)
        if args.dry_run:
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix in TEXT_SUFFIXES or src.name.startswith("."):
            text = src.read_text(encoding="utf-8")
            if src.suffix != ".py":  # the generator is copied verbatim
                for k, v in subs.items():
                    text = text.replace(k, v)
            out.write_text(text, encoding="utf-8")
        else:
            shutil.copy2(src, out)

    verb = "Would write" if args.dry_run else "Wrote"
    print(f"{verb} {len(written)} files under {dest}")
    for r in written:
        print(f"  + {r}")
    if skipped:
        print(f"Skipped {len(skipped)} existing files:")
        for r in skipped:
            print(f"  = {r}")

    gen = dest / "docs" / "implementation-status" / "_generate.py"
    if not args.dry_run and gen.exists():
        res = subprocess.run([sys.executable, str(gen)], capture_output=True, text=True)
        if res.returncode == 0:
            print("Generated docs/implementation-status/status-light.svg, status-dark.svg, index.html")
        else:
            print("Status generator failed:\n" + res.stderr, file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
