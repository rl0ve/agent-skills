#!/usr/bin/env python3
"""Preview or install the AI Work Router's custom Codex agent profiles."""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import tempfile
import tomllib
from datetime import datetime, timezone
from pathlib import Path


REQUIRED_FIELDS = {"name", "description", "developer_instructions"}
SOURCE_DIR = Path(__file__).resolve().parents[1] / "assets" / "agent-profiles"
LEGACY_RENAMES = {"economy-worker": "luna-economy-worker"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_profile(path: Path) -> str:
    with path.open("rb") as handle:
        profile = tomllib.load(handle)
    missing = REQUIRED_FIELDS.difference(profile)
    if missing:
        raise ValueError(f"{path.name}: missing {', '.join(sorted(missing))}")
    name = profile["name"]
    if not isinstance(name, str) or not name:
        raise ValueError(f"{path.name}: name must be a non-empty string")
    if path.stem != name:
        raise ValueError(f"{path.name}: filename must match name {name!r}")
    return name


def atomic_copy(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary_name = tempfile.mkstemp(
        prefix=f".{destination.name}.", dir=destination.parent
    )
    os.close(handle)
    temporary = Path(temporary_name)
    try:
        shutil.copy2(source, temporary)
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Preview or install bundled Codex custom-agent profiles."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Install changed profiles. Without this flag, only show the plan.",
    )
    parser.add_argument(
        "--destination",
        type=Path,
        default=Path.home() / ".codex" / "agents",
        help="Agent profile directory (default: ~/.codex/agents).",
    )
    parser.add_argument(
        "--profile",
        action="append",
        dest="profiles",
        help="Install one named profile. Repeat for multiple profiles.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    sources = sorted(SOURCE_DIR.glob("*.toml"))
    if not sources:
        raise SystemExit(f"No profiles found in {SOURCE_DIR}")

    names = {validate_profile(path): path for path in sources}
    requested = set(args.profiles or names)
    unknown = requested.difference(names)
    if unknown:
        raise SystemExit(f"Unknown profile(s): {', '.join(sorted(unknown))}")

    destination = args.destination.expanduser().resolve()
    changes: list[tuple[Path, Path, str]] = []
    for name in sorted(requested):
        source = names[name]
        target = destination / source.name
        if not target.exists():
            status = "create"
        elif digest(source) == digest(target):
            status = "unchanged"
        else:
            status = "update"
        print(f"{status:9} {name}: {target}")
        if status != "unchanged":
            changes.append((source, target, status))

    legacy_targets: list[Path] = []
    for legacy_name, replacement_name in LEGACY_RENAMES.items():
        if replacement_name not in requested:
            continue
        legacy_target = destination / f"{legacy_name}.toml"
        if legacy_target.exists():
            print(
                f"{'retire':9} {legacy_name}: {legacy_target} "
                f"(replaced by {replacement_name})"
            )
            legacy_targets.append(legacy_target)

    if not args.apply:
        total = len(changes) + len(legacy_targets)
        print(f"Dry run: {total} profile operation(s) pending. Re-run with --apply.")
        return 0
    if not changes and not legacy_targets:
        print("All selected profiles are already current.")
        return 0

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup_dir = destination / "backups" / f"ai-work-router-{timestamp}"
    updated_targets = [target for _, target, status in changes if status == "update"]
    backup_targets = updated_targets + legacy_targets
    if backup_targets:
        backup_dir.mkdir(parents=True, exist_ok=False)
        for target in backup_targets:
            shutil.copy2(target, backup_dir / target.name)
        print(f"backup    {len(backup_targets)} profile(s): {backup_dir}")

    for source, target, _ in changes:
        atomic_copy(source, target)

    for legacy_target in legacy_targets:
        legacy_target.unlink()

    print(f"Installed {len(changes)} profile(s) into {destination}")
    if legacy_targets:
        print(f"Retired {len(legacy_targets)} renamed legacy profile(s).")
    print("Start a new Codex task to load the refreshed profiles.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
