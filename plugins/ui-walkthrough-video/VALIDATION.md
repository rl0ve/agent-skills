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

## Version 1.1.0

- Thirteen offline tests passed: Gemini request construction, PCM-to-WAV sample layout, invalid/empty/odd/truncated-response rejection, no implicit or unauthorized speech generation, provider-key isolation, and the existing caption/output tests.
- Silent render executed against the previously verified two-beat Edge capture: H.264 output produced with no audio stream. No system speech or paid provider was called for this revision.
- Google Gemini connectivity and perceptual voice quality remain untested. OpenAI, Gemini and ElevenLabs require a real listening audition before a quality claim.
- Current provider documentation and dated Artificial Analysis native-voice rankings informed selection guidance; no comparative audio benchmark was run.
- Clueso/Recordly/Remotion routing is documentation-based, not an executed integration or proof of visual parity. The included helpers remain basic capture/assembly.
- The v1.0 local-speech result above is historical engineering evidence, not an accepted narration choice. The new default is silent technical testing.

## Version 1.2.0

- Executed three real Edge beats against the existing Design Router field guide:
  changed Surface, changed Audience, then scrolled through the resulting route.
  Each changed value and resulting page text was asserted; screenshots and actual
  footage were reviewed. Native selects used a real click followed by selectOption.
- Generated three narration clips with Google Gemini 3.1 Flash TTS, Kore, through
  OpenRouter. The user approved the opening audition. This is not a provider
  comparison or a claim that the complete soundtrack received a listening review.
  Audio durations: 7.200s, 9.240s and 10.000s; measured peaks below clipping.
- Rendered eased cursor movement, actual click pulses, explicit camera zooms, a
  framed 1600×1000 canvas, chapter labels, progress, and scene-level captions below
  the UI. The 30fps edit is planned at 30.033s (MP4 duration 30.055s), with 0.5s narration lead-in per beat and space
  after speech. Exported narrated/silent MP4s, SRT and measured source offsets.
- Capture used a 2880×1800 viewport with temporary 2× CSS zoom. Device scale factor
  alone produced padded output on this backend and was rejected. Encoder startup
  and tail buffers were added after a cold recording failed duration validation.
- Nineteen focused offline tests and twelve repository tests passed. JavaScript
  syntax and skill-frontmatter checks passed. Full final FFmpeg decode passed.
- Actual frame review checked opening/ending states, selector zooms, cursor targets,
  scroll result, caption placement and framing. The example demonstrates the
  implemented effects, not Clueso/Recordly parity. Automatic camera decisions,
  word alignment, semantic action retiming and an editing GUI remain unavailable.
- A portable narration plan and capture recipe ship with the skill. Credentials,
  private browser state, failed takes and personal paths are not packaged.

## Version 1.3.0

- Reused the previously approved Gemini Kore audio; no new TTS API call. This sample
  is locally recaptured/composited but is not a demonstration of local TTS generation.
- Recaptured the two real selector changes without a baked-in cursor. The reading
  scene is established after scrolling during setup, then recorded; the edit does
  not show or imply an on-screen scroll action in that beat.
- Browser source cadence is 25fps. Cursor/camera composition is independently 60fps;
  continuous app animation remains limited by the source. Actual browser hover is
  updated on pointer arrival; the smooth path is composited from timed endpoints.
- A 0.7s constant-camera cursor traverse produced 42 video frames and 42 unique frame
  hashes, confirming output-frame motion rather than repeated 25fps pointer frames.
- Twenty-one focused tests passed, including continuous cursor interpolation and
  conservative camera fallback. JavaScript syntax/frontmatter checks passed.
- Gentler camera paths replace repeated zoom resets. Idle pointers fade. Narration
  uses loudness normalization with peak headroom; no denoising or speech retiming.
- Product/local-tool assessment is based on official documentation and source, not
  comparative rendered output. Local TTS candidates have not been auditioned here.
  Native Recordly capture was not tested because Screen Recording permission was
  missing; no permission setting was changed.
- Final MP4: 30.088s, H.264 1600×1000 at 60fps, AAC; full decode passed.
  Reviewed actual frames from all three scenes. Final measured true peak -2.12 dBTP.
  Twelve repository tests also passed (33 tests total). Perceptual motion acceptance
  remains the user's decision; no native-editor head-to-head trial was completed.
