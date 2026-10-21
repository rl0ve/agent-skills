# Interactive review

Use when comments, alternatives or decisions across several findings materially help.
For one conversational issue or a static handoff, prefer the simpler mode. Adapt the
self-contained [review template](../assets/review-template.html) to the project using
[the issue format](issue-format.md). It runs locally without a build step, service,
external JavaScript, paid package or particular browser.

Keep a short current-state overview and a navigable issue list. Show the selected
issue's Problem, Impact, Proposed solution and evidence together; navigation and
optional detail are allowed, but essential explanation must not require nested panels.
Include readable before/proposed-after, evidence links/captions and accurate execution
state. A print view should expose all issues and their current comments/decisions.

Review controls record feedback only. Use explicit choices: unreviewed, accept
proposal, revise, defer and reject. Avoid a button labeled Publish or Save to the live
product when the artifact has no such integration. Keep any future live-system action
separately authorized and implemented; do not embed it in this starter.

Make feedback persistence visible. The starter restores browser-local feedback by
assessment/revision and offers JSON export/import. That storage can be unavailable or
cleared, and is not cross-device sync. Export creates a durable transferable snapshot;
show pending export after subsequent edits. Confirm before an import would replace
unexported feedback. Validate the whole file before changing state, and surface errors
without losing the current choices. Downloading a file does not mean an agent received it.

Before delivery, exercise decisions, multiline comments, reload persistence,
export/import round-trip, wrong assessment/revision rejection, malformed imports,
keyboard navigation, the image size toggle, before/after pairing and mobile stacking. Inspect desktop and narrow renders, and the
print layout if a print/export view is delivered. Keep private findings and test
captures outside the shared package. The included examples are fictional help-center
content; replace them, not their proper nouns, with actual evidence-backed findings.
