# Canonical chain composition

The named chains below preserve the original Perplexity research. They describe the intended division of labor even when a dependency is missing. After choosing a canonical chain, inspect the live catalog and produce an executable chain with explicit substitutions.

Use exactly one broad lead and no more than three focused layers. Optional entries are alternatives, not an instruction to load everything.

## Marketing / landing

**Canonical:** `taste/design-taste-frontend` → `hallmark` → `impeccable Persuade` → `marketing-skills`

- Add `no-ai-slop` when copy quality is part of the request.
- Add `wondel-storybrand` when a named messaging/CRO framework is useful.
- Add a Meng or Huashu specialist only when expression is explicitly part of the value.
- Installed fallback pattern: `frontend-design` → an installed Impeccable capability → brand/UX-copy layer. Report that Taste or Hallmark is missing; do not rename the fallback as Taste.

## Product / app

**Canonical:** `interface-design` → `impeccable Operate` → `shadcn-official` → `jakub-better-stack`

- `paperclip/design-guide` is an alternative product lead, not a layer stacked with `interface-design`.
- Add `addy-web-quality` for a release-quality accessibility/performance gate.
- Add `ibelick-ui` for baseline cleanup or design-system documentation.
- Installed fallback pattern: `frontend-design` or an installed product-design skill → Impeccable Operate equivalent → installed design-system/accessibility layers.

## Creative / expressive

Choose one lead by medium:

- WebGL/cinematic: `meng-webgl-stack`;
- framework-rich 3D/motion: `claudedesignskills`;
- portfolio scroll experience: `awwwards-3d`;
- explicitly generative: `p5-pipeline`.

**Canonical layers:** chosen lead → `impeccable Experience` → `emil-motion` → `gsap-scrolltrigger`

Use `huashu-design`, `garden-skills`, or `industrial-brutalist-ui` only when their specific output or aesthetic is requested. For `b2b-saas` or `internal-tool`, stop at the mismatch gate before choosing this chain.

## Content / editorial

**Canonical:** `taste` in docs/editorial mode → `impeccable Read` → `jakub-better-stack` typography/layout → `addy-web-quality`

The lead owns hierarchy and reading composition. Copy/voice layers remain separate and run only when rewriting was requested.

## Motion only

**Canonical:** `emil-motion` → `jakub-feel-better` → `transitions-dev`

Add `gsap-scrolltrigger` only for a GSAP/scroll-driven implementation. Preserve the existing layout, type, color, and copy.

## Image to code — fixed sequence

1. `extract-design-system` or `firecrawl-clone` — persist tokens and `DESIGN.md`.
2. `meng-stitched-capture`, `meng-video-superprompt`, or the supplied still image — capture the full reference.
3. `taste-image-to-code` — implement one bounded region at a time.
4. `impeccable critique/audit` — compare every region and list deviations.
5. `meng-html-interactions` — optional extraction of a successful interaction for reuse.

Do not replace this sequence with a single broad frontend skill unless the canonical tools are unavailable. If substituting, preserve the same extraction → capture → bounded implementation → diff workflow.

## Systems extraction

**Canonical:** `extract-design-system` or `firecrawl-clone` → `stitch-design-md` → `impeccable document/extract` → `ibelick-ui/create-design-md`

Use `hue` when the goal is a reusable brand-derived system rather than only tokens.

## Review / audit

**Canonical:** `impeccable` → `addy-web-quality` → `jakub-better-stack` → `ibelick-ui`

`antfu-guidelines` or `vercel-labs` may substitute for a focused web/React quality review. Stay read-only unless fixes were requested.

## Writing / anti-slop

Use one context-holding editor. Multiple humanizer passes tend to flatten voice, weaken qualifications, and replace coherent structure with watched-word substitutions.

- **Standalone prose or supplied draft:** `natural-writing` alone.
- **Product or interface copy:** product semantics or UX-copy layer → `natural-writing` final editor.
- **Marketing copy:** marketing or brand-voice layer → `natural-writing` final editor.
- **Voice calibration:** a representative author sample feeds `natural-writing`; use `write-like-me` only when the user explicitly wants a durable voice profile.

When `natural-writing` is unavailable, select exactly one fallback editor from `no-ai-slop`, `blader-humanizer`, or `humanizer-local` based on the request. Preserve facts, qualifications, product terminology, identifiers, and formatting. Do not run all three sequentially.

## Component library

**Canonical:** `shadcn-official` → `impeccable Operate` → `jakub-better-stack` → `addy-web-quality`

Cover variants, states, tokens, keyboard behavior, responsive behavior, accessibility, and usage guidance.

## Audience modifiers

Apply the selected audience file after choosing the surface chain:

- `b2b-saas`: Operate + Read; restrained motion; density and states;
- `b2c-ecommerce`: Persuade + Operate; product media, trust, cart/checkout;
- `b2c-consumer-app`: Experience + Operate; personality, gesture, feedback;
- `b2b-marketing`: Persuade + Read; proof and executive scanability;
- `b2c-marketing`: Persuade + Experience; brand and editorial expression;
- `prosumer-tool`: Operate + restrained Experience; expert speed and visible craft;
- `internal-tool`: Operate only; throughput and predictability;
- `content-editorial`: Read; typography, measure, structure, citations;
- `portfolio-personal`: Experience + Persuade; authored voice and work proof.

## Compatibility rules

- Do not stack two broad aesthetic directors.
- Impeccable is normally an operating layer; it becomes the lead for `review-audit`.
- Motion specialists may stack when each owns a different level: decision framework, tactile detail, or implementation primitive.
- Writing can use one upstream semantics or brand layer followed by one editor. Do not stack broad humanizers.
- A locally installed substitute must be labeled as a substitute, not silently promoted into the canonical research record.
