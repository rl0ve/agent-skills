# Visual Version Review

Compare existing UI implementations when branches, previews and saved screenshots are
becoming hard to track. The skill inventories each version, captures equivalent
screens and puts them in one HTML review with source labels and expandable images.

## What it produces

- A version inventory with branch, commit, entry path and capture provenance.
- Matched opening, browsing, detail and mobile views where evidence is available.
- Dedicated views for distinctive features such as globes, maps, charts or media.
- One comparison page with an all-views mode, filters and full-size inspection.
- Component-level preferences when requested, with review decisions kept separate
  from permission to implement, merge or revert.

An offline HTML file embeds its media and fonts and is tested without networking.
Historical captures and missing states remain labeled. Motion claims need clips or
exercised controls; still screenshots alone do not establish interaction behavior.

## Use

```text
Use Visual Version Review to compare these implemented branches.
Include the opening, globe, article reader and mobile views in one HTML page.
```

The skill stays in the active host and model. It needs access to source implementations
or authentic captures and the host's normal browser and HTML authoring tools; it does
not require a specific paid service or additional plugin.

## Install

```bash
# Codex
codex plugin marketplace add rl0ve/agent-skills
codex plugin add visual-version-review@rl0ve-agent-skills

# Claude Code
claude plugin marketplace add rl0ve/agent-skills
claude plugin install visual-version-review@rl0ve-agent-skills
```

For the local repository installer, `python3 install.py --plugin versions` prints
the Claude installation plan. Add `--execute` only when ready to run it.

## Boundaries

Visual Version Review compares implementations that exist. Capability Storyboard
organizes a demo narrative; Clear Assessment Guides handles broader assessments and
issue triage. Those plugins remain independent and are not required dependencies.

Keep project captures, inventories and decisions in the consuming project. The shared
skill contains only reusable guidance. It does not automatically install itself,
publish previews, switch models or change product code.
