# Verify an interactive experience

Use for substantial custom motion, scroll choreography, canvas, WebGL, sound/media
interactions, or a reported motion/performance defect. The selected specialist owns implementation; this reference
adds completion evidence, not another lead or a mandatory animation stack. For a small
transition change, check the affected behavior and relevant reduced-motion state.

## Keep the experience usable

- Make the first readable frame and primary controls usable without waiting for an
  introductory sequence. Provide meaningful content when decorative graphics fail.
- Give each interaction an appropriate keyboard and touch path. Translate an essential
  hover, drag or cursor action into focus, tap, explicit steps or another equivalent
  action when needed. Test native vertical scrolling alongside touch gestures.
- Preserve text semantics when splitting animated letters or words. Ensure assistive
  technology receives the intended phrase once, and reduced motion retains its meaning.
- Give each animated property one owner at a time. Avoid competing CSS, animation
  library and render-loop writes; deliberate handoffs should release the previous
  owner. Add a smooth-scroll engine only when needed and avoid competing scroll owners.
- For transformed scenes with tools such as a loupe or selection overlay, decide which
  coordinate space owns each layer. Check pointer alignment under the actual transforms
  before choosing a scene child or an independent overlay. Ordinary layouts do not
  need scene architecture.

## Bound work over time

- Suspend unnecessary continuous effects when offscreen or the document is hidden;
  resume without duplicate loops or a large simulation jump. Account for CSS and
  pseudo-element animations as well as JavaScript and renderer loops.
- Clean up listeners, observers, timers, animation instances and graphics resources
  when the surface unmounts or is replaced. Handle late asynchronous loads too.
- Choose resolution, pixel ratio, particles, shadows and other quality costs against
  the target device and viewport. Use a simpler treatment where needed while preserving
  the chosen character and task. Do not copy a demo's quality constants as universal
  budgets or assume coarse pointer alone measures device capability.

## Sound and media when the task uses them

Apply this section to a player, lesson, soundscape or other experience in which audio
or video is part of the task. A silent decorative page does not need an audio system.

- Establish the sound-starting gesture and the intended quiet state. Keep Play, Pause,
  Continue, Stop and Mute behavior distinct where those actions are offered. Do not
  assume that opening a page authorizes autoplay or microphone capture.
- Keep the relevant controls reachable during the main activity. For use away from a
  desk or with occupied hands, test readable controls in the intended orientation and
  provide a usable touch/keyboard path alongside optional voice or gesture controls.
- When several views represent the same media, agree on one playback clock. Verify
  position, rate, looping and synchronized highlights/captions through seeks and view
  changes. Muting should preserve position unless the product specifies otherwise.
  Check that independent sound layers mute and restore according to their labels.
- Exercise loading, repeated Play, cancellation, blocked playback, permission denial,
  media replacement, leaving and returning. Prevent late loads or recognition results
  from restarting a session after Stop or navigation. State whether resume is manual
  or automatic rather than leaving different controls to decide independently.
- Keep essential spoken guidance available as text, and captions/transcripts when
  applicable. Label their availability and source; do not fabricate missing lyrics,
  transcripts, scores or synchronized note data under an authentic recording's title.
- Voice input is optional when offered: explain activation and browser/service use,
  show when it is listening, provide an immediate off control and define its lifecycle.
  Feature detection or a simulated recognizer does not prove recognition on a device
  while music is playing. Separate command recognition from performance assessment.
- Inspect the actual source and permitted use of selected media. A working embed,
  embeddability metadata, source identity and instructional accuracy are different
  claims. If the source is blocked, expose recovery without substituting unrelated
  content or silently switching versions, arrangements or clocks.

Choose a representative journey such as entry → intentional playback → change view
or passage → mute and restore → leave and return. Inspect appearance and audible/state
behavior separately. Record device, browser, input method and the limits of observation;
a captured promo or desktop viewport test does not establish real-tablet audio or voice.

## Observe the relevant states

For a performance change, record a baseline and compare the same viewport, content and
interaction before and after. Exercise visible, offscreen, hidden, resumed and repeated
entry/exit states when relevant. Check the page's top, middle and end for scroll-driven
work, plus a relevant touch viewport. Verify no unintended horizontal overflow and
that intended vertical scrolling still works; do not use clipping to conceal a defect.

Use appropriate browser or renderer measurements for the actual work. A host-page
requestAnimationFrame FPS counter does not prove an embedded renderer's frame rate or
GPU cost. Stable screenshots, a successful build or unavailable heap measurements do
not prove smoothness or absence of leaks. Report the tested environment, observed
changes and limits; source inspection alone remains source inspection.
