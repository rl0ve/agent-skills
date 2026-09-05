# UI skill discovery and verification

Use this only when the user asks for newer skills or the required capability is
missing. General discovery belongs to `work-router:discover-capabilities` when that
skill is available. Run its process once, then apply the UI-specific checks here.
Do not assume a sibling plugin is installed or follow a hardcoded cache path.

## Standalone fallback

When Work Router is unavailable, check installed skills and tools first. Search
[skills.sh](https://skills.sh/) for a specific skill; use the current host's official
catalog for plugins and integrations. Use [Skillselion](https://skillselion.com/) for
category exploration, or [SkillsMP](https://skillsmp.com/) for broader examples when
needed. [Skill Leaderboard](https://skillleaderboard.com/) is optional trend browsing.
Do not query every directory. Inspect the exact upstream SKILL.md, scripts/hooks,
maintenance, license, cost, host support and overlap before adopting a candidate.
Popularity does not establish quality. Honor existing install authorization; otherwise
recommend the candidate without executing the install. Verify installed, enabled and
loaded state separately.

## Design-specific evidence

- For inspiration and implementation resources, use [visual-resources.md](visual-resources.md).
  Assets, component libraries and workflow skills are different kinds of capability.
- [podo/design-agent-skills](https://github.com/podo/design-agent-skills),
  [awesomeskills.dev](https://awesomeskills.dev/) and
  [mastering-claude.com](https://mastering-claude.com/) are optional domain pointers.
  Verify the original source rather than treating an entry as an endorsement.
- Preserve the selected design lead. Add only focused layers with distinct ownership;
  avoid another broad aesthetic director or an extra final prose editor.
- Compare the candidate against the actual surface, audience, reference fidelity,
  accessibility and motion requirements. Evaluate it on a representative UI task.
- Bookmarks and outside advice may suggest a narrow improvement to an existing skill.
  Check original dates, follow-ups and current upstream evidence; distinguish adopted
  methods, optional experiments and unreviewed leads.

Normally compare at most three candidates: missing capability, exact source, fit,
checked evidence, cost, overlap and recommended action. The companion installer
produces a plan for selected catalog entries; it does not search the web. Use current
upstream install syntax, and preserve existing authorization rather than asking again
solely because the script is plan-first.
