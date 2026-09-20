# Quick screenshots and recordings

Use for a quick look at an existing site or interface. A few useful screenshots or a
brief silent recording may be the entire deliverable. Reuse the user's browser and
scope; do not introduce narration, an editor, new dependencies or a format questionnaire
unless they help meet an explicit requirement. Preserve requested native editability
when a video is required; an old production preference does not expand a screenshot task.

## Check the source and capture route

1. Confirm the intended URL and state. For a local preview, make a fresh navigation or
   safe reload and confirm the page actually loads; an already-open page can remain
   visible after its server has stopped. Preserve unsaved state, using a separate tab
   when appropriate. An HTTP response alone does not establish rendered page health.
   If the preview is unavailable, use its documented startup only within the authorized
   scope and verify the destination again. Do not restart unrelated services or switch
   to production to make the capture work.
2. For video, inspect the available recorder's supported interface and discover the
   exact target window. Before promising a recording, verify that the target can be
   captured with a scoped still or short test. Inspect those pixels; a window ID and
   successful process do not establish correct content. Follow the existing
   [occlusion and recording checks](automation-trials.md#cap-supported-cli-editable-project).
3. An empty window list is an observed capability failure, not proof of a specific
   permissions problem. Use relevant read-only diagnostics if available; retry only
   when evidence or state changes justify it. Do not automatically broaden capture to
   the whole display, grant permissions, bypass host restrictions or use an internal
   recorder engine. Report the limit and follow the host's authorization rules.
4. If the user asked for screenshots **or** a quick video, deliver useful screenshots
   when recording is unavailable. If video is required, label screenshots as partial
   evidence and explain the blocker. Never present a slideshow as a recording of motion.

## Save and inspect the result

- Use the current viewport unless a requested responsive view or breakpoint needs an
  override. Record the dimensions and restore temporary overrides after capture.
- Inspect the screenshot's bytes or decoder-reported format before assigning its
  extension and MIME type. A screenshot API may return JPEG without a format option;
  saving those bytes as `.png` does not convert them. Use `.jpg` for JPEG, `.png` for
  PNG, and the corresponding extension for other detected formats. Verify that the
  saved file decodes and inspect it for missing content, errors and private material.
- Capture sections when sticky or scroll-driven content makes a full-page image
  misleading. Stills establish appearance; they do not establish animation timing.
- Save artifacts locally to the task's output folder, identify the captured page and
  viewport, and show screenshots inline when the host supports it. A capture manifest
  is useful for a collection, but not mandatory for one image. Report a video only
  after checking the actual exported file and representative playback frames.

## Evidence and policy cases

A September 20, 2026 local-site capture observed three separate facts: the original
page remained visible while a new navigation failed to connect; screenshot bytes
were JPEG despite an initial `.png` filename; and Cap window discovery returned an
empty list. The recording failure's cause was not established. No successful video
capture or permissions repair is inferred from that run.

Manual policy review cases, not automated recorder trials:

| Case | Expected result |
|---|---|
| User accepts screenshots or video; recorder returns no windows | Deliver verified screenshots, disclose that no video was recorded, avoid a prolonged recorder setup. |
| User specifically requests a video or editable video project | Screenshots remain partial; report the missing recording capability without calling the request complete. |
| JPEG bytes arrive from the browser screenshot API | Save with `.jpg` and `image/jpeg`; decode and inspect the artifact. |
| PNG bytes arrive from another capture backend | Retain `.png` and `image/png`; no unnecessary conversion. |
| Open local page remains visible but fresh navigation fails | Treat the runtime as unavailable until an authorized startup and fresh load succeed. |
| Page contains unsaved work | Preserve it; verify in a separate tab rather than discarding it to reload. |
| User requests a polished narrated walkthrough | Use the main production workflow, including its requested editing and audio requirements. |
