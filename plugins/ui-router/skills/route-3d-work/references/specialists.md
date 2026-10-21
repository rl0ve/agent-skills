# 3D specialists, knowledge layers and tools

Load only what the current task needs. The project's own direction and pipeline lead
when they exist; entries here are layers or tools under that lead.

## Knowledge layers

| Need | Source | How to use |
| --- | --- | --- |
| Core three.js API for the pinned version | [three.js llms.txt](https://threejs.org/docs/llms.txt) / [llms-full.txt](https://threejs.org/docs/llms-full.txt) | Read the sections in use. The docs track the latest release; check the project's pinned `three` version before applying new APIs. |
| Blender to glTF/KTX2/Draco export and optimization | `blender-web-pipeline` (claudedesignskills) | Layer for export settings, compression and batch scripts. |
| Vanilla three.js scene structure | `threejs-webgl` (claudedesignskills) | Basics only; the project's existing renderer and loaders win. |
| Close-up wood, stone, fabric and foliage materials | Meng `3d-high-resolution-textures`, `3d-high-poly-models` | Layer for a named surface or prop; follow the asset plan in [spatial-realism.md](spatial-realism.md). |
| Water, fountains, open sky | Meng `3d-ultra-realistic-water`, `3d-sky-background` | Load when the scene contains that element. |
| Frame time, draw calls, memory, load cost | Meng `optimize-threejs-games` | Load when a measured budget fails. |
| Sourced Blender-to-three.js, IBL, baking and XR recipes | [3dviz-pro-max](https://github.com/viettranx/3dviz-pro-max) (MIT, targets three 0.180) | **Retrieval only.** Clone outside skill folders and query from the clone root with `python3 skills/3dviz-pro-max/scripts/search.py "<question>"` (add `--kind` or `--collection` to narrow; `resolve.py <id>` prints a record). Do not install it as a skill: its description would trigger on every 3D edit and its kit defaults conflict with an established pipeline. |
| Technical-art and debugging checklists | [threejs-game-skills](https://github.com/majidmanzarpour/threejs-game-skills) `technical-art.md`, `debug-playbook.md` | **Read those two files only.** Do not install or run its director or asset generators: its credential probe reads shell profiles and starts paid generation when keys exist, which this router forbids. |
| Gaussian-splat captured spaces | three.js [`GaussianSplat`](https://threejs.org/docs/pages/GaussianSplat.html) (r186+), or [Spark](https://sparkjs.dev/docs/overview/) | Only when a captured-space study is in scope; a study does not change the production stack. Use the built-in add-on for object- or room-scale captures in a `WebGPURenderer` project; it has no streaming or level of detail. Use Spark (WebGL2) for `WebGLRenderer` projects, mobile or WebXR. For streaming or level of detail, check the current support of whichever renderer you choose. Checked October 20, 2026. |

## Tools

| Tool | Use |
| --- | --- |
| Blender headless CLI (`blender --background --python ...`) | Source of truth for deterministic builds and bakes that must reproduce. |
| [Blender MCP](https://github.com/ahujasid/mcp-for-blender) (`mcp-for-blender`, pinned, safe mode) | Live inspection, measurement and small checked edits in an open scene. Keep paid generation integrations off unless the user authorizes them. Fold any accepted MCP edit back into the CLI build script. |
| Project capture and measurement harnesses | Screenshots, clips, frame time, draw calls, triangles, texture memory and transfer size from the running build. |
| [Needle Inspector](https://engine.needle.tools/docs/three/needle-devtools-for-threejs-chrome-extension.html) + MCP | Trial: live scene graph, material and draw-call inspection. Its agent tooling is young; keep it only if a trial on one scene saves time over the project's harnesses. |

## Excluded by default

Babylon.js, PlayCanvas, A-Frame, Spline, React Three Fiber, pmndrs/xr, Substance, PixiJS
and WebGPU/TSL-only packs (for example linegel/threejs-complete-set-of-skill) when the
project runs another runtime. Generator-first packs (Tripo, Hyper3D/Rodin) stay
conditional on explicit authorization. Load one of these only for a runtime decision
or an approved pilot.

### Playable-world design and feedback

Selected paths below were reviewed at MengTo/Skills revision
[`d5bd3a7e`](https://github.com/MengTo/Skills/tree/d5bd3a7e9c9f4b00853e84fffa60bc38eee9e744)
on October 1, 2026. Load only the complete specialist that fits the task.

| Need | Exact entrypoint and boundary |
| --- | --- |
| Objectives, consequential choices, pacing and recovery | [design-game-encounters](https://github.com/MengTo/Skills/blob/main/agent-skills/game-development/design-game-encounters/SKILL.md). It targets action combat; a learning-world adaptation preserves decisions and recovery without importing enemies, timers or combat pressure. |
| Legible space, landmarks and collision authoring | [author-game-levels](https://github.com/MengTo/Skills/blob/main/agent-skills/game-development/author-game-levels/SKILL.md). Its strict flat-plane convention belongs to its game workflow; do not impose it on an existing multi-level architectural or XR world. |
| Camera framing, occlusion, touch and reduced motion | [build-game-camera-controls](https://github.com/MengTo/Skills/blob/main/agent-skills/game-development/build-game-camera-controls/SKILL.md). Match the actual locomotion and input design. |
| Responsive sound and browser audio lifecycle | [build-game-audio-feedback](https://github.com/MengTo/Skills/blob/main/agent-skills/game-development/build-game-audio-feedback/SKILL.md). Preserve narration intelligibility, mute and visual equivalents; the voice-narration owner still owns generated speech. For music/effects authoring and mixing, use [the scene-audio checks](runtime-and-slice.md#author-sound-as-part-of-the-scene). |

Use the [playable-slice criteria](runtime-and-slice.md#design-a-reason-to-keep-playing)
for shared product decisions. A popular video is reference evidence, not a
playthrough, performance benchmark or proof of educational value.

### Photoreal interactive worlds and spatial scenes

The current Meng 3D bundle is under `agent-skills/3d/`. Select by the camera freedom
the experience actually needs, then load the complete selected `SKILL.md` and its
required references before implementation:

| Camera or output need | Exact upstream entrypoint | Route boundary |
|---|---|---|
| Close-up surfaces with physically coherent detail | [3d-high-resolution-textures](https://github.com/MengTo/Skills/blob/main/agent-skills/3d/3d-high-resolution-textures/SKILL.md) | Choose texel density and map resolution from projected coverage, PBR roles and delivery cost. Do not assign 4K or 8K to every map by default. |
| Hero assets whose silhouette and edges must hold up close | [3d-high-poly-models](https://github.com/MengTo/Skills/blob/main/agent-skills/3d/3d-high-poly-models/SKILL.md) | Spend geometry on visible silhouette, bevels and surface form, then prepare runtime LODs. Triangle count is not the target. |
| Guided tours, room navigation, orbit inspection or requested free walking | [3d-virtual-tour](https://github.com/MengTo/Skills/blob/main/agent-skills/3d/3d-virtual-tour/SKILL.md) | Orbit inspection is not free walking. Add first-person collision and walkable-surface checks only when free walking is requested or required. |
| Water, fountains and pools | [3d-ultra-realistic-water](https://github.com/MengTo/Skills/blob/main/agent-skills/3d/3d-ultra-realistic-water/SKILL.md) | Reflection, refraction and motion must read at the scene's camera distance within the frame budget. |
| Open sky, atmosphere and horizon | [3d-sky-background](https://github.com/MengTo/Skills/blob/main/agent-skills/3d/3d-sky-background/SKILL.md) | Match sky lighting to the scene's baked or runtime light so the two do not disagree. |
| Crisp WebGL output on HiDPI displays | [3d-retina-resolution](https://github.com/MengTo/Skills/blob/main/agent-skills/3d/3d-retina-resolution/SKILL.md) | Treat fixed 200% rendering as a display-quality choice with a measured fallback; it does not make coarse geometry or low-resolution textures realistic. |

For a composed image or 2.5D image-layer presentation, use the project's image,
canvas or camera-composition workflow. A realistic screenshot or clip is appearance
evidence, not proof of explorable geometry. Match the controls to the brief: a fixed
camera, object inspection, guided navigation, free walking or XR/head tracking.
A fixed-camera real-time scene can still need material and geometry specialists;
do not add navigation to satisfy the route. Do not force the scroll-world specialist
onto a single free scene; it owns a persistent scroll-authored journey through several
compositions.

Before calling a spatial scene photoreal, record an asset and material plan with a
provenance ledger: source, license or ownership, attribution, procedural/generated
status, intended camera distance and target devices. Record the geometry plan for
silhouette, bevels, normals and close-up surface form; the texture plan for texel
density and PBR maps; and the lighting plan, including which light and shadow work is
static or baked versus moving at runtime. Verify the result with screenshots or a
short clip from the actual working scene and relevant frame-time, draw-call,
triangle, texture-memory and load evidence. Name the tested device and runtime;
mark estimates, unavailable measurements and untested target devices explicitly.
Primitives suit structure and blockout; the rendered result decides photorealism.

When the scene includes object tasks, apply [interaction-contracts.md](interaction-contracts.md)
alongside the selected specialist. Detailed assets must keep the task's meaning,
selection, placement and recovery working ([gate 5](../SKILL.md#6-gates)).
For a substantial realism pass, use [spatial-realism.md](spatial-realism.md) for
asset integration, interface framing, baked dependencies and comparable runtime evidence.
It also describes the conditional Hyper3D/Rodin route without requiring generation.

The optional installer's `meng-3d` and `meng-game-dev` entries name these skills
individually; install only the ones a project uses. Other Meng skills are discoverable
when a new need appears.
