# Choose the stack for an interactive world

Use when choosing or materially changing the architecture of a playable 3D world,
simulation or spatial learning product. Keep a working stack for a scoped art, copy
or interaction fix. A decorative scene does not need a game architecture review.

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

## Keep live model decisions bounded

Use authored rules or a state machine where they satisfy the behavior. Add a model
for a specific unresolved need, such as interpreting an open-ended response or choosing
among context-sensitive NPC actions. Keep requests off the render/physics loop; trigger
them at relevant events or a bounded cadence with a latency and session-cost budget.

For example, [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) is a
conditional structured-decision service, not a 3D engine or dialogue generator. Its
vendor describes typed probabilistic choices and gives up string generation. Output
type guarantees and reported confidence do not prove a decision is correct for the
game or learner; vendor demos are not a workload benchmark. Do not add it when ordinary
rules work. Dialogue, speech and packaged NPC services need their own task-specific
quality, delay, cost and recovery checks.

Treat a model response as a proposal. Validate its action, target and preconditions
against current authoritative state before applying it. Discard stale responses from
a prior scene/turn, prevent duplicate actions on retries, and preserve a useful pending
state and timeout fallback. Keep assessment evidence separate from the NPC's assertion
that the player succeeded. Use [interaction-contracts.md](interaction-contracts.md)
for the task and learning semantics.

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
assets and performance, and the selected [playable-game specialist](upstream-skills.md)
for relevant controls and regression checks. Record measured results and remaining
uncertainty; a policy walkthrough or attractive video does not establish a successful
migration, headset support or learning benefit.

Source checks and adoption decisions: [September 27 review](../../../docs/interactive-worlds-review-2026-09-27.md).
