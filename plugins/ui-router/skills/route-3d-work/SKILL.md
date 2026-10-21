---
name: route-3d-work
description: Route real-time 3D work to the right knowledge layers, specialists, fidelity loop and tools. Use for playable 3D worlds, spatial scenes, three.js/WebGL/WebXR builds, Blender-to-web asset pipelines, 3D realism or fidelity passes, Dream Loop, and runtime or engine choices. Interface chrome over a 3D scene (HUD, menus, overlays) routes through route-ui-work as a layer.
---

# Route 3D work

**Purpose:** pick the smallest set of guidance for a 3D task, keep the project's own
pipeline in charge, and judge the result from the running build.

## 1. Find the lead

| Situation | Lead |
| --- | --- |
| The project has a recorded direction, pipeline or checkpoint docs | **The project.** Read its `AGENTS.md` and current-phase docs first. Everything below is a layer under it. |
| New world or game, runtime unsettled | [runtime-and-slice.md](references/runtime-and-slice.md): choose the runtime from delivery and authoring needs, then prove a representative slice. |
| Scroll-authored journey on a marketing or portfolio page | Hand off to `route-ui-work` (creative-expressive, `meng-webgl-stack`). Come back here only for the fidelity gate. |
| Live AI in the world, a hosted builder, or a ChatGPT/MCP App host | Add [live-ai-and-hosts.md](references/live-ai-and-hosts.md) for that question only. |

Use one lead. Add at most three layers for the current pass.

## 2. Map runtime to knowledge

| Runtime | Base knowledge | Technique layers |
| --- | --- | --- |
| Vanilla three.js, WebGLRenderer | three.js `llms.txt`, checked against the pinned version | Meng 3D, Meng game-development, `blender-web-pipeline`, 3dviz-pro-max retrieval |
| React Three Fiber | R3F/drei docs plus three.js `llms.txt` | Meng 3D; pmndrs docs, and the pmndrs/xr skill for XR |
| three.js WebGPURenderer / TSL | three.js `llms.txt` (WebGPU/TSL sections) | WebGPU/TSL packs become eligible; recheck the Meng skills for renderer assumptions |
| Babylon.js, PlayCanvas, Godot, Unity | That engine's official docs and MCP | Generic three.js packs do not apply |

The details, entrypoints and exclusions are in [specialists.md](references/specialists.md).
Do not install broad packs for a runtime the project does not use.

## 3. Choose specialists by need

- **Playable design** (objectives, levels, camera, audio feedback, playtesting): Meng
  game-development entries in [specialists.md](references/specialists.md#playable-world-design-and-feedback).
- **Surfaces and props seen up close:** Meng `3d-high-resolution-textures`,
  `3d-high-poly-models`, plus [spatial-realism.md](references/spatial-realism.md) for
  the asset, material and lighting plan. Diagnose a visual defect at its stage (source,
  export, optimization, runtime) and verify the delivered asset boundary before
  remodeling.
- **Water, sky, atmosphere:** Meng `3d-ultra-realistic-water`, `3d-sky-background`.
- **Tours, orbit inspection or free walking:** Meng `3d-virtual-tour`. Match the
  controls to the brief.
- **Frame-time, memory or load budget failures:** Meng `optimize-threejs-games`; for
  startup stalls from code-built geometry, [spatial-realism.md](references/spatial-realism.md#assign-authoring-and-runtime-responsibilities).
- **Object tasks** (pick up, place, combine, inspect):
  [interaction-contracts.md](references/interaction-contracts.md).

## 4. Fidelity loop

When acceptance depends on requested high graphical fidelity, use Dream Loop under the
[fidelity execution gate](references/fidelity-loop.md#fidelity-execution-gate).

- **Host-native harness:** run in the host you are in. Codex uses GPT-6 Astra; Claude
  Code uses Claude Opus 5.5. A model the user names overrides this. Never move the work
  to another host to match upstream's tested harness.
- **Target first:** lock a product-specific in-engine target before the build pass.
  Reject the generic flat, pastel, toy-like look unless the brief asks for it.
- **Rounds:** start at medium effort, cap at 2–3 rounds, and stop when recorded gaps
  close. Work Router owns any effort increase.
- **Fallback:** UI Router's [visual-build-loop](../route-ui-work/references/visual-build-loop.md)
  is a disclosed adaptation, not Dream Loop. Report it by name.

## 5. Tools

| Tool | Role |
| --- | --- |
| Blender headless CLI | Deterministic builds and bakes. The source of truth. |
| Blender MCP (pinned, safe mode) | Live inspection and small edits. Fold accepted edits back into scripts. |
| Project capture and measurement harnesses | Screenshots, clips, frame time, draw calls, memory, transfer size. |
| 3dviz-pro-max `scripts/search.py` | Retrieval for Blender↔three.js, IBL, bake and XR recipes. Clone it outside skill folders. |
| Needle Inspector + MCP | Trial only, for live scene-graph inspection. |

## 6. Gates

Treat a pass as complete only when every applicable gate is **met**, or is marked
**open** or **blocked** with the reason:

1. **Lead and layers named:** which skills were loaded and which ran.
2. **Provenance ledger:** source, license, generated or procedural status, and camera
   distance for each new asset.
3. **Runtime evidence:** screenshots from the running build on a named device, plus a
   short clip along the real camera path when the camera moves (stills miss flicker,
   pop-in, floating parts and moving parts that turn about the wrong pivot); frame time, draw calls, triangles, texture memory and
   transfer size. Estimates are labeled as estimates.
4. **Target comparison:** for a fidelity pass, the build has been compared with the
   locked target and the remaining gaps are recorded.
5. **Interaction intact:** task meaning, selection, placement and recovery still work
   after the visual changes.
6. **No paid generation or secret lookup** without explicit authorization for that run.
7. **Untested devices** (headset, mobile, voice) are listed as untested. They are not
   implied by desktop results.

## Boundaries

- Do not copy a specialist's procedure into this file. Load the original.
- Interface chrome, typography and layout over the scene go through `route-ui-work`.
- Model effort and delegation go through Work Router when it is installed.
