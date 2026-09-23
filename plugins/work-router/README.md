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

## Codex with Astra, Sol, Luna, and Terra

Use GPT-6 Sol for substantial everyday reasoning and implementation; choose GPT-6
Astra directly for the hardest judgment, unresolved creative/spatial direction where
maximum quality matters, or a demonstrated Sol capability limit. GPT-6 Luna handles
bounded repeatable work with objective checks. GPT-5.6 Terra remains a conditional
read-only specialist when user preference or workload evidence warrants it; no GPT-6
Terra or retirement is inferred. Preserve a progressing capable parent.

Use the [task-by-task model and reasoning matrix](../../README.md#which-model-and-reasoning-level-should-i-use)
to choose a starting route. It includes implementation, research, review, visual direction,
spatial work and background jobs.

The [latency and token-use table](../../README.md#how-latency-and-token-use-affect-the-choice)
explains how interactive, cost-first and quality-first work change the recommendation.
The default uses ordered priorities rather than invented percentage weights, and
considers the full task including context duplication, retries and review.

### How to choose the reasoning level

Effort gives a model more opportunity to reason; it does not turn one model into another.
The same label across families is not an equal-time, equal-cost or equal-quality setting.
Check which levels the current host actually supports.

| Level | Good reason to use it | Boundary |
|---|---|---|
| **low** | Bounded, read-only triage or a quick first pass where low stakes and a small question justify it. | Not the default for demanding design, architecture or consequential review. Keep tiny work in the active session rather than switching merely to select low. |
| **medium** | Sol's ordinary substantial-work default; Terra's conditional reading route; ordinary work in an already active Astra session. | Move to high when missing depth is the problem. Resolve missing context before increasing effort. |
| **high** | Complex Sol work; a new demanding Astra task; bounded Luna work with objective acceptance checks. | This is the usual starting point for difficult work, not a universal quality guarantee. |
| **xhigh** | Difficult reasoning remains unresolved after a serious attempt, and more depth is likely to help. | Consider Astra directly when the need is greater capability or judgment; do not exhaust every Sol effort level first. |
| **max** | A justified critical review within Sol, or the explicitly cost-first Luna economy profile. | A conditional setting, not the default for an important task. The Luna profile is not a measured universal cost winner. |
| **ultra** | A deliberately selected frontier task with a specific reason for this setting and compatible delegation requirements. | Verify model/host support and current delegation behavior. A long task, 3D scene, or executive audience alone does not justify it. |

| Model | Usual starting point | Harder work | Special cases |
|---|---|---|---|
| **Luna 6** | high, for narrow work with clear checks | Send substantial ambiguity or judgment to Sol/Astra | max only for the conditional background economy route |
| **Terra 5.6** | medium, when there is a reason to prefer its reading route | A capable Sol/Astra owner handles consequential synthesis | No assumed speed or cost advantage over the current GPT-6 models |
| **Sol 6** | medium for ordinary substantial work | high; xhigh when unresolved reasoning needs more depth | low for bounded triage; max for justified critical review |
| **Astra 6** | high for new unusually demanding work; preserve an effective active setting | xhigh when needed | max/ultra require a specific justification; Astra can be selected directly |

A representative comparison should hold the task, tool access, acceptance criteria and
service tier constant, then record accepted quality, elapsed time, retries and review
work. We have not verified a current four-model visual-quality or matched wall-clock
benchmark. These tables are routing recommendations with explicit limits.

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
