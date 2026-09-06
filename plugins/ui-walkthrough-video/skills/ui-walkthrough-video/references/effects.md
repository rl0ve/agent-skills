# Effects that improve a walkthrough

Reviewed 2026-09-05 against official product pages, documentation and repositories.
“Confirmed” means documented capability, not a successful integration or a comparative
rendering test. “Unconfirmed” is missing evidence, not proof the product cannot do it.

## Product capability map

| Effect family | Clueso | Recordly | DreamCut | HeyGen AI Studio |
|---|---|---|---|---|
| Cursor treatment | Size/color/animation; smoothing unconfirmed | Separate overlay, smoothing, motion blur, sway | Mouse-follow and custom movement | Cursor-aware editing unconfirmed |
| Click emphasis | Cursor highlights | Click bounce; extension effects | Click detection | Unconfirmed |
| Focus | Automatic/custom zoom and spotlight | Suggested/manual zoom regions | Automatic/editable zoom | Generic scene layout; cursor zoom unconfirmed |
| Remove wasted time | Dead-air/filler tools | Trim regions | Transcript-based gap/filler edits | Trim/split |
| Speed | Repetitive-region speed tools | Speed regions | General timeline edits | Semantic retiming unconfirmed |
| Transitions | Transition tools | Motion/timeline system | Zoom/slide presets | Scene composition |
| Explain a target | Spotlight/callouts/highlights | Text/image/shape annotations | Annotations | Text/motion graphics |
| Privacy masking | Sensitive-content blur | Core PII blur unconfirmed | Background blur; PII masking unconfirmed | Automatic PII masking unconfirmed |
| Captions | Styled/word-aware | Core captions unconfirmed | Timed and word animation | Styled word-synced |
| Speech/action sync | Word-to-frame sync points | Manual timeline/audio | Transcript/timeline editing | Avatar/script timing |
| Narration | Editable generated voice, pacing | Imported audio; mic/system tracks | TTS and voice tools | Generated voice and presenter |
| Audio repair | Voice workflow | Separate audio regions | Normalization/noise/Studio Sound | Voice editing workflow |
| Frame/brand | Brand assets and overlays | Background/padding/shadow/aspect | Canvas/camera presets | Brand/templates |
| Camera/presenter | Screen-demo focus | Webcam bubble | Camera layers | Generated avatars central |
| Localization | Multilingual voice/captions | Unconfirmed | Unconfirmed | Translation/revoice/lip-sync |

Sources:
[Clueso screen recorder](https://www.clueso.io/features/screen-recorder),
[Clueso official skills](https://github.com/clueso-ai/skills),
[Clueso sync points](https://help.clueso.io/sync-points/sync-point-basics/sync-point-basics),
[Recordly feature list](https://github.com/webadderallorg/Recordly),
[Recordly extension API](https://marketplace.recordly.dev/extensions),
[DreamCut](https://dreamcut.ai/),
[DreamCut features](https://dreamcut.ai/features),
[DreamCut support](https://dreamcut.ai/support),
[HeyGen screen recorder](https://help.heygen.com/en/articles/14251628-how-to-use-screen-recorder-in-ai-studio),
[HeyGen Studio](https://help.heygen.com/en/articles/11049655-overview-our-new-ai-studio),
[HeyGen translation](https://help.heygen.com/en/articles/10029081-how-to-get-started-with-video-translation).

Clueso's distinctive value is tying speech to screen actions. Recordly's strongest
local reference is cursor/camera rendering with editable telemetry. DreamCut combines
screen presentation with transcript/audio editing. HeyGen Studio primarily adds a
presenter and localization; importing a screen video does not establish cursor-aware
editing. HeyGen also publishes HyperFrames, a separate local composition framework;
do not confuse that project with its hosted avatar service.

DreamCut documents project-aware MCP editing, but a general supported rendering API
was not established. Its support and feature-log statements about external voice keys
conflict; verify the current installed plan and contract rather than assuming access.

## Automatic defaults: ordered by viewer value

These are editorial defaults, subject to a representative proof. They are not a
license to generate every effect in the product matrix.

| Priority | Default | Rule | Bundled-helper status in 1.3 |
|---|---|---|---|
| 1 | Legible UI and state continuity | Preserve task context, keep target/result visible, hold after meaningful changes | Capture assertions, framing and crop checks implemented; author verifies context |
| 2 | Smooth separate cursor | Sample motion at output frame rate; stable size, no trails, fade when idle | Implemented at 60fps from timed endpoints; actual hover updates at arrival |
| 3 | Restrained click pulse | Only actual recorded clicks; about 0.45s; no click sounds by default | Implemented |
| 4 | Selective focus zoom | One modest emphasis, usually 1.1–1.2×; camera settles before pointer moves; avoid repeated resets | Conservative automatic fallback for clustered targets; explicit keyframes override |
| 5 | Consistent audio level | Normalize loudness with peak headroom; preserve delivery and pace | FFmpeg loudnorm target -16 LUFS / -1.5 dBTP implemented; no automatic denoising |
| 6 | Readable captions | Short readable lines outside the UI; accurate timing; avoid covering controls | Scene-level captions implemented; word alignment remains separate |
| 7 | Remove true setup/dead air | Preserve loading/result evidence and reading time; never hide a failed action | Setup marker trim implemented; arbitrary silence/idle detection not implemented |
| 8 | Calm composition | Minimal padding/shadow, optional chapter title; maximize useful screen area | Implemented; no mandatory intro/outro |
| 9 | Simple edits | Cut between distinct beats; do not repeatedly zoom out then back in | Hard cuts implemented; automatic shot matching not implemented |

Automatic camera fallback inspects recorded target bounds after capture. It stays
wide for early actions, scroll events or dispersed targets; otherwise it ends a
1.15× zoom before the first pointer movement. This is a deterministic heuristic,
not semantic understanding. It intentionally declines many zoom opportunities.

A 60fps export does not turn a 25fps browser capture into 60fps app animation.
Separately composing cursor and camera motion removes their dependence on capture
cadence. Native recording at the intended output cadence is preferable for scrolling,
dragging, hover menus, kinetic interfaces and application animation. Do not interpolate
text-heavy footage with optical-flow warping merely to claim 60fps.

## Conditional effects

- **Spotlight, outline, arrow or callout:** use for a dense screen or subtle change;
  choose one emphasis mechanism at a time. Keep labels factual and anchored to a
  verified target. No bundled general callout/spotlight renderer yet.
- **Keyboard shortcut badge:** show when the shortcut itself teaches the task. Do not
  expose typed secrets or turn ordinary typing into distracting keystroke overlays.
- **Speed-up:** only boring waits/repetition, with explicit source-to-edit mapping.
  Preserve narration, the start/end states and any meaningful errors. Not implemented
  automatically in the helper.
- **Word highlighting:** needs real word timestamps, preferably forced alignment and
  review of names. Proportional timing is insufficient. For ordinary demos, calm
  phrase captions often compete less with the UI than karaoke animation.
- **Noise removal:** only audible noise in a recording; avoid degrading clean TTS.
  Background music is off unless useful and requested; duck it under speech.
- **Privacy blur:** mask known fields across their whole visible lifetime and inspect
  the export. Detection may flag risk, but must not certify privacy automatically.
- **Webcam/AI presenter:** useful for instructor presence or personal trust, not a
  default decoration. Avoid covering controls; generated avatars require an explicit
  choice and appropriate consent. No bundled avatar generation.
- **Translation/dubbing:** an explicit language deliverable with glossary and review;
  translating voice does not translate baked-in screen text.
- **Alternate aspect ratios:** reframe and recheck targets/captions; do not stretch
  footage or assume the desktop crop works vertically. Current helper is 16:10 only.

Avoid by default: cursor sway/bounce, sparkles, repeated punch-in zooms, 3D tilts,
large moving backgrounds, decorative slides, whoosh/click sounds and unrequested
avatars. Motion blur can soften a moving cursor, but should not compromise readable
screen text. These features can serve a promotional brief; they are not automatic
improvements to a procedural explanation.

## Quality proof

Review motion in playback, not only still frames. Include a long cursor traverse,
a real click, a content change, one focus move, and a scene join. Check both the
rendered cadence and the source cadence. Stop pursuing decorative polish when a
native editor can meet the brief sooner. Use [local-tools.md](local-tools.md) to choose
that route. Keep implemented effects, documented specialist capability and future
helper work separate in delivery notes.
