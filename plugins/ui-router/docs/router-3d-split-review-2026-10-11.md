# Router 3D split and slimming review: October 11, 2026

Record behind UI Router 1.19.0 and Work Router 1.9.0. The draft was independently
verified by Claude Fable 5.1 (max reasoning) against this repo, Lumbre,
threejs-game-skills and 3dviz-pro-max before the changes were made.

## Measurements before the change

- A substantial 3D route loaded ~20,000 words of router text: 8,602 (UI SKILL and core
  references) + 7,155 (3D references) + 4,290 (Work Router SKILL).
- About 700 words (~24%) of `route-ui-work/SKILL.md` was model policy that duplicated
  Work Router; the model table existed in five places.
- `optional-skills.json` listed `claudedesignskills` and `awwwards-3d` with no
  `skills` selector, so the `creative` profile installed every pack skill (Babylon,
  PlayCanvas, A-Frame, Spline, R3F, Substance, PixiJS and others).

## Upstream state (GitHub API, October 11, 2026)

| Repo | Stars | Last push | Decision |
| --- | --- | --- | --- |
| [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) | 30,489 | 2026-10-06 | Tool; CLI stays source of truth |
| [MengTo/Skills](https://github.com/MengTo/Skills) | 6,715 | 2026-10-06 | Named 3D and game-dev layers |
| [sparkjsdev/spark](https://github.com/sparkjsdev/spark) | ~3,700 | 2026-10-07 | Conditional, studies only |
| [CloudAI-X/threejs-skills](https://github.com/CloudAI-X/threejs-skills) | 3,530 | 2026-07-09 | Not adopted; covered by llms.txt |
| [majidmanzarpour/threejs-game-skills](https://github.com/majidmanzarpour/threejs-game-skills) | 2,476 | 2026-09-28 | Two reference files, read-only. Director and generators excluded: its credential probe sources shell profiles and starts paid generation when keys exist |
| [achimala/dream-loop](https://github.com/achimala/dream-loop) | 1,679 | 2026-09-09 | Fidelity loop; host-native harness |
| [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | 1,431 | 2026-10-09 | Not adopted; basics |
| [freshtechbro/claudedesignskills](https://github.com/freshtechbro/claudedesignskills) | 1,031 | 2025-11-20 | Demoted to three named layers |
| [viettranx/3dviz-pro-max](https://github.com/viettranx/3dviz-pro-max) | 724 | 2026-09-11 | CLI retrieval only; targets three 0.180 |
| [tsogjavklann/awwwards-3d](https://github.com/tsogjavklann/awwwards-3d) | 26 | 2026-05-08 | Conditional |
| [linegel/threejs-complete-set-of-skill](https://github.com/linegel/threejs-complete-set-of-skill) | 9 | 2026-09-24 | Watchlist; WebGPU/TSL only |

Official [three.js llms.txt](https://threejs.org/docs/llms.txt) became the base
knowledge layer. Posts on X in September–October describe GPT-6 Astra with Blender MCP
(sometimes with Tripo) as a strong 3D workflow, for example
[West Lord](https://x.com/MyWestLord/status/2099588840419651890) and
[walterzhu8](https://x.com/walterzhu8/article/2100255999365964113). That is background
for Codex sessions only; the harness rule is host-native.

## Verifier corrections adopted

- Blender MCP was already installed for Lumbre with a CLI-for-builds,
  MCP-for-inspection policy; the gap was only this repo's silence.
- Dream Loop had been loaded with a locked target; the open question was the harness.
  The user set the rule: the active host's model, overridable per run.
- `blender-web-pipeline`, used by Lumbre, comes from `claudedesignskills`, so the pack
  is demoted rather than dropped.
- `route-3d-work` lives inside the ui-router plugin (the package tests assert four
  plugins), with redirect stubs for moved anchors.

## Not yet measured

Whether the slimmer routes produce better or faster accepted results. See
[the paired-eval protocol](../tests/route-3d-paired-eval.md).
