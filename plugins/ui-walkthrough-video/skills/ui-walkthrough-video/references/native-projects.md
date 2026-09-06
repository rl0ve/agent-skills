# Editable native-project handoff

Reviewed 2026-09-06. Use this when a person wants to continue editing a walkthrough
in Cap Studio or Recordly, rather than only change code and render another MP4.

## Choose before capture

Offer **native project + source assets + MP4** alongside **MP4 only** when the delivery
preference is unknown. A short question is sufficient: “Would you like an editable
Cap/Recordly project plus the MP4, or just the finished video?” Reuse a known answer;
when editable output is already preferred, select that delivery without asking again.
This is a format choice, not an extra permission gate. Preserve clean sources while
an optional answer is pending; do not commit to irreversible flattening.

For an editable Mac demo, recommend **Cap Studio first**, **Recordly second**, and
**Custom when native editability is unnecessary or a required effect needs code**.
The first choice reflects documented editing breadth and a supported project/CLI
workflow. It is not a measured quality victory or proof that every editor control
is available to automation. Honor an explicit editor preference and verify the
installed version, access and required features before committing to the route.

## Editing comparison

| Capability | Cap Studio | Recordly | Implication |
|---|---|---|---|
| Zooms and cursor | Editable zoom track and recorded-cursor controls | Zoom regions/suggestions and cursor motion effects | Both suit screen-demo polish; preserve usable pointer metadata |
| Timeline and sound | Clip operations, transitions and separate audio lanes | Trims, speed regions and additional audio regions | Store narration in the native timeline |
| Advanced overlays | Separate mask/highlight and text tracks; beta captions and keyboard tracks | Text/image/figure annotations documented | Cap is the first candidate for a broader layered edit; equivalent Recordly tracks are not established by this review |
| Screen and camera | Multiple scene layouts, canvas controls and reusable presets | Frame styling, webcam controls and zoom-reactive webcam scaling | Pick the editor that fits the actual presentation |
| Extensions | No extension advantage established here | Documented extension system, including render hooks and styling | Recordly may win for a specific available extension; verify it |
| Saved project | `.cap` retains media and configuration | `.recordly` retains editor state and media references | Bundle all dependencies and verify reopening |
| Automation evidence here | Recording, config, trim and native export tested | Internal capture helper tested | Neither trial established a complete edited-project handoff with zooms, native narration and editable pointer motion |

Sources: [Cap Studio documentation](https://cap.so/docs/recording/studio-mode),
[Recordly features and project model](https://github.com/webadderallorg/Recordly#core-features).
“Not established” means missing evidence, not proof that a feature is absent.
Cap's tested window capture can include occluding windows; control foreground or use
a separately verified compatible capture path. Do not hide that constraint to favor it.

## Build the project, then export

1. Create a real native project through a supported interface or verified editor
   workflow. Do not rename an MP4 to a project extension or assume importing a
   flattened custom video reconstructs its editing layers.
2. Retain clean footage and valid cursor/click metadata if editable pointer motion or
   automatic action zooms are required. Browser automation does not necessarily move
   the OS cursor. Verify telemetry against actual actions; use supported capture or
   documented import when available. A browser-drawn arrow is baked into the video
   and must be disclosed as such. Do not fabricate native click evidence.
3. Put planned zooms into native zoom regions, preserving timing, focus and scale.
   Manual zoom regions can be useful without action metadata, but do not recreate
   independently editable cursor motion. Save trims, speed changes, layouts and
   supported titles/captions/masks as native editor objects.
4. Import approved narration as a separate native audio track, with its timing and
   source file retained. A soundtrack muxed only into the exported MP4 is not an
   editable narration handoff. Do not regenerate an approved voice unnecessarily.
5. Save before export. Produce the final MP4 from that saved project when possible.
   If extra finishing happens outside the editor, keep the editor export too and
   describe exactly which changes exist only in the final rendered version.

A basic native capture project and a fully edited project are different deliverables.
Report each requested layer as **editable**, **baked into video**, **not included**,
or **not verified**. Do not call the handoff complete when a requested layer is only
present in the MP4. An unsupported automated editor operation is a concrete gap:
use an authorized editor workflow where available, or deliver the safe partial work
and explain the unresolved requirement without silently changing the promised format.

## Package and verify

Deliver the `.cap` project or `.recordly` file with all referenced media, narration,
images and other dependencies, plus the MP4 and a short opening/editability note.
Use an editor-supported collection/export mechanism or verified relinking. Do not
assume a project file embeds its assets; avoid dependencies that exist only in a
temporary working directory. Include the editor version and any required extensions.

Verify the packaged copy, not just the original working directory:

- Open it in the target editor from the delivery location; resolve all media links.
- Inspect representative zoom regions, narration placement and other promised layers.
- On a duplicate, adjust one zoom or audio timing value, save/reopen and undo or
  discard the test. Confirm that it is an editor object, not merely rendered pixels.
- Export a short segment and check the actual frames and audio against the preview.

Record what was checked and any remaining limits. A valid JSON file, a ZIP archive
or a playable MP4 alone is not proof of an editable project. If editor reopening
cannot be verified, say so rather than reporting full handoff validation.

## Current trial boundary

The delivered Cap sample has native framing and trimming, but no populated zoom
track; its arrow is baked in and narration was added after export. The delivered
Recordly sample is a finished MP4, without a native project. They demonstrate
capture/assembly, not the complete handoff specified here. This guidance update
does not retrofit those examples or implement new native editor integrations.
