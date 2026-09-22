# Work Router

Task-first routing for Codex and Claude Code. Optimize total completion time first,
reliable completion second, and cost/token use third unless the user chooses otherwise.

The plugin contributes:

- `/work-router:route-ai-work`, an auto-invocable policy with a table for each host;
- `/work-router:check-routing-setup`, a manual, read-only environment check;
- `/work-router:discover-capabilities`, focused discovery for missing capabilities;
- `/work-router:deduplicate-skills`, installed-skill auditing and scoped consolidation;
- six Claude subagents spanning Haiku, Sonnet, Opus, and Fable;
- six separately installable Codex profiles spanning Sol, Terra, and Luna;
- a Claude `PreToolUse` hook that blocks Bash commands containing `sudo`.

## Codex with GPT-6 Sol and Luna

Use GPT-6 Sol for new demanding Codex work: ambiguous decisions, difficult debugging,
complex synthesis, broad implementation, integration, and final verification. Medium
is the ordinary-work default; use high for complex reasoning and xhigh only when a
material question remains unresolved. GPT-6 Luna is the narrow worker for clear,
repeatable tasks with objective checks, including an explicitly cost-first background
route. Preserve a well-progressing Astra parent rather than switching families solely
because Sol is newer.

A handoff must repay context, startup, and review cost. Model release positioning is
not proof of comparative UI quality, wall-clock speed, or lower end-to-end cost. A
built-in worker's name does not establish its model; verify the effective model and
effort. The router recommends settings but cannot silently switch a running session.

Fast routing and Codex Fast service are separate. Service defaults to Standard; offer
Fast once only when it could materially help, and require explicit user choice plus
account/workspace availability before changing it.

See the [policy](skills/route-ai-work/SKILL.md),
[evidence basis](skills/route-ai-work/references/routing-basis.md), and
[routing cases](skills/route-ai-work/references/routing-scenarios.md).

## Long-running work

Use [bounded phases](skills/route-ai-work/references/long-running-work.md) for substantial
multi-stage work or repeated polishing stalls. Completion requires evidence for the
phase's outcome, and the parent preserves the full task scope. A manager/implementer
split is conditional; no agent-limit changes, goals, or background schedules are
created by installing the skill. Social recommendations remain dated evidence.

## Codex profile setup

The shared skill works without installing custom profiles. If requested, preview the
standalone Codex profiles with:

```bash
python3 plugins/work-router/skills/route-ai-work/scripts/sync_agent_profiles.py
```

From the repository root, rerun with `--apply` to install them after reviewing the plan
and satisfying any destination write permissions. Changed profiles are backed up;
unrelated profiles are preserved. Start a new Codex task to load the changes. A
successful copy does not prove that the host supports a model or has loaded the profile.
The stable Sol and Luna profile names now target GPT-6 model IDs; Terra retains its existing ID.

## Claude Code

Stay in the parent for trivial or tightly coupled work. Use a bounded subagent only
when specialization, context isolation, or independent reading repays the handoff.
Fable handles long-horizon work and prose whose quality is the deliverable. The Claude
route table and six Claude agent definitions are unchanged by the GPT-6 Sol/Luna update.

The router does not modify user or managed settings. Organization model allowlists,
effort caps, and explicit user choices always win.

## Skill and plugin discovery

Use `work-router:discover-capabilities` to find missing skills, plugins or integrations
across domains. It checks installed capabilities, searches a conditional shortlist,
and verifies upstream fit and overlap. UI Router adds design-specific checks when
available; neither router requires the other.

## Skill deduplication

Use [deduplicate-skills](skills/deduplicate-skills/SKILL.md) for duplicate copies,
same-name variants or competing broad owners across Codex. Its read-only inventory
helper resolves aliases, checks supporting-file fingerprints and reads exact listed
plugin versions. It separates disabled remnants from possible active conflicts and
keeps prompt-time visibility unverified until checked in a fresh session.

The skill produces a concrete keep/inspect/disable/archive plan. Authorized cleanup
uses the smallest reversible control, with private backups and checks that retained
skills and sibling tools still work. It does not automatically delete skills, remove
a whole plugin because one skill overlaps, or turn a broad lead into a replacement
for every specialist. No global audit runs during ordinary routed work.
