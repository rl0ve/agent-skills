#!/usr/bin/env python3
"""Deny Claude Code Bash tool calls that contain a sudo executable."""

from __future__ import annotations

import json
import re
import sys
from typing import Any


SUDO_PATTERN = re.compile(r"(?<![A-Za-z0-9_-])(?:/[A-Za-z0-9_./-]+/)?sudo(?=$|[\s;&|()])")


def decision_for(payload: dict[str, Any]) -> dict[str, Any] | None:
    if payload.get("tool_name") != "Bash":
        return None
    tool_input = payload.get("tool_input")
    if not isinstance(tool_input, dict):
        raise ValueError("Bash hook payload is missing tool_input")
    command = tool_input.get("command", "")
    if not isinstance(command, str):
        raise ValueError("Bash hook command is not a string")
    if not SUDO_PATTERN.search(command):
        return None
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                "This router disallows sudo. Use an unprivileged command or ask the user or administrator "
                "to perform the privileged step outside Claude Code."
            ),
        }
    }


def main() -> int:
    try:
        payload = json.load(sys.stdin)
        decision = decision_for(payload)
    except (json.JSONDecodeError, TypeError, ValueError) as exc:
        print(f"Unable to inspect Bash command safely: {exc}", file=sys.stderr)
        return 2
    if decision is not None:
        print(json.dumps(decision))
    return 0


if __name__ == "__main__":
    sys.exit(main())
