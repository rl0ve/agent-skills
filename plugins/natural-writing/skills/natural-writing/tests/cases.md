# Forward-test cases

Run these as fresh tasks with only the skill and the prompt. Judge the output against `../eval.md`.

Where a case targets a catalog row, its heading is that row's exact name, matching the row and its worked example in `../references/pattern-catalog.md` (or `../references/spoken-register.md`). `test_catalog_structure.py` checks this.

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

## 12. Recap ending

Prompt: “Edit: The migration finishes Tuesday. This exciting milestone sets the stage for a brighter future.”

Pass if the result ends on the Tuesday fact rather than replacing the flourish with another flourish.

## 13. Validation preamble

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

## 17. Pace compression

Prompt: “Lightly edit this scene without making it uniformly plain: Every shadow whispered. The hallway held its breath. The clock carved grief into the bruised silence. Mara crossed the room and opened the drawer.”

Pass if the edit keeps at most one earned image, retains the action, and adds no new story fact.

## 18. Explained subtext

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

## 23. Telegraphic speech

Prompt: “This is a demo script I will read aloud. Edit it: Each main stage carries a clock, a warning when it is at risk and an escalation when it breaches.”

Pass if the result is longer than the input, names the mechanism as a person would say it (an SLA that escalates when at risk), and uses the product's word rather than a paraphrase. Fail if the sentence is tightened further.

## 24. Stacked precision

Prompt: “Talk track, keep it sayable: Thirteen stages. Thirty-nine tasks. Eighty-nine rules. Ninety variables. The screen behind me shows all four.”

Pass if the result keeps one exact figure and rounds the rest audibly, or keeps them all and says why the on-screen figures must not be contradicted. Fail if it approximates a number the audience can read.

## 25. Label read cold

Prompt: “Presenter notes, spoken: No rule resolves a combined cause. Recurrence confirmed, gates closure.”

Pass if each label is glossed as what it means and who acts on it. Fail if either label is delivered verbatim as a sentence.

## 26. Label read cold (written control)

Prompt: “Edit this caption under a screenshot: No rule resolves a combined cause.”

Pass if the caption keeps the label verbatim or near-verbatim. The spoken repairs from cases 23 to 25 must not be applied to written prose.

## 27. Editing a set

Prompt: “Here are 40 one-line captions. Vary the openings; they all start with a verb.” (Supply 40 captions.)

Pass if the response varies the openings and then reports what the pass installed across the set (opening word, closing shape, connective) or runs `--set` and reads its output. Fail if it fixes the verbs and stops.

## 28. Offer options when the call is taste

Prompt: “Rewrite the opening of all twelve sections of this deck to land harder.” (Supply the deck.)

Pass if the response offers three to five approaches that differ in kind, names what each trades away, recommends one, and waits for a choice before rewriting twelve sections. Fail if it rewrites all twelve to one taste first.

## 29. Ask before a substantial pass

Prompt: “Edit this keynote talk track.” (Supply a 900-word script with figures in it.)

Pass if the response asks, in one message, no more than four questions with defaults, and one of them is how precise the numbers should be out loud. Fail if it asks them one at a time or guesses silently.

## 30. Eval check 3: markup round-trip

Prompt: “Edit the prose in this HTML fragment and hand it back as HTML.” (Supply a fragment with `<b>`, `<i>`, `<code>`, and a link.)

Pass if the count of each inline token type in the result matches the source and no `**` or `_` carrier markup leaks into the output.

## 31. Nominated significance

Prompt: “Edit: Look at the owner column. That is the point. What matters is how many of these run every day.”

Pass if the result states the finding (what the owner column shows about daily work) rather than pointing at it. If the finding cannot be derived from the supplied text, the response asks for it.

## 32. Interface as narrator

Prompt: “Edit: The app keeps score on itself, and the map admits what it does not know.”

Pass if the result says what is on screen or names the person reading it, and keeps any verb a screen genuinely does (show, list, mark).

## 33. Exit check 27: a passing draft is returned unchanged

Prompt: “Polish: The migration finishes Tuesday. Support sees the new export screen Wednesday morning, and the old one goes away a week later.”

Pass if the response returns the text unchanged, or with at most a punctuation change it can justify, and says the draft already passes. Fail if it swaps a word to show work.

## 34. Candor announcement

Prompt: “Edit into a standalone note: Honestly? The honest answer is that the pilot is not ready. Here's where I'd push back: the vendor's number is six months old.”

Pass if the result states the two facts without any phrase announcing frankness, and does not soften them.

## 35. Vague connection

Prompt: “Edit: The foundation is associated with the university. (Source: the university founded it in 1998.)”

Pass if the result says the university founded the foundation in 1998. Then: “Edit: The foundation is associated with the university.” with no source. Pass if the result keeps the vagueness or asks what the relation is; fail if it invents one.

## 36. Nominated significance (interpretive metadiscourse)

Prompt: “Edit: As you can see, the queue drains by noon. This distinction matters. The key insight is that nobody owns the nightly run.”

Pass if the result keeps the two facts (queue drains by noon; nobody owns the nightly run) and drops the three phrases that tell the reader what to notice.

## 37. Intensifier padding

Prompt: “Edit: This is genuinely hard. The teams really do struggle with it, and it truly matters that we actually fix it this quarter.”

Pass if the result removes the cluster of intensifiers and either states the evidence the draft implies or flags that none was supplied. Fail if it strips every adverb from a draft that used one.

## 38. Universal quantifier

Prompt: “Edit: Everyone skips the onboarding video. (Source: a survey of six teams; five skipped it.)”

Pass if the result says five of six, most, or the teams surveyed. Fail if “everyone” survives with the source in hand.

## 39. Quotable closer

Prompt: “Edit these three paragraphs.” (Supply three short paragraphs, each ending on an aphorism.)

Pass if at most one paragraph still ends on a pull-quote line and the facts are intact. Fail if the result adds a fourth aphorism or turns the paragraphs into a list.
