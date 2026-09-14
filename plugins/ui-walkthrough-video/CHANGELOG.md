# Changelog

## 1.5.4 — 2026-09-14

- Add a route for capturing an installed desktop application on the user's own machine, with the executed mechanics: accessibility clicks report success without actuating embedded web content or moving the OS cursor, real HID events do both, and a compilable pointer program ships as an asset.
- Record the recorder contract: `screencapture -v` writes only when it ends on its own, so pass `-V seconds`; two takes were destroyed by signalling it. A capture script must be the tracked process, not a detached child.
- Require every pointer move to sit on a phrase that names what it points at: schedule the path from silence-detected narration timings against a monotonic clock, and treat stillness as a choice. A move with no verbal cue reads as nervous and pulls attention to the pointer.
- Do not pan or zoom a captured still. `zoompan` resolves its crop to whole pixels, so a gentle ramp pumps: measured 0.2362 mean frame-to-frame luma change against 0.0007 for the same shot held static.
- Record that `activate` is not a window selector: with two windows of one browser on different profiles, the app fronted the signed-out one and its page carried a notice the accepted footage did not. Verify the expected state in a still before recording.
- Add programmatic take review: diff a downscaled crop of every frame against a confirmed reference frame to locate foreign windows, and scan the assembled cut for unintended jumps. A two-and-a-half-second intrusion that eye review missed was found this way.
- Record the operator as the main hazard to a take, with the mitigations: activate the target immediately before the recorder starts, state the hands-off window, and clear permission prompts beforehand.
- Document fitting the picture to accepted narration with a `setpts` ratio, the roughly 1.3x slowdown ceiling for cursor-only motion, and the resulting capture headroom.
- Record Algenib as an accepted single-narrator direct-Gemini profile, with the pace and the constant delivery instruction that let re-synthesised lines splice against earlier takes.
- State plainly that every prebuilt voice on the model is selectable: the voice names in this package are dated listening results, not a supported subset, and none of them is a default.

## 1.5.3 — 2026-09-13

- Record Algieba + Sulafat as an accepted direct-Gemini, male-presenting two-host profile and Kore as an accepted female-presenting Southern-style product-demo voice through OpenRouter.
- Separate Gemini voice availability from provider-route capabilities: shared voice names do not prove matching prompt, multi-speaker, format, quota or catalog behavior.
- Add the observed long-form limitation: split two-speaker production at natural one-to-three-minute exchanges and verify speaker continuity.

## 1.5.2 — 2026-09-06

- Offer native project + source assets + MP4 before capture; reuse an established editable-project preference.
- Rank Cap Studio first for documented editing breadth and Recordly second, with an editing matrix directly in the README.
- Require native zoom/audio/layer preservation, packaged-project reopening and edit checks; distinguish this target from the limited existing trials.

## 1.5.1 — 2026-09-06

- Put the preference, quality evidence and pros/cons matrices directly in the README, including Mac narration status.
- Correct the Cap trial record: later frames showed an occluding Edge window, missed by earlier review.
- Document the fresh foreground-controlled take, matched narration in both native examples, and stronger content/audio verification.
- Make the Cap recommendation conditional on foreground control and keep framework showcases separate from the product-demo page.

## 1.5.0 — 2026-09-06

- Add a separate voice-narration skill for provider selection, auditions, audio-only output and revoicing, sharing the existing audio helper.
- Add MiniMax synchronous speech support with explicit model/voice, validated hex MP3 responses, prior paid-call authorization and no automatic retries.
- Distinguish MiniMax Desktop Design, coding, generated assets and speech API routes; retain real capture evidence and untested quality labels.
- Move provider guidance under the narration skill, preserve existing links, and document complementary OpenAI speech and natural-writing skills.

## 1.4.2 — 2026-09-06

- Add the preferred Mac workflow, qualitative fit/quality assessment, pros/cons and explicit trial boundaries.
- Separate established Kore narration from unintegrated, unauditioned Chatterbox/Kokoro candidates; exclude the NVIDIA route from the Mac default.
- Document shorter cursor/camera timing and the remaining viewer-acceptance and combined-pipeline checks.

## 1.4.1 — 2026-09-06

- Require a visible standard pointer for mouse-driven demos unless cursorless output is requested.
- Record the tested browser-pointer overlay repair for Cap/Recordly and distinguish baked footage from editable native cursor layers.

## 1.4.0 — 2026-09-06

- Record actual HyperFrames and Remotion composition trials, including working configurations, timed-out attempts, camera bounds and reuse limits.
- Document executed Cap CLI capture/config/export and Recordly bundled-engine recording, keeping supported interfaces distinct from experimental internals.
- Add automatic-work routing across browser navigation, native capture, composition, and refinement of existing videos; preserve editable sources and a normal cursor option.
- Require recorded-pixel checks for window occlusion, persistent native menus and real pointer telemetry; successful page assertions or a valid capture project alone are insufficient.

## 1.3.0 — 2026-09-05

- Separate cursor rendering from 25fps browser capture and animate cursor/camera at 60fps; fade idle pointers and retain real click timestamps.
- Reduce repeated zoom resets and competing motion in the existing-site example; add a conservative target-bounds camera fallback and loudness normalization.
- Assess screen-editor/presenter effects, automatic versus conditional defaults, local tools, local TTS, and HeyGen HyperFrames as distinct from hosted avatars.
- Preserve the source-cadence limitation and actual hover-at-arrival behavior; do not claim native 60fps app animation or product parity.

## 1.2.0 — 2026-09-05

- Add real 2× capture with eased cursor movement, actual click pulses and timestamped targets, plus a Pillow/FFmpeg compositor for explicit camera zooms, framing and captions.
- Add a reproducible demonstration using the existing Design Router Field Guide and user-auditioned Gemini Kore narration.
- Add OpenRouter speech support, including the live-confirmed Gemini PCM requirement, secure shared-credential discovery, partial-take voice metadata and response-format validation.
- Require playable examples for quality claims and keep manual camera planning/scene-level captions distinct from automatic editing and word alignment.

## 1.1.0 — 2026-09-05

- Add Google Gemini TTS/Kore support, natural-voice audition gates, silent technical tests and explicit-only local test speech.
- Add dated benchmark evidence and polished production routing for Clueso, Recordly and Remotion; distinguish basic capture from demonstrated visual quality.


## 1.0.0 — 2026-09-05

- Real UI capture by beat, screenshots, configurable voice quality/provider/model, secure environment credentials, captions and silent revoice output.
- Measured media timing, non-destructive takes, explicit supplied captions, and synthetic fixture for reproducible smoke testing.
