# Opus 5.5 routing review

Reviewed October 2, 2026. This assessment supersedes the Opus 5 implementation,
effort and automatic Fable preferences; historical source packs retain their dates.
It changes Claude routes and informs an open host choice, not the available models
inside a running Codex task.

## Product and host facts

[Anthropic's model overview](https://platform.claude.com/docs/en/models/opus-5-5/overview)
lists `claude-opus-5-5`, released September 22, with a 1M context, 128K maximum
output, always-on adaptive thinking and medium default effort. Standard API input/
output pricing is $4/$20 per million tokens; cache reads are $0.20. These are API
prices, not subscription debits or complete-task costs.

[Claude Code model configuration](https://code.claude.com/docs/en/model-config)
requires version 2.1.280 or later. The `opus` alias resolves differently by provider:
the documented Anthropic route uses 5.5 while Foundry still uses 4.6. An override,
gateway or organization policy can change that. Verify the actual model ID and
supported effort; use a full provider-supported ID when the exact revision matters.
Portable plugin aliases remain aliases, not proof that a session uses 5.5.

## Decision-driving evidence

The [Arena WebDev overall board](https://arena.ai/leaderboard/code), dated October 1
and checked October 2, reports:

| Configuration | Score / marginal interval | Votes | Rank spread |
|---|---|---:|---|
| Opus 5.5 Max | 1815 +/-16 | 2,062 | 1-2 |
| Astra 6 Max | 1788 +/-10 | 6,123 | 2-3 |
| Sol 6.1 Max | 1758 +/-17 | 1,620 | 3-5 |
| Fable 5.1 Max | 1749 +/-10 | 6,318 | 4-5 |

This supports Opus 5.5 as a quality-focused route when starting substantial UI
work with host choice open. Rank uncertainty remains; the board measures preference
in that setup, not maintainability, accessibility, native-harness time or medium/
high performance. Harness version, budgets and service tier were not disclosed in
the retrieved rows. No domain-specific winner is inferred from the overall board.

[Artificial Analysis's September 22 evaluation](https://artificialanalysis.ai/articles/claude-opus-5-5)
reports Intelligence Index v4.3.2 58 at Max with default fallback enabled,
Terminal-Bench 4.0 59.6%, AA-Briefcase v1.1 Elo 1822 and GDPval-AA v2.1 Elo 1846.
It reports higher analytical and presentation scores than Fable 5.1, while Fable
remains slightly ahead on the Briefcase rubric. These knowledge-work evaluations
do not directly rank voice matching or spoken cadence. The index includes its
constituent benchmarks; they are not independent replications. Max also used more
output tokens per task than Opus 5 Max, so cheaper tokens do not imply lower burn.

The current [high/medium comparison](https://artificialanalysis.ai/models/comparisons/claude-opus-5-5-high-vs-claude-opus-5-5-medium)
reports index 54/51 and Terminal-Bench 4.0 57%/53%, with default fallback enabled.
This shows an effort tradeoff, not a need to run every task at Max. Anthropic's
[Claude Code effort guidance](https://code.claude.com/docs/en/model-config#adjust-effort-level)
starts 5.5 at medium and recommends calibrating instead of inheriting Opus 5 effort.
Higher levels remain conditional on the task and accepted quality.

[METR's preliminary predeployment assessment](https://metr.org/blog/2026-09-22-claude-opus-5-5/)
found incremental improvement over Fable 5.1 on five AI-R&D tasks. It did not find
full AI-R&D automation or establish a human-task time horizon for this router.
The original [Terminal-Bench page](https://www.tbench.ai/) did not expose a populated
4.0 board in this retrieval; the numeric result above is AA's independent evaluation.
No matched local Claude Code/Codex timing trial or paid generation was run.

## Apply the assessment

- Start new substantial Claude implementation, analysis and prose at Opus 5.5
  medium; high for difficult diagnosis or consequential verification. Low remains
  suitable for small supervised work. A critical xhigh review needs a concrete
  reason; Max is not a general default or a necessary ladder rung.
- Keep Sonnet for bounded planned work. Retire the blanket dominance claim based
  on Sonnet 5 versus Opus 5; it cannot settle the 5.5 comparison.
- Prefer Opus 5.5 before automatically selecting Fable for a long job or prose.
  Preserve explicit Fable choices and task-specific evidence of a better result.
- Preserve active context and explicit host/model constraints. In Codex, use the
  supported Codex models. An open host comparison may recommend Claude; it cannot
  switch a session, enable paid API use or change service tier.

## Conditional harness and UI guidance

For custom integrations, follow the
[migration guide](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide):
thinking cannot be disabled or assigned a manual budget; forced tool selection is
rejected. Preserve thinking blocks only within the same model and conversation.
Check the supported computer-use tool version. Parse response blocks by type;
between-tool progress uses thinking blocks and needs the documented display mode.
These are integration checks, not reasons to modify a stock Claude Code installation.

The [Opus 5.5 prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
suggests evidence-based completion checks for unattended runs: a text-only end of
turn can be a progress report. Inspect remaining requirements and pending work;
use bounded continuations and stop repeated no-progress loops for review. Optional
elapsed-time signals can help a permitted agent team; they do not authorize
delegation or make requirements optional. For cross-app work, retrieve relevant
records before changing them and preserve untrusted-content boundaries.

For UI, give concrete reference traits and task-specific constraints instead of
a vague request to avoid generic design. Do not turn the provider's example styles
into a universal ban. Use original high-resolution visual evidence; crop/zoom dense
charts or diagrams when necessary. A better visual reader still needs rendered,
responsive and exercised-interaction checks.

Revisit this route when relevant category evidence, provider support or representative
accepted-work results change. A release claim or API throughput cannot prove the
fastest reliable completion for a specific user's task.
