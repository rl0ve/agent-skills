---
name: route-ai-work
description: Choose model, effort, orchestration and execution location for agent work, including subagents, separate threads, remote machines and cloud tasks. Use for routing decisions, coordinated work, private project context, conditional native goals, workflow conflicts or improvements. Check host capabilities and authorization before dispatch. Ordinary contained work stays in the parent.
compatibility: Claude Code and Codex. Each has its own route table below; the method is the same.
---

# Route AI Work

Choose the route that can reliably finish with the least total elapsed time, including
handoffs, retries and integration. Order: elapsed time first, reliable completion
second, token use third, unless the user sets a different order. A smaller model is
not automatically faster.

## Overrides and timing

- **Explicit user choices win:** model, effort, timing, budget, delegation and safety.
  A locked model applies to children too. Persist an override only when asked; use
  [the override contract](references/model-routes.md#routing-overrides-full-contract).
- **Timing from language:** "fast/now" → Fast; "balanced" → Balanced; "cheapest" →
  Economy; "quality first/executive-critical" → Quality-first. No signal → Fast for
  ordinary interactive work. Ask one short timing question only when the answer would
  materially change the route. [Full rules](references/model-routes.md#timing-full-rules).
- **Codex Fast and Ultrafast service tiers** are separate from Fast routing. Never
  enable either or claim it is active without application confirmation. Ultrafast
  (Astra and Sol) bills far above Standard; offer it only when the user asks or a
  stated deadline repays the cost, never as a default.
  [Service tiers](references/model-routes.md#timing-full-rules).
- **Host-native harness:** host-sensitive workflows such as Dream Loop run in the host
  the user is in (Codex → GPT-6 Astra, Claude Code → Claude Opus 5.5) unless the user
  names another model for that run. Never move work to another host to match an
  upstream harness; a cross-host handoff needs availability, authorization and a
  benefit that repays its startup and integration cost.
- **Fidelity rounds** (Dream Loop or the visual build loop) start at medium effort and
  stop after 2–3 rounds or when the recorded gaps close. Raise effort only when a round
  at the current level stops closing gaps.
  [Rounds and effort](references/model-routes.md#fidelity-rounds).

## Route the task

1. Honor explicit model, effort, timing, budget, delegation and safety choices.
2. Check context before changing a knob. Missing requirements or files are not a model failure.
3. Keep trivial, tightly coupled or already-contained work in the parent.
4. Choose execution location and one orchestration owner using the section below.
   Delegate only when isolation, specialist capability or independent work repays
   startup, duplicated context, transfer, review and integration costs.
5. **One write-capable owner per working tree.** Never run the parent and a writing
   subagent against overlapping files at the same time.
6. Choose the initial model and effort from the task. Astra or xhigh can be chosen
   upfront when warranted; no failed lower attempt is required.
7. After an inadequate attempt, fix context or tools first; then add effort for missing
   depth, or a stronger model for missing capability or judgment.
8. Count total completion cost: retries, review and integration, not token price alone.

Before substantial work and at phase boundaries, [reassess the main thread's model
and effort](references/model-routes.md#reassess-the-main-thread). Give one brief
recommendation when a change would materially help, respecting explicit choices.
Separate the recommendation from a confirmed host setting change.

Before a substantial retry or refinement loop, use the
[loop controls](references/long-running-work.md#define-the-loop-before-repeating-attempts)
to establish verification, applicable limits, progress checks and recovery. Continue
useful work within scope; repeated activity alone does not establish progress.

## Choose where work runs and who coordinates it

Execution location is separate from model, effort, service tier and engineering method.
Use the current task by default. Consider a bounded subagent for independent work within
the task; an existing or new thread for a durable workstream; a connected remote machine
for its files, tools or compute; and a cloud task for portable work with a reviewable
return artifact. A separate chat is not automatically an isolated checkout or a remote
executor. Moving the active work and creating a parallel worker are different actions.

When one of these routes would help, read [execution locations](references/execution-locations.md)
for selection, capability checks, authorization, dispatch, handoff and integration.
Inspect relevant existing work before creating duplicates. Recommend a route freely;
execute it only within the user's authorization and the live tool contract. A request
to improve this router does not itself authorize new tasks or messages to other chats.

During coordinated work, [reassess routes at meaningful checkpoints](references/execution-locations.md#reassess-at-coordination-checkpoints),
including phase completion and before closing an authorized work window. An initial
local choice does not settle the route for later independent work.

When tasks need shared decisions across sessions or environments, use
[private project state](references/shared-project-state.md). Scope it by project,
with optional repository links; desktop Work and other local projects can have no
Git repository. Keep private context out of public Git history, verify access and revision,
and reconcile worker returns through one acceptance owner.

Choose one owner of decomposition, dispatch and acceptance. When Ultra or an explicitly
selected development workflow already owns orchestration, avoid adding another manager
or duplicate agents. Read [orchestration compatibility](references/orchestration-compatibility.md)
for host-specific Ultra behavior, Superpowers and other engineering frameworks. Work
Router can supply constraints and location choice while that owner executes the plan.

## Decide whether a native goal helps

For work likely to need continued execution across turns, or when the user asks about
goals, apply [the native-goal policy](references/native-goals.md) once in the owning
chat. Automatic creation requires a bounded outcome, verifiable finish and material
continuation benefit. A user's explicit request for a specific goal overrides that
usefulness recommendation, subject to host rules. With applicable authorization and
host support, inspect current state, reuse a matching active goal, or create one when
none is unfinished. Ordinary edits and one-off reviews or audits need no automatic
goal. Loading this skill or judging a task substantial is not consent. UI Router
defers this decision here.

When instructions, scope or acceptance conditions change, [reconcile the active goal](references/native-goals.md#reconcile-the-goal-as-work-changes).
Apply clear user changes without asking again. Distinguish a revised working plan from
a confirmed change to the host's registered objective; inspect the supported controls.

## Notice reusable workflow improvements

At meaningful checkpoints, a recurring routing problem, a clear reusable correction
or a verified capability change may warrant an improvement. Use
[workflow feedback](references/workflow-feedback.md) to distinguish project fixes,
personal preferences and shared skill changes, then propose the smallest supported
correction. Keep current work moving and avoid routine audits or repeated prompts.

For new capabilities use [discover-capabilities](../discover-capabilities/SKILL.md); for
duplicate skills use [deduplicate-skills](../deduplicate-skills/SKILL.md). Neither runs
on ordinary tasks; use existing capabilities first, and finding a duplicate is not
permission to remove it. UI Router owns design selection; this skill owns execution.

## Default routes

Read the table for the host you are running in and ignore the other.

### If you are Claude Code

Prefer **Opus 5.5 at medium** for new substantial work. Verify `opus` resolves to
`claude-opus-5-5` (Claude Code 2.1.280+). If exactly 5.5 is required and unavailable,
report it rather than substituting.

| Work shape | Route | Model | Effort | Notes |
|---|---|---|---|---|
| One-step, tightly coupled, or conversational | Parent | active model | active effort | Delegation overhead would dominate. |
| Narrow lookup, classification, repository map, or evidence collection | `work-router:fast-scout` | Haiku | low | Read-only; return compact evidence. `haiku` is 5.5 only on the Anthropic API with 2.1.293+. |
| Defined implementation with clear acceptance criteria | `work-router:sonnet-builder` | Sonnet | medium | Sole writer; verify proportionately. |
| Substantial implementation, planning, synthesis, or a multi-file change | Parent | Opus 5.5 | medium | New substantial-work default; preserve useful parent context. |
| Difficult diagnosis, architecture, or consequential tradeoff | `work-router:opus-architect` | Opus 5.5 | high | Read-only by default; parent integrates. |
| High-stakes final review after a strong implementation | `work-router:critical-reviewer` | Opus 5.5 | xhigh | Read-only; justify added depth by the critical boundary and verify its benefit. |
| Long-horizon, multi-stage autonomous project | Parent or sole assigned writer | Opus 5.5 | medium or high | Start with bounded phases; duration alone does not require Fable or delegation. |
| Prose whose quality is the deliverable: talk track, narration, naming, UX copy, executive writing, voice match | Parent with Natural Writing | Opus 5.5 | medium | Preserve facts and register; judge the delivered prose. |
| A demonstrated Opus 5.5 capability/style limit or explicit Fable choice | `work-router:fable-runner` or `work-router:fable-wordsmith` | Fable | high | Conditional specialist; runner is sole writer, wordsmith returns text for parent review. |

`work-router:haiku-builder` (Haiku, high) is an opt-in, untested sole writer for
mechanical edits with objective checks; use it only when the user or an override
names it. Calibration, Haiku 5.5, Fable and billing notes:
[Claude Code detail](references/model-routes.md#claude-code-calibration-billing-and-host-choice).

### If you are Codex

Resolve the active model, efforts and agents against the current host catalog. Use
**GPT-6.1 Sol** for substantial everyday and complex work, **GPT-6 Astra** for a clear
maximum-capability need or a demonstrated Sol limit, and **GPT-6 Luna** for narrow work
with objective checks. Never silently change a selected model.

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

**Effort:** Sol medium for ordinary substantial work, high for complex reasoning; Astra
high for new demanding work. xhigh is an explicit upfront choice when depth is clearly
needed. Max and ultra need a specific justification. Detail:
[Codex family policy](references/model-routes.md#codex-family-policy-and-narrative).

## Keep context lean

- Pass only the objective, exact inputs, owned files, acceptance criteria and return format.
- Do not copy the conversation into a subagent; give the precise file map.
- One scout over several overlapping scouts. Parallelize independent reads; serialize dependent work.
- Switch model families at a phase or compaction boundary, not mid-turn.
- Stop escalating once the acceptance criteria are met.
- For lower usage at the same quality, follow
  [the usage procedure](references/usage-economy.md); quality stays a constraint.

## Delegate safely

Before substantial delegated work, announce exactly:

`Route: <agent> (<model>, <effort>) - <one-line reason>`

Give each subagent a bounded prompt containing:

- objective and relevant inputs;
- owned or allowed files;
- acceptance criteria and required validation;
- required return: concise findings or diff summary, exact checks, and unresolved risks;
- a reminder that other agents may be active and their edits must not be reverted.

Avoid recursive delegation trees. The parent remains responsible for requirements,
decisions, integration, final validation and the user-facing answer.

## Escalate deliberately

- Fix missing context or a faulty tool/validation path before raising capability.
- Return ambiguous Luna work and judgment-heavy reader findings to the capable owner.
- Do not escalate solely because work is slow or difficult.
- Never execute an irreversible action without explicit user confirmation.

## Host notes

- **Portable user preferences:** when a user asks to carry their workflow between
  environments, use [profile setup](references/portable-preferences.md). Explicitly
  select the profile and host, preview, apply and verify. Shipped templates are inert;
  loading or installing this plugin never opts a user into personal preferences.
- **Work accounts:** use [work-account setup](references/work-account-setup.md) for
  separate private project records, managed policies and per-environment verification.
  A sign-in change or realm label alone does not establish data isolation.
- **Claude Code managed workspaces:** model aliases and effort levels are requests;
  company `availableModels`, effort caps and provider mappings win. Report the actual
  model when Claude Code substitutes one, and do not bypass company policy.
- **Codex agent profiles:** to install or refresh them, run
  `scripts/sync_agent_profiles.py` as a dry run, get approval, then `--apply`, and tell
  the user to start a new task. [Details](references/model-routes.md#codex-custom-agent-profiles).

## References

- [model-routes.md](references/model-routes.md): full override, timing, Claude, Codex,
  benchmark, token, long-task, escalation and host-specific notes (managed workspaces,
  Codex profile sync).
- [long-running-work.md](references/long-running-work.md): multi-phase work, Claude Code
  dynamic workflows, loop limits and progress checks, Codex cross-window notes and outside advice.
- [execution-locations.md](references/execution-locations.md): current task, subagents,
  separate threads, remote and cloud execution; dispatch and return contracts.
- [shared-project-state.md](references/shared-project-state.md): private project scope,
  local and shared storage, revisions, worker returns and evidence consolidation.
- [work-account-setup.md](references/work-account-setup.md): reuse the public method in
  a work environment without importing personal records; includes desktop Work without Git.
- [orchestration-compatibility.md](references/orchestration-compatibility.md): one
  coordinator with native Ultra, Superpowers or another development workflow.
- [native-goals.md](references/native-goals.md): conditional creation, standing opt-in,
  goal reconciliation, existing-goal ownership and host lifecycle rules.
- [workflow-feedback.md](references/workflow-feedback.md): evidence-based improvement
  suggestions during active work, scoped ownership and authorized maintenance.
- [routing-scenarios.md](references/routing-scenarios.md): representative decisions.
- [routing-basis.md](references/routing-basis.md): distilled policy and current-product overlay.
- [benchmark-sources.md](references/benchmark-sources.md): release reviews and comparisons.
- [opus-5-5-review.md](references/opus-5-5-review.md): Opus 5.5 long runs and API harnesses.
- [haiku-5-5-review.md](references/haiku-5-5-review.md): Haiku 5.5 alias gate, scout and opt-in builder.
- Historical source packs (`source-*.md`) predate GPT-6 Sol and Luna and do not override
  this policy; search them by model or claim rather than reading them whole.
