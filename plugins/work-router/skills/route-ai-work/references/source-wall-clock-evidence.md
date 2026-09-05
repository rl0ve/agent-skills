# Coding-agent wall-clock, cost, steps and token evidence — as of August 1, 2026

> Historical source pack from August 2026; predates Astra. For current routes and
> escalation, follow [SKILL.md](../SKILL.md) and [routing-basis.md](routing-basis.md).
> The model rankings below are retained as dated evidence, not current defaults.

All values below were read from pages fetched in this session. Two independent measurement systems cover the requested configurations:

1. **Artificial Analysis Coding Agent Index v1.3** — runs the *native harnesses* (Codex, Claude Code, Cursor CLI, etc.) over DeepSWE + Terminal-Bench v2 + SWE-Atlas-QnA (321 tasks), and reports **average agent wall time per task**, average API cost per task, steps and tokens ([Artificial Analysis coding agents](https://artificialanalysis.ai/agents/coding-agents)). AA defines this metric explicitly: "This chart uses agent wall time: how long the agent process was actively running on each task. It does not include environment startup, verifier or judge time, or other harness overhead" and "Execution time on this page refers to average wall-clock task runtime per task, not just raw model latency" ([Artificial Analysis coding agents](https://artificialanalysis.ai/agents/coding-agents)).
2. **DeepSWE (Datacurve), 113 tasks, updated July 25, 2026** — all models run on the **mini-swe-agent** harness (not Codex / not Claude Code), 4 whole-benchmark runs per configuration, with per-trial **mean and median wall-clock duration**, cost, agent steps and output tokens in the leaderboard data ([DeepSWE leaderboard](https://deepswe.datacurve.ai/)). Datacurve states it tracks "median wall-clock duration" and "median dollar cost per trial" per trial ([DeepSWE methodology blog](https://deepswe.datacurve.ai/blog/deepswe)).

Because DeepSWE fixes the harness at mini-swe-agent, its minutes are **not** Codex or Claude Code elapsed times; the AA rows are the ones measured inside Codex / Claude Code. Both are reported separately below and never mixed.

---

## A. Native-harness measurements (Codex / Claude Code) — Artificial Analysis Coding Agent Index v1.3

Source for every value in this table: [Artificial Analysis coding agents](https://artificialanalysis.ai/agents/coding-agents) (values read from the page's embedded leaderboard dataset).

| Configuration (harness) | AA Coding Agent Index v1.3 | Component pass@1 (DeepSWE / Terminal-Bench v2 / SWE-Atlas-QnA) | Avg cost per task (USD) | Median cost per task | **Avg agent wall time per task (measured)** | Avg steps | Avg total tokens per task (in / out / cache) |
|---|---|---|---|---|---|---|---|
| **Codex — GPT-5.6 Luna (max)** | 0.587 | 0.634 / 0.798 / 0.328 | $0.313 | $0.255 | **479.7 s = 8.00 min** | 115.0 | 15.46 M (7.91 M in / 64.9 k out / 7.49 M cache; 91.4 % cache hit) |
| **Codex — GPT-5.6 Luna (high)** | 0.514 | 0.534 / 0.718 / 0.290 | $0.192 | $0.150 | **339.1 s = 5.65 min** | 84.2 | 9.50 M (4.89 M in / 32.3 k out / 4.58 M cache) |
| **Codex — GPT-5.6 Sol (medium)** | 0.606 | 0.640 / 0.778 / 0.401 | $2.991 | $2.269 | **310.2 s = 5.17 min** | 72.4 | 5.82 M (3.00 M in / 19.1 k out / 2.80 M cache) |
| **Codex — GPT-5.6 Sol (high)** | 0.641 | 0.649 / 0.825 / 0.449 | $4.144 | $3.195 | **379.3 s = 6.32 min** | 85.9 | 8.08 M (4.16 M in / 28.2 k out / 3.89 M cache) |
| **Codex — GPT-5.6 Sol (max)** | 0.666 | 0.687 / 0.877 / 0.433 | $7.084 | $6.393 | **610.1 s = 10.17 min** | 114.2 | 13.23 M (6.81 M in / 54.9 k out / 6.36 M cache) |
| **Claude Code — Opus 5 (max)** | 0.655 | 0.631 / 0.845 / 0.489 | $8.950 | $8.008 | **1424.0 s = 23.73 min** | 166.1 | 23.89 M (11.91 M in / 80.5 k out / 11.73 M cache) |
| **Claude Code — Opus 5 (xhigh)** | 0.667 (highest index on the board) | 0.605 / 0.849 / 0.548 | $8.235 | $6.967 | **1418.8 s = 23.65 min** | 153.0 | 21.82 M (10.88 M in / 72.8 k out / 10.71 M cache) |
| **Claude Code — Opus 5 (high)** | 0.634 | 0.608 / 0.802 / 0.492 | $3.797 | $3.066 | **802.3 s = 13.37 min** | 92.6 | 9.70 M (4.83 M in / 35.4 k out / 4.75 M cache) |
| **Claude Code — Opus 5 (medium)** | 0.619 | 0.628 / 0.786 / 0.444 | $3.144 | $2.530 | **731.5 s = 12.19 min** | 82.9 | 7.94 M (3.95 M in / 29.6 k out / 3.88 M cache) |
| **Claude Code — Opus 5 (low)** | 0.568 | 0.569 / 0.742 / 0.392 | $2.178 | $1.694 | **569.3 s = 9.49 min** | 63.8 | 5.16 M (2.57 M in / 22.3 k out / 2.51 M cache) |
| **Claude Code — Fable 5 (max) (with Opus 4.8 fallback)** | 0.659 | 0.661 / 0.825 / 0.489 | $11.711 | $10.287 | **1403.4 s = 23.39 min** | 137.8 | 13.98 M (6.96 M in / 73.6 k out / 6.80 M cache) |
| **Claude Code — Fable 5 (medium)** | n.a. — not on the AA coding-agent board | n.a. | n.a. | n.a. | **n.a.** | n.a. | n.a. |
| **Claude Code — Fable 5 (high)** | n.a. — not on the AA coding-agent board | n.a. | n.a. | n.a. | **n.a.** | n.a. | n.a. |
| **Claude Code — Sonnet 5 (any effort)** | n.a. — no Claude Code Sonnet 5 variant is measured; the AA coding-agent board's Sonnet entry is Claude Code — Sonnet 4.6 (medium), index 0.376, $2.006/task, 807.4 s wall time, 67.2 steps | n.a. | n.a. | n.a. | **n.a.** | n.a. | n.a. |

Useful non-requested reference rows measured on the same page and same definition ([Artificial Analysis coding agents](https://artificialanalysis.ai/agents/coding-agents)): Codex — GPT-5.6 Luna (medium) 0.424 index, $0.095, **202.3 s**, 57.7 steps; Codex — GPT-5.6 Luna (low) 0.251 index, $0.042, **115.4 s**, 35.3 steps; Codex — GPT-5.6 Terra (max) 0.623 index, $2.206, **502.4 s**, 96.9 steps; Claude Code — Opus 4.8 (max) 0.605 index, $7.698, **1387.7 s**, 165.8 steps; Grok Build — Grok 4.5 (high) 0.644 index, $2.594, **991.6 s**, 60.9 steps; Kimi Code CLI — Kimi K3 0.613 index, $3.175, **1427.7 s**, 124.6 steps.

## B. Fixed-harness measurements (mini-swe-agent) — DeepSWE v1.1, 113 tasks, updated July 25, 2026

Source for every value in this table: [DeepSWE leaderboard](https://deepswe.datacurve.ai/) (values read from the leaderboard dataset embedded in the page; each configuration = 4 full benchmark runs, 95 % run-to-run CI). **Harness is mini-swe-agent, not Codex/Claude Code.**

| Configuration (mini-swe-agent) | pass@1 ± 95 % CI | pass@4 | Mean cost / task | Median cost / task | **Mean wall-clock min / task** | **Median wall-clock min / task** | Mean / median agent steps | Mean / median output tokens | Mean input tokens |
|---|---|---|---|---|---|---|---|---|---|
| gpt-5.6-luna [max] | 67.2 % ± 4.0 | 90.3 % | $0.61 | $0.46 | **18.7** | **16.4** | 101.7 / 92.5 | 73.4 k / 70.3 k | 15.44 M |
| gpt-5.6-luna [high] | 44.2 % ± 2.9 | 75.2 % | $0.16 | $0.13 | **7.9** | **6.6** | 49.0 / 44 | 25.8 k / 24.8 k | 3.37 M |
| gpt-5.6-luna [xhigh] | 56.9 % ± 2.2 | n.a. | $0.31 | $0.25 | **12.2** | **10.1** | 71.1 / 63 | 44.7 k | n.a. |
| gpt-5.6-sol [medium] | 61.1 % ± 1.6 | 80.5 % | $1.86 | $1.55 | **7.1** | **5.9** | 30.9 / 26 | 18.4 k / 17.6 k | 1.51 M |
| gpt-5.6-sol [high] | 69.4 % ± 1.4 | 86.7 % | $3.47 | $2.98 | **9.9** | **8.6** | 36.9 / 32 | 28.5 k / 27.7 k | 2.71 M |
| gpt-5.6-sol [xhigh] | 70.7 % ± 0.8 | n.a. | $4.70 | $4.12 | **13.3** | **11.6** | 44.0 / 39 | 40.7 k | n.a. |
| gpt-5.6-sol [max] | 72.7 % ± 2.8 | 85.8 % | $8.39 | $6.84 | **18.8** | **16.9** | 61.3 / 53 | 60.0 k / 58.8 k | 7.91 M |
| claude-opus-5 [max] | **73.6 % ± 3.9 (board leader)** | 88.5 % | $11.84 | $10.43 | **31.9** | **30.0** | 99.0 / 90.5 | 117.6 k / 113.4 k | 15.03 M |
| claude-opus-5 [xhigh] | 73.2 % ± 3.1 | n.a. | $9.07 | $7.93 | **26.0** | **24.1** | 88.7 / 80 | 91.7 k | n.a. |
| claude-opus-5 [high] | 72.8 % ± 1.9 | 87.6 % | $6.08 | $4.97 | **19.4** | **16.8** | 72.9 / 64 | 64.2 k / 59.9 k | 7.23 M |
| claude-opus-5 [medium] | 68.9 % ± 1.2 | 89.4 % | $3.29 | $2.48 | **12.7** | **9.8** | 52.3 / 43 | 37.0 k / 33.4 k | 3.58 M |
| claude-opus-5 [low] | 58.1 % ± 2.3 | n.a. | $1.66 | $1.22 | **7.8** | **5.6** | 35.6 / 29 | 19.9 k | n.a. |
| claude-fable-5 [medium] | 65.4 % ± 4.4 | 83.2 % | $6.09 | $4.62 | **13.5** | **10.7** | 48.4 / 41 | 40.2 k / 36.0 k | 2.94 M |
| claude-fable-5 [high] | 68.6 % ± 1.1 | 86.7 % | $9.18 | $7.32 | **17.7** | **15.0** | 58.7 / 49 | 57.3 k / 52.6 k | 4.83 M |
| claude-fable-5 [xhigh] | 69.9 % ± 3.2 | n.a. | $13.41 | $11.34 | **23.5** | **20.5** | 68.4 / 61.5 | 80.4 k | n.a. |
| claude-fable-5 [max] | 69.7 % ± 4.0 | n.a. | $21.63 | $19.23 | **34.9** | **31.6** | 88.4 / 79 | 118.6 k | n.a. |
| claude-sonnet-5 [medium] | 39.8 % ± 3.1 | 64.6 % | $4.08 | $3.36 | **18.7** | **16.3** | 107.6 / 100.5 | 56.8 k / 50.4 k | 9.29 M |
| claude-sonnet-5 [high] | 48.2 % ± 4.5 | 79.6 % | $7.43 | $5.83 | **28.8** | **25.7** | 146.6 / 138 | 87.3 k / 78.0 k | 18.25 M |
| claude-sonnet-5 [max] | 53.8 % ± 4.2 | 78.8 % | $26.40 | $23.28 | **80.1** | **72.4** | 268.5 / 260 | 214.1 k / 203.9 k | 72.42 M |
| claude-sonnet-5 [xhigh] | 49.7 % ± 3.5 | n.a. | $11.89 | $9.97 | **40.2** | **37.2** | 185.5 / 174 | 120.7 k | n.a. |
| claude-sonnet-5 [low] | 30.5 % ± 1.1 | n.a. | $2.19 | $1.68 | **12.2** | **10.4** | 76.9 / 70 | 35.6 k | n.a. |

Contextual anchors from the same DeepSWE dataset ([DeepSWE leaderboard](https://deepswe.datacurve.ai/)): gpt-5.5 [xhigh] 67.0 % at 30.1 mean / 26.5 median min and $7.23; claude-opus-4.8 [max] 59.0 % at 58.2 mean / 48.1 median min and $13.22; kimi-k3 [max] 68.5 % at 75.7 mean / 66.2 median min and $4.65; gemini-3.1-pro-preview [high] 11.8 % at 36.6 mean min. Datacurve's own write-up frames the same metric narratively: "gpt-5.5 reaches the highest score (70%) at a median of 20 minutes per trial," while "gemini-3.5-flash runs faster at 15 minutes but lands at a lower 28% score" ([DeepSWE methodology blog](https://deepswe.datacurve.ai/blog/deepswe)).

## C. Model-level latency (NOT task elapsed time) — Artificial Analysis model pages

These are single-request streaming metrics and must not be confused with the agent wall-clock minutes above. Values are medians on AA's "long" (≈10k-token) and "medium" prompt classes.

| Model (page headline variant) | Median output speed (tok/s), long / medium | Median time to first answer token (s), long / medium | Median end-to-end response time (s), long / medium | Source |
|---|---|---|---|---|
| GPT-5.6 Luna (max) | 172.1 / 174.2 | 121.9 / 80.1 | 124.8 / 83.0 | [AA GPT-5.6 Luna](https://artificialanalysis.ai/models/gpt-5-6-luna) |
| GPT-5.6 Sol (max) | 63.5 / 68.1 | 133.0 / 77.7 | 140.9 / 85.1 | [AA GPT-5.6 Sol](https://artificialanalysis.ai/models/gpt-5-6-sol) |
| Claude Opus 5 (max) | 53.6 / 56.2 | 92.0 / 25.5 | 101.3 / 34.4 | [AA Claude Opus 5](https://artificialanalysis.ai/models/claude-opus-5) |
| Claude Fable 5 (with fallback) | 66.2 / 59.9 | 89.0 / 61.9 | 96.6 / 70.2 | [AA Claude Fable 5](https://artificialanalysis.ai/models/claude-fable-5) |
| Claude Sonnet 5 (max) | 74.2 / 83.6 | 188.1 / 105.3 | 194.8 / 111.3 | [AA Claude Sonnet 5](https://artificialanalysis.ai/models/claude-sonnet-5) |

Note that the ordering of these latency numbers does **not** track the agent wall-clock ordering: Luna is by far the fastest streamer (172 tok/s) yet Codex — Luna (max) still takes 8.0 min per task, and Opus 5's fast time-to-first-token (25.5 s on medium prompts) coexists with the longest Claude Code wall times (23.7 min) ([Artificial Analysis coding agents](https://artificialanalysis.ai/agents/coding-agents)).

## D. Coverage / gaps

- **Claude Fable 5 medium and high**: wall-clock evidence exists only under mini-swe-agent on DeepSWE (13.5 / 17.7 mean min) ([DeepSWE leaderboard](https://deepswe.datacurve.ai/)); **no Claude Code-harness measurement exists** — n.a. on Artificial Analysis ([Artificial Analysis coding agents](https://artificialanalysis.ai/agents/coding-agents)).
- **Claude Sonnet 5**: publicly measured on DeepSWE at all five efforts with wall-clock durations ([DeepSWE leaderboard](https://deepswe.datacurve.ai/)); **no Claude Code coding-agent row** on the AA board — n.a.
- **GPT-5.6 Luna in Codex at "max"** is measured on both systems; the Codex wall time (8.0 min over 321 tasks incl. shorter Q&A tasks) is much lower than the DeepSWE-only mini-swe-agent time (18.7 mean / 16.4 median min) because the task mixes differ. Do not compare across the two tables.
- No per-task **median** wall time is published on the AA coding-agent page (only means; medians are published for cost and total tokens) ([Artificial Analysis coding agents](https://artificialanalysis.ai/agents/coding-agents)). DeepSWE publishes both mean and median durations ([DeepSWE leaderboard](https://deepswe.datacurve.ai/)).
- Anthropic's own launch material makes only relative timing claims, not measured minutes: partners report Fable 5 "finishing runs 25–30% faster" than Opus 4.8 on a spreadsheet suite ([Anthropic — Claude Fable 5](https://www.anthropic.com/claude/fable)). Treat as vendor-reported, not a wall-clock benchmark.

## E. Routing implications

All routing statements below rest on the measured values already cited above.

- **Fast mode (minimize user-visible elapsed time, accept some quality loss).** In Codex, **GPT-5.6 Sol (medium)** is the strongest fast option: 5.17 min average agent wall time with a 0.606 index — only 0.06 index below Sol (max) at half the elapsed time and 42 % of the cost ([Artificial Analysis coding agents](https://artificialanalysis.ai/agents/coding-agents)). Sol (high) at 6.32 min / 0.641 index is the better fast pick when quality matters more than 1 extra minute. Avoid Claude Code for this mode: the fastest measured Opus 5 setting (low) still needs 9.49 min at a lower 0.568 index ([Artificial Analysis coding agents](https://artificialanalysis.ai/agents/coding-agents)).
- **Balanced.** **Codex — GPT-5.6 Sol (high)** sits at 0.641 index / 6.32 min / $4.14, capturing ~96 % of the top index at ~27 % of Opus 5 (xhigh)'s elapsed time ([Artificial Analysis coding agents](https://artificialanalysis.ai/agents/coding-agents)). On the harness-controlled DeepSWE view the same conclusion holds: sol [high] scores 69.4 % at 9.9 mean min vs opus-5 [high] 72.8 % at 19.4 mean min ([DeepSWE leaderboard](https://deepswe.datacurve.ai/)). If the workload is Claude-native, **Opus 5 (medium)** (0.619 index, 12.19 min, $3.14) is the balanced Claude Code setting ([Artificial Analysis coding agents](https://artificialanalysis.ai/agents/coding-agents)).
- **Economy / background (cost-dominant, latency tolerated).** **Codex — GPT-5.6 Luna (max)** is the outlier: $0.313 per task for a 0.587 index — roughly 1/29 the cost of Claude Code Opus 5 (max) at $8.95 and 1/23 of Fable 5 (max) at $11.71 — but it burns 115 steps and 15.5 M tokens and takes 8.0 min ([Artificial Analysis coding agents](https://artificialanalysis.ai/agents/coding-agents)). On DeepSWE the same configuration reaches 67.2 % pass@1 for $0.61 mean per task, versus $11.84 for the 73.6 % leader ([DeepSWE leaderboard](https://deepswe.datacurve.ai/)). Luna (high) at $0.192 / 5.65 min / 0.514 index is the cheapest still-usable tier ([Artificial Analysis coding agents](https://artificialanalysis.ai/agents/coding-agents)). Because Luna's wall time is step-driven rather than token-speed-driven (172 tok/s median output speed, [AA GPT-5.6 Luna](https://artificialanalysis.ai/models/gpt-5-6-luna)), it is best routed to asynchronous/background queues where its high step count is invisible.
- **Quality-first.** Two defensible endpoints, measured in their native harnesses: **Claude Code — Opus 5 (xhigh)** tops the composite at 0.667 index (best SWE-Atlas-QnA component, 0.548) for $8.24 and 23.65 min, and **Codex — GPT-5.6 Sol (max)** is statistically adjacent at 0.666 index (best Terminal-Bench v2 component, 0.877) for $7.08 in **10.17 min — 2.3× faster elapsed** ([Artificial Analysis coding agents](https://artificialanalysis.ai/agents/coding-agents)). On DeepSWE alone, opus-5 [max] leads at 73.6 % vs sol [max] 72.7 %, within overlapping CIs, but costs $11.84 vs $8.39 and takes 31.9 vs 18.8 mean minutes ([DeepSWE leaderboard](https://deepswe.datacurve.ai/)). Practical rule: route quality-first *interactive* work to Sol (max) in Codex, and quality-first *long-horizon async* work to Opus 5 (xhigh/max) in Claude Code.
- **Configurations to avoid for latency-sensitive routing.** Claude Sonnet 5 at high effort is both slow and weak in the fixed-harness view (48.2 % pass@1, 28.8 mean min, 146.6 steps), and Sonnet 5 [max] degenerates to 80.1 mean min, 268.5 steps and $26.40 per task for only 53.8 % ([DeepSWE leaderboard](https://deepswe.datacurve.ai/)). Fable 5 (max) in Claude Code costs $11.71 per task with a 0.659 index — worse on both axes than Opus 5 (xhigh) at $8.24 / 0.667 ([Artificial Analysis coding agents](https://artificialanalysis.ai/agents/coding-agents)).
- **Do not infer elapsed time from steps.** The measured data contradicts step-based proxies: Codex — Luna (max) runs 115.0 steps in 8.00 min while Claude Code — Opus 5 (high) runs fewer steps (92.6) in 13.37 min ([Artificial Analysis coding agents](https://artificialanalysis.ai/agents/coding-agents)); on DeepSWE, luna [max] takes 101.7 steps in 18.7 mean min while opus-5 [max] takes 99.0 steps in 31.9 mean min ([DeepSWE leaderboard](https://deepswe.datacurve.ai/)). Steps, tokens, time-to-first-token and elapsed minutes are four separate quantities here.
