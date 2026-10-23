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

1. Run `claude --version` and inspect command help when needed. Use
   `claude plugin list --json` to check this plugin's version, scope and enablement.
2. Inspect `claude plugin details <exact-plugin-id>` when supported, plus relevant
   installed agent definitions. Distinguish packaged agents from those available
   in this session. Do not assume `claude agents` lists definitions: current clients
   use it to manage running sessions. No test agent or model call is required.
3. Check effective user/project instructions for an active routing override and
   explicit model, revision, effort or delegation constraints. Inspect only relevant
   provider, alias, model allowlist and effort-cap metadata from authorized settings.
   A fixed-model agent does not inherit the parent's family constraint automatically.
4. Verify the actual provider/revision behind `opus`, `sonnet`, `haiku` and any proposed
   Fable route. Apply the dated model assessments and current host catalog: for example,
   Haiku 5.5 needs Claude Code 2.1.293+, and provider aliases can still resolve to older
   models. An enabled plugin does not prove model availability or exact revision.
5. Separate requested settings from host-reported active model and effort. Use available
   session metadata; ask for `/status`, `/model` or `/effort` evidence only when needed.
   Report unavailable evidence as unverified and a conflicting managed cap as an unmet
   requirement, following [managed-workspace rules](../route-ai-work/references/managed-workspaces.md).
   Do not change settings, start a session or bypass policy to complete the check.

The [model controls](https://code.claude.com/docs/en/model-config) and
[plugin component inventory](https://code.claude.com/docs/en/discover-plugins#see-what-an-installed-plugin-adds-to-your-sessions)
were checked October 22, 2026; the installed client's help remains authoritative.

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

## Private shared-state access

When the requested setup includes shared project context, use
[the state contract](../route-ai-work/references/shared-project-state.md). Inspect only
the selected private record, not every project or personal memory store. Check realm,
project, coordinator, revision and the actual backend/transport. Repositories are
optional: desktop Work with local file access can use a private folder without Git.
For a Git-backed record, verify the intended remote/audience and exact context commit;
repository access does not imply file-level privacy. The helper requires `--allow-git`
for explicitly selected checkouts and does not verify hosting visibility.

For the local template layout, `private_project_state.py check` under
`../route-ai-work/scripts/` checks placement, file modes, basic schema and an optional
`--expected-revision`. It is read-only and does not prove acceptance, effective ACLs,
remote access or synchronization. Do not initialize, repair permissions, change a
coordinator or write test records during this check.

Verify the relevant executor can read the selected accepted revision using existing
authorized tools. Local success is not remote evidence. Where checking another task
requires a message, preserve that tool's human-authorization rule and report access
as unverified until it can be checked. Identify stale snapshots, conflicting copies
and missing access; never silently fall back to a different realm or personal library.
Keep private record content and concrete bindings out of public diagnostic artifacts.

## Report

Separate facts into `verified`, `organization-controlled`, and `not yet verified`.
Recommend an upgrade only when the installed client lacks a feature the user needs.
Report a requested configuration separately from the actual configuration.
