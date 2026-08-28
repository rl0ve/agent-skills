# Model and agent routing for writing

Use this reference only when model or agent selection matters. Do not turn an ordinary writing request into a routing exercise.

## Core rule

The parent agent that holds the conversation should normally write the final copy. It has the best access to the user's audience, intent, corrections, source material, and voice samples. Treat Natural Writing as the editorial specialization; a separate “writer agent” is usually unnecessary.

Use the host the user chose. Do not dispatch work between Codex and Claude unless the user explicitly asks for a cross-provider comparison or workflow.

Prefer model families or roles over exact version numbers. Select the newest permitted model in the named family so this guidance does not become stale when providers update their lineups.

## Default routing matrix

| Work | Codex | Claude | Notes |
| --- | --- | --- | --- |
| Routine drafting, editing, and rewriting | Parent Sol-family model, medium effort | Parent Sonnet-family model, medium effort | Best default balance of judgment, speed, and voice fidelity. |
| Executive, persuasive, creative, or unusually voice-sensitive prose | Parent Sol-family model, high effort | Parent Opus-family model, medium or high effort | Escalate only when nuance or consequences justify it. |
| Source-heavy writing | Terra-family explorer gathers and organizes evidence; parent Sol writes | Haiku may scan or gather; parent Sonnet or Opus writes | The research agent must not become the final voice. |
| Consequential final audit | Sol advisor or equivalent read-only reviewer | Opus-family read-only reviewer | Reviewer returns findings; parent decides and applies edits. |
| Long-horizon, corpus-scale project | Parent Sol with research support | Fable-family model only when sustained autonomous work is genuinely needed | Do not use a long-horizon agent merely to improve an email, memo, post, or article. |

## Effort policy

- Default to medium effort. More reasoning is not automatically better prose.
- Use high effort for difficult argument structure, ambiguous evidence, delicate positioning, or close voice calibration.
- Reserve xhigh or max for exceptional analysis or high-stakes review, not routine composition. Excess deliberation can produce scaffolding, taxonomies, caveats, and symmetrical structure the prose does not need.
- A strong representative writing sample matters more than a one-step model upgrade.

## One-writer, one-reviewer pattern

For consequential prose, use two passes:

1. The parent writes or edits the complete piece with the user's full context.
2. A fresh read-only reviewer checks factual preservation, voice drift, generic assistant phrasing, repetition, over-formatting, and the strength of the opening and ending.
3. The parent evaluates the findings and makes the final changes.

Do not let two write-capable agents revise the same artifact in parallel. Competing rewrites tend to blur ownership and flatten voice.

## Reviewer contract

If a dedicated Natural Writing Reviewer is available, it should:

- be read-only;
- quote only the smallest useful excerpts;
- separate factual or voice failures from optional preferences;
- identify no more issues than materially affect the reader;
- propose repair directions rather than replacing the entire piece;
- avoid AI-authorship guesses and detector claims;
- return “no material issues” when the draft already works.

Do not use a fast scout, implementation-focused agent, or research agent as the final editorial authority. Those roles can locate patterns or evidence, but the context-holding parent should own the finished prose.
