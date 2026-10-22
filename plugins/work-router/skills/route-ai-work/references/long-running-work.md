# Bounded progress on long tasks

Use for several dependent phases, repeated loss of context, or stalled progress caused
by polishing already adequate work. Keep ordinary edits in the parent without creating
a manager, dashboard, or elaborate checklist.

For work that benefits from continued execution across turns, first apply the
[native-goal policy](native-goals.md). A goal can keep a bounded outcome active;
it does not replace the phase plan, evidence or authorization checks below.

When phases span separate threads, remote machines or cloud tasks, use
[execution locations](execution-locations.md) for destination checks, one coordinator,
isolated writers and verified return/integration. Native orchestration or a selected
engineering workflow may own a phase; resolve overlap through
[orchestration compatibility](orchestration-compatibility.md).

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

Use the [coordination checkpoint](execution-locations.md#reassess-at-coordination-checkpoints)
to choose where the next useful work should run. Recheck when a worker becomes free,
a dependency blocks progress, scope or timing changes, and before closing an authorized
work window. Preserve the existing coordinator and integration owner.

At a checkpoint, compare progress against the user's highest-priority unmet condition,
not only the easiest things to count. More content, tests, assets or minor refinements
do not compensate for an unresolved core requirement such as visual fidelity,
interactive behavior or deployment. When that condition survives repeated passes,
identify the limiting cause and make the next useful phase test a materially different
approach or resolve its prerequisite. Expand breadth when it advances the outcome;
do not use it to avoid the difficult acceptance decision. Keep implementation scores,
verified coverage and measured user outcomes separate. Preserve optional opportunities
as such instead of continually promoting them into new completion requirements.

Adapt the implementation plan when new facts invalidate it, recording the reason and
preserving the user's requested outcome. Ask only for a material decision that cannot
be inferred within the authorized scope.

If a restart or handoff is necessary, pass the accepted decisions, exact artifacts,
remaining checks, known failures and next action. Use normal context management while
it works; a fresh agent for every phase is an experiment, not a default. Verify current
project state before the replacement continues. Stop when the requested outcome and
required checks are complete, or report the actual blocking condition under host rules.

## Resume interrupted external work from current evidence

After interruption, first inspect the owned artifact and exact process/job/tab handle
that was in flight. Retain job IDs, output paths and pending checks in the checkpoint;
record observations separately from intended next steps. A stale summary, former port,
or saved lock is not proof a service is still running. A polling timeout is not proof
it stopped: re-poll the same handle or check another authoritative signal before
restarting. Confirm termination or a missing handle before replacing a local process.
For an ambiguous paid submission, follow the provider's recovery path rather than
risking a duplicate charge. Reconnect only the affected handles; preserve user state
and avoid rerunning accepted research, builds or actions without a relevant change.

## Host-native long-task features

Use a host feature when it fits the work's shape; do not rebuild it by hand, and do not
turn it on just because it exists. Both features below change cost or configuration, so
they follow the host's authorization rules.

**Claude Code dynamic workflows.** Claude writes a JavaScript orchestration script that
runs many subagents in the background and can be saved and rerun as a command. Fit:
the same check or edit across many files or items, large migrations, codebase-wide
audits, research whose claims must be cross-checked, several independent drafts of a
plan, or a checker-and-fix cycle that repeats until it passes or stops improving. Not a
fit: ordinary edits, work one conversation can coordinate, or work that needs the user
between stages.

- **Opt in per task.** "Use a workflow" or the `ultracode` keyword in a typed prompt
  opts one task in; `/effort ultracode` opts in every substantive task in the session,
  removes the large-run warning and the concurrent-subagent limit, and sets `xhigh` when
  started from the command line. Keep it per task unless the whole session is fan-out
  work. The keyword counts only as human input, so a `claude -p` call, a scheduled
  prompt or a relayed comment does not start a workflow.
- **No input mid-run.** A run pauses only for permission prompts or usage limits. Run
  each stage that needs sign-off as its own workflow.
- **Cost.** Workflows can use meaningfully more tokens than the same task in
  conversation and count toward plan limits. Start with a scoped run to gauge usage
  before a codebase-wide one.
- **Acceptance stays with the parent.** Inspect the result and run the checks; agent
  votes or reviewer agreement do not replace them. `/deep-research` is the built-in
  cross-checked research workflow and needs web search.

**Codex cross-window notes with Astra.** OpenAI describes an experimental mode in which
Astra keeps notes across context windows and can search earlier windows instead of
compressing them into one summary. It is set in the Codex config under
`features.context_management`, and OpenAI says it will become the Astra default. As of
October 20, 2026, the Codex configuration reference still lists it as not currently
available, so check the installed client before relying on it. When it is active, prefer
it over a hand-written handoff for an unfinished Astra session. Still write the
state-spec file below when the work changes model, agent or host, because notes stay
inside one Codex task.

Sources, checked October 20, 2026: [Claude Code dynamic workflows](https://code.claude.com/docs/en/workflows),
[Anthropic launch article](https://claude.com/resources/articles/introducing-dynamic-workflows-in-claude-code),
[OpenAI GPT-6 Astra](https://openai.com/index/gpt-6-astra/),
[Codex configuration reference](https://developers.openai.com/codex/config-reference).

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
