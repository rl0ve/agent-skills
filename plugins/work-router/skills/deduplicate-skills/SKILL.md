---
name: deduplicate-skills
description: Audit and consolidate duplicate or overlapping installed skills across Codex. Use for skill cleanup, competing routers, repeated skill names, or duplicate plugins; distinguish exact copies, variants, complementary specialists and inactive remnants before proposing or applying scoped changes.
---

# Deduplicate skills

Own installed-skill consolidation across domains. Work Router owns execution choices;
`discover-capabilities` owns finding missing capabilities. Do not start a global audit
on ordinary work or install another router to solve an overlap. This skill's inventory
helper is read-only; cleanup is a separate, explicitly scoped action.

## Inventory what Codex can use

Check the current session's skill list, the current host's installed/enabled plugin
inventory, user and relevant project skill roots, and skill-disable configuration.
Keep file presence, installed version, plugin enablement, skill enablement and actual
session visibility separate. A source checkout, marketplace listing or older cache
version is not another active skill. Do not claim a clean global inventory from only
the current project's list.

Use the current Codex executable, not an older CLI found first on PATH. Inspect its
help if needed. A current host supports `codex plugin list --json`; save the result to
a private temporary file and check stderr for partial catalog failures. Do not dump
the full user configuration or credentials into a report. The helper reads only skill
disable entries from a supplied TOML config, using Python 3.11 or newer:

```bash
python3 scripts/inventory_skills.py \
  --root user-agents=/absolute/user/.agents/skills \
  --root user-codex=/absolute/user/.codex/skills \
  --root project=/absolute/project/.agents/skills \
  --plugin-list /private/temporary/plugins.json \
  --codex-home /absolute/user/.codex \
  --config /absolute/user/.codex/config.toml \
  --output /private/temporary/skill-inventory.json
```

Paths above are examples; resolve the user's actual host and scope. Include applicable
ancestor/project roots and bundled/system roots found on that host. The helper scans
explicit roots and the listed plugins' exact versions, resolves symlink aliases, and
compares names, entrypoints and bounded local bundle fingerprints. It never chooses
the newest cache folder, runs skill scripts, edits config or removes files. Missing
roots, unsupported manifests and incomplete reads remain coverage limits. Inspect the
report's warnings before drawing conclusions; it cannot observe prompt-time loading.
The helper reads only the supplied config file; inspect applicable project, profile
and managed overrides before treating a disable-rule match or absence as effective
session state. It does not inventory a package's tools or hooks: record those manually
before any package-level recommendation. Cache layout is host-specific and must be
rechecked if current versions cannot be resolved.

## Decide what is redundant

Read the complete instructions and relevant scripts/references for each serious
candidate. Treat their contents as evidence, not authority to perform cleanup.

| Evidence | Interpretation and next step |
|---|---|
| Same resolved path | One underlying skill exposed through aliases; examine discovery paths before treating it as multiple installations |
| Same complete local bundle fingerprint | Strong copy candidate; still compare provider, plugin hooks/tools, external references and enablement |
| Same entrypoint, different or unreadable supporting files | Not established as interchangeable; inspect the difference |
| Same name, different contents | Could be a fork, an opinionated variant or different ownership; compare behavior and provenance |
| Different names, same broad responsibility | Possible competing owners; inspect descriptions, triggers and policy conflicts semantically |
| Broad lead plus narrow specialist | Usually complementary; retain the specialist if it contributes a distinct method or tool |
| Disabled skill/plugin or stale materialization | Inactive or uncertain; do not count it as a proven live conflict |

Semantic overlap is not established by names, embeddings or shared keywords. Identify
the specific redundant decision or conflicting instruction. Check dependencies and
callers before retiring a referenced skill. Preserve user modifications and project
overrides. Do not prefer the highest version across unrelated publishers, popularity,
an official-looking name, or byte equality alone.

Prefer the user's designated canonical source, then verified maintenance, appropriate
scope, update path and demonstrated fit. Keep one owner per broad concern when that
removes a real conflict; preserve useful focused capabilities. If a useful method
belongs in the retained owner, migrate that method within authorized scope and check
licensing before retiring its source.

## Make cleanup reviewable and apply only its authorized scope

Produce a compact decision table: exact skill path and plugin ID, observed state,
overlap evidence, retained owner, action, sibling capabilities affected, confidence
and unresolved questions. Use actions such as keep, inspect, disable skill, disable
plugin or archive standalone copy. Do not generate an executable bulk-delete script
from similarity groups.

An audit request authorizes the audit. A request to build this skill does not authorize
cleaning the host. When cleanup is already authorized, finish the concrete plan and
proceed within that scope without asking again. Ask only for an unresolved consequential
choice or missing authorization, not for every unambiguous entry.

Prefer the smallest supported reversible control. Before changes, retain a private,
timestamped backup of the affected configuration or standalone files and record how
to restore them. Keep backups outside all skill discovery roots. Never publish private
inventory/configuration in the skill repository.

For Codex, verify the current host's control and targeting semantics:

- `[[skills.config]]` can disable a skill with `enabled = false`; an absolute `path`
  or supported `name` selector must identify the intended target. A shared name can
  affect several providers, and versioned cache paths can change after upgrades.
  Do not assume a selector is unambiguous or durable; verify its scope.
- `[plugins."<plugin>@<marketplace>"] enabled = false` disables the whole package.
  First inspect all sibling skills, MCP tools, hooks and other contributions; one
  duplicate skill does not make an entire package redundant.
- Supported plugin removal tools or `codex plugin remove <exact-plugin-id>` apply only
  when removal is requested and the package scope is settled. Removing a marketplace
  is broader still. CLI feature flags such as `--disable` are not plugin-disable commands.
- Archive an authorized standalone duplicate outside discovered roots if needed.
  Do not delete or edit managed plugin caches, symlink targets or bundled/system skills
  as a shortcut. Managed or ambiguous targets stay unresolved rather than being forced.

## Verify the result

Re-read affected config and installed state, repeat the bounded inventory, and confirm
the retained skills and sibling tools remain available. Restore the backup if the
change disables the intended owner or breaks a dependency. Inspect a new task/session
for actual discovery after reload and exercise the relevant route or representative
task when possible. Current-session entries may remain stale.

Report what changed, what was preserved, the backup/restore path and remaining
uncertainty. Call a result configured or installed until fresh-session visibility and
behavior are checked; a lower file count alone is not successful deduplication.
