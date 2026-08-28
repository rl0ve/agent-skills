---
name: install-ui-stack
description: Plan or execute an explicit install of documented Claude Code UI skills from the Claude UI Router catalog. Manual only because installation changes the user's or project's skill inventory.
disable-model-invocation: true
argument-hint: "[--list | --profile NAME | --skill KEY] [--scope project|user] [--execute]"
---

# Install UI Stack

Treat `$ARGUMENTS` only as options accepted by the bundled installer. Reject unrelated shell syntax or commands.

Run:

```bash
python3 "${CLAUDE_SKILL_DIR}/../../scripts/install_optional_skills.py" $ARGUMENTS
```

Rules:

1. With no selection, list profiles and skill keys.
2. Without `--execute`, show the exact upstream sources and commands; make no changes.
3. Execute only when the user explicitly included `--execute`.
4. Never add `--yes` or `--allow-third-party-hooks` unless the user explicitly included it.
5. Never use `sudo`, run as root, or evaluate an installer command as a shell string.
6. Stop on the first failure and report what completed.
7. After installation, tell the user to restart Claude Code or run `/reload-plugins`, then verify the expected skills appear.
