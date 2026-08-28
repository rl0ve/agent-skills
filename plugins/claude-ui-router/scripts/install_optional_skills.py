#!/usr/bin/env python3
"""Plan or install explicitly selected Claude UI Router dependencies.

The default behavior is read-only. Pass --execute to run the printed commands.
Commands are passed to subprocess as argument arrays and are never evaluated by a shell.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "skills" / "route-ui-work" / "references" / "optional-skills.json"


def refuse_elevated_execution(effective_uid: int | None = None, sudo_uid: str | None = None) -> None:
    if effective_uid is None:
        effective_uid = os.geteuid() if hasattr(os, "geteuid") else None
    if sudo_uid is None:
        sudo_uid = os.environ.get("SUDO_UID")
    if effective_uid == 0 or sudo_uid:
        raise SystemExit("Optional skill installer must not be run as root or with sudo.")


def load_catalog(path: Path = CATALOG_PATH) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def skill_index(catalog: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["key"]: item for item in catalog["skills"]}


def resolve_selection(
    catalog: dict[str, Any], skill_keys: list[str], profiles: list[str]
) -> list[dict[str, Any]]:
    index = skill_index(catalog)
    unknown_skills = sorted(set(skill_keys) - set(index))
    unknown_profiles = sorted(set(profiles) - set(catalog["profiles"]))
    if unknown_skills:
        raise SystemExit(f"Unknown skill key(s): {', '.join(unknown_skills)}")
    if unknown_profiles:
        raise SystemExit(f"Unknown profile(s): {', '.join(unknown_profiles)}")

    ordered_keys: list[str] = []
    for profile in profiles:
        ordered_keys.extend(catalog["profiles"][profile])
    ordered_keys.extend(skill_keys)

    seen: set[str] = set()
    selected: list[dict[str, Any]] = []
    for key in ordered_keys:
        if key not in seen:
            selected.append(index[key])
            seen.add(key)
    return selected


def build_command(
    item: dict[str, Any], scope: str, assume_yes: bool, allow_third_party_hooks: bool
) -> list[str]:
    installer = item["installer"]
    if installer == "skills":
        command = ["npx", "-y", "skills", "add", item["source"], "--agent", "claude-code"]
        for skill in item.get("skills", []):
            command.extend(["--skill", skill])
        if scope == "user":
            command.append("--global")
        if assume_yes:
            command.append("--yes")
        return command
    if installer == "impeccable":
        if allow_third_party_hooks:
            return ["npx", "-y", "impeccable", "install"]
        return ["npx", "-y", "impeccable", "skills", "install"]
    raise SystemExit(f"Unsupported installer for {item['key']}: {installer}")


def print_catalog(catalog: dict[str, Any]) -> None:
    print("Available profiles:")
    for name, keys in catalog["profiles"].items():
        print(f"  {name:<14} {', '.join(keys)}")
    print("\nInstallable skill keys:")
    for item in catalog["skills"]:
        selectors = f" [{', '.join(item.get('skills', []))}]" if item.get("skills") else ""
        print(f"  {item['key']:<24} {item['source']}{selectors}")


def print_plan(
    items: list[dict[str, Any]], scope: str, assume_yes: bool, allow_third_party_hooks: bool
) -> None:
    print(f"Plan: {len(items)} selected item(s) | agent=claude-code | scope={scope}")
    print("Nothing runs unless --execute is supplied.\n")
    for number, item in enumerate(items, start=1):
        command = build_command(item, scope, assume_yes, allow_third_party_hooks)
        print(f"{number}. {item['name']} [{item['key']}]")
        print(f"   Source:  {item['url']}")
        print(f"   Why:     {item['note']}")
        print(f"   Command: {shlex.join(command)}")
        if item.get("writes_hooks"):
            state = "enabled by explicit flag" if allow_third_party_hooks else "disabled; skills-only install"
            print(f"   Hooks:   {state}")
        print()


def execute_plan(
    items: list[dict[str, Any]],
    scope: str,
    assume_yes: bool,
    allow_third_party_hooks: bool,
    project_dir: Path,
) -> None:
    commands = [
        (item, build_command(item, scope, assume_yes, allow_third_party_hooks)) for item in items
    ]
    missing = sorted({command[0] for _, command in commands if not shutil.which(command[0])})
    if missing:
        raise SystemExit(f"Required command(s) not found on PATH: {', '.join(missing)}")

    cwd = project_dir.resolve()
    if not cwd.is_dir():
        raise SystemExit(f"Project directory does not exist: {cwd}")

    completed: list[str] = []
    for item, command in commands:
        print(f"Installing {item['name']} from {item['url']}", flush=True)
        result = subprocess.run(command, cwd=cwd, check=False)
        if result.returncode != 0:
            done = ", ".join(completed) if completed else "none"
            raise SystemExit(
                f"Install failed for {item['key']} with exit code {result.returncode}. Completed: {done}."
            )
        completed.append(item["key"])

    print("\nSelected installations completed.")
    print("Restart Claude Code or run /reload-plugins, then verify the expected skills are listed.")
    if allow_third_party_hooks:
        print("Review the Impeccable hook in /hooks before relying on it.")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="List profiles and installable skill keys.")
    parser.add_argument("--skill", action="append", default=[], metavar="KEY", help="Select one skill key.")
    parser.add_argument("--profile", action="append", default=[], metavar="NAME", help="Select a profile.")
    parser.add_argument("--scope", choices=["project", "user"], default="user")
    parser.add_argument("--project-dir", type=Path, default=Path.cwd())
    parser.add_argument("--execute", action="store_true", help="Run the printed plan.")
    parser.add_argument("--yes", action="store_true", help="Skip skills CLI confirmations; requires --execute.")
    parser.add_argument(
        "--allow-third-party-hooks",
        action="store_true",
        help="Allow the Impeccable installer to offer its own Claude Code hook.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    refuse_elevated_execution()
    args = parse_args(argv)
    if args.yes and not args.execute:
        raise SystemExit("--yes is valid only with --execute.")
    if args.allow_third_party_hooks and not args.execute:
        raise SystemExit("--allow-third-party-hooks is valid only with --execute.")

    catalog = load_catalog()
    if args.list or (not args.skill and not args.profile):
        print_catalog(catalog)
        if not args.skill and not args.profile:
            return 0

    selected = resolve_selection(catalog, args.skill, args.profile)
    print_plan(selected, args.scope, args.yes, args.allow_third_party_hooks)
    if args.execute:
        execute_plan(
            selected,
            args.scope,
            args.yes,
            args.allow_third_party_hooks,
            args.project_dir,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
