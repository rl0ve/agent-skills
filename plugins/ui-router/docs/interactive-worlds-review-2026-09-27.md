# Interactive-world tooling review — September 27, 2026

The 1.18.0 release distilled three supplied AI research conversations into conditional
engineering and design guidance. The two completed deep-research reports are dated
September 23; the conversational report's publication date was not established. The
1.18.2 follow-up also incorporates the previously inaccessible fourth source, supplied
as a 16-page decision report dated September 27. All pages were reviewed. An additional
share was checked and contains identical completed report text to the second deep-research
report, rather than a new independent source. Private share links and copied reports
remain outside the repository.

The decision report says its author could access only placeholders for the two
ChatGPT reports. The completed reports were recovered and reviewed independently for
this update. Its proposed experiments, purchases and schedules remain recommendations,
not user instructions or evidence that those activities were performed.

The reports disagree about the preferred browser stack: Three.js/R3F, Needle, or
PlayCanvas/Babylon.js. None supplies a controlled comparison on the same product,
hardware, authoring constraints and acceptance criteria. Their rankings, model
preferences, speed/cost claims and projected schedules are leads, not policy.

## Decisions

| Candidate | Decision and owner |
| --- | --- |
| Separate runtime, learning/content, asset authoring and optional live intelligence | **Adopt** in `interactive-worlds.md`. A coding-agent choice does not determine the shipped runtime or require live inference. |
| Choose runtime from delivery, authoring and existing implementation | **Adopt conditionally** for unresolved architecture. Compare credible candidates without mandating a rewrite or treating a browser-first recommendation as universal. Native/XR requirements can justify a different starting route. |
| A browser frontend means a browser-native renderer | **Reject.** Pixel Streaming runs the application elsewhere; hosting, GPU capacity and network behavior belong in the evaluation. |
| GLB export enables a later one-click engine migration | **Reject.** Art portability does not establish portability of scripts, interaction, shaders, persistence or curriculum. |
| Make the language goal and observable world outcome explicit | **Adopt** as a focused extension of `interaction-contracts.md`; preserve the requested comprehension or production mode and distinguish interface/help locale from target language and NPC text. |
| Every language-learning experience needs compulsory speech | **Reject.** Select response mode from the learning objective. ASR uncertainty is not automatically learner error; text/selection does not prove pronunciation. No universal pedagogy or learning-effect claim is added. |
| Keep authoritative state and assessment outside free-form dialogue | **Adopt** the explicit model-output case: validate actions/current preconditions, reject stale results, prevent duplicate effects and retain useful recovery. NPC assertions are not assessment evidence. |
| Jev or another NPC/decision service should be mandatory | **Conditional only.** A structured-decision service can address a bounded need; rules/state machines remain valid. Type guarantees/confidence do not establish semantic correctness. No service, account or per-frame inference is required. |
| Generated spaces or Gaussian splats are complete interactive levels | **Reject the blanket claim.** Inspect actual exported geometry, collision and object semantics; add only missing components. An exported collider may be useful without providing manipulable semantic objects. |
| Meng, Dream Loop, asset QA, voice auditions and model routing need replacement | **Already covered.** Preserve selected upstream workflows, spatial integration checks, the existing voice-narration owner and Work Router. No model ranking or agent-count rule changes. |
| A fixed download/FPS target or attractive video proves success | **Reject.** Use device- and task-specific budgets and a representative playable slice. Existing interaction/evidence rules cover assisted completion versus competence and rubric scores versus measured learning. |

## Follow-up decisions for 1.18.2

| Candidate | Decision and owner |
| --- | --- |
| Verify editable export before relying on a hosted builder | **Adopt conditionally** in `interactive-worlds.md`. When portability matters, inspect plan/project rights and prove the exported project can be edited and rebuilt outside the service, including required integrations. Playable export, code-tab access and commercial rights are separate claims. |
| Compare voice prices or provider response times directly | **Reject the shortcut.** Evaluate complete comparable interactions, audible useful-response latency and session reliability; cost assumptions must identify billing units, pauses, backend/context use, retries and included credits. No provider or price is frozen into the skill. |
| English decision accuracy or confidence transfers to every language | **Reject.** Check supported inputs and representative target-language decisions, calibrate thresholds with a fallback and revisit them when the model changes. |
| Add a new conversational-voice skill or expand narration scope | **Defer.** This update supplies conditional architecture/evaluation guidance in the interactive-world reference. The existing narration skill continues to own authored clips. |
| Treat weighted engine scores, ten-minute cost scenarios or a small usability pilot as proof of superiority | **Reference only.** These are assumptions and proposed comparisons, not measured engine rankings, equivalent service quality or established learning effects. Existing evidence guidance covers the distinction; no mandatory benchmark project is added. |
| Replace the current model-routing policy with the reports' model tables | **Reject.** Preserve the independent benchmark review shipped in 1.18.1 and Work Router's current evidence policy. No new model ranking is asserted here. |

## Primary-source checks

Checked September 27. These establish documented capabilities and distinctions, not
comparative quality, current account entitlements or a production benchmark.

- [Three.js game manual](https://threejs.org/manual/pages/game.html) describes Three.js
  as a rendering library and identifies game systems the application supplies.
  [React Three Fiber](https://github.com/pmndrs/react-three-fiber) is a React renderer.
- [Babylon.js specifications](https://www.babylonjs.com/specifications/) and
  [PlayCanvas Engine documentation](https://developer.playcanvas.com/user-manual/engine/)
  support considering integrated browser-engine facilities. The
  [PlayCanvas Editor](https://github.com/playcanvas/editor) is a distinct authoring route.
- [Needle technical overview](https://engine.needle.tools/docs/technical-overview.html)
  and [Blender integration](https://engine.needle.tools/docs/blender/) document a
  Three.js-based runtime, component/export workflow and editor integrations.
- [Unity browser compatibility](https://docs.unity3d.com/Manual/webgl-browsercompatibility.html),
  [Godot web export](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_web.html)
  and [Unreal Pixel Streaming](https://dev.epicgames.com/documentation/unreal-engine/pixel-streaming-in-unreal-engine)
  are point-of-use checks for the actual delivery route; no engine version or license
  threshold is frozen into the skill.
- [TypeSafe's Jev introduction](https://typesafe.ai/blog/introducing-system-one-models-and-jev),
  dated September 15, describes typed probabilistic outputs without string generation
  and supplies vendor evaluation caveats. It does not justify universal NPC use,
  semantic infallibility or an unmeasured per-frame request pattern.
- [World Labs API](https://docs.worldlabs.ai/api) separates splats, collider meshes and
  mesh exports. These outputs do not alone establish the product's object semantics.

The follow-up also checked:

- [Tesana export documentation](https://docs.tesana.ai/building/exports) distinguishes
  playable builds from Godot source and limits source export by project provenance.
  [Rosebud pricing and entitlements](https://rosebud.ai/pricing) separates code-tab
  access, commercial rights and downloadable project code. These are reasons to check
  actual entitlements and export artifacts, not blanket endorsements of either builder.
- [TypeSafe model documentation](https://docs.typesafe.ai/models) describes input limits,
  unequal language performance and moving model aliases. Validate the chosen version
  and task before interpreting confidence as calibrated correctness.
- [OpenAI voice-agent guidance](https://developers.openai.com/api/docs/guides/voice-agents)
  distinguishes speech architectures and evaluates completed tasks, audible latency,
  interruption and reliability. [Inworld pricing](https://inworld.ai/pricing) illustrates
  different speech meters, separate model costs, concurrency limits and subscription
  credits. Current account terms and measured session usage still need verification.

## Scope and validation

The new reference is loaded only for unresolved architecture in interactive worlds.
The learning subsection applies only when learning is part of the requested product.
No desktop app, game engine, provider account, plugin dependency or runtime service is
installed by this release. Work Router and voice-narration remain unchanged.

Package/frontmatter/link checks and scoped policy exercises validate the release's
structure and decision boundaries. No game was built, learner study run, voice service
benchmarked, generated asset purchased or target headset tested for this release.


### Policy exercises

A read-only reviewer walked through these requests with the edited skill. These are
scenario decisions, not executed product tests.

| Request | Result |
| --- | --- |
| Improve an existing Three.js recognition activity with no backend | Retain the stack, recognition mode and authored interaction; diagnose the visible limitation and add a specialist only when useful. |
| Choose a stack for an offline native headset simulation | Make native/offline/input requirements decisive; use compatible specialists and require an actual package/device slice with the relevant network access disabled. |
| An NPC response arrives after reset and claims a passed lesson | Check current turn/state and preconditions before action; stale text cannot perform an old action or award progress. |
| Replace one supplied button translation in an accepted scene | Direct local edit and affected layout/action check; no new architecture, discovery or engine comparison. |
| A pronunciation exercise gets uncertain speech recognition | Recover uncertain input and distinguish recognition from pronunciation evidence; typed success cannot stand in for the requested skill. |

The review prompted two bounded clarifications: diagnose existing scene issues before
adding a specialist, and use runtime-compatible specialists plus actual offline/headset
acceptance evidence. No new universal workflow or safety checklist was added.

### Release checks

- All 22 root package/inventory tests passed after aligning both marketplace versions.
- Local reference destinations, field-guide data/version parity and preserved routing
  data passed; `git diff --check` passed.
- The bundled `quick_validate.py` rejects the existing `compatibility` frontmatter field
  on both baseline and candidate. The [Agent Skills specification](https://agentskills.io/specification)
  permits it. Its value is unchanged; the remaining validator checks passed on a scratch
  copy omitting that field. Source frontmatter retains the portable declaration.

### Follow-up policy exercises

These are maintainer walkthroughs of the added guidance, not executed provider trials.

| Request | Result |
| --- | --- |
| Adopt a hosted builder for an independently deployed lesson; its remix downloads as a playable build | Verify source rights for that project and perform an editable export/rebuild before claiming portability; retain the unverified dependency if source is unavailable. |
| Compare a connected-minute voice service with character-billed TTS plus separate recognition/dialogue | Use the same lesson and language, include the full pipeline and pauses/credits, and compare useful audible responses and task outcomes as well as cost. |
| Replace a single prerecorded greeting or adjust a recognition-only activity | Retain the narration owner or deterministic activity; do not introduce a live-conversation comparison. |
| Apply an English-calibrated decision threshold to learner responses in another language | Validate representative target-language cases, retain abstention/fallback and track the selected model version before trusting that threshold. |

The follow-up preserves 1.18.1's benchmark-based model guidance and leaves Work Router,
voice-narration and the existing learning-mode contracts unchanged. All 22 package
checks passed for 1.18.2, along with 39 local Markdown destinations, release-data/version
parity and `git diff --check`. No paid trial or product benchmark is represented as
completed.
