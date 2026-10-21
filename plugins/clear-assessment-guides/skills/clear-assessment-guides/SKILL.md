---
name: clear-assessment-guides
description: Create source-backed assessments and practical guides, walk through annotated issues one at a time, or build an interactive HTML review with comments and decisions. Use for improvement briefs, content reviews, guided triage and before/after checks of a change; to choose among several implemented versions, use Visual Version Review. Not a mandatory format for ordinary replies or every document.
---

# Clear Assessment Guides

Help a reader understand the current experience, assess a proposed change, and decide
what to do next. This method is product-, vendor-, and host-neutral. Apply the user's
chosen audience, medium, style, editing roles and scope; do not infer them from the
application under review.

## Choose the review mode

These are alternatives, not compulsory stages. Honor an explicit choice; otherwise
choose the smallest format that answers the reader's immediate need. Do not create
three deliverables when one will do.

| Need | Mode | Read next |
|---|---|---|
| Standalone assessment, full priority list or shareable guide | Document | [Document mode](references/document-mode.md) |
| Discuss and resolve one issue together | Guided triage | [Guided review](references/guided-review.md) |
| Collect comments, alternatives and decisions across issues | Interactive HTML | [Interactive review](references/interactive-review.md) |

For visual artifacts, also read [design standard](references/design-standard.md).
Before delivering, apply the selected mode's [quality checks](references/quality-checklist.md).
When choosing between a review copy and a live original, use the focused
[edit-location rubric](references/edit-location-rubric.md).

## Establish the current state

Explain what was examined, who uses it, their task, and what already works before
recommending changes. Verify relevant primary sources, discussion context, later
replies and live destinations when accessible. Source text, repository state and the
published experience are different evidence. Report missing access and uncertainty;
do not invent a finding to fill a slot or manufacture issues when the source is sound.

For each finding, keep a concise substantive **Problem**, **Impact** and **Proposed
solution**, with evidence adjacent. Mark likely impact as inferred unless observed or
measured. Use concrete before/after wording when helpful, and label the proposed state.
A procedural guide instead uses actions and success checks; do not force assessment
anatomy into every step or routine reply.

## Compare a before and after

A before and after inside a finding belongs here: it is evidence for one problem and
its proposed fix. Label each side as captured, proposed or text only. When both sides
are rendered (two branches, a preview against the live page, or one page before and
after a fix), capture them as a matched pair: same route, viewport, scroll position,
interaction state and loading readiness, with each caption naming its source (commit
or URL) and capture time. Visual Version Review's capture contract covers this when it
is installed. If the reader must instead choose among several implemented versions, or
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
