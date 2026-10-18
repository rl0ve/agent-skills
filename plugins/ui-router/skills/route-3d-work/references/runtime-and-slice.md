# Choose the stack for an interactive world

Use when choosing or materially changing the architecture of a playable 3D world,
simulation or spatial learning product. Keep a working stack for a scoped art, copy
or interaction fix. A decorative scene does not need a game architecture review.

For a hosted builder, a live model decision, live conversation or a host plugin
(ChatGPT/MCP App), read [live-ai-and-hosts.md](live-ai-and-hosts.md).

## Separate the decisions

| Concern | What owns it |
| --- | --- |
| Runtime and authoritative state | Rendering, input, collision, navigation, legal actions, progression and persistence; use ordinary code for exact rules. |
| Content and learning design | Authored scenarios, semantic objects, language targets, support and success evidence when this is a learning product. |
| Authoring and assets | Blender, licensed libraries, procedural modeling and selected generators produce or edit assets. Meng skills and Dream Loop guide construction and critique; they are not game engines. |
| Optional live intelligence | Dialogue, speech or bounded decisions serve an identified interaction need. The model used to build the app need not run inside the shipped product. |

Select only the concerns this product needs. Do not add multiplayer, a backend, an
NPC service or continuous inference because a research stack includes them. A solo
recognition activity can work with authored content and deterministic interactions.

## Choose from delivery and authoring needs

Start with the existing code and skills, target devices, distribution, camera/input
requirements, fidelity and content-authoring workflow. Select specialists compatible
with the chosen runtime; a web-only scene procedure does not establish a native-engine
workflow. Web, native and headset targets
can lead to different choices; an XR-first requirement belongs in the initial decision.
The following are conditional candidates, not a ranking or mandatory dependency list.

| Project need | Candidate and tradeoff to examine |
| --- | --- |
| An existing web application with bounded 3D interactions | [Three.js](https://threejs.org/manual/pages/game.html), with [React Three Fiber](https://github.com/pmndrs/react-three-fiber) when React fits. Three.js supplies rendering; explicitly account for the required game systems and their maintenance. R3F is a React renderer, not a complete game engine. |
| A browser game that needs more integrated engine facilities | Compare [Babylon.js](https://www.babylonjs.com/specifications/) with [PlayCanvas](https://developer.playcanvas.com/user-manual/engine/). Inspect required physics, navigation, tooling and deployment paths; evaluate the PlayCanvas Editor separately from the engine. |
| Visual scene authoring in Blender or Unity with browser delivery | Consider [Needle Engine](https://engine.needle.tools/docs/technical-overview.html), a Three.js-based runtime with editor integrations. Trial the actual component/export workflow and current license; this is not the same as a Unity player build. |
| Native/mobile or headset delivery, or an established game-engine pipeline | Evaluate Unity, Godot or Unreal against the required device and team workflow. Do not postpone a decisive platform requirement to an assumed later port. For web delivery, inspect the selected [Unity browser compatibility](https://docs.unity3d.com/Manual/webgl-browsercompatibility.html) or [Godot export constraints](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_web.html). |
| Unreal fidelity delivered through a browser stream | Evaluate [Pixel Streaming](https://dev.epicgames.com/documentation/unreal-engine/pixel-streaming-in-unreal-engine) as remote application hosting, including network latency, GPU capacity and recurring session cost. A browser frontend does not establish client-side rendering. |

Verify version, license, export and target-device support for the selected route at
point of use. Compare one or two credible alternatives only when a real uncertainty
justifies it. A GLB can carry art between engines; it does not port gameplay code,
shaders, input, persistence or a complete lesson. Include migration and regression
work before recommending a rewrite. Demo quality and model release dates do not
establish an engine's superiority or change Work Router's model policy.

## Prove specialist device input early

When a required target uses eye/hand input, a locomotion treadmill or another
specialist peripheral, inspect the actual SDK, driver and distribution path before
committing to an engine. WebXR support does not establish that an external device's
input reaches the web application. For example, Meta's
[VR Glasses web guide](https://developers.meta.com/vr/documentation/iwsdk/guides/get-started-glasses/)
and Virtuix's [Omni One PCVR guide](https://support.virtuix.com/hc/en-us/articles/36063096094349-Intro-to-Using-Omni-One-for-PCVR)
describe different integration paths. Check the selected device/version and account
access rather than inferring universal support from the product family.

Keep targeting, selection and locomotion adapters separate from semantic actions,
collision, learning evidence and save state. Prove one representative action and
movement sequence, including interruption and fallback. Do not combine tracked head
pose with artificial movement twice. Preserve stationary/accessible play when it
fits the brief. Emulation and a related headset can expose gaps; only the actual
device establishes its tracking, comfort and sustained performance.

## Author sound as part of the scene

Use when a game/world needs music, environmental loops or action sounds. Separate
these asset jobs from narration and from the runtime mix; the voice-narration owner
continues to own generated speech. Specify the place, material, action, duration,
loop behavior and mood. Prefer isolated effects when the engine will supply space
and ambience; keep speech intelligible with separate levels and ducking.

A multimodal workspace such as [MiniMax Design](https://design.minimax.io/en) and
an asset service such as [Higgsfield's CLI catalog](https://github.com/higgsfield-ai/cli/blob/main/MODELS.md)
are conditional authoring routes, not game engines or proven quality winners.
[ElevenLabs Sound Effects](https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert)
is another candidate when explicit loop/duration control fits. Compare a short,
same-brief kit with existing recordings or licensed assets; inspect loop seams,
naturalness, speech masking, export, editing time and cost across attempts.

When the agent cannot listen, a local analysis tool such as
[earshot](https://github.com/Leonxlnx/earshot) (MIT, CPU-only, CLI and MCP) can
describe candidates, score them against the brief and time effects against picture.
Use it to screen and catch sync errors; accept sounds by listening in the scene. Its
optional cloud critique uploads audio, so leave it off without the user's consent.

Verify access, the actual billing route and commercial rights for the selected
model, plan and delivery platforms. Music rights can differ from speech/effects;
an aggregator's web allowance can differ from CLI/API credits. Cache accepted
assets with provenance and test their final in-scene playback, mute, separate
volumes, speech transitions and suspend/resume. A creator's tool mention is a lead,
not evidence to replace working assets or purchase a plan.

## Design a reason to keep playing

Use for a playable world or a learning product whose engagement is unresolved.
Define a concrete goal, the information the player must interpret, meaningful
actions or choices, visible consequences, useful recovery and a reason to explore
the changed world. Object counts, a free camera and a sequence of Next buttons do
not establish this loop. Preserve a calm or input-first brief; game structure does
not require points, streaks, combat, timers or forced speech.

Build one connected scenario before adding many isolated activities. For learning,
make understanding the target language useful to the action, reintroduce it in a
changed context, and distinguish assisted success from independent recognition.
Exercise alternative choices, understandable mistakes, recovery and resume.
Record whether a learner understands the goal and voluntarily continues; keep
observed engagement separate from delayed transfer or retention evidence.
Self-scored rubrics and social likes cannot substitute for those observations.

## Prove a representative playable slice

Before expanding or migrating, exercise one scenario with a representative asset and
the real controls: enter, act, receive feedback, recover and save/resume if required.
For learning, include the target language and agreed response mode. Add a live service
only if it is part of the proposed route, and check its delay, interruption and failure
behavior. Set transfer, memory, frame-time and response budgets from target devices and
use; do not copy a universal download size or FPS target from a demo.

For offline or headset requirements, exercise the actual package/device with the
required network access disabled and the chosen locomotion/input modes. Identify any
setup/download exception in the brief; do not silently add a cloud dependency.

Compare appearance, exercised behavior, authoring effort and runtime evidence with the
existing implementation. Apply [spatial-realism.md](spatial-realism.md) for destination
assets and performance, and the selected [playable-game specialist](specialists.md)
for relevant controls and regression checks. Record measured results and remaining
uncertainty; a policy walkthrough or attractive video does not establish a successful
migration, headset support or learning benefit.

Source checks and adoption decisions: [September 27 review](../../../docs/interactive-worlds-review-2026-09-27.md).

October 1 follow-up: [playable-world and host review](../../../docs/playable-worlds-review-2026-10-01.md).
October 18: [three.js builder review](../../../docs/threejs-builders-review-2026-10-18.md).

## Gate

- [ ] Runtime chosen from delivery and authoring needs, with the rejected options noted.
- [ ] Game state, content and optional live intelligence kept separate.
- [ ] Specialist device input proven on the device, or listed as untested.
- [ ] A representative playable slice exercised end to end before expansion or migration.
- [ ] Sound authored as part of the scene when the task uses it.
