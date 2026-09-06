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

## Expanded review after the quality target was clarified

[Clueso official skills](https://github.com/clueso-ai/skills) were missed in the initial
comparison. Its `polish-screen-demo`, `revoice-video`, and `screenshots-to-walkthrough`
are substantially closer to polished walkthrough production. Skills: Apache-2.0;
service/MCP remains proprietary and plan-dependent. [MCP docs](https://help.clueso.io/mcp-setup).

[Recordly](https://recordly.dev/) links to [canonical upstream](https://github.com/webadderallorg/Recordly).
Verified real cursor telemetry and editor export; no documented supported CLI found.
The smoke-export hook is internal testing infrastructure. License: AGPL-3.0.
[Dreamcut](https://dreamcut.ai/) is an editor/reference, not a tested adapter here.

Additional narrow discovery queries combined `clueso`, `polish-screen-demo` and
`screen demo` with skills.sh, Skillselion, SkillsMP and Skill Leaderboard domains.
No indexed matches from those queries; that does not establish absence. Homepages
of Skillselion, SkillsMP and Skill Leaderboard were opened; this was not an exhaustive
internal catalog search. Exact Clueso upstream/MCP docs yielded the actionable result.
No additional plugin was installed. Read polish.md and benchmarks.md for decisions.
