---
name: route-ui-work
description: Route UI, UX, frontend, design review, motion, design-to-code, component-library, and interface-copy work through the researched named skill catalog and the capabilities actually installed in Claude Code. Use when choosing or combining Taste, Hallmark, Interface Design, Impeccable, Emil, Jakub, Meng, Addy, ibelick, shadcn, frontend-design, or related UI skills. Honor explicitly named skills and avoid unnecessary stacking.
compatibility: Claude Code with Agent Skills and plugin support.
---

# Route UI Work

Select one design lead, add only focused layers that own distinct concerns, and apply audience constraints before implementation. Preserve the canonical researched chain even when the executable Claude Code chain uses a substitute.

## Route the request

1. Honor explicit skill, model, framework, aesthetic, reference, fidelity, and scope choices.
2. Read [references/taxonomy.md](references/taxonomy.md) and classify one primary surface plus one audience.
3. Ask one short question only when two plausible classifications produce materially different work.
4. Read only the matching surface in [references/chains.md](references/chains.md). Choose one named lead and zero to three focused layers. If prose is being created or rewritten, use one semantic or brand owner followed by one final editor; never stack multiple humanizers.
5. Inspect the live Claude Code environment:
   - installed plugins from `claude plugin list --json` when useful;
   - project skills under `.claude/skills/`;
   - user skills under `~/.claude/skills/` when access is permitted;
   - plugin skills already listed in the current session.
6. Read matching entries in [references/catalog.md](references/catalog.md). Mark each canonical entry as `installed`, `equivalent available`, or `missing candidate`.
7. Substitute transparently. Never rename Anthropic `frontend-design` or another fallback as Taste, Hallmark, Interface Design, or Impeccable.
8. Read only the selected section in [references/audiences.md](references/audiences.md).
9. Load the complete selected skill instructions before using them. Do not load the whole catalog into context.
10. Apply [references/quality-gates.md](references/quality-gates.md) before declaring completion.

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
5. Verified external candidate, recommended but not installed automatically.

Do not stack two broad aesthetic directors. A broad lead can pair with focused accessibility, motion, copy, system, performance, or review layers.

## Guardrails

- **B2B/internal creative mismatch:** pause when a full creative-expressive route conflicts with a B2B SaaS or internal-tool audience.
- **Review stays read-only:** review or audit produces findings unless the user also requests fixes.
- **Motion stays scoped:** motion-only work must not restyle layout, color, typography, or copy.
- **Reference fidelity wins:** image-to-code follows extraction, capture, bounded implementation, and comparison.
- **No silent installs:** present the source and exact plan; execute only after explicit user direction.
- **No catalog erasure:** a locally available fallback does not remove the original named research entry.
- **One final editor:** verify the companion Natural Writing plugin before routing to it. When available, it is the sole anti-slop and voice-preserving editor. If unavailable, select exactly one documented fallback; never run sequential humanizer passes.
- **Copy boundaries:** the UX, product, or marketing layer owns labels, states, claims, requirements, and terminology. Natural Writing improves the prose without inventing behavior or altering supported meaning.
- **No `sudo`:** both plugin hook and installer reject privileged execution.

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
Missing: <capability> | Candidate: <verified source> | Install requires approval: yes
```

## Visual references

The plugin bundles two text-bearing field cards under `assets/source-visuals/`:

- `ui-design-router-named-skill-chains-2026-08-16.png` for task-first chains;
- `ui-skill-directory-provenance-2026-08-16.png` for named ownership and provenance.

Use the cards for recall. Use `references/chains.md` and `references/catalog.md` as the detailed authority.

## Finish with evidence

Report changed surfaces, checks, meaningful deviations, assumptions, unavailable canonical skills, and explicit substitutions.
