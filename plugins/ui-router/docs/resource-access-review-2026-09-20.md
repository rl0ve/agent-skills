# Resource access review — 2026-09-20

This review corrects resource selection and setup assumptions. It is not a benchmark
of generated design quality, an adoption mandate, or evidence that a retrieved
component works in a destination project. Account details and local credentials are
excluded from the shared repository.

| Source and observation | Decision |
|---|---|
| [21st plans](https://21st.dev/plans) and [CLI/MCP guide](https://21st.dev/mcp) include free component search and limited code retrieval. The official `@21st-dev/cli` 1.17.1 reported a free tier, two daily retrievals and hosted AI disabled. | Correct the older map's implication that MCP/CLI search requires membership. Check current account capabilities before promising a paid operation. |
| An authenticated CLI search returned public carousel candidates. One retrieval of [Circular Carousel](https://21st.dev/@nexus-ui/components/circular-carousel) returned component/demo source and reduced the free allowance from two to one. | Search, authenticated source retrieval and remaining quota were exercised. Compilation, accessibility, visual quality and destination integration were not tested. |
| [Motion AI Kit installation](https://motion.dev/docs/ai-kit-install) documents a free hosted documentation server and separate Motion+ access. The official `motion-ai` 14.1.0 package identifies [upstream revision 1140efe](https://github.com/motiondivision/ai-kit/tree/1140efe9ad5e03c689ea6bb19d9d3850a4dae5f7). | Route to the complete selected official specialist and current hosted integration; do not recreate its detailed craft in UI Router. |
| The free Motion server completed initialization without credentials and exposed `search-motion-docs`. A React carousel query returned documentation and premium-example metadata; `resources/read` resolved the documentation. | Account-free documentation access was exercised. Premium source, MotionScore audits and an interactive transition editor were not verified. |
| The reviewed Motion skill describes `generate-css-easing` as free, but the live free server did not expose it; the public install guide places CSS spring generation under Motion+. | Use current tool and entitlement evidence for availability. Do not promise a tool merely because a skill or installer lists it. Preserve the upstream skill rather than silently rewriting its advertised tiers locally. |

The focused checks support free-first setup, explicit cost categories and accurate
capability reporting. They do not establish that all account tiers, paid features or
future upstream versions behave identically. Recheck the selected path when used.

Manual policy cases are in [resource-access-cases.md](../tests/resource-access-cases.md).

## Conditional shortlist follow-up

The resource map already covers Dream Loop, Codrops, Layers, AI Elements, Toolcraft
and HyperFrames; the catalog includes Addy Osmani's Web Quality Skills. These remain
selected task resources, not mandatory installations or subscriptions.

The [Rive state-machine guide](https://rive.app/docs/editor/state-machine/state-machine)
and [plan guide](https://rive.app/docs/account-admin/pricing) support a route for
app-driven animated assets, with free editor work distinct from runtime export.
[DiffUI's site](https://diffui.ai/) and [pricing](https://diffui.ai/pricing) support
an optional visual-direction comparison, with paid generation distinct from beta
code conversion. Neither product was behaviorally or comparatively tested here.

The complete Meng playable-testing skill at upstream revision
`5f47e389dac337a1bca5cddf376419248b3010f6` was reviewed alongside the four 3D
specialists. Its precise entrypoint now complements the existing spatial routes.

Manual selection checks: an event-driven learning character can select Rive; a
settled button transition does not. An unresolved visual direction can justify a
bounded DiffUI comparison; a specified spacing fix does not. Playable save/retry
regressions can select Meng's testing workflow; a static scene does not require a
gameplay matrix. These are policy checks, not independent agent or runtime trials.
