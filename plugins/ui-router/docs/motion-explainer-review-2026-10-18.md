# Motion-explainer craft review: October 18, 2026

Decision behind UI Router 1.19.5 and the UI Walkthrough Video 1.7.2 handoff. A
conceptual explanation can have useful content and still miss its motion reference
when every beat is authored as a finished slide plus entrance effects. The missing
decision is visual direction across time, not necessarily a rendering engine.

Public source and instruction review only. No candidate was installed, rendered or
benchmarked for this release. The reusable guidance is independently written; no
third-party skill, prompt, template, media or private reference file is bundled.

## Sources and decisions

| Source | Evidence checked | Decision |
| --- | --- | --- |
| [Official HyperFrames creative skill](https://github.com/heygen-com/hyperframes/tree/main/skills/hyperframes-creative) and [animation skill](https://github.com/heygen-com/hyperframes/tree/main/skills/hyperframes-animation) | Creative entrypoint plus house-style, video-composition and beat-direction references; animation entrypoint and core dependency. Covers type hierarchy, composition, beat concepts, concrete motion verbs, scene handoffs, motion recipes and deterministic timelines. Repository license is Apache-2.0. | **Conditional lead** for authored HTML/video. Load complete selected workflows and required references. Apply requested reference and teaching needs before promotional defaults. |
| [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | SKILL.md, aesthetic-rules.md, README, gallery structure, repository metadata and its entry in [Remotion's own resources](https://www.remotion.dev/docs/resources). Recipe cards include camera, typography, transitions, rhythm and data shots with implementations. Source code/docs are Apache-2.0; bundled audio has separate per-file terms, and Remotion has its own license. | **Conditional craft lead** for a Remotion product film or recipe-based composition. Prefer the original repository to forks. Teaching pace, asset choice and user scope override promo defaults. |
| [Official Remotion skills](https://www.remotion.dev/docs/ai/skills) | Framework-maintained implementation workflow; distinct from the community shotcraft art-direction method. | **Supporting implementation** for a selected Remotion project; not proof that a default render has cinematic direction. |
| [HyperFrames Motion Director](https://github.com/geekjourneyx/hyperframes-motion-director) | Entry point, anti-PPT section, workflow, license and metadata. Explicit camera/type/transition planning and midpoint review; defaults to Chinese vertical promos, requires a proposal-confirmation phase, and is AGPL-3.0. | **Reference only**, not a default install or copied dependency. Its scope, workflow and licensing need deliberate evaluation for a project. No blanket language, format, approval or scoring rules imported. |
| [Rob Sobers' first-person maker report](https://www.linkedin.com/posts/rsobers_ive-been-playing-around-with-motion-design-activity-7513591523603595264-zYoe), indexed October 7, 2026 | Reports Claude Code with HyperFrames and official Remotion skills, a storyboard contact sheet and critique before rendering. Public post retrieved directly. | **Method corroboration**, not a reproduced result, comparative benchmark or industry-adoption survey. Contact sheets support composition review; playback remains necessary. |
| [Claude Motion documentation](https://support.claude.com/en/articles/17454997-get-started-with-claude-motion) | Official product documentation distinguishes code-based motion artifacts from generated footage. | **Product identity check**. Do not equate Claude Motion with Motion.dev or infer that a supplied artifact used Remotion. |

## Dated adoption signals

GitHub's public API reported 12,382 stars / 1,114 forks for video-shotcraft,
66,631 / 6,032 for HyperFrames, and 462 / 47 for HyperFrames Motion Director on
October 18. Remotion's resource list independently links video-shotcraft. These
are ecosystem/discovery signals, not install counts, specific-skill usage, output
quality or industry market share. Exact recipe counts differ between indexes and
the current repository; no count is made a routing requirement.

Observed default-branch revisions:

- `heygen-com/hyperframes`: `b46ebedeae959d3060ca4ece244ea6861d0f2352`.
- `Vincentwei1021/video-shotcraft`: `43bd349a136651865ecfa6ea1cf012f6e957d304`.
- `geekjourneyx/hyperframes-motion-director`: `0b66750322ccb50ae56ace5a8d361da2c1f65400`.

The official creative references also include opinionated defaults: technical
subjects on dark canvases, font restrictions, multiple focal points, ambient motion
and prescribed effect diversity. Those are not universal teaching requirements.
Preserve the user's reference, correct semantics and deliberate stillness. More
decoration, camera movement or music does not automatically improve comprehension.

## Smallest reusable change

- UI Router gains a `motion-explainer` surface and one focused reference with
  craft/engine separation, a beat contract, a representative moving proof and
  separate content, aesthetic, audio and technical checks.
- The walkthrough skill routes conceptual films to that direction and keeps
  observed capture ownership for mixed productions. Its optional HyperFrames path
  now names creative and animation skills when those concerns are in scope.
- No bulk installation, new rendering helper, required paid service, universal
  style prescription or extra standing approval step is added.

## Validation and limits

[Policy cases](../tests/motion-explainer-cases.md) cover the applicable route and
nearby non-triggers. They are a written decision review, not an executed multi-model
evaluation. Package/version parity, local Markdown targets/anchors and existing
video-helper tests validate packaging and compatibility; they do not measure film
quality. A future production should compare the same content in a representative
moving sequence before claiming improved polish or parity with a named product.

Revisit tool preference after an actual comparable production, material upstream
workflow/license changes, or demonstrated gaps in composition and choreography.
