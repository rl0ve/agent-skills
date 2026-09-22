# Routing basis

Use this reference when explaining or revising the routing policy. Treat benchmark figures as dated evidence, not timeless product facts.

## Current product guidance: September 22, 2026

OpenAI's current model guidance names GPT-6 Sol (`gpt-6-sol`) for demanding agentic
work and GPT-6 Luna (`gpt-6-luna`) for faster, lower-cost, well-defined work. The
release makes both valid Codex routes; exact availability, effort support, pricing,
service tier, and child-model overrides remain host- and workspace-dependent.

The policy inference is to use GPT-6 Sol for new demanding work and consequential
synthesis, and GPT-6 Luna for narrow tasks with objective checks. Preserve a
well-progressing Astra parent rather than paying an unnecessary family switch and
context reload. Retain Terra only as a conditional read-only route when the current
host still offers it. Release positioning is not a comparative UI-quality benchmark,
a latency measurement, or proof of lower total cost after retries and review.

Fast routing concerns total completion time. Codex Fast is a separate service-tier
choice requiring explicit user selection and current account/workspace support;
Standard remains the default. Verify effective model and effort on every handoff.

Primary current sources:

- [Latest model guidance](https://developers.openai.com/api/docs/guides/latest-model)
- [GPT-6 Sol model page](https://developers.openai.com/api/docs/models/gpt-6-sol)
- [GPT-6 Luna model page](https://developers.openai.com/api/docs/models/gpt-6-luna)

## Historical product guidance (predates GPT-6 Sol and Luna)

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

## Current policy implications

1. Optimize total user-visible elapsed time, including duplicated context, retries,
   review, and integration. Neither a smaller model nor a handoff inherently saves time.
2. GPT-6 Sol owns new demanding judgment and broad integration. Preserve an active
   Astra parent when its loaded context and progress make switching wasteful.
3. Terra collects independent evidence; the parent owns consequential synthesis.
4. Keep Luna high narrow and Luna max explicitly cost-first. Old economy results do
   not prove GPT-6 Luna is cheaper end to end for a new workload.
5. Escalate effort for missing depth, capability for insufficient judgment, and fix
   missing inputs before either. Max and ultra are not artifact or audience defaults.
6. Prefer one parent and one useful specialist. Preserve explicit model constraints,
   permit only one writer per working tree, and verify the actual child configuration.

## Profile compatibility

The bundled Sol and Luna profiles now target `gpt-6-sol` and `gpt-6-luna`; profile
names stay stable. Terra remains on its existing ID. Installing the plugin does not
refresh standalone profiles already copied into user or project configuration. Use
the included sync script when authorized, then start a new task to load them.

Historical source packs, images, and GPT-5.6 benchmark rows remain dated evidence;
the active SKILL.md takes precedence over their model rankings.
