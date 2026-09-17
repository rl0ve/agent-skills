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

**Reviewed 2026-09-17.** This is routing judgment from a secondary synthesis, not a
measurement this plugin made.

The ordering came from a comparison built on Artificial Analysis Intelligence Index v4.3
scores against estimated per-task burn. On that data Opus low scored well above Sonnet
medium for roughly a tenth more burn, and above Sonnet max while consuming far less.
Every Sonnet setting above medium fell off the efficient frontier, as did every `max`
setting in all three families: Sonnet max scored below Opus low at several times the
burn, Opus max showed no gain over Opus xhigh, and Fable max tied Fable xhigh for about
a quarter more. Six of fifteen settings were strictly dominated, collapsing the usable
ladder to Sonnet low/medium, Opus low, Opus medium, and the Fable medium-to-high band,
with Opus high/xhigh preferred over Fable medium for long autonomous runs because Fable
bills separately.

Four limits keep this a heuristic rather than a fact:

- Intelligence Index v4.3 is a composite of math, science, coding and reasoning. It is
  not an agentic-coding measurement, which is what this router actually routes.
- The burn figures are benchmark-harness API dollars. Anthropic publishes no conversion
  to Pro/Max allowance depletion, so the ratios do not transfer to a plan.
- Retry count is absent from the comparison and often dominates real cost per task.
  Hence policy rule 8: count retries.
- Opus low reportedly does not shorten its output and delegates eagerly, so its real
  burn can exceed the estimate. Corroborating reports here are practitioner posts, not
  controlled runs.

Anthropic's own guidance still names Sonnet the everyday interactive default and Opus
the escalation for hard diagnosis and multi-file scope, and separate guidance argues
xhigh is the floor for demanding long-horizon agentic runs. This policy does not
contradict either: it narrows Sonnet to low and medium rather than demoting the family,
and it keeps high and xhigh Opus for long autonomous runs where low effort stalls.

Treat the ordering as falsifiable. If a Sonnet high route is landing work you keep on
the first attempt, that evidence outranks this note.

## Primary sources

- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/slash-commands
- https://claude.com/blog/claude-model-and-effort-level-in-claude-code
- https://claude.com/resources/tutorials/choosing-the-right-claude-model

This router is an engineering policy. It is not a claim that the plugin itself has been benchmarked against Claude Code's native delegation behavior.
