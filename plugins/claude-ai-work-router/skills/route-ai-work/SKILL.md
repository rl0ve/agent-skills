---
name: route-ai-work
description: Route substantial Claude Code work to the leanest reliable parent or subagent configuration using task shape, context coupling, ambiguity, risk, latency, and token use. Use for model or effort selection, delegation, parallel work, large context, architecture, debugging, review, long autonomous jobs, or when the user asks to save tokens or time. Do not delegate trivial work.
compatibility: Claude Code; Fable route requires Claude Code 2.1.170+ and organizational access.
---

# Route AI Work

Choose the smallest route that can reliably finish the task. Optimize user-visible elapsed time first, reliable completion second, and token use third unless the user chooses a different order.

## Route the task

1. Honor explicit model, effort, timing, budget, delegation, and safety choices.
2. Check context before changing a knob. Missing requirements or missing files are not a model failure.
3. Keep trivial, tightly coupled, or already-contained work in the parent session.
4. Delegate only when a bounded specialist, context isolation, or independent read-only work repays startup and duplicated-context cost.
5. Use one write-capable owner per working tree. Never run the parent and a writing subagent against overlapping files at the same time.
6. Prefer a one-step effort increase before moving to a larger model when the model understood the problem but did not inspect, verify, or persist enough.
7. Prefer a larger model when the full relevant context was available, the model genuinely tried, and capability or judgment was still insufficient.

## Default routes

| Work shape | Route | Model | Effort | Notes |
|---|---|---|---|---|
| One-step, tightly coupled, or conversational | Parent | active model | active effort | Delegation overhead would dominate. |
| Narrow lookup, classification, repository map, or evidence collection | `claude-ai-work-router:fast-scout` | Haiku | low | Read-only; return compact evidence. |
| Defined implementation with clear acceptance criteria | `claude-ai-work-router:sonnet-builder` | Sonnet | medium | Sole writer; verify proportionately. |
| Difficult diagnosis, architecture, or consequential tradeoff | `claude-ai-work-router:opus-architect` | Opus | high | Read-only by default; parent integrates. |
| High-stakes final review after a strong implementation | `claude-ai-work-router:critical-reviewer` | Opus | xhigh | Read-only; use only when the risk justifies it. |
| Long-horizon, multi-stage, highly ambiguous autonomous project | `claude-ai-work-router:fable-runner` | Fable | high | Sole writer; only when Fable is permitted and the task is large enough. |

Use Sonnet at high effort in the parent for tightly coupled multi-file work that needs more thoroughness but not Opus-class judgment. Use Opus at low or medium effort only when expert recognition matters more than exhaustive repository work. Use Fable at low effort only for long agentic runs made of individually easy steps; it is still the heaviest family and must not become a routine shortcut.

## Token and latency controls

- Keep the routing skill and agent prompt concise; pass only the objective, exact inputs, owned files, acceptance criteria, and return format.
- Do not copy the full conversation into a subagent. Summarize only the facts it needs.
- Prefer one scout over several overlapping scouts.
- Parallelize independent read-only questions; serialize dependent work.
- Do not ask a writing agent to re-discover context the parent already has. Give it the precise file map.
- Stop escalation once the acceptance criteria are satisfied.
- Do not use `max` merely because a task is important. Use it only after a strong route failed or for a genuinely critical one-shot decision.

## Managed workspace behavior

Model aliases and effort levels are requests, not authority. Company `availableModels`, effort caps, provider mappings, and marketplace rules win.

- If Claude Code substitutes another model, report the requested route and the actual model shown by Claude Code.
- If Fable is unavailable, use the newest permitted Opus route for deep work, or the inherited model when the organization blocks the family.
- If the client does not support a requested effort level, use the nearest supported level at or below it and say so.
- Do not edit managed settings or attempt to bypass a company policy.

## Announce the route

For substantial work, emit one compact line before acting:

```text
Route: <parent or agent> | Model: <family> | Effort: <level> | Why: <task-fit reason> | Token controls: <one short control>
```

Do not narrate routing for trivial work.

## Delegate safely

Every delegation prompt must include:

- a bounded objective;
- exact inputs and owned files;
- whether the agent is read-only or the sole writer;
- acceptance criteria and validation;
- a compact result format;
- a reminder not to revert unrelated work.

The parent owns requirements, integration, unresolved decisions, and the final user response.

## Escalation ladder

1. Improve missing context.
2. Increase effort by one level when thoroughness was the failure.
3. Move Haiku to Sonnet when routine judgment or implementation exceeds the scout.
4. Move Sonnet to Opus when the issue is capability, ambiguity, or expert judgment.
5. Move Opus to Fable only for the longest, hardest connected work or after Opus genuinely failed.
6. Use `max` only at the critical boundary; test for diminishing returns.

Read [references/routing-policy.md](references/routing-policy.md) when explaining or changing the matrix. Read [references/managed-workspaces.md](references/managed-workspaces.md) when company policy, provider routing, or unavailable models matter.
