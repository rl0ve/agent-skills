# Changelog

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
