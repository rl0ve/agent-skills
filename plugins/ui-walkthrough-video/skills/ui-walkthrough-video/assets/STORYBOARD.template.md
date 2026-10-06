# Walkthrough storyboard

Keep exact approved copy in SCRIPT.md. This document records editorial decisions;
storyboard.json is the executable timing contract. Change both when revising an edit.

- Audience and task:
- Treatment: tutorial / product demo / teaser
- HyperFrames choice: selected by the user / declined / awaiting choice
- Delivery: native editor project / HTML composition source / MP4
- Source identity, version and capture assertions:
- Output variants: landscape / portrait, each with its own storyboard.json
- Narration: accepted take IDs, measured lengths, alignment provenance
- Music/SFX: requested assets and gain/ducking choices, or none
- Brand: actual fonts, colors, logo files; reuse established product assets

| Scene | Global in/out | Source in/out | Visible action and observed result | Speech cue and audio offset | Canvas/focal rectangles | Cut from/to rectangles | Motion and reading hold |
| --- | --- | --- | --- | --- | --- | --- | --- |
| context | | | | | | | |
| action | | | | | | | |
| result | | | | | | | |

Source ranges map to the original footage. Global times map to the final edit.
Rectangles use [x, y, width, height] pixels, with the coordinate space named.
Storyboard cut rectangles are an editorial seam contract, not an automatically
generated transition. The bundled template hard-cuts scenes; custom match cuts
require authored seek-safe motion and snapshot review on both sides of the cut.

For speech-triggered highlights, record the aligned word index and observed source
rectangle. Highlighting a word does not retime the underlying UI action. Never imply
an action/result occurred earlier than the retained evidence shows.

For a teaser, pick the music and measure its beat grid before fixing visual cuts.
For a tutorial, prioritize speech, readable results and deliberate reading holds.
Do not impose a universal BPM or force all tutorial cuts onto the music beat.

## Review record

- Draft: first frame, motion midpoint, action/result, seam and final frame
- Random/backward seek comparison:
- Decoding, final duration, dimensions/FPS, black/frozen interval inspection:
- Captions, UI fidelity and privacy review:
- Full motion playback reviewer and findings:
- Loudness/true peak, names/numbers, audio joins, full listening reviewer:
- User changes and final acceptance:
- Packaged-source reopening/rerender check:
