---
name: ui-walkthrough-video
description: Produce narrated UI walkthrough videos by navigating a real interface, recording scene clips and screenshots, and assembling synchronized voiceover, captions, and a silent revoice version. Use for product demos, tutorials, and portfolio walkthroughs.
---

# UI walkthrough video

Turn an observed UI flow into a reproducible recording and a clear narrated demo.
The working unit is a short **beat**: one visible action or result and its narration.
Do not substitute a slideshow or simulated UI for real navigation without saying so.

## Choose the result

Infer audience, flow, approximate length, aspect ratio and browser from the request
and project. Ask only for consequential missing choices. Default to a concise demo
of one complete task with readable UI at 1440×900 or 1920×1080. Respect the user's
browser preference; the example uses Edge in a fresh automation profile.

Offer this voice prompt when no preference is known:

> What voice quality should I target: a free local draft, a polished natural voice,
> or a premium voice audition? You can give a range such as “polished to premium,
> up to $2,” or name a provider, model, voice, language, accent and speaking style.

Treat these as subjective targets, not guaranteed model rankings. For a range,
select within the budget and audition the same 10–15 second excerpt before a full
paid generation. Existing user choices persist. If awaiting a choice, continue
storyboarding and capture; use a clearly labeled local draft only for testing.
Read [voice.md](references/voice.md) for provider choices and secure key setup.

## Build and capture

1. Inspect the actual interface and implementation or accessibility tree. Write a
   brief scene plan: starting state → action → observed result → narration. Explain
   the user's benefit; avoid narrating every click or making unverified claims.
2. Use a demo/fixture environment for actions that change data. A recording request
   alone does not authorize production approvals, sends, resets or submissions.
   Record authentication state only in ignored local files. Use synthetic data or
   mask private fields **throughout the recording**, not just in screenshots.
3. Copy [the example flow](assets/flow.example.mjs) into the project and replace
   its fixture steps with observed selectors. Split long scenes into short beats.
   Each beat declares an ID and narration and implements `run(page)` with assertions
   on the observable result. The runner trusts these assertions; it cannot infer
   whether an arbitrary click achieved the intended result. Prefer role/name or stable test IDs; assert the resulting
   state before taking a screenshot. A click alone is not success. Wait on states;
   reserve fixed waits for deliberate reading time, not application readiness.
4. Use a supported browser tool to explore an existing authenticated UI. For a
   local app or fixture where direct Playwright automation is allowed, use the
   included capture runner. Do not bypass host browser restrictions. If capture
   tooling exposes snapshots only, label the output as a snapshot walkthrough.
5. Record each beat separately and save evidence screenshots. Flush video by
   closing its context before obtaining the file. Reuse a context between beats
   only by adapting the runner deliberately; the included runner isolates them,
   so each beat establishes its own starting state. Never reset shared data as an
   implicit setup step.

## Render

Requirements: Node with Playwright, Python 3.10+, FFmpeg/ffprobe on PATH, and the
chosen installed browser. Use project dependencies when present; do not silently
install large browser/runtime packages. No paid API is needed for the local test.

```sh
# Run in a fresh output directory. Paths may be absolute.
node /path/to/skill/scripts/capture.mjs ./flow.mjs ./capture
python3 /path/to/skill/scripts/render.py voice ./capture/manifest.json ./audio
python3 /path/to/skill/scripts/render.py assemble ./capture/manifest.json ./audio ./render
```

`PLAYWRIGHT_PACKAGE` may point to an existing project's `package.json` to resolve
Playwright without another install. `FFMPEG` and `FFPROBE` may override executable
names. Commands refuse existing output directories; use a new take for revisions.
Read [manifest.md](references/manifest.md) for supplied audio, explicit subtitles,
and custom capture backends. Change only narration/voice and reuse capture when
revoicing; changed UI actions require recapture.

The renderer retains the complete clip and narration, padding whichever is shorter.
It never silently truncates an action or speeds up speech. Large mismatches are QA
warnings: shorten the copy, remove dead time with explicit cuts, split the beat or
recapture. This preserves evidence but is not automatic semantic synchronization.
To tightly align “click,” “opens,” and “result,” use separate beats or edit explicit
visual cue points. Do not imply that proportional captions are word-aligned.

## Quality gate and delivery

Run a 2–3 beat proof before a long recording. Inspect screenshots and actual video
at scene boundaries; listen to the audition and at least the opening, names, numbers
and transitions. Check readable UI, unclipped text, correct state, cursor/callout
placement, narration timing, pauses, voice consistency and absence of private data.
Use natural-writing's spoken guidance if available, without making it a dependency.

Deliver `walkthrough.mp4`, `silent.mp4`, `captions.srt`, `timeline.json`, individual
clips, screenshots, narration audio and the editable manifest/flow. The MP4 has
selectable captions; the SRT can also accompany the silent revoice version. For
burned captions, inspect FFmpeg filter support first; if libass is absent, use
transparent browser-rendered text overlays or an available composition tool.

Report tested providers and capture backend, technical checks, human/agent playback
review and remaining limitations separately. Label local drafts, synthetic fixtures,
AI-generated narration and estimated captions. Do not call paid voice quality tested
when only API mocks or local speech ran. Publishing is a separate requested action.

Read [sources.md](references/sources.md) only when choosing complementary tools such
as Remotion, speech providers or browser recording skills.
