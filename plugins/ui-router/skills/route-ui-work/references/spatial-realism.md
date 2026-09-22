# Realistic scenes that survive interaction

Use for a substantial realism pass in an explorable world, close-up configurator or
spatial learning experience. This supplements the selected 3D specialist; it is not
a new aesthetic lead. Skip it for ordinary UI edits, decorative stills and an already
accepted scene whose unrelated copy is changing.

## Diagnose the limiting layer

Compare one representative view and action against the requested target. Identify
whether the visible gap comes from construction and silhouette, surface detail,
lighting/reflections, composition, or delivery limits. Higher texture resolution or
render scale cannot repair every layer. If the whole environment lacks coherence,
compare a coherent authored or licensed scene with the current approach before
spending another phase on scattered props. Keep the real interaction in that comparison.

Judge the slice at the actual viewing distance with its interface visible. A detailed
object behind a text panel is not a usable referent. Check the active target and its
relation to nearby objects in the settled camera view, including narrow layouts.
Change composition or a scoped placement when needed; preserve semantics and reset
scene-specific offsets when leaving the activity. Do not hide required text to win
a screenshot comparison.

## Select and integrate assets

Choose licensed/scanned assets, authored modeling, procedural geometry or generation
for a concrete missing capability. Keep semantic object IDs, hit targets, collision,
placement anchors and animation pivots separate from the replaceable art where useful.
A generated or imported fused mesh may need separation before a lid, door or carried
object can work. Retain a source/master and a small provenance record for selected
assets; reject unsuitable candidates without importing their whole dependency tree.

For replacement art, validate scale, bounds, maps and required parts before retiring
the working fallback. Handle failed or late loads without duplicate art, lost hit
targets or leaked resources. When geometry controls placement, test the longest relevant
arrangement, not just one object: successive objects placed beside earlier objects
must all remain supported. A container's outside bounds do not prove its interior fits.
Check facing direction and visibility as well as intersection: paper can be inside a
bag yet need part of its label above the rim to communicate the action.

### Conditional generated-asset route: Hyper3D / Rodin

[Hyper3D MCP](https://hyper3d.ai/features/mcp) provides generation, progress and results;
its [Rodin API documentation](https://docs.hyper3d.ai/en/api-specification/rodin-gen2-5)
describes text/image inputs and supported model outputs. Inspect the live connector
schema: an API option is not necessarily exposed through MCP. Prefer an already
connected, authorized tool; availability alone establishes neither credits nor quality.

Choose one representative asset and a format/polycount appropriate to the destination
before expanding. Follow current credit, upload, result-link and download restrictions
within the user's existing authorization; do not require a second approval when the
specific use is already covered. Do not infer an asset budget from an audio budget.
Record a returned generation ID and poll that job. A wait timeout is not failure;
an ambiguous submission is not permission to submit a duplicate paid job. Follow the
connector's recovery instructions if submission returns no usable ID. Keep temporary
signed file URLs out of public notes and use its permitted permanent result link.

A generated model still needs the integration checks above and the scene's own lighting.
This route is optional, has no claimed quality advantage here, and does not replace
architecture, rendering or headset validation. Connection discovery is not a generation
trial; generation completion is not destination acceptance.

## Treat baked lighting as a derived artifact

When a scene uses baked light, occlusion or reflection captures, retain the source
revision/hash and describe the geometry, materials, lights and states actually included.
An export may contain fixed meshes while excluding semantic movable objects; inspect
its contents before claiming a whole-scene match. After a relevant change, rebake the
affected dependencies or record why the existing result remains adequate and what it
cannot represent. Do not rebake unrelated regions merely to produce a fresh artifact.

Keep direct light, diffuse bounce, contact shadow and reflected light conceptually
separate when diagnosing a discrepancy. Static captures do not automatically track
moved props, switched lamps or closed doors. Inspect a relevant changed state for leaks,
double-darkening, stale reflections and false contact. Name the approximation instead
of describing a static solution as fully dynamic.

## Compare runtime evidence fairly

Use the same device, viewport, render scale, graphics mode, camera path and settled
scene state for a performance comparison. Avoid competing live preview renderers when
measuring one scene. Report loading/shader warm-up separately from steady-state walking
or manipulation; include frame-time variation rather than only a short average FPS.
Distinguish compressed transfer bytes, decoded geometry/textures and estimated GPU
allocation. A successful desktop pass is not a mobile or stereo-headset result.

Apply [interaction-contracts.md](interaction-contracts.md) for task/evidence semantics
and [motion-quality.md](motion-quality.md) for input, media and lifecycle. Capture the
final changed view and exercise its affected action after the last material edit.
Review record and conditional cases: [September 22 spatial review](../../../docs/spatial-workflow-review-2026-09-22.md).
