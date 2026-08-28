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

Two manifests over **one** plugin tree. Every plugin here is installable by both agents, so
every plugin is one folder with one `skills/` directory and a `.claude-plugin` and
`.codex-plugin` beside each other carrying the same name and version. No plugin is named
after an agent, because none of them belongs to one.

```
.claude-plugin/marketplace.json    Claude Code discovery
.agents/plugins/marketplace.json   Codex discovery
plugins/
  natural-writing/   .claude-plugin/ + .codex-plugin/
  ui-router/         .claude-plugin/ + .codex-plugin/
  work-router/       .claude-plugin/ + .codex-plugin/
```

Where the two agents genuinely differ, the difference is carried inside the shared file
rather than by forking it: `work-router` has one method and two route tables, and
`ui-router`'s catalog carries `installer_codex` for the two skills whose install command is
not the same on both.

## What is in it

| | What it does |
|---|---|
| **Natural Writing** | Diagnoses, edits, rewrites, voice-matches, or drafts prose while preserving facts, formatting, terminology, register, and the author's voice. Ships a linter with a per-document mode and a set-level mode. |
| **UI Router** | Routes UI, UX, design-review, motion, design-to-code, and interface-copy work through a researched skill catalog and what is actually installed. Uses Natural Writing as its sole final editor for copy. |
| **Work Router** | Chooses whether work stays in the parent session or moves to a bounded subagent, on task shape, ambiguity, risk, latency and token use rather than defaulting to the largest model. One method, with a route table for each agent. |

All three install in Claude Code and Codex. The routers ship a deterministic hook that blocks
Bash commands containing `sudo`; the installers refuse root or `sudo` execution and never
evaluate a shell string.

## Install

```bash
# Claude Code
claude plugin marketplace add rl0ve/agent-skills
claude plugin install ui-router@rl0ve-agent-skills

# Codex
codex plugin marketplace add rl0ve/agent-skills
codex plugin add ui-router@rl0ve-agent-skills
```

Swap `ui-router` for `natural-writing` or `work-router`. If you would rather not add a
marketplace, `plugins/ui-router/scripts/install-into-codex-skills.sh` copies the routing
skill straight into `~/.codex/skills`, and `plugins/ui-router/docs/field-guide.html` opens
standalone.

## Fast local test (Claude Code)

From this directory, start a disposable session with any one plugin:

```bash
claude --plugin-dir ./plugins/work-router
claude --plugin-dir ./plugins/ui-router
claude --plugin-dir ./plugins/natural-writing
```

Then try:

```text
/work-router:route-ai-work review this task and choose the leanest reliable route
/ui-router:route-ui-work design a B2B operations dashboard
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
claude plugin install work-router@rl0ve-agent-skills --scope user
claude plugin install ui-router@rl0ve-agent-skills --scope user
claude plugin install natural-writing@rl0ve-agent-skills --scope user
```

Restart Claude Code or run `/reload-plugins` after installation.

## Company-managed Claude Code

Your administrator can restrict models, effort levels, local marketplaces, and plugin enablement. The routers honor those controls. See [ADMIN.md](ADMIN.md) for the exact marketplace settings pattern to give your Claude Code administrator.

The AI router uses family aliases rather than pinning provider-specific IDs. If Fable is unavailable, its long-horizon route falls back to the newest permitted Opus family model or the inherited session model, and Claude Code reports the substitution.

## Optional UI skills

The UI router does not silently install its catalog. List or plan a curated profile:

```bash
python3 plugins/ui-router/scripts/install_optional_skills.py --list
python3 plugins/ui-router/scripts/install_optional_skills.py --profile product
```

Execution is explicit:

```bash
python3 plugins/ui-router/scripts/install_optional_skills.py --profile product --execute
```

The same flow is available inside Claude Code through `/ui-router:install-ui-stack`.

## Version boundary

The packages use the documented Claude Code plugin layout and validate with `claude plugin validate`. Model and effort aliases are intentionally policy-aware: company allowlists win. Fable requires Claude Code 2.1.170 or later and organizational access. Newer conveniences may require a newer client, but the core skills, agents, hook, and marketplace layout remain conventional.

## Icons

Each plugin bundles a square PNG icon for the website and portable package. Claude Code's current plugin manifest does not expose a rendered icon field, so the files are metadata/assets rather than a promise that `/plugin` will display artwork.
