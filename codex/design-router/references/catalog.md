# Canonical design-skill catalog

This catalog preserves the named skill universe researched in the original Perplexity task. It is a **research snapshot dated 2026-08-15**, not an assertion that every entry is installed, safe, current, or still available. Inspect the live catalog first and verify upstream before recommending an installation.

Status language:

- **canonical** — part of the original routing system;
- **sub-skill** — supplied inside another canonical repository;
- **local** — user-specific capability rather than a third-party dependency;
- **lower confidence** — useful lead whose upstream availability or packaging needed another check in the supplied research.

## Aesthetic and interface leads

| Key | Upstream | Role | Use | Research status |
|---|---|---|---|---|
| `taste` | `Leonxlnx/taste-skill` | High-taste frontend director with landing, redesign, image-to-code, brand-kit, and visual-style sub-skills | Marketing, landing pages, portfolios, reference-led redesign | canonical |
| `hallmark` | `Nutlope/hallmark` | Macrostructure and anti-cliche composition | Pre-primary or focused layer for public-facing page structure | canonical |
| `interface-design` | `Dammyjay93/interface-design` | Product and dashboard design lead | Apps, dashboards, admin, tools, settings, data interfaces | canonical |
| `ui-ux-pro-max` | `nextlevelbuilder/ui-ux-pro-max-skill` | Broad UI/UX rule and style library | Fallback or broad exploration, not the default lead | canonical |
| `paperclip` | `getpaperclipai/paperclip` · `design-guide` | Opinionated product design guide | Alternative product/app lead | lower confidence |
| `frontend-design` | `anthropics/skills` or the installed Codex adaptation | General aesthetic frontend baseline | Installed fallback when a canonical specialist is unavailable | compatibility fallback |

## Persistent operating layer

| Key | Upstream | Role | Use | Research status |
|---|---|---|---|---|
| `impeccable` | `pbakaus/impeccable` | Persistent design context, critique, audit, polish, hardening, onboarding, typography, layout, color, motion, and deterministic anti-pattern checks | Layer after generation; primary only for review/audit | canonical |

Impeccable modes are part of routing: **Persuade** for marketing, **Operate** for product work, **Read** for editorial/docs, and **Experience** for expressive/portfolio work.

## Motion and interaction

| Key | Upstream | Role | Use | Research status |
|---|---|---|---|---|
| `emil-motion` | `emilkowalski/skills` | Motion decision framework and animation review | Motion-only primary; focused layer elsewhere | canonical |
| `jakub-feel-better` | `jakubkrehel/make-interfaces-feel-better` | Tactile details, optical alignment, interruptible motion, number and icon behavior | Micro-polish layer | canonical |
| `transitions-dev` | `Jakubantalik/transitions.dev` | Copy-ready CSS transition patterns | Common application transitions | canonical |
| `gsap-scrolltrigger` | `freshtechbro/claudedesignskills` | GSAP and ScrollTrigger implementation guidance | Expressive motion layer | canonical |

## Creative and expressive

| Key | Upstream | Role | Use | Research status |
|---|---|---|---|---|
| `meng-webgl-stack` | `MengTo/Skills` | Large specialist library for cinematic motion, Three.js, capture, reference workflows, and reusable techniques | Creative/WebGL specialist library, not one universal lead | canonical |
| `claudedesignskills` | `freshtechbro/claudedesignskills` | Three.js, GSAP, R3F, Framer Motion, Babylon.js, Spline, and Rive pack | Creative-expressive lead option | canonical |
| `awwwards-3d` | `tsogjavklann/awwwards-3d` | Scroll-driven 3D visual language | Portfolio and Awwwards-style experiences | canonical |
| `industrial-brutalist-ui` | `code-yeongyu/lazycodex` · `industrial-brutalist-ui` | Swiss-modernist and military-terminal aesthetic | Explicitly requested data-heavy aesthetic | canonical |
| `huashu-design` | `alchaincyf/huashu-design` | HTML-native prototypes, slides, animation, MP4/GIF export | Expressive campaigns and presentations | canonical |
| `garden-skills` | `ConardLi/garden-skills` | Web design, video presentation, article, and image-generation stack | Optional expressive production layer | canonical |
| `p5-pipeline` | `nousresearch/hermes-agent` · `p5js` | Seeded generative-art workflow | Generative and algorithmic art | canonical |

## Image-to-code sequence

| Key | Upstream | Role | Use | Research status |
|---|---|---|---|---|
| `extract-design-system` | `arvindrk/extract-design-system` | Extract colors, type, spacing, radius, and shadows | Token extraction | canonical |
| `firecrawl-clone` | `firecrawl/firecrawl-workflows` · `firecrawl-website-design-clone` | Website evidence to agent-ready `DESIGN.md` | URL-to-design-context | canonical |
| `meng-stitched-capture` | `MengTo/Skills` | Full-page stitched capture | Avoid hero-only reference capture | sub-skill |
| `meng-video-superprompt` | `MengTo/Skills` | Video to detailed design prompt | Motion/video references | sub-skill |
| `meng-html-interactions` | `MengTo/Skills` | Extract sections and interactions from HTML | Reusable interaction reference | sub-skill |
| `taste-image-to-code` | `Leonxlnx/taste-skill` | Reference image to code with taste constraints | Implementation step after extraction/capture | sub-skill |

## Systems and extraction

| Key | Upstream | Role | Use | Research status |
|---|---|---|---|---|
| `stitch-design-md` | `google-labs-code/stitch-skills` · `design-md` | Google Stitch design-system documentation | Stitch-native extraction/build | canonical |
| `hue` | `dominikmartn/hue` | Brand-to-design-system from URL, name, or screenshot | Brand-derived reusable system | canonical |
| `ibelick-ui` | `ibelick/ui-skills` | Baseline cleanup, design-md, accessibility, metadata, motion performance | Systems and review layer | canonical |

## Review, accessibility, and performance

| Key | Upstream | Role | Use | Research status |
|---|---|---|---|---|
| `addy-web-quality` | `addyosmani/web-quality-skills` | Accessibility, Core Web Vitals, performance, SEO, best practices | Technical quality gate | canonical |
| `jakub-better-stack` | `jakubkrehel/skills` | Better interface, type, color, layout, accessibility, motion, and writing | Focused design review layers | canonical |
| `antfu-guidelines` | `antfu/skills` · `web-design-guidelines` | Developer-tooling-friendly web design review | Review layer | canonical |
| `vercel-labs` | `vercel-labs/agent-skills` | Web design and React quality guidance | Review and implementation quality | canonical |

## Writing and voice

| Key | Upstream | Role | Use | Research status |
|---|---|---|---|---|
| `no-ai-slop` | `petergyang/no-ai-slop` | Concise, voice-preserving removal of AI tells | Anti-slop primary | canonical |
| `natural-writing` | This repository (`plugins/natural-writing`), tool-neutral | Voice-preserving editor and anti-slop router | Default final editor for standalone prose, interface copy, marketing copy, documentation, and executive writing | in this repo |
| `blader-humanizer` | `blader/humanizer` | General AI-tell removal | Fallback editor when Natural Writing is unavailable | canonical |
| `write-like-me` | `dookaloosy/write-like-me` | Derive a reusable voice profile from writing samples | Voice calibration | canonical |
| `humanizer-local` | User-scoped `humanizer` | Robert-specific AI-writing rules | Legacy fallback editor | local |

## Marketing and components

| Key | Upstream | Role | Use | Research status |
|---|---|---|---|---|
| `marketing-skills` | `coreyhaines31/marketingskills` | Copy, CRO, email, positioning, and marketing frameworks | Marketing craft layer | canonical |
| `wondel-storybrand` | `wondelai/skills` | StoryBrand, one-page marketing, CRO, offers, hooked UX | Named marketing-framework layer | canonical |
| `shadcn-official` | `shadcn-ui/ui` · `shadcn` | Add, search, fix, style, and compose shadcn components | Component-library primary | canonical |

## Additional researched watchlist

The supplied research also identified useful adjacent references that were not promoted into every default chain: `ahpxex/open-dashboard` for admin components and forms, `Owl-Listener/designer-skills` for token/icon/motion governance, `github/awesome-copilot` for ecosystem comparison, `ceorkm/mobile-app-ui-design` for lower-signal mobile specialization, and focused humanizers from `harshaneel/humanize` and `Aboudjem/humanizer-skill`.

Keep these as watchlist entries. Do not imply endorsement or installation without current upstream review.

## Targeted gap pass — 2026-08-16

| Gap | Candidate | Judgment |
|---|---|---|
| Web data visualization and charts | `openai/plugins` · `build-web-data-visualization` | Strong, distinct orchestration reference from OpenAI's plugin repository. Keep on the watchlist until the complete plugin and its sibling references can be installed together; do not extract the single router skill by itself. |
| Mobile-native UI | `mdrmuhaimin/agentic-skills` · `mobile-ui-ux-designer` | Detailed and explicitly Codex-oriented, but not promoted into a default chain without more adoption and maintenance evidence. |
| Complex forms | Existing `interface-design`, Impeccable, Jakub accessibility, Addy quality, and `open-dashboard` coverage | No clearly superior standalone specialist surfaced. Preserve this as a real gap instead of padding the stack with a weak candidate. |
| Email design | Corey Haines email/marketing skills plus framework-native React Email or MJML documentation | No strong dedicated agent skill surfaced. Keep the route at marketing craft plus implementation documentation. |

The optional installer includes only candidates with a known installation route and enough role clarity to explain what will be added. Watchlist entries are never auto-promoted.
