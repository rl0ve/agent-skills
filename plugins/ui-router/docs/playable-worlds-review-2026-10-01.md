# Playable-world source review — October 1, 2026

Reviewed selected complete MengTo/Skills entrypoints at
[d5bd3a7e9c9f4b00853e84fffa60bc38eee9e744](https://github.com/MengTo/Skills/tree/d5bd3a7e9c9f4b00853e84fffa60bc38eee9e744)
(MIT). This was a targeted review, not a whole-repository audit or installation.

| Finding | Decision |
| --- | --- |
| Encounter decisions, level landmarks, camera readability and audio lifecycle | Adopt precise specialist routes with scope boundaries; adapt the shared choice/consequence/recovery principle. |
| Combat defaults and strict flat-plane level geometry | Conditional within the upstream action-game scope; do not impose them on calm learning or architectural/XR worlds. |
| Playable-game testing | Already covered; keep real controls, deterministic review states and save/retry checks. |
| Score-to-target and blind-judge workflow | Reference only; self-scores do not prove user engagement or learning. Do not import automatic delegation, indefinite polishing or publishing authority. |
| Fullscreen ChatGPT sidebar apps and conversation panels | Conditional delivery option; trial a real scene and state lifecycle before platform commitment. |
| Model choice from likes or author claims | Reject as a benchmark; Work Router owns model routing. |

Public examples inspected on X include Meng's
[September 23 boat scene](https://x.com/MengTo/status/2102760783344189761),
[September 28 layered holographic card](https://x.com/MengTo/status/2104565735288938804),
and [October 1 Three.js device editor](https://x.com/MengTo/status/2105680287854440715).
The card illustrates camera-dependent 2D/3D composition; the editor illustrates
coherent tools and direct manipulation. These posts and demonstrations do not
establish whole-game playability, native-device performance or one-shot completion.

Official platform sources: [extensions](https://developers.openai.com/plugins/build/extensions)
and [MCP UI](https://developers.openai.com/plugins/build/chatgpt-ui).

Policy cases: a calm language mystery triggers connected choices and changed-context
retrieval, without combat or forced speech; a static product card does not trigger
a game-loop redesign; an existing standalone world gains a host adapter only after
a real host trial. This is a policy walkthrough, not a comparative user study.
