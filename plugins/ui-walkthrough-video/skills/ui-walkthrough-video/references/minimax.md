# Where MiniMax fits

Reviewed 2026-09-06. MiniMax is a model/provider and application family. Keep its
coding agent, creative studio, speech and generated video capabilities distinct.

| Need | MiniMax role | Boundary |
|---|---|---|
| Narration for an actual UI recording | MiniMax Speech is an alternative to the existing voice provider | Use the sibling `voice-narration` skill. The shared helper has an offline-tested adapter; no live audition or quality win is established. |
| Images, ambient clips or illustrative footage | MiniMax/Hailuo generation can supply optional assets | Generated footage is not evidence that the real app performed an action. Label illustrative sequences and preserve captured UI for the walkthrough. |
| A creative website with coordinated visual/audio assets | MiniMax Code or Design is an integrated workflow candidate | This belongs with the user's coding/design workflow. Do not switch agent, install an app or move a project merely because this video skill is active. |
| Exact text, timing, captions, cursor paths and reusable video layouts | Supply generated assets to a compositor if useful | HyperFrames/Remotion and native capture still have distinct jobs. The presence of a generative model does not prove exact editor control. |

For an ordinary walkthrough, retain the [preferred capture/composition approach](preferred-approach.md)
and consider MiniMax at the narration or optional-asset step. For a media-rich website,
its integrated workflow is worth evaluating separately; this plugin does not claim
a MiniMax Code or Design integration, or demonstrated cost savings over another agent.

## Desktop Design or API?

Use **Desktop Design** when the desired result is a creative project managed in that
application: brief, generated assets, revisions and delivery. Inspect the actual
available app and controls; this plugin does not automate it. Use **the API or a
connected MCP** when MiniMax supplies a specific step inside the current workflow,
such as one narration track or an illustrative clip. For this plugin's narration,
the API is the implemented route.

Honor the user's named surface. If they ask to work in Desktop Design, do not turn
that into API setup; if they ask to add MiniMax narration to an existing walkthrough,
do not require a desktop-app installation. Account access, credits and billing may
differ; verify them for the chosen route. Neither route implies offline generation.

## Integration choices

Prefer an already connected official MiniMax tool when it meets the job. Its MCP
exposes speech and voice tools plus image/video generation; inspect the loaded tool
contract and available account before use. An upstream MCP existing is not evidence
that it is installed, enabled, authenticated or callable in this session.

The bundled fallback implements synchronous MiniMax speech through the global HTTP
endpoint. It does not implement the creative desktop app, video generation, cloning,
voice design, streaming or provider timestamps. Advanced operations may use an
available supported tool under the user's authorization, with separate verification.
The shared credential helper may support other providers without supporting MiniMax;
check its actual provider list instead of modifying global credentials implicitly.

Hosted API generation works from a Mac without a local NVIDIA GPU. Installing a
Mac client does not make its model inference offline. Downloads, local application
availability, API access and paid generation permission are separate facts.

## Current assessment

**Narration fit: promising audition candidate; quality Unrated.** The speech request,
hex response validation, failure handling and real FFmpeg conversion are tested with
local fixtures. No MiniMax voice sample was generated or heard for this release.
**Generated assets / integrated site creation: documentation-reviewed candidates.**
No local application trial, asset generation or recorder replacement was demonstrated.
Do not change the preferred voice or recorder on the strength of this reference alone.

Sources: [MiniMax Code](https://agent.minimax.io/tools/ai-coding-agent),
[MiniMax Design](https://design.minimax.io/),
[API overview](https://platform.minimax.io/docs/api-reference/api-overview),
[speech endpoint](https://platform.minimax.io/docs/api-reference/speech-t2a-http),
[official MCP](https://github.com/MiniMax-AI/MiniMax-MCP).
