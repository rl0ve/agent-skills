# Changelog

## 1.7.2 - 2026-09-20

- At long-task checkpoints, prioritize the highest-priority unmet requirement over
  easier growth in content, tests or assets. Repeated misses require cause diagnosis
  and a phase that changes the approach or resolves its prerequisite.
- Keep implementation scores and verified coverage separate from measured outcomes;
  preserve optional improvements without continually expanding completion scope.
- No model, effort, delegation or service-tier defaults change.

## 1.7.1 - 2026-09-17

- Correct the basis recorded for retiring Sonnet above medium. The direction now cites
  this repository's own harness evidence in `source-wall-clock-evidence.md` and
  `source-research-evidence.md` rather than a secondary score table.
- Record that the triggering synthesis quoted Intelligence Index scores for Sonnet 5 at
  medium and high, two settings for which this repository already verified that
  Artificial Analysis publishes no index. Those figures are unsourced.
- Note that Sonnet 5 high is the product's default effort, so narrowing Sonnet to low
  and medium is a deliberate departure from a default.

## 1.7.0 - 2026-09-17

- Retire Sonnet high, xhigh and max as routes. Sonnet medium is now the top of that
  family; the step above it is Opus low, not more Sonnet effort.
- Make Opus low the primary route for reasoning-dense implementation, in the parent,
  with Opus medium as the first escalation when it stalls or thrashes.
- Rank the Fable band explicitly and prefer Opus high/xhigh over Fable medium for long
  autonomous runs, since Fable bills separately.
- Declare `max` off the efficient frontier in every family.
- Add a retry-count rule: cost per completed task, not token price, decides the route.
- Record the caveats on Opus low: low effort does not shorten output and it delegates
  to subagents readily, so real burn can exceed a per-task estimate.
- Time a family switch to a phase or compaction boundary, because the prompt cache is
  per-model.
- Add phase-boundary handoff guidance: write a state spec rather than a conversation
  recap, keep the rejected alternatives with reasons, write to a file, and treat the
  replacement's re-reads as correct behavior.
- Document the basis for the dominance ordering and its four limits in
  `references/routing-policy.md`. It is a secondary synthesis over a composite
  benchmark, not an agentic-coding measurement.

## 1.6.0 - 2026-09-06

- Add `deduplicate-skills` as the owner for installed-skill consolidation across Codex,
  separate from capability discovery and domain-specific routing.
- Include a read-only inventory helper for explicit roots, exact listed plugin
  versions, symlink aliases, entrypoint/bundle fingerprints and disable-rule evidence.
- Distinguish copies, variants, competing owners, useful specialists and inactive
  remnants. Require scoped cleanup decisions, private backups and state verification;
  do not infer permission to remove skills from an audit request.
- Route overlap cleanup from Work Router and capability discovery without adding a
  global audit to ordinary tasks. Add regression checks for inventory safety and scope.

## 1.5.0 - 2026-09-05

- Add cross-domain capability discovery with a conditional source shortlist, installed-first checks, and explicit ownership of overlapping skills/plugins.

## 1.4.0 - 2026-09-05

- Add conditional long-task phases with explicit outcomes, ownership, acceptance
  evidence, stall diagnosis and compact handoffs. Keep routine work in the parent.
- Distinguish useful source methods from anecdotal agent counts, stale model routes,
  unexplained settings and untested context-reset suggestions.
- Preserve required scope when progress slows; phase completion is not whole-task
  completion. Extend routing review cases without claiming comparative benchmarks.

## 1.3.0 - 2026-09-05

- Make Codex routing Astra-aware: keep demanding work and loaded context in an
  active Astra parent; retain Sol, Terra, and Luna as deliberate bounded specialists.
- Separate effort escalation from model selection, and Fast routing from Codex Fast
  service. Preserve Standard service by default and explicit user model constraints.
- Verify child model/effort rather than assuming a built-in worker or a named Sol
  profile inherits Astra. No new custom profile or global settings change is required.
- Update bundled profile escalation, shared setup checks, documentation, and scenario
  guidance. Mark pre-Astra source packs as historical evidence.
- Basis: current host model catalog and routing judgment; no Astra speed/cost benchmark.

## 1.2.0

Adds `fable-wordsmith` and the rule that puts work there.

- **New agent: `work-router:fable-wordsmith`** (Fable, high, read-only). For prose whose
  quality is the deliverable: talk tracks, narration, naming, UX copy, executive writing,
  voice matching, line-level naturalness. It invokes natural-writing, runs that skill's
  linter per piece and across the set, preserves every fact, and returns keyed text for the
  parent to verify and apply. Read-only on purpose: prose edits are cheap to review and
  expensive to apply blindly.
- **Language work routes on a different axis.** The route table ranks families by reasoning
  difficulty, and that ranking does not carry to writing. Prose goes to the wordsmith rather
  than to `opus-architect` at any difficulty; Opus keeps prose only when the hard part is the
  argument or the facts rather than the words.
- **New escalation trigger.** A reader rejecting prose on feel rather than content ("this
  sounds off") is a language problem, not a reasoning one, and escalates to the wordsmith
  once the parent's own revision has failed to land.

Basis is one observed session, recorded as such in `references/routing-policy.md`, not a
benchmark.


## 1.0.0 - 2026-08-18

- Initial Claude Code-native release.
- Added task-first model and effort routing.
- Added five bounded subagents and one-writer guardrails.
- Added managed-workspace fallback behavior.
- Added deterministic `sudo` blocking hook.
