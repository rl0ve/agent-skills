# Capturing a native desktop app you do not control

Executed 2026-09-14 on Apple Silicon macOS against a desktop editor with an embedded
web panel and a deployed browser application. The rest of this package assumes either
a browser you drive with Playwright or a recorder with its own CLI. Neither applies
when the subject is somebody's installed application, on their machine, in the state
they have it in. These are the mechanics that decided whether a take was usable.

## Accessibility input does not actuate content; HID events do

`osascript` / System Events `click at {x, y}` returns the accessibility path of the
element under those coordinates, which reads exactly like success. It is not a click.
On the target's embedded web panel a disclosure row stayed closed after repeated
attempts; on a browser page a link reported hit did not navigate. It also never moves
the OS cursor, so nothing about it appears in the recording.

Posting real events through `CGEvent(... .cghidEventTap)` actuated both surfaces on the
first attempt and put a visible moving cursor in the capture. Compile
[assets/hid-pointer.swift](../assets/hid-pointer.swift) with the `swiftc` that ships
with the Command Line Tools; no package install is involved. The same program is the
only reason cursor movement exists in this route, so treat it as capture equipment
rather than a convenience.

Keyboard input through System Events **does** work on the application's own chrome:
menus, a command palette, an address bar. So navigate by keyboard and point with HID
events. Keyboard navigation has a second advantage — it lands on whatever window is
actually frontmost, with no window handle to get wrong.

Coordinates are global points, top-left origin. Displays here reported "UI looks like
2560x1440" at 1x, so points equalled the pixels in a `screencapture` still; on a Retina
panel they are half. Two displays were mirrored, and captures returned different pixel
dimensions depending on which was the target, which silently invalidated a first set of
computed coordinates. Read the geometry, convert once, and verify by clicking something
harmless before the recorder is running.

## Browser connectors can be attached to a different browser than the one on screen

A browser-extension connector reported navigating a tab while the window visible on
screen stayed where it was. It was attached to a second Chromium browser, and both had
the same page open under different profiles, so every symptom pointed at bad
coordinates instead. Before trusting any connector for capture, confirm which process
owns the window you are recording — on macOS, ask System Events which process has a
window with that title — and be aware that a signed-in profile and a signed-out one
render different banners in the same app.

`activate` is not a window selector, and this cost a take on its own. Two windows of
the same browser were open on different profiles; the app came forward with the
signed-out one, whose page carried a "not signed in" notice the accepted footage did
not have. Nothing in the script could see that. So capture a still and check for the
state you expect — a profile chip, an account name, the absence of a sign-in prompt —
before the recorder starts, and prefer a host with a single window of the target app.
When only the operator knows which window is the right one, have them front it and say
so, rather than resolving it programmatically.

## `screencapture -v`: give it a duration, never a signal

Two takes were destroyed by stopping the recorder. `SIGINT` did not stop it; the
following `SIGTERM` killed it before it finalised, and no file was written at all — the
recording only appears on disk when the process ends on its own terms.

Use the built-in limit and let it finish:

```sh
screencapture -v -V 46 -T 0 take.mov   # 46 seconds, no delay, writes on its own
```

Verify the contract on the host with a 5 second capture before a real take. Size the
window generously: an over-long take costs disk, a truncated one costs the performance.
The cursor is recorded by default, which is what makes the HID route above visible.

A capture script launched as a detached child of a short-lived wrapper was killed when
the wrapper exited. Run the capture script **as** the tracked background process, not as
something it spawns in the background.

## The operator is the main hazard

Every lost take in this session came from focus, not framing. Twice the person watching
typed into a chat window and pulled it into frame mid-take; once a macOS automation
consent dialog opened in the centre of the screen. None of that is visible to the
script driving the capture.

- Activate the target application immediately before the recorder starts, not merely
  before the sequence.
- State the hands-off window as a number of seconds and include the recorder's own
  duration in it.
- Do any permission-triggering work well before recording. An unrelated automation
  request can raise a consent dialog seconds later, over the subject.

## Scan the take; do not watch it

Reviewing by eye missed a foreign window that a scan found immediately. Pick one frame
you have confirmed shows the subject, then diff a small downscaled crop of every frame
against it and flag anything above a threshold:

```sh
ffmpeg -v error -i take.mov -vf "fps=2,crop=600:400:0:0,scale=200:-1" scan/s%03d.jpg
# then, per frame: mean absolute difference against a known-good reference frame
```

On one 60 second take this returned `5.0 … 7.5` — a two and a half second intrusion in
the middle of otherwise clean footage, which is not something a reviewer reliably
notices. The same scan on the rebuilt clip returned nothing, which is the evidence that
the repair worked. Run the same check with known scene boundaries excluded on the
assembled cut to catch unintended jumps.

A crop is enough and is much cheaper than whole frames; choose a region the subject
always occupies, such as the top-left chrome.

Expect false positives and read them before acting. A run that flagged three seconds
of one take had found the tooltip raised by the script's own hover, not an intrusion.
The flag is a prompt to look at that frame, not a verdict: open it, and only then
decide whether the take is damaged. A scan that flags nothing is the useful signal; a
scan that flags something means inspect, because the same threshold catches your own
hovers, menus, and any transient the product itself draws.

## Fit the picture to accepted audio, not the reverse

Narration that a person has approved is the fixed quantity. Measure each file, then
stretch or compress only the picture:

```
setpts=PTS*(audio_seconds/video_seconds)
```

Cursor-only motion tolerated roughly 1.3x of slowdown here without reading as
sluggish; past that it looks like the machine is struggling. So capture 30 to 50 percent
more than the narration needs, and expect to lose some of it — after cutting an
intrusion out of a 28 second span there were 25 seconds left to cover 34 seconds of
speech, which was the whole slack budget.

When a section must get shorter, splice the accepted take inside its own pauses before
resynthesising it: one beat lost 17 seconds that way with no audible seam and no change
of delivery.

## Every pointer move needs a word attached to it

The strongest note from the reviewed production was about motion, not mechanics: a
cursor that visits things the narration never mentions reads as nervous, and the
viewer starts watching the pointer instead of the screen. Stillness is a choice you
are allowed to make. Through an opening that names nothing on screen, the right
number of moves is zero.

So schedule the path from the audio rather than from a stopwatch. Silence-detect the
accepted narration to get phrase boundaries, write down which phrase names which
region, and start each move a fraction before its phrase so the pointer arrives as the
words land:

```sh
ffmpeg -hide_banner -i beat.wav -af "silencedetect=n=-38dB:d=0.28" -f null /dev/null
```

Then drive the moves against a monotonic clock seeded once at the recorder's start, not
a chain of `sleep` calls, or the path drifts out of sync with the words by the end of a
thirty second beat.

Two consequences worth planning for. The path is only correct for the script it was
timed against, so a rewritten line means a re-timed take — cheap if the sequence is a
script, expensive if a person is holding the mouse. And because the moves now sit on
the phrases, the footage should not need retiming to fit the audio, which removes the
slowdown discussed above and its ceiling.

The same rule governs a cursor drawn in post: give it one gesture on the phrase that
earns it. A circling pass over two regions was cut from the reviewed production because
nothing in that stretch of narration distinguished the two; it became a single sweep
across the whole diagram on the words "the whole process drawn out".

## Do not pan or zoom a still to fake motion

A slow `zoompan` over a captured still was the one artifact a reviewer called glitchy.
`zoompan` resolves its crop to whole pixels per frame, so a gentle ramp pumps: measured
against the same source, the zoom produced a mean frame-to-frame luma change of 0.2362
with spikes to 1.67, against 0.0007 and 0.1150 for the identical shot held static.

Hold the still instead. A static application window is what a recording of a static
application window looks like, and it costs nothing. Measure before believing either
result:

```sh
ffmpeg -v error -i shot.mp4 -t 10 -vf scale=480:-1 -pix_fmt gray -f rawvideo -
# then: mean absolute difference between consecutive frames
```

## Overlaying a cursor in post

Where no real cursor could be driven, an overlay of a cursor sprite along a timed path
served the narration honestly, as long as it is disclosed as a non-native layer the same
way a baked arrow is elsewhere in this package. `overlay` accepts expressions of `t` for
`x` and `y`, so an ellipse around a region and a move to the next one need no
compositor.

One trap specific to building this on a still frame: the still already contains the
operator's real cursor, so the result shows two. Find it — a small cluster of dark
pixels — and paste a clean patch of neighbouring background over it before rendering.

## Boundaries

This is a capture route for an application in someone else's hands, not a claim about
any recorder's editing features, and it produces a flattened MP4 rather than an
editable project. Nothing here was tested on Windows or Linux, or on a machine where
the recording window is not the main display. `screencapture` behaviour, display
geometry and consent prompts are all OS-version dependent; re-verify with a short take
on every new host.
