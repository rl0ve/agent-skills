# Help the user steer the design

Use for a substantial new design or redesign when visual direction is unresolved.
For a small defined edit, an established design system, or a clear fidelity reference,
follow the existing direction and do the work. Do not add a questionnaire or options
round to every UI task. If the uncertainty is about users, objects or behavior,
use [product-decisions.md](product-decisions.md) for that decision first.

## Turn context into a short brief

Read the conversation, existing interface, project design notes and supplied references.
Infer the intended audience, main task, content priorities, constraints and things to
preserve. State only consequential assumptions and ask about gaps that materially
change the result. Do not ask the user to repeat known information or supply design
terminology. Keep implementation vocabulary in the agent's work, not the user's brief.

Separate decisions the agent should make through craft (type scale, spacing, motion
implementation, accessibility) from choices that need the user's intent or taste
(what matters most, recognizable brand traits, desired feeling, unacceptable changes).
Explain a tradeoff in terms of what the user will see or be able to do.

## Make uncertain direction concrete

When plausible directions would produce meaningfully different results, show two or
three relevant references or small previews, with a recommendation and one sentence
about each tradeoff. Prefer visual evidence over abstract style labels. Keep content
and the represented task comparable so the choice is about design, not different copy
or missing functionality. Do not build several complete products to solicit feedback.

Use the user's reference first. Clarify whether it supplies inspiration or requires
fidelity only when that distinction is unresolved. Apply the reference method in
[visual-resources.md](visual-resources.md) to extract the traits that matter. If the
user has already chosen a direction, do not reopen it merely to display alternatives.

Invite a concrete reaction, such as which direction feels closest and what should be
kept or changed. Use the host's question/input tools when available. Ask early enough
for the answer to inform the work; continue independent authorized work while waiting.
If an answer is required, do not treat silence as approval. If the choice is optional
or the user delegates taste, proceed with the recommended direction, label the
assumption, and keep it easy to revise. Do not add an approval gate for routine craft.

## Translate reactions into bounded changes

Plain-language feedback is sufficient. Translate it into a proposed visual change
while preserving existing scope and constraints. For example, “too corporate” might
suggest less generic imagery or a more distinctive type treatment; it does not by
itself authorize reducing useful density, removing information or adding animation.
“I like this typography” selects a type treatment, not the reference's entire layout.
“Keep the density” should survive later spacing and hierarchy refinements.

When several interpretations would lead to materially different work, offer the most
likely interpretation with a focused question or small comparison. Otherwise make
the smallest supported change and show the result. Do not require the user to name
fonts, easing curves or layout systems to express a preference.

## Establish a representative slice, then expand

Choose one region or interaction that exposes the important design decisions, such
as a hero with real content or a dense list with its key action. Reuse existing work
when it already provides that evidence. Implement and inspect it against the brief,
references and relevant viewport/state before extending the approach.

Seek feedback before costly expansion when unresolved taste could change the whole
design. Respect an instruction to proceed autonomously. Once direction is chosen,
apply it consistently and keep moving; do not repeatedly ask approval for each screen.
User preference feedback does not replace accessibility, behavior or responsive checks
in [quality-gates.md](quality-gates.md).

## Retain project decisions

Update the project's existing design notes when useful; create a short project-local
note only when the task needs a durable record. Keep the chosen direction, reference
URLs and their intended contribution, things to preserve or avoid, key decisions,
and consequential unresolved assumptions. Distinguish user choices from agent
assumptions. Update settled decisions rather than accumulating contradictory drafts.
Do not reopen them without new evidence or a user change of direction.

Project taste and private feedback stay in the project. Do not turn them into global
preferences, write agent memories, or publish them in a shared skill. The reusable
skill owns this steering method; specialist skills continue to own design execution.
