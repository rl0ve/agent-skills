---
name: capability-storyboard
description: Build a capability-first, multi-tool HTML storyboard for a product keynote, demo walkthrough, or "here's what happens when..." narrative doc. Use this whenever asked to build a keynote/demo storyboard, turn a beat-by-beat customer-scenario script into something a large or mixed audience can actually follow, add a spoken talk-track and director's-notes column to a demo doc, make several different tools visually distinguishable in one mockup document, or add realistic screen chrome (browser, native app, or a bare presentation slide) to HTML product mockups. Trigger this even if the user doesn't say "storyboard" — phrases like "walk through the demo", "build the keynote deck for X", "mock up what the presenter sees", or "make this less confusing for the audience" all fit.
---

## When to use this vs. a full beat-by-beat walkthrough

Two shapes for a demo document, and they solve different problems:

- **Beat-by-beat walkthrough** (one scenario, start to finish, every step shown): right when the audience needs to trust that one specific case works end to end, or when a small technical group needs to sign off on every step. It gets long, and it centers the *scenario* rather than the *product*.
- **Capability-first storyboard** (this skill): right for a keynote-scale or mixed audience, where the point is "look what the product can do," not "watch this one claim get processed." A small number of Acts, each demonstrating one capability, all riding on the *same* running example so the audience keeps one thread — but the thread is in service of the capabilities, not the other way around.

Ask which one the user actually needs before building. If an existing beat-by-beat script exists, this skill is often used to *compress* it: pull out the handful of moments that best demonstrate distinct capabilities, and cut everything else. Don't invent new capabilities to demo — the ones worth showing usually already exist in the source material (a script, a set of feature notes, a leadership deck) and can be adapted with light rewrites, not paraphrased into marketing copy from scratch.

## The eight things that make this format work

These are lessons pulled from actually building one of these under real back-and-forth review with the person it was for. Read `references/example-full.html` afterward: a worked board, in an invented scenario, that has every mechanism below wired up and running.

**1. Structure: Acts = capabilities, Scenes = moments, each Scene has three parts.**
Every scene is one screen mockup + a **Talk track** + a **Demo** list. The talk track is the literal words a presenter would say — if there's an existing script (a real demo talk track, a keynote draft, a customer-facing script), adapt it with the lightest possible touch: swap nouns and numbers for the new scenario, keep the sentence structure and rhythm intact. Don't rewrite a working script into your own voice just because the scenario changed. The Demo list is terse director's notes — what to put on screen, what to point at, and explicit "Don't..." lines for things that would go wrong done live (don't type the prompt live, don't ask a follow-up question, etc.). Put the talk track and demo notes in a narrow stacked column beside the mockup, not competing with it for width — if reviewers say "the picture got too small," that column is almost always the reason; stack its two pieces vertically in one ~200px rail instead of two side-by-side rails.

**2. Multi-tool honesty: never let two different tools look like the same screen.**
A realistic demo usually crosses several real products. Give each one its own visual identity pulled from **real design tokens** — if the product exists and you can reach it, actually open it and read its computed CSS (font-family, accent color, background, border-radius) rather than guessing. A generic "make it look nice" palette reads as fake and, worse, makes genuinely different tools look interchangeable, which is the one thing that will confuse a reviewer who knows the products. Three chrome shapes cover almost everything:
- a generic light **browser chrome** (traffic-light dots, a fake tab, a plausible cloud URL) for anything that's a web app,
- a **native-app chrome** (its own title bar, no address bar, its own left sidebar/tab strip) for a tool with a real, recognizable desktop or IDE identity — build both a dark developer-tool variant and a light business-app variant, they read very differently,
- a **bare full-bleed slide** with zero product chrome for anything that isn't a screen of any product at all (an opening title, a closing slide) — don't put a browser frame around a slide, it undercuts the moment.

**3. If two OOTB screens of the real product are involved, match them closely — don't improvise a "close enough" version.**
When the user hands you real screenshots of the actual product screens (an instance list view, a single-instance detail view, a modal dialog), treat those as ground truth, not inspiration. Match the layout, the terminology, and which actions live on which screen (e.g., "Migrate" might be a bulk action that only appears after selecting rows in a list, not a button floating in a single-instance sidebar — get this right, because a viewer who knows the product will notice immediately and it undermines trust in the whole document). It's fine to simplify visual density (fewer decorative icons, fewer table rows) but don't relocate functionality to where it's more convenient to draw.

**4. Label surfaces explicitly whenever two scenes could be mistaken for the same screen.**
A small pill above the mockup frame, e.g. "Personal queue · Cases tab" vs. "Fleet-wide view · Insights tab", or "Design time · Studio" vs. "Runtime · Case App". Cheap to add, and it's the fix every time a reviewer says "wait, is this the same screen as before?"

**5. When a presentation choice is genuinely undecided, build a toggle instead of guessing.**
If it's unclear whether a moment should be a terminal/CLI or a polished chat UI, or any other either/or, build both into the scene and add a tiny segmented control (e.g. "Terminal / UI") in the mockup's own title bar — plain vanilla JS toggling one CSS class on the frame. Default to whatever the presenter said they'd probably use. This turns a blocking decision into a reversible one and the reviewer can flip it themselves later instead of asking you to redo work.

**6. The masthead has to actually orient the reader, in this order: what happened, then the steps in plain words, then what's literally on screen.**
Don't open with capability marketing copy ("this demonstrates four powerful capabilities..."). Open with the concrete story: what triggered the scenario, in one or two sentences a non-expert would follow, then the stages/steps it moves through in plain language (not the internal jargon names), *then* a short literal bullet list of the real product/tool names that appear on screen, in the order they appear. Keep this purely orienting. If the document will be shown to people who weren't in the room for whatever internal debate produced this approach, cut anything defensive or self-justifying ("why we moved away from X") — that's process history for you, not content for the reader.

**7. Verify by looking, not by reading the code.**
After every edit, actually render the file and check the browser console for errors. Real bugs that only showed up this way, every time: a screen accidentally double-wrapped in two layers of chrome, a CSS `::marker` given an HTML entity instead of a literal Unicode character (CSS `content` doesn't decode HTML entities), a flex-sized element collapsing to near-zero height because it inherited `flex:1` inside a parent that wasn't actually a flex container in that context. None of these were visible from reading the markup.

**8. Run a writing pass on every scene title, caption, and talk track — if the `natural-writing` skill is available, invoke it; otherwise apply the same checks by hand.**
Two specific patterns came up over and over in review, both already named in natural-writing's own pattern catalog under different labels, worth watching for by name here:
- *Negative parallelism / binary template* — "Sarah isn't reconstructing the case across five systems — she's spending her time on the decision that needs her" reads as hedgy and AI-flavored. Rewrite action-first, caveat second: "Sarah spends her time on the decision that needs her, not reconstructing the case across five systems." The rule the person reviewing this actually gave: *start with the action, then the caveat if one is needed* — not the reverse.
- *Colon-drama titles* — "Open one case: the recommendation is already there" is a label-plus-reveal, not a sentence a person would say. Rewrite as a plain sentence: "The recommendation is waiting before Sarah opens the case."

One nuance specific to this workflow that a general writing pass won't know on its own: **when a scene's talk track is adapted from an existing source script** (point 1 above), fidelity to that source and freedom from these patterns can pull in opposite directions — the source script might itself contain a negative-parallelism construction, inherited directly from whatever real presenter or document it came from. Fix the pattern anyway if asked to, but don't treat "stay close to the source" as blanket permission to leave every AI-slop-shaped sentence alone just because it existed in the source, and don't treat "fix the writing" as permission to silently drift from a source the person explicitly asked you to track closely — when the two goals conflict on a specific line, that's worth surfacing rather than picking one silently.

Separately: if this storyboard will be shown to a broader audience than the people who worked out the approach with you, that's also a writing-pass concern, not just a content one (see point 6) — re-read every scene for tone, not just content, since internal-politics phrasing can hide in a caption's word choice even after the paragraph-level content has been cleaned up.

## The reusable technical pattern

Start from `references/template.html` — a trimmed, working skeleton with placeholder content that has the mechanics below already wired up. Copy it, then fill in the Acts/Scenes array and swap the design tokens per real product. For denser examples of specific components (a stats strip, a modal dialog, mini "screenshot" thumbnails for a closing slide, a stage-canvas diagram, a phone frame, a light business-app chrome), read `references/example-full.html`, which is a complete nine-scene board — lift whatever component you need out of it rather than reinventing it. Its scenario and its three products are invented, so nothing in it needs sanitising before you borrow from it.

- **Single self-contained HTML file.** Inline `<style>`, inline `<script>` at the bottom. No build step, no external JS — it needs to open directly in a browser and be embeddable as an Artifact.
- **The `--s` scaling trick.** Each mockup is authored at a fixed 1280×800 "screen" and scaled down responsively via a CSS custom property (`transform: scale(var(--s,1))`) computed from the actual rendered width of its container using a `ResizeObserver`. This keeps every mockup crisp regardless of embed width instead of trying to hand-write responsive breakpoints for dozens of screens.
- **Data-driven Acts → Scenes.** One JS array of Acts, each with a `scenes` array. Each scene carries `actor`, `title`, `tt` (talk track), `demo` (array of strings), `status` (a build-status dot: e.g. `built` / `partial` / `build`), and a `views` key naming which render function draws its mockup body. A small dispatcher function maps view names to render functions and to which chrome wrapper they need.
- **Sticky left table-of-contents.** One sidebar, sticky-positioned, listing every Act and Scene as anchor links. This is what lets a reviewer jump straight to "the scene with the problem" instead of scrolling. A per-scene build-status dot (e.g. `built` / `partial` / `build`) is a genuinely useful optional add-on when the document doubles as a build-tracking artifact for a team — but it's not load-bearing for the storyboard format itself, and it's an easy first thing to cut if a reviewer says the sidebar feels cluttered or the status framing isn't something they need.
- **The masthead + capbox.** A short plain-language two-or-three-paragraph intro (see point 6 above), followed by a distinctly-colored callout box that's just a plain bulleted list — either the literal product/tool names shown, in order, or (if asked for capabilities instead) the capability list, but not both mashed into one box; ask which the user wants.

Read the template file's comments for exactly where each of these lives before you start filling in content.


## Lessons 9–14, from a 27-scene keynote board

Distilled from three weeks of real review cycles on a 27-scene, four-act board that shipped ~20
releases. Each earns its place by a defect it ended.

**9. Scene anatomy that survived review:** the bold headline is a *storybook sentence* (read all of
them in order cold — every joint must hand off to the next); a **status pill** on each scene says
whether the screen *exists today / partially exists / is to build*; the long narrative rides as a
**caption under the slide**, visible in every view, never line-clamped (mid-sentence ellipsis was
the user's first complaint). The screen's identity lives on a small frame label above the mockup,
not in the headline.

**10. Three reading modes, one dataset:** Narrative (a plain-language walkthrough, standalone),
Strip (thumbnail grid — the default), Flow (talk track + director's notes per scene). The
walkthrough is a section shown only by the Narrative toggle — never a collapsible duplicated by a
view mode. A masthead stat line ("N screens · X exist today · Y partially exist · Z to build") is
**computed from the scene data** at render, never typed.

**11. Nothing hardcoded that the data can compute.** Scene cross-references are written
`@scene:viewkey` in copy and resolved to numbers at render — hardcoded "scene 12" went stale on
every renumbering, five times. Same for counts, act ranges, and the stat line.

**12. Scenes get cut and un-cut constantly — park, don't delete.** Removed scenes keep their view
functions in the file behind a comment ("parked, one re-add away"); only the ACTS entries move.
Mock-only frames carry a small `mock · separate tab` tag on the frame label (never in the nav).

**13. The srcdoc trap:** if the board is hosted inside an app via `<iframe srcDoc>`, bare `#id`
hrefs resolve against the *parent* URL and the iframe navigates to the app itself, nesting it.
Intercept in-page anchors: `closest('a[href^="#"]')` → `scrollIntoView` + `history.replaceState`.

**14. Verification is a render pass, not a re-read:** serve the file and assert — zero overflow in
every mockup body (`scrollHeight` vs `clientHeight`), zero clipped headlines in strip view, zero
unresolved `@scene:` tokens, zero internal colleague names (shared artifact — provenance lives in
the README and decision record, and sweep case-SENSITIVELY: `He/His` hides after `he/his` is
cleared), all view modes toggle. For reviewer briefs, export the board's text with a script that
**asserts every scene was extracted** — a lossy hand-rolled extract once produced phantom review
findings. Publishing anywhere is gated on the owner's explicit per-release go after a local preview.

## Lesson 15 — Ground app frames in the running app, not in meeting notes

Frames drawn from working-session notes shipped five drifts in one evening: a rename that had
not actually landed in code ("Tasks"), a button the app never had ("+ New case"), an option
order that didn't match, a flag-gated widget drawn as if default-on, and a mislabeled tab.
When a teammate's app is the subject: `npm run dev` their repo, walk every screen the scenes
claim, and rebuild frames from what renders. The repo at a pinned commit outranks both the
deployment and anyone's notes about it. Corollary: never draw the demo rig — feature-flag
panels, VITE_ notes, mock tags. Flag-gated UI is drawn at its shipped default; a beat that
needs a non-default flag belongs in the demo notes, not the frame.

## Lesson 16 — Real screens beat redrawn screens

When the screen a scene shows actually exists — a deployed app, a running prototype — the frame
shows a capture of it: keep the storyboard's browser chrome and captions, embed the real pixels
as a data URI so the board stays one self-contained file. Hand-drawn mocks are only for surfaces
that don't exist yet. A simplified redrawing of a good screen reads as "dumbing down and changing
the look & feel" to the people who built it. Tweaking a capture slightly is fine (zoom, a changed
word) — stay at the prototype's fidelity. Hide dev chrome (sign-in banners, feature-flag panels)
before capturing, and re-capture when the source app moves. Keep the parked view functions: a
mock is the fallback when a real screen regresses or disappears.
