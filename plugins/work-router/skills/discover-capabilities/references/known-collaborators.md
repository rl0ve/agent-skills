# Known collaborators

Checked October 20, 2026. These are maintained upstream skill families that cover
concerns this repository deliberately does not own. Listing a family here is not an
install recommendation and does not authorize an install. Inspect the exact upstream
skill before adopting it, and install by name, not by collection.

## Engineering discipline

Work Router decides **who** does coding work and at what model and effort. It does not
prescribe **how**: specification, test-first implementation, diagnosis, review or
hardening. When that method is the missing capability, compare one family below
before writing a new skill.

| Family | Signal (Oct 20) | Skills worth inspecting |
|---|---|---|
| [mattpocock/skills](https://github.com/mattpocock/skills) | About 299K stars; six of the top ten skills.sh skills ([Skillselion](https://skillselion.com/leaderboard)) | `grill-me` / `grill-with-docs` (interview a plan until it is decidable), `to-spec`, `tdd`, `diagnosing-bugs` |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | About 109K stars | `spec-driven-development`, `code-review-and-quality`, `security-and-hardening` |
| [obra/superpowers](https://github.com/obra/superpowers) | About 303K stars | Broad overlap with both families above |

Stars and leaderboard rank are leads, not evidence of task quality.

### Adoption rules

- **Pick one family per concern.** The three overlap heavily; installing all of them
  creates competing owners for planning, TDD and review.
- **Prefer a few named skills** (about four) over a full collection, with the user's
  approval for each install.
- **Handoff overlap.** Pocock's `handoff` and an installed `coding-agent-handoff`
  cover the same concern. Keep one; use [deduplicate-skills](../../deduplicate-skills/SKILL.md)
  when both are already installed.
- **Routing still applies.** A discipline skill changes method, not model choice. The
  route table in [route-ai-work](../../route-ai-work/SKILL.md) still picks the owner.
- **Verify on a representative task.** Report installed, enabled and loaded
  separately, then judge whether the method improved accepted output.
