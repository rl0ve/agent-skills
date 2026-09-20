# Reference and sample steering review cases

Reviewed 2026-09-06 against the 1.10.0 policy. These are manual policy consistency
checks, not executed agent trials or evidence of improved design outcomes.

| Case | Expected route and evidence | Review |
|---|---|---|
| New consumer cooking app; visual direction open | Consumer task and audience; two or three visible directions, then a representative slice. No inherited B2B dashboard or mandatory AI chat. | Covered by taxonomy and design-steering |
| Expressive educational atlas from a user who works in SaaS | Preserve learning and reading tasks; select a compatible expressive direction. Profession does not set the aesthetic. | Covered by taxonomy and art-direction |
| Business analytics app with explicitly bold visual direction | Preserve density and task completion; do not block solely on the B2B label. Raise only a concrete conflict. | Covered by chains, audiences and guide matrix |
| Existing shop, change button padding | Apply the defined correction directly. No research, samples or approval round. | Covered by steering exclusions |
| Gallery navigation has two materially different interaction choices | Show comparable component examples, recommend one, explain navigation tradeoff; adapt to the existing system. | Covered by component checkpoint and adoption rules |
| Iteration: keep the density but make the navigation less corporate | Preserve accepted density; use a focused current-versus-alternative comparison only if interpretation remains consequential. | Covered by reaction and iteration rules |
| Accepted site needs only a small motion adjustment | Compare playable motion when useful, retain layout, copy and tokens; support reduced motion. | Covered by motion-only route and source map |
| AI-powered creative editor | Select relevant AI status/control examples without forcing a chat shell; actual status and recovery must work. | Covered by AI-interface adoption rules |
| Reference connector unavailable or preview restricted | Report access/display limit; use a supported accessible reference or labeled approximation. No bulk scrape, silent purchase or claim of unseen evidence. | Covered by resource and steering access rules |
| User delegates taste and asks for autonomous execution | Recommend and proceed on reversible assumptions; no repeated approval gates. Silence does not authorize dependent actions requiring permission. | Covered by existing steering authorization rules |
| Attractive component needs another framework and fails long-text state | Prefer adapting the technique or an existing equivalent; verify the destination with realistic content. Demo quality does not justify a framework switch. | Covered by adoption and quality gates |

## September 20 additions — 1.15.0

Manual policy review only; these are not automated agent trials or device tests.

| Case | Expected route and evidence | Review |
|---|---|---|
| Public listening room is explicitly the learning app | Consumer product/expressive primary; landing secondary. Preserve entry → song selection → learning and return. No “app or preview?” question because intent is settled. | Taxonomy hybrid case |
| “Build a landing page like this interactive room,” with no task brief | Ask whether people use the experience there or preview a separate product, because the answer changes the structure. One lead and a representative slice. | Steering question table |
| Expressive learning site, uncertain entry sound | Ask whether Enter intentionally starts sound or opens quietly with separate Play. Show a small entry comparison if useful. No automatic microphone request. | Steering and media checks |
| User specifies quiet entry, an iPad on a stand and optional hands | Implement those constraints directly; retain hands-off and large reachable transport. Do not repeat resolved device/sound/style questions. Real-device speech remains a separate check. | Steering exclusions and media checks |
| User delegates taste for an ordinary static portfolio | Choose a reversible direction and proceed. No sound system, spatial scene or mandatory approval question. | Nearby non-trigger case |
| Attractive lesson demo shows notes over an artist recording | Verify source identity and note provenance separately. Do not present invented exercise notes as a verified score. Check shared playback/mute/seek state in the destination. | Media evidence boundary |
| X post links a public repository without a reuse license | Inspect as reference; do not copy the design/assets or assume “open-sourced” grants reuse. No automatic library or paid service install. | Existing source/license checks |

## CMS acceptance additions — 1.15.1

Manual policy review only; no new CMS execution is claimed by this release.

| Case | Expected route and evidence | Review |
|---|---|---|
| Strong HTML prototype is recreated in WordPress/Elementor | Assess the saved destination pages and interactions; keep prototype scores preliminary. | CMS acceptance gate |
| User requires native editor maintenance | On the authorized test copy, edit/save/reload/reopen a representative widget; restore temporary content and identify the reviewed revision and custom dependencies. | CMS acceptance gate |
| Captions or video controls change after a visual review | Recheck affected playback, captions, transcripts and responsive behavior; update that assessment and retain valid evidence for unaffected flows. | CMS acceptance gate |
| Only the live production editor is available, with live edits forbidden | Do not edit it to satisfy the gate; report native editability as unverified until a permitted environment exists. | Authorization boundary |
| Existing static site needs one spacing fix | Use the narrow existing browser checks; no CMS editor ceremony or full-site reassessment. | Nearby non-trigger case |

## Media runtime additions — 1.16.1

Manual policy consistency review informed by observed application failures. These
cases do not constitute a new browser trial or a universal provider compatibility rule.

| Case | Expected route and evidence | Review |
|---|---|---|
| Several real recordings fail under one local origin, while a tutorial plays | Compare the same recording under a relevant alternative origin/browser before more source swaps. Keep the real parent identity; report the result only for the tested environment. | Media diagnosis |
| A source plays in a regular browser but its frame never becomes ready in an in-app browser | Distinguish environments; bound player readiness separately from API loading, offer recovery and suppress late callbacks. | Media lifecycle |
| Returning from a related lesson recreates a paused recording | Verify settled position, pause state, rate and loop against actual media; seeking a cued player may start it. | Shared playback state |
| A local preview hostname changes after preferences and markers exist | Preserve origin-scoped data, keep existing destination settings, and verify migration rather than silently resetting it. | Preview-origin migration |
| A shared audio API was fixed but the browser still uses an old imported module | Check the loaded entrypoint/dependency revision before changing the implementation again. | Runtime evidence |
| Existing static page needs a small spacing correction | Check the affected view; do not introduce a media/browser matrix or migration workflow. | Nearby non-trigger case |

## Evidence decisions

- **Adopt:** the sample checkpoints and task-specific resource selection; extend the
  existing steering owner instead of adding another broad skill.
- **Conditional:** third-party code, MCP access and motion skills. Inspect current
  availability, license, dependencies, cost and overlap for the chosen item.
- **Already covered:** one design lead, user references first, representative slices,
  ordinary-language feedback and project-local decisions. Preserve these rules.
- **Reference only:** vendor claims about taste, quality or speed. The review verified
  documented capabilities, not comparative results or specific designers' usage.
- **Defer:** the rest of the supplied top-20 list until a task needs it and its current
  official source has been checked. Do not impose a ranking or six-site sequence.

Official source URLs and the review date live in
[visual-resources.md](../skills/route-ui-work/references/visual-resources.md).
The source review did not exercise authenticated MCP access, install libraries, or
measure motion timing. Subsequent project work must verify those outcomes separately.
