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

The quality target is natural narration and deliberate, polished screen-demo motion.
Robotic delivery is a failed result, regardless of price or benchmark rank. Do not
fall back to macOS/browser system speech when a key is missing. Use a silent technical
proof while awaiting a voice choice or credentials.

Offer this prompt when preferences are unknown:

> Should I start with your preferred natural voice, or audition two or three current
> candidates? You can specify a provider/model/voice, or a range such as “natural to
> studio-quality, under $2,” plus language and delivery style.

Honor known voice choices. Include Google Gemini TTS when Google is preferred;
Kore is a useful explicit example, not proof of naturalness or a universal best voice.
Audition the same 10–20 second passage, including a product name, number and transition.
Reject flat prosody, metallic artifacts, exaggerated acting/accent, and audible joins.
Never call an unheard sample natural. Read [voice.md](references/voice.md) and, when
selecting current models, [benchmarks.md](references/benchmarks.md).

## Choose the production route

Read [effects.md](references/effects.md) for ranked automatic effects and conditional
treatments. Read [local-tools.md](references/local-tools.md) when hosted media APIs
are unwanted or agent-operated local tools are preferred.

Read [polish.md](references/polish.md) when the target resembles Recordly, Clueso,
Dreamcut or Screen Studio. Prefer an available, authorized specialist that can meet
the requested visual quality. Clueso's official skills/MCP are a close documented
fit. Recordly is an editor/capture route; do not rely on its internal smoke-export
hook as a supported headless API. Remotion is a programmable composition option.

The basic `capture.mjs` / `render.py` route remains available. Version 1.3 provides a
working polished route: `capture-polished.mjs` records clean footage, pointer endpoints,
clicks and scroll events; `polish.py` renders the cursor/camera at 60fps, a presentation
frame and captions outside the UI. Read [polished-example.md](references/polished-example.md)
for the tested existing-site recipe. A conservative automatic zoom is available when keyframes are omitted;
camera direction and action timing still need editorial review. Native source footage
may remain 25fps; 60fps composition smooths the cursor/camera, not app animation.
Neither route performs word-level forced alignment or proves
parity with an editing product.
If specialist tools are unavailable, preserve footage and a concrete edit plan,
report the missing capability, and continue only the portions the available tools
can perform. Do not quietly downgrade a requested polished final into raw footage.

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
chosen installed browser. The optional polished compositor also needs Pillow. Use project dependencies when present; do not silently
install large browser/runtime packages. No paid API is needed for a silent capture test. Before asking for a key, follow any
existing global credential-helper or secret-manager instructions. On a configured
host, `ai-credentials status` reports availability without exposing values; use
`ai-credentials run <provider> -- ...` for the synthesis process. Stored is not the
same as authenticated or authorized for generation.

```sh
# Run in a fresh output directory. Paths may be absolute.
node /path/to/skill/scripts/capture.mjs ./flow.mjs ./capture
# Silent technical proof: no robotic placeholder narration.
python3 /path/to/skill/scripts/render.py silent ./capture/manifest.json ./silent-proof
# After voice selection, audition and budget authorization:
python3 /path/to/skill/scripts/render.py voice ./capture/manifest.json ./audio --allow-paid
python3 /path/to/skill/scripts/render.py assemble ./capture/manifest.json ./audio ./render
```

`PLAYWRIGHT_PACKAGE` may point to an existing project's `package.json` to resolve
Playwright without another install. `FFMPEG` and `FFPROBE` may override executable
names. Commands refuse existing output directories; use a new take for revisions.
Read [manifest.md](references/manifest.md) for supplied audio, explicit subtitles,
and custom capture backends. Change only narration/voice and reuse capture when
revoicing; changed UI actions require recapture.

The basic renderer retains the complete clip and narration, padding whichever is shorter.
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
clips, screenshots, narration audio and the editable manifest/flow. The basic MP4 has
selectable captions; the polished MP4 burns captions into the presentation canvas.
The polished silent version retains those visible captions; edit the cues and rerender
when revoicing with changed wording. The SRT is also exported separately. For
burned captions, inspect FFmpeg filter support first; if libass is absent, use
transparent browser-rendered text overlays or an available composition tool.

Show a playable short example when asked for quality proof, using a real existing
site if the target app is unavailable. State which visible effects were actually
rendered, and which capabilities remain guidance or future work.

Report tested providers and capture backend, technical checks, human/agent playback
review and remaining limitations separately. Label silent technical proofs, synthetic fixtures,
AI-generated narration and estimated captions. Do not call paid voice quality tested
when only API mocks or local speech ran. Publishing is a separate requested action.

Read [sources.md](references/sources.md) only when choosing complementary tools such
as Remotion, speech providers or browser recording skills.
