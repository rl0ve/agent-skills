#!/usr/bin/env python3
"""
export_powerpoint_screenshots_mac.py
macOS screenshot export via real PowerPoint.

Uses AppleScript via `osascript` to drive real Microsoft PowerPoint for Mac,
exporting each slide as a PNG. This is the macOS equivalent of the Windows
win32com/pywin32 path — real PowerPoint renders at full fidelity, not
LibreOffice approximations.

Requirements:
  - macOS with Microsoft PowerPoint for Mac installed
  - The .pptx file must be at an absolute path readable by PowerPoint

Usage (standalone):
  python3 export_powerpoint_screenshots_mac.py /abs/path/to/deck.pptx /abs/path/to/output_folder/

Usage from Cowork mode (mcp__Control_your_Mac__osascript):
  from scripts.export_powerpoint_screenshots_mac import build_applescript
  script = build_applescript("/abs/path/to/deck.pptx", "/abs/path/to/output/")
  # then: mcp__Control_your_Mac__osascript(script=script)
  # PNGs appear in output_folder as Slide1.png, Slide2.png, ...
"""

import subprocess
import sys
from pathlib import Path


def build_applescript(pptx_path: str, output_folder: str) -> str:
    """
    Return an AppleScript string that:
      1. Opens the .pptx in Microsoft PowerPoint for Mac
      2. Exports all slides as PNG to output_folder
      3. Closes the presentation without saving

    output_folder must already exist before running.
    PowerPoint names the output files Slide1.png, Slide2.png, etc.
    """
    pptx_posix = str(Path(pptx_path).resolve())
    out_posix  = str(Path(output_folder).resolve())

    return f'''tell application "Microsoft PowerPoint"
    set pptxFile to POSIX file "{pptx_posix}"
    set outFolder to POSIX file "{out_posix}"
    open pptxFile
    set thePresentation to active presentation
    save thePresentation in outFolder as save as PNG
    close thePresentation saving no
end tell'''


def export_via_osascript(pptx_path: str, output_folder: str) -> tuple[bool, str]:
    """
    Run the AppleScript directly via the system osascript binary.
    Returns (success: bool, message: str).
    """
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    script = build_applescript(pptx_path, output_folder)
    result = subprocess.run(
        ["osascript", "-e", script],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        pngs = sorted(Path(output_folder).glob("*.png"))
        return True, f"Exported {len(pngs)} slide PNG(s) to {output_folder}"
    else:
        return False, f"AppleScript error: {result.stderr.strip()}"


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 export_powerpoint_screenshots_mac.py <deck.pptx> <output_folder>")
        sys.exit(1)

    pptx_path, output_folder = sys.argv[1], sys.argv[2]

    if not Path(pptx_path).exists():
        print(f"ERROR: file not found: {pptx_path}")
        sys.exit(1)

    print(f"Exporting: {pptx_path}")
    print(f"To folder: {output_folder}")
    print("Launching PowerPoint via AppleScript...")

    ok, msg = export_via_osascript(pptx_path, output_folder)
    print(f"{'OK' if ok else 'FAILED'}: {msg}")

    if ok:
        for p in sorted(Path(output_folder).glob("*.png")):
            print(f"  {p.name}")

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
