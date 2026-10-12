# Paired eval: slim 3D route vs. the 1.18.11 route

**Question:** does UI Router 1.19.0 with `route-3d-work` and Work Router 1.9.0 produce
accepted 3D work at least as well as 1.18.11 / 1.8.9, with fewer tokens or less time?

This compares the slim route to the current route, not router vs. no router: the safety
ledger and gates are kept in both arms.

## Setup

- **Arms:** A = tag or commit before 1.19.0 (`15f6ea8`); B = 1.19.0.
- **Host:** run both arms in the same host and model (host-native rule). Repeat in the
  other host only if you want a cross-host read.
- **Isolation:** a fresh Lumbre worktree per run from the same base commit; same
  installed specialists, MCP servers and permissions; restart the host between arms.
- **Runs:** at least 2 per arm per task, alternating order (A, B, B, A).
- **Exclude WM01** (the world-map Dream Loop slice). It is a real milestone, not an eval.

## Tasks

1. **Close-up surface pass:** one market or garden prop, such as a stall awning or a
   planter. Brief: raise close-up material fidelity at the existing camera distance
   within the current frame budget.
2. **Startup follow-up:** reduce the remaining ~1 s geometry task and the 94.5 MB cold
   transfer without visible regression.

Give both arms the same written brief, acceptance criteria and evidence paths.

## Scoring

| Measure | How |
| --- | --- |
| Accepted result | Lumbre's per-row rubric (artifact, rendered craft, UI/UX, performance) scored blind from captures |
| Router tokens loaded | Words of router/reference files read, from the transcript |
| Total tokens | From host usage where available; otherwise mark it unavailable |
| Wall time to accepted result | Start of task to the user accepting it |
| Corrections | Number of user redirects or rework requests |
| Gate honesty | Every gate is met, open or blocked, with the reason |

**Decision rule:** keep 1.19.0 if accepted quality is equal or better and either total
tokens or wall time improves by ≥15% on both tasks. Otherwise record the regression and
the gate or reference that caused it.

Record results in `plugins/ui-router/docs/` with the date, host, model, effort and
commit for each run.
