# Routing policy basis

**Verified:** 2026-08-18 against current Claude Code and Claude model documentation.

## Product facts used by the router

- Claude Code supports the model aliases `haiku`, `sonnet`, `opus`, and `fable` for subagents. A company allowlist can substitute or block a requested family.
- Current Claude Code effort levels are `low`, `medium`, `high`, `xhigh`, and `max` on current model families, with model- and organization-specific limits.
- Anthropic describes Haiku as the lightest quick route, Sonnet as the versatile coding default, Opus as the complex-reasoning expert, and Fable as the heaviest long-horizon model.
- Anthropic recommends checking context first. Increase model capability when the model knew the relevant facts and still could not solve the problem; increase effort when it skipped files, verification, or follow-through.
- Higher effort changes more than private thinking. It also affects files read, tool use, verification, and persistence through multi-step work.
- Skills load their full body only when invoked, while component descriptions contribute a small always-on token cost. Keep descriptions short and detailed references lazy.

## Policy implications

1. Parent execution is the latency winner for trivial and tightly coupled work.
2. Haiku is useful for bounded evidence collection, not ambiguous implementation.
3. Sonnet low and medium are the routine routes for mechanical and already-planned work. Sonnet high, xhigh and max are dominated: Opus low reaches higher quality for comparable or lower cost per completed task, so Opus low is the implementation and planning default and Opus medium is its first escalation. Basis and limits below.
4. Opus high is for expert judgment and hard diagnosis, not every code change.
5. Fable is for projects larger than a normal sitting and should not be a default merely because it is available.
5a. Fable is also the route for prose whose quality is the deliverable, at any size. Family ranking by reasoning difficulty does not predict writing quality, so a short talk track can be correct work for the heaviest family while a large refactor is not. Basis: observed on a keynote talk-track set in Sep 2026, where a Fable pass found key-point echo, stage directions in spoken lines and unsayable written constructions that two prior Opus passes had walked past, and correctly declined to edit 11 of 40 pieces. That is one session, not a benchmark.
6. Parallel subagents multiply context and output tokens. Use them only for independent questions.
7. One writer avoids conflict, duplicated verification, and expensive integration repair.

## The Sonnet-above-medium dominance claim

**Reviewed 2026-09-17.** The direction rests on this repository's own harness evidence.
The prompt that triggered the change was a secondary synthesis whose numbers do not
survive checking; keep the conclusion and discard its table.

The load-bearing evidence is already in
[source-wall-clock-evidence.md](source-wall-clock-evidence.md): on the DeepSWE
leaderboard's fixed harness, Sonnet 5 at high effort is both slow and weak (48.2% pass@1,
28.8 mean minutes, 146.6 steps), and Sonnet 5 at max degenerates to 80.1 mean minutes,
268.5 steps and $26.40 per task for 53.8%. Artificial Analysis's coding-agent figures put
Fable 5 (max) at $11.71 per task for a 0.659 index, worse on both axes than Opus 5 (xhigh)
at $8.24 for 0.667. [source-research-evidence.md](source-research-evidence.md) reaches the
same verdict on Sonnet 5 max independently: avoid it unless cost-pinned to Sonnet and
latency is irrelevant, given a 188-second measured TTFT.

That is enough to retire Sonnet above medium and to treat `max` as off the frontier in
every family. It does not by itself establish the Opus-low-versus-Sonnet-medium margin,
which remains a judgment.

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

One caveat on Opus low survives from the practitioner reports rather than from
measurement: low effort is said not to shorten its output, and it delegates to subagents
readily, so real burn can exceed a per-task estimate. Treat that as a thing to watch on a
long run, not an established figure.

**This policy steers away from a product default.** Sonnet 5 high is the default effort on
the Claude API and in Claude Code. Narrowing Sonnet to low and medium is therefore a
deliberate departure, and worth restating to anyone who inherits this router.

Anthropic's own guidance still names Sonnet the everyday interactive default and Opus
the escalation for hard diagnosis and multi-file scope, and separate guidance argues
xhigh is the floor for demanding long-horizon agentic runs. This policy does not
contradict either: it narrows Sonnet to low and medium rather than demoting the family,
and it keeps high and xhigh Opus for long autonomous runs where low effort stalls.

Treat the ordering as falsifiable. If a Sonnet high route is landing work you keep on the
first attempt, that evidence outranks this note. Prefer a measured run in your own harness
over any leaderboard row, and over this paragraph.

## Primary sources

- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/slash-commands
- https://claude.com/blog/claude-model-and-effort-level-in-claude-code
- https://claude.com/resources/tutorials/choosing-the-right-claude-model

This router is an engineering policy. It is not a claim that the plugin itself has been benchmarked against Claude Code's native delegation behavior.
