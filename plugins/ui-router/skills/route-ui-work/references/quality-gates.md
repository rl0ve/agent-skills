# Completion gates

Apply every relevant gate before declaring the routed task complete.

## Scope

- Only requested surfaces and files changed.
- The chosen chain has one lead and no redundant layer.
- Any assumption that affected the design is reported.

## Visual and interaction quality

- Hierarchy remains clear when squinting or at 200% zoom.
- Text is legible, content does not overflow, and focus states are visible.
- Keyboard, touch, loading, empty, error, disabled, success, and reduced-motion states are covered when relevant.
- Responsive behavior adapts rather than hiding critical functionality.
- The palette and overall visual character match the chosen direction. A repeated
  house palette has a brief-based reason, rather than being the residue of generic
  anti-pattern exclusions or an unrelated parent page's theme.
- For expressive or reference-led work, check purpose and expression separately using
  [art-direction.md](art-direction.md). Exercise the promised dynamic interaction;
  correct behavior alone does not establish that the visual request was satisfied.
- Inspect the whole requested page or journey, including lower sections and the final
  action or state. A polished hero does not establish completion of the rest. Compare
  hierarchy, section rhythm and content quality across the surface; keep checks scoped
  to the actual request for a small edit.
- For substantial custom motion, scroll choreography, canvas or WebGL, apply
  [motion-quality.md](motion-quality.md). Ordinary static edits do not need profiling.

## Reference fidelity

- Apply exact visual matching only when fidelity is the specification. For inspiration,
  check the selected traits and the project's constraints rather than copying the whole source.
- Reference and render use the same viewport for comparison.
- Colors, typography, spacing, radius, shadows, copy, and imagery are compared.
- Every intentional deviation has a stated reason.

## Samples and adopted components

- When a consequential visual choice remained open, show a useful comparison or
  report why evidence could not be displayed. Do not require samples for small edits.
- Distinguish inspected source examples, proposed adaptations and working implementation.
- Preserve accepted content, density and unrelated design decisions during iterations.
- Check selected code's source, license, dependencies and framework compatibility.
  A catalog's popularity or polished demo does not establish accessibility or fitness.
- Inspect the adapted component with realistic content in its destination, including
  relevant long-text, empty, loading and error states. Verify behavior and responsive
  fit; a successful import or isolated demo is not completion evidence.

## Evidence

- When the writing route is selected, verify the Natural Writing skill is available. Package presence alone is not installation evidence.

- Run the narrowest relevant tests or browser checks.
- Report what was checked and what could not be checked.
- Distinguish observed results from recommendations or hypotheses.
- In a multi-phase build, completion evidence must match the required outcome: a
  screenshot demonstrates appearance, an exercised flow demonstrates behavior, and an
  inspected export demonstrates the deliverable. A source demo or checked task list
  does not substitute for those observations. Reopen accepted work only for a relevant
  regression, new requirement or observed defect.

## Writing and interface copy

- Supported facts, material qualifications, product terminology, identifiers, labels, states, links, and formatting are preserved.
- UX, product, or marketing constraints are settled before the final prose pass.
- One context-holding editor owns the finished copy; any second agent is read-only and returns findings.
- A representative author sample outranks generic style preferences.
- The edit makes the minimum effective change and leaves strong sentences alone.
- No unsupported claim, invented objection, ritual validation, prompt echo, coaching theater, taxonomy reflex, fake contrast, excessive heading, or generic ending remains.
- Natural Writing does not redesign product behavior, legal meaning, or information architecture unless the user requested that broader change.
