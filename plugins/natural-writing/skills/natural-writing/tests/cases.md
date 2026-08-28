# Forward-test cases

Run these as fresh tasks with only the skill and the prompt. Judge the output against `../eval.md`.

## 1. Minimal edit

Prompt: “Humanize this: I think the rollout is mostly good, but honestly the missing undo button still bothers me.”

Pass if the result keeps the first-person uncertainty and concern. It may cut “honestly” only if the voice does not need it.

## 2. No fabrication

Prompt: “Improve this: Our integration significantly reduced processing time.”

Pass if the result does not invent a number, benchmark, customer, or mechanism. It may flag the missing evidence.

## 3. Diagnose only

Prompt: “Audit this without rewriting: This pivotal launch marks a transformative moment, showcasing our unwavering commitment to innovation.”

Pass if the response names observable patterns, quotes short excerpts, suggests repairs, and does not estimate whether AI wrote it.

## 4. Protected literals

Prompt: “Edit the prose but preserve code: Run `deploy --target=prod`, then open https://example.com/a-b.”

Pass if the command and URL are byte-for-byte unchanged.

## 5. Voice sample outranks defaults

Prompt: “Sample: I like em dashes—probably too much—but that's how I think. Rewrite in my voice: The plan has two risks and both deserve attention.”

Pass if the rewrite may use an em dash and does not apply a blanket punctuation ban.

## 6. Executive register

Prompt: “Turn these notes into a two-sentence executive update: launch delayed to Oct 12; security review owns the delay; no customer data exposed.”

Pass if the update leads with delay or risk, preserves the date and ownership, and adds no forecast.

## 7. Technical register

Prompt: “Edit: The configuration is parsed by the loader. Invalid keys are rejected by the validator.”

Pass if actors and actions become clear without changing the technical meaning.

## 8. Intentional fragment

Prompt: “Light edit, keep the tension: Ten minutes left. No backup. The client was watching.”

Pass if the fragments remain mostly intact.

## 9. Real qualification

Prompt: “Polish: The treatment may reduce symptoms in some adults, based on one small trial.”

Pass if uncertainty and evidence limits remain.

## 10. File mode

Prompt: “Edit prose in a Markdown file that contains YAML, a table, and fenced code.”

Pass if only prose changes and the response summarizes rather than dumping the file.

## 11. Draft from sparse evidence

Prompt: “Draft a product announcement from: beta opens Friday; limited to 100 teams; export supports CSV only.”

Pass if every claim comes from the notes and the copy does not imply general availability or other formats.

## 12. Generic ending

Prompt: “Edit: The migration finishes Tuesday. This exciting milestone sets the stage for a brighter future.”

Pass if the result ends on the Tuesday fact rather than replacing the flourish with another flourish.

## 13. Claude validation preamble

Prompt: “Edit this into a standalone recommendation: You're absolutely right to focus on onboarding. That's exactly the key distinction. I would recommend a two-week pilot.”

Pass if the result begins with the two-week-pilot recommendation and does not preserve ritual praise.

## 14. Collaboration theater

Prompt: “Edit: Three things you improved, and one thing I want to push on gently that may be hard to see from inside: the pricing argument still lacks evidence.”

Pass if the result states that the pricing argument lacks evidence without narrating the coaching posture.

## 15. Real objection survives

Prompt: “Edit: The CFO objected that the pilot would delay the renewal. The pilot team disagreed because it ends six weeks before renewal.”

Pass if the named objection, source, and timing remain.

## 16. Taxonomy reflex

Prompt: “Simplify: There are three lenses here: the strategic lens, the operational lens, and the human lens. Strategically, we lack a buyer. Operationally, we lack an owner. From the human lens, the team is tired.”

Pass if the result keeps the three distinct facts but removes decorative lens labels unless the requested format needs comparison.

## 17. Fiction pace

Prompt: “Lightly edit this scene without making it uniformly plain: Every shadow whispered. The hallway held its breath. The clock carved grief into the bruised silence. Mara crossed the room and opened the drawer.”

Pass if the edit keeps at most one earned image, retains the action, and adds no new story fact.

## 18. Unexplained subtext

Prompt: “Edit: He put two cups on the table, remembered she was gone, and felt an overwhelming wave of grief that showed how deeply he missed her.”

Pass if the concrete action carries the emotion without changing the event.

## 19. Default writing route

Prompt: “Which Codex or Claude agent should write a normal executive email?”

Pass if the answer recommends the context-holding parent at medium effort—Sol for Codex or Sonnet for Claude—rather than automatically spawning an agent or choosing the largest model.

## 20. Voice-sensitive escalation

Prompt: “This speech has to sound unmistakably like me and the stakes are high. Which model should I use?”

Pass if the answer prioritizes a representative writing sample, then recommends a higher-judgment parent model such as Sol at high effort or Opus at medium/high effort. It must not promise that the model alone will preserve voice.

## 21. Research is not final voice

Prompt: “Use an explorer to research this report and have it write the finished version.”

Pass if the workflow lets the explorer gather and organize evidence but assigns the final prose to the context-holding parent.

## 22. Independent editorial audit

Prompt: “Use another agent to polish my final draft.”

Pass if an important draft may receive a read-only audit that returns prioritized findings, while the parent retains authorship and applies any accepted changes. It should not launch competing write-capable rewrites.
