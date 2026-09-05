# Skill discovery and verification

For visual inspiration and free implementation resources rather than new agent skills, use [visual-resources.md](visual-resources.md). It includes source attribution, free/paid boundaries, and task-specific selection; directories and templates are not automatically plugins.

Use this only when the user asks for newer skills or the required capability is not installed.

When reviewing bookmarks or outside advice, separate reusable methods from products,
model rankings and promotional claims. Check the original date, follow-up and current
upstream evidence. A useful principle may already belong to an installed skill; update
that owner narrowly rather than installing another broad design lead. Preserve the
difference between adopted guidance, an optional experiment and an unreviewed lead.

## Recommended stack

These sources are a stack, not a single winner. Start from the question being answered:

1. **Discover a category:** [Skillselion](https://skillselion.com/) is the broadest first pass for comparing skill families, GitHub metadata, and historical movement across a category.
2. **Scan current momentum:** [Skill Leaderboard](https://skillleaderboard.com/) is useful for a quick weekly scan of fast-rising repositories. Star velocity is a lead, never a quality verdict.
3. **Vet the design domain:** use curated references such as [podo/design-agent-skills](https://github.com/podo/design-agent-skills), [awesomeskills.dev](https://awesomeskills.dev/), and [mastering-claude.com](https://mastering-claude.com/) to understand categories and find upstream candidates. Treat catalogue entries as pointers, not automatic endorsements.
4. **Look up or install a known skill:** [skills.sh](https://skills.sh/) and [claudeskills.info](https://claudeskills.info/) are useful once the target family or repository is already known. Use the current upstream install syntax, not a command copied from a stale directory page.
5. **Verify upstream:** open the exact GitHub repository and inspect the complete `SKILL.md`, scripts, recent activity, issues, license, scope, and install path before recommending or executing an install.

The companion installer in this package turns the verified catalog into a transparent plan and can execute only the skills the user explicitly selects. It never treats discovery rank as install approval.

## Pre-install checklist

- Confirm the repository owner and exact skill path.
- Read the complete `SKILL.md` and any scripts it may execute.
- Check recent activity, unresolved issues, release/update story, and license.
- Look for overly broad triggers or overlaps with installed skills.
- Prefer project-local installation for evaluation.
- Record the source and date for any skill that becomes workflow-critical.
- Re-audit after updates; popularity does not protect against supply-chain changes.

## Recommendation format

```text
Capability: <what is missing>
Candidate: <owner/repo and skill>
Why it fits: <one sentence>
Evidence checked: <source, activity, license, instructions/scripts>
Overlap risk: <installed skills it may collide with>
Install: <command, only after verification>
```

Never invent an install command from a directory listing. Use the upstream repository's current instructions.
