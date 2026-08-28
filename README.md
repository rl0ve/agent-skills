# agent-skills

Agent skills and routers. One of them is tool-neutral and one folder is Codex-native, so
this is not a Claude-only repository — but two of the four pieces do route Claude models
and subagents, and those are Claude-specific by nature.

| Start here | If you are |
|---|---|
| [AGENTS.md](AGENTS.md) | Codex, or any agent that reads `AGENTS.md` |
| `claude plugin marketplace add rl0ve/agent-skills` | Claude Code |
| `plugins/natural-writing/skills/natural-writing/SKILL.md` | Anything else — it is plain Markdown and Python |

## Layout

Three top-level folders, because the two agents consume the same work differently.

```
.claude-plugin/     marketplace.json — how Claude Code discovers this repo. Nothing else reads it.
plugins/            the three Claude Code plugins. natural-writing sits here because that is
                    where the marketplace expects to find it, not because it needs Claude.
codex/              the Codex-native design-router, its installer, and a standalone field guide.
```

`plugins/` and `codex/` are packaging, not capability. `natural-writing` under `plugins/`
has no Claude dependency — it is Markdown, a Python linter, and 47 tests, and Codex reads it
straight from that path.

## What is in it

| | What it does | Works with |
|---|---|---|
| **Natural Writing** | Diagnoses, edits, rewrites, voice-matches, or drafts prose while preserving facts, formatting, terminology, register, and the author's voice. Ships a linter with a per-document mode and a set-level mode. | Any agent |
| **Design Router** (`codex/`) | Routes UI, UX, design-review, motion, design-to-code, and interface-copy work through a researched skill catalog and what is actually installed. | Codex |
| **Claude UI Router** | The same routing idea as a Claude Code plugin, with scout, builder, and critic subagents. Uses Natural Writing as its sole final editor for copy. | Claude Code |
| **Claude AI Work Router** | Chooses whether work stays in the parent session or moves to a bounded Haiku, Sonnet, Opus, or Fable subagent, optimizing latency and token use rather than defaulting to the largest model. | Claude Code |

The two Claude routing plugins include a deterministic `PreToolUse` hook that blocks Bash
commands containing `sudo`. The installers refuse root or `sudo` execution and never
evaluate a shell string.

## Codex

```bash
./codex/install.sh              # copy design-router into ~/.codex/skills
./codex/install.sh --dry-run    # show what it would do; no network, no third-party installs
```

Open `codex/guide/index.html` directly for the field guide. See [AGENTS.md](AGENTS.md) for
the read order and the linter commands.

## Fast local test (Claude Code)

From this directory, start a disposable session with any one plugin:

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
