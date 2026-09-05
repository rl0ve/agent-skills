# agent-skills

Portable agent skills, plus shared Codex and Claude Code routing plugins. Everything here is plain
Markdown and Python: no build step, no runtime, nothing to install.

## For Codex (and any agent that reads AGENTS.md)

**natural-writing** is the tool-neutral one and the reason this repo is worth reading.
It diagnoses, edits, rewrites, voice-matches, or drafts prose while preserving facts,
formatting, terminology, register, and the author's voice.

Read in this order when a task is "make this prose better":

| File | Read it when |
|---|---|
| `plugins/natural-writing/skills/natural-writing/SKILL.md` | Always first. Routing, the layered edit, output discipline. |
| `.../eval.md` | Before returning any edit. 26 checks; fix every failure you can without new facts. The last four cover spoken delivery and taste calls. |
| `.../references/pattern-catalog.md` | Every written-prose pattern by family, each table followed by a worked example per row. Read **Editing a set** before editing many pieces to one standard. |
| `.../references/spoken-register.md` | Any talk track, demo script, presenter note or narration. The spoken register, its own patterns, and the `--spoken` checks. |
| `.../references/voice-and-register.md` | Voice matching, the written registers, and the order conflicting instructions resolve in. |

Two things worth running rather than reading:

```bash
# per-document scan: named patterns, em-dash density, sentence-shape runs,
# flat-declarative runs, stacked precision. Frequency rules report once with a
# count; headings, lists, tables and code are skipped by the sentence checks.
python3 plugins/natural-writing/skills/natural-writing/scripts/lint_natural_writing.py DRAFT.md

# spoken scan: adds the three checks that only make sense out loud
python3 .../scripts/lint_natural_writing.py --spoken SCRIPT.md

# set-level scan: blank-line separated pieces measured against EACH OTHER.
# Flags any opening word, closing pair, or connective shared by more than a fifth
# of the set. Run this AFTER an edit pass over many pieces - it catches what your
# own fix installed, which is invisible from inside any single piece.
python3 .../scripts/lint_natural_writing.py --set PIECES.md
```

Treat every match as a review prompt, not a verdict. Patterns are evidence in clusters.

Tests: `cd plugins/natural-writing/skills/natural-writing && python3 -m unittest discover -s tests` (linter behaviour, plus structure tests that keep the catalog, examples, lint map and forward cases naming the same rows)

## Install from this repo

Codex reads `.agents/plugins/marketplace.json`, so this repo is a Codex marketplace:

```bash
codex plugin marketplace add rl0ve/agent-skills
codex plugin add natural-writing@rl0ve-agent-skills
codex plugin add ui-router@rl0ve-agent-skills
codex plugin add work-router@rl0ve-agent-skills
```

All three are shared plugins rather than Codex ports: one folder, one `skills/` directory,
a `.codex-plugin` and a `.claude-plugin` side by side. `work-router` carries a route table
for each agent under `## Default routes` - read the one matching the agent you are running
as. `ui-router`'s optional-skill catalog carries `installer_codex` where the install command
differs.

`plugins/ui-router/scripts/install-into-codex-skills.sh` is the no-marketplace path, and
`plugins/ui-router/docs/field-guide.html` is a standalone field guide.

## For Claude Code

This repo is also a plugin marketplace.

```bash
claude plugin marketplace add rl0ve/agent-skills
claude plugin install natural-writing@rl0ve-agent-skills
```

`work-router` and `ui-router` are shared plugins with host-specific guidance.
For Codex model decisions, use the Astra-aware Codex table in
`plugins/work-router/skills/route-ai-work/SKILL.md`; historical source packs do not
override it. `natural-writing` also stands alone.

## Conventions

- Skills are `plugins/<plugin>/skills/<skill>/SKILL.md` with frontmatter.
- Versions live in both `plugins/<plugin>/.claude-plugin/plugin.json` and
  `plugins/<plugin>/.codex-plugin/plugin.json`, plus `.claude-plugin/marketplace.json`.
  Keep all three aligned and add a `CHANGELOG.md` entry.
- The routing plugins ship a deterministic `PreToolUse` hook that blocks Bash
  commands containing `sudo`. Installers refuse root and never evaluate a shell string.
