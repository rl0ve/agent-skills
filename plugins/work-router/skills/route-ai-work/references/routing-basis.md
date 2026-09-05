# Routing basis

Use this reference when explaining or revising the routing policy. Treat benchmark figures as dated evidence, not timeless product facts.

## Verified host facts: September 5, 2026

The local Codex model catalog (`~/.codex/models_cache.json`) and host tool metadata
identify `gpt-6-astra` as the most capable model for complex, demanding work. The
catalog default is medium; supported effort levels are low, medium, high, xhigh,
max, and ultra. Ultra is described as maximum reasoning with automatic delegation.
The host also lists Sol as an everyday agentic workhorse, Terra as a balanced coding
model, and Luna as fast and affordable for simpler work.

These facts establish availability, supported settings, and product positioning on
this host. They do not establish account-wide availability, exact cost, or relative
end-to-end latency. No Astra comparative benchmark was run for this release.

The policy inference is to keep demanding, context-heavy work in an active Astra
parent, use Astra high when selecting a route for new demanding work, and retain
Sol, Terra, and Luna for bounded tasks where a handoff has a concrete benefit. Do not
interpret the historical timing figures below as measurements of Astra.

Fast routing concerns total completion time. Codex Fast is a separate service-tier
choice requiring explicit user selection and current account/workspace support;
Standard remains the default. Verify effective model and effort on every handoff.

## Historical product guidance (predates Astra)

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
2. Astra owns demanding judgment and broad integration when already active. Sol
   medium/high remains useful for bounded advice and defined implementation.
3. Terra collects independent evidence; the parent owns consequential synthesis.
4. Keep Luna high narrow and Luna max explicitly cost-first. Old economy results do
   not prove it is cheaper than Astra for a new workload.
5. Escalate effort for missing depth, capability for insufficient judgment, and fix
   missing inputs before either. Max and ultra are not artifact or audience defaults.
6. Prefer one parent and one useful specialist. Preserve explicit model constraints,
   permit only one writer per working tree, and verify the actual child configuration.

## Profile compatibility

The bundled Sol, Terra, and Luna TOML profiles retain their model IDs. Installing the
plugin does not install those standalone Codex profiles or convert them to Astra.
Use the included sync script when a profile installation is requested, then start a
new task to load them. Existing names remain compatible; no Astra profile is required
because the parent or a supported built-in agent can supply that model explicitly.

Sol reviewer profiles now return demanding escalation decisions to the parent instead
of unconditionally selecting another Sol profile. Historical source packs and images
remain dated evidence; the active SKILL.md takes precedence over their model rankings.
