# Three.js builder review: October 18, 2026

Record behind UI Router 1.19.3. Sources: Meng To's posts from September 20 to
October 18, top three.js posts on X from October 1 to 18, and the threads, replies
and repositories they link. Older posts were kept only where the method still holds.
Every claim below is the author's report unless it says it was checked. Nothing was
installed, run, purchased or generated for this review.

## Adopted

| Finding | Source | Edit |
| --- | --- | --- |
| Review a moving camera as a clip. A one-minute clip review returned timestamped defects: a porch collapsing into a floating wall at 24.1 s, a lantern hanging off a wall, a doormat flickering to lawn. Flicker and angle-dependent collapse do not show in a settled still. | [Meng, Oct 16](https://x.com/MengTo/status/2111147234171764759) | Gate 3 in `SKILL.md`; moving-view check and gate in `spatial-realism.md`; rendered comparison in `fidelity-loop.md`. The method is adopted; the reviewing model he used (Elorian Glimpse) is not. |
| Code-built geometry can be baked once instead of built at startup. Athenaion builds heavy terrain, statues and a giant head at first load "which is slow", and ships a bake step. | [Athenaion README](https://github.com/Leonxlnx/athenaion) (MIT), [three.js repost, Oct 18](https://x.com/threejs/status/2111747312343281703) | `spatial-realism.md`, runtime responsibilities; pointer from the load-budget line in `SKILL.md`. |
| Seat imported and scanned props in the ground. Poly Haven scans read as part of the coast once their bases were sunk into the terrain, scale and rotation varied and rocks overlapped into formations. | [zavrenn, Oct 16 reply](https://x.com/zavrenn/status/2110759896580858276) | `spatial-realism.md`, asset integration. |
| glTF has no ratified lightmap slot. Bakes travel on a second UV set with a separately loaded texture, or are packed into emissive maps; Ben Houston opened KHR_lightmap on October 14 to replace the emissive workaround. Checked: [KhronosGroup/glTF#2679](https://github.com/KhronosGroup/glTF/pull/2679) and the vendor draft [#2672](https://github.com/KhronosGroup/glTF/pull/2672) were open on October 18. | [Ben Houston, Oct 15](https://x.com/benhouston3d/status/2110713492198322182), [brice_deg replies, Oct 13](https://x.com/brice_deg/status/2109628401774477374) | `spatial-realism.md`, baked lighting. |
| Show what the bake does. Turning the bake off in a capture shows which light is baked in Blender and which reflections and beams are live in three.js. | [brice_deg, Oct 14](https://x.com/brice_deg/status/2110342713228865764) | `spatial-realism.md`, baked lighting. |

## Conditional

| Finding | Source | Decision |
| --- | --- | --- |
| Agent-side listening. earshot (MIT, CPU-only, CLI and MCP) describes a sound, scores it against a description, finds moments in a long take and lays out a timeline against picture cuts. Its optional cloud critique uploads audio with the user's own key. | LexnLin's launch, quoted by [Meng, Oct 16](https://x.com/MengTo/status/2110938316162076685); [repo](https://github.com/Leonxlnx/earshot) | Added to `runtime-and-slice.md` as a screening aid when the agent cannot listen. Human listening still accepts sound; the upload path needs consent. No trial was run. |
| Color statistics against the target. Athenaion's look-dev rounds compared each render with its reference side by side and with color statistics. | [Athenaion README](https://github.com/Leonxlnx/athenaion) | Added as an optional aid to the rendered comparison. It does not replace the critique. |

## Already covered

- Blender driven by scripts that build geometry, materials and lighting, export GLB and
  check renders ([chetanankola, Oct 8](https://x.com/chetanankola/status/2108105321239789624)).
  The CLI is already the source of truth.
- Procedural code for buildings and vegetation, imported models for characters and
  some props ([zavrenn](https://x.com/zavrenn/status/2110759896580858276)); "for more
  detail, this might need blender" ([Meng, Oct 17](https://x.com/MengTo/status/2111516431552848274)).
  The hybrid pipeline covers it.
- Proportions first, then one part at a time against fixed references; rework or drop
  an asset that does not fit. Covered by the limiting-layer diagnosis.
- Image generation first, then code ([Meng, Oct 18](https://x.com/MengTo/status/2111709544103752163)).
  Covered by the locked target.
- Scoring toward 8/10 rather than 10 ([Meng, Oct 8](https://x.com/MengTo/status/2107985872201400772)).
  Covered by the selected workflow's exit and stall rules; still reference only.
- "Three.js for now, Unreal later" ([Meng, Oct 3](https://x.com/MengTo/status/2106435376865006055)).
  `runtime-and-slice.md` already warns against postponing a decisive platform
  requirement to an assumed later port.
- A Unity demo ported to three.js in two days but unpublishable because of the asset
  license ([mrdoob, Oct 5](https://x.com/mrdoob/status/2107140346576818474)). The
  provenance ledger covers it.
- Image-to-world and image-to-asset generators ([NVIDIA Lyra 2.0](https://x.com/oliviscusAI/status/2105515139382272262),
  [TRELLIS.2 and others](https://x.com/Mnilax/status/2109716261160538324), photo-to-world repos). Covered by the generated-worlds section and the generator-first default.
- Dan Greenheck's character pipeline: Tripo3D model and rig, re-texture with image
  generation, Mixamo animation ([Oct 12](https://x.com/dangreenheck/status/2109539619125498028)).
  The conditional generated-asset route covers it. His [Fire Pro](https://github.com/dgreenheck/threejs-fire-pro)
  (MIT) needs `WebGPURenderer`, so the existing WebGPU exclusion applies to WebGL projects.
- AA-3D's agent sandbox (Blender, Rapier, a headless browser for self-checks and a CC0
  library) matches the router's tool table ([Artificial Analysis, Oct 12](https://x.com/ArtificialAnlys/status/2109791341802885209)).

## Reference only

- Athenaion's build: art bible and module contract, 12 specialist agents rendering
  against references, 55 subagents, about 45 hours and a reported $1.8k to $2.3k
  API-equivalent. Its 4K stills come from an offline accumulation renderer, so they
  are appearance evidence, not runtime evidence. Delegation stays with Work Router.
- Pine & Parcel and Stillwater ([zavrenn](https://x.com/zavrenn/status/2109312983402782988)):
  calm browser worlds capped at 30 FPS with loading still in progress.
- [three-liltoon](https://github.com/mochiya-labs/three-liltoon) (MIT) for VRM and GLB toon avatars, if a stylized cast is chosen.
- Meng's [icon-to-3D tool](https://x.com/MengTo/status/2107445210011849103),
  [Fil](https://x.com/MengTo/status/2108581305197924583), the open-source
  [Shaders library](https://x.com/MengTo/status/2108924473265275003),
  [Anatomy](https://x.com/MengTo/status/2109182449179836579),
  [ThreeUI](https://x.com/MengTo/status/2103155074705019158) and the
  [Pika plugin](https://x.com/MengTo/status/2111294425959923839). Landing-page and
  explainer work stays with `route-ui-work`.
- Browser-game economics: a [CrazyGames launch estimate](https://x.com/froessell/status/2110671824279179694)
  and a [22 MB world built for $6,500 in API credits](https://x.com/chrisfirst/status/2107966951200866422).
  These are product questions, not routing rules.

## Defer

- [In-browser lightmapping](https://x.com/marco_fugaro/status/2110262616425955359) (unreleased) and WebGPU path tracers such as
  [pissang/mutracer](https://github.com/pissang/mutracer) (MIT) as lighting reference
  renders. Revisit when a bake discrepancy needs ground truth.
- [Genex desktop](https://github.com/genex-games/genex-desktop) (MIT) and Scenario's
  [GameDev OS](https://x.com/emmanuel_2m/status/2103097017073361137). Both are full
  game-dev harnesses; no trial, and their generators are paid.
- [Motion-matched animation from video references](https://x.com/MrCollison/status/2107214135188656510)
  and the [ik01 locomotion engine](https://x.com/shoejaat/status/2108391208825287098).

## Rejected as routing policy

Model rankings from demos and single-prompt comparisons, and benchmark leaderboards
([AA-3D](https://x.com/ArtificialAnlys/status/2109791341802885209),
[3JSBench](https://x.com/generalcontext_/status/2108313483293147292),
[Blender Bench v1](https://x.com/refresh_dev/status/2105359734287249559),
[LuminaBench 3D Seaplane](https://x.com/LuminaBench/status/2106850337592328658)). Work Router owns model
choice; AA-3D's cost frontier is a candidate input for its benchmark sources.

## Check

Fresh read-only subagents (Claude Opus 5.5, Claude Code) ran two briefs against the
repository files before and after the edits. This is a policy walkthrough, not a
build, device trial or comparative benchmark.

**Applicable brief:** a calm first-person browser world (three.js 0.180, Blender bakes
on a second UV set) adds a market scene. Six problems from its last pass were given.

| Problem | 1.19.2 | 1.19.3 |
| --- | --- | --- |
| One-second startup task from code-built geometry | Instancing and measurement; "pre-building geometry into GLB is outside router" | Bake at build time or build off the main thread, then compare startup |
| Trunk emerging through paving | Limiting layer, support and facing; "ground-blending techniques are outside router" | Sink, vary, cluster, give a footing; fix placement before remodeling |
| Flicker seen only in a recording | Clips allowed; the cause is "outside router" | Clip along the real path with timestamped causes; recheck the same path |
| Washed-out bake after re-export | Strongest coverage (boundary diagnosis); color space and UV set "outside router" | Adds transport record and UV set, color space and intensity check |
| Baked versus live light unclear | Lighting plan; "debug isolation views are outside router" | Review switch that turns baked layers off |
| Agent cannot listen | Same-brief kit comparison; "nothing specific about a non-listening agent" | Local screening tool, acceptance by listening, consent before upload |

Both runs kept the project as lead, held the fidelity loop back for a calm pass,
listed the headset and treadmill as untested and kept paid generation off. The
second run noted that installing the audio tool needs the user's approval.

**Routing brief:** a scroll-driven landing-page hero, a HUD label change and a rug
that flickers while walking. Both runs sent the first two to `route-ui-work` without
3D layers. For the flicker, 1.19.2 called the clip question "router silent, and that
leaves a gap", because the spatial gate asked only for settled views; 1.19.3 required
the clip and cited the cause list. Neither run applied the new checks to the
landing-page or HUD requests.

Not measured: whether these edits change accepted results, tokens or time on a real
pass. The [paired-eval protocol](../tests/route-3d-paired-eval.md) still applies.
