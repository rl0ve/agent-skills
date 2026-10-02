# Routing policy basis

**Current review:** October 2, 2026 against Claude Code, Anthropic, Arena and
Artificial Analysis. See the [Opus 5.5 assessment](opus-5-5-review.md) for exact
configurations, dates, evidence limits and conditional integration guidance.

## Product facts used by the router

- Claude Code supports the model aliases `haiku`, `sonnet`, `opus`, and `fable` for subagents. A company allowlist can substitute or block a requested family.
- Current Claude Code effort levels are `low`, `medium`, `high`, `xhigh`, and `max` on current model families, with model- and organization-specific limits.
- Opus 5.5 defaults to medium effort in the current Claude Code documentation.
  Verify the provider's actual alias resolution and current host support.
- Anthropic recommends checking context first. Increase model capability when the model knew the relevant facts and still could not solve the problem; increase effort when it skipped files, verification, or follow-through.
- Higher effort changes more than private thinking. It also affects files read, tool use, verification, and persistence through multi-step work.
- Skills load their full body only when invoked, while component descriptions contribute a small always-on token cost. Keep descriptions short and detailed references lazy.

## Policy implications

1. Parent execution is the latency winner for trivial and tightly coupled work.
2. Haiku is useful for bounded evidence collection, not ambiguous implementation.
3. Keep Sonnet low/medium for bounded planned work when it meets the checks. Start
   substantial Claude implementation and planning at Opus 5.5 medium; high fits
   difficult diagnosis and consequential edge-case verification.
4. Choose xhigh/max for justified deeper work, not from an old model's effort label
   or a Max-only leaderboard row. Low fits supervised small tasks or measured savings.
5. Prefer Opus 5.5 for long work and prose before automatically selecting Fable.
   Retain Fable for explicit preference, representative quality evidence or an Opus
   capability/style limit. Natural Writing remains the final prose editor.
6. Parallel subagents multiply context and output tokens. Use them only for independent questions.
7. One writer avoids conflict, duplicated verification, and expensive integration repair.

## Historical Sonnet 5 dominance claim: superseded for current models

**Reviewed 2026-09-17; qualified October 2.** The direction rested on older harness evidence.
The prompt that triggered the old change was a secondary synthesis whose numbers
did not survive checking. Retain the verified older rows, not that synthesis table.

The load-bearing evidence is already in
[source-wall-clock-evidence.md](source-wall-clock-evidence.md): on the DeepSWE
leaderboard's fixed harness, Sonnet 5 at high effort is both slow and weak (48.2% pass@1,
28.8 mean minutes, 146.6 steps), and Sonnet 5 at max degenerates to 80.1 mean minutes,
268.5 steps and $26.40 per task for 53.8%. Artificial Analysis's coding-agent figures put
Fable 5 (max) at $11.71 per task for a 0.659 index, worse on both axes than Opus 5 (xhigh)
at $8.24 for 0.667. [source-research-evidence.md](source-research-evidence.md) reaches the
same verdict on Sonnet 5 max independently: avoid it unless cost-pinned to Sonnet and
latency is irrelevant, given a 188-second measured TTFT.

Those rows do not establish a universal Sonnet effort ceiling, rank Sonnet 5.5,
or make Max inefficient in every current family. Opus 5.5's medium/high/xhigh/Max
rows now have distinct tradeoffs. Preserve this history to explain the old route;
follow the current assessment for new decisions. The original Opus-low versus
Sonnet-medium margin was a judgment even at the time.

**What was discarded, and why it matters.** The synthesis that prompted this revision
presented an Intelligence Index v4.3 score-versus-burn table covering all fifteen
settings, including 28 for Sonnet 5 medium and 32 for Sonnet 5 high. Those two numbers
cannot be what they claim: this repository's own check, recorded at the end of
[source-research-evidence.md](source-research-evidence.md), found that Artificial Analysis
shows N/A for the Sonnet 5 Intelligence Index at medium and high, and that Sonnet 5 has no
row at all in the Coding Agent Index v1.3. Treat the rest of that table's figures as
unsourced. Its per-task burn column was also benchmark-harness API dollars, with no
published conversion to Pro/Max allowance depletion, and it carried no retry column -
hence policy rule 8: count retries, because a first-attempt success usually beats a
nominally cheaper route corrected twice.

Older practitioner reports about Opus-low output length and eager delegation do
not establish 5.5's behavior. Count actual output, duplicate context and retries;
retain bounded delegation and one writer independently of model revision.

The prior automatic Fable prose route was based on one September talk-track session,
where Fable caught issues two Opus passes had missed and left 11 of 40 pieces alone.
The Opus revision was not a controlled 5.5 comparison. Retain that evidence for the
same voice/assignment; do not transfer it into a universal Fable preference.

Representative accepted work can override these starting recommendations. Preserve
task, tools, acceptance criteria, effort, actual revision and total completion cost.

## Primary sources

- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/slash-commands
- https://claude.com/blog/claude-model-and-effort-level-in-claude-code
- https://claude.com/resources/tutorials/choosing-the-right-claude-model

This router is an engineering policy. It is not a claim that the plugin itself has been benchmarked against Claude Code's native delegation behavior.

## Subscription billing update: October 1, 2026

The older claim that Fable always bills separately is superseded. Anthropic's
[current plan documentation](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)
includes Fable 5 and 5.1 on Max and specified premium seats, up to 50% of the
regular weekly allowance. It shares that allowance and consumes it faster; it is
not an additional 50%. Pro and standard Team seats require usage credits.
API use is billed separately. Check live plan eligibility and remaining limits.

[Claude Code plan authentication](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)
also matters: subscription login and an API-key billing route are different.
Do not convert benchmark API prices into subscription debits, or enable extra
usage merely because a model is recommended. This correction does not establish
a new performance ranking between Opus and Fable.
