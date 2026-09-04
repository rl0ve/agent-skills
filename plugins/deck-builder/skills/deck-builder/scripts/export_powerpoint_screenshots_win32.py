#!/usr/bin/env python3
from __future__ import annotations

import argparse
import platform
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export one image per slide using real Microsoft PowerPoint on Windows."
    )
    parser.add_argument("deck_path", help="Path to the input .pptx deck")
    parser.add_argument(
        "--output-dir",
        help="Directory for exported slide images. Defaults to a sibling folder next to the deck.",
    )
    parser.add_argument("--width", type=int, default=1920, help="Export width in pixels")
    parser.add_argument("--height", type=int, default=1080, help="Export height in pixels")
    parser.add_argument(
        "--format",
        default="PNG",
        choices=["PNG", "JPG"],
        help="PowerPoint export format",
    )
    parser.add_argument(
        "--keep-powerpoint-open",
        action="store_true",
        help="Leave the PowerPoint application running after export.",
    )
    return parser.parse_args()


def require_windows() -> None:
    if platform.system() != "Windows":
        raise SystemExit(
            "This script requires Windows because it exports screenshots via Microsoft PowerPoint automation."
        )


def export_slides(
    deck_path: Path,
    output_dir: Path,
    width: int,
    height: int,
    image_format: str,
    keep_powerpoint_open: bool,
) -> list[Path]:
    try:
        import pythoncom
        import win32com.client  # type: ignore[import-not-found]
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency: pywin32. Install it before using the PowerPoint screenshot pipeline."
        ) from exc

    pythoncom.CoInitialize()
    app = None
    presentation = None
    exported: list[Path] = []

    try:
        app = win32com.client.DispatchEx("PowerPoint.Application")
        app.Visible = 0
        presentation = app.Presentations.Open(str(deck_path), WithWindow=False)

        output_dir.mkdir(parents=True, exist_ok=True)
        extension = image_format.lower()

        for slide in presentation.Slides:
            index = int(slide.SlideIndex)
            out_path = output_dir / f"slide-{index:03d}.{extension}"
            slide.Export(str(out_path), image_format, width, height)
            exported.append(out_path)

        return exported
    finally:
        if presentation is not None:
            presentation.Close()
        if app is not None and not keep_powerpoint_open:
            app.Quit()
        pythoncom.CoUninitialize()


def main() -> int:
    args = parse_args()
    require_windows()

    deck_path = Path(args.deck_path).expanduser().resolve()
    if not deck_path.exists():
        print(f"File not found: {deck_path}", file=sys.stderr)
        return 2

    output_dir = (
        Path(args.output_dir).expanduser().resolve()
        if args.output_dir
        else deck_path.parent / f"{deck_path.stem}_powerpoint_exports"
    )

    exported = export_slides(
        deck_path=deck_path,
        output_dir=output_dir,
        width=args.width,
        height=args.height,
        image_format=args.format,
        keep_powerpoint_open=args.keep_powerpoint_open,
    )

    print(f"Exported {len(exported)} slide image(s) to {output_dir}")
    for path in exported:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
