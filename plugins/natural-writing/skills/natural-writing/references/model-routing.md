# Model and agent routing for writing

Use this reference only when model or agent selection matters. Do not turn an ordinary
writing request into a routing exercise.

## Core rule

The parent agent that holds the conversation writes the final copy. It has the best
access to the user's audience, intent, corrections, sources and voice samples. Natural
Writing is the editorial specialization; a separate "writer agent" is usually
unnecessary.

**Host-native:** write in the host and model the user is working in. Do not dispatch
writing between Codex and Claude unless the user asks for a cross-provider comparison
or workflow. When Work Router is installed it owns model, effort and delegation; this
file only adds what is specific to prose.

## Effort for prose

- Medium effort is the default. More reasoning is not automatically better prose.
- Use high effort for difficult argument structure, ambiguous evidence, delicate
  positioning or close voice calibration.
- Reserve xhigh or max for high-stakes review, not routine composition. Excess
  deliberation produces scaffolding, taxonomies, caveats and symmetrical structure
  the prose does not need.
- A strong writing sample matters more than a one-step model upgrade.

## Source-heavy writing

A scout or research agent may gather and organize evidence. It must not become the
final voice. The parent writes from the evidence it returns.

## One writer, one reviewer

For consequential prose:

1. The parent writes or edits the complete piece with the user's full context.
2. A fresh read-only reviewer checks factual preservation, voice drift, generic
   assistant phrasing, repetition, over-formatting and the strength of the opening
   and ending.
3. The parent evaluates the findings and makes the final changes.

Do not let two write-capable agents revise the same artifact in parallel. Competing
rewrites blur ownership and flatten voice.

## Reviewer contract

A Natural Writing reviewer:

- is read-only;
- quotes only the smallest useful excerpts;
- separates factual or voice failures from optional preferences;
- raises no more issues than materially affect the reader;
- proposes repair directions rather than replacing the piece;
- makes no AI-authorship guesses or detector claims;
- returns "no material issues" when the draft already works.

A fast scout, an implementation agent or a research agent is never the final
editorial authority.
