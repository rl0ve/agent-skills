---
name: design-router
description: Routes UI, UX, frontend, design-review, motion, design-to-code, component-library, and interface-copy work through a canonical researched skill catalog and the capabilities actually installed. Use when several design skills could match, when choosing or comparing a UI skill stack, when an audience or surface changes the right design approach, when named families such as Taste, Hallmark, Impeccable, Meng, Emil, Jakub, or Addy must be distinguished, or when a missing design capability must be discovered safely. Honor an explicitly named skill and do not add layers unless they solve a distinct need.
---

# Design Router

Select one design lead, add only the specialist layers the task actually needs, and apply audience-specific craft constraints before implementation. Preserve two separate truths: the **canonical researched chain** and the **available chain in the current environment**. Never erase the former merely because a dependency is not installed.

## Route the request

1. **Honor explicit choices.** Preserve any user-selected skill, framework, model, aesthetic, reference, scope, or fidelity requirement.
2. **Classify two axes.** Read [references/taxonomy.md](references/taxonomy.md), then assign:
   - one primary `surface`;
   - one `audience`, or `audience-agnostic` only when the task truly has no user-facing outcome.
3. **Clarify only consequential ambiguity.** Ask one short question when two plausible classifications would produce materially different work. Otherwise state the assumption and continue.
4. **Compose the canonical chain.** Read the matching surface section in [references/chains.md](references/chains.md). Choose one named lead and zero to three named layers. Each layer must own a different concern.
5. **Resolve provenance and availability.** Inspect the live skill/tool catalog. Read the matching entries in [references/catalog.md](references/catalog.md). Mark every canonical entry as `installed`, `equivalent available`, or `missing candidate`; never imply that a catalog entry is installed merely because it is documented here.
6. **Substitute only transparently.** An installed equivalent may replace a missing canonical skill when it covers the same role. Announce the substitution and keep the canonical chain visible. If no credible equivalent exists, follow [references/discovery.md](references/discovery.md); do not silently dilute the route.
7. **Apply audience rules.** Read only the selected audience section in [references/audiences.md](references/audiences.md).
8. **Run the available chain.** Read each selected installed skill's complete `SKILL.md` and its required references before acting. The selected implementation skill owns its workflow.
9. **Validate.** Apply [references/quality-gates.md](references/quality-gates.md) before declaring completion.

## Selection order

Use this priority:

1. Explicit user choice.
2. Canonical role and chain from the researched catalog.
3. The exact canonical skill when installed.
4. An installed official, vendor, bundled, or focused community equivalent, with the substitution stated.
5. A verified external candidate, recommended but not installed automatically.

Do not stack two broad aesthetic directors. A broad lead may be paired with focused layers for accessibility, motion, copy, design systems, performance, or review.

## Guardrails

- **B2B/internal creative mismatch:** If `b2b-saas` or `internal-tool` is paired with `creative-expressive`, ask whether to use restrained-but-distinctive treatment or proceed with full expression against the router's recommendation.
- **Review stays read-only:** `review-audit` produces findings unless the user also asks for fixes.
- **Motion stays scoped:** `motion-only` must not restyle layout, color, type, or copy.
- **Reference fidelity wins:** `image-to-code` preserves the reference. Extract tokens, persist the reference, build in bounded sections, and compare each section before moving on.
- **No silent installs:** If a capability is missing, read [references/discovery.md](references/discovery.md), verify the upstream source, and give the install option. Install only when the user asks.
- **No false precision:** Popularity, stars, and install counts are discovery signals, not proof of quality, safety, or fit.
- **No catalog erasure:** A locally available fallback does not replace the research record. Preserve Taste, Hallmark, Impeccable, interface-design, Emil, Meng, Jakub, Addy, extraction, writing, marketing, and component families in the reported route whenever they are the canonical fit.

## Facilitate optional installs

When the user explicitly asks to install a documented dependency, use the bundled companion installer:

```bash
python3 scripts/install_optional_skills.py --list
python3 scripts/install_optional_skills.py --skill taste
python3 scripts/install_optional_skills.py --skill taste --execute
```

The selection command without `--execute` is a read-only plan. Show the user the exact upstream source and command before executing it. Never add `--yes` or `--allow-hooks` unless the user explicitly approves that behavior. The installer refuses root and `sudo`, never evaluates a shell string, and stops on the first failed dependency. Profiles are convenience selections, not permission to install an entire ecosystem.

## Announce the route

Before implementation, emit one compact line:

```text
Detected: <surface> × <audience> | Canonical: <lead> → <0-3 layers> | Guardrails: <short list>
```

Then report the executable route:

```text
Available now: <installed lead> → <installed layers> | Substitutions: <none or explicit mapping>
```

If something is missing, add:

```text
Missing: <capability> | Verified candidate: <source> | Install requires approval: yes
```

## Visual references

Two polished, text-bearing Imagegen field cards are bundled under `assets/source-visuals/`:

- `ui-design-router-named-skill-chains-2026-08-16.png` is the compact task-first matrix for the five most common UI surfaces plus motion and systems specialists.
- `ui-skill-directory-provenance-2026-08-16.png` maps the major named skills to upstream repositories and roles, and makes clear that `audit`, `critique`, `normalize`, and `delight` are Impeccable commands.

Use the field cards for fast visual recall. Use `references/chains.md` and `references/catalog.md` as the authoritative detailed record when an exact route, status, or source matters.

## Finish with evidence

Report:

- files or surfaces changed;
- checks performed;
- meaningful differences from the reference or prior confirmed state;
- assumptions and unresolved risks.
- canonical skills that were unavailable and any substitutions used.
