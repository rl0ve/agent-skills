# Meng To repository review

Reviewed 2026-09-06. This is a source and policy review, not a live accessibility,
performance or comparative design trial. Selected files were read; the repositories
were not exhaustively audited. No source code or external skill was copied or installed.

## Sources inspected

Links pin the revisions reviewed so later upstream changes do not alter the evidence.

- **Skills**, revision `321c769`, 2026-08-28:
  [design-first prompting](https://github.com/MengTo/Skills/blob/321c769739b823de5eb94eb3a52aa1974fe783a2/agent-skills/ui/design-first-ui-prompting/SKILL.md),
  [design coherence](https://github.com/MengTo/Skills/blob/321c769739b823de5eb94eb3a52aa1974fe783a2/agent-skills/ui/no-ai-design-slop/SKILL.md),
  [expressive websites](https://github.com/MengTo/Skills/blob/321c769739b823de5eb94eb3a52aa1974fe783a2/agent-skills/web-design/build-awwwards-quality-sites/SKILL.md),
  [animation optimization](https://github.com/MengTo/Skills/blob/321c769739b823de5eb94eb3a52aa1974fe783a2/agent-skills/codex/optimize-web-animations/SKILL.md),
  [full-page capture](https://github.com/MengTo/Skills/blob/321c769739b823de5eb94eb3a52aa1974fe783a2/agent-skills/codex/stitched-full-page-capture/SKILL.md), and
  [reference originality](https://github.com/MengTo/Skills/blob/321c769739b823de5eb94eb3a52aa1974fe783a2/agent-skills/codex/audit-reference-originality/SKILL.md).
  The inspected repository license is MIT; its policy preferences are not universal requirements.
- **threeui**, revision `68802d5`, 2026-09-01:
  [discrete preview controls](https://github.com/MengTo/threeui/blob/68802d5428071ada5c20db8094b1649e6bb770ed/src/components/CheckpointSliderControl.tsx),
  [preview FPS meter](https://github.com/MengTo/threeui/blob/68802d5428071ada5c20db8094b1649e6bb770ed/src/components/PreviewFpsMeter.tsx), and
  [condensation renderer](https://github.com/MengTo/threeui/blob/68802d5428071ada5c20db8094b1649e6bb770ed/src/shaders/condensation/condensationRenderer.ts).
  These show bounded controls, visibility-aware sampling, pixel-ratio and delta caps,
  cached drawing resources and disposal. They do not establish runtime performance.
  The README distinguishes MIT code from separately governed media and fonts.
- **kage**, revision `4399487`, 2026-08-09:
  [page implementation](https://github.com/MengTo/kage/blob/4399487d2fb42bce39c7b032fbbb50d230bf4f0b/index.html)
  includes graphics quality controls, semantic split text and reduced-motion paths.
  The [commit record](https://github.com/MengTo/kage/commit/4399487d2fb42bce39c7b032fbbb50d230bf4f0b)
  describes responsive checks; those are upstream reports, not tests repeated here.
  Its README explicitly withholds a license for original code and artwork: study the
  methods, do not treat the implementation or art as reusable assets.
- **sketchbook**, revision `c1e4778`, 2026-08-06:
  [page implementation](https://github.com/MengTo/sketchbook/blob/c1e477814c4c9e204452ebf9b298aa13629cbfc2/index.html)
  separates the loupe from the transformed book, uses coarse-pointer alternatives and
  allows vertical touch scrolling. This is evidence for conditional interaction and
  coordinate-space choices, not proof of complete keyboard accessibility.

## Decisions

| Practice | Decision and scope | Existing owner |
|---|---|---|
| Concrete composition, type, spacing, imagery and motion choices before polish | Adopt for substantial visual work; infer from the brief and established system without a user questionnaire | Design steering |
| Refine a few variables while preserving accepted decisions | Adopt for diagnosis; optional temporary controls for material or motion studies | Design steering |
| Coherent section rhythm, hierarchy before wrappers, element removal test | Adopt without requiring minimalism or suppressing purposeful expression | Art direction |
| Inspect the requested surface beyond the hero | Adopt; keep narrow edits narrow | Quality gates |
| Usable initial content, semantic text and equivalent touch/keyboard actions | Strengthen for substantial custom motion and spatial work | Motion quality, linked by quality gates |
| Single property ownership, visibility suspension, cleanup and measured quality budgets | Conditional on custom motion/graphics or a performance defect; no prescribed stack or numeric defaults | Motion quality |
| Separate coordinate spaces for transformed scenes and tools | Conditional on alignment-sensitive overlays; not a default app architecture | Motion quality |
| Warm-scroll and stitch only when ordinary capture misses content | Conditional on full-page evidence requirements and observed capture failure | Visual resources |
| Check for unrelated source copy, branding, claims and hidden labels | Conditional on reference adaptation; preserve intended attribution and fidelity | Visual resources |
| User references first, bounded slice, chosen expression, source/license checks | Already covered; retain rather than duplicate a broad skill | Existing steering and resource method |
| Mandatory GSAP/Lenis, fixed icon/font choices, blanket technique bans | Reject as universal policy; specific projects may choose them | User intent and one selected lead |
| Bulk skill installs, exhaustive originality audit, history rewrites, single-file app architecture | Not adopted; not warranted by this review | Existing scope and permission rules |

## Applicability review

These are manual policy walkthroughs, not executions by a fresh agent or automated
behavioral evaluations. The updated references were checked against each case.

| Case | Expected behavior | Review result |
|---|---|---|
| New expressive portfolio with a clear reference | Make concrete choices, build a slice, retain personality and check lower sections | Covered; no forced aesthetic or extra approval round |
| Accepted dashboard needs an eight-pixel spacing correction | Make the correction and inspect the affected layout | Covered; no research, preview controls or graphics profiling |
| Feedback says the material is too shiny | Compare a bounded material change against the accepted baseline | Covered; unrelated layout, palette and content stay settled |
| Drag-driven book has essential page navigation | Provide usable keyboard/touch paths and verify vertical scrolling | Covered; no claim that a desktop hover demo proves touch access |
| WebGL background slows down after route revisits | Compare equivalent before/after states, inspect lifecycle and repeated entries | Covered; build/screenshot/FPS counter alone cannot certify performance |
| User requests a lush, ornamented treatment | Preserve expressive ornament when it contributes to the chosen character | Covered; removal test does not impose minimalism |
| Full-page capture omits a lazy-loaded lower section | Inspect and warm-scroll; stitch only if needed and check artifacts | Covered; no mandatory stitching for every task |
| Reference-inspired page contains the source company's hidden label | Correct the unrelated label while preserving intended attribution | Covered; shared layout conventions are not treated as infringement |

Revisit if observed builds still drift from accepted decisions, motion checks impose
unnecessary work on simple tasks, or the selected specialist already provides equivalent
evidence more economically. Future upstream releases require their own scope and license
review before code adoption.
