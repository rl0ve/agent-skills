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

## Routing overrides

Resolve an active user override before applying the defaults below. Users can separately
choose ordered accuracy/latency/credit-conservation priorities, a credit policy, and an
optional model or effort constraint. “Use available credits” favors useful quality over
saving allowance; it never requests waste or authorizes extra spend. A locked model
applies to children as well as the parent. Generic default routes do not cancel it.

For an override request, persistence, change, or disable operation, follow the
[override contract and removable instruction block](references/routing-overrides.md).
Listen for clear task-local quality, speed and credit cues; ask one optional preference
question only when consequential ambiguity remains. Preserve explicit model constraints
and persist changes only when requested. Keep normal defaults intact: disabling the
override returns to those defaults. Changes
are scoped to the user's request; never claim a saved instruction switched a running
model, propagated to other hosts, or activated a different service tier.

## Route the task

1. Honor explicit model, effort, timing, budget, delegation, and safety choices.
2. Check context before changing a knob. Missing requirements or missing files are not a model failure.
3. Keep trivial, tightly coupled, or already-contained work in the parent session.
4. Delegate only when a bounded specialist, context isolation, or independent read-only work repays startup and duplicated-context cost.
5. Use one write-capable owner per working tree. Never run the parent and a writing subagent against overlapping files at the same time.
6. Choose the initial model and effort from the task requirements. Astra or xhigh can be selected upfront when warranted; the diagnostic steps below do not require a failed lower-capability attempt.
7. After an inadequate attempt, fix missing context or tool problems first. Consider more effort when the model understood the problem but lacked depth; choose a more capable model when capability or judgment was insufficient. Apply the host-specific guidance below, including the Claude Sonnet medium boundary.
8. Count total completion cost, including retries, review, and integration, rather than token price alone. Repeated capability failures favor a stronger route; a retry by itself does not prove that another model would be faster or cheaper. Use comparable task evidence where available.

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
- Treat "cheapest," "lowest cost," or similar explicit budget language as **Economy**.
- Treat "background" or "no rush" as timing flexibility; consider **Balanced** or **Economy** according to task fit and the user's cost preference. Timing flexibility alone does not request Luna max.
- Treat "quality first," "highest assurance," "executive-critical," or an explicit high-stakes boundary as **Quality-first**.

When the user gives no timing signal:

1. Keep trivial work direct without asking.
2. Default ordinary interactive work to **Fast**, because this router prioritizes wall-clock latency first, quality second, and cost third.
3. Override that default only when safety, irreversibility, or explicit quality requirements demand it.
4. Offer one short timing preference only when Fast and Economy or Balanced are both plausible and the choice would materially change elapsed time, cost, or quality. Prefer **Need it soon / Background is fine**; include a balanced option only when that distinction helps.

Do not ask the timing question when the request or existing instructions already answer it.

**Use context and a lightweight preference check.** An imminent meeting/demo, active
incident, or interactive debugging session is a latency cue. "No rush," a later
review date, batch processing, or explicit background work can support an Economy
route when the task itself is suitable. Do not infer urgency from importance alone.
When timing is unclear and it would materially change the model/effort route, offer
one short choice such as **Need it soon / Background is fine**, preferably through an
available asynchronous preference control. Continue useful independent work while the
choice is pending. Treat it as an optional preference check, not a permission gate;
without an answer, retain the existing default and state the assumption if material.
Do not repeatedly ask on routine subtasks or when timing has already been established.

Luna is eligible for bounded objective work in any mode, including urgent work when
it is likely to finish sooner. A relaxed deadline makes its cost-first route more
plausible; it does not make Luna suitable for ambiguous or consequential judgment.
The recommendation still accounts for context loading, retries, review and integration.


**Fast routing is separate from Codex Fast service.** Default the service tier to
Standard. If Codex Fast could materially shorten model-bound interactive work, surface
Standard versus Fast once; Fast requires account and workspace availability and an
explicit user choice. Never enable it or claim it is active without confirmation from
the application. A request for quick routing alone does not authorize a service-tier change.

## Default routes

The rules above are the same whichever agent you are. The table is not: read the one that
matches the agent you are running as, and ignore the other.

### If you are Claude Code

For new substantial Claude work, prefer **Opus 5.5 at medium effort** when supported
and permitted. Verify that `opus` resolves to `claude-opus-5-5` on this provider;
an alias, installed plugin or older client does not prove the model revision. Opus
5.5 requires Claude Code 2.1.280 or later. Keep portable family aliases in the
bundled agents; request the full provider-supported ID when revision fidelity matters.
Preserve an explicit model/effort choice and a capable parent already progressing.
If the user requires exactly 5.5 and it is unavailable, report the unmet constraint;
an older alias is not a completed 5.5 route or permission to substitute.

| Work shape | Route | Model | Effort | Notes |
|---|---|---|---|---|
| One-step, tightly coupled, or conversational | Parent | active model | active effort | Delegation overhead would dominate. |
| Narrow lookup, classification, repository map, or evidence collection | `work-router:fast-scout` | Haiku | low | Read-only; return compact evidence. |
| Defined implementation with clear acceptance criteria | `work-router:sonnet-builder` | Sonnet | medium | Sole writer; verify proportionately. |
| Substantial implementation, planning, synthesis, or a multi-file change | Parent | Opus 5.5 | medium | New substantial-work default; preserve useful parent context. |
| Difficult diagnosis, architecture, or consequential tradeoff | `work-router:opus-architect` | Opus 5.5 | high | Read-only by default; parent integrates. |
| High-stakes final review after a strong implementation | `work-router:critical-reviewer` | Opus 5.5 | xhigh | Read-only; justify added depth by the critical boundary and verify its benefit. |
| Long-horizon, multi-stage autonomous project | Parent or sole assigned writer | Opus 5.5 | medium or high | Start with bounded phases; duration alone does not require Fable or delegation. |
| Prose whose quality is the deliverable: talk track, narration, naming, UX copy, executive writing, voice match | Parent with Natural Writing | Opus 5.5 | medium | Preserve facts and register; judge the delivered prose. |
| A demonstrated Opus 5.5 capability/style limit or explicit Fable choice | `work-router:fable-runner` or `work-router:fable-wordsmith` | Fable | high | Conditional specialist; runner is sole writer, wordsmith returns text for parent review. |

**Calibrate effort for the new revision.** Start new substantial work at medium;
low fits a small, supervised exchange or a measured cost-sensitive route. High fits
deep diagnosis and edge-case verification. Use xhigh/max selectively when the task
and observed quality benefit justify their extra work; do not carry an Opus 5 setting
over by label alone. Fix missing context before escalating. The previous blanket
Sonnet-above-medium dominance claim used Sonnet 5/Opus 5 evidence and cannot rank
Sonnet 5.5 against Opus 5.5. Retain Sonnet for bounded planned implementation when
it meets the checks; choose Opus 5.5 for substantial judgment without a mandatory retry.

**Writing and long work no longer automatically select Fable.** Opus 5.5's new
communication and knowledge-work evidence warrants a fresh starting route. The old
Fable preference from one talk-track session remains useful for that voice, not a
universal writing ranking. Use the existing semantic owner and Natural Writing as
the final editor. Retain Fable when explicitly preferred, when representative work
demonstrates a benefit, or when Opus 5.5 reaches a capability/style limit. Keep prose
specialists read-only and verify every material fact before applying their text.
Task-specific voice evidence and explicit style preferences take precedence over
generic task size and family rankings, including for a single spoken line.

**Subscription and API billing are separate.** As checked October 1, 2026, Fable 5 and 5.1 are included on Claude Max within a limit of up to 50% of the regular weekly allowance; this is a shared limit, not an extra allowance. Pro and standard Team seats use usage credits for Fable. Check the current plan, remaining allowance and authentication route before choosing on cost. Claude Code subscription login can use the plan; an API-key route can incur separate API charges. Do not enable extra usage or substitute API billing without authorization. See [current billing evidence](references/routing-policy.md#subscription-billing-update-october-1-2026).

For Opus 5.5's long runs and custom API harnesses, read the focused
[release assessment](references/opus-5-5-review.md). It covers effort, actual alias
resolution, migration breaks, progress delivery and completion checks. Better native
delegation does not authorize more agents: keep exact ownership and one writer,
count duplicated context, and measure accepted work. API savings and output speed
do not establish subscription burn or native Claude Code completion time.

If host choice is genuinely open for a new substantial UI task, Opus 5.5 is a
strong quality-focused Claude route based on the current WebDev evidence. In an
active Codex task, retain the Codex table and preserve useful context; any cross-host
handoff must be available, authorized and worth its startup/integration cost.

### If you are Codex

Resolve the active model, supported efforts, available agents, and user constraints
against the current host catalog. As reviewed October 1, 2026, the current family
contains GPT-6 Astra, GPT-6.1 Sol, and GPT-6 Luna; Terra remains GPT-5.6 Terra where offered. Do not
invent GPT-6 Terra, declare Terra retired, or silently change a selected model.

**Use GPT-6.1 Sol for substantial everyday and complex work; reserve Astra for a
clear maximum-capability need.** Sol 6.1 is the default for demanding implementation,
architecture, diagnosis, synthesis, integration, and substantial UI work, including
new builds with a normal visual-quality bar. Select Astra directly for the hardest
cross-system judgment, exceptionally difficult unresolved creative/spatial direction
where maximum quality matters, or a demonstrated Sol 6.1 capability limit. The newer
Arena WebDev evidence narrows but does not reverse Astra's measured Max-effort visual
edge; it no longer justifies a blanket Astra route for every substantial UI build.
Do not require a failed Sol attempt before an obviously harder quality-first task.
Preserve a progressing capable parent; a new release alone does not justify a handoff.

Use Luna for stable, narrow, repeatable work with objective checks. Terra is a
conditional reading specialist, not the automatic scout: use it when the user prefers
it or representative workload evidence supports it. For a straightforward inventory or
extraction, consider Luna; use Sol when interpreting the evidence requires substantial
judgment. Neither token prices nor older benchmark rows establish a current speed or
quality ranking across these tasks. See [the evidence basis](references/routing-basis.md).

| Route | Use it for | Default configuration | Write policy |
|---|---|---|---|
| Current capable parent | Trivial or tightly coupled work, orchestration, integration, final verification | Active model and effort | May write |
| GPT-6 Astra parent or explicitly configured built-in agent | Hardest diagnosis or synthesis; exceptionally difficult unresolved creative/spatial direction with maximum quality at stake; demonstrated Sol 6.1 capability limit | GPT-6 Astra; high for new demanding work, preserve active setting when progressing | Parent owns decisions; child read-only unless sole writer |
| GPT-6.1 Sol parent or bounded built-in agent | Substantial everyday and complex reasoning, implementation, architecture, diagnosis, synthesis, integration, and typical substantial UI builds | GPT-6.1 Sol; medium ordinarily, high for complex work | Parent writes; child read-only unless sole writer |
| Explicit Sol xhigh route | Difficult architecture, diagnosis, or reasoning with unresolved dependencies that merits more depth within Sol | GPT-6.1 Sol, xhigh; may be chosen upfront when warranted | Parent writes; child read-only unless sole writer |
| Explicit Astra xhigh route | Exceptionally demanding reasoning or creative/spatial judgment with difficult unresolved tradeoffs | GPT-6 Astra, xhigh; may be chosen upfront when warranted | Parent owns decisions; child read-only unless sole writer |
| `sol-advisor` | Bounded judgment, quick review, UX opinion, or first-pass diagnosis | GPT-6.1 Sol, medium | Read-only |
| Built-in Sol `worker` or parent Sol | Defined multi-file implementation beyond Luna's scope | GPT-6.1 Sol, normally high; verify effective model | Sole writer |
| `terra-explorer` | Independent reading or evidence extraction when user preference or workload evidence warrants this route | GPT-5.6 Terra, medium; only if currently available | Read-only; capable parent owns consequential synthesis |
| Built-in Luna reader or `luna-builder` | Small inventories, extraction, narrow clear implementation, mechanical changes with objective checks | GPT-6 Luna, normally high; use a read-only role for reading | Sole writer only when implementation is assigned |
| `luna-economy-worker` | Stable bounded background work with explicit cost-first preference and acceptable validation cost | GPT-6 Luna, max; conditional named profile, not proof of lowest cost | Sole writer |
| `sol-architect` | Complex bounded specialist work when Sol is sufficient and a handoff helps | GPT-6.1 Sol, high | Read-only |
| `sol-critical` | Critical independent review within the deliberately selected Sol family | GPT-6.1 Sol, max; not a required step before Astra | Read-only |

Keep delegation bounded and useful alongside parent work. A smaller model or a cheaper
token rate need not shorten completion after context loading, retries, review, and
integration. Do not launch a model tournament for ordinary work. When routing itself
is disputed, compare a representative task at the same acceptance criteria, tool access
and service tier; record accepted quality, elapsed time, retries and review effort.

**Effort:** preserve an effective active setting. Sol medium fits ordinary substantial
work; high fits complex reasoning. Astra medium fits ordinary work when already active;
high is the usual starting point for new unusually demanding work. **Sol xhigh** is an
explicit choice for deeper reasoning, architecture or diagnosis within Sol. **Astra
xhigh** is an explicit choice for exceptionally demanding reasoning or creative/spatial
judgment. Either xhigh route may be selected upfront when the required depth is clear;
a failed high-effort attempt is not a prerequisite.

Increase effort when depth is missing; choose Astra directly when the task calls for
the highest capability, or when adequate context and a serious Sol attempt reveal a
judgment limit. Do not exhaust Sol's effort levels before considering Astra. Max and
ultra need a specific justification, not merely an executive audience, visual artifact
or long task. Check ultra's current delegation behavior, especially under a single-agent
constraint. Luna economy's configured max is a conditional exception, not a general
cost benchmark. These are task-based starting recommendations, not a measured ranking
of every model/effort combination; higher effort does not guarantee a better result.

**Model constraints and inheritance:** an explicit family choice applies to parent and
children. Do not silently substitute Luna, Terra, Sol, or Astra. A `worker` or `explorer`
name does not select a model; named profiles retain their configured models. Follow host
restrictions on overrides and context inheritance, and verify the actual configuration.
If no compatible child exists, stay in the compatible parent; if neither is available,
explain the limit. A plugin update does not update standalone profiles already copied
into user/project directories or models already loaded in a task. Use the supported
profile sync workflow when authorized.

No custom Astra profile is required: use the Astra parent or a supported built-in agent
explicitly configured for Astra. For unavailable optional routes, choose a permitted
capable parent or compatible built-in agent and state the substitution. Never claim to
switch a running parent's model, effort, or service tier without application confirmation.


## Benchmark evidence for routing

When reviewing releases or changing comparative routing guidance, use
[the regular benchmark sources and comparison rules](references/benchmark-sources.md):
Arena's task-relevant boards, Artificial Analysis, and original task-specific evaluators
such as SWE-bench/DeepSWE, Terminal-Bench, METR or OSWorld. Verify availability and
supported settings with the host/provider. Apply this to Codex and Claude routes.

Record dated results, model/effort/harness, uncertainty and limitations; distinguish
preference, success, capability, cost and latency. Do not dismiss relevant UI evidence
because no universal design benchmark exists, or promote a Max result into proof for
other efforts. Refresh for new releases, material evidence changes or disputed routes;
reuse the assessment during ordinary work rather than browsing every board each time.
This policy does not create a scheduled monitor. See [the current assessment](references/routing-basis.md).

## Token and latency controls

Use ordered preferences, not a fixed percentage weighting: total elapsed time first,
reliable completion second, and token use third by default. Explicit timing, quality
and budget choices can change that order. Compare routes that can meet the acceptance
criteria; a fast incorrect attempt is not completion. For cost-first work, count the
whole job: input and duplicated context, reasoning and output, subagents, retries,
verification and integration. Where available, record actual usage and accepted
completion time; label estimates and missing measurements. API token prices do not
directly measure Codex subscription consumption.

- Keep the routing skill and agent prompt concise; pass only the objective, exact inputs, owned files, acceptance criteria, and return format.
- Do not copy the full conversation into a subagent. Summarize only the facts it needs.
- Prefer one scout over several overlapping scouts.
- Parallelize independent read-only questions; serialize dependent work.
- Do not ask a writing agent to re-discover context the parent already has. Give it the precise file map.
- Stop escalation once the acceptance criteria are satisfied.
- Switch families at a phase or compaction boundary, not mid-turn. The prompt cache is per-model, so changing family rewrites the whole cached prefix at the cache-write premium. That cost is real but small; it is a reason to time the switch, never a reason to finish substantial work on a route you have already judged wrong.
- In Codex, justify `max` or `ultra` against the task and supported host settings; importance alone is insufficient. A critical review or documented strong failure can justify extra effort. The named Luna economy profile is a conditional exception, not a universal cost result.
- In Claude Code, retain the dated dominance guidance in the Claude table and its evidence reference. Do not apply its cross-family effort ranking to Codex models.

## Save usage without lowering the quality bar

When the user asks for lower usage at the same or better quality, treat quality as a
constraint and optimize total usage among acceptable routes; do not simply lower every
model or effort setting. Begin with redundant context and repeated work. Use a verbatim
current-state view with targeted source reads, retain historical evidence on demand,
and preserve unresolved limits, failed approaches and required verification. Do not
replace meaningful context with an untested lossy summary.

Use scripts and cached results for deterministic work; avoid rerunning accepted checks
on unchanged inputs unless a new concern requires it. Keep rendered checks, critical
review and demanding creative/spatial judgment. Introduce a decision model such as Jev
only when a representative comparison shows less total usage at the same acceptance
bar, including retries, review and integration. A new key or impressive demo alone
does not establish savings or authorize spending. See the conditional
[usage-saving procedure and evidence limits](references/usage-economy.md).

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
- In Sol, use medium to high when depth is missing; choose Sol xhigh when deeper
  reasoning is justified, including upfront for a clearly exceptional task.
- Select Astra directly for the hardest quality-first work or a demonstrated capability
  limit. Astra high is the usual demanding-work start; Astra xhigh fits exceptionally
  deep reasoning or creative/spatial judgment and can also be selected upfront. No
  mandatory failed high attempt or Sol max-first ladder applies. Preserve a progressing
  Astra parent and its loaded context. Do not equate Sol 6.1's release with proven superior design.
- Return ambiguous Luna work and judgment-heavy Terra findings to the capable Sol or
  Astra owner. Do not ask a bounded reader to make the consequential synthesis.
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

The sync tool stores backups outside the scanned agents directory and relocates old
nested backups on apply. It backs up changed or renamed profiles, retires only known legacy names, and never deletes unrelated profiles. Do not hand-edit global routing configuration as part of this workflow.

Load detailed references only when needed:

- Read [references/routing-scenarios.md](references/routing-scenarios.md) for representative decisions and review cases.
- Read [references/routing-basis.md](references/routing-basis.md) for the distilled policy, migration logic, and current-product overlay.
- Historical source packs below predate GPT-6 Sol and Luna and do not override this policy.
- Read [references/source-shared-routing-guide.md](references/source-shared-routing-guide.md) when revising task, timeliness, harness, or mixed-workflow routes.
- Read [references/source-codex-agents.md](references/source-codex-agents.md) when revising agent behavior, delegation, or quality gates.
- Read [references/source-wall-clock-evidence.md](references/source-wall-clock-evidence.md) when comparing measured completion time, cost, steps, or tokens. Search this large reference by model name or benchmark before reading broad sections.
- Read [references/source-research-evidence.md](references/source-research-evidence.md) when reviewing model, effort, harness, context-management, or cross-harness research. Search this large reference for the exact claim or model first.
