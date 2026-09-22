# Routing basis

Use this reference when explaining or revising the routing policy. Treat benchmark figures as dated evidence, not timeless product facts.

## Current model and benchmark evidence: September 22, 2026

OpenAI's [current model guide](https://developers.openai.com/api/docs/guides/latest-model)
distinguishes Astra for highest capability, Sol for strong reasoning on demanding tasks,
and Luna for efficient repeatable work. The
[Sol/Luna release](https://openai.com/index/introducing-gpt-6-sol-and-luna/) explicitly
retains Astra for the most demanding work. Sol is a practical substantial-work default,
not a replacement for Astra when maximum capability matters.

The [Terra model page](https://developers.openai.com/api/docs/models/gpt-5.6-terra)
still documents GPT-5.6 Terra. The [GPT-5.6 introduction](https://openai.com/index/gpt-5-6/)
describes capability tiers advancing at their own cadence. No listed GPT-6 Terra does
not establish retirement. Verify host availability and keep the actual version label.

Published evidence, with settings preserved:

| Evaluation | GPT-6 Astra | GPT-6 Sol | GPT-6 Luna | Interpretation boundary |
|---|---:|---:|---:|---|
| DeepSWE v1.1 | 74.1%, best reported effort | 68.8%, max | 66.6%, max | Complex engineering, not visual taste or Codex elapsed time |
| OSWorld 2.0 v2026.08.08, offline partial reward | 72.6%, best reported effort | 60.5%, xhigh | Not included here | Computer workflows, not a rendering or design-quality test |
| AutomationBench | 41.4%, best reported effort | 33.2%, xhigh | Not included here | Highest capability and cost efficiency are different decisions |

Sources: [Astra evaluation table](https://openai.com/index/gpt-6-astra/) and
[Sol/Luna release](https://openai.com/index/introducing-gpt-6-sol-and-luna/).
These are reported configurations across releases, not an equal-effort, equal-budget
or live Codex timing experiment. The [DeepSWE author leaderboard](https://deepswe.datacurve.ai/)
reports Astra xhigh at about 74% with a 3-point uncertainty interval in mini-swe-agent;
that harness is not native Codex. Do not treat point differences as certainty per task.

Sol's efficiency case is concrete: AutomationBench Sol xhigh scores 33.2% at $0.27/task
versus Astra low's 30.3% at 3.9 times the cost. That supports selecting Sol for suitable
work; it does not establish that Sol exceeds Astra at every effort or on every task.

The published internal design result compares Astra 50.0% with **GPT-5.6 Sol** 47.4%,
not Sol 6. BenchCAD concerns reconstruction of geometry, not visual taste. No verified
current four-model aesthetic comparison or matched wall-clock study supports a universal
UI winner. Rendered task-specific review remains necessary. Release demos and social
examples are references, not controlled benchmarks.

At review time, API input/output prices per million tokens are Astra $10/$50,
Sol $2/$10, Luna $0.10/$0.50, and Terra 5.6 $2/$12. Sol therefore has no sticker-price
disadvantage to Terra, but rates alone do not measure completed-task cost, Codex usage
limits, retries, or latency. No direct current Terra-versus-Sol-6/Luna-6 workload
benchmark was verified. Keep Terra situational rather than an automatic cheap scout.
Pricing sources: the releases above and the
[Terra page](https://developers.openai.com/api/docs/models/gpt-5.6-terra).

Fast routing concerns elapsed time. Codex Fast is a separate service-tier choice that
requires explicit user selection and current account/workspace support; Standard remains
the default. Verify effective model and effort on every handoff.


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
| GPT-5.6 Sol medium | 5.17 min | 0.606 | $2.991 |
| GPT-5.6 Sol high | 6.32 min | 0.641 | $4.144 |
| GPT-5.6 Sol max | 10.17 min | 0.666 | $7.084 |
| GPT-5.6 Luna high | 5.65 min | 0.514 | $0.192 |
| GPT-5.6 Luna max | 8.00 min | 0.587 | $0.313 |

These figures were recorded from the Artificial Analysis Coding Agent Index v1.3 in the source pack. The pack separately records DeepSWE mini-swe-agent results; those durations are not Codex wall-clock times and must not be mixed with native Codex measurements.

Evidence sources:

- [Artificial Analysis coding agents](https://artificialanalysis.ai/agents/coding-agents)
- [DeepSWE](https://deepswe.datacurve.ai/)

## Current policy implications

1. Optimize total user-visible elapsed time, including duplicated context, retries,
   review, and integration. Neither a smaller model nor a handoff inherently saves time.
2. Sol fits substantial everyday work; Astra fits the hardest judgment, unresolved
   quality-first direction, or a demonstrated Sol capability limit. Preserve useful context.
3. Luna fits bounded objective work. Terra 5.6 is conditional on availability and user
   preference or workload evidence. A capable parent owns consequential synthesis.
4. Keep Luna high narrow and Luna max explicitly cost-first. Old economy results do
   not prove GPT-6 Luna is cheaper end to end for a new workload.
5. Escalate effort for missing depth, capability for insufficient judgment, and fix
   missing inputs before either. Max and ultra are not artifact or audience defaults.
6. Prefer one parent and one useful specialist. Preserve explicit model constraints,
   permit only one writer per working tree, and verify the actual child configuration.

## Profile compatibility

The bundled Sol and Luna profiles now target `gpt-6-sol` and `gpt-6-luna`; profile
names stay stable. Terra remains explicitly `gpt-5.6-terra`. Installing the plugin does not
refresh standalone profiles already copied into user or project configuration. Use
the included sync script when authorized, then start a new task to load them.

Historical source packs, images, and GPT-5.6 benchmark rows remain dated evidence;
the active SKILL.md takes precedence over their model rankings.
