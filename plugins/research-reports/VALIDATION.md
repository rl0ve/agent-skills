# Validation

Release 1.0.2, checked 2026-10-21.

Instruction-only patch covering strategy/source scope, actual data-access coverage,
populated persona fields and joins, final prose review, purposeful HTML controls and
readable rendered/print text. No renderer, template or feedback runtime changed.

- Both Skill Creator validators passed; 49 repository tests, 109 Natural Writing
  tests, 45 UI Walkthrough Video tests and the assessment Node suite passed.
- Marketplace and both changed plugin manifests passed Claude Code validation;
  whitespace and local reference targets checked.
- Author policy review: a broad strategy brief with one product example, sparse CRM
  roles and a saved dashboard must retain scope, missingness and access limits, keep
  short evidence visible and review final prose. An explicitly requested interactive
  cohort explorer may still use controls; an explicit dual-format request remains
  valid. A single-heading correction does not trigger a new investigation.

These are package checks and an author review of instruction behavior, not a new
independent model trial or rendered-report benchmark. Prior independent exercises
retain their recorded scope. No private source captures or research facts were added.

Release 1.0.1, checked 2026-10-21.

Instruction-only follow-up: add a visual completion gate and a short decision record
that must be reconciled with the delivered artifact. This covers a visual chosen
during planning but lost during writing/export, and an invited motion overview whose
learning-value decision otherwise goes unrecorded. It does not impose a visual quota.
Rechecked both skill validators, all 49 repository tests, changed plugin/marketplace
validation and whitespace checks. The 1.0.0 independent behavioral exercises below
remain relevant; no new end-to-end renderer or model trial is claimed for this patch.

Release 1.0.0, checked 2026-10-21.

## Package checks

- Skill Creator validation passed for Research Reports and the updated Clear
  Assessment Guides entry point.
- Repository tests: 49 passed, including installer coverage, both marketplaces,
  three-manifest identity/description/version parity and discovery-description budgets.
- Natural Writing tests: 109 passed. UI Walkthrough Video tests: 45 passed.
- Existing assessment Node tests passed. Marketplace and all nine plugin manifests
  passed Claude Code validation.
- Both Research Reports local reference targets and the fourteen assessment reference
  targets resolve. Source diff has no whitespace errors.

## Independent forward test

An independent GPT-6.1 Sol advisor read the new skill and its references, then applied
them to three synthetic user requests. It received raw source excerpts and user
constraints rather than the expected decisions.

| Request | Observed output |
|---|---|
| Substantial PDF meeting research with mixed evidence, invited visuals and optional motion | Wrote an evidence-qualified opening, extended an existing leadership direction rather than manufacturing disagreement, chose one dependency diagram and a compact measurement table, avoided an unsupported funnel, kept one PDF and deferred motion without a demonstrated learning gain. |
| Correct one heading in an existing DOCX | Kept the edit scoped, returned DOCX only and did not invoke the research workflow. |
| Explicitly request DOCX, matching PDF and a short sequential overview | Honored all requested outputs, kept claims consistent, included a static alternative and planned checks of the actual document/video exports. |

The advisor found no instruction conflict. These are behavioral exercises of routing,
short research prose and delivery planning, not a full end-to-end investigation or a
comparative benchmark. No report, diagram or video renderer was exercised by this
plugin release; each real artifact still requires its own source and rendered checks.

The package contains generic methods and synthetic validation summaries only, with no
customer data, internal source links, private captures or account details.
