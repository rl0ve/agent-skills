# agent-skills

Portable agent skills, plus two Claude Code routing plugins. Codex and other
AGENTS.md-aware agents should start at [AGENTS.md](AGENTS.md); Claude Code can add
this repo as a marketplace with `claude plugin marketplace add rl0ve/agent-skills`.

Three plugins:

- **Claude AI Work Router** chooses whether work stays in the parent session or moves to a bounded Haiku, Sonnet, Opus, or Fable subagent. It optimizes latency and token use without treating the largest model or highest effort as a default.
- **Claude UI Router 1.2.0** preserves the researched UI skill directory, chooses one design lead plus focused layers, distinguishes canonical skills from what is actually installed, and routes final prose through the separately verified Natural Writing companion.
- **Natural Writing** diagnoses, edits, rewrites, or drafts natural prose while preserving facts, formatting, terminology, register, and author voice. It is also the UI Router's sole final editor for copy.

The two routing plugins include a deterministic `PreToolUse` hook that blocks Bash commands containing `sudo`. The installers also refuse root or `sudo` execution and never evaluate a shell string.

## Fast local test

From this directory, start a disposable Claude Code session with either plugin:

```bash
claude --plugin-dir ./plugins/claude-ai-work-router
claude --plugin-dir ./plugins/claude-ui-router
claude --plugin-dir ./plugins/natural-writing
```

Then try:

```text
/claude-ai-work-router:route-ai-work review this task and choose the leanest reliable route
/claude-ui-router:route-ui-work design a B2B operations dashboard
Humanize this email and keep my voice: ...
```

## Install from the local marketplace

The installer is a plan by default:

```bash
python3 install.py --plugin all
```

Execute only after reviewing the printed commands:

```bash
python3 install.py --plugin all --execute
```

Equivalent Claude Code commands:

```bash
claude plugin marketplace add . --scope user
claude plugin install claude-ai-work-router@rlove-claude-routers --scope user
claude plugin install claude-ui-router@rlove-claude-routers --scope user
claude plugin install natural-writing@rlove-claude-routers --scope user
```

Restart Claude Code or run `/reload-plugins` after installation.

## Company-managed Claude Code

Your administrator can restrict models, effort levels, local marketplaces, and plugin enablement. The routers honor those controls. See [ADMIN.md](ADMIN.md) for the exact marketplace settings pattern to give your Claude Code administrator.

The AI router uses family aliases rather than pinning provider-specific IDs. If Fable is unavailable, its long-horizon route falls back to the newest permitted Opus family model or the inherited session model, and Claude Code reports the substitution.

## Optional UI skills

The UI router does not silently install its catalog. List or plan a curated profile:

```bash
python3 plugins/claude-ui-router/scripts/install_optional_skills.py --list
python3 plugins/claude-ui-router/scripts/install_optional_skills.py --profile product
```

Execution is explicit:

```bash
python3 plugins/claude-ui-router/scripts/install_optional_skills.py --profile product --execute
```

The same flow is available inside Claude Code through `/claude-ui-router:install-ui-stack`.

## Version boundary

The packages use the documented Claude Code plugin layout and validate with `claude plugin validate`. Model and effort aliases are intentionally policy-aware: company allowlists win. Fable requires Claude Code 2.1.170 or later and organizational access. Newer conveniences may require a newer client, but the core skills, agents, hook, and marketplace layout remain conventional.

## Icons

Each plugin bundles a square PNG icon for the website and portable package. Claude Code's current plugin manifest does not expose a rendered icon field, so the files are metadata/assets rather than a promise that `/plugin` will display artwork.
