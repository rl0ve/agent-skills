# Benchmark sources for routing decisions

Reviewed October 2, 2026. Work Router owns this source policy for both Codex and
Claude Code. Benchmark rankings are evidence about tested configurations, not standing
instructions to switch models. Keep dated measurements in `routing-basis.md` or a
linked review, so the entrypoint does not accumulate volatile leaderboard tables.

## When to refresh

Use Arena and Artificial Analysis as regular inputs when reviewing a model release,
changing a model/effort default, answering a disputed comparative claim, or reassessing
a route after repeated failures. Add the task-specific original benchmark below.
Refresh before making a current recommendation if the saved snapshot predates a
relevant release, benchmark revision, new comparison, or integrity correction.

This is a review workflow, not a scheduled monitor. Do not browse every source on
ordinary implementation tasks, add a background job, or run paid model comparisons
merely because the skill was invoked. Reuse a still-relevant dated assessment.

## Select evidence by the decision

| Source | Use it for | Interpretation boundary |
|---|---|---|
| [Arena WebDev](https://arena.ai/leaderboard/code) and its relevant domain categories | Human preference for generated web applications; UI implementation and design direction | Preserve category, effort, votes, confidence/rank intervals and harness. Inspect reference-based design or frontend categories when relevant; do not transfer an overall rank into an unmeasured category. Preference does not prove accessibility, maintainability or production correctness. |
| [Arena Agent](https://arena.ai/leaderboard/agent) and [methodology](https://arena.ai/blog/agent-arena-methodology) | Agent completion, response to corrections, tool recovery and task cost | Agent Arena uses causal treatment-effect estimates from randomized components, not WebDev's pairwise preference scores. Net improvement is not an absolute task-success rate. Inspect individual signals and uncertainty, not only overall rank. |
| [Artificial Analysis](https://artificialanalysis.ai/) with [intelligence](https://artificialanalysis.ai/methodology/intelligence-benchmarking) and [performance methods](https://artificialanalysis.ai/methodology/performance-benchmarking) | Independent capability evaluations, supported effort variants, API response time, throughput and cost tradeoffs | Preserve index version, subtest, endpoint, effort and reasoning-token accounting. Use task-relevant subtests; an aggregate intelligence score is not a visual-quality test. API latency or tokens/second is not accepted Codex task time. |
| [SWE-bench](https://www.swebench.com/) and [DeepSWE](https://deepswe.datacurve.ai/) | Repository issue resolution and substantial engineering | Preserve dataset/version, same-harness comparisons, budget, pass metric and verification status. SWE-bench's checked entries and Bash Only view help distinguish submissions and model effects. DeepSWE uses mini-swe-agent. Neither is a UI taste benchmark; check saturation, contamination concerns and author corrections. |
| [Terminal-Bench](https://www.tbench.ai/) and its [updates](https://www.tbench.ai/news) | Terminal workflows, tool use, debugging and environment work | Compare model plus agent/harness, benchmark version, resources and time limits. Check integrity notices and revised tasks; do not pool different versions or infer raw-model superiority from different agents. |
| [METR time horizons](https://metr.org/time-horizons/) and [limitations](https://metr.org/notes/2026-01-22-time-horizon-limitations/) | Reliability on longer software/research tasks and autonomy-related decisions | Human task-duration at a stated success probability is not AI runtime or safe unattended duration. Keep confidence intervals, task distribution and 50%/80% reliability separate. Missing models are missing coverage, not inferior models. |
| [OSWorld](https://osworld-v2.xlang.ai/) | Visual computer-use workflows | Preserve version, online/offline mode, reward definition, action/step budget and tools. Operating an interface is different from designing a good one. |
| Original model/provider documentation and current host catalog | Availability, model IDs, supported efforts, context, prices and vendor-reported evaluations | Verify product facts at their owner. Label vendor measurements and check the benchmark author's result where available; provider positioning alone cannot settle a comparative default. |

These are selected sources with inspectable methods, not an exhaustive or permanent
ranking of evaluators. Add another original evaluator when it addresses a missing
task dimension and exposes methods, configuration and limitations. Social posts and
aggregators are leads; follow them to the original evidence before adopting a claim.

## Record and compare

For a decision-driving result, retain:

- Exact source URL, review date, leaderboard/result date, benchmark version and category.
- Model ID and revision if published, effort, harness/version, tools, budgets and service
  tier or endpoint when disclosed. Mark unknown fields rather than guessing equivalence.
- Metric and direction, score, sample size, uncertainty, and preliminary/verified status.
- Measured latency and complete-task cost only where available, with their definitions;
  distinguish medians from means, API costs from subscription usage, and estimates from
  observed measurements. Include retries, human review and integration in local trials.
- Decision, applicable task, remaining uncertainty and what would reverse the decision.

Prefer the original live board or its dated dataset to cached search snippets or a
homepage summary. Check [Arena's changelog](https://arena.ai/company/leaderboard-changelog)
for model additions and [dataset documentation](https://arena.ai/blog/arena-leaderboard-dataset)
for snapshots. A result published after an earlier review belongs in a dated addendum;
do not imply it was available or evaluated earlier.

Triangulate a consequential default with relevant independent evidence where available.
Do not average ranks, Elo/preference scores, success percentages and composite indexes,
or count a vendor's repost of one result as a second independent evaluation. An index
and one of its constituent benchmarks also share evidence. If coverage is missing,
state the gap and make a provisional task-specific recommendation rather than inventing
consensus. Cross-task agreement supports a broad capability hypothesis; it does not
prove a particular design outcome or native-harness speed advantage.

Read confidence intervals and sample sizes. Overlapping marginal intervals warrant
caution but are not a formal pairwise significance test. Separated intervals strengthen
the evidence within that setup without proving universal superiority. Do not turn
Max-versus-Max results into measured claims about high, xhigh or ultra. Choose effort
from task needs and supported settings; label an untested effort recommendation as such.

When sources disagree, inspect task mix, versions, effort, harness and scoring before
changing a route. For a consequential unresolved decision, propose a bounded local
comparison using the same brief, tools, acceptance criteria and service tier, recording
accepted quality, elapsed time, retries and review effort. Do not run a tournament for
routine work or spend on external evaluations without authorization.

## Applying the evidence to UI work

The [October 2 Opus 5.5 assessment](opus-5-5-review.md) adds a quality-focused
Claude route when host choice is open. It changes the Claude implementation start
to Opus 5.5 medium and qualifies the former automatic Fable preference. Its WebDev
Max result cannot establish medium/high quality, the fastest accepted result or a
universal visual winner. Keep active host constraints and useful parent context.

The October 1 Sol 6.1 review supersedes the September 27 family preference for ordinary
new UI work within Codex: start with Sol 6.1 for a typical substantial build, including one with a
visual-quality bar. Astra still has a narrower measured Max-effort WebDev advantage;
prefer it when unresolved creative/spatial judgment is exceptionally difficult and
maximum quality matters. Keep small changes in a capable parent and honor explicit
cost, latency and model constraints.

This inference does not prescribe Max, establish Astra as best in every design category,
or replace UI Router's design lead, rendered comparison, responsive/accessibility checks
and exercised interactions. Refresh the dated assessment when relevant evidence changes.
