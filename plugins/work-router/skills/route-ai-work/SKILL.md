---
name: route-ai-work
description: Route substantial agent work to the leanest reliable parent or subagent configuration using task shape, context coupling, ambiguity, risk, latency, and token use. Use for model or effort selection, delegation, parallel work, large context, architecture, debugging, review, long autonomous jobs, or when the user asks to save tokens or time. Do not delegate trivial work.
compatibility: Claude Code and Codex. Each has its own route table below; the method is the same.
---

# Route AI Work

Choose the smallest route that can reliably finish the task. Optimize user-visible elapsed
time first, reliable completion second, and token use third unless the user chooses a
different order.

## Route the task

1. Honor explicit model, effort, timing, budget, delegation, and safety choices.
2. Check context before changing a knob. Missing requirements or missing files are not a model failure.
3. Keep trivial, tightly coupled, or already-contained work in the parent session.
4. Delegate only when a bounded specialist, context isolation, or independent read-only work repays startup and duplicated-context cost.
5. Use one write-capable owner per working tree. Never run the parent and a writing subagent against overlapping files at the same time.
6. Prefer a one-step effort increase before moving to a larger model when the model understood the problem but did not inspect, verify, or persist enough.
7. Prefer a larger model when the full relevant context was available, the model genuinely tried, and capability or judgment was still insufficient.

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

## Default routes

The rules above are the same whichever agent you are. The table is not: read the one that
matches the agent you are running as, and ignore the other.

### If you are Claude Code

| Work shape | Route | Model | Effort | Notes |
|---|---|---|---|---|
| One-step, tightly coupled, or conversational | Parent | active model | active effort | Delegation overhead would dominate. |
| Narrow lookup, classification, repository map, or evidence collection | `work-router:fast-scout` | Haiku | low | Read-only; return compact evidence. |
| Defined implementation with clear acceptance criteria | `work-router:sonnet-builder` | Sonnet | medium | Sole writer; verify proportionately. |
| Difficult diagnosis, architecture, or consequential tradeoff | `work-router:opus-architect` | Opus | high | Read-only by default; parent integrates. |
| High-stakes final review after a strong implementation | `work-router:critical-reviewer` | Opus | xhigh | Read-only; use only when the risk justifies it. |
| Long-horizon, multi-stage, highly ambiguous autonomous project | `work-router:fable-runner` | Fable | high | Sole writer; only when Fable is permitted and the task is large enough. |

Use Sonnet at high effort in the parent for tightly coupled multi-file work that needs more thoroughness but not Opus-class judgment. Use Opus at low or medium effort only when expert recognition matters more than exhaustive repository work. Use Fable at low effort only for long agentic runs made of individually easy steps; it is still the heaviest family and must not become a routine shortcut.

### If you are Codex

| Route | Use it for | Default configuration | Write policy |
|---|---|---|---|
| Parent agent | Trivial work, tightly coupled changes, integration, final verification | Current session | May write |
| `terra-explorer` | Read-heavy repository exploration, large-file review, documentation checks, supporting-document synthesis | GPT-5.6 Terra, medium | Read-only |
| `luna-builder` | Narrow, clear, repeatable implementation with an objective definition of done | GPT-5.6 Luna, high | Sole writer |
| `luna-economy-worker` | Cost-first background implementation with stable requirements and objective checks | GPT-5.6 Luna, max | Sole writer |
| `sol-advisor` | Fast expert judgment, sanity checks, UX opinions, quick review, first-pass diagnosis | GPT-5.6 Sol, medium | Read-only |
| `sol-architect` | Ambiguous architecture, difficult debugging, multi-subsystem reasoning, complex edge cases | GPT-5.6 Sol, high | Read-only by default |
| `sol-critical` | Security-sensitive work, irreversible production changes, release gates, or a prior strong attempt that failed | GPT-5.6 Sol, max | Read-only by default |
| Built-in `worker` or parent Sol | Defined implementation that is too broad, contextual, or consequential for Luna | Effective Sol setting, normally high | Sole writer |

If a named custom profile is unavailable, use the closest built-in fallback: `explorer` for read-heavy work, `worker` for implementation, or the parent agent for judgment. State the fallback; do not fail merely because a profile is missing.

## Token and latency controls

- Keep the routing skill and agent prompt concise; pass only the objective, exact inputs, owned files, acceptance criteria, and return format.
- Do not copy the full conversation into a subagent. Summarize only the facts it needs.
- Prefer one scout over several overlapping scouts.
- Parallelize independent read-only questions; serialize dependent work.
- Do not ask a writing agent to re-discover context the parent already has. Give it the precise file map.
- Stop escalation once the acceptance criteria are satisfied.
- Do not use `max` merely because a task is important. Use it only after a strong route failed or for a genuinely critical one-shot decision.

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

## Escalate deliberately

- Escalate `sol-advisor` to `sol-architect` when the task needs deep tracing, architecture decisions, or sustained edge-case analysis.
- Escalate `sol-architect` to `sol-critical` only for security, irreversible actions, release-gating risk, or a documented prior strong failure.
- Escalate Luna work to the parent or a Sol worker when requirements become ambiguous, context becomes large, or the change crosses subsystems.
- Escalate Terra synthesis to Sol when the remaining work is judgment-heavy rather than read-heavy.
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

- Read [references/routing-basis.md](references/routing-basis.md) for the distilled policy, migration logic, and current-product overlay.
- Read [references/source-shared-routing-guide.md](references/source-shared-routing-guide.md) when revising task, timeliness, harness, or mixed-workflow routes.
- Read [references/source-codex-agents.md](references/source-codex-agents.md) when revising agent behavior, delegation, or quality gates.
- Read [references/source-wall-clock-evidence.md](references/source-wall-clock-evidence.md) when comparing measured completion time, cost, steps, or tokens. Search this large reference by model name or benchmark before reading broad sections.
- Read [references/source-research-evidence.md](references/source-research-evidence.md) when reviewing model, effort, harness, context-management, or cross-harness research. Search this large reference for the exact claim or model first.
