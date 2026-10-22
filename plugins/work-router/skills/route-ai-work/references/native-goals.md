# Conditional native goals

Work Router owns this decision for all work, including UI and 3D. Evaluate it once in
the chat responsible for acceptance and integration. A native goal supports continued
execution toward an outcome; a plan organizes steps, a checkpoint preserves evidence,
and a schedule wakes work later. These are different capabilities.

## Fit and authorization

Use a goal when **all three** are true:

1. The already-authorized task has one bounded outcome and concrete completion checks.
2. Several dependent phases, asynchronous results or a repeated repair-and-check cycle
   make continued execution across turns materially useful.
3. The owning agent can make progress without inventing scope or waiting on a missing
   prerequisite that prevents any useful work from starting.

Examples: integrate several completed branches, resolve conflicts and verify the
combined result; or implement a defined interaction, inspect rendered behavior and
repair failures through a fixed acceptance gate. State the actual finish line, not
"keep improving the product." Duration, difficulty, model choice, credits available,
the number of agents and a high visual score request are insufficient by themselves.

Skip goals for routine fixes, one-off reviews, bounded audits, research answers and
short visual passes that can finish normally. Also skip open-ended coordination,
indefinite monitoring and a separate goal for every child, phase or fidelity round.
Reassess if the work actually becomes a qualifying multi-turn task. An explicit user
request for a specific goal may override this usefulness recommendation, within host
rules; an explicit no-goal instruction always wins.

Inspect the current host's available goal tools and instructions. When they require
an explicit user, system or developer request, neither skill loading nor this policy
supplies that permission. An explicit current request or an applicable user-authored
standing opt-in may supply it if the host permits that form of authorization. Merely
discussing goals, asking how they work, or saying "finish the task" is not such an opt-in.
Without authorization, continue the authorized work normally. Recommend a goal only
if its benefit is material; do not turn its absence into a blocker or repeated prompt.

When the user explicitly asks for automatic goal use, a narrowly scoped standing
preference can say:

> For my already-authorized tasks, use a native goal automatically when Work Router's
> native-goal policy finds a bounded outcome, verifiable finish and material benefit
> from continuation across turns. This is my standing request for that conditional
> goal creation in the current owning chat, subject to the host's rules. Do not create
> goals for routine edits, one-off audits/reviews or indefinite project work. Do not
> replace an unfinished goal. A later no-goal instruction overrides this preference.

Persist that preference only when the user asks for ongoing automatic use, in the
host's supported user-instruction location; preserve other instructions. Keep personal
opt-ins out of the published plugin. State which host was updated; another machine,
cloud executor or already-running chat may not have loaded it.

## Inspect, then act once

- Read live goal state before mutation. Use `get_goal` when provided; an equivalent
  authoritative host surface is acceptable. If state cannot be inspected, continue
  normally and report the limitation when relevant rather than guessing or retrying
  blind creation. A stop-only goal tool is not a creation capability.
- **Matching active goal:** reuse it. Do not create a duplicate or silently broaden
  its objective to cover unrelated new work.
- **Unrelated unfinished goal:** preserve it. Do not complete, block, pause or replace
  it to free a slot. Continue separable authorized work normally; obtain user direction
  only if the ownership conflict prevents useful progress.
- **Paused, blocked or budget-limited goal:** follow the host's resume rules. This
  standing creation preference does not authorize resuming a user's paused goal or
  bypassing a limit. A completed goal may be followed by a new qualifying goal; do not
  reopen accepted work without new evidence or a changed requirement.
- **No unfinished goal:** with automatic-use fit or an explicit specific-goal request,
  plus authority and a creation tool confirmed, create one concrete objective with
  its completion conditions. Supply a token budget only
  when explicitly requested; never invent one from account balances or estimates.
- Check the tool result before saying the goal is active. If creation fails or has an
  uncertain outcome, inspect state before retrying. State "continuing without a native
  goal" when that distinction matters; a Markdown checkbox is not a registered goal.

The accepting parent owns the goal. A child's bounded assignment normally reports
back to that parent without creating another goal. Native goals never authorize new
chats, recurring automations, extra workers, model or service-tier changes, purchases,
paid APIs, usage resets or actions outside the user's task.

## Lifecycle and stopping

Continue against the existing acceptance conditions and preserve a concise checkpoint
at useful phase boundaries. Do not poll goal status after every tool call. Inspect it
again after interruption or when the host indicates a state or budget change.

Follow the live tool contract for lifecycle actions. In Codex hosts exposing
`create_goal`, `get_goal` and `update_goal`, the current contract requires:

- Mark complete only after the objective and required checks are actually finished.
  A pushed branch, passing unit tests or an advisory review alone may leave required
  integration, rendered checks or delivery unfinished. Do not add optional polish to
  keep a satisfied goal running, or claim completion to avoid a budget limit.
  Exhausting a refinement-round cap does not satisfy an unmet quality requirement.
- Pause only on the user's explicit request. Report the returned state and stop goal
  work; do not use pause as the agent's discretionary exit.
- Mark blocked only after the same blocker has recurred for at least three consecutive
  goal turns and no meaningful progress remains without user input or external change.
  Slow or difficult work is not blocked. Resuming a previously blocked goal starts a
  fresh blocker audit. Once the host's threshold is met, actually mark it blocked.
- Honor host budget/usage limits. If a budgeted goal completes, report the final usage
  returned by the tool when required. A near-exhausted budget does not mean success.

These names and semantics are a host adapter, not a universal API. If another host
lacks native goals, use its normal plan/checkpoint and finish the task; do not emulate
goals with hooks, background scripts or schedules, or switch hosts just to obtain one.
This is a routing policy with scenario review, not a claim that every host implements
goals or that installing the plugin changes an already-running session.
