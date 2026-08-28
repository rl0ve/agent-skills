# Work Router 2.1

Updated August 1, 2026. Choose a timeliness mode before the task route. Optimize for measured wall-clock time, not steps, tokens, time to first token, or output speed.

## Timeliness Modes

| Mode | Priority | Default | Measured coding-agent evidence |
|---|---|---|---|
| Fast | Minimize user-visible elapsed time | Codex, Sol Medium | 5.17 min average native-harness wall time; DeepSWE mini-swe-agent 7.1 min mean |
| Balanced | Optimize quality per minute | Codex, Sol High | 6.32 min at Coding Agent Index 0.641; DeepSWE 69.4% in 9.9 min mean |
| Economy | Minimize cost; background latency is acceptable | Codex, Luna Max | $0.313/task in Codex at 8.00 min; DeepSWE 67.2% for $0.61 in 18.7 min mean |
| Simple + fast | Finish narrow, verifiable work cheaply | Codex, Luna High | 5.65 min in Codex; use Luna Medium for classification-grade work |
| Quality-first | Maximize outcome quality | Opus 5 XHigh or Sol Max | Near-tied native-harness index: 0.667 in 23.65 min vs 0.666 in 10.17 min |

Artificial Analysis reports average active agent wall time in each native harness. DeepSWE uses mini-swe-agent and reports mean and median duration; its times are not Codex or Claude Code times ([Artificial Analysis](https://artificialanalysis.ai/agents/coding-agents), [DeepSWE](https://deepswe.datacurve.ai/)).

## Default Routing

| Work | Best quality | Fast/value |
|---|---|---|
| Orchestration and planning | Claude Code, Opus 5 High | Codex, Sol Medium |
| Executive writing | Claude, Opus 5 Max | Codex, Sol High |
| Presentations and documents | Codex, Sol Max | Codex, Sol High |
| Routine coding | Codex, Sol High | Codex, Luna High |
| Architecture, hard debugging, security | Claude Code, Opus 5 XHigh | Codex, Sol XHigh |
| Frontend and UI coding | Claude Code, Opus 5 High | Codex, Sol High |
| Data analysis | Claude, Opus 5 High | Codex, Luna Medium for clean transforms |
| Research synthesis | Codex, Sol Ultra | Codex, Sol Medium |
| Long autonomous work | Claude Code, Opus 5 XHigh | Codex, Sol Max or Ultra |

## Ten Rules

1. Choose Fast, Balanced, Economy, Simple + fast, or Quality-first before selecting the model.
2. Start interactive work with Sol Medium in Codex.
3. Use Luna High for tests, extraction, triage, small fixes, and volume subagents.
4. Use Luna Max when cost dominates and an 8 to 19 minute background run is acceptable.
5. Do not use Luna for large repositories or multi-document synthesis.
6. Raise effort one step before changing models.
7. Use Opus 5 High for novel judgment, planning, and unfamiliar problems.
8. Use Opus 5 XHigh asynchronously for the hardest architecture, debugging, and code review.
9. Use parallel agents only for independent workstreams; serialize overlapping edits.
10. Default to each provider's native harness. Mixed harnesses are bounded handoffs, not hidden routing.
11. For OpenAI long runs, use the Responses API, retain reasoning via the previous response ID, and compact rather than truncate.

## Important Changes

- Luna Max is the economy winner, not the speed winner. On DeepSWE it beats Sol Medium on pass@1, 67.2% versus 61.1%, and cost, $0.61 versus $1.86, but takes 18.7 versus 7.1 mean minutes. In native Codex, Luna Max takes 8.00 minutes versus 5.17 for Sol Medium ([DeepSWE](https://deepswe.datacurve.ai/), [Artificial Analysis](https://artificialanalysis.ai/agents/coding-agents)).
- Opus 5 now replaces Fable 5 as the premium general default. Opus 5 Max leads the measured intelligence set while costing half Fable's list token price ([Anthropic](https://docs.claude.com/en/docs/about-claude/models/overview), [Artificial Analysis](https://artificialanalysis.ai/models/claude-opus-5)).
- Sol Max leads presentation visual quality, while Anthropic models lead analytical substance. For board or executive artifacts, draft substance with Opus 5 Max and render with Sol Max ([Artificial Analysis](https://artificialanalysis.ai/articles/gpt-5-6-has-landed)).
- Codex and Claude Code tie at Coding Agent Index 67, but the measured Codex configuration completes tasks in 10.2 minutes versus 23.6 minutes for Claude Code. Codex is therefore the latency-first coding default; Claude Code remains the judgment and rubric-style QA specialist ([Artificial Analysis](https://artificialanalysis.ai/agents/coding-agents/comparisons/claude-code-vs-codex)).

## Harness Policy

### Use Codex

- Fast coding, terminal work, routine implementation, research, and final deck rendering.
- Sol Medium for interactive work.
- Sol High or XHigh for consequential engineering.
- Luna High for scoped workers.
- Sol Ultra only when four workstreams are genuinely independent.

### Use Claude Code

- Architecture, novel planning, root-cause debugging, frontend judgment, long autonomy, and rubric-style review.
- Opus 5 High for planning and unfamiliar problems.
- Opus 5 XHigh for the hardest architecture and review.
- Opus 5 Max for executive judgment, not as the normal coding setting.
- Sonnet 5 High for lower-cost Claude-side execution.

### Use Mixed Workflows Only When

1. Claude plans and Codex implements a bounded feature.
2. Codex authors and Claude Code performs an asynchronous review.
3. Anthropic drafts substance and Sol renders the deck, document, or spreadsheet.
4. Codex runs independent tests or investigations.
5. A second opinion is worth the added latency and failure surface.

Use one parent harness and one bounded specialist. The handoff must define the objective, allowed files, acceptance criteria, isolated worktree, tests, and required return: diff, test results, concise summary, and risks. Do not permit overlapping edits, repeated full-context transfers, or recursive cross-harness agent trees.

Do not route OpenAI models through Claude Code or Claude models through Codex as hidden model substitution. A Claude Code Codex plugin is appropriate for explicit asynchronous handoffs, but MCP bridging adds overhead, and Anthropic's OpenAI-compatible layer is explicitly not production-ready ([Anthropic](https://platform.claude.com/docs/en/api/openai-sdk)).

## ARC-AGI-3 Lesson

OpenAI moved the same Sol Max checkpoint from 13.3% to 38.3% on the public ARC-AGI-3 set while using six times fewer output tokens by retaining reasoning and replacing rolling truncation with compaction. This proves that results are model × effort × harness × context management; it does not prove that Codex wins every task ([OpenAI](https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/)).
