# Validation — 2026-09-05

- Actual two-beat synthetic interface capture in Microsoft Edge using bundled Playwright: passed. Button click revealed the expected detail panel; evidence screenshots checked.
- macOS Samantha narration: two WAVs, 2.822s and 3.360s. No paid API call or credentials used.
- FFmpeg assembly: 6.755s MP4, H.264 1440×900 at 30fps, AAC stereo 48kHz, mov_text captions. Full decode passed.
- Rendered frame contact sheet visually checked for both UI states. Audio non-silent: mean -18.9 dB, peak -5.2 dB. Perceptual voice audition and full playback listening remain unverified.
- Silent MP4, SRT, measured timeline and individual clips emitted. Caption timing is estimated.
- Eight unit tests cover caption continuity/overlap, timecode rollover, provider request contracts and output preservation. Skill frontmatter validator passed.
- Paid provider request construction tested offline; OpenAI/ElevenLabs connectivity, account voice access and perceived voice quality were not tested.
- Reproduction: run capture.mjs with assets/flow.example.mjs into a fresh directory, render.py voice, then render.py assemble. See SKILL.md. Runtime resolution can use PLAYWRIGHT_PACKAGE.
- Environment observations: the source project's old Playwright installation was incomplete; bundled Playwright worked. Sandboxed macOS say produced empty audio, caught by duration validation; authorized execution outside the sandbox succeeded.

Independent review fixes: preserved supplied subtitle cues through capture (then recaptured and assembled); failed takes retain diagnosis manifests; media child processes do not inherit provider keys; unknown voice fields are rejected before export; capture assertions are explicitly the flow author's responsibility.
