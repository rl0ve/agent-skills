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

## Assign authoring and runtime responsibilities

For a Three.js web experience, prefer a hybrid pipeline when it fits the existing
stack. Choose per asset and behavior from fidelity at task distance, editability,
reuse, export support and measured delivery cost; no tool is the universal winner.
Record a short owner/format/runtime-contract map before substantial asset work.

| Work | Useful owner and boundary |
| --- | --- |
| Distinctive architecture, terrain, steps, close-up props or characters | Blender or another compatible authoring tool for intentional silhouette, detail, UVs, collision/source geometry and reusable assets. Do not remodel a sound asset to repair a runtime camera or shader defect. |
| Rigging, authored animation clips, static texture/AO/light baking | Author offline where useful; runtime code owns playback, blending, state changes and any dynamic lighting those bakes cannot represent. |
| Scene assembly, camera/framing, input, legal actions and feedback | Three.js and the application's authoritative state. An exported scene does not supply gameplay or learning semantics. |
| Responsive water, wind, particles, material/light changes and simple repeated forms | Consider bounded runtime shaders or procedural geometry. Reuse/instance appropriate authored geometry rather than regenerate each copy. Measure the chosen effect on target conditions. |

Do not make Blender generate the whole experience by default, or replace distinctive
art with crude code primitives merely because they are easy to generate. A licensed,
authored or procedural asset earns its place through the representative task and
requested craft. Reuse audited assets first when they fit; new generation/downloads
still need the applicable authorization and provenance. Three.js recommends
[glTF/GLB for runtime assets](https://threejs.org/manual/pages/loading-3d-models.html);
[instancing](https://threejs.org/docs/pages/InstancedMesh.html) can reduce draw calls
for repeated geometry/materials, but does not by itself establish a performance pass.

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

### Verify the asset boundary before remodeling

For unexpected white/missing colors, flat lighting, lost texture detail or wrong
scale, locate the first failing boundary: source/master, exported asset, optional
compression/optimization, or destination loader/material/render setup. Compare the
actual files used; a good authoring preview is not proof of a faithful shipped asset.
Record source/exporter versions, relevant export options and source/delivered hashes.

Use deterministic representative checks for required material/mesh IDs, color or
custom attributes, UVs, texture references, transforms and state variants as relevant.
An attribute's presence, an object count or an export exit code does not prove its
values survived. When feasible, inspect a minimal uncompressed export to isolate a
loss before changing geometry, rebaking everything or blaming the runtime. Preserve
the working master and failure evidence; diagnostic markers/copies are not shipping
art. Do not generalize a version-specific exporter workaround into a universal rule.

Verify the resulting delivered asset in the real runtime, in each affected state
(for example Day/Night), with the real action and UI. Capture after camera/layout
transitions settle and record current/selected/task-target presence as well as
containment: filtering off-screen targets can make a bounds check pass vacuously.
Keep real landmark coordinates honest; if a target is absent, report the framing
gap rather than declare success from the remaining labels. Fix it in its owning
layer and recheck dependent states and performance before expanding the asset set.

Keep artifact correctness, rendered craft, non-3D UI/UX and device performance
verdicts separate. A passing build/test or repaired export does not erase a rejected
visual score; rerender and use the selected specialist's actual critique/refinement
and stall policy. Honor explicit full Dream Loop requirements rather than substitute
a lighter loop silently. Unknown human/device/accessibility gates remain unknown.

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

## Generated worlds and semantic assets

A navigable reconstruction or Gaussian splat is a visual representation; inspect what
its export actually provides. For example, [World Labs' API](https://docs.worldlabs.ai/api)
distinguishes splats, collider meshes and other mesh exports. A collider can support
movement without providing separate manipulable objects, action anchors or task rules.
Do not assume these are absent from every generator; verify and add the missing layer.
Keep the visual environment separate from the semantic objects and authoritative state
needed for the requested activity. For learning assets, retain relevant referent,
localized labels and lesson tags alongside stable IDs when replacing the art.

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
