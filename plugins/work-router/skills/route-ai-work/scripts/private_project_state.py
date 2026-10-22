#!/usr/bin/env python3
"""Initialize or inspect private local project records; never sync or publish them."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import stat
import sys


ASSETS = Path(__file__).resolve().parents[1] / "assets" / "project-state"
MAX_BYTES = 1024 * 1024
SLUG = re.compile(r"[a-z0-9][a-z0-9-]{0,79}\Z")
STATUSES = {"proposed", "assigned", "running", "returned", "needs_recheck",
            "accepted", "blocked", "superseded", "cancelled"}


def slug(value: str) -> str:
    if not SLUG.fullmatch(value):
        raise ValueError("Realm and project identifiers must be short lowercase slugs, not paths.")
    return value


def checked_path(path: Path) -> Path:
    path = Path(os.path.abspath(path.expanduser()))
    for part in (path, *path.parents):
        if part.is_symlink() or (hasattr(part, "is_junction") and part.is_junction()):
            raise ValueError("Use a canonical path without symlinks or junctions.")
        if os.path.lexists(part / ".git") or (
            (part / "HEAD").is_file() and (part / "objects").is_dir()
            and (part / "refs").is_dir()
        ):
            raise ValueError("Private state must be outside every Git checkout and bare repository.")
    return path


def inspect_entry(path: Path) -> os.stat_result:
    if hasattr(path, "is_junction") and path.is_junction():
        raise ValueError("State must not contain directory junctions.")
    info = path.lstat()
    if not (stat.S_ISDIR(info.st_mode) or stat.S_ISREG(info.st_mode)):
        raise ValueError("State contains a link or non-regular filesystem entry.")
    if stat.S_ISREG(info.st_mode) and info.st_nlink != 1:
        raise ValueError("State files must not have hard links.")
    if os.name == "posix":
        if info.st_uid != os.geteuid() or stat.S_IMODE(info.st_mode) & 0o077:
            raise ValueError("State must be owned by the current user with no group/other access.")
    return info


def read_json(path: Path) -> dict:
    info = inspect_entry(path)
    if not stat.S_ISREG(info.st_mode) or info.st_size > MAX_BYTES:
        raise ValueError("STATE.json must be a bounded regular file.")
    with path.open("rb") as handle:
        opened = os.fstat(handle.fileno())
        if (opened.st_dev, opened.st_ino) != (info.st_dev, info.st_ino):
            raise ValueError("State changed during inspection; retry from current evidence.")
        raw = handle.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError("STATE.json exceeds the size limit.")
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("STATE.json contains duplicate keys.")
            result[key] = value
        return result
    try:
        value = json.loads(raw, object_pairs_hook=unique_keys)
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise ValueError("STATE.json is not valid UTF-8 JSON.") from None
    if not isinstance(value, dict):
        raise ValueError("STATE.json must contain an object.")
    return value


def validate_record(record: dict, realm: str, project: str) -> None:
    if record.get("schema_version") != 1 or type(record.get("schema_version")) is not int:
        raise ValueError("Unsupported state schema version.")
    if record.get("realm") != realm or record.get("project_id") != project:
        raise ValueError("State belongs to a different realm or project.")
    revision = record.get("revision")
    if type(revision) is not int or revision < 0:
        raise ValueError("State revision must be a non-negative integer.")
    if "coordinator" not in record:
        raise ValueError("State must declare a coordinator or explicitly leave it null.")
    owner = record["coordinator"]
    if owner is not None and (not isinstance(owner, str) or not owner.strip()):
        raise ValueError("Coordinator must be null or a nonempty local identifier.")
    if not isinstance(record.get("updated_at"), str):
        raise ValueError("State must record an update time.")
    try:
        updated = datetime.fromisoformat(record["updated_at"].replace("Z", "+00:00"))
        if updated.tzinfo is None:
            raise ValueError
    except ValueError:
        raise ValueError("State update time must include a timezone.") from None
    if not isinstance(record.get("resources"), list):
        raise ValueError("Resources must be a list; a project may have no repositories.")
    for resource in record["resources"]:
        if not isinstance(resource, dict) or not all(
            isinstance(resource.get(key), str) and resource[key].strip()
            for key in ("kind", "reference")
        ):
            raise ValueError("Each linked resource needs a kind and private reference.")
    tasks = record.get("tasks")
    if not isinstance(tasks, list):
        raise ValueError("Tasks must be a list.")
    if tasks and owner is None:
        raise ValueError("Assign a coordinator before recording task ownership.")
    ids = set()
    for task in tasks:
        if not isinstance(task, dict) or not all(
            isinstance(task.get(key), str) and task[key].strip()
            for key in ("task_id", "attempt_id", "owner", "status")
        ):
            raise ValueError("Each task needs an ID, attempt ID, owner and status.")
        if task["task_id"] in ids:
            raise ValueError("A task has more than one current record.")
        ids.add(task["task_id"])
        if task["status"] not in STATUSES:
            raise ValueError("Unknown task state.")
        if type(task.get("input_revision")) is not int or not 0 <= task["input_revision"] <= revision:
            raise ValueError("Task input revision is missing or ahead of accepted state.")
        if not isinstance(task.get("dependencies"), list) or not all(
            isinstance(item, str) and item.strip() for item in task["dependencies"]
        ):
            raise ValueError("Task dependencies must be a list of task IDs.")
        if task["status"] == "accepted" and not all(
            isinstance(task.get(key), str) and task[key].strip()
            for key in ("result", "accepted_by")
        ):
            raise ValueError("Accepted tasks need result evidence and an acceptance owner.")
    for task in tasks:
        if task["task_id"] in task["dependencies"] or not set(task["dependencies"]) <= ids:
            raise ValueError("A task dependency is self-referential or missing.")
    pending = {task["task_id"]: set(task["dependencies"]) for task in tasks}
    while pending:
        ready = {task_id for task_id, dependencies in pending.items() if not dependencies}
        if not ready:
            raise ValueError("Task dependencies contain a cycle.")
        pending = {task_id: dependencies - ready for task_id, dependencies in pending.items()
                   if task_id not in ready}


def inspect_state(path: Path, realm: str, project: str, expected_revision: int | None = None) -> dict:
    path = checked_path(path)
    if not path.is_dir():
        raise ValueError("State directory is unavailable on this executor.")
    inspect_entry(path)
    count = 0
    for current, directories, files in os.walk(path, followlinks=False):
        for name in [*directories, *files]:
            count += 1
            if count > 10000:
                raise ValueError("State directory is too large for this bounded inspection.")
            item = Path(current) / name
            if name == ".git":
                raise ValueError("State must not contain a nested Git repository.")
            inspect_entry(item)
    for name in ("INDEX.md", "DECISIONS.md", "KNOWLEDGE.md"):
        if not (path / name).is_file():
            raise ValueError("Project record is incomplete; a required Markdown file is missing.")
    if not (path / "returns").is_dir():
        raise ValueError("Project record is incomplete; returns directory is missing.")
    record = read_json(path / "STATE.json")
    validate_record(record, realm, project)
    if expected_revision is not None and record["revision"] != expected_revision:
        raise ValueError("State revision differs from the expected revision; reconcile before proceeding.")
    return {
        "status": "local-layout-checked",
        "revision": record["revision"],
        "coordinator_assigned": record["coordinator"] is not None,
        "task_count": len(record["tasks"]),
        "git_placement": "outside-repositories",
        "permissions": "owner-only-posix" if os.name == "posix" else "acl-unverified",
        "remote_access": "not-tested",
        "sync": "not-provided",
    }


def initialize(root: Path, realm: str, project: str, apply: bool = False) -> dict:
    slug(realm)
    slug(project)
    destination = checked_path(root / realm / project)
    if destination.exists():
        raise ValueError("State already exists; inspect it instead of initializing over it.")
    if not apply:
        return {"status": "preview", "destination": str(destination), "writes": False}
    if os.name != "posix":
        raise ValueError("Automatic initialization requires POSIX permissions; use the templates with an approved Windows ACL setup.")
    if os.geteuid() == 0 or os.environ.get("SUDO_UID"):
        raise ValueError("Do not initialize project state as root or with sudo.")
    # Preflight all templates before making a private destination. No project files,
    # transcripts, credentials or environment values are copied by this command.
    templates = {name: (ASSETS / name).read_bytes()
                 for name in ("INDEX.md", "DECISIONS.md", "KNOWLEDGE.md")}
    missing = []
    parent = destination.parent
    while not parent.exists():
        missing.append(parent)
        parent = parent.parent
    for directory in reversed(missing):
        directory.mkdir(mode=0o700)
    checked_path(destination)
    destination.mkdir(mode=0o700)
    (destination / "returns").mkdir(mode=0o700)
    for name, content in templates.items():
        descriptor = os.open(destination / name, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
    record = {
        "schema_version": 1, "realm": realm, "project_id": project, "revision": 0,
        "coordinator": None, "updated_at": datetime.now(timezone.utc).isoformat(),
        "resources": [], "tasks": [],
    }
    descriptor = os.open(destination / "STATE.json", os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
        json.dump(record, handle, indent=2)
        handle.write("\n")
    result = inspect_state(destination, realm, project)
    return {**result, "status": "initialized", "destination": str(destination)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_subparsers(dest="mode", required=True)
    init = modes.add_parser("init", help="Preview or create empty private local records")
    init.add_argument("--root", type=Path, default=Path.home() / ".agent-skills" / "project-state")
    init.add_argument("--realm", required=True)
    init.add_argument("--project", required=True)
    init.add_argument("--apply", action="store_true")
    check = modes.add_parser("check", help="Read-only local placement, permission and revision inspection")
    check.add_argument("--state-dir", type=Path, required=True)
    check.add_argument("--realm", required=True)
    check.add_argument("--project", required=True)
    check.add_argument("--expected-revision", type=int)
    args = parser.parse_args(argv)
    try:
        slug(args.realm)
        slug(args.project)
        if args.mode == "init":
            result = initialize(args.root, args.realm, args.project, args.apply)
        else:
            result = inspect_state(args.state_dir, args.realm, args.project, args.expected_revision)
        print(json.dumps(result, indent=2))
        return 0
    except (OSError, ValueError, RecursionError) as error:
        # Do not include record contents, source excerpts or credential values.
        message = "State is too deeply nested for this inspection." if isinstance(error, RecursionError) else str(error)
        print(f"Project state check failed: {message}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
