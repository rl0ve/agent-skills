---
name: route-ai-work
description: Route substantial agent work to the leanest reliable parent or subagent configuration using task shape, context coupling, ambiguity, risk, latency, and token use. Use for model or effort selection, delegation, parallel work, large context, architecture, debugging, review, long autonomous jobs, or when the user asks to save tokens or time. Do not delegate trivial work.
compatibility: Claude Code and Codex. Each has its own route table below; the method is the same.
---

# Route AI Work

Choose the route that can reliably finish with the least total elapsed time, including
handoffs, retries, and integration. A smaller model is not automatically faster. Optimize user-visible elapsed
time first, reliable completion second, and token use third unless the user chooses a
different order.

## Route the task

1. Honor explicit model, effort, timing, budget, delegation, and safety choices.
2. Check context before changing a knob. Missing requirements or missing files are not a model failure.
3. Keep trivial, tightly coupled, or already-contained work in the parent session.
4. Delegate only when a bounded specialist, context isolation, or independent read-only work repays startup and duplicated-context cost.
5. Use one write-capable owner per working tree. Never run the parent and a writing subagent against overlapping files at the same time.
6. Prefer a one-step effort increase before moving to a larger model when the model understood the problem but did not inspect, verify, or persist enough - except above Sonnet medium, where the next family is the cheaper step (see the dominance note below the Claude Code table).
7. Prefer a larger model when the full relevant context was available, the model genuinely tried, and capability or judgment was still insufficient.
8. Count retries, not token price. A route that lands on the first attempt is usually cheaper than a nominally cheaper route you correct twice. If you are re-prompting a model on the same problem, you are already past the point where the larger family was the economical choice.

## Missing skills, plugins or integrations

When the user asks to find new capabilities or an actual capability gap blocks the
work, use the bundled [discover-capabilities](../discover-capabilities/SKILL.md) skill.
It owns general discovery and overlap checks across domains. Use existing capabilities
first; do not search for new packages on every routed task. UI Router owns design
selection when available; Work Router continues to own execution and model decisions.

For existing skill duplication, competing workflow owners or a requested cleanup,
use [deduplicate-skills](../deduplicate-skills/SKILL.md). It owns the cross-domain
inventory, overlap decisions and scoped consolidation. Do not run a global audit on
ordinary tasks or treat discovery of a duplicate as permission to remove it.

## Resolve timing without nagging

Infer the mode when the user's language is clear:

- Treat "fast," "quick," "interactive," "now," or similar language as **Fast**.
- Treat "balanced," "best tradeoff," or "quality per minute" as **Balanced**.
- Treat "background," "no rush," "cheapest," "lowest cost," or similar language as **Economy**.
- Treat "quality first," "highest assurance," "executive-critical," or an explicit high-stakes boundary as **Quality-first**.

When the user gives no timing signal:

1. Keep trivial work direct without asking.
2. Default ordinary interactive work to **Fast**, because this router prioritizes wall-clock latency first, quality second, and cost third.
3. Override that default only when safety, irreversibility, or explicit quality requirements demand it.
4. Ask one concise question only when Fast and Economy or Balanced are both plausible and the choice would materially change elapsed time, cost, or quality: `Should I optimize for fastest completion, balanced quality, or lowest-cost background work?`

Do not ask the timing question when the request or existing instructions already answer it.

**Fast routing is separate from Codex Fast service.** Default the service tier to
Standard. If Codex Fast could materially shorten model-bound interactive work, surface
Standard versus Fast once; Fast requires account and workspace availability and an
explicit user choice. Never enable it or claim it is active without confirmation from
the application. A request for quick routing alone does not authorize a service-tier change.

## Default routes

The rules above are the same whichever agent you are. The table is not: read the one that
matches the agent you are running as, and ignore the other.

### If you are Claude Code

| Work shape | Route | Model | Effort | Notes |
|---|---|---|---|---|
| One-step, tightly coupled, or conversational | Parent | active model | active effort | Delegation overhead would dominate. |
| Narrow lookup, classification, repository map, or evidence collection | `work-router:fast-scout` | Haiku | low | Read-only; return compact evidence. |
| Defined implementation with clear acceptance criteria | `work-router:sonnet-builder` | Sonnet | medium | Sole writer; verify proportionately. |
| Reasoning-dense implementation: a feature, a multi-file change, or work where the plan is not yet settled | Parent | Opus | low | Primary default for real implementation. No subagent; the parent already holds the context. |
| Difficult diagnosis, architecture, or consequential tradeoff | `work-router:opus-architect` | Opus | high | Read-only by default; parent integrates. |
| High-stakes final review after a strong implementation | `work-router:critical-reviewer` | Opus | xhigh | Read-only; use only when the risk justifies it. |
| Long-horizon, multi-stage, highly ambiguous autonomous project | `work-router:fable-runner` | Fable | high | Sole writer; only when Fable is permitted and the task is large enough. |
| Prose whose quality is the deliverable: talk track, narration, naming, UX copy, executive writing, voice match | `work-router:fable-wordsmith` | Fable | high | Read-only; returns text the parent verifies and applies. |

**Language work routes on a different axis.** The table above ranks families by reasoning difficulty, and that ranking does not carry over to writing. When the deliverable is the prose itself - a line a person will say on a stage, a name, a paragraph of UX copy, a voice match against a sample - route to `work-router:fable-wordsmith` rather than to `opus-architect`, at any difficulty. Opus is the better diagnostician; Fable hears cadence, register and the tics a reader feels but cannot name. Use Opus for prose only when the hard part is the argument or the facts rather than the words. Keep the wordsmith read-only: prose edits are cheap to review and expensive to apply blindly, and the parent owns checking every figure before anything ships.

**Sonnet above medium is a dead rung.** Sonnet high, xhigh and max cost more per completed task than Opus low without matching its quality, so treat Sonnet medium as the top of that family and step to Opus low rather than raising Sonnet effort. Reserve Sonnet low and medium for what they are genuinely best at: mechanical edits, tests, boilerplate, config, and fast interactive work where a plan already exists and latency is the binding constraint. Opus low is the route for anything with real reasoning content, and Opus medium is the first escalation when Opus low stalls or thrashes. In the frontier band, Fable medium is the value rung and Fable high is the route for the hardest repo-wide and architectural work; Fable xhigh is a ceiling for genuinely frontier tasks. Fable low is situational rather than cheap - it edges past Opus medium on quality but costs more, so reach for it only on long agentic runs made of individually easy steps, and never as a routine shortcut. For a long autonomous run, prefer Opus high or xhigh over Fable medium: same band, and Fable bills separately.

Two caveats on Opus low, both of which cut against the arithmetic. Low effort does not shorten its replies, and output is the expensive half of the meter, so a run can cost more than a per-task estimate predicts. It also delegates to subagents readily, which multiplies context. Give it an exact file map, hold the one-writer rule, and check actual burn on a long run instead of assuming the low setting is thrifty. The basis for this ordering, and its limits, are in [references/routing-policy.md](references/routing-policy.md).

### If you are Codex

Resolve the active model, supported effort levels, available agents, and user constraints
against the current host catalog before routing. The September 22, 2026 GPT-6 Sol and
GPT-6 Luna release changes the default Codex family choices; it does not make a model
handoff free or invalidate work already progressing well on Astra, Terra, or another
explicitly selected model.

**GPT-6 Sol is the default for new demanding Codex work.** Keep ambiguous requirements,
consequential decisions, difficult diagnosis, synthesis across documents, broad
implementation, integration, and final verification in a Sol parent. Use GPT-6 Luna
for narrow, clear, repeatable work whose result has objective acceptance criteria.
Neither release description establishes that a model is best for every UI, fastest for
every task, or cheaper end to end after retries and review.

| Route | Use it for | Default configuration | Write policy |
|---|---|---|---|
| Current parent | Trivial or tightly coupled work, orchestration, integration, final verification | Active model and effort | May write |
| GPT-6 Sol parent or bounded built-in Sol agent | Ambiguous architecture, difficult debugging, consequential judgment, complex synthesis, or broad implementation | GPT-6 Sol; medium for ordinary work, high for complex work | Parent writes; delegate read-only unless assigned sole ownership |
| `sol-advisor` | A bounded sanity check, quick review, UX opinion, or first-pass diagnosis that repays a handoff | GPT-6 Sol, medium | Read-only |
| Built-in Sol `worker` or parent Sol | Defined multi-file implementation beyond Luna's scope, with clear requirements and sufficient context | GPT-6 Sol, normally high; explicitly verify effective model | Sole writer |
| `terra-explorer` | Independent repository exploration, large-file reading, documentation checks, evidence extraction | GPT-5.6 Terra, medium | Read-only; parent owns consequential synthesis |
| `luna-builder` | Narrow, clear, repeatable implementation with objective acceptance criteria | GPT-6 Luna, high | Sole writer |
| `luna-economy-worker` | Stable, bounded, cost-first background work | GPT-6 Luna, max | Sole writer; economy exception to rare max use |
| `sol-architect` | Complex bounded specialist work when a handoff is useful | GPT-6 Sol, high | Read-only |
| `sol-critical` | Critical independent review after a strong attempt | GPT-6 Sol, max | Read-only; not a mandatory rung |
| Existing Astra parent | Work already progressing with loaded Astra context, or an explicit Astra constraint | Active Astra setting | Preserve ownership; do not switch merely because Sol is newer |

For new demanding work when model choice is open, prefer GPT-6 Sol high. Use Luna for
narrow repeatable work and Terra for read-only evidence collection when it remains
available and a handoff pays. In a Sol parent, delegate only with a concrete benefit:
an independent question can run alongside useful parent work, a small isolated task
avoids loading irrelevant context, or the user explicitly prefers cost over latency.

**Effort:** keep the active setting unless there is a reason to change it. Recommend
Sol medium for ordinary work, high for complex reasoning, and xhigh for unresolved
reasoning or a consequential final review needing more depth. Reserve max for a
justified hardest-case escalation; do not choose it merely for an executive audience,
a rendered artifact, or a long task. Ultra is not a routine next rung: check current
behavior and delegation permission before recommending it, especially under a
single-agent constraint.

**Model constraints and inheritance:** an explicit family choice applies to the parent
and delegated work. Do not silently substitute Luna, Astra, Terra, or Sol. A `worker`
or `explorer` name does not select a model; named profiles retain their configured
models. Follow host restrictions on overrides and context inheritance, and verify the
actual configuration. If no compatible child can be created, stay in the compatible
parent; if neither is available, explain the limit without changing the requested
model. GPT-5.6 Sol/Luna profiles already installed outside this repository are not
updated by a plugin checkout alone; use the profile sync workflow when authorized.

When a named profile is missing, use a compatible built-in `explorer` for reading or
`worker` for implementation, or keep the work in the parent. State the fallback and its
effective model and effort. Never claim to change a running parent's model, effort, or
service tier without application confirmation.

## Token and latency controls

- Keep the routing skill and agent prompt concise; pass only the objective, exact inputs, owned files, acceptance criteria, and return format.
- Do not copy the full conversation into a subagent. Summarize only the facts it needs.
- Prefer one scout over several overlapping scouts.
- Parallelize independent read-only questions; serialize dependent work.
- Do not ask a writing agent to re-discover context the parent already has. Give it the precise file map.
- Stop escalation once the acceptance criteria are satisfied.
- Switch families at a phase or compaction boundary, not mid-turn. The prompt cache is per-model, so changing family rewrites the whole cached prefix at the cache-write premium. That cost is real but small; it is a reason to time the switch, never a reason to finish substantial work on a route you have already judged wrong.
- Do not use `max` merely because a task is important. `max` is off the efficient frontier in every Claude family: Sonnet max scores below Opus low at several times the burn, Opus max adds nothing over xhigh, and Fable max ties Fable xhigh while costing a quarter more. Outside the explicitly cost-first Luna economy route, use it only after a strong route failed or for a critical one-shot decision.

## Delegate safely

Before substantial delegated work, announce exactly:

`Route: <agent> (<model>, <effort>) - <one-line reason>`

Give each subagent a bounded prompt containing:

- objective and relevant inputs;
- owned or allowed files;
- acceptance criteria and required validation;
- required return: concise findings or diff summary, exact checks, and unresolved risks;
- a reminder that other agents may be active and their edits must not be reverted.

Parallelize independent read-heavy exploration, tests, triage, and summarization. Serialize overlapping work and allow only one write-capable agent per working tree. Avoid recursive delegation trees and do not transfer full context repeatedly.

The parent remains responsible for requirements, decisions, integration, final validation, and the user-facing answer.

## Long tasks and outside advice

For work spanning several dependent phases or losing time to repeated polishing, read
[references/long-running-work.md](references/long-running-work.md). Use bounded phase
outcomes and evidence of completion; add a manager/implementer split only when it earns
its coordination cost. This does not create a goal, schedule background work, or change
agent limits. Follow the host's authorization rules for those actions.

Treat social recommendations as dated, task-specific evidence. A saved post, impressive
demo, or benchmark rank does not override the user's model choices or prove a cheaper
end-to-end route. Check the original source, current host support and comparable task
conditions before changing routing. Preserve useful methods without copying old model
assignments, unexplained settings, claimed savings, or mandatory agent counts.

## Escalate deliberately

- Fix missing context or a faulty tool/validation path before increasing model capability.
- In a GPT-6 Sol parent, keep demanding work there; recommend medium to high when
  more depth is needed, then high to xhigh for unresolved reasoning.
- Preserve a well-progressing Astra parent and its loaded context. For new work with
  an open model choice, use GPT-6 Sol rather than routing through an obsolete ladder.
- Return ambiguous Luna work or judgment-heavy Terra findings to the Sol parent.
  Do not ask Luna to make the consequential synthesis.
- When staying in the Sol family, escalate `sol-advisor` to `sol-architect` for deep
  tracing or system design, and to `sol-critical` only for critical review or a
  documented strong failure. Critical work does not automatically require max if a
  capable parent and focused independent review can satisfy the acceptance criteria.
- In Claude Code, escalate a draft from the parent to `work-router:fable-wordsmith` when a reader has rejected prose on feel rather than on content ("this sounds off", "I hate how this reads") and the parent's own revision did not land. That verdict is a language problem, not a reasoning one.
- Do not escalate solely because work is slow or difficult.

Never execute an irreversible action without explicit user confirmation.

## Agent-specific notes

### Claude Code: managed workspaces

Model aliases and effort levels are requests, not authority. Company `availableModels`, effort caps, provider mappings, and marketplace rules win.

- If Claude Code substitutes another model, report the requested route and the actual model shown by Claude Code.
- If Fable is unavailable, use the newest permitted Opus route for deep work, or the inherited model when the organization blocks the family.
- If the client does not support a requested effort level, use the nearest supported level at or below it and say so.
- Do not edit managed settings or attempt to bypass a company policy.

### Codex: custom agent profiles

The plugin skill is the routing policy. Runnable custom agents remain standalone TOML profiles because Codex loads them from `~/.codex/agents/` or a project's `.codex/agents/` directory.

When asked to install, refresh, or inspect the bundled profiles:

1. Run `scripts/sync_agent_profiles.py` without `--apply` for a dry run.
2. Show the proposed changes and obtain any approval needed to write the destination.
3. Run `scripts/sync_agent_profiles.py --apply`.
4. Tell the user to start a new Codex task so new profiles are loaded.

The sync tool backs up changed or renamed profiles, retires only known legacy names, and never deletes unrelated profiles. Do not hand-edit global routing configuration as part of this workflow.

Load detailed references only when needed:

- Read [references/routing-scenarios.md](references/routing-scenarios.md) for representative decisions and review cases.
- Read [references/routing-basis.md](references/routing-basis.md) for the distilled policy, migration logic, and current-product overlay.
- Historical source packs below predate GPT-6 Sol and Luna and do not override this policy.
- Read [references/source-shared-routing-guide.md](references/source-shared-routing-guide.md) when revising task, timeliness, harness, or mixed-workflow routes.
- Read [references/source-codex-agents.md](references/source-codex-agents.md) when revising agent behavior, delegation, or quality gates.
- Read [references/source-wall-clock-evidence.md](references/source-wall-clock-evidence.md) when comparing measured completion time, cost, steps, or tokens. Search this large reference by model name or benchmark before reading broad sections.
- Read [references/source-research-evidence.md](references/source-research-evidence.md) when reviewing model, effort, harness, context-management, or cross-harness research. Search this large reference for the exact claim or model first.
