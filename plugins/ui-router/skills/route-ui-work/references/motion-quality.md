# Verify an interactive experience

Use for substantial custom motion, scroll choreography, canvas or WebGL, or a reported
motion/performance defect. The selected specialist owns implementation; this reference
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
