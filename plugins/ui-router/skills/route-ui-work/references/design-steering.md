# Help the user steer the design

Use for a substantial new design or redesign when visual direction is unresolved,
a prominent component choice, or an iteration whose interpretation would materially
change the experience.
For a small defined edit, a choice already covered by the design system, or a clear fidelity reference,
follow the existing direction and do the work. Do not add a questionnaire or options
round to every UI task. If the uncertainty is about users, objects or behavior,
use [product-decisions.md](product-decisions.md) for that decision first.

For a rejected palette, visual sameness, or a requested expressive reference that was
lost in implementation, use [art-direction.md](art-direction.md) to diagnose lead
identity, aesthetic-rule conflicts, and the distinction between purpose and styling.

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

For substantial visual work, turn the direction into a few concrete decisions before
polishing: the focal point and hierarchy, type roles and scale, spacing relationships,
palette roles, imagery or material treatment, and the purpose of motion when present.
Use real copy where available. Reuse the existing system and project notes; this is
the agent's design work, not a template the user must fill out. For text-bearing
generated art, verify the lettering; use separately typeset text when generation
cannot preserve the required copy.

## Show samples at useful decision points

Choose the smallest comparison that resolves the actual decision. Offer visual
evidence proactively when these triggers apply; do not wait for the user to request
samples or turn every build into a gallery tour.

| Moment | Show | Skip when |
|---|---|---|
| New direction | Two or three relevant references or small previews, with a recommended direction | The user supplied a clear specification or the system is settled |
| Prominent component or interaction | Two or three examples of the same region or behavior, such as navigation, gallery, timeline, composer or hero | The established component already satisfies the task |
| Before costly expansion | One working representative slice with realistic content and relevant states | Existing work already demonstrates the chosen direction |
| Meaningful iteration | The current treatment beside one or two alternatives focused on the unresolved issue | Feedback specifies a clear, small correction |

Use the host's visual display or browser tools to make the samples visible. Prefer
permitted source previews for references, playable demos for motion, and a local
working preview for adaptations. Include direct source links and creator credit.
A list of homepages or style adjectives is not a visual comparison. If access or
display is unavailable, state the limit and use an accessible reference or clearly
labeled approximation; do not claim to have inspected an unseen example. Respect
source restrictions on screenshots, embeds and redistribution.

Label each sample as a source reference, an adaptation, or an implemented preview.
For each, state what to borrow, what the user gains or gives up, and which option you
recommend. The user should be able to select typography, structure, density or motion
independently without adopting an entire reference. When showing custom alternatives,
keep content, task, viewport and represented state comparable. Explain material
differences in source examples rather than pretending they are controlled comparisons.

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

Choose references by the current project's purpose and character. When it adds a
useful idea, include one relevant reference from another domain and explain the
transferable trait. Do not default to business software, a chat layout, or an AI
component library because of the user's background or the agent doing the work.
Treat an available component as a candidate: adapt it to the chosen system rather
than combining unrelated gallery styles or changing frameworks to match a demo.

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

If an iteration changes direction or repeated corrections show that the current
interpretation is failing, return to a small comparison of the disputed region.
Keep the accepted baseline visible and explain the intended difference. Do not
restart research across the whole product or reopen unrelated settled choices.

Refine one or two consequential variables at a time when diagnosing visual feedback,
so the comparison reveals what helped. For a material or motion study, a few temporary
preview controls can make alternatives easier to judge; keep them out of the finished
interface unless adjusting those properties is itself part of the user's task.

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

For reused components, also retain the original source, the selected variant and
material adaptations. Capture rejected traits only when they prevent repeated
misinterpretation; do not build a growing archive of discarded mockups.

Project taste and private feedback stay in the project. Do not turn them into global
preferences, write agent memories, or publish them in a shared skill. The reusable
skill owns this steering method; specialist skills continue to own design execution.
