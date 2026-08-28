#!/usr/bin/env python3
"""Plan or install explicitly selected Design Router dependencies.

The default behavior is read-only. Pass --execute to run the printed commands.
No command is evaluated by a shell.
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
CATALOG_PATH = ROOT / "references" / "optional-skills.json"


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


def resolve_selection(catalog: dict[str, Any], skill_keys: list[str], profiles: list[str]) -> list[dict[str, Any]]:
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


def build_command(item: dict[str, Any], agent: str, scope: str, assume_yes: bool) -> list[str]:
    installer = item["installer"]
    if installer == "skills":
        command = ["npx", "-y", "skills", "add", item["source"], "--agent", agent]
        for skill in item.get("skills", []):
            command.extend(["--skill", skill])
        if scope == "global":
            command.append("--global")
        if assume_yes:
            command.append("--yes")
        return command
    if installer == "impeccable":
        return ["npx", "-y", "impeccable", "install"]
    if installer == "codex-plugin":
        return ["codex", "plugin", "marketplace", "add", item["source"], *item.get("extra_args", [])]
    raise SystemExit(f"Unsupported installer for {item['key']}: {installer}")


def print_catalog(catalog: dict[str, Any]) -> None:
    print("Available profiles:")
    for name, keys in catalog["profiles"].items():
        print(f"  {name:<14} {', '.join(keys)}")
    print("\nInstallable skill keys:")
    for item in catalog["skills"]:
        selectors = f" [{', '.join(item.get('skills', []))}]" if item.get("skills") else ""
        print(f"  {item['key']:<24} {item['source']}{selectors}")


def print_plan(items: list[dict[str, Any]], agent: str, scope: str, assume_yes: bool) -> None:
    print(f"Plan: {len(items)} selected item(s) | agent={agent} | scope={scope}")
    print("Nothing runs unless --execute is supplied.\n")
    for number, item in enumerate(items, start=1):
        command = build_command(item, agent, scope, assume_yes)
        print(f"{number}. {item['name']} [{item['key']}]")
        print(f"   Source:  {item['url']}")
        print(f"   Why:     {item['note']}")
        print(f"   Command: {shlex.join(command)}")
        if item.get("writes_hooks"):
            print("   Gate:    writes a Codex hooks file; --allow-hooks is required")
        print()


def executable_for(command: list[str]) -> str | None:
    return shutil.which(command[0])


def execute_plan(items: list[dict[str, Any]], agent: str, scope: str, assume_yes: bool, allow_hooks: bool, project_dir: Path) -> None:
    hook_items = [item["key"] for item in items if item.get("writes_hooks")]
    if hook_items and not allow_hooks:
        raise SystemExit(
            "Selection includes a hook-writing installer "
            f"({', '.join(hook_items)}). Review its upstream source, then rerun with --allow-hooks."
        )

    missing: set[str] = set()
    commands: list[tuple[dict[str, Any], list[str]]] = []
    for item in items:
        command = build_command(item, agent, scope, assume_yes)
        commands.append((item, command))
        if not executable_for(command):
            missing.add(command[0])
    if missing:
        raise SystemExit(f"Required command(s) not found on PATH: {', '.join(sorted(missing))}")

    cwd = project_dir.resolve()
    if not cwd.is_dir():
        raise SystemExit(f"Project directory does not exist: {cwd}")

    for item, command in commands:
        print(f"Installing {item['name']} from {item['url']}", flush=True)
        result = subprocess.run(command, cwd=cwd, check=False)
        if result.returncode != 0:
            raise SystemExit(f"Install failed for {item['key']} with exit code {result.returncode}.")

    print("\nSelected installations completed.")
    if hook_items:
        print("Open /hooks in Codex, inspect the Impeccable hook, and approve it explicitly.")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="List profiles and installable skill keys.")
    parser.add_argument("--skill", action="append", default=[], metavar="KEY", help="Select one skill key. Repeat as needed.")
    parser.add_argument("--profile", action="append", default=[], metavar="NAME", help="Select a curated profile. Repeat as needed.")
    parser.add_argument("--agent", choices=["codex", "claude-code"], default="codex")
    parser.add_argument("--scope", choices=["project", "global"], default="global")
    parser.add_argument("--project-dir", type=Path, default=Path.cwd(), help="Working directory for project-scope installs.")
    parser.add_argument("--execute", action="store_true", help="Run the printed plan. Without this flag, the command is read-only.")
    parser.add_argument("--yes", action="store_true", help="Skip skills CLI confirmations. Requires --execute.")
    parser.add_argument("--allow-hooks", action="store_true", help="Allow explicitly selected installers that write Codex hooks.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    refuse_elevated_execution()
    args = parse_args(argv)
    if args.yes and not args.execute:
        raise SystemExit("--yes is valid only with --execute.")

    catalog = load_catalog()
    if args.list or (not args.skill and not args.profile):
        print_catalog(catalog)
        if not args.skill and not args.profile:
            return 0

    selected = resolve_selection(catalog, args.skill, args.profile)
    print_plan(selected, args.agent, args.scope, args.yes)
    if not args.execute:
        return 0

    execute_plan(selected, args.agent, args.scope, args.yes, args.allow_hooks, args.project_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
