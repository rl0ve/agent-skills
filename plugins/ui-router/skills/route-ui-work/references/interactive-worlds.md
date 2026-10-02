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

## Verify a hosted builder's exit path

Separate playable export, editable source, commercial rights and independent hosting.
Check the current plan and project provenance: original projects, templates and remixes
may have different export rights. A code tab or downloaded game does not establish a
complete editable project. When portability is required, export a representative slice,
open it in the supported editor/version, change it and rebuild outside the service.
Verify scripts, scenes, assets/licenses and required backend or voice integrations;
record any dependency that still requires the hosted service. Keep unverified export
claims unresolved rather than treating a prototype as a portable production foundation.

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

Verify access, the actual billing route and commercial rights for the selected
model, plan and delivery platforms. Music rights can differ from speech/effects;
an aggregator's web allowance can differ from CLI/API credits. Cache accepted
assets with provenance and test their final in-scene playback, mute, separate
volumes, speech transitions and suspend/resume. A creator's tool mention is a lead,
not evidence to replace working assets or purchase a plan.

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
rules work. Check the chosen model's supported inputs and evaluate decisions in the
actual target language; English results do not establish multilingual accuracy. Calibrate
any confidence threshold on representative task data, allow abstention/fallback, and
recheck after a model change. Dialogue, speech and packaged NPC services need their own
task-specific quality, delay, cost and recovery checks.

OpenAI's [Decisions API announcement](https://x.com/OpenAIDevs/status/2105003318917697873)
describes selection from predefined answers, powered by Luna, in limited preview
as of September 29, 2026. Treat it as another conditional decision route, distinct
from Jev and other services with the same API name. Verify official request schema,
account availability and pricing at use. A model's presence in a coding host does
not establish access to that runtime API or a benefit over authored rules.

Treat a model response as a proposal. Validate its action, target and preconditions
against current authoritative state before applying it. Discard stale responses from
a prior scene/turn, prevent duplicate actions on retries, and preserve a useful pending
state and timeout fallback. Keep assessment evidence separate from the NPC's assertion
that the player succeeded. Use [interaction-contracts.md](interaction-contracts.md)
for the task and learning semantics.

## Evaluate live conversation as a complete interaction

Use this check when live conversation is part of the intended activity. Prerecorded
clips remain with the voice-narration owner. Choose direct speech or a transcription,
dialogue and speech-synthesis pipeline from the task's control and observability needs.
When comparing candidates, use the same lesson, target language, input conditions and
success criteria. Listen to pronunciation and intelligibility; exercise recognition,
turn-taking, corrections, interruptions and connection recovery. Verify the resulting
world/lesson state as well as the spoken response. Reuse [motion-quality.md](motion-quality.md)
for microphone intent, cancellation and playback lifecycle checks.

Measure the user's wait from the end of their speech to audible useful response,
including endpoint detection, network, model/tool work, buffering and playback. Separate
an acknowledgment from a useful answer. With repeated observations, report median and
tail latency plus failures; provider time-to-first-byte is not the complete experience.

Estimate cost per comparable completed lesson using current rates and explicit learner
speech, NPC speech and pause durations. Identify the actual meters: connected time and
any billed silence, audio/text tokens, characters, backend calls and growing context.
Include retries, reconnects and applicable minimums; distinguish usage from subscription
fees and included credits without double-counting. Character-to-minute assumptions need
checking in the target language. Check expected concurrency separately from single-session
cost. Label estimates and failed/incomplete sessions; cheaper output does not establish
equivalent teaching quality. Align connection lifetime with the intended interaction
and preserve lesson state when closing an idle metered session.

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

## Treat host plugins as a delivery choice

When a ChatGPT plugin or MCP App is proposed, use current official platform docs
and the host's app-development specialist. The October 2026
[extensions documentation](https://developers.openai.com/plugins/build/extensions)
supports fullscreen sidebar apps and conversation panels. That is an additional
surface, not evidence that the host supplies a game engine or supports immersive XR.
Keep the scene, rules and content separable from a small host adapter where practical.

Trial one real scene in the target host before committing: WebGL/resource loading,
input focus and pointer behavior, user-gesture audio, resizing, background/return,
save/resume and accessible controls. Check the current
[UI/CSP and state guidance](https://developers.openai.com/plugins/build/chatgpt-ui).
Authoritative progress must survive widget remounts; do not rely only on ephemeral
widget state. Verify actual headset support separately when required. A launch/resume
or contextual-help companion may be the appropriate first surface.

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

October 1 follow-up: [playable-world and host review](../../../docs/playable-worlds-review-2026-10-01.md).
