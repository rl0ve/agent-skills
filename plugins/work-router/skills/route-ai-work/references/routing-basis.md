# Routing basis

Use this reference when explaining or revising the routing policy. Treat benchmark figures as dated evidence, not timeless product facts.

## GPT-6.1 Sol review: October 1, 2026

[OpenAI's model page](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
positions GPT-6.1 Sol as near-Astra performance for complex coding, computer use and
professional work; its [model selection guide](https://developers.openai.com/api/docs/guides/model-selection)
still reserves Astra for the most demanding tasks. These are provider claims, not a
matched Codex completion-time or visual-quality trial. The current host catalog lists
`gpt-6.1-sol` with low through max effort. The three bundled Sol profiles are updated
to that model ID; already installed copies require a separate sync.

The [Arena WebDev board](https://arena.ai/leaderboard/code/webdev), checked October 1,
reports Astra Max at rank 2, 1789 +/-10 with 5,918 votes and Sol 6.1 Max at rank 3,
1759 +/-19 with 1,264 votes. Astra retains a measured Max-setting edge, but the gap
is much smaller than the September 27 Astra-versus-Sol-6 comparison below. The
displayed marginal intervals nearly meet; they are not a pairwise significance test.
Different vote counts, release ages and unknown Codex harness settings limit transfer.

[Artificial Analysis's comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-astra-xhigh),
checked October 1, reports Intelligence Index 51 versus 52 and AutomationBench-AA
67% for both at xhigh; Terminal-Bench 4.0 is 54% for Sol 6.1 versus 60% for Astra.
The page's estimated per-task costs ($0.39 versus $2.31) are specific to its
evaluation, not Codex subscription usage or accepted-work costs. These mixed results
support Sol 6.1 as the normal substantial-work default and preserving Astra for a
demonstrated or clearly anticipated capability limit. They do not establish equal
performance on every task, equal effort cost or shorter native Codex wall time.

**Decision:** route typical substantial implementation, architecture, diagnosis,
synthesis and new UI builds to Sol 6.1 at task-appropriate effort. Reserve upfront
Astra for the hardest quality-first judgment or exceptionally difficult unresolved
creative/spatial direction; keep it when a capable Astra parent is progressing.
Rendered comparison remains the acceptance test for UI. Revisit this decision when
task-specific data or representative accepted-work trials change.

## Independent evidence addendum: September 27, 2026

Use the [regular source policy](benchmark-sources.md) for future reviews. The September
22 review below did not evaluate Arena. Arena's [changelog](https://arena.ai/company/leaderboard-changelog)
dates Sol Max's WebDev addition to September 23, after that review.

The [WebDev board](https://arena.ai/leaderboard/code), dated September 25 and checked
September 27, reports GPT-6 Astra Max at rank 2, score 1792 +/-11, 4,908 votes; GPT-6
Sol Max at rank 5, score 1681 +/-15, 2,019 votes. This overall-category comparison
provides meaningful evidence favoring Astra for generated web applications. The
displayed intervals are separated. It does not establish a winner in every domain,
production correctness, native Codex completion time, or high/xhigh effort performance.

The [Agent board](https://arena.ai/leaderboard/agent), also dated September 25, reports
Astra Max net improvement 10.85% +/-2.29% versus Sol Max 7.68% +/-2.57%; intervals
overlap. Sol's steerability estimate is higher (15.70% +/-5.92% versus 0.89% +/-5.11%) and reported
median task cost lower ($0.81 versus $2.69). These are distinct signals, not evidence
that either model wins every workflow. [Agent methodology](https://arena.ai/blog/agent-arena-methodology)
uses treatment-effect estimates; net improvement is not absolute task-success rate.

Artificial Analysis's [Astra Max](https://artificialanalysis.ai/models/gpt-6-astra) and
[Sol Max](https://artificialanalysis.ai/models/gpt-6-sol) pages, checked September 27,
report Intelligence Index scores of 53 and 48 under
[v4.3.2](https://artificialanalysis.ai/methodology/intelligence-benchmarking). This is
an independent broad-capability cross-check, not a second visual-quality experiment.
Do not infer total task speed from endpoint token throughput or combine this index
numerically with Arena scores.

**Decision at September 27:** prefer Astra for a new substantial UI build where visual quality is a
primary acceptance criterion, subject to user constraints and current availability.
Retain Sol for substantial implementation with settled design and objective checks,
and preserve a progressing capable parent. Astra high/xhigh remain task-based starting
recommendations, not efforts validated by the Max-only Arena comparison. No automatic
Max setting, model switch, paid trial or delegation follows from these results.

Source coverage for this addendum also included the original SWE-bench and DeepSWE
pages, Terminal-Bench, METR methods/limitations and OSWorld. They inform task selection
and interpretation in the source policy; this is not a claim that all supplied fresh
Sol-6/Astra-6 comparisons. DeepSWE's extracted board showed Astra xhigh and older
Sol-5.6 rows; no new Sol-6 row was verified there. Terminal-Bench's current 4.0 page
did not expose populated result rows in the retrieved view. No values were inferred
from either gap. The retrieved Arena rows did not specify exact harness versions, time/token budgets
or service tiers; those fields remain unknown. No matched local Codex timing or
visual-output trial was run.

Revisit the UI preference when relevant category results, model revisions, uncertainty
or representative accepted work change. Lower API price alone cannot establish the
fastest accepted result; total elapsed time, quality and rework remain separate.

## Model and benchmark evidence: September 22, 2026

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
not Sol 6. BenchCAD concerns reconstruction of geometry, not visual taste. No
current four-model aesthetic comparison or matched wall-clock study was verified in
that review. The September 27 addendum adds relevant Arena evidence without claiming a
universal UI winner. Rendered task-specific review remains necessary. Release demos and social
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
2. Sol 6.1 fits substantial everyday and complex work, including typical new UI;
   Astra fits the hardest judgment, exceptionally difficult unresolved
   quality-first direction, or a demonstrated Sol capability limit. Preserve useful context.
3. Luna fits bounded objective work. Terra 5.6 is conditional on availability and user
   preference or workload evidence. A capable parent owns consequential synthesis.
4. Keep Luna high narrow and Luna max explicitly cost-first. Old economy results do
   not prove GPT-6 Luna is cheaper end to end for a new workload.
5. Escalate effort for missing depth, capability for insufficient judgment, and fix
   missing inputs before either. Sol xhigh and Astra xhigh are explicit depth choices
   that may be selected upfront when warranted; no failed high attempt is required.
   High remains the usual demanding-work start. Max and ultra need separate justification.
   These are policy recommendations, not a measured ranking of every effort setting.
6. Prefer one parent and one useful specialist. Preserve explicit model constraints,
   permit only one writer per working tree, and verify the actual child configuration.

## Profile compatibility

The bundled Sol and Luna profiles now target `gpt-6.1-sol` and `gpt-6-luna`; profile
names stay stable. Terra remains explicitly `gpt-5.6-terra`. Installing the plugin does not
refresh standalone profiles already copied into user or project configuration. Use
the included sync script when authorized, then start a new task to load them.

Historical source packs, images, and GPT-5.6 benchmark rows remain dated evidence;
the active SKILL.md takes precedence over their model rankings.
