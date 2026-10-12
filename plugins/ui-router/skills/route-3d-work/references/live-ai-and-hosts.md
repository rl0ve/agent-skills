# Hosted builders, live intelligence and host delivery

On-demand reference for the 3D route. Read only the section that matches the open
question; a settled stack without live AI or a host plugin does not need this file.
Dated vendor details below were checked on the stated dates; re-verify at use.

## Verify a hosted builder's exit path

Separate playable export, editable source, commercial rights and independent hosting.
Check the current plan and project provenance: original projects, templates and remixes
may have different export rights. A code tab or downloaded game does not establish a
complete editable project. When portability is required, export a representative slice,
open it in the supported editor/version, change it and rebuild outside the service.
Verify scripts, scenes, assets/licenses and required backend or voice integrations;
record any dependency that still requires the hosted service. Keep unverified export
claims unresolved rather than treating a prototype as a portable production foundation.

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
world/lesson state as well as the spoken response. Reuse [motion-quality.md](../../route-ui-work/references/motion-quality.md)
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

