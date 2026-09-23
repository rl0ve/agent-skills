---
name: route-ui-work
description: Route UI, UX, frontend, design review, motion, design-to-code, component-library, and interface-copy work through the researched skill catalog and live installed capabilities. Includes project-specific reference research, visual and component samples at useful decision points, iteration steering, and implementation-resource selection. Honor explicitly named skills and avoid unnecessary stacking.
compatibility: Codex and Claude Code with Agent Skills and plugin support.
---

# Route UI Work

Select one design lead, add only focused layers that own distinct concerns, and apply audience constraints before implementation. Preserve the canonical researched chain even when the executable chain uses a substitute.

## Route the request

For a small defined change within an established design, use the existing owner and
read only the guidance needed for the affected region. Do not run the full classification,
capability-inventory or sample-selection sequence for a mechanical typo, token or
contrast correction. Creating or rewriting prose needs the copy ownership below; a
mechanical correction does not require a new semantic-owner/editor handoff.

1. Honor explicit skill, model, framework, aesthetic, reference, fidelity, and scope choices.
2. Read [references/taxonomy.md](references/taxonomy.md) and classify one primary surface plus one audience from this project's purpose. Do not inherit an audience or aesthetic from the user's profession, previous projects, or use of AI to build.
3. Ask one short question only when two plausible classifications produce materially different work.
4. Read only the matching surface in [references/chains.md](references/chains.md). Choose one named lead and zero to three focused layers. If prose is being created or rewritten, use one semantic or brand owner followed by one final editor; never stack multiple humanizers.
5. Inspect capabilities in the current host, starting with skills and tools listed in this session. In Codex inspect project/user `.agents/skills`, `.codex/skills`, and enabled plugins as needed. In Claude Code inspect `.claude/skills` and `claude plugin list --json`. Record the chosen lead's provider and exact skill path, not only its display name: same-named originals and derivatives can contain different aesthetic rules. File presence does not prove an executable, MCP connection, or current-session skill is available.
6. Read matching entries in [references/catalog.md](references/catalog.md). Mark each canonical entry as `installed`, `equivalent available`, or `missing candidate`.
7. Substitute transparently. Never rename Anthropic `frontend-design` or another fallback as Taste, Hallmark, Interface Design, or Impeccable.
8. Read only the selected section in [references/audiences.md](references/audiences.md).
9. Load the complete selected skill instructions and the supporting files required for the chosen workflow. For external specialists, apply [references/upstream-skills.md](references/upstream-skills.md); a catalog link or router summary is not a loaded skill. Do not load the whole catalog into context.
10. Apply [references/quality-gates.md](references/quality-gates.md) before declaring completion. For broad visual reviews, including explicit Impeccable invocations, its rendered readability and composition pass is required alongside technical auditing; a technical pass alone cannot justify an overall quality score.

## Help the user establish design direction

For a substantial new design or redesign with unresolved visual direction, a consequential
component choice, or an iteration with materially different interpretations, read
[references/design-steering.md](references/design-steering.md). Infer a short brief,
show actual references or comparable previews when useful, translate plain-language feedback,
and establish a representative slice before costly expansion. That reference also
covers conditional imagegen-to-code comparisons when visual direction remains unsettled. Keep chosen direction
in project notes. Clear references, established systems and small defined edits stay
direct; do not require a prompting method, questionnaire or repeated approval rounds.

## Improve an existing experience

For improvements to an existing site/app or feedback that a redesign lost useful
content, brand, messaging or interactions, read
[references/existing-site-improvements.md](references/existing-site-improvements.md).
Before a substantial revision or recovery from a rejected redesign, reconcile the
accumulated brief and make the reference's before-editing check explicit. Start from
what works, prioritize the largest observed obstacle, and compare the candidate with
the original visitor journey. Keep small defined edits scoped; an explicit rebrand
can justify a broader change.

## Product decisions before polish

For a broad redesign or unexplained usability problem, read
[references/product-decisions.md](references/product-decisions.md). Identify whether
the unresolved decision concerns user evidence, product objects and states, interaction
flow, or visual presentation. Address the relevant layer with the existing lead;
use a focused specialist only when needed. Do not impose a discovery workshop on a
defined visual edit or invent user research to fill gaps.

## Preserve the requested art direction

For a named visual reference, expressive redesign, or feedback that the result feels
generic, dull, too muted, or repeatedly uses the same palette, read
[references/art-direction.md](references/art-direction.md). Resolve skill identity and
conflicting aesthetic heuristics before implementation. Preserve product purpose
separately from old styling, make the palette and motion choices explicit, and compare
the implemented experience with the requested traits. An editorial audience does not
imply a conservative newspaper aesthetic. A working flow and a list of references do
not by themselves establish that the requested visual direction was delivered.

## Upstream specialist workflows

Prefer the complete selected upstream workflow when its distinctive method fits.
UI Router owns selection and shared checks; specialists own detailed execution.
Use [references/upstream-skills.md](references/upstream-skills.md) for exact Meng and
Dream Loop entrypoints, selective loading/installation, and clearly labeled adaptations.

## Graphical and interactive builds

For substantial graphical apps, scenes, creative tools or expressive sites, select a
suitable [upstream specialist](references/upstream-skills.md), including Dream Loop when
high graphical fidelity calls for its target/build/critique method. The lighter
[visual build loop](references/visual-build-loop.md) is an adaptation for proportionate
work or a stated fallback, not an equivalent replacement for a selected specialist.
For realistic interactive 3D, apply the focused [spatial checks](references/spatial-realism.md)
when assets, lighting, interface framing or delivery are the unresolved concern.
Pair appearance with an exercised user action, keep generated targets distinct from
working output, and verify assets in the destination. For spatial entrances and sound/media experiences,
preserve the route into the real task and apply the relevant
[motion and media checks](references/motion-quality.md). A public page can also be
the working product; use the hybrid case in the taxonomy and the focused question
examples in design steering when intent remains consequentially unclear. Small edits
and settled designs stay direct.

## Inspiration sources and visual resources

For inspiration, substantial new visual work with unresolved direction, motion references, creative editors, or component sourcing, read only the matching section of [references/visual-resources.md](references/visual-resources.md). It maps sources to design questions, access boundaries and upstream documentation. Clear references, settled direction and small defined edits do not require a broad search.

- Start from the user's reference; otherwise choose one or two relevant references. Record what each contributes before implementing.
- Use ThreeUI Community for procedural 3D examples, Toolcraft for a canvas with creative controls, and Canvas UI for a specific GPU effect. They are implementation resources, not additional aesthetic directors.
- Treat Neuform and Aura as exploration, prototype and handoff tools. Their generated or exported HTML can provide a visual direction and implementation reference, but does not establish a clean import into a CMS or a maintainable page-builder edit. Recreate the selected structure in the destination and verify it there.
- Treat ThreeUI Pro as an entitled source-delivery route for a compatible code project, not a native CMS component library. Keep any selected spatial scene bounded, preserve a readable fallback, and test the destination's actual runtime.
- For an exported product video or animated explainer, consider HyperFrames' free local renderer. A website animation and a rendered video need different validation; select the output route first.
- For product screens and flows consider Mobbin or Refero; inspect available connector tools before assuming access is missing. Consider 21st.dev for component samples and selected code, Component Gallery for conventions, and the resource map for expressive and editorial references. Select AI-interface examples only when the product exposes AI behavior.
- Choose motion references by behavior: product feedback, page/scroll choreography, experimental interaction, small interaction details, or spatial 3D. Use the matching resource-map row and inspect actual motion; screenshots alone do not establish timing or gestures.
- Keep dependencies project-local and add only what the chosen output needs. A resource catalog entry is not an installed plugin. A Blender workflow skill is not the Blender application.
- For resource recommendations or access problems, distinguish free code, account-free tools, free account allowances, paid upgrades and separate execution costs. Use the resource map's access guidance and a relevant live check; a useful resource is not automatically a purchase or a required signup.
- Honor an explicit free-only constraint: public browsing, verified free code and free allowances are eligible; paid MCPs, trials that require billing and usage that incurs charges are not. Existing user authorization covers the agreed install scope; do not ask again solely because an installer is plan-first.
- A previous tool failure does not establish continuing unavailability. Retry an already configured and authorized connected service when it is relevant, then record the current result. Keep account status session-scoped.

In Codex, use Work Router's Codex table or stay in the parent. The Claude agent names and model defaults below apply only in Claude Code.

## Claude execution routes

When the Work Router is installed, apply its work route after composing the UI skill chain. Otherwise use these defaults:

| UI work | Agent | Model | Effort |
|---|---|---|---|
| Route discovery, inventory, and reference mapping | `ui-router:ui-scout` | Sonnet | medium |
| Defined UI implementation | `ui-router:ui-builder` | Opus | low |
| Consequential visual, accessibility, or system review | `ui-router:ui-critic` | Opus | high |

Keep trivial UI adjustments in the parent. In Codex, follow Work Router's model policy:
GPT-6 Sol for substantial design reasoning and broad implementation; GPT-6 Astra for
the hardest creative/spatial judgment, unresolved quality-first direction, or a
demonstrated Sol capability limit; GPT-6 Luna for narrow objectively verifiable work.
GPT-5.6 Terra is a conditional reference/evidence reader, not the final visual judge.
Preserve explicit model choices and a progressing capable parent. No current four-model
benchmark establishes the best visual taste or fastest accepted design. UI Router still
owns the design chain, rendered comparison and exercised interaction. A model release
does not justify 3D, image generation or subagents. These Claude profiles do not switch
the parent.

For Codex effort selection, **Sol high** fits substantial implementation with a settled
direction; **Sol xhigh** fits unusually deep implementation reasoning within Sol.
**Astra high** is the usual starting point for difficult unresolved creative/spatial
direction; **Astra xhigh** fits exceptionally demanding judgment or tradeoffs. Either
xhigh route can be selected upfront when warranted. No failed Sol attempt or automatic
max/ultra escalation is required. Apply Work Router's task-dependent latency/token
tradeoffs and contextual timing check; do not ask a second timing question here.

**Do not raise Sonnet above medium to get a better UI build.** Opus at low effort is the
implementation route because the Sonnet effort rungs above medium cost more than Opus low
without matching it. Use Sonnet low or medium for the mechanical tail: token renames,
copy swaps, class cleanups, test and story files, and any surface where a plan already
exists and latency matters more than judgment. When `ui-builder` stalls or thrashes,
raise it to Opus medium rather than reaching for a different family.

Watch two things on Opus low: replies stay long, and it delegates to subagents readily.
Give `ui-builder` an exact file map and hold it to sole-writer scope so that eagerness
does not turn into a second writer in the tree. See Work Router's
`references/routing-policy.md` for the basis and its limits.

## Selection order

1. Explicit user choice.
2. Canonical role and chain from the research catalog.
3. Exact selected skill when installed, or its verified complete upstream workflow
   loaded as task context when appropriate. Preserve a distinctive method that fits.
4. A compatible installed substitute or scoped adaptation when warranted; state why
   and do not imply equivalent results without evidence.
5. Install a selected verified skill for repeated use only within explicit current
   or prior user authorization; preserve its required supporting files.

Do not stack two broad aesthetic directors. A broad lead can pair with focused accessibility, motion, copy, system, performance, or review layers.

## Guardrails

- **Audience fit:** identify a concrete conflict with task completion, legibility, performance or user intent before challenging expression. A B2B/internal label alone is not a mismatch; honor explicitly requested creative direction while preserving the task's requirements.
- **Review stays read-only:** review or audit produces findings unless the user also requests fixes.
- **Motion stays scoped:** motion-only work must not restyle layout, color, typography, or copy.
- **Reference fidelity wins:** image-to-code follows extraction, capture, bounded implementation, and comparison.
- **Aesthetic heuristics are not user requirements:** generic anti-pattern advice must not veto the user's chosen colors, effects, or references. Resolve an incompatible lead or layer instead of silently substituting a safer house style.
- **No silent installs:** present the source and exact plan; execute within explicit current or prior user authorization. Do not request the same permission again.
- **No catalog erasure:** a locally available fallback does not remove the original named research entry.
- **One final editor:** verify the companion Natural Writing plugin before routing to it. When available, it is the sole anti-slop and voice-preserving editor. If unavailable, select exactly one documented fallback; never run sequential humanizer passes.
- **Copy boundaries:** the UX, product, or marketing layer owns labels, states, claims, requirements, and terminology. Natural Writing improves the prose without inventing behavior or altering supported meaning.
- **No `sudo`:** both plugin hook and installer reject privileged execution.

## Discover a missing capability

Read [references/discovery.md](references/discovery.md) when a capability is missing
or the user asks for newer skills. Use Work Router's `discover-capabilities` when
available for the general search, then apply the UI-specific checks. The reference
also provides a standalone fallback; neither plugin requires the other to be installed.

## Optional skill installs

Use `/ui-router:install-ui-stack` only when the user explicitly asks to install skills. The companion script is plan-first:

```bash
python3 scripts/install_optional_skills.py --list
python3 scripts/install_optional_skills.py --skill taste
python3 scripts/install_optional_skills.py --profile product
```

Nothing runs without `--execute`. Do not add `--yes` or `--allow-third-party-hooks` unless the user explicitly requested that behavior.

## Announce the route

Before substantive implementation, emit:

```text
Detected: <surface> x <audience> | Canonical: <lead> -> <layers> | Available: <lead> -> <layers> | Substitutions: <none or mapping>
```

If a capability is missing, add:

```text
Missing: <capability> | Candidate: <verified source> | Authorization: <already granted within scope / needed>
```

## Visual references

The plugin bundles two text-bearing field cards under `assets/source-visuals/`:

- `ui-design-router-named-skill-chains-2026-08-16.png` for task-first chains;
- `ui-skill-directory-provenance-2026-08-16.png` for named ownership and provenance.

Use the cards for recall. Use `references/chains.md` and `references/catalog.md` as the detailed authority.

## Finish with evidence

Report changed surfaces, checks, meaningful deviations, assumptions, unavailable canonical skills, and explicit substitutions.
