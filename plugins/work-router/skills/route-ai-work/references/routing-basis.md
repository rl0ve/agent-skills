# Routing basis

Use this reference when explaining or revising the routing policy. Treat benchmark figures as dated evidence, not timeless product facts.

## Current product guidance

As checked on August 1, 2026, OpenAI's Codex subagent documentation recommends:

- GPT-5.6 Sol for demanding, ambiguous, multi-step work requiring planning, tools, validation, and follow-through.
- GPT-5.6 Terra for speed- and efficiency-oriented exploration, read-heavy scans, large-file review, and supporting-document processing.
- GPT-5.6 Luna for fast, narrow, clear, repeatable, or high-volume work.
- Medium effort as the balanced default, high for complex logic and edge cases, and max or xhigh only for especially demanding reasoning.
- Parallel agents primarily for independent read-heavy work; parallel write-heavy work creates conflict and coordination risk.
- Custom agents as standalone TOML files in `~/.codex/agents/` or `.codex/agents/`. Skills can request delegation, but they do not replace those runnable profiles.

Primary sources:

- [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [GPT-5.6 model guidance](https://developers.openai.com/api/docs/guides/latest-model)
- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Plugins](https://learn.chatgpt.com/docs/plugins)

## Evidence retained from Work Router 2.1

The source pack's August 1, 2026 benchmark synthesis supports a latency-first default while separating native-harness measurements from fixed-harness measurements:

| Configuration | Native Codex average wall time | Coding Agent Index | Average cost per task |
|---|---:|---:|---:|
| Sol medium | 5.17 min | 0.606 | $2.991 |
| Sol high | 6.32 min | 0.641 | $4.144 |
| Sol max | 10.17 min | 0.666 | $7.084 |
| Luna high | 5.65 min | 0.514 | $0.192 |
| Luna max | 8.00 min | 0.587 | $0.313 |

These figures were recorded from the Artificial Analysis Coding Agent Index v1.3 in the source pack. The pack separately records DeepSWE mini-swe-agent results; those durations are not Codex wall-clock times and must not be mixed with native Codex measurements.

Evidence sources:

- [Artificial Analysis coding agents](https://artificialanalysis.ai/agents/coding-agents)
- [DeepSWE](https://deepswe.datacurve.ai/)

## Policy implications

1. Optimize measured user-visible wall-clock time, not token count, step count, time to first token, or output speed.
2. Keep Sol medium as the fast judgment route and Sol high as the consequential reasoning route.
3. Keep Luna high narrow. Luna max is an economy/background route, not the fastest route.
4. Add Terra for read-heavy work because current product guidance distinguishes that workload from Luna's narrow, repeatable work.
5. Keep `sol-critical` rare; max effort is a risk boundary, not a generic quality upgrade.
6. Prefer a single parent and one bounded specialist. Add parallel agents only for genuinely independent workstreams.

## Migration from the earlier profiles

- Retain `sol-advisor`, `sol-architect`, and `sol-critical`; their medium, high, and max escalation boundaries remain useful.
- Retain but narrow `luna-builder` to clear, repeatable implementation. Broad or consequential implementation stays with the parent or a Sol-backed worker.
- Add `terra-explorer` for read-heavy exploration and supporting-document work.
- Add `luna-economy-worker` for bounded, cost-first background work. Keep the Luna prefix visible because the route deliberately uses GPT-5.6 Luna at max effort.
- Remove duplicate self-announcements and elapsed-time claims from child profiles. The parent announces the route, and elapsed time is reported only when actually measured.
- Do not create a separate `sol-builder` merely as another effort label. Use the built-in `worker` or parent Sol for defined work that exceeds Luna's scope.
- Infer obvious timing intent and default ordinary interactive requests to Fast. Ask one short timing question only when the choice is genuinely ambiguous and materially consequential.
