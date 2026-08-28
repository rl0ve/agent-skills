#!/usr/bin/env python3
"""Install AI Work Router, its custom agents, and managed personalization."""

from __future__ import annotations

import argparse
import json
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


PLUGIN_NAME = "ai-work-router"
MARKETPLACE_NAME = "ai-work-router-portable"
PLUGIN_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = PLUGIN_ROOT.parents[1]
MARKETPLACE_FILE = PACKAGE_ROOT / ".agents" / "plugins" / "marketplace.json"
PERSONALIZATION_FILE = PACKAGE_ROOT / "PERSONALIZATION.md"
PROFILE_INSTALLER = (
    PLUGIN_ROOT
    / "skills"
    / "route-ai-work"
    / "scripts"
    / "sync_agent_profiles.py"
)
MANAGED_START = "<!-- ai-work-router personalization:begin -->"
MANAGED_END = "<!-- ai-work-router personalization:end -->"
LEGACY_PERSONALIZATION = """Prioritize total wall-clock latency first, quality second, and cost third.

Before substantial delegated work, announce:
Route: <agent> (<model>, <effort>) - <reason>

Prefer:
- luna-builder for defined implementation
- sol-advisor for fast judgment and initial diagnosis
- sol-architect for architecture and deep investigation
- sol-critical only for critical or previously failed work

Do not spawn subagents for trivial work. Use only one write-capable agent per working tree."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Install AI Work Router, its six Codex agent profiles, and its "
            "managed personalization block."
        )
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Check the bundle and show the plan without changing anything.",
    )
    parser.add_argument(
        "--skip-personalization",
        action="store_true",
        help="Install the plugin and profiles without changing Codex personalization.",
    )
    parser.add_argument(
        "--agent-destination",
        type=Path,
        help="Override the agent-profile destination (mainly useful for testing).",
    )
    parser.add_argument(
        "--personalization-destination",
        type=Path,
        default=Path.home() / ".codex" / "AGENTS.md",
        help="Personalization file (default: ~/.codex/AGENTS.md).",
    )
    return parser.parse_args()


def find_codex() -> Path:
    configured = os.environ.get("AI_WORK_ROUTER_CODEX_BIN")
    discovered = shutil.which("codex")
    candidates = [
        Path(configured).expanduser() if configured else None,
        Path(discovered) if discovered else None,
        Path("/Applications/ChatGPT.app/Contents/Resources/codex"),
        Path("/Applications/Codex.app/Contents/Resources/codex"),
    ]
    for candidate in candidates:
        if candidate and candidate.is_file() and os.access(candidate, os.X_OK):
            return candidate.resolve()
    raise SystemExit(
        "Could not find the Codex command. Install the Codex desktop app, or set "
        "AI_WORK_ROUTER_CODEX_BIN to the full path of the codex executable."
    )


def validate_bundle() -> None:
    required = [MARKETPLACE_FILE, PROFILE_INSTALLER, PERSONALIZATION_FILE]
    missing = [path for path in required if not path.is_file()]
    if missing:
        raise SystemExit(f"Missing bundle file: {missing[0]}")
    try:
        marketplace = json.loads(MARKETPLACE_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Invalid marketplace file: {exc}") from exc
    if marketplace.get("name") != MARKETPLACE_NAME:
        raise SystemExit(
            f"Marketplace name must be {MARKETPLACE_NAME!r}, found "
            f"{marketplace.get('name')!r}."
        )
    if not PERSONALIZATION_FILE.read_text(encoding="utf-8").strip():
        raise SystemExit("The bundled personalization is empty.")


def display_command(arguments: list[str | Path]) -> str:
    return shlex.join(str(value) for value in arguments)


def run_checked(arguments: list[str | Path]) -> None:
    command = [str(value) for value in arguments]
    print(f"\n> {display_command(arguments)}", flush=True)
    completed = subprocess.run(command, check=False)
    if completed.returncode:
        raise SystemExit(
            f"Command failed with exit code {completed.returncode}: "
            f"{display_command(arguments)}"
        )


def add_marketplace(arguments: list[str | Path]) -> None:
    command = [str(value) for value in arguments]
    print(f"\n> {display_command(arguments)}", flush=True)
    try:
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=120,
        )
    except subprocess.TimeoutExpired as exc:
        raise SystemExit(
            "Codex did not finish registering the marketplace within two minutes. "
            "Quit any other Codex installation or update process, then try again."
        ) from exc

    if completed.stdout:
        print(completed.stdout.rstrip())
    if completed.stderr:
        print(completed.stderr.rstrip(), file=sys.stderr)
    if completed.returncode == 0:
        return

    message = f"{completed.stdout}\n{completed.stderr}".lower()
    duplicate_markers = ("already configured", "already exists", "already added")
    if any(marker in message for marker in duplicate_markers):
        print(f"Marketplace {MARKETPLACE_NAME!r} is already registered; continuing.")
        return
    raise SystemExit(
        f"Command failed with exit code {completed.returncode}: "
        f"{display_command(arguments)}"
    )


def merge_personalization(existing: str, body: str) -> str:
    managed = f"{MANAGED_START}\n{body.strip()}\n{MANAGED_END}"
    start_index = existing.find(MANAGED_START)
    end_index = existing.find(MANAGED_END)
    if (start_index == -1) != (end_index == -1):
        raise SystemExit(
            "The existing personalization contains only one AI Work Router marker. "
            "Repair or remove that incomplete managed block, then rerun the installer."
        )
    if start_index != -1:
        if end_index < start_index:
            raise SystemExit("The AI Work Router personalization markers are out of order.")
        end_index += len(MANAGED_END)
        merged = existing[:start_index] + managed + existing[end_index:]
        return merged.strip() + "\n"

    recommended = body.strip()
    if recommended in existing:
        merged = existing.replace(recommended, managed, 1)
        return merged.strip() + "\n"
    if LEGACY_PERSONALIZATION in existing:
        merged = existing.replace(LEGACY_PERSONALIZATION, managed, 1)
        return merged.strip() + "\n"
    if not existing.strip():
        return managed + "\n"
    return existing.rstrip() + "\n\n" + managed + "\n"


def personalization_plan(destination: Path) -> tuple[str, str, str]:
    destination = destination.expanduser()
    existing = destination.read_text(encoding="utf-8") if destination.exists() else ""
    body = PERSONALIZATION_FILE.read_text(encoding="utf-8")
    merged = merge_personalization(existing, body)
    if not destination.exists():
        status = "create"
    elif merged == existing:
        status = "unchanged"
    else:
        status = "update"
    return existing, merged, status


def install_personalization(destination: Path) -> None:
    destination = destination.expanduser()
    existing, merged, status = personalization_plan(destination)
    print(f"{status:9} personalization: {destination}")
    if status == "unchanged":
        return

    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        backup_dir = (
            destination.parent
            / "backups"
            / f"ai-work-router-personalization-{timestamp}"
        )
        backup_dir.mkdir(parents=True, exist_ok=False)
        backup = backup_dir / destination.name
        shutil.copy2(destination, backup)
        print(f"backup    personalization: {backup}")

    handle, temporary_name = tempfile.mkstemp(
        prefix=f".{destination.name}.", dir=destination.parent
    )
    os.close(handle)
    temporary = Path(temporary_name)
    try:
        temporary.write_text(merged, encoding="utf-8")
        if destination.exists():
            shutil.copymode(destination, temporary)
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)


def main() -> int:
    args = parse_args()
    validate_bundle()
    codex = find_codex()

    marketplace_command: list[str | Path] = [
        codex,
        "plugin",
        "marketplace",
        "add",
        PACKAGE_ROOT,
    ]
    plugin_command: list[str | Path] = [
        codex,
        "plugin",
        "add",
        f"{PLUGIN_NAME}@{MARKETPLACE_NAME}",
    ]
    profile_command: list[str | Path] = [sys.executable, PROFILE_INSTALLER, "--apply"]
    if args.agent_destination:
        profile_command.extend(["--destination", args.agent_destination])

    print("AI Work Router portable installer")
    print(f"Codex command: {codex}")
    print(f"Package: {PACKAGE_ROOT}")

    if args.dry_run:
        print(f"Would run: {display_command(marketplace_command)}")
        print(f"Would run: {display_command(plugin_command)}")
        preview_command = [value for value in profile_command if value != "--apply"]
        print(f"\nProfile preview: {display_command(preview_command)}")
        sys.stdout.flush()
        profile_status = subprocess.run(
            [str(value) for value in preview_command], check=False
        ).returncode
        if not args.skip_personalization:
            _, _, status = personalization_plan(args.personalization_destination)
            print(
                f"{status:9} personalization: "
                f"{args.personalization_destination.expanduser()}"
            )
        else:
            print("skip      personalization")
        return profile_status

    add_marketplace(marketplace_command)
    run_checked(plugin_command)
    run_checked(profile_command)
    if args.skip_personalization:
        print("skip      personalization")
    else:
        install_personalization(args.personalization_destination)

    print("\nAI Work Router is installed with all six agent profiles.")
    if not args.skip_personalization:
        print("The managed AI Work Router personalization is installed.")
    print("Quit and reopen Codex, then start a new task.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
