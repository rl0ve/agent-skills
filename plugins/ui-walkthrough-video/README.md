# UI Walkthrough Video

A shared Codex and Claude Code plugin for recording a real interface and assembling narrated demos.

Install from the rl0ve-agent-skills marketplace with `codex plugin add ui-walkthrough-video@rl0ve-agent-skills` or `claude plugin install ui-walkthrough-video@rl0ve-agent-skills`.

The standalone skill is `skills/ui-walkthrough-video`. Read its SKILL.md for the flow, voice prompt and test commands. Runtime requirements: Node + Playwright, an installed browser, Python 3.10+, FFmpeg and ffprobe. Google Gemini, OpenAI and ElevenLabs need their respective API keys. Technical tests default to silent output; local system speech requires explicit test opt-in. Other providers may supply WAV files.

Source and fixture checks are in `VALIDATION.md`. Paid provider quality was not auditioned for this release.
