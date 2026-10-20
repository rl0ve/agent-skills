# Validation

Release 1.0.0, checked 2026-10-20.

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
