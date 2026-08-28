---
name: route-ai-work
description: Automatically classify Codex work and route it to the appropriate direct path or subagent based on wall-clock latency, quality, cost, ambiguity, risk, context size, and write ownership. Use for delegation, parallel-agent requests, multi-step implementation, codebase exploration, architecture, debugging, review, security, high-stakes work, background/economy runs, or model and reasoning-effort selection. Do not delegate trivial one-step work.
---

# Route AI Work

Route work automatically while preserving explicit user choices, repository instructions, permissions, and safety boundaries.

## Route the task

1. Honor any explicit agent, model, effort, cost, or timeliness choice from the user.
2. Keep trivial, tightly coupled, or already well-contained work in the parent agent.
3. For substantial work, resolve the timeliness mode before selecting an agent:
   - **Fast**: minimize user-visible elapsed time. Prefer the parent or `sol-advisor` at medium effort.
   - **Balanced**: optimize quality per minute. Prefer Sol at high effort for consequential work.
   - **Economy**: minimize cost and accept background latency. Use `luna-economy-worker` only for bounded work with objective acceptance criteria.
   - **Quality-first**: use `sol-architect` or, only at the critical boundary below, `sol-critical`.
4. Delegate only when a bounded specialist or independent parallel workstream materially improves speed, quality, or context hygiene.
5. Prefer one reasoning-effort step up before changing model families or adding another agent.

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

## Choose the route

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

## Maintain the profiles

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
