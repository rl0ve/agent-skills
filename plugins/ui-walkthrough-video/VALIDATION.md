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

## Version 1.4.0

- Automatically recorded the same real Edge window with Cap 0.5.9 (bundled CLI
  0.1.0) and Recordly 1.3.3's bundled ScreenCaptureKit helper. Final native flow
  used focus/selectOption for two actual form values, asserted the results, and
  visibly scrolled the route. No microphone, camera, system audio or upload.
- Cap's supported CLI produced a valid editable project and a native framed export:
  H.264 1460×1000 at 60fps, 31.583s. Its requested 1600×1000 bounding box preserved
  capture aspect ratio. Export includes a silent AAC track. No native zoom/cursor
  editing was demonstrated.
- Recordly native raw MP4: H.264 2564×1760, 30.457s, variable cadence averaging
  about 57.03fps. This is internal-engine recording, not Recordly editor automation.
  All 1,738 source packet DTS values were ordered without duplicates. Full decoding
  passed with the demuxer time base; initial null-muxer timestamp warnings were
  output rounding rather than a demonstrated source defect.
- Rejected Cap take 1 because an occluding Codex window appeared despite a correct
  target ID. Foregrounding the dedicated Edge window fixed the capture. Rejected
  take 2 because a native select popup remained visible despite passing page-value
  assertions. Final take 3 avoided opening that popup. Reviewed action/result
  frames and fully decoded both final native outputs.
- HyperFrames 0.8.29 and Remotion 4.0.521 both produced actual narrated 1600×1000
  60fps H.264/AAC exports from the same real clips and approved Kore audio. Measured
  durations: 30.067s and 30.123s. Normal cursor, click pulses, camera, frame and
  scene captions were authored in each framework. Full decode and actual frame
  review passed. These are capability trials, not a general visual-quality benchmark.
- HyperFrames final check: zero lint/runtime/layout/motion findings, 15/15 text
  contrast checks passed. Single hardware-GPU worker completed in reported 39.2s;
  an initial concurrent/software-fallback render timed out. Remotion TypeScript
  check passed; an initial media-component render timed out, then the documented
  FFmpeg-backed component completed when run without the other renderer.
- Twelve repository release tests and skill frontmatter validation passed. No
  implementation code changed in this release; tested recipes and failure-based
  quality gates were the necessary plugin correction.

## Version 1.4.1

**Superseded Cap result:** later review found another Edge window in this take.
The early pointer checks below missed that contamination; see version 1.5.1.

- Corrected the cursorless native examples after user review. Both Cap and Recordly
  recorded a standard visible arrow driven by actual browser pointer events. Four
  paced movements led to the two selects and route headings; state changes and
  final scroll result were still asserted.
- Recorded 307 trusted pointer events with 302 distinct positions. Actual native
  frames showed different arrow positions during travel and the arrow at the
  intended selection/result targets. The arrow is baked into footage, not a native
  editor cursor layer. No additional narration or media API call.
- Added a visible-pointer quality gate and documented the corrected capture recipe.

## Version 1.4.2

- Documentation release: preferred Mac workflow, evidence-qualified ratings and
  explicit narration integration/audition status. No new speech model was installed
  or generated; no runtime implementation changed.
- Additional local examples: HyperFrames rendered an 18-second animated explainer;
  Remotion rendered two 16-second audience editions from one React composition and
  different input props. Actual frames, full decoding and browser playback were
  checked. These demonstrate workflow fit, not comparative quality superiority.
- The existing narrated helper example was rerendered with 0.4-second cursor moves
  and 0.6-second camera transitions after feedback that movement was too slow.
  Full decode and sampled frame checks passed; final MP4 is 30.088s, H.264
  1600×1000 at 60fps. Click/result telemetry was preserved and AAC packets matched
  the prior soundtrack. Revised viewer acceptance remains unverified.
- Cap-to-HyperFrames narration is a recommendation assembled from separate tested
  components, not a newly executed end-to-end pipeline.

## Version 1.5.0

- New voice-narration skill works with audio-only manifests and the shared helper;
  browser/video fields are not required. Existing video commands remain in place.
- MiniMax offline tests cover explicit request fields, unsupported options, text and
  speed limits, complete-response validation, malformed/error/empty audio rejection,
  preflight of the entire batch, missing credentials, paid-call authorization,
  metadata preservation after errors, no automatic retry and media-child key isolation.
- A mocked MiniMax HTTP response carried a locally generated MP3 tone through the
  complete voice command and real FFmpeg/ffprobe conversion into measured 48kHz
  stereo WAV. No speech model, paid API, voice clone or local model download was used.
- MiniMax voice quality and live-account access remain untested. Desktop Design,
  MiniMax Code, generated assets and official MCP integration are documentation-only
  routes; no installation or app automation was performed.
- Manual routing review: audio-only MiniMax uses the narration path; a silent UI proof
  does not generate speech; a Mac/offline request does not select CUDA or a hosted
  provider; named Desktop Design work does not imply API credentials; an existing
  OpenAI speech specialist remains usable. These are instruction reviews, not live
  trials of those applications or speech providers.
- Twenty-nine focused offline tests passed, including eight new MiniMax tests and
  the existing renderer/compositor tests. Both skill frontmatter checks and relative
  documentation-link checks passed.

## Version 1.5.1

- Rejected the wrong-window Cap take and rerecorded Cap/Recordly with a dedicated
  foreground window. Actual source comparison and final opening/action/scroll/ending
  frames now show the intended field guide. See the automation-trial correction for
  the 1,805 sampled-frame comparison and 44 resolved scroll-timing flags.
- Added the approved Kore soundtrack to both native exports with FFmpeg. Final
  H.264/AAC videos fully decoded and their audio packets matched the approved
  reference. This is not native editor voiceover automation.
- Simplified the local product-demo page to Custom, Cap and Recordly; framework
  showcases remain separate. Replaced the Cap project download with the correct take.
- Downgraded the Cap recommendation to conditional on controlled foreground
  recording, and strengthened whole-timeline content and narration checks.
- Edge playback verification passed for all three examples: playback advanced,
  AAC decoded, player was unmuted at nonzero volume, and three caption cues were
  available. Download paths resolved and the page fit a 390px viewport.
