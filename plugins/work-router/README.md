# Work Router

Task-first routing for Codex and Claude Code. Optimize total completion time first,
reliable completion second, and cost/token use third unless the user chooses otherwise.

The plugin contributes:

- `/work-router:route-ai-work`, an auto-invocable policy with a table for each host;
- `/work-router:check-routing-setup`, a manual, read-only environment check;
- six Claude subagents spanning Haiku, Sonnet, Opus, and Fable;
- six separately installable Codex profiles spanning Sol, Terra, and Luna;
- a Claude `PreToolUse` hook that blocks Bash commands containing `sudo`.

## Codex with Astra

Keep demanding work in an active Astra parent: ambiguous decisions, difficult debugging,
complex synthesis, broad implementation, integration, and final verification. For new
work that warrants Astra, recommend high effort; medium remains its ordinary-work
default. Use xhigh only when unresolved reasoning warrants more depth. Do not default
to max or ultra because a task is important or long.

Use Sol for bounded advice and defined implementation, Terra for independent reading,
and Luna for narrow repeatable tasks. A handoff must repay context, startup, and review
cost. These are policy choices based on task fit and the current host catalog; no Astra
comparative speed or cost benchmark is claimed.

“Astra throughout” also applies to children. Use the Astra parent or a supported
built-in agent explicitly configured for Astra. Named Sol/Terra/Luna profiles keep their
own models; a built-in worker's name does not establish its model. Verify the effective
configuration. The router recommends parent setting changes; it cannot silently switch
a running session.

Fast routing and Codex Fast service are separate. Service defaults to Standard; offer
Fast once only when it could materially help, and require explicit user choice plus
account/workspace availability before changing it.

See the [policy](skills/route-ai-work/SKILL.md),
[evidence basis](skills/route-ai-work/references/routing-basis.md), and
[routing cases](skills/route-ai-work/references/routing-scenarios.md).

## Codex profile setup

The shared skill works without installing custom profiles. If requested, preview the
standalone Codex profiles with:

```bash
python3 plugins/work-router/skills/route-ai-work/scripts/sync_agent_profiles.py
```

From the repository root, rerun with `--apply` to install them after reviewing the plan
and satisfying any destination write permissions. Changed profiles are backed up;
unrelated profiles are preserved. Start a new Codex task to load the changes. A
successful copy does not prove that the host supports a model or has loaded the profile.
No Astra custom profile is bundled; the parent or a supported built-in agent can use it.

## Claude Code

Stay in the parent for trivial or tightly coupled work. Use a bounded subagent only
when specialization, context isolation, or independent reading repays the handoff.
Fable handles long-horizon work and prose whose quality is the deliverable. The Claude
route table and six Claude agent definitions are unchanged by the Astra update.

The router does not modify user or managed settings. Organization model allowlists,
effort caps, and explicit user choices always win.
