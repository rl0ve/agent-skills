# Local and no-hosted-API routes

Reviewed 2026-09-05. These are task-fit recommendations from current official
capabilities, not a measured head-to-head quality leaderboard. Run the same short
capture and narration through finalists before declaring a winner.

“No API” can mean no separate media API bill, or completely offline execution.
Codex/Claude Code can orchestrate local programs through a CLI or local MCP; that
local interface is still technically an API. Their own model inference may remain
hosted. Initial software/model downloads, license activation, cloud AI, sharing,
avatars and TTS are separate dependencies. Never call a whole workflow offline
because its video renderer is local.

## Rank by the job

| Priority | Candidate | Why it fits | Boundary |
|---|---|---|---|
| 1 for an agent-operated desktop workflow | Cap Studio + CLI/local MCP | Local editable capture, click metadata, cursor polish, zooms, captions, local export; explicit Codex/Claude Code interface | Verify installed command contract and actual editing controls. Cloud library/AI/sharing are separate. Distributed desktop builds require a commercial license for commercial use. |
| 1 for a free local screen-demo editor | Recordly | Native Mac/Windows capture; cursor separation, smoothing, zoom suggestions, timeline and frames | Desktop/editor integration, no supported production CLI confirmed. Linux cannot currently hide captured cursor. AGPL and additional license text apply to source reuse. |
| 1 for ready-made Mac presentation | Screen Studio | Purpose-built automatic zooms, cursor smoothing/hiding, audio cleanup and local transcripts | Paid Mac app; no supported general production CLI confirmed. Best polish candidate, not a measured winner in this review. |
| 1 for a permissively licensed agent compositor | HyperFrames | Local deterministic HTML/CSS/media-to-MP4 rendering, agent skills, Apache-2.0 | Composition framework; it does not automatically record a real app or understand every action. Hosted rendering and generated media are optional separate services. |
| 2 for an agent compositor; 1 in an existing React video stack | Remotion | Local CLI rendering, React compositions, reusable timelines and official agent skills | More engineering than a screen editor. Commercial licensing depends on use and organization. Not universally free or permissively licensed. |
| 1 for flexible capture infrastructure | OBS + FFmpeg | Cross-platform local recording and programmatic control via bundled obs-websocket | Requires separate cursor telemetry and editing for Screen Studio-style results. Recording infrastructure, not an automatic polish engine. |

For the smallest path to a polished screen recording, trial a dedicated native
recorder before extending the bundled Playwright compositor. For repeatable branded
variants or integration into a build workflow, trial HyperFrames/Remotion with real
capture inputs. Keep the included helper as an editable fallback and test harness;
do not rank it above mature editors merely because it is already implemented.

[Cap Studio](https://cap.so/docs/recording/studio-mode),
[Cap agent interface](https://cap.so/docs/agents),
[Cap commercial builds](https://cap.so/docs/commercial-license),
[Recordly source/features](https://github.com/webadderallorg/Recordly),
[Recordly license](https://github.com/webadderallorg/Recordly/blob/main/LICENSE.md),
[Screen Studio](https://screen.studio/),
[HyperFrames](https://github.com/heygen-com/hyperframes),
[Remotion rendering](https://www.remotion.dev/docs/render),
[Remotion license](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md),
[OBS](https://obsproject.com/),
[OBS local control](https://github.com/obsproject/obs-websocket).

## Local narration: separate audition ranking

| Trial priority | Model | Best starting environment | Tradeoff |
|---|---|---|---|
| 1 on Apple Silicon | Chatterbox full model | Official MPS/CPU Mac example; local Python; MIT | Reference-guided voice and expressive controls; approve the reference and audition. Turbo's documented CUDA path is not the same Mac support claim. |
| 1 on Windows with NVIDIA; 2 overall | Qwen3-TTS | Official CUDA deployment, 0.6B/1.7B downloadable models; Apache-2.0 | Voice design/cloning and custom voices. Official repository does not establish Mac/MPS support; community ports need separate validation. |
| 3; first for minimum footprint | Kokoro-82M | Small local Python model, optional community ONNX/MLX runtimes; Apache | Fast preset-voice baseline. Small/fast does not mean the most natural delivery. |

All need initial model assets; none needs a hosted TTS call for local inference.
Codex/Claude Code can invoke a script producing WAV, then measure its duration.
Do not install multi-gigabyte weights for an informational comparison. Do not reuse
or clone an identifiable person's voice without their authorization. A built-in
or properly licensed reference voice is preferable when no authorized clip exists.

This is a trial order, not proof that one model sounds better. Use identical copy,
including product names and transitions; level-match samples before listening.
The hard gate remains “does this delivery sound natural to this user?” A lightweight
system voice is not an acceptable automatic fallback.

[Chatterbox](https://github.com/resemble-ai/chatterbox),
[official Mac example](https://github.com/resemble-ai/chatterbox/blob/master/example_for_mac.py),
[Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS),
[Kokoro](https://github.com/hexgrad/kokoro).

Fish S2's research license and flagship hardware requirements make it a poor default
for this production workflow. F5's code license and noncommercial pretrained-weight
license differ. CosyVoice is promising but its official deployment is CUDA-oriented.
Do not infer unrestricted commercial usage from an open GitHub repository.
[Fish](https://github.com/fishaudio/fish-speech),
[F5](https://github.com/SWivid/F5-TTS),
[CosyVoice](https://github.com/QwenAudio/CosyVoice).

## HeyGen distinction

HeyGen's hosted avatar/localization product and its open-source HyperFrames project
solve different problems. HyperFrames belongs in the local composition shortlist;
it does not imply offline access to HeyGen avatars, cloned cloud voices, dubbing or
lip-sync. See [effects.md](effects.md) for the screen-editor versus presenter comparison.
