# Automatic capture and composition trials

Tested September 5–6, 2026 on Apple Silicon macOS, using the same Design Router
field-guide task: choose a Surface, choose an Audience, and read the resulting route.
These are executed capability trials, not a general visual-quality benchmark.

## Route by the work that must run automatically

- **A fresh browser walkthrough:** automate observed, asserted actions in a dedicated
  browser context. Capture and compose are separate steps; a renderer does not operate
  the product merely because it can animate a video of it.
- **Native recording with an editable project:** prefer Cap's supported CLI when the
  installed contract meets the task. Validate actual pixels before trusting a window ID.
- **Repeatable authored edits:** use HyperFrames for HTML/CSS/GSAP composition or
  Remotion for a React timeline. Preserve real footage, narration, timed action evidence,
  captions and source. Prompt-driven changes still require code/render verification.
- **Recordly specifically requested:** its tested bundled capture engine is an
  experimental option. This does not establish automatic control of its editor.
- **Refining an existing video:** inspect its audio, dimensions and available sources;
  preserve the original and edit a derivative. Reuse a Cap project or composition
  source when present. A flattened MP4 does not retain editable cursor/camera layers.

For browser-agent navigation plus recording, use an authorized browser driver and
a separate capture backend. Clean footage plus actual timed pointer targets can be
composited with a standard arrow; the result need not show the agent tool's cursor
indicator. Inspect the captured footage first for any baked-in pointer and never
overlay a second cursor. Smooth interpolation between real targets is a visual
treatment; retain actual click times and do not imply intermediate hover states.

The included Pillow/FFmpeg route remains the smallest existing dependency path for
this skill. Do not automatically migrate a working video to another framework unless
its editing, reuse or rendering capabilities help the requested result.

## Cap: supported CLI, editable project

Observed installation: Cap desktop 0.5.9, bundled CLI 0.1.0. Discover the current
installed command contract with `--help`; do not assume those versions on another host.
On this Mac the CLI was available inside the app even though `cap` was absent from PATH:
`/Applications/Cap.app/Contents/MacOS/cap-cli`.

Executed lifecycle (substitute discovered IDs and new output paths):

```sh
cap doctor --json
cap targets windows --json
cap record start --window WINDOW_ID --mode studio --fps 60 --path take.cap --detach --json
# Run the authorized UI actions and assert each result.
cap record stop --path take.cap --json
cap project validate take.cap --json
cap project config get take.cap --json
# Modify a complete copy of the actual config, passing JSON as one structured argument.
cap project config set take.cap --settings-json FULL_CONFIG_JSON --json
cap export take.cap --output edited.mp4 --fps 60 --resolution 1600x1000 --quality maximum --json
```

Retain start/stop results, require `recordingMetaExists: true`, validate the project,
and inspect actual exported frames at every action boundary. Preserve the entire
`.cap` directory for later editor refinement. Use subprocess argument arrays for JSON;
never interpolate configuration text into a shell command. Unspecified config settings
may reset to defaults, so read and modify the full current configuration.

**Observed capture failure:** a valid project created with the correct Edge window ID
contained Codex pixels while the requested window was occluded. Foregrounding the task's
Edge window was required for the repeat. A target ID, process success or project
validation alone does not prove correct content. Inspect a short test before a long take,
keep the intended window unobscured, and stop/retry if another app contaminates footage.

Playwright's browser pointer is not necessarily the OS cursor tracked by native capture.
The trial hid the cursor rather than showing unrelated desktop pointer motion. Do not
claim automatic cursor smoothing or click zooms from this trial. Use a real supported
OS pointer route or separately verified pointer telemetry if those effects are needed.
Native selects also exposed a second failure: page value assertions passed while an
OS popup remained visible. The final trial focused each real select and used Playwright
`selectOption` to change it without opening a native popup. This is programmatic control
of the real form, not proof of OS mouse interaction. If showing the native menu is
required, use a supported OS interaction route and inspect its dismissal in footage.
No microphone, camera, system audio, upload, cloud AI or sharing was used.

## Recordly: actual native engine, experimental integration

Observed installation: Recordly 1.3.3. Its bundled macOS executable was:
`/Applications/Recordly.app/Contents/Resources/app.asar.unpacked/electron/native/bin/darwin-arm64/recordly-screencapturekit-helper`.
The installed `electron/native/ScreenCaptureKitRecorder.swift` defined this contract:

```json
{"windowId": 1234, "fps": 60, "outputPath": "/absolute/new-take.mp4", "capturesSystemAudio": false, "capturesMicrophone": false}
```

Pass that object as the first JSON argument in an argv array, wait for stdout
`Recording started`, execute the authorized flow, then send `stop\n` to stdin and
wait for a successful process exit. The example window ID is a placeholder; discover
its live value. Ensure stop runs during failure cleanup too. Do not copy app source
into this plugin; recheck the installed protocol and licensing before adapting it.

The tested installed engine isolated the selected window and hid the OS cursor. Its
raw H.264 recording had variable frame timing despite a requested maximum of 60fps.
Full decoding with the demuxer time base passed. A default null-output check initially
reported timestamp warnings caused by rounding to its output time base; the final
source had no duplicate or decreasing packet DTS. Use
`ffmpeg -v error -i raw.mp4 -enc_time_base demux -fps_mode passthrough -f null -`
to preserve that timing during a decoder check. Never label requested FPS as measured FPS.

This is proof of automatic recording through Recordly's shipped native component.
It is **not** a supported public CLI, a Recordly editor project, automatic editing,
zoom suggestions or export through the Recordly editor. Protocol paths and behavior
are version-dependent. Treat failures as a reason to use the supported app workflow
or another capture backend, not to invent hidden production APIs.

## HyperFrames and Remotion: actual composition exports

Both rendered the same three clean UI clips and previously approved narration with
a normal arrow, timed click pulses, camera movement, chapter text and captions.
The 25fps UI source was trimmed once; both composed their overlays at 60fps.
Captions remained scene-level. Small easing/typography differences are expected;
these are comparable authored examples, not a pixel-identical benchmark.

- **HyperFrames 0.8.29 / GSAP 3.14.2:** HTML/CSS with a registered paused timeline,
  separately timed video/audio elements, and a clamped camera inside a clipping
  frame. Final H.264/AAC: 1600×1000, 60fps, 30.067s. The successful single-worker
  hardware-GPU run reported 39.2s render time on this host. Initial parallel-worker
  execution fell back to software after a GPU probe timeout and later hit its
  FFmpeg encode watchdog. Do not generalize the successful time into a benchmark.
- **Remotion 4.0.521:** React composition, `Sequence`, `useCurrentFrame`,
  `OffthreadVideo` and `Html5Audio`. Final H.264/AAC: 1600×1000, 60fps, 30.123s.
  Initial `@remotion/media` Video execution timed out at a frame while the two
  renderers ran concurrently. The successful attempt used the documented
  FFmpeg-backed video component and sequential rendering. The trial does not
  isolate which change resolved the timeout.

Successful commands, in their respective prepared projects:

```sh
# Node 24.12.0 was used; HyperFrames requires Node >=22.
npm run check
npx --yes hyperframes@0.8.29 render --fps 60 --quality high --workers 1 --browser-gpu --output walkthrough.mp4

# Remotion: pin dependencies and register the composition before rendering.
npx remotion render src/index.ts DesignRouter walkthrough.mp4 --codec h264 --concurrency 4 --timeout 120000 --browser-executable /path/to/installed/browser
```

Run a representative still before a full render. Clamp camera translation to the
scaled footage edges; a valid zoom value can otherwise expose empty borders.
Set absolute pointer/pulse origins explicitly before applying transforms. Mark
intentional clipped camera overflow only after visual inspection, not to hide a
layout defect. Final HyperFrames lint/runtime/layout/motion checks had no findings;
all 15 text contrast checks passed. Remotion TypeScript checks passed. Both final
videos fully decoded and actual action/boundary/ending frames were inspected.

These frameworks automate rendering of an authored plan. They do not themselves
establish automatic recording, semantic zoom selection or word-level alignment.
Keep source projects and media for later agent edits. A raw MP4 alone is less
editable than the source, and neither trial generated a new voice.

## Shared verification

Keep capture, composition and editor automation as separate reported outcomes.
Compare equivalent content and show playable artifacts. State whether a sample is a
native raw take, a native edited export or a programmatically authored composition.
Reuse approved narration for comparisons instead of buying new synthesis for every
renderer. Inspect beginning, action, result and ending frames; check full decoding,
duration, audio presence and caption timing. Absence of decoder failure is not a
visual review or a listening audition.

Sources: [Cap agent interface](https://cap.so/docs/agents),
[Recordly source](https://github.com/webadderallorg/Recordly),
[HyperFrames](https://github.com/heygen-com/hyperframes),
[Remotion rendering](https://www.remotion.dev/docs/render).
