---
name: check-routing-setup
description: Inspect the active Codex or Claude Code host, router components, model catalog, and workspace constraints. Run only when the user explicitly asks to check or troubleshoot the router setup.
disable-model-invocation: true
---

# Check Routing Setup

Perform a read-only check for the active host. Never modify user, project, local, or
managed settings during this check. Do not print credentials, complete settings files,
or full model-cache records; extract only relevant model and effort metadata.

## Codex

1. Use the current host's tools or CLI to identify client version and enabled Work
   Router version. Verify supported commands with that client's help before using them.
2. Inspect the host's model/agent metadata (or selected fields from
   `~/.codex/models_cache.json` when present) for the active model, Astra availability,
   supported reasoning levels, and custom profiles actually exposed in this task.
3. Distinguish bundled profiles, files installed in `~/.codex/agents/` or project
   `.codex/agents/`, and agents actually loaded/callable. A plugin install does not
   establish the latter two. The profile sync script's dry run only compares files.
4. Check explicit model and delegation constraints. A named Sol profile stays Sol
   under an Astra parent; a built-in worker may inherit or accept overrides according
   to the host. Verify effective model and effort before recommending that route.
5. Separate Fast routing from service-tier state. Treat unknown service status as
   unverified, and require an explicit user choice for any move from Standard to Fast.
   Check ultra's delegation behavior before recommending it with restricted delegation.

## Claude Code

1. Run `claude --version`.
2. Run `claude plugin list --json` and confirm this plugin is enabled.
3. Run `claude agents` and confirm the router agents are listed.
4. Ask the user to open `/model` or `/effort` only when model visibility cannot be
   verified another way.

## Capability and plugin overlap

When the user asks about conflicting skills or plugins, also inspect enabled router
copies and matching installed skill names/paths. Compare instructions and provenance,
not just names. Report legacy duplicate routers, competing broad leads, duplicate
editors and complementary integrations separately. Recommend one canonical owner per
concern; do not disable anything during this read-only check.

## Report

Separate facts into `verified`, `organization-controlled`, and `not yet verified`.
Recommend an upgrade only when the installed client lacks a feature the user needs.
Report a requested configuration separately from the actual configuration.
