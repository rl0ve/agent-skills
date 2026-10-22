# Formats and explanatory visuals

## Choose the reading package before exporting

Honor an explicit format and known preferences. Otherwise choose the smallest coherent
package for the task: PDF for a finished reading/reporting artifact, DOCX for substantive
editing, or an HTML explanation when interactive navigation/detail materially improves
understanding. Default to one primary document; produce both DOCX and PDF only when
requested. A construction tool's ability to export both is not a reason to do so.

A requested one-page meeting aid may accompany a substantial report. Give it the same
claims and IDs, and label its compression. An optional visual guide or short overview
needs a distinct reading/learning purpose, not another copy of the executive summary.
Keep exact source detail in the report or linked ledger so the reader need not infer
what a polished derivative is based on. A deck is appropriate for actual presentation,
not a compulsory extra format for research.

Use the user's established palette, medium and audience. Do not infer warm paper,
muted brown, a dark dashboard, decorative cards or any other aesthetic from the word
"editorial," a B2B topic or the use of AI. A confirmed style carries across derivatives;
a collaborator's shipped default does not override it. Retain legible text, sufficient
contrast and a coherent reading order at the actual output size.

HTML can earn its place through clear diagrams and a coherent reading layout without
requiring interactive controls. For independent reading, keep short evidence,
qualifiers and conclusions visible. Section links can aid navigation; an accordion
that only hides a short paragraph adds work. Use interaction when a reader benefits
from exploring alternatives, filtering data, inspecting substantial optional detail
or recording decisions. An explicitly requested interactive exploration remains valid.

Inspect body text, diagram labels, metadata and print styles at their actual reading
size. Do not shrink evidence or caveats to fit, or turn them into decorative microtext
above headings. Review automated design findings against the rendered artifact; fix
real problems and disclose any intentional exceptions rather than claiming an unchecked
or merely linted artifact has passed visual inspection.

## Select a few visuals by the explanation

For the central findings, make a small visual plan before implementation. Record the
question each candidate answers, its source/proposal status and why prose alone is
harder to interpret. Select the few that earn their place; neither zero nor a quota is
the goal. Keep essential interpretation, source and limitations adjacent to the visual.

Use a short project-local decision record for the central findings: reader question,
visual/table/text choice and reason, evidence/proposal status, selected collaborator
or fallback, and included/checked/pending state. Revisit it against the final artifact.
This catches the case where a visual was appropriate but disappeared during writing
or export; a visual plan alone is not completion evidence.

| Explanatory need | Useful visual | Important boundary |
|---|---|---|
| Who does what, and where work crosses teams | Swimlane or service blueprint | Distinguish proposed responsibilities from an agreed charter. |
| One changing fact affects several surfaces | Dependency map or structural before/after | Align unchanged elements; do not claim automation exists merely because it is drawn. |
| A process moves through readiness, failure and recovery | State/sequence diagram | Producer acknowledgement and accepted outcome can be different states. |
| Magnitude, concentration, recurrence or uncertainty | Appropriate chart/small multiples | Keep units, denominator, sample selection and period explicit. |
| Evidence for a visible interface problem | Actual screenshot with restrained annotations | Preserve pixels and source date; proposed UI is not observed evidence. |
| Tradeoffs consisting mainly of attributes | Compact table | Do not draw a network just to display a list. |

Resolve Diagram Design, Archify, data/plotting, Visual Explainer, document and other
specialists from the current host; read selected instructions and verify capability.
Use only collaborators needed for distinct jobs. Do not assume an installed name
means a working renderer, supported export or authenticated data connection. Simple
editable shapes or supported diagram notation can be a proportionate fallback.

Avoid a funnel or Sankey unless the data establishes compatible populations and the
transitions/flows being encoded. Cross-sectional stage counts and unlike units are
not observed conversions. Do not use arbitrary node size, arrows, color or timing to
imply measured impact, causal links or a quantitative ranking that the sources lack.

Keep a diagram's detail within a reader's working memory. Split overview/detail when
necessary; avoid shrinking labels to fit. Export only formats the task needs, retain
editable diagram source when practical, and inspect labels, connectors, captions and
page breaks after actual rendering. Card grids and colored typography do not satisfy
the need for a visual explanation.

## Choose a renderer for the selected surface

Use an existing report, notebook or dashboard workflow's native chart renderer when
that workflow owns the artifact. In particular, `data-analytics:visualize-data` owns
durable quantitative figures under its selected surface contract; `visualize:visualize`
supports exploration directly in chat. Read available collaborators' current
instructions. Neither is a mandatory dependency or a reason to change the requested
medium. Do not introduce React solely to draw a few standalone figures.

For standalone HTML outside an owning workflow, choose by the explanation:

| Need | Candidate | Selection reason |
|---|---|---|
| Statistical comparisons, distributions and small multiples | [Observable Plot](https://observablehq.com/plot/) | Concise layered marks and faceting for report figures. |
| Declarative specifications and linked interactive views | [Vega-Lite](https://vega.github.io/vega-lite/) | Reproducible JSON specifications with layers, facets and selections. |
| Rich exploration of dense or hierarchical data | [Apache ECharts](https://echarts.apache.org/en/feature.html) | Built-in zoom, brushing and a broad set of chart families. |
| Scientific/statistical exploration alongside Python analysis | [Plotly](https://github.com/plotly/plotly.js) | Reuse the analysis ecosystem when it already fits. |
| A bespoke explanatory graphic or unusual interaction | [D3](https://github.com/d3/d3) or authored SVG | Custom geometry and behavior when higher-level tools do not fit. |

These are optional candidates, not a load list or a comparative performance ranking.
Prefer one suitable renderer and verify its current API, runtime and needed export.
Preserve editable source and data; inspect the delivered HTML and requested static
export, including any view-dependent evidence. Keep essential conclusions and
qualifiers readable without hover or interaction. Bundle dependencies when offline
delivery is required and verify that delivered form.

Visual Explainer can own an HTML companion or selected mechanism explanation, but
its figure-led defaults must not compress away the report's reasoning, evidence or
uncertainty. Keep the agreed palette and medium; avoid a picture for every number.
Use available plugins rather than installing overlapping skills for the same job.

ImageGen or another available image tool may help with a conceptual illustration
when that image teaches something the exact figures do not. Label its illustrative
status. Keep quantitative charts, exact labels and structural relationships in
code-rendered or editable graphics; generated art is not observed evidence or an
actual interface capture. Image generation is optional, not a default report step.

## Gate a HyperFrames-style overview on learning value

A concise conceptual overview may be useful even when no real UI recording is needed.
Consider it when the user invites motion and an ordered mechanism, change propagation
or cause-and-effect explanation is easier to grasp over time. Prefer the chosen stills
or an illustrated reading guide when motion would mainly animate prose or add another
asset to maintain. Do not make video a default companion to every report.

Before a substantial render, identify the specific learning gain, intended length,
audience, static alternative and source-backed story. Use a short representative
sequence to settle unresolved direction before expanding. Existing authorization can
cover a local optional overview within the requested package; missing paid-service,
voice or external-publication authorization still needs resolution at that boundary.
Do not ask again merely because another skill repeats an approval step.

Use the available HyperFrames or authored-motion workflow for conceptual motion;
the selected motion-design lead owns composition, while the renderer owns execution.
Use UI Walkthrough Video when the job actually requires recorded product interaction.
A renderer name alone does not choose the storytelling method or establish runtime
readiness. Read the selected workflow before promising narration, duration or export.

Show meaning through transitions, continuity and attention, not merely paragraphs
appearing on successive slides. Keep the report's facts, provenance and distinctions
intact; time-based illustration is not observed telemetry. Supply a readable static
or text alternative, respect reduced-motion behavior where relevant, and check the
rendered opening, important transitions, captions/audio when present and final export.
Never describe an unrendered storyboard as a completed video.

## Continue and retire cleanly

Inventory supplied and generated assets before updating a research package. Identify
the canonical current report, meeting aid and necessary derivatives. Update or
explicitly supersede affected assets; leave original evidence available as historical
material without forcing the reader to open several old versions to reconstruct the
current answer. A dated addendum can preserve the old body, but clearly state which
claims/proposals it updates and which printed page/source IDs belong to the original.

Check a self-contained HTML artifact for dependencies and its actual destination before
claiming offline portability. Check links, exports and controls in delivered form.
Distinguish content review, mechanical checks, visual inspection and an independent
reader test; none substitutes for the others.
