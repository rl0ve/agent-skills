## 1.9.0

Three checks earned by a keynote talk track whose author could hear the problem
but could not name it: "you're still have a backwards facing kind of syntax...
it's hard to describe" and "I hate the flat declaratives."

- **Backwards-facing clause** (catalog + spoken register + lint). A clause finished
  by an earlier one instead of standing on its own: "built for exactly that," "runs
  the way the map said it could," "where nothing made them wait." Pointer words carry
  the structure, so the listener has to hold the previous clause to parse this one.
  Costly in prose, unaffordable in speech, where nobody can look back.
- **Flat-declarative run** (lint: `flat-declarative-run`). The monotony check the old
  `sentence-shape-run` missed. Three or more consecutive sentences of near-identical
  length that none of them turns, where each sentence is individually good and the run
  reads as a list being recited. A sentence carrying a turn - a contrast, a colon, a
  subordinate move - breaks the run, because that is the prescribed fix.
- **Stacked precision** (lint: `stacked-precision`). Three or more consecutive
  sentences each landing an exact figure. Rounding aloud is the repair, so audibly
  rounded figures ("call it forty", "close to a hundred") do not count against it. One
  hard rule added to the spoken register: never say an approximation that contradicts
  an exact number the audience can read on the screen behind you.

Nine new unit tests, 56 in total.

# Changelog

## 1.8.0 - 2026-08-28

- `scripts/lint_natural_writing.py --set <file>`: measure a set of blank-line
  separated pieces **against each other**, not each piece against the rules.
  Flags any opening word, closing pair, or connective shared by more than a
  fifth of the set. The catalog's *Editing a set* already demanded this
  measurement and shipped no way to do it, which is exactly how a careful
  headline pass left 16 of 40 titles and 34 of 125 key points opening on the
  same article - the substitution failure the catalog names, invisible from
  inside any single piece.
- **Land callbacks forwards** (voice-and-register.md, spoken register): the
  register already banned act numbers and stage directions, but not the
  rhetorical callback - "Remember...", "Keep that in mind", "what the last act
  comes back to" - which looks harmless one at a time and reads as a tic in
  aggregate. Named as a set-level check.
- *Editing a set* and SKILL.md now point at `--set`, so the instruction and the
  tool that satisfies it are in the same place.
- Four unit tests for the new mode (47 total). A length-spread heuristic was
  written and then cut: it false-positived on a set that had just been varied
  on purpose, and the threshold was invented rather than derived.

## 1.7.0 - 2026-08-28

- Add a **Scripts meant to be spoken** register (voice-and-register.md): gloss
  screen labels rather than reading them cold, speak in the room rather than
  about the talk, keep the screen's own word for each thing, treat bold anchors
  as navigation the speaker needs (the one register where added bold is earned),
  and break lines at beat changes. Distilled from a day of live talk-track
  editing with the author reading every pass.
- Four catalog rows with linter checks where a regex is honest: **circular
  assertion** ("the rules ... are these rules"), **furniture inventory** ("three
  cards:"), **label read cold** (catalog-only; register-dependent), **speaker
  meta** ("easy to mix up", "hold that pattern", spoken act references).
- Extend **synonym cycling**: when a screen or document is in view, use its
  word - "reasons" on screen means not switching to "causes" in the walk.

## 1.6.0 - 2026-08-28

- Widen **interface as narrator** to derived artifacts and agency verbs: "the
  recommendation splits the claim" is the same disease as "the app keeps score" -
  an artifact doing an actor's verb. The catalog now says the noun list is
  open-ended on purpose; the linter adds recommendation/finding/proposal/
  rationale/brief and splits/decides. Caught in the wild by the reader after the
  original rule's noun list let it through - a class-boundary miss, not a revert.
- Add **trailer cadence**: compressed ad-copy rhythm in place of a spoken
  sentence ("One glance and Sarah has the case"). Let a person do it at normal
  speed.

## 1.5.0 - 2026-08-28

- Add **interface as narrator**: a screen, app, map, record or row performing a
  human verb, usually with a vague pronoun carrying the sentence - "the app
  keeps score on itself", "the map admits what it does not know", "each one says
  who owns it". Say what is on screen, or name the person reading it. The
  sibling of org-chart actor, and caught the same way: in the wild, three times
  in one sitting, by the person being read to. `show`, `list` and `mark` are
  deliberately not flagged - those are what screens do; the tell is attitude.
- Add **announced virtue**: prose that rates its subject instead of showing it -
  "and it is honest", "the useful thing about it is", "that matters more than it
  sounds", "because a picture is not a receipt". Cut the rating and let the
  evidence carry the judgment. If the evidence is missing, the rating was the
  only claim being made.

## 1.4.0 - 2026-08-28

- Add **em dash default**: use a typed dash (a hyphen, or a hyphen with a
  space on each side) as the reflexive connector instead of an em dash; keep
  the em dash for the rare case it is clearly the better mark. New linter
  check `scan_em_dash` fires on density across a piece, never on a single
  instance, matching the existing false-positive guardrail.
- Add **clause-shape monotony**: break up a run of four or more consecutive
  sentences in one paragraph that share the same shape, compound/hedged or
  short and simple. New linter check `scan_sentence_shape` finds the run and
  reports its length. Both checks run outside `scan()`, at the whole-piece or
  whole-paragraph level rather than per line, since the failure is a pattern
  across sentences, not a single line.

## 1.3.0

- Add **org-chart actor**: a department performing a human verb ("product
  quality gets the failure record"). The reader pictures nobody; name the
  people. A function can own or approve; it cannot hear, learn, or remember.
- Add **insider jargon**: systems vocabulary in reader-facing prose --
  "read-only evidence," "system of record," "human-in-the-loop." Say what
  happens in the reader's world instead. Both caught in the wild on the same
  paragraph, which is how they earned their rules.

## 1.2.0

- Add the **spec-sheet coda**: a finished sentence followed by a verbless list of
  qualities ("Plain language, no jargon, ready to use as it stands."). It reads as
  product-blurb summary rather than a claim, and it survived the earlier passes
  because each fragment is short and none of the existing rules look at what
  follows a sentence-ending period. Catalogue row, linter rule, three tests.

## 1.1.0 - 2026-08-25

- Added four pattern-catalog entries: deferred point, contrastive definition, mechanism-speak, and unglossed shorthand.
- Added an "Editing a set" section. Editing many pieces to one standard installs that standard as the next pattern, and each fix tends to substitute for what it removed. Measure the fix, not only the fault, and count words rather than sentences when length matters.
- Added three frequency rules to the linter for the same patterns, documented as corpus-level findings rather than per-line faults.
- SKILL.md now points at "Editing a set" whenever the job covers a set rather than a single piece.


## 1.0.1 - 2026-08-19

- Broadened auto-invocation from example phrases to semantic writing intent.
- Added paraphrased and implicit trigger cases plus non-writing boundary cases.

## 1.0.0 - 2026-08-19

- Added Claude Code-native Natural Writing skill and icon.
- Added explicit auto-invocation triggers for editing, drafting, voice matching, anti-slop work, interface copy, and Claude-specific writing residue.
- Added source synthesis, pattern catalog, voice guidance, model routing, examples, deterministic lint checks, and 22 forward-test cases.
