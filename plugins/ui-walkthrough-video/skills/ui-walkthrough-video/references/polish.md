# Polished screen demos

Aim for intentional attention guidance, not constant camera movement. Match a short
representative sample to the requested reference before recording a long flow.

## Beat sheet

For each beat record: actual UI start/result, target selector and rectangle, action
and completion times, narration phrase/action word, cursor journey, camera framing,
cut points, and expected screenshot. Capture these from the real interaction; do
not invent evidence. Keep raw source-time and final edit-time mappings separate.

- Cursor: one deliberate path to a target, eased arrival, brief dwell and restrained
  click feedback. Keep tip inside actual target bounds. Avoid teleports between
  continuous shots and remove idle wiggle. Keep original cursor hidden if adding
  a rendered cursor, so there is never a doubled pointer.
- Camera: establish full context, ease toward the relevant control/result, hold long
  enough to read, then restore context before the next task. One useful move per
  beat usually suffices. Keep labels and result text within frame; avoid overshoot.
- Editing: remove dead time only between verified states; never cut away the result
  used to substantiate narration. Use clean cuts for UI continuity and restrained
  transitions for scene changes. Preserve source-to-edit time mapping after cuts.
- Narration: generate coherent phrases (not one TTS call per click), then use actual
  word timestamps or reviewed sync points. Pin emphasis to an action word and the
  actual action/result. Recalculate camera/caption timing after revoice or cuts.
- Review: inspect cursor tip, target framing, zoom extrema and cut boundaries. Listen
  to opening, joins, names and numbers; reject robotic prosody or unnatural acting.
  Export a short sample first. Record remaining defects rather than averaging them
  into an overall quality score.

## Available routes

Clueso: inspect current official `polish-screen-demo`, `revoice-video` and (for
stills only) `screenshots-to-walkthrough`. Its MCP documents automatic recording,
voiceovers, synchronization points, animated elements and export. Verify actual
connected tools, account entitlements and costs. Skill files alone do not grant
service access. Preserve original audio or import approved narration when supported;
do not silently replace a preferred Google voice with a service default.

Recordly: its actual editor supports cursor telemetry, zooms, styling and exports.
Use the supported app workflow when available. Its internal smoke-test export is
not a supported production CLI. Source is AGPL-3.0; inspect obligations before reuse.

Remotion: use the official skills when constructing a programmable composition.
It needs explicit cursor/camera/sync data and editorial decisions; installing it
alone does not polish a recording. Verify runtime licensing for the user's context.

Dreamcut: a relevant visual/editor reference; no tested integration is bundled here.
The fallback FFmpeg assembler is explicitly basic. Do not represent any of these
external routes as installed, exercised or benchmarked unless actually verified.

## Implemented local route

Version 1.2 implements an explicit capture/composition path with cursor motion, click
pulses, camera easing, a rounded frame and external captions. See
[the reproducible example](polished-example.md). This supplements the specialist
routes above; it is not a Clueso or Recordly integration.

For the detailed product effect map, defaults and implementation gaps, read
[effects.md](effects.md). For offline/local alternatives, including HyperFrames,
Cap, Recordly and local speech models, read [local-tools.md](local-tools.md).
