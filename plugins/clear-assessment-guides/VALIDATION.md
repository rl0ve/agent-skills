# Validation

Release 1.5.1, checked 2026-10-23.

Display-name and cross-reference update only: Explain & Review replaces the prior
human-facing name, while the plugin ID, skill invocation, paths and behavior remain
unchanged. All 94 repository, 109 Natural Writing and 45 UI Walkthrough Video tests,
the Node assessment suite, marketplace and all nine plugin manifest validations,
and the system Skill Creator validator passed. No new behavioral or rendering
trial was needed for this metadata-only release.

Release 1.5.0, checked 2026-10-23.

Instruction-only addition of interface explanation, with routing handoffs from UI
Router 1.21.3 and UI Walkthrough Video 1.7.5. All 94 repository tests, 109 Natural
Writing tests, 45 UI Walkthrough Video tests and the assessment Node suite passed.
The marketplace and every plugin passed Claude manifest validation; the explanation
and capture skills passed the system Skill Creator validator. UI Router retains its
existing `compatibility` frontmatter field, which the generic system validator rejects
on both the unchanged baseline and this release; repository package checks pass.
All local Markdown reference targets in this skill resolve; whitespace checks pass.

Author-reviewed policy cases: several unfamiliar controls use a verified numbered
legend; an unknown icon stays unknown; a status badge is not described as an action;
an archive/delete action's consequences need separate evidence; a simple known icon
gets a direct definition; an interaction requiring motion uses the existing sequence
or capture route. These are instruction reviews, not independent model trials.
No screenshot, renderer, feedback schema or template/runtime changed. No private source
capture or project-specific icon behavior is included in the package.

Release 1.4.2, checked 2026-10-21.

Instruction-only patch clarifying final prose review, purposeful controls and rendered
reading/print typography. Both skill validators, 49 repository tests, 109 Natural
Writing tests, 45 UI Walkthrough Video tests, the assessment Node suite, marketplace
and changed plugin manifest validation passed. Whitespace and local references checked.

Author policy review: a static guide keeps short evidence visible and reviews actual
headings/captions/prose; an interactive issue board still supports comments and decisions.
A simple wording correction requires neither a diagram nor an interactive board.
This is instruction review, not a fresh model trial or rendered-template test. The
feedback template/runtime is unchanged; earlier evidence retains its original scope.

Release 1.4.1, checked 2026-10-21.

Instruction-only patch: the selected-mode quality checklist now explicitly checks
that chosen visuals are present and inspected, complex prose-only treatment has a
concrete reason, invited motion has a learning-value decision, and a second document
format was requested. Both skill validators, 49 repository tests, changed plugin and
marketplace validation and whitespace checks passed. No template or feedback runtime
changed; earlier rendered and behavioral evidence retains its original scope.

Release 1.4.0, checked 2026-10-21.

This release changes instructions and routing only. Research Reports now owns
open-ended synthesis; assessment document mode defaults to one requested document
format; visual selection and invited conceptual motion are explicit decisions.
Skill validation, 49 repository tests, existing assessment Node tests, all nine
plugin manifests and the marketplace passed. The other package suites passed
(109 Natural Writing tests; 45 UI Walkthrough Video tests). All fourteen local
assessment reference targets resolve. The HTML template and feedback code are
unchanged, so their prior rendered checks are retained rather than claimed as fresh.
Research Reports' validation record describes the independent format/visual/motion
forward tests; these are not a new rendering or full research benchmark.

Release 1.3.0, checked 2026-10-20.

The 1.3.0 change adds evidence provenance to the review template. Node tests cover a
valid before/after pair, the five evidence kinds and four invalid provenance records,
alongside the existing feedback cases. A test copy with a before/after pair and a
proposed image was rendered in headless Chromium at 1280 and 390 px wide and printed to
PDF: no script errors, pair images aligned, proposed image labeled as not observed, the
size toggle worked by keyboard with aria-pressed updated, the page did not overflow
horizontally, and the pair stacked on narrow screens. The browser file-picker import
was not exercised.

Release 1.1.0, checked 2026-10-20.

The 1.1.0 change adds instructions and collaborator routing only; the interactive
template and feedback code are unchanged. Rechecked skill validation, both manifests,
repository package parity, feedback tests, local reference targets and product-neutral
content. Routing reviewed against a relationship diagram, a simple label correction,
a substantial guide and a one-issue screenshot review: optional collaborators are
chosen by task, the three delivery modes remain available, and unavailable tools have
simpler fallbacks. No optional collaborator was installed or integration-tested.

The following template checks and limits were recorded for 1.0.0:

- Skill Creator quick_validate.py: valid skill.
- Claude plugin manifest validation: passed.
- Repository package tests: 14 passed, including paired manifests and marketplace parity.
- Local Markdown reference targets and both discovery entries: verified.
- Skill instructions, templates and references scanned for project/vendor details:
  no product names, internal links, account identifiers or private source artifacts.
- Node feedback tests: valid export/import round-trip with multiline and markup-like
  text; nine malformed/mismatched feedback cases rejected; duplicate assessment IDs
  and malformed evidence rejected; execution claims in imported feedback ignored.
- Chrome desktop: rendered and visually inspected; decision selection and multiline
  comment worked; export produced a download notification; reload restored the
  decision and comment while execution remained not started.

Limits: the downloaded file was not independently read back. Browser file-picker
import, narrow/mobile render, keyboard-only navigation and print preview were not
completed in this environment. A browser URL-policy block prevented further local-file
browser automation; no alternate route was used to bypass it. Import data validation
was tested as pure JavaScript; that is not an end-to-end file-picker test.

Behavioral review of instructions: document mode keeps evidence next to prioritized
findings; guided mode pauses after one issue and preserves the chosen editor/saver;
interactive choices record feedback without live execution. Ordinary chat and simple
rewrites are outside the skill's discovery scope. These are instruction reviews, not
independent model benchmarks. Each generated project artifact still needs its own
mode-specific verification.

Run package checks from the repository root:

```bash
python3 -m unittest discover -s tests -p test_packages.py
node plugins/clear-assessment-guides/tests/test-review-state.mjs
```
