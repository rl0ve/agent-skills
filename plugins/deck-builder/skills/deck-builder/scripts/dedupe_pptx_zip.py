#!/usr/bin/env python3
"""Remove duplicate zip entries from a .pptx.

Why this exists
---------------
python-pptx cannot truly delete a slide part from the package zip. Deleting a
slide only removes it from the slide ID list; the original `slide1.xml` stays in
the archive. When your build then writes its own `slide1.xml`, both entries end
up in the zip. PowerPoint reads that as a corrupt package and shows the
"PowerPoint found a problem with content" repair dialog on every open.

Any build that starts from a template containing slides is exposed to this. It
looks like a broken deck and is actually a packaging artefact.

Run this after every `prs.save()`. Last copy of a duplicated name wins, which is
the one your build wrote.

    from dedupe_pptx_zip import deduplicate_pptx_zip
    prs.save(out)
    deduplicate_pptx_zip(out)

or from the shell:

    python3 dedupe_pptx_zip.py deck.pptx
"""

from __future__ import annotations

import argparse
import shutil
import sys
import zipfile
from pathlib import Path


def find_duplicates(path: Path) -> dict[str, int]:
    """Return {entry name: count} for every name appearing more than once."""
    counts: dict[str, int] = {}
    with zipfile.ZipFile(path, "r") as zin:
        for info in zin.infolist():
            counts[info.filename] = counts.get(info.filename, 0) + 1
    return {name: n for name, n in counts.items() if n > 1}


def deduplicate_pptx_zip(path: str | Path) -> int:
    """Rewrite the package so each entry name appears exactly once.

    Later entries overwrite earlier ones, so the copy your build wrote survives
    and the template's stub does not. Returns the number of entries removed.
    """
    path = Path(path)
    tmp = path.with_suffix(path.suffix + ".tmp")

    with zipfile.ZipFile(path, "r") as zin:
        infos = zin.infolist()
        # Last write wins: iterating in order leaves the final copy in `latest`.
        latest: dict[str, bytes] = {}
        for info in infos:
            latest[info.filename] = zin.read(info.filename)

        written: set[str] = set()
        with zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for info in infos:
                if info.filename in written:
                    continue
                written.add(info.filename)
                zout.writestr(info, latest[info.filename])

    removed = len(infos) - len(written)
    shutil.move(str(tmp), str(path))
    return removed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pptx", type=Path, help="Path to the .pptx to rewrite in place.")
    ap.add_argument("--check", action="store_true",
                    help="Report duplicates and exit non-zero, without rewriting.")
    args = ap.parse_args()

    if not args.pptx.exists():
        print(f"No such file: {args.pptx}", file=sys.stderr)
        return 2

    dupes = find_duplicates(args.pptx)

    if args.check:
        if not dupes:
            print(f"{args.pptx.name}: no duplicate entries.")
            return 0
        for name, n in sorted(dupes.items()):
            print(f"  {name} appears {n} times")
        print(f"{args.pptx.name}: {len(dupes)} duplicated entr"
              f"{'y' if len(dupes) == 1 else 'ies'}. PowerPoint will show the repair dialog.")
        return 1

    if not dupes:
        print(f"{args.pptx.name}: already clean, nothing to do.")
        return 0

    removed = deduplicate_pptx_zip(args.pptx)
    print(f"{args.pptx.name}: removed {removed} duplicate entr"
          f"{'y' if removed == 1 else 'ies'} "
          f"({', '.join(sorted(dupes))}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
