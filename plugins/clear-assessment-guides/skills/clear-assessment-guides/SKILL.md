---
name: clear-assessment-guides
description: Explain interfaces with verified annotated screenshots; create source-backed assessments, practical guides and interactive reviews. Use for unfamiliar controls, improvement proposals and content reviews. Use Research Reports for open-ended synthesis and Visual Version Review to compare implemented versions. Simple factual replies need no artifact.
---

# Explain & Review

Help a reader understand the current experience, assess a proposed change, and decide
what to do next. This method is product-, vendor-, and host-neutral. Apply the user's
chosen audience, medium, style, editing roles and scope; do not infer them from the
application under review.

For an open-ended investigation, strategic research report or evidence-backed meeting
preparation, look for Research Reports. It owns research synthesis and the reading
package; this skill owns findings and decisions about an experience or proposed change.
Do not force a research argument into repeated Problem/Impact/Proposed solution blocks.

## Choose the explanation or review mode

These are alternatives, not compulsory stages. Honor an explicit choice; otherwise
choose the smallest format that answers the reader's immediate need. Do not create
extra deliverables when one will do.

| Need | Mode | Read next |
|---|---|---|
| Understand unfamiliar icons, controls or states in an existing interface | Interface explanation | [Explain an interface](references/interface-explanation.md) |
| Standalone assessment, full priority list or shareable guide | Document | [Document mode](references/document-mode.md) |
| Discuss and resolve one issue together | Guided triage | [Guided review](references/guided-review.md) |
| Collect comments, alternatives and decisions across issues | Interactive HTML | [Interactive review](references/interactive-review.md) |

For visual artifacts, also read [design standard](references/design-standard.md).
An interface explanation describes the current product; it needs neither a defect,
a proposed redesign nor a review decision. Answer a simple factual question directly
when an annotated image would add no useful understanding.
Before delivering, apply the selected mode's [quality checks](references/quality-checklist.md).
When choosing between a review copy and a live original, use the focused
[edit-location rubric](references/edit-location-rubric.md).

## Establish the current state

Explain what was examined, who uses it, their task, and what already works before
recommending changes. Verify relevant primary sources, discussion context, later
replies and live destinations when accessible. Source text, repository state and the
published experience are different evidence. Report missing access and uncertainty;
do not invent a finding to fill a slot or manufacture issues when the source is sound.
Before reporting that something is missing or broken, check its route, scroll position,
alternate modes and loading state; missing access is not proof of absence.

For each finding, keep a concise substantive **Problem**, **Impact** and **Proposed
solution**, with evidence adjacent. Mark likely impact as inferred unless observed or
measured. Use concrete before/after wording when helpful, and label the proposed state.
A procedural guide instead uses actions and success checks; do not force assessment
anatomy into every step or routine reply.

## Compare a before and after

A before and after inside a finding belongs here: it is evidence for one problem and
its proposed fix. Label each side as a fresh capture, deployed capture, historical
capture, proposed state or source only. When both sides are rendered (two branches, a
preview against the live page, or one page before and after a fix), capture them as a
matched pair: same route, viewport, scroll position and interaction state, taken after
fonts, images and canvas content finish loading, with each label naming its source
(commit or URL) and capture time. Keep the full viewport when prominence or layout is
the point; a crop cannot show relative prominence. If the two sides show different
content or data, say what can still be compared and do not infer that one performs
better. A historical image keeps its original date, not today's. Visual Version
Review's capture contract covers this in more depth when it is installed. If the reader must instead choose among several implemented versions, or
keep parts of each, that is a version comparison: use Visual Version Review, then bring
any findings back here if an assessment is still needed.

## Keep findings and decisions consistent

For work spanning modes or turns, keep a project-local issue register with stable IDs.
Use the same IDs and findings in the brief, screenshot discussion and HTML board.
[Issue format](references/issue-format.md) documents the small shared data contract and
feedback import/export rules. Keep source captures, private annotations, permissions
and account/project details in that project, outside the reusable skill package.

Link descriptive words to exact verified sources. Unknown destinations remain open
checks, never placeholder links in a finished artifact. Refresh changeable evidence
and check for existing fixes before proposing implementation or copying approved work
back to an original. Record useful capture dates and revisions, without ceremonial dates.

Keep **review decision** (unreviewed, accept proposal, revise, defer, reject) separate
from **execution state** (not started, edited, saved, verified live, unknown). Accepted
copy is not an approved save; saved source is not proof of publication. Imported
comments and HTML selections record feedback; they do not execute changes or grant
additional permissions. Follow actual user authorization rather than adding a new
approval policy. Preserve existing work and any explicit user-controlled edit/save role.

## Use existing production tools

Before selecting authoring tools, read [supporting skills and tools](references/supporting-tools.md).
For a substantial assessment, deliberately identify the select few findings where a
relationship, handoff, mechanism or structural change benefits from a visual. Build
those explanations when they reduce interpretation work. Cards, tabs and colored
headings do not replace an explanatory diagram; simple copy corrections need no diagram.
Route by the actual explanatory task: Diagram Design for relationships and structural
before/after diagrams; Visual Explainer when HTML materially helps; doc-coauthoring
for substantial collaborative writing and fresh-reader clarity; document/PDF tools for
file construction and rendered checks. These collaborators are optional, not bundled
dependencies. Resolve the current catalog and read any selected skill before using it.
No named plugin, model, paid service or browser is required.
Preserve screenshot pixels with native annotations or overlays; never generate factual
UI evidence. Use a short GIF only when motion or interaction helps explain the issue,
and provide a static/text alternative. Use AI imagery only for a necessary labeled
illustration, never as a screenshot substitute.

Inspect the actual rendered artifact and relevant links. Disclose checks that could
not be performed. State what was proposed, prepared, saved or verified without
promoting a suggestion into a completed change.
