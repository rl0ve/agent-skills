# agent-skills

Nine plugins of agent skills for Codex and Claude Code. Each plugin installs in both
hosts from one shared source; where the hosts differ, the shared file says so instead
of forking.

## Plugins

| Plugin | What it does |
|---|---|
| [Work Router](plugins/work-router/README.md) | Decides whether work stays in the parent session or goes to a bounded subagent, and at which model and effort. One method, a route table per host. Also audits the skills ecosystem against bookmarks, stars, and current discussion. |
| [UI Router](plugins/ui-router/README.md) | Routes UI, UX, design review, motion, design-to-code, interface copy and real-time 3D work to the right specialist skills and checks the result in a browser. |
| [Natural Writing](plugins/natural-writing/README.md) | Edits, rewrites, voice-matches or drafts prose while keeping facts, terminology and the author's voice. Includes a linter. |
| [UI Walkthrough Video](plugins/ui-walkthrough-video/README.md) | Records real interface flows and turns them into narrated MP4s with captions. Needs browser and media runtimes. |
| [Capability Storyboard](plugins/capability-storyboard/README.md) | Builds an HTML storyboard for a keynote or demo, with a talk track and director's notes per scene. |
| [Deck Builder](plugins/deck-builder/README.md) | Builds `.pptx` decks on your own template and verifies them by rendering slides. |
| [Clear Assessment Guides](plugins/clear-assessment-guides/skills/clear-assessment-guides/SKILL.md) | Produces source-backed assessments, one-issue walkthroughs, or interactive HTML reviews with comments and decisions. |
| [Research Reports](plugins/research-reports/README.md) | Investigates a consequential question and builds an evidence-backed report with selected explanatory visuals and an optional motion overview. Defaults to one primary document format. |
| [Visual Version Review](plugins/visual-version-review/README.md) | Compares implemented branches and previews in one labeled HTML page, with matched captures, distinctive visuals and full-size inspection. |

### When two plugins could apply

| You want to | Use |
|---|---|
| Choose which implemented version, or which parts of each, to keep | Visual Version Review |
| Explain what is wrong and what to change, including a before/after of one change | Clear Assessment Guides |
| Investigate a strategic question or prepare a deep research report for a meeting | Research Reports |
| Track comments on a rendered page through to a verified fix | UI Router |
| Plan a keynote or demo with mockups and a talk track | Capability Storyboard |
| Record a narrated video of the real product | UI Walkthrough Video |
| Build or fix slides | Deck Builder |

These hand off to each other. A before/after in an assessment can use Visual Version
Review's capture rules, and a storyboard's talk track can become a walkthrough script.

## Install

```bash
# Claude Code
claude plugin marketplace add rl0ve/agent-skills
claude plugin install ui-router@rl0ve-agent-skills

# Codex
codex plugin marketplace add rl0ve/agent-skills
codex plugin add ui-router@rl0ve-agent-skills
```

Use any folder name under `plugins/` in place of `ui-router`. In Claude Code, restart or
run `/reload-plugins` afterward.

**From a local clone (Claude Code).** `install.py` prints its plan and runs nothing
until you add `--execute`:

```bash
python3 install.py --plugin all              # review the plan
python3 install.py --plugin all --execute    # run it
```

Choose a subset with repeated `--plugin` flags: `ai`, `ui`, `writing`, `video`,
`storyboard`, `deck`, `assessment`, `research`, `versions`.

**Try one plugin without installing:**

```bash
claude --plugin-dir ./plugins/work-router
```

**Optional UI skills.** UI Router never installs its catalog silently. List or plan a
profile, then execute explicitly (also available as `/ui-router:install-ui-stack`):

```bash
python3 plugins/ui-router/scripts/install_optional_skills.py --list
python3 plugins/ui-router/scripts/install_optional_skills.py --profile product --execute
```

**Safety.** Work Router and UI Router ship a hook that blocks Bash commands containing
`sudo`. Every installer refuses to run as root and never evaluates a shell string.

## Model routing

To carry the same personal workflow between machines, explicitly select and apply a
[portable preference profile](plugins/work-router/skills/route-ai-work/references/portable-preferences.md)
after installing Work Router. The included `rl0ve` profile supports Codex and Claude
Code, preserves unrelated local instructions, and provides a repeatable drift check.
Each machine or remote environment needs setup; plugin installation alone does not
activate personal preferences or synchronize account settings.

Work Router owns model and effort choice. Reviewed October 2026:

- **Codex:** GPT-6.1 Sol for substantial work (medium, high when complex), GPT-6 Astra
  for maximum capability, GPT-6 Luna for narrow work with objective checks. Fast and
  Ultrafast service tiers are opt-in only.
- **Claude Code:** Opus 5.5 at medium for substantial work, high for hard diagnosis and
  consequential review; Sonnet for defined implementation; Haiku for scouting; Fable on
  explicit preference.
- Host-sensitive workflows stay in the host you are in unless you name another model.

See the [task-by-task routes](plugins/work-router/README.md#task-by-task-starting-routes)
and the agent-facing [route-ai-work skill](plugins/work-router/skills/route-ai-work/SKILL.md).

## Managed environments

- **Claude Code admins** can restrict models, effort, marketplaces and plugins; the
  routers follow those limits. Settings patterns are in [ADMIN.md](ADMIN.md).
- **ChatGPT workspace admins** can import this repository as a marketplace that syncs
  daily. Installation policy is set in the workspace, not by this repository. See
  [workspace import](ADMIN.md#chatgpt-and-codex-workspace-import).
- Because of the `sudo` hook, Work Router and UI Router are not eligible for OpenAI's
  public plugin directory; install them manually or through workspace import.

**Client versions.** Opus 5.5 needs Claude Code 2.1.280+. `haiku` means Haiku 5.5 only on
the Anthropic API with Claude Code 2.1.293+; Bedrock, Vertex and Foundry resolve it to
Haiku 4.5. Fable needs organizational access; without it, Work Router falls back to the
newest permitted Opus and says so.

## Repository layout

```
.claude-plugin/marketplace.json    Claude Code marketplace
.agents/plugins/marketplace.json   Codex marketplace
plugins/<name>/
  plugin.json                      portable manifest (Agent Plugins 1.0)
  .claude-plugin/plugin.json       Claude Code manifest
  .codex-plugin/plugin.json        OpenAI overlay (interface metadata)
  skills/<skill>/SKILL.md
```

All three manifests carry the same name, version and description. Agents working in
this repository read [AGENTS.md](AGENTS.md).

## Development

CI ([checks.yml](.github/workflows/checks.yml)) runs on every push and pull request.
Run the same checks locally before publishing:

```bash
(cd tests && python3 -m unittest)
(cd plugins/natural-writing/skills/natural-writing && python3 -m unittest discover -s tests)
(cd plugins/ui-walkthrough-video/skills/ui-walkthrough-video && python3 -m unittest discover -s tests)
for t in plugins/*/tests/*.mjs; do node "$t"; done
claude plugin validate . && for p in plugins/*/; do claude plugin validate "$p"; done
```

Publishing a commit does not refresh installed plugin caches. The release workflow is in
[skill maintenance](docs/skill-maintenance.md).
