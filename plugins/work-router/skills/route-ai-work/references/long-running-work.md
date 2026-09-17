# Bounded progress on long tasks

Use for several dependent phases, repeated loss of context, or stalled progress caused
by polishing already adequate work. Keep ordinary edits in the parent without creating
a manager, dashboard, or elaborate checklist.

## Phase ownership and completion

Keep the overall user outcome and required scope visible, but detail only the current
phase and the next dependencies. For each phase record:

- the outcome and owned files or artifacts;
- concrete acceptance conditions and the checks that establish them;
- dependencies, unresolved decisions and authorized limits;
- the next handoff when the phase is accepted.

Prefer the existing issue, plan or project note. Create a small checkpoint only when
it will prevent rediscovery. A dashboard is useful when requested or when it makes a
long run meaningfully easier to inspect; box count alone is not progress evidence.

The parent owns scope, acceptance and integration. It can implement directly, or manage
one writing implementer when delegation is permitted and worthwhile. The implementer
returns changed artifacts, observed check results and remaining failures. Inspect those
results before accepting the phase; the agent's confidence or self-reported completion
does not establish correctness. Reuse a progressing implementer for related fixes.

When a consequential independent review is justified, keep it bounded and read-only.
Do not create user-visible tasks, persistent goals, recurring jobs, or additional agent
capacity merely to imitate a source's setup. Those are separate host capabilities with
their own authorization requirements.

## When progress slows

Look at the last verified outcome, unresolved blocker and work since then. Time without
a checked box may reflect useful diagnosis; easy checkboxes may hide missing behavior.
If work repeats without new evidence, diagnose the cause: missing input, broken tools,
unclear acceptance, difficult reasoning, or optional polish. Repair the relevant cause
or make progress on an independent requirement. Never skip a required dependency just
to improve the progress chart, weaken a failing test, or silently drop scope.

Once acceptance is met, move on. Reopen a completed phase for new evidence or a changed
requirement, not an unlimited request for perfection. A phase boundary is a checkpoint,
not a reason to stop before the user's full task is complete.

Adapt the implementation plan when new facts invalidate it, recording the reason and
preserving the user's requested outcome. Ask only for a material decision that cannot
be inferred within the authorized scope.

If a restart or handoff is necessary, pass the accepted decisions, exact artifacts,
remaining checks, known failures and next action. Use normal context management while
it works; a fresh agent for every phase is an experiment, not a default. Verify current
project state before the replacement continues. Stop when the requested outcome and
required checks are complete, or report the actual blocking condition under host rules.

## Handoff and context at a phase boundary

Carrying a large transcript forward is not the lossless option people assume it is. The
realistic choice is between a summary you wrote and a summary you did not. Auto-compaction
fires after the degradation, not before it, so decisions made in the crowded window are
already made and cannot be undone by compacting afterwards. Successive compactions
summarize summaries.

- **Write the handoff as a state spec, not a conversation recap.** Current contracts and
  interfaces as they now stand; architectural decisions; naming conventions and constraints
  found by trial; done, in progress, next; known traps and dead ends.
- **Include the rejected alternatives and why they were rejected.** This is the part that
  exists only in the transcript and the part a lossy summary drops first, and losing it is
  what makes a replacement re-walk work you already ruled out.
- **Write it to a file, not a message.** Files survive whatever a summary keeps.
- **Expect the replacement to re-read files, and treat that as correct.** The repository is
  the source of truth; a long transcript contains superseded decisions. Re-reads land at the
  front of a clean window where recall is strongest. A small deliberate primer outperforms a
  large history on any model.
- **Time a family switch to this boundary.** The cache is being rebuilt anyway, so the
  cache-write cost of changing model disappears.

Prefer aimed compaction over a handoff when the task is unfinished, the reasoning chain
still matters and you can state explicitly what to keep. Prefer a clean restart when the
phase is separable, when the model has anchored on a wrong assumption that condensing would
carry forward, or when you have corrected the same mistake more than twice.

Context degradation is directional evidence, not a threshold to enforce. Reported ranges
vary widely by task and model, and the "lost in the middle" effect is measured on retrieval
benchmarks rather than on agentic coding. Use observed symptoms - instructions missed,
decisions contradicted, files re-read wrongly - ahead of any token count.

## Evidence and limits

Reviewed September 5, 2026. This is routing judgment, not a measured performance claim.

- [Matt Shumer, September 3](https://x.com/mattshumer_/status/2095723177389232540)
  reports improved long-task results with phased management. His large agent count,
  wording preference and progress chart are anecdotal; they do not establish defaults.
  His [September 4 follow-up](https://x.com/mattshumer_/status/2095724719408386326)
  explicitly labels fresh implementers and plan revision as untested suggestions.
- [Pablo Stanley, July 7](https://x.com/pablostanley/status/2074704410211467294)
  recommends scoped delegation, diff review and returning fixes to the same agent.
  Retain those methods where useful; his family assignments are not a current model
  benchmark and do not justify moving loaded context out of a capable parent.
- [Anthropic, November 26, 2025](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
  describes incremental work, durable progress artifacts and end-to-end checks in a
  particular coding harness. It leaves the relative benefit of multi-agent designs
  unresolved. This supports careful checkpoints, not a universal agent topology.
