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
3. Sonnet medium is the routine implementation route; high is the thorough parent route.
4. Opus high is for expert judgment and hard diagnosis, not every code change.
5. Fable is for projects larger than a normal sitting and should not be a default merely because it is available.
5a. Fable is also the route for prose whose quality is the deliverable, at any size. Family ranking by reasoning difficulty does not predict writing quality, so a short talk track can be correct work for the heaviest family while a large refactor is not. Basis: observed on a keynote talk-track set in Sep 2026, where a Fable pass found key-point echo, stage directions in spoken lines and unsayable written constructions that two prior Opus passes had walked past, and correctly declined to edit 11 of 40 pieces. That is one session, not a benchmark.
6. Parallel subagents multiply context and output tokens. Use them only for independent questions.
7. One writer avoids conflict, duplicated verification, and expensive integration repair.

## Primary sources

- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/slash-commands
- https://claude.com/blog/claude-model-and-effort-level-in-claude-code
- https://claude.com/resources/tutorials/choosing-the-right-claude-model

This router is an engineering policy. It is not a claim that the plugin itself has been benchmarked against Claude Code's native delegation behavior.
