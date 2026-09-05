# Source and overlap review — 2026-09-05

Derived from an existing working local pipeline: scene-isolated Playwright capture,
ElevenLabs narration, FFmpeg normalization/assembly, screenshots, captions and a
silent revoice export. The reusable package contains no source-project case data,
recordings, voice IDs, credentials or narration. Implementation was generalized
independently; no third-party skill code was copied.

| Candidate | Useful method / decision | Boundary |
|---|---|---|
| [Remotion official skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion-best-practices) | Conditional: measured narration duration drives scene duration; use for designed overlays, transitions, zooms and motion graphics | Not needed for basic capture/FFmpeg assembly; check runtime commercial license before adopting |
| [Playwright recording skill](https://github.com/digitalsamba/claude-code-video-toolkit) | Adopt method: deterministic viewport, per-scene recording, flush on context close | Complements composition; browser footage is not desktop capture |
| [ElevenLabs speech skill](https://github.com/elevenlabs/skills/tree/main/text-to-speech) | Conditional: model/voice settings, text normalization, adjacent-text stitching if scene joins sound unnatural | Provider-specific; requires key and may incur charges |

Discovery used skills.sh and exact upstream repositories. Existing local
`web-video-presentation` overlaps in manifest-first narration, duration measurement
and audio-driven scene changes. Use it when the requested deliverable is a narrated
HTML presentation; this skill owns recordings of actual UI tasks. Existing `video`
is a broader format/tool chooser. Neither needs disabling or reinstalling.

Provider contracts: [OpenAI speech API](https://platform.openai.com/docs/api-reference/audio/createSpeech),
[ElevenLabs create speech](https://elevenlabs.io/docs/api-reference/text-to-speech/convert).
Capture lifecycle: [Playwright videos](https://playwright.dev/docs/videos).
Composition licensing: [Remotion license](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md).
Model lists, price and account voice access must be rechecked at use time.
