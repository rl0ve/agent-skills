#!/usr/bin/env python3
"""Preview, check or explicitly apply a portable user preference profile."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile


PROFILE_ROOT = Path(__file__).resolve().parents[1] / "assets" / "user-preferences"
HOSTS = ("codex", "claude-code")
MARKER = re.compile(rb"<!-- work-router ([a-z][a-z-]*):(begin|end) -->")
MARKER_LIKE = re.compile(rb"<!--[ \t]*work-router\b[^\r\n]*?(?:-->|(?=\r?$))", re.IGNORECASE | re.MULTILINE)
MAX_BYTES = 1024 * 1024


def refuse_elevated_execution() -> None:
    if (hasattr(os, "geteuid") and os.geteuid() == 0) or os.environ.get("SUDO_UID"):
        raise ValueError("Do not run preference setup as root or with sudo.")


def regular_bytes(path: Path) -> bytes:
    info = path.lstat()
    if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
        raise ValueError(f"Expected a regular, non-linked file: {path}")
    if info.st_size > MAX_BYTES:
        raise ValueError(f"Instruction/profile file exceeds {MAX_BYTES} bytes: {path}")
    value = path.read_bytes()
    value.decode("utf-8")
    return value


def safe_path(path: Path) -> Path:
    # Do not resolve away a symlink before checking it. Use an explicit canonical
    # destination when a host deliberately keeps instructions in a linked folder.
    path = Path(os.path.abspath(path.expanduser()))
    for item in (path, *path.parents):
        if item.is_symlink():
            raise ValueError(f"Refusing linked instruction/backup path: {item}")
    parent = path.parent
    while not parent.exists():
        parent = parent.parent
    if not parent.is_dir():
        raise ValueError(f"Output parent must be a real directory: {parent}")
    return path


def default_destination(host: str) -> Path:
    if host == "codex":
        home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex").expanduser()
        override = home / "AGENTS.override.md"
        if (override.exists() or override.is_symlink()) and regular_bytes(override).strip():
            return override
        return home / "AGENTS.md"
    home = Path(os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude").expanduser()
    return home / "CLAUDE.md"


def block_spans(content: bytes) -> dict[str, tuple[int, int]]:
    for candidate in MARKER_LIKE.finditer(content):
        if not MARKER.fullmatch(candidate.group()):
            raise ValueError("Malformed Work Router marker; repair it before setup.")
    spans: dict[str, tuple[int, int]] = {}
    opened: tuple[str, int] | None = None
    for match in MARKER.finditer(content):
        name, action = (part.decode() for part in match.groups())
        if action == "begin":
            if opened or name in spans:
                raise ValueError(f"Nested or duplicate Work Router block: {name}")
            opened = (name, match.start())
        elif not opened or opened[0] != name:
            raise ValueError(f"Unmatched Work Router end marker: {name}")
        else:
            spans[name] = (opened[1], match.end())
            opened = None
    if opened:
        raise ValueError(f"Unclosed Work Router block: {opened[0]}")
    return spans


def load_profile(name: str, host: str) -> tuple[dict, dict[str, bytes]]:
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", name):
        raise ValueError("Profile must be a name, not a path.")
    folder = PROFILE_ROOT / name
    if folder.is_symlink():
        raise ValueError("Profile directory must not be a symlink.")
    metadata = json.loads(regular_bytes(folder / "profile.json"))
    if not isinstance(metadata, dict) or metadata.get("schema_version") != 1 or metadata.get("name") != name:
        raise ValueError("Invalid preference profile schema/name.")
    if type(metadata.get("revision")) is not int or metadata["revision"] < 1:
        raise ValueError("Profile revision must be a positive integer.")
    files = metadata.get("hosts", {}).get(host)
    if not isinstance(files, list) or not files:
        raise ValueError(f"Profile has no {host} instruction template.")
    blocks: dict[str, bytes] = {}
    for filename in files:
        if not isinstance(filename, str) or not re.fullmatch(r"[a-z0-9-]+\.md", filename):
            raise ValueError("Profile template must be a local Markdown filename.")
        content = regular_bytes(folder / filename).replace(b"\r\n", b"\n").replace(b"\r", b"\n").strip()
        spans = block_spans(content)
        if len(spans) != 1 or next(iter(spans.values())) != (0, len(content)):
            raise ValueError(f"Template must contain one bounded block: {filename}")
        key = next(iter(spans))
        if key in blocks:
            raise ValueError(f"Profile repeats a block: {key}")
        blocks[key] = content
    return metadata, blocks


def merge_blocks(original: bytes, blocks: dict[str, bytes], remove: bool = False) -> bytes:
    original.decode("utf-8")
    spans = block_spans(original)
    result = original
    newline = b"\r\n" if b"\r\n" in original and b"\n" not in original.replace(b"\r\n", b"") else b"\n"
    replacements = []
    for key, content in blocks.items():
        if key in spans:
            start, end = spans[key]
            replacements.append((start, end, b"" if remove else content.replace(b"\n", newline)))
    for start, end, content in sorted(replacements, reverse=True):
        result = result[:start] + content + result[end:]
    if not remove:
        for key, content in blocks.items():
            if key not in spans:
                if result and not result.endswith(newline):
                    result += newline
                if result and not result.endswith(newline * 2):
                    result += newline
                result += content.replace(b"\n", newline) + newline
    if len(result) > MAX_BYTES:
        raise ValueError("Result exceeds the instruction-file safety limit.")
    return result


def apply_change(path: Path, original: bytes, updated: bytes, existed: bool,
                 backup_directory: Path | None = None) -> Path | None:
    if original == updated:
        return None
    safe_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    safe_path(path)
    current = regular_bytes(path) if path.exists() else b""
    if path.exists() != existed or current != original:
        raise ValueError("Instructions changed after preview; inspect and retry.")
    mode = stat.S_IMODE(path.stat().st_mode) if existed else 0o600
    backup: Path | None = None
    # Backups are outside instruction/agent discovery and contain the entire
    # private original. Never print their contents or copy them into a repository.
    if existed:
        backup_root = safe_path((backup_directory or Path.home() / ".agent-skills" / "preference-backups") / "placeholder").parent
        backup_root.mkdir(mode=0o700, parents=True, exist_ok=True)
        descriptor, backup_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".bak", dir=backup_root)
        backup = Path(backup_name)
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(original)
            handle.flush()
            os.fsync(handle.fileno())
    descriptor, temporary_name = tempfile.mkstemp(prefix="." + path.name + ".", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(updated)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, mode)
        safe_path(path)
        if path.exists() != existed or (regular_bytes(path) if path.exists() else b"") != original:
            raise ValueError("Instructions changed during setup; original preserved.")
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)
    return backup


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True, help="Explicitly selected profile, e.g. rl0ve.")
    parser.add_argument("--host", required=True, choices=HOSTS)
    parser.add_argument("--destination", type=Path, help="Explicit instruction file; may affect everyone loading that project file.")
    parser.add_argument("--backup-dir", type=Path, help="Private backup directory (default: ~/.agent-skills/preference-backups); keep outside shared repositories.")
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--apply", action="store_true", help="Apply this user-selected preference; not implied by plugin installation.")
    action.add_argument("--check", action="store_true", help="Exit 1 on drift; never write.")
    action.add_argument("--print", dest="print_profile", action="store_true", help="Print only the selected profile for review or a host instruction surface.")
    parser.add_argument("--remove", action="store_true", help="Remove only selected managed blocks; preview unless --apply is set.")
    args = parser.parse_args(argv)
    try:
        refuse_elevated_execution()
        metadata, blocks = load_profile(args.profile, args.host)
        if args.print_profile:
            if args.remove:
                raise ValueError("--print and --remove cannot be combined.")
            print(b"\n\n".join(blocks.values()).decode())
            return 0
        path = safe_path(args.destination or default_destination(args.host))
        if args.host == "codex" and path.name == "AGENTS.md":
            override = path.with_name("AGENTS.override.md")
            if (override.exists() or override.is_symlink()) and regular_bytes(override).strip():
                raise ValueError(f"This file is shadowed by {override}; select that file explicitly or use the default destination.")
        existed = path.exists()
        original = regular_bytes(path) if existed else b""
        updated = merge_blocks(original, blocks, args.remove)
        operation = "remove" if args.remove else "apply"
        changed = updated != original
        print(f"Profile: {args.profile} revision {metadata['revision']}; host: {args.host}")
        print(f"Destination: {path}")
        print(f"Managed blocks: {', '.join(blocks)}; {operation}: {'pending' if changed else 'current'}")
        print("Only managed blocks change; unrelated instructions remain byte-identical.")
        if args.check:
            return int(changed)
        if not args.apply:
            print("Dry run: no files changed. Use --print to review the profile, then --apply to install it.")
            return 0
        backup = apply_change(path, original, updated, existed, args.backup_dir)
        if backup:
            print(f"Private backup: {backup}")
        print(f"Instruction SHA-256: {hashlib.sha256(updated).hexdigest()}")
        print("Applied" if changed else "Already current")
        print("Start a fresh session and verify loaded instructions. This does not change models, tiers, plugins or other machines.")
        return 0
    except (OSError, ValueError, KeyError) as error:
        print(f"Preference setup: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
