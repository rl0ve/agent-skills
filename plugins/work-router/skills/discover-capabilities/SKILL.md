---
name: discover-capabilities
description: Find and evaluate missing agent skills, plugins, or integrations when the user asks to extend capabilities or an installed capability cannot cover the task. Check existing capabilities, compare current sources, and avoid duplicate installs.
---

# Discover capabilities

Own the general discovery process across domains. Work Router chooses execution;
UI Router chooses the design lead and focused layers. Neither requires a new install
when an existing capability or direct work can finish the task.

## Start from the missing outcome

Identify the task, host and actual gap. Check session-listed skills and tools first,
then relevant enabled plugins and project/user skill paths. Installed files, enabled
plugins, authenticated tools and capabilities loaded in this session are different
states. Do not scan every directory or tool on ordinary tasks.

Separate reusable instructions (skills), packages of skills/tools (plugins), live
integrations (often MCP), and implementation libraries or assets. A workflow skill
does not install its application. For UI work, use UI Router when available to choose
the domain lead; its visual resource map covers assets and inspiration.

## Choose sources by the question

Sources checked September 5, 2026; verify current upstream details for each candidate.

| Need | Start here | Expand only if useful |
|---|---|---|
| A specific skill | [skills.sh](https://skills.sh/) | [SkillsMP](https://skillsmp.com/) for broader public examples |
| A plugin or integration | The current host's official plugin catalog; [Claude Code official marketplace](https://github.com/anthropics/claude-plugins-official) for Claude | [Skillselion](https://skillselion.com/) for skills, marketplaces and MCP discovery |
| Explore an unfamiliar category | [Skillselion](https://skillselion.com/) | SkillsMP or a domain curator |
| What's gaining attention | [Skill Leaderboard](https://skillleaderboard.com/) | Optional trend research, never a required install step |
| Verify a candidate | The creator's exact upstream repository | Current host/vendor documentation |

This is a conditional search workflow, not a federated crawler. Do not query every
source by default. SkillsMP indexes examples without certifying quality or safety.
Install counts, stars and leaderboard rank are leads, not evidence of task quality.

If the installed `find-skills` helper is useful, use it for skills.sh lookup and
current CLI syntax; do not launch a second full discovery pass. Its popularity
heuristics do not replace source inspection or exclude a well-supported niche skill.
The upstream [Skills CLI](https://github.com/vercel-labs/skills) supports
`npx skills find <keywords>`; check current syntax before installing.

## Evaluate and adopt

- Inspect the exact owner, complete SKILL.md, executable scripts, hooks, permissions,
  current activity/issues, license, host compatibility and update mechanism.
- Compare scope with installed capabilities. Prefer one owner per concern. A useful
  method may be a narrow improvement to an existing skill instead of another plugin.
- Distinguish free code from paid APIs, subscriptions or billing-required trials.
  Honor the user's cost constraints and existing authorization.
- Normally return at most three candidates with the missing capability, source,
  fit, meaningful overlap, cost and recommended action. State when none is needed.
- For an authorized install, state the exact package/source and scope, then proceed.
  Do not ask again for permission already granted; no authorization is implied by a
  directory rank. Prefer project-local evaluation when suitable.
- Verify with a representative task. Report installed, enabled and loaded separately;
  a package check is not proof that a workflow improves outcomes.

## Resolve overlaps without blanket disabling

Check actual enablement and loaded instructions; a stale config entry or a matching
name alone is insufficient. Distinguish duplicate copies of the same skill, competing
broad workflow owners, and complementary specialist skills or authenticated tools.
Recommend keeping one maintained canonical router per concern. Do not disable a
useful specialist merely because another plugin covers a related domain. A request
to inspect conflicts is read-only; change enablement only within authorized scope.

Treat outside advice as dated evidence. Verify the original source and current
support before adopting a reusable method, and do not import promotional claims,
old model rankings, or arbitrary popularity thresholds as policy.
