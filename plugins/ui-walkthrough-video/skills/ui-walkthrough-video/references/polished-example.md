# A tested polished capture path

Version 1.3 improves working motion and composition helpers. This is an explicit,
editable route toward Recordly/Clueso-style presentation, not an integration with
those products or a claim of feature parity.

## What the helpers actually do

- Record real Edge/browser interactions at 2880×1800 using a 1440×900 logical
  layout with 2× CSS zoom. Set `captureScale: 1` for sites incompatible with this
  temporary scaling. Device scale factor alone padded the tested recorder output.
- Render one eased cursor at 60fps, with a pulse at the actual recorded click. Pointer movement, click
  positions, target rectangles, scrolls and verification times are recorded.
- Insert a small pre-roll marker; locate its first stable exit in decoded video
  and trim setup footage. Preserve source-frame offsets in the edit timeline.
- Interpolate camera centers and zoom levels with a smooth curve, clamp the crop
  inside the recording, and check that click/pointer destinations remain visible.
- Compose a rounded UI frame, shadow, chapter label, restrained progress indicator,
  and balanced captions outside the UI. Narration starts after an explicit offset.
- Export the narrated MP4, silent revoice MP4, SRT, clips and measured timeline.

The compositor uses Pillow and FFmpeg, not Remotion. Cursor movement is rendered
from timed endpoints; the real browser mouse moves to the destination at arrival.
This does not reproduce intermediate hover effects. Use native capture when hover
paths, dragging or continuous app animation matter. The source recorder remains
25fps; output-frame cursor/camera interpolation does not change that source cadence.
Narration is level-normalized with peak headroom; clean TTS is not denoised. Capture and audio generation
remain separate, so revoice can reuse footage when the duration and action timings
still fit. When keyframes are omitted, a conservative target-bounds heuristic may add one small
zoom. It does not infer the semantically best camera path, align individual words, retime
actions semantically, remove arbitrary dead time, or supply an editing GUI.

## Reproduce the field-guide demonstration

Use the existing `plugins/ui-router/docs/field-guide.html` from the agent-skills
repository. The recording starts at its working Route a task section. No website
content or application logic is changed; temporary CSS scaling and a synchronization
marker are applied only to the recording session. The example is a real existing site, not a generated UI fixture.

1. Copy `assets/field-guide-narration.example.json` to a work directory. Choose and
   audition a voice first. Check the current speech model/voice catalog and existing
   secure credential helper. The demonstrated voice was Google Gemini 3.1 Flash TTS,
   Kore, accessed through OpenRouter. Do not infer direct Google key validity from
   successful OpenRouter generation.
2. Generate the narration into a new audio directory. If a shared helper is already
   configured, use it rather than copying credentials:

   ```sh
   ai-credentials run openrouter -- python3 /path/to/skill/scripts/render.py voice narration.json audio --allow-paid
   ```

   Use a Python runtime with a working CA trust store. Never disable certificate
   validation. `--allow-paid` indicates that the task/provider budget is authorized;
   it is not authorization by itself. Gemini through OpenRouter requires PCM in
   this tested route; the adapter wraps its 24 kHz mono PCM16 output in WAV.
3. Record the existing page with the example recipe. The flow measures the WAV files
   and adds breathing room, so it does not blindly reuse the original demo length.

   ```sh
   DEMO_URL=file:///absolute/path/agent-skills/plugins/ui-router/docs/field-guide.html \
   DEMO_AUDIO_DIR=/absolute/path/audio \
   DEMO_PLAN=/absolute/path/narration.json \
   PLAYWRIGHT_PACKAGE=/path/to/existing/package.json \
   node /path/to/skill/scripts/capture-polished.mjs /path/to/skill/assets/field-guide.flow.mjs capture
   ```

4. Compose the result. Pillow must be available to this Python runtime. `--font`
   accepts a local TTF path; the default is macOS Arial.

   ```sh
   python3 /path/to/skill/scripts/polish.py capture/manifest.json audio render --brand 'DESIGN ROUTER'
   ```

5. Review actual video frames at pointer arrivals, clicks, zoom extremes, scroll
   boundaries and cuts. Listen to the opening, joins and pronunciations. Show the
   playable example to the user; passing unit tests is not a substitute for this.

Native select popups vary by browser/capture backend. The example clicks the real
select, closes the transient native popup, uses Playwright `selectOption`, and asserts
the resulting value and page text. It does not fabricate a dropdown animation.

## Adapt it to another interface

Each beat supplies `setup(page)`, `perform({page, at, point, scroll, events})`, a
duration measured from narration, and optional camera keyframes `{time, zoom, cx, cy}`. Omit them for conservative
auto-framing; use `cursor: false` for a reading-only beat.
Camera centers use the logical viewport; capture converts them to source pixels.
Locator bounds, pointer telemetry and scroll offsets use the actual scaled viewport;
the example scales its scroll distances accordingly. `point`
rejects obscured/out-of-view targets and checks again before a real click. Scroll
explicitly and recalculate bounds; do not rely on a locator to silently scroll.

Start every beat with enough context to recognize the UI. End with the result
visible. Use zooms up to 2×; 1.2–1.5× is usually sufficient. Set action offsets to
match the actual narration and check them after regeneration. Scene-level captions
are the default; supply explicit timed cues when finer timing is needed.

The current canvas is 1600×1000 with a 1312×820 UI card. It expects a 16:10 capture.
Other aspect ratios require an explicit canvas/layout change, not a stretched UI.
This helper is for pages where direct automation is permitted. Use the host's
approved browser tools or a supported specialist for existing authenticated sessions.

The revised example holds its camera across the first join, uses gentler zooms,
and cuts to an already-scrolled detail shot for the final explanation. The final
scroll occurs during setup; it is not shown as an on-screen action. The narration
and two real selector changes are retained.
