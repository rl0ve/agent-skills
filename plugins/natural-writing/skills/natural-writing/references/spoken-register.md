# Scripts meant to be spoken

Talk tracks, demo scripts, presenter notes, video narration. Everything spoken lives here: the register rules, the patterns that only exist out loud, and the checks that go with them. Read this file before touching any of those and skip it for written prose, because most of what follows is wrong for a reader.

The test for every sentence: can a person say this on a stage at normal speed, and does the room follow it cold?

## Register rules

- Gloss what the screen says; never read a label or column value as if it were a sentence. "No rule resolves a combined cause" is a cell, not speech - say what it means and who acts on it.
- Speak in the room, not about the talk. No section or act numbers aloud, no narrating the audience ("they are easy to mix up"), no stage directions in the words ("hold that pattern").
- Land callbacks forwards. "The ledger was empty when we published the map. It is not empty now" does the same work as "Remember the empty ledger?" without asking the room to go back and fetch it, and it survives a listener who missed the first mention. Each backwards reference looks harmless alone, so this is a set-level check: count "Remember…", "Keep that in mind", "hold that", "as you saw earlier", and anything pointing at the deck's own structure ("what the last act comes back to") across the whole script. More than one or two and it reads as a speaker who does not trust the material. A callback to a number the audience genuinely needs is fine; state it, do not request it.
- Speech carries connective tissue that writing edits out, and it should. A talk track is not a compressed sentence read aloud: it opens with a filler that buys the room a beat ("Now," "So," "And here is the thing"), it names the subject again rather than pronouning it, and it walks a mechanism through in full instead of listing its parts. "Each main stage carries a clock, a warning when it is at risk and an escalation when it breaches" is a spec line. "Now, each main stage has an SLA, and when that SLA is at risk of being breached, Maestro Case will escalate it to the right person automatically" is the same fact said by a person. The second is longer on purpose. Tighten written prose; let spoken prose breathe.
- Say the product's own word rather than a friendly paraphrase. If the thing is an SLA, say SLA. Glossing exists for column headings and jargon the room cannot parse, not for terms the audience came to hear.
- Every clause has to stand up on its own. A listener cannot look back, so a clause finished by an earlier one ("built for exactly that," "runs the way the map said it could") costs them the sentence they are currently in. Name the subject again rather than pointing at it, and define a thing by what it does rather than by what is absent. The general rule is the catalog's **Backwards-facing clause**; it applies everywhere and is unaffordable here.
- Vary sentence length inside the paragraph, and make the variety carry something. Three sentences of the same shape in a row read as a list being recited, and this is as true of short flat declaratives as of long hedged ones. Give one sentence a turn - a contrast, a repeat that lands, an ordinary phrase like "messy work" - and let its neighbours run longer or shorter. Vary them; do not shorten them all. Cutting every sentence to its shortest form produces the flattest run of the lot, and in a spoken piece the longer flowing sentence is usually the one carrying the listener.
- Round numbers out loud. Three or more exact figures in consecutive sentences cannot be heard, so keep the one the point rests on and approximate the rest audibly on purpose ("call it forty"). One hard constraint: never say an approximation that contradicts an exact number the audience can read on the screen behind you.
- Keep one name per thing, and keep it the name the screen shows. If the column says "reason," do not switch to "cause" mid-walk unless the screen does.
- Emphasis is navigation, not decoration: on a script of any length, bold the number the speaker must hit and one load-bearing phrase per beat - two to five words, at least one per paragraph. This is the one register where added bold is earned; do not strip it as decorative.
- Start a new line where the beat changes, so the speaker can find their place at a glance.

## Ask before the pass

Who is saying this and to whom; what is on screen behind them while they say it; which figures the audience can read for themselves; how long the beat is; and whether any line is dictated, protected, or already agreed with someone else. Ask them together, each with the default you would otherwise assume. The one that earns its place above the others, because its answer is invisible in the draft, is how precise the numbers should be out loud.

## Patterns that only exist out loud

These sit here rather than in the general catalog because each one is correct, or harmless, in written prose. A caption can quote a label verbatim; a spec sheet can list a mechanism's parts; a table can stack exact figures. Say the same words on a stage and they fail.

| Pattern | Signal | Better move |
|---|---|---|
| Label read cold | The script recites a screen label or column value as if it were a sentence: "No rule resolves a combined cause. Recurrence confirmed, gates closure." | Gloss it for the room: what it means, and who acts on it. If the source does not say what it means, ask; a gloss built from the label's own words ("the case does not close until recurrence is confirmed") is the label read twice. |
| Speaker meta | The script talks about the talk: "they are easy to mix up," "hold that pattern," "as we saw in Act I," "this is the one this whole story is about." | Say the thing itself. Distinctions are stated, not announced as confusing; callbacks name the content ("the empty ledger from the artifact"), not the section. **Linted:** `speaker-meta`. |
| Trailer cadence | Compressed ad-copy rhythm standing in for a spoken sentence: "One glance and Sarah has the case," "One click and it ships," "Instant clarity." | Let a person do it at normal speed: "Sarah opens it, and the whole case is in front of her." The tell is a beat pattern - stakes compressed into a fragment - where a walkthrough needs a subject and a verb. **Linted:** `trailer-cadence`. |
| Telegraphic speech | A spoken line compresses a mechanism into a noun-phrase list: "a clock, a warning when it is at risk and an escalation when it breaches." It reads fine and cannot be said convincingly, because a listener needs the connective tissue a reader can skip. | Walk it through as a person would: an opener that buys a beat ("Now,"), the subject named rather than pronouned, and the mechanism in full - "when that SLA is at risk of being breached, it escalates to the right person automatically." Longer on purpose. **Partly linted, deliberately not fully:** `--spoken` catches three narrow shapes that measured clean on a 40-piece corpus (a noun-plus-temporal-clause series, stacked object pronouns, a paragraph opening on a pronoun). The general call stays judgment. A first prototype keyed on any verbless comma inventory was rejected because that is also the shape of a legitimate pointing beat. A second, keyed on a noun-phrase series of three or more with a subordinate clause, produced 19 candidates across 40 talk tracks, nearly all deliberate rhetoric ("every one taken by a person, every one carrying its rationale"), and missed the canonical case, which carries only one comma. No regex can know that "a stage that is meant to take four" is an SLA. Read the piece aloud. |
| Stacked precision | Three or more exact figures land in consecutive sentences: "thirteen stages, thirty-nine tasks, eighty-nine rules, ninety variables." Each is true and the run is unhearable. | Keep the one number the point rests on and round the rest out loud - "call it forty" - so the rounding is audibly deliberate. Never let a spoken approximation contradict an exact figure the audience can see on screen. **Linted:** `stacked-precision`. **Known false positive:** a chain of figures that derive from one another and are all on the frame behind the speaker (a cost split walked against an authority limit, a queue count walked down to a percentage). Each follows from the last and rounding any of them would contradict the screen. The check cannot tell a derived chain from an unrelated stack, so read the excerpt before editing. |

Four general-catalog patterns bite hardest here and are worth re-reading before a spoken pass: **Backwards-facing clause**, **Clause-shape monotony**, **Interface as narrator**, and **Furniture inventory**.

Worked examples for the rows above, headed by row name:

### Telegraphic speech, Stacked precision, Label read cold

Before (a talk track; the screen behind the speaker labels the clock "SLA", and the speaker's note says "recurrence confirmed" means an engineer has ruled the fault will recur, and the case cannot close until then):

> Each main stage carries a clock, a warning when it is at risk and an escalation when it breaches. Thirteen stages, thirty-nine tasks, eighty-nine rules. Recurrence confirmed, gates closure.

After:

> Now, each main stage has an SLA, and when that SLA is at risk of being breached, it escalates automatically. There are thirteen stages in this case and, call it, forty tasks and ninety rules behind them. And this line here, **recurrence confirmed**, means an engineer has ruled that the fault will come back, and the case cannot close until they have.

Why: three spoken-only patterns in three sentences. **Telegraphic speech**: the first sentence is a spec line nobody can say at speed; the after is longer on purpose and uses the screen's own word, SLA, which the note supplies. **Stacked precision**: three exact figures in a row cannot be heard; the point rests on thirteen, so that stays exact and the other two are rounded audibly rather than dropped. **Label read cold**: "recurrence confirmed, gates closure" is a screen cell; the after says what the speaker's note says it means and who acts on it. Without that note the right move is to ask, not to gloss the label from its own words. Applied to written prose, every one of these edits would be wrong. See [spoken-register.md](spoken-register.md).

### Speaker meta

Before:

> As we saw in Act I, these two are easy to mix up. Hold that pattern, because this is the one this whole story is about.

After:

> The blue line is the estimate and the black line is what the customer was actually paid. On this case they were 9,000 apart.

Why: Section numbers, a narrated audience, a stage direction and a trailer line, and no content. The after says the distinction the before called confusing. The two lines and the gap are from the screen the speaker is standing in front of.

### Trailer cadence

Before:

> One glance and Sarah has the case. One click and it ships. Instant clarity.

After:

> Sarah opens the case, and the estimate, the photos and the adjuster's note are all on one screen. She approves it here, and it goes to payment.

Why: Ad-copy beats standing in for a spoken walkthrough. The after lets a person do it at normal speed with a subject and a verb. The three things on screen are from the demo, not invented.

## Say it out loud

The last step of a spoken edit, and the one no linter replaces: deliver every sentence at presentation speed. Any sentence you have to slow down for, re-run, or take a breath inside is compressed, and the fix is to walk the mechanism through rather than list its parts.

## Checks

```bash
python3 scripts/lint_natural_writing.py --spoken SCRIPT.md
```

`--spoken` adds `compressed-mechanism`, `stacked-object-pronouns` and `paragraph-opens-on-pronoun`. All three were measured against a 40-piece corpus before shipping and fired only on true positives. `stacked-precision` and `flat-declarative-run` run without the flag because a written piece can have the same defect, but they were built for this register and are read here first. Treat every match as a review prompt.
