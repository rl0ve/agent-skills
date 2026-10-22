---
name: check-routing-setup
description: Inspect the active host, router components, model catalog, execution locations, orchestration overlap and workspace constraints. Run only when the user explicitly asks to check or troubleshoot the router setup.
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
   `~/.codex/models_cache.json` when present) for the active model, GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna and GPT-5.6 Terra availability,
   supported reasoning levels, and custom profiles actually exposed in this task.
3. Distinguish bundled profiles, files installed in `~/.codex/agents/` or project
   `.codex/agents/`, and agents actually loaded/callable. A plugin install does not
   establish the latter two. The profile sync script's dry run only compares files.
4. Check the effective user/project instruction sources for an active [routing override](../route-ai-work/references/routing-overrides.md). Report its scope, enabled state, priorities, credit policy, model constraint and expiry; distinguish saved instructions from the configuration loaded by this chat. Check explicit model and delegation constraints. A named profile retains its configured family under a different parent; a built-in worker may inherit or accept overrides according
   to the host. Verify effective model and effort before recommending that route.
5. Separate Fast routing from service-tier state. Treat unknown service status as
   unverified, and require an explicit user choice for any move from Standard to Fast
   or Ultrafast. Report Ultrafast as unavailable unless the plan and workspace show it.
   Check ultra's delegation behavior before recommending it with restricted delegation.

## Claude Code

1. Run `claude --version`.
2. Run `claude plugin list --json` and confirm this plugin is enabled.
3. Run `claude agents` and confirm the router agents are listed.
4. Report the provider and client version behind `haiku`: Haiku 5.5 requires the
   Anthropic API and Claude Code 2.1.293+; Bedrock, Vertex and Foundry map it to 4.5.
5. Ask the user to open `/model` or `/effort` only when model visibility cannot be
   verified another way.

## Capability and plugin overlap

When the user asks about conflicting skills or plugins, also inspect enabled router
copies and matching installed skill names/paths. Compare instructions and provenance,
not just names. Report legacy duplicate routers, competing broad leads, duplicate
editors and complementary integrations separately. Recommend one canonical owner per
concern; do not disable anything during this read-only check.

When Ultra or Superpowers is relevant, use the
[compatibility guide](../route-ai-work/references/orchestration-compatibility.md).
Distinguish ChatGPT Work's native Ultra orchestration from local Codex effort and
delegation permissions. Inspect the installed Superpowers version and exact skills;
the upstream version can have different review or branch-finishing rules. Identify
the current coordinator before recommending another orchestration layer.

## Execution locations

When the requested setup includes separate threads, remote or cloud work, use the
[execution guide](../route-ai-work/references/execution-locations.md). Inspect the
available creation, reading, messaging, handoff and wait controls and relevant saved
projects. Report which destinations are discovered, reachable, model-compatible and
ready with the required inputs; keep missing evidence explicit. Do not create a test
task, send a message, move a live thread or install remote infrastructure during this
read-only check. Distinguish a local task, a remote project, Codex Cloud and cloud Work.
Report whether safe isolation and artifact return are available for a writing route.

## Report

Separate facts into `verified`, `organization-controlled`, and `not yet verified`.
Recommend an upgrade only when the installed client lacks a feature the user needs.
Report a requested configuration separately from the actual configuration.
