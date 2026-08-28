# Claude AI Work Router

Claude Code-native routing for lower latency and lower token use without sacrificing the quality floor a task actually needs.

The plugin contributes:

- `/claude-ai-work-router:route-ai-work`, an auto-invocable routing policy;
- `/claude-ai-work-router:check-routing-setup`, a manual environment check;
- five bounded subagents spanning Haiku, Sonnet, Opus, and Fable;
- a `PreToolUse` safety hook that blocks `sudo`.

The router does not modify user or managed settings. It can route bounded work through model-specific subagents and recommend `/model` or `/effort` changes when the parent session itself is the right owner. Organization allowlists and effort caps always win.

## Lean default

Stay in the parent session for trivial or tightly coupled work. Use one bounded subagent only when specialization, context isolation, or parallel read-only work repays the startup and duplicated-context cost.

Fable is an escalation for long-horizon work, never the default. `max` effort is an escalation, never the default.
