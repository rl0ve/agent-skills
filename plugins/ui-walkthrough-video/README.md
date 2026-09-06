# UI Walkthrough Video

A shared Codex and Claude Code plugin with two skills: real UI walkthrough production and reusable voice narration.

Install from the rl0ve-agent-skills marketplace with `codex plugin add ui-walkthrough-video@rl0ve-agent-skills` or `claude plugin install ui-walkthrough-video@rl0ve-agent-skills`.

Use [ui-walkthrough-video](skills/ui-walkthrough-video/SKILL.md) for capture and video assembly, or [voice-narration](skills/voice-narration/SKILL.md) for audio-only work, provider auditions and revoicing. Both share one audio helper; the narration skill does not require a browser or video input. Copy the complete plugin if using the scripts outside the marketplace. Audio requires Python 3.10+, FFmpeg and ffprobe. Browser capture additionally requires Node + Playwright and an installed browser. Google Gemini, OpenAI, ElevenLabs, OpenRouter and MiniMax use their respective API credentials. Technical tests default to silent output; local system speech requires explicit test opt-in. Other providers may supply WAV files.

Start with the [preferred Mac approach and ratings](skills/ui-walkthrough-video/references/preferred-approach.md) for the recommendation, pros/cons, narration status and evidence limits.

Source and fixture checks are in `VALIDATION.md`. The approved Kore audition was reused; these trials did not compare speech providers.

Version 1.2 includes a working polished capture/composition route and an existing-site
[example recipe](skills/ui-walkthrough-video/references/polished-example.md), with
Google Kore narration through OpenRouter. Camera planning remains explicit.

Version 1.3 separates cursor/camera animation at 60fps from source footage, adds
conservative auto-framing and loudness normalization, and documents effect priorities
and local/no-hosted-API routes. See the skill references for capability boundaries.

Version 1.4 adds [executed automation guidance](skills/ui-walkthrough-video/references/automation-trials.md)
for native recording, programmable composition, and later refinement.

Version 1.5 adds the separate narration skill and MiniMax speech support. MiniMax's
adapter passed offline contract and media-conversion tests; no live voice-quality
comparison was run. [MiniMax routing](skills/ui-walkthrough-video/references/minimax.md)
distinguishes Desktop Design, coding, hosted speech and generated assets.
