# Changelog

## 1.3.0 — 2026-10-20

- Adopt Visual Version Review's capture rules for before/after pairs: five evidence kinds, loading readiness, full viewport when prominence matters, content-mismatch disclosure and original dates for historical images.
- Review template: optional evidence `side`, `kind`, `source` and `capturedAt`; one before and one after shown side by side with aligned images; proposed images marked as not observed; image fit/original-size toggle.
- Absence check before reporting something missing; offline and hosted delivery checks.
- Tests: evidence provenance validation in the Node suite; repository test keeps template kinds and documentation in sync.

## 1.2.0 — 2026-10-20

- Add a before-and-after section: a before/after inside a finding stays here; rendered pairs are captured as matched pairs with source and capture time; choosing among implemented versions goes to Visual Version Review.
- Description names the before/after case and the handoff; quality checklist adds the matched-pair check.

## 1.1.1 — 2026-10-20

- Supporting tools: add Archify as an alternative for interactive codebase, plan and
  architecture diagrams delivered as self-contained HTML, with its update check disabled
  for confidential work.

## 1.1.0 — 2026-10-20

- Add optional collaborator routing for Diagram Design, Visual Explainer, doc-coauthoring
  and document/PDF workflows, with simple fallbacks and explicit availability checks.
- Keep imagery and motion conditional, distinguish author self-review from independent
  fresh-reader testing, and preserve the three existing review modes.

## 1.0.0 — 2026-10-20

- Add one product-neutral skill with document, guided triage and interactive review modes.
- Include source-backed assessment/guide templates, evidence and edit-location guidance.
- Add a local HTML review template with separate review/execution states and validated
  JSON feedback export/import; no live-system actions or required services.
