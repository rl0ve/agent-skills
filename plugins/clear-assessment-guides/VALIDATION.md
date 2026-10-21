# Validation

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
