#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
from zipfile import ZipFile


def human_size(size: int) -> str:
    units = ["B", "KB", "MB", "GB"]
    value = float(size)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.1f}{unit}"
        value /= 1024
    return f"{size}B"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Report where a PPTX file's package size is coming from."
    )
    parser.add_argument("deck_path", help="Path to the .pptx file")
    parser.add_argument(
        "--top",
        type=int,
        default=15,
        help="How many largest package parts to print (default: 15)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    deck_path = Path(args.deck_path).expanduser().resolve()
    if not deck_path.exists():
        raise SystemExit(f"File not found: {deck_path}")

    bucket_sizes: dict[str, int] = defaultdict(int)
    media_count = 0

    with ZipFile(deck_path) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        for info in infos:
            parts = info.filename.split("/")
            bucket = "/".join(parts[:2]) if len(parts) >= 2 else info.filename
            bucket_sizes[bucket] += info.file_size
            if info.filename.startswith("ppt/media/"):
                media_count += 1

        print(f"Deck: {deck_path}")
        print(f"On-disk size: {human_size(deck_path.stat().st_size)}")
        print(f"Package entries: {len(infos)}")
        print(f"Media assets: {media_count}")
        print()
        print("Top package buckets:")
        for bucket, size in sorted(bucket_sizes.items(), key=lambda item: item[1], reverse=True):
            print(f"- {bucket:<24} {human_size(size)}")

        print()
        print(f"Top {args.top} largest parts:")
        for info in sorted(infos, key=lambda item: item.file_size, reverse=True)[: args.top]:
            print(f"- {info.filename:<70} {human_size(info.file_size)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
