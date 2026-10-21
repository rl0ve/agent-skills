# Quality checks by mode

Apply the common checks and only the selected mode's checks. Do not require a document
outline, GIF or interactive board when the user asked for a simple correction.

## Common

- Is the current experience and the user's task understandable, including what works?
- Are the issue, relevant impact and proposed change concrete and evidence-bounded?
- Are observations, inferred effects, proposals, others' work and unknowns distinguishable?
- Are source links exact, relevant and checked where accessible? Are access gaps explicit?
- Are actual screenshot pixels preserved, with useful orientation, readable annotations,
  a visible border and nearby caption? Are mockups unmistakably proposed?
- Does the content preserve the requested audience, style and scope rather than impose
  a vendor's terminology, brand or operational assumptions?
- Is review feedback distinct from execution, save and live verification? Are the
  user's editor/saver choices and existing work preserved?
- Has the actual final output been inspected for clipping, readability, broken links,
  detached evidence and misleading status? Report what could not be verified.
- Before anything is reported missing or broken, were its route, alternate modes and
  loading state checked?
- If delivered as one standalone file, are images embedded and does it open with
  networking off? If hosted, was the returned URL opened? Local success is not proof
  that hosting worked.

## Supporting tools

- For a substantial assessment, were the central findings reviewed for the few visual
  explanations that would reduce interpretation work? Are selected visuals present
  and checked in the delivered artifact, rather than promised for later? If a complex
  relationship, handoff or sequence remains prose-only, is the reason concrete?
- If motion was invited, was it included or omitted for a stated learning-value reason,
  with a static alternative when included?
- Was each collaborator selected for a concrete task and verified available, without
  installing optional dependencies or changing the requested mode by default?
- Were relationships distinguished from simple text changes, and useful HTML from
  unnecessary animation or elaborate layouts?
- Can an unfamiliar reader understand the artifact? Is a self-review honestly
  distinguished from an independent fresh-reader test?
- Were document/PDF rendering checks used for actual final exports, with imagery
  and motion included only when they materially help?

## Document

- Is there one primary document format, with both DOCX and PDF produced only if requested?
- Does the opening establish the current state and purpose for an unfamiliar reader?
- Are assessment findings prioritized, with substantive Problem/Impact/Proposed solution
  lines? Does a guide instead use actions and visible success checks?
- Is the main read appropriately concise without tiny type or missing context?
- Can each recommendation be understood without navigation or expanding hidden detail?
- Have all rendered pages and requested editable/exported versions been inspected,
  including hyperlinks, tables, borders and page breaks?

## Guided review

- Is exactly one issue shown, using current relevant evidence and an exact proposed change?
- Is the copy/original choice explained and the editor/saver role clear?
- Does a GIF add necessary interaction evidence, with a static/text alternative?
- Does the conversation pause for feedback before advancing or making an undelegated edit?
- After an edit, does the verification distinguish previewed, saved and live states?

## Interactive HTML

- Do overview, issue navigation, decisions and comments work by keyboard and at narrow widths?
- Are the explanation and evidence visible for the selected issue without nested disclosure?
- Do before/after and execution labels distinguish actual captures from proposed changes?
- When both sides of a before/after are rendered, do they match route, viewport and
  state, and does each caption name its source and capture time?
- Are review choices stored separately from execution state, with no live action behind them?
- Do export/import round-trip decisions and multiline comments? Do invalid, wrong-revision
  and duplicate-ID imports fail without overwriting current work?
- Are local-storage availability, pending export and import results communicated accurately?
- Is feedback retained safely on refresh when storage works, with explicit export as
  the durable copy and a warning before replacing unexported edits?
- Have the rendered desktop, narrow and print views been inspected and actual controls tested?
