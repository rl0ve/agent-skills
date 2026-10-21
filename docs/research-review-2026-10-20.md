# Bookmarks, stars and current-practice review

Reviewed October 20, 2026. This pass covered 193 saved X posts and 235 starred GitHub
repositories. Items already assessed in earlier reviews ([September 5](research-review-2026-09-05.md),
the UI Router reviews in `plugins/ui-router/docs/` and the Work Router benchmark reviews)
were not reassessed. It is a targeted review, not a survey or a benchmark. Adoption is a
routing judgment unless a test is named.

## Adopted

| Source | Assessment | Result |
|---|---|---|
| [Claude Code dynamic workflows](https://code.claude.com/docs/en/workflows) and [launch article](https://claude.com/resources/articles/introducing-dynamic-workflows-in-claude-code); anticipated in [Daniel Miessler's May 24 post](https://x.com/DanielMiessler/status/2058699741140222055) | **Adopt as a host feature.** Generally available on paid plans. It fits fan-out work and costs more tokens than a conversation. | Work Router 1.11.0: when to use it, per-task opt-in, sign-off stages, scoped first run. |
| [OpenAI GPT-6 Astra](https://openai.com/index/gpt-6-astra/), surfaced by [Gabriel Chua](https://x.com/gabrielchua/status/2096097151524978891) | **Conditional.** OpenAI announces cross-window notes as experimental; the [Codex configuration reference](https://developers.openai.com/codex/config-reference) still lists the setting as not currently available. | Work Router 1.11.0: check the client first; keep the file handoff when switching model, agent or host. |
| [Karpathy, October 2](https://x.com/karpathy/status/2105819303471976479), and [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf) | **Adopt as an opt-in register.** The rules come from the published standard; the readability benefit is a practitioner report. | Natural Writing 1.16.0: controlled English under technical documentation. |
| [EL4CTEO/blender-skills](https://github.com/EL4CTEO/blender-skills), from [Hakimi Eiqbal's post](https://x.com/hakimieiqbal/status/2111747882843873538) | **Trial.** MIT, Blender 5.2+, a pre-delivery QA skill; young (6 commits). | UI Router 1.21.0: trial layer in 3D specialists. |
| [Karpathy-style scripted Blender car animation](https://x.com/Lummox_eth/status/2111877394545975595) | **Adopt one check.** A door turning about the wrong axis breaks the result; the rest is already covered by the CLI-build rule. | UI Router 1.21.0: wrong-pivot check in the runtime-evidence gate. |
| [image-blaster](https://github.com/neilsonnn/image-blaster) ([post](https://x.com/BrooksWhaleX/status/2108393219663036667)) and [Scenario skills / GameDev OS](https://github.com/scenario-labs/skills) ([post](https://x.com/emmanuel_2m/status/2103097017073361137)) | **Conditional.** Both generate through paid services (World Labs and FAL; the Scenario MCP). | UI Router 1.21.0: listed with the generator-first packs that need authorization. |
| [OpenDesign](https://github.com/nexu-io/open-design) ([Motion post](https://x.com/OpenDesignHQ/status/2111440345032790310)) | **Conditional lead.** Apache 2.0; motion renders through HyperFrames, which the router already covers. | UI Router 1.21.0: motion-explainer lead row. |
| [VoiceStudio](https://github.com/debpalash/VoiceStudio) | **Unrated local candidate.** AGPL-3.0 app; model terms are separate. | UI Walkthrough Video 1.7.3: voice-choice row. |
| [Archify](https://github.com/tt-a1i/archify) | **Adopt as an alternative.** MIT; self-contained HTML diagrams; optional update check. | Clear Assessment Guides 1.1.1: supporting tools. |

## Not adopted

| Source | Reason |
|---|---|
| [Meng's paid-apps playbook](https://x.com/MengTo/status/2107862479548403806) and [Pika plugin art direction](https://x.com/MengTo/status/2111294425959923839) | Already covered: one reference per feature, generated targets before building, self-scoring with screenshots (fidelity loop and visual build loop). Pika is a paid generator; use it under the existing image-generation authorization rule. |
| [Peter Steinberger's 12-subagent QA prompt](https://x.com/steipete/status/2081169376317932017) and [graph-to-Codex method](https://x.com/steipete/status/2080779917130858598) | Covered by dynamic workflows, Codex subagents and the long-running guide. A target bug count is not an acceptance condition. |
| [Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | The user's skill set already includes its `understand` skills; no router change needed. |
| [Orca](https://github.com/stablyai/orca), [Conductor](https://github.com/conductor-oss/conductor), [xyflow](https://github.com/xyflow/xyflow), [DigUp](https://github.com/ARahim3/DigUp), [Helix Foundry](https://github.com/HelixDB/helix-foundry) | Agent-fleet, workflow-engine, UI-library and local-search products, not skills. Nothing to route. |
| [Remotion motion-graphics skill](https://github.com/Liamrjohnston/remotion-motion-graphics-skill) | Small and new; the router already uses official Remotion guidance and video-shotcraft. |
| [Genex](https://x.com/genex_games/status/2107148754633507237), [Mnimiy's 15-repo 3D list](https://x.com/Mnilax/status/2109716261160538324), three.js scene demos | Discovery only. The list's three.js, Blender MCP, World Labs and splat entries are already in the 3D route. |

## Validation scope

The repository tests, the plugin test suites, `claude plugin validate` and CI ran on the
change. Links were checked by the repository link test. No new skill was installed and
no tool above was executed.
