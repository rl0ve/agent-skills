# Validation

Release: 1.1.0, October 20, 2026 (US Eastern). Adds the feedback contract; a
repository test parses its example and checks the choice values. Instructions only: no
comparison page was regenerated for this release.

Release: 1.0.0, October 20, 2026 (US Eastern).

## Checks performed

- Repository package, routing and parity suite: 46 tests passed, including seven new
  Visual Version Review structural checks.
- Natural Writing suite: 109 tests passed.
- UI Walkthrough Video suite: 45 tests passed.
- Existing Node review-state tests: passed.
- Claude marketplace and all eight plugin manifests: passed `claude plugin validate`.
- New README, skill hub and both references: no configured high-signal patterns from
  the repository's Natural Writing linter after review.
- Frontmatter, bounded description and bundled-reference paths were checked. The
  dedicated `agentskills` validator was unavailable in this environment.

## Scope of evidence

The workflow was developed during an actual comparison of implemented UI versions.
The consuming project's single-file HTML review passed 23 local checks, including
offline media loading, filters, version selection, enlargement, keyboard navigation
and viewport fit. Its project-specific captures and QA records remain in that project.

Those checks do not constitute a fresh-agent skill execution, a comparative usability
benchmark or proof of a hosted deployment. This release adds reusable instructions
and discovery metadata; it does not ship a general-purpose gallery renderer.

Publishing this plugin in the canonical repository does not install or load it in
the user's local Codex or Claude sessions, nor in a separate hosted skill library.
