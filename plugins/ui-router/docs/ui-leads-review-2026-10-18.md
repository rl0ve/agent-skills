# UI leads review: October 18, 2026

Record behind UI Router 1.19.4. The [three.js builder review](threejs-builders-review-2026-10-18.md)
kept two of Meng To's links out of `route-3d-work` because landing-page and explainer
work belongs to `route-ui-work`. This review evaluates them for `route-ui-work`. The
posts are leads. Every fact below was checked in the upstream repository, its
package metadata or its source on October 18. Nothing was installed, run or rendered.

| Lead | Decision | Checked upstream | Edit |
| --- | --- | --- | --- |
| [Shaders](https://github.com/shader-effects-inc/shaders), shared by [Meng, Oct 10](https://x.com/MengTo/status/2108924473265275003) | **Conditional** | The `shaders` npm package (4.0.4, on npm since June 2025, source open since September 29) is MIT. The editor, presets, sections, Framer plugin and unwatermarked rendering have separate platform terms, and presets and sections need Pro. `gpu/support.ts`: WebGPU only. When WebGPU is unavailable it leaves a transparent canvas, stays silent in the console and reports through `isWebGPUSupported` and `onError`. `telemetry/`: samples 5% of visitors (preview components always report) and sends frame timing, component names, domain, browser family and device type to shaders.com. `disableTelemetry` turns it off, and Do Not Track is honored. A code search found no reduced-motion handling. | Section in `visual-resources.md`; named beside Canvas UI in `SKILL.md`. |
| [Anatomy](https://github.com/wheresryan22/anatomy), shared by [Meng, Oct 11](https://x.com/MengTo/status/2109182449179836579) | **Conditional** | MIT, no runtime dependencies, Node 20.10+, Chrome for its own checks, React 18+ only for React output. It outputs standalone HTML, a lone SVG or React/Next.js components. WebGL layers are optional and the SVG reads without them. Figures stay still under reduced motion. It does not do charts, people or maps, a session is long, and 3D mode is beta. Gallery submission opens a pull request after the user agrees. | Opt-in entry in `optional-skills.json` (no profile), a catalog row, a section in `visual-resources.md` and the `SKILL.md` bullet. |
| [ThreeUI](https://x.com/MengTo/status/2103155074705019158) | **Already covered** | Community and Pro routes already exist. | None. |

## Overlap

- **Canvas UI** already covered "a specific GPU effect" (MIT with Commons Clause, a WebGL
  path, copied in through a registry). Shaders has the plainer license and wider
  framework coverage but no WebGL path, so Canvas UI stays the choice when WebGL is required.
- Nothing in the catalog drew explanatory figures. HyperFrames still owns exported
  explainer video, and charts stay with the chart route.

## Not adopted

- Shaders' own skill as a global install. It triggers on any GPU visual and advises
  against adding three.js, which conflicts with projects that already render with it.
  It is installed through `npx shaders connect` only when the user wants editor sync.
- `npx shaders install-mcp`, which edits several clients' configuration. Not needed
  for the free component route.
- Anatomy's 3D mode (beta): reference only.

## Revisit when

Shaders gains a WebGL fallback or changes its telemetry default, Anatomy's 3D mode
leaves beta, or a project trial gives evidence about either in use.

## Check

Policy cases are in [reference-steering-cases.md](../tests/reference-steering-cases.md).
After the edit, a fresh read-only subagent (Claude Sonnet, Claude Code) read only the
skill files, not the cases or this review, and answered four briefs. It made the
expected picks on all four:

- **Svelte gradient hero:** Shaders with a fallback underneath, real Safari and
  Firefox checks, reduced motion supplied and a telemetry decision. It looked at
  Canvas UI first because the owner named those browsers.
- **Bloom on an existing three.js scene:** kept the scene's renderer and sent the work
  to the 3D route rather than Shaders.
- **Connection-pool docs figure:** Anatomy under the docs lead, with real pool numbers
  and the readouts checked.
- **Revenue chart:** neither resource.

After its notes, the wording now asks for the user's approval before either install,
a WebGPU check in the target browsers, and states that Anatomy figures respond to
pointer and keyboard. Its other notes were left alone. Chart coverage and when a
listening review may stay pending are outside these leads. This is a policy
walkthrough, not a build, device trial or benchmark.
