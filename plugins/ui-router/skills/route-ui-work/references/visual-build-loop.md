# UI Router adaptation: visual targets and working interactions

This is UI Router's lighter method, informed by Dream Loop but not equivalent to its
full workflow. Choose the route using [upstream-skills.md](upstream-skills.md) first.
Use this adaptation when proportionate, explicitly chosen, or as a stated fallback;
do not layer its pass limits or parent-only option over a selected upstream procedure.
It applies to substantial graphical work needing refinement under the design lead.
Small edits, settled components and ordinary forms stay on their existing route.

## Choose the evidence before building

Write down the intended user action and the visible result, then choose a representative
slice that exercises both. For example: select a material and see the object change;
move a character and see the camera follow; edit a canvas and reopen its exported file.
A decorative scene only needs the interactions actually requested. Do not invent a
backend, game mechanics or a persistence requirement for a visual demo.

Use an existing reference or accepted design first. When direction is unresolved and
image generation would clarify it, create a labeled proposed target using the host's
supported image tool within the user's authorization. For an existing product, supply
a current capture and the requested changes so useful content and constraints survive.
A generated target is a design proposal, not proof of a running application. Keep real
copy, semantic controls and layout in the implementation; do not flatten a working UI
into an image to make a screenshot match. If image generation is unavailable or outside
scope, continue from supplied references, a sketch or a working slice where possible.

Separate fixed requirements from exploratory traits. An inspirational image need not
match pixel for pixel; a fidelity specification requires explaining deviations. A still
image cannot specify drag behavior, camera movement or timing: record those separately
from live examples, recordings or the user's requirements. Store only the selected
reference, current capture and useful decisions in project-local notes.

## Build, inspect and revise

1. Build a runnable slice in the destination stack with realistic content and the main
   interaction. Start with composition, hierarchy and input behavior before fine detail.
2. Capture the actual running result at a comparable viewport and application state.
   Compare framing, type, color, content and, when relevant, lighting and materials.
3. Exercise the promised interaction from its initial state through its result. Check
   recovery, interruption or reversal where relevant, plus keyboard/touch alternatives.
   A control that animates without changing the intended state is not a working feature.
4. Identify the few discrepancies that most affect the brief. Make bounded corrections,
   preserve accepted behavior, then repeat the capture and the affected interaction.
   Retain a known-good checkpoint before a substantial change.

A fresh read-only critic can help on consequential visual judgments when delegation is
allowed and repays the handoff. Give it the brief, target, actual capture and relevant
behavior evidence; request concrete discrepancies, not an unexplained taste score.
Work Router owns model/effort selection and the one-writer rule. Without a critic,
perform an explicit comparison in the parent and say so; independent review is not a
prerequisite. Do not infer models, parallelism or budgets from an account's subscription.

## Keep the iteration bounded

Honor the user's deadline and budget, including asset generation. For ordinary scoped
work without a stated limit, plan a first implementation and up to two focused refinement
passes, then assess the evidence. This is a refinement budget, not permission to stop
with fixable required functionality broken. Longer autonomous work follows the user's
scope and Work Router's long-running guidance.

If the same important discrepancy survives two passes, diagnose the cause before more
polish: camera/composition, unsuitable asset, conflicting styles, wrong rendering path
or an impossible target. Change the approach only within scope. Do not endlessly
regenerate targets, lower the requested quality silently, or replace the brief with an
easier image. Stop refinement when the selected traits and relevant checks pass; at a
real limit, preserve the best result and report the specific remaining gap.

## Assets and runtime

Choose existing licensed assets, entitled component source, procedural geometry,
Blender modeling or generated assets according to the target and destination. There
is no universal requirement for Blender or a paid image-to-3D service. A configured
API key does not authorize spending, and an asset restriction also applies to external
generation unless the user says otherwise. Check executable/tool availability separately
from installed workflow instructions. Use the host's credential mechanism; do not
import another skill's secret-search or environment-dump instructions.

Inspect imported models for scale, orientation, bounds, texture/material support and
asset paths in the running scene. Measure performance in the target browser/device
conditions; report those conditions rather than claiming a universal frame rate.
Apply [motion-quality.md](motion-quality.md) for lifecycle, input and graphics fallback.

## Completion evidence

Apply [quality-gates.md](quality-gates.md). Report appearance and behavior separately:
what was visually compared, which action reached which observed result, and any limits.
For an editor/exporter, open the actual export. For a data-backed app, distinguish mocked
states from verified reads/writes. A simulated demo is valid when requested and labeled.
A screenshot, subjective score or successful build alone cannot establish these outcomes.

Method informed by [Dream Loop](https://github.com/achimala/dream-loop), reviewed
2026-09-19. See the [decision record](../../../docs/interactive-workflows-review-2026-09-19.md)
for the pinned source, adopted ideas and deliberate differences. The upstream package
is not installed or required by this reference.
