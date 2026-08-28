#!/usr/bin/env python3
"""Plan or install the local Claude Router marketplace without sudo."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
from typing import Iterable


ROOT = Path(__file__).resolve().parent
MARKETPLACE_NAME = "rl0ve-agent-skills"
PLUGIN_NAMES = {
    "ai": "work-router",
    "ui": "ui-router",
    "writing": "natural-writing",
}


def refuse_elevated_execution(effective_uid: int | None = None, sudo_uid: str | None = None) -> None:
    if effective_uid is None:
        effective_uid = os.geteuid() if hasattr(os, "geteuid") else None
    if sudo_uid is None:
        sudo_uid = os.environ.get("SUDO_UID")
    if effective_uid == 0 or sudo_uid:
        raise SystemExit("Claude Router installer must not be run as root or with sudo.")


def normalize_plugins(values: Iterable[str]) -> list[str]:
    chosen: list[str] = []
    for value in values:
        keys = list(PLUGIN_NAMES) if value == "all" else [value]
        for key in keys:
            name = PLUGIN_NAMES[key]
            if name not in chosen:
                chosen.append(name)
    return chosen


def build_plan(plugins: list[str], scope: str) -> list[list[str]]:
    commands = [["claude", "plugin", "marketplace", "add", str(ROOT), "--scope", scope]]
    commands.extend(
        ["claude", "plugin", "install", f"{name}@{MARKETPLACE_NAME}", "--scope", scope]
        for name in plugins
    )
    return commands


def configured_marketplaces() -> set[str]:
    result = subprocess.run(
        ["claude", "plugin", "marketplace", "list", "--json"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return set()
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError:
        return set()
    return {item.get("name", "") for item in payload if isinstance(item, dict)}


def print_plan(commands: list[list[str]]) -> None:
    print("Claude Router install plan")
    print("Nothing runs unless --execute is supplied.\n")
    for index, command in enumerate(commands, start=1):
        print(f"{index}. {shlex.join(command)}")


def execute_plan(commands: list[list[str]]) -> None:
    if not shutil.which("claude"):
        raise SystemExit("Claude Code is not available on PATH.")
    known = configured_marketplaces()
    for index, command in enumerate(commands):
        if index == 0 and MARKETPLACE_NAME in known:
            print(f"Marketplace {MARKETPLACE_NAME} is already configured; skipping add.")
            continue
        print(f"Running: {shlex.join(command)}", flush=True)
        result = subprocess.run(command, cwd=ROOT, check=False)
        if result.returncode != 0:
            raise SystemExit(f"Command failed with exit code {result.returncode}: {shlex.join(command)}")
    print("\nInstallation complete. Restart Claude Code or run /reload-plugins.")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--plugin",
        action="append",
        choices=["ai", "ui", "writing", "all"],
        default=[],
        help="Plugin to install. Repeat as needed; default is all.",
    )
    parser.add_argument("--scope", choices=["user", "project", "local"], default="user")
    parser.add_argument("--execute", action="store_true", help="Run the printed commands.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    refuse_elevated_execution()
    args = parse_args(argv)
    plugins = normalize_plugins(args.plugin or ["all"])
    commands = build_plan(plugins, args.scope)
    print_plan(commands)
    if args.execute:
        execute_plan(commands)
    return 0


if __name__ == "__main__":
    sys.exit(main())
