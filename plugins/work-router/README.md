# Work Router

Task-first routing for Codex and Claude Code. Optimize total completion time first,
reliable completion second, and cost/token use third unless the user chooses otherwise.

The plugin contributes:

- `/work-router:route-ai-work`, an auto-invocable policy with a table for each host;
- [main-thread recommendations](skills/route-ai-work/references/model-routes.md#reassess-the-main-thread)
  for useful model or reasoning changes, with explicit constraints and confirmed settings;
- [execution location routing](skills/route-ai-work/references/execution-locations.md)
  for subagents, separate threads, connected machines and cloud tasks;
- [orchestration compatibility](skills/route-ai-work/references/orchestration-compatibility.md)
  for native Ultra and optional engineering workflows such as Superpowers;
- [conditional native goals](skills/route-ai-work/references/native-goals.md), with
  explicit authorization, live-state reuse, goal reconciliation and host lifecycle checks;
- [loop controls](skills/route-ai-work/references/long-running-work.md#define-the-loop-before-repeating-attempts)
  for verification, applicable limits, progress checks and recovery;
- [workflow feedback](skills/route-ai-work/references/workflow-feedback.md) for
  occasional evidence-based improvement suggestions during active work;
- `/work-router:check-routing-setup`, a manual, read-only environment check;
- `/work-router:discover-capabilities`, focused discovery for missing capabilities;
- `/work-router:deduplicate-skills`, installed-skill auditing and scoped consolidation;
- [`/work-router:skills-ecosystem-audit`](skills/skills-ecosystem-audit/SKILL.md),
  comparison of bookmarks, GitHub stars, and current discussion with the full ecosystem;
- Claude subagents for scouting, building, architecture, critical review and Fable
  specialists, plus an opt-in, untested Haiku builder for mechanical edits;
- six separately installable Codex profiles spanning Sol, Terra, and Luna;
- a Claude `PreToolUse` hook that blocks Bash commands containing `sudo`.

## Threads, remote machines and cloud tasks

Work Router now chooses where work should run as well as who should do it. It uses
the current host's native tools, with one coordinator and one writer per checkout.
Ordinary contained work stays in the current task.

| Choice | Use it when |
|---|---|
| Stay here | Loaded context and tightly connected steps make a handoff wasteful. |
| Use a subagent | A bounded specialist or independent review can report back within this task. |
| Continue or create a separate thread | A workstream benefits from durable ownership and separate history. |
| Use a connected machine | Its tools, data, hardware or existing environment materially help. |
| Use a cloud task | Inputs are portable, access is available, and the result can return for review. |

For example, ask it to compare execution locations, create a separate task in a
worktree for a named independent component, or coordinate specified existing threads.
The [execution guide](skills/route-ai-work/references/execution-locations.md) checks
destination capability and permission before dispatch, carries the exact base and
acceptance criteria, and follows work through return, integration and cleanup. New
tasks, messages and moves follow the host's authorization rules. A recommendation
does not silently create them, and a cloud Work task is distinct from Codex Cloud.

Ultra and Superpowers are optional. Ultra's delegation behavior depends on the host;
local Codex's effort setting does not by itself authorize delegation. Superpowers can
supply development methods, or own a selected implementation phase, while Work Router
supplies model and location constraints. Choose one coordinator for each phase and
avoid duplicate agent/review loops. Neither option is required for remote routing,
and Ultra is separate from the Ultrafast service tier.

## Private project context

For shared context, use [private project state](skills/route-ai-work/references/shared-project-state.md):
Markdown decisions and knowledge, a compact task record, and one coordinator who
accepts worker returns against current revisions. Projects can span repositories or
have no Git repository, including ChatGPT Work with local files in desktop mode.
The optional initializer creates empty owner-only local records outside Git by default,
with an explicit option for an approved checkout. A private project or companion
repository can carry versioned handoffs; the helper does not commit, push or synchronize
machines. Obsidian is an optional viewer/editor for the Markdown.

The [work-account guide](skills/route-ai-work/references/work-account-setup.md) explains
how to reuse public skills with separate private work records and managed policies.
Public packages contain methods and templates, never the live project library.

## Optional routing override

Use a [removable override](skills/route-ai-work/references/routing-overrides.md) when you
want different priorities for a task, project, or all chats on a host. Choose accuracy,
latency and credit conservation independently of an optional model constraint. For
example, prioritize quality and use available credits with Astra throughout, then later
release the model constraint or turn the override off. Normal router defaults remain
unchanged. These are instruction preferences, not account settings or a live model switch.

## Portable workflow preferences

Carry a selected profile across machines with the opt-in
[preference setup script](skills/route-ai-work/references/portable-preferences.md).
Preview, apply and check it separately on each host. The included `rl0ve` profile
keeps shared workflow choices together with a Codex-only Astra constraint; Claude
Code keeps its own model routing. Unrelated local instructions and credentials stay
in place. Plugin installation and updates do not activate or synchronize a profile.

## Codex with Astra, Sol, Luna, and Terra

Use GPT-6.1 Sol for substantial everyday and complex reasoning, implementation, and
typical new UI builds; choose GPT-6 Astra directly for the hardest judgment,
exceptionally difficult unresolved creative/spatial direction where maximum quality
matters, or a demonstrated Sol capability limit. GPT-6 Luna handles
bounded repeatable work with objective checks. GPT-5.6 Terra remains a conditional
read-only specialist when user preference or workload evidence warrants it; no GPT-6
Terra or retirement is inferred. Preserve a progressing capable parent.

### Task-by-task starting routes

These are **recommended starting routes**, reviewed October 2, 2026 (moved here from the
root README in 1.9.0). They combine current model guidance with task characteristics;
they are not a benchmark ranking of every model-and-effort combination. Keep a capable,
progressing session when changing models would add more handoff work than benefit. The
agent-facing tables are in the [route-ai-work skill](skills/route-ai-work/SKILL.md#default-routes).

| What you need done | Start with | Reasoning | When to change the route |
|---|---|---|---|
| A tiny edit, one-step answer, or tightly connected follow-up | Current capable model | Keep the active level | Do it directly; creating another agent usually adds overhead. |
| A small inventory, extraction, classification, or clearly specified mechanical edit | **Luna 6** | **high** | Use Sol when interpretation, ambiguity, or consequential judgment becomes the hard part. |
| Routine coding, a defined feature, ordinary debugging, or substantive synthesis | **Sol 6.1** | **medium** | Raise to high when the task requires deeper tracing or more edge-case analysis. |
| Complex implementation, architecture, difficult debugging, or integrating several systems | **Sol 6.1** | **high** | Consider xhigh for unresolved reasoning; choose Astra when maximum capability or better judgment is needed. |
| Difficult architecture, diagnosis, or reasoning with unresolved dependencies that needs deeper analysis within Sol | **Sol 6.1** | **xhigh** | Use when the added depth is justified; choose Astra instead when model capability or judgment is the limiting factor. |
| A quick independent UX opinion, implementation review, or first-pass diagnosis | **Sol 6.1** | **medium** | Use high for deep review. Low is an option only for bounded, read-only triage with low stakes. |
| Substantial UI implementation with an established visual direction | **Sol 6.1** | **high** | Use Astra when the unresolved problem is exceptionally difficult creative or spatial judgment. |
| New substantial UI build with a normal visual-quality bar | **Sol 6.1** | **high** | Render and compare the result; a model label does not establish visual quality. |
| Exceptionally difficult unresolved art direction or creative/spatial work where maximum quality matters | **Astra 6** | **high** | Consider xhigh if difficult decisions remain unresolved. A failed Sol attempt is not required. |
| The hardest reasoning, diagnosis, or synthesis across several systems where maximum capability is needed | **Astra 6** | **high** | Consider xhigh when depth remains insufficient; justify max or ultra separately. |
| Exceptionally demanding reasoning or creative/spatial judgment with difficult unresolved tradeoffs | **Astra 6** | **xhigh** | A deliberate deeper pass, including upfront when clearly warranted. Validate the result; max/ultra are not automatic next steps. |
| Independent document or repository reading with a demonstrated Terra advantage, or an explicit Terra preference | **Terra 5.6** | **medium** | Use Luna for straightforward extraction or Sol for judgment-heavy interpretation when there is no reason to prefer Terra. |
| Stable, bounded background work where cost matters more than latency | **Luna 6** | **max**, for the named economy profile | Measure accepted work, retries and review time; this setting is not proven cheapest for every task. |
| Critical independent review when deliberately staying within Sol | **Sol 6.1** | **max**, conditionally | Use only when the risk or a prior strong failure warrants it; this is not a required rung before Astra. |

Host-sensitive workflows such as Dream Loop run in the host you are in (Codex → Astra,
Claude Code → Opus 5.5) unless you name another model; no cross-host move is made to
match an upstream harness.

### How latency and token use affect the choice

The default priority is **total elapsed time first, reliable completion second, and
token use third**, unless you choose another priority. These are ordered preferences,
not a fixed numerical weighting. The table recommends a route likely to complete the
work correctly; it does not optimize a cheap first attempt in isolation.

| Task or preference | How the recommendation changes |
|---|---|
| Interactive work; fastest useful completion | Favor the capable route likely to finish with little rework. Avoid delegation when loading context and integrating results would take longer. |
| Stable background work; explicit cost-first preference | Consider Luna and a bounded brief with objective checks. Include verification and retries in the cost; the named max-effort economy profile is conditional. |
| Quality-first design or a consequential decision | Give capability and adequate reasoning more weight. Astra can be the first choice; use focused independent review when it adds assurance. |
| A task already progressing well | Keep its useful context; recommend a change only when the remaining work justifies the switching and verification cost. |

Infer timing from the conversation first. If timing is unclear and would materially
change the route, offer a brief **Need it soon / Background is fine** choice. Assess
token use across the whole job: input and duplicated context, reasoning and output,
subagents, retries, and review. Lower token prices do not establish lower total cost,
and API prices do not directly measure Codex subscription usage. Full rules:
[model-routes.md](skills/route-ai-work/references/model-routes.md#token-and-latency-controls).

### How to choose the reasoning level

Effort gives a model more opportunity to reason; it does not turn one model into another.
The same label across families is not an equal-time, equal-cost or equal-quality setting.
Check which levels the current host actually supports.

| Level | Good reason to use it | Boundary |
|---|---|---|
| **low** | Bounded, read-only triage or a quick first pass where low stakes and a small question justify it. | Not the default for demanding design, architecture or consequential review. Keep tiny work in the active session rather than switching merely to select low. |
| **medium** | Sol 6.1's ordinary substantial-work default; Terra's conditional reading route; ordinary work in an already active Astra session. | Move to high when missing depth is the problem. Resolve missing context before increasing effort. |
| **high** | Complex Sol work; a new demanding Astra task; bounded Luna work with objective acceptance checks. | This is the usual starting point for difficult work, not a universal quality guarantee. |
| **xhigh** | Sol or Astra work with difficult unresolved dependencies or tradeoffs where added reasoning depth is justified. It can be selected upfront for an unusually deep task, or after high leaves important questions unanswered. | Sol xhigh deepens reasoning within Sol; Astra xhigh combines added depth with the more capable family. Do not exhaust every Sol effort level before considering Astra. |
| **max** | A justified critical review within Sol, or the explicitly cost-first Luna economy profile. | A conditional setting, not the default for an important task. The Luna profile is not a measured universal cost winner. |
| **ultra** | A deliberately selected frontier task with a specific reason for this setting and compatible delegation requirements. | Verify model/host support and current delegation behavior. A long task, 3D scene, or executive audience alone does not justify it. |

| Model | Usual starting point | Harder work | Special cases |
|---|---|---|---|
| **Luna 6** | high, for narrow work with clear checks | Send substantial ambiguity or judgment to Sol/Astra | max only for the conditional background economy route |
| **Terra 5.6** | medium, when there is a reason to prefer its reading route | A capable Sol/Astra owner handles consequential synthesis | No assumed speed or cost advantage over the current GPT-6 models |
| **Sol 6.1** | medium for ordinary substantial work | high; xhigh when unresolved reasoning needs more depth | low for bounded triage; max for justified critical review |
| **Astra 6** | high for new unusually demanding work; preserve an effective active setting | xhigh when needed | max/ultra require a specific justification; Astra can be selected directly |

A representative comparison should hold the task, tool access, acceptance criteria and
service tier constant, then record accepted quality, elapsed time, retries and review
work. Within Codex, October 1 Arena WebDev evidence shows a narrower Astra Max edge over Sol 6.1 Max;
Sol 6.1 remains the starting route for typical new UI builds in Codex, with Astra reserved for
exceptionally difficult quality-first direction. The Max comparison does not validate other effort settings or
native Codex completion time. These tables are starting recommendations, not a universal
ranking. Model reviews regularly consult Arena, Artificial Analysis and original
specialist evaluators through the [benchmark source policy](skills/route-ai-work/references/benchmark-sources.md).

A handoff must repay context, startup, and review cost. Model release positioning is
not proof of comparative UI quality, wall-clock speed, or lower end-to-end cost. A
built-in worker's name does not establish its model; verify the effective model and
effort. The router recommends settings but cannot silently switch a running session.

Fast routing and Codex Fast or Ultrafast service are separate. Service defaults to
Standard; offer Fast once only when it could materially help, and require explicit user
choice plus account/workspace availability before changing it. Ultrafast bills at a
large multiple of Standard and is used only on request or for a stated deadline.

See the [policy](skills/route-ai-work/SKILL.md),
[evidence basis](skills/route-ai-work/references/routing-basis.md), and
[routing cases](skills/route-ai-work/references/routing-scenarios.md).

## Long-running work

Use [bounded phases](skills/route-ai-work/references/long-running-work.md) for substantial
multi-stage work or repeated polishing stalls. Completion requires evidence for the
phase's outcome, and the parent preserves the full task scope. A manager/implementer
split is conditional; no agent-limit changes, goals, or background schedules are
created by installing the skill. Social recommendations remain dated evidence.

For repeated attempts, distinguish hard limits from checkpoints for changing approach;
verify the runtime's stopping controls before promising an unattended cutoff. Reconcile
the goal when the user changes the outcome or acceptance conditions. A status-only
goal tool cannot rewrite an objective, and a working checkpoint must not imply it did.
Recurring workflow problems can prompt a concrete maintenance proposal at a useful
boundary, with project fixes, personal preferences and shared changes kept in scope.

## Lower usage at the same quality

For an explicit savings request, preserve acceptance criteria and first remove
redundant context and repeated work. A current-state reader can omit archived phases
without deleting them; source and required checks remain authoritative. Decision
models are conditional experiments, not automatic additions. See the
[procedure and measured-context limits](skills/route-ai-work/references/usage-economy.md).

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
The stable Sol profile names now target GPT-6.1 Sol; Luna targets GPT-6 Luna and Terra retains its existing ID.

## Claude Code

Stay in the parent for trivial or tightly coupled work. Use a bounded subagent only
when specialization, context isolation, or independent reading repays the handoff.
New substantial Claude work starts with **Opus 5.5 medium**, including implementation,
analysis, long jobs and prose with Natural Writing. Use high for difficult diagnosis
or consequential verification; xhigh/Max need a task-specific reason and a quality
benefit. Low fits supervised small work. Fable is conditional on explicit preference,
representative quality evidence or an Opus capability/style limit.

Verify the actual provider model: `opus` is a portable alias and can resolve to an
older revision. Opus 5.5 requires Claude Code 2.1.280+. The
[October 2 assessment](skills/route-ai-work/references/opus-5-5-review.md) records
the release, independent evidence and conditional API migration guidance. Current
WebDev evidence supports an Opus 5.5 quality-focused route when host choice is open;
it does not require leaving a productive Codex session or prove native task speed.

The router does not modify user or managed settings. Organization model allowlists,
effort caps, and explicit user choices always win.

## Skill and plugin discovery

Use `work-router:discover-capabilities` to find missing skills, plugins or integrations
across domains. It checks installed capabilities, searches a conditional shortlist,
and verifies upstream fit and overlap. UI Router adds design-specific checks when
available; neither router requires the other.

It also reviews installed packages' distribution and freshness. When you prefer plugins,
it checks for a maintained upstream plugin before recommending standalone skills. A
directory release can lag GitHub without implying that every plugin is stale. The
[distribution guide](skills/discover-capabilities/references/plugin-distribution.md)
keeps connectors, host runtimes, hooks, content differences and update paths in the
decision, and distinguishes an audit recommendation from permission to migrate.

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
