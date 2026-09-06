---
name: route-ui-work
description: Route UI, UX, frontend, design review, motion, design-to-code, component-library, and interface-copy work through the researched skill catalog and live installed capabilities. Includes project-specific reference research, visual and component samples at useful decision points, iteration steering, and implementation-resource selection. Honor explicitly named skills and avoid unnecessary stacking.
compatibility: Codex and Claude Code with Agent Skills and plugin support.
---

# Route UI Work

Select one design lead, add only focused layers that own distinct concerns, and apply audience constraints before implementation. Preserve the canonical researched chain even when the executable chain uses a substitute.

## Route the request

1. Honor explicit skill, model, framework, aesthetic, reference, fidelity, and scope choices.
2. Read [references/taxonomy.md](references/taxonomy.md) and classify one primary surface plus one audience from this project's purpose. Do not inherit an audience or aesthetic from the user's profession, previous projects, or use of AI to build.
3. Ask one short question only when two plausible classifications produce materially different work.
4. Read only the matching surface in [references/chains.md](references/chains.md). Choose one named lead and zero to three focused layers. If prose is being created or rewritten, use one semantic or brand owner followed by one final editor; never stack multiple humanizers.
5. Inspect capabilities in the current host, starting with skills and tools listed in this session. In Codex inspect project/user `.agents/skills`, `.codex/skills`, and enabled plugins as needed. In Claude Code inspect `.claude/skills` and `claude plugin list --json`. Record the chosen lead's provider and exact skill path, not only its display name: same-named originals and derivatives can contain different aesthetic rules. File presence does not prove an executable, MCP connection, or current-session skill is available.
6. Read matching entries in [references/catalog.md](references/catalog.md). Mark each canonical entry as `installed`, `equivalent available`, or `missing candidate`.
7. Substitute transparently. Never rename Anthropic `frontend-design` or another fallback as Taste, Hallmark, Interface Design, or Impeccable.
8. Read only the selected section in [references/audiences.md](references/audiences.md).
9. Load the complete selected skill instructions before using them. Do not load the whole catalog into context.
10. Apply [references/quality-gates.md](references/quality-gates.md) before declaring completion.

## Help the user establish design direction

For a substantial new design or redesign with unresolved visual direction, a consequential
component choice, or an iteration with materially different interpretations, read
[references/design-steering.md](references/design-steering.md). Infer a short brief,
show actual references or comparable previews when useful, translate plain-language feedback,
and establish a representative slice before costly expansion. Keep chosen direction
in project notes. Clear references, established systems and small defined edits stay
direct; do not require a prompting method, questionnaire or repeated approval rounds.

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

## Inspiration sources and visual resources

For inspiration, substantial new visual work with unresolved direction, motion references, creative editors, or component sourcing, read only the matching section of [references/visual-resources.md](references/visual-resources.md). It maps sources to design questions, access boundaries and upstream documentation. Clear references, settled direction and small defined edits do not require a broad search.

- Start from the user's reference; otherwise choose one or two relevant references. Record what each contributes before implementing.
- Use ThreeUI Community for procedural 3D examples, Toolcraft for a canvas with creative controls, and Canvas UI for a specific GPU effect. They are implementation resources, not additional aesthetic directors.
- For an exported product video or animated explainer, consider HyperFrames' free local renderer. A website animation and a rendered video need different validation; select the output route first.
- For product screens and flows consider Mobbin or Refero; inspect available connector tools before assuming access is missing. Consider 21st.dev for component samples and selected code, Component Gallery for conventions, and the resource map for expressive and editorial references. Select AI-interface examples only when the product exposes AI behavior.
- Choose motion references by behavior: product feedback, page/scroll choreography, experimental interaction, small interaction details, or spatial 3D. Use the matching resource-map row and inspect actual motion; screenshots alone do not establish timing or gestures.
- Keep dependencies project-local and add only what the chosen output needs. A resource catalog entry is not an installed plugin. A Blender workflow skill is not the Blender application.
- Honor an explicit free-only constraint: public browsing and verified free code are eligible; paid MCPs, trials that require billing, and metered services are not. Existing user authorization covers the agreed install scope; do not ask again solely because an installer is plan-first.

In Codex, use Work Router's Codex table or stay in the parent. The Claude agent names and model defaults below apply only in Claude Code.

## Claude execution routes

When the Work Router is installed, apply its work route after composing the UI skill chain. Otherwise use these defaults:

| UI work | Agent | Model | Effort |
|---|---|---|---|
| Route discovery, inventory, and reference mapping | `ui-router:ui-scout` | Sonnet | medium |
| Defined UI implementation | `ui-router:ui-builder` | Sonnet | high |
| Consequential visual, accessibility, or system review | `ui-router:ui-critic` | Opus | high |

Keep trivial UI adjustments in the parent. Use Fable only for a connected, long-horizon multi-surface or design-system transformation that truly benefits from sustained autonomy.

## Selection order

1. Explicit user choice.
2. Canonical role and chain from the research catalog.
3. Exact canonical skill when installed.
4. Installed official, vendor, bundled, or focused community equivalent, with the substitution stated.
5. Verified external candidate; install only within explicit current or prior user authorization.

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
