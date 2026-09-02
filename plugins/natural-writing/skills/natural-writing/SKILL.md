---
name: natural-writing
description: Diagnoses, edits, rewrites, voice-matches, or drafts reader-ready prose while preserving facts, intent, register, formatting, product terminology, and distinctive author voice. Use for any request whose intended outcome is clearer, more natural, less generic, less assistant-like, more audience-appropriate, or more recognizably the author's writing—even when the user never says “humanize” or “AI slop.” This includes implicit intent expressed through a draft plus requests to tighten, polish, simplify, make ready to send, sound more candid or direct, match a sample, explain why prose feels synthetic, or improve emails, reports, essays, posts, product and interface copy, documentation, marketing copy, and executive writing. Also use when prose contains dialogue residue, ritual validation, prompt echoes, coaching theater, taxonomy reflexes, fake contrasts, excessive headings, or generic endings.
compatibility: Claude Code with Agent Skills and plugin support.
---

# Natural Writing

Improve writing, not detector scores. Treat “AI slop” as a set of observable editing problems, never as proof of authorship.

## Non-negotiables

1. Preserve every supported fact, name, number, date, quote, citation, requirement, and material qualification.
2. Never invent specificity. Ask for a missing fact when it is essential; otherwise use a plain, bounded statement.
3. Preserve the writer's stance, register, and recognizable habits. Do not turn every author into the same polished professional.
4. Protect code, commands, URLs, file paths, identifiers, tables, frontmatter, legal text, and quoted material unless the user asks to edit them.
5. Make the minimum effective edit. Leave strong human sentences alone.
6. Do not promise that prose will evade an AI detector. Diagnose named patterns the reader can verify.

## Route the request

Choose one mode from the user's intent:

- **Diagnose:** The user asks to audit, flag, scan, or explain why text feels artificial. Identify patterns and suggest fixes without rewriting unless asked.
- **Edit:** The user supplies a draft and wants it clearer, more natural, or less generic. This is the default for supplied prose.
- **Draft:** The user supplies a brief, notes, or source material and wants new prose. Build from the evidence and requested voice without fabricating details.
- **Voice match:** The user supplies representative writing samples. Calibrate from those samples, then diagnose, edit, or draft. A reliable sample outranks generic style preferences.

If the mode is unclear, infer it from the requested deliverable. Ask one focused question only when audience, channel, or desired effect would materially change the result.

Route by semantic intent, not by literal trigger words. The examples in this skill are illustrative, not an allowlist. A supplied draft plus an implicit request for reader-ready prose is enough; the user does not need to name AI, Claude, slop, humanizing, voice, or editing.

## Calibrate before writing

Read the full input. Internally note:

- the reader and what they should know, feel, or do;
- the core point and the evidence that supports it;
- three to five voice signals: vocabulary, sentence rhythm, directness, humor, uncertainty, formality, digressions, punctuation, and paragraph length;
- protected content and the author's deliberate rough edges.

When the piece is a script meant to be spoken (a talk track, demo script, or narration), read the **Scripts meant to be spoken** register in [references/voice-and-register.md](references/voice-and-register.md) first: gloss screen labels, never talk about the talk, keep the screen's own word for each thing, treat bold anchors as navigation the speaker needs rather than decoration, make every clause stand up without the one before it, round numbers aloud rather than stacking exact ones, and let the line breathe - spoken prose keeps the connective tissue written prose edits out, so a mechanism gets walked through in full rather than compressed into a noun-phrase list.

### Ask before a substantial pass

A handful of answers change every line, and guessing them costs a whole cycle. Ask them together, in one message, each with the default you would otherwise assume, so the author can wave it through. Never more than four, and never one you can infer from the piece itself.

For a spoken piece: who is saying this and to whom; what is on screen behind them while they say it; which figures the audience can read for themselves; how long the beat is; and whether any line is dictated, protected, or already agreed with someone else. For a written piece: the reader, the decision they have to make, the register, and the length.

One question earns its place above the others because its answer is invisible in the draft: **how precise should the numbers be out loud.** A paragraph that quantifies is written one way for a reader and another way for a listener.

When a writing sample is provided, match its tendencies rather than isolated quirks. Do not copy memorable phrases from unrelated samples. For detailed calibration, read [references/voice-and-register.md](references/voice-and-register.md).

## Edit in layers

Work from meaning to surface. Do not patch watched words one at a time.

1. **Purpose:** Remove material that does not help the piece do its job.
2. **Structure:** Put the useful point where the reader needs it. Keep setup, detours, and suspense when they add context, tension, or character.
3. **Paragraphs:** Give each paragraph a real function. Merge tiny sections and split dense ones only when readability improves.
4. **Sentences:** Clarify actors and actions, untangle syntax, and vary cadence without manufacturing random “burstiness.”
   - Default to a typed dash - a hyphen, or a hyphen with spaces around it - over an em dash. Use an em dash rarely, only where it earns its place; never as the reflexive connector for an aside. See [references/pattern-catalog.md](references/pattern-catalog.md)'s **Em dash default**.
   - Read each paragraph's sentences in sequence and name each one's shape: compound/hedged (subordinate clauses, qualifiers like "although," "which," "may," "arguably") or simple/direct. Break up a run of four or more sentences in the same shape; a paragraph should alternate stretches of hedge and directness, not commit to one for its whole length. See [references/pattern-catalog.md](references/pattern-catalog.md)'s **Clause-shape monotony**.
   - Do not let a screen, app, map or record perform a human verb, and do not let a vague "it" or "each one" carry the sentence. Say what is on screen, or name the person reading it. See the catalog's **Interface as narrator**.
   - Do not rate the subject in place of showing it ("and it is honest", "the useful thing about it is"). Cut the rating; the evidence carries the judgment. See the catalog's **Announced virtue**.
5. **Words:** Prefer concrete nouns, direct verbs, and ordinary language. Retain technical terms that are precise for the audience.
6. **Voice:** Restore edge, uncertainty, humor, asymmetry, or understatement that an overly tidy edit removed.
7. **Integrity:** Compare the result with the source claim by claim.
8. **Say it out loud** (spoken pieces only): deliver every sentence at presentation speed. Any sentence you have to slow down for, re-run, or take a breath inside is compressed, and the fix is to walk the mechanism through rather than list its parts. No linter finds this one; see the catalog's **Telegraphic speech**.

Use [references/pattern-catalog.md](references/pattern-catalog.md) when the draft has repeated stock phrasing, generic structure, promotional tone, or suspiciously uniform cadence. Patterns are evidence only in clusters. Do not ban a word or punctuation mark merely because it appears once.

When the job covers a set rather than one piece, read the catalog's **Editing a set** before starting and measure again after. A standard applied across many items becomes the next pattern, and each fix tends to install a substitute for what it removed.

## Offer options when the call is taste

Correctness has one answer. Cadence, how much to compress, how many numbers to say aloud, how formal to be, which of two true framings to lead with: these have several, and the author owns the choice. Return options rather than your favourite.

- Three to five, and they must differ in **approach**, not phrasing. A different opening move, a different spine, a different shape. Five rewordings of one sentence is not a choice, and the author will feel handled.
- Name what each one trades away. An option presented without a cost has not been thought about.
- Recommend one and say why, so the author can accept without reading all five.
- Every option states the same facts. Options are about how it sounds, never about what is true.
- When the author picks one "stylistically", they have chosen the **approach and not the words**. Fix the flaw they named in the option they chose. Handing the same text back with the flaw still in it reads as not listening.
- Offer options before a large pass, not after. Rewriting forty pieces to a taste that turns out to be wrong is the expensive version of this mistake.

## Diagnose mode

Return a compact report. For each real issue:

1. name the pattern;
2. quote the smallest useful excerpt;
3. explain its effect on this reader;
4. give a short repair direction.

Separate high-confidence problems from optional style choices. Do not score the chance that AI wrote the text. Do not flag quotations, titles, proper names, code, or necessary legal/technical wording.

## Edit mode

Rewrite the whole passage coherently, then run [eval.md](eval.md). If a local phrase still feels artificial, revise the sentence or paragraph around its actual point instead of swapping synonyms.

Return:

1. the complete edited text;
2. a short **What changed** note covering only material edits;
3. any unresolved factual or audience question that prevented a safe fix.

For file edits, change only the requested prose and preserve the file's syntax and non-prose content. Summarize the result instead of pasting the whole file unless the user asks.

## Draft mode

Build a claim-and-evidence spine before drafting. Use only facts from the user's brief, provided sources, or verified research. Choose an opening suited to the channel; do not default to a throat-clearing hook. Let concrete evidence carry emphasis.

After drafting, apply the same layered edit and evaluation. If the brief lacks a critical fact, mark a concise placeholder or ask rather than inventing it.

## Output discipline

- Follow the requested format and length.
- Keep headings and lists only when they help navigation or comparison.
- Do not append a generic summary, uplift, call to action, or offer to continue.
- Do not narrate the editing process unless the user asks.
- Round-tripping prose through another agent or a plain-text scratch file converts inline markup to whatever carrier you chose (`<b>` to `**`, `<i>` to `_`). Convert every one of them back, and verify by counting each token type in the source and the result. A count that matches on bold and silently drops italics ships a literal underscore into the artifact.
- When another task embeds this skill, return only the finished artifact unless a change note is useful to that workflow.

When the Claude UI Router supplies product semantics, UX labels, states, marketing claims, or brand constraints, treat them as protected inputs. Natural Writing is the final prose editor; it must not redesign the interface or invent product behavior.

## Supporting resources

- Read [references/model-routing.md](references/model-routing.md) when the user asks which Codex or Claude model/agent should write or review the piece, or when consequential writing may justify an independent editorial audit.
- Read [references/pattern-catalog.md](references/pattern-catalog.md) for anti-patterns, exceptions, and rewrite heuristics.
- Read [references/claude-patterns.md](references/claude-patterns.md) when the user names Claude, complains about assistant-like dialogue residue, or asks for fiction/creative prose cleanup.
- Read [references/voice-and-register.md](references/voice-and-register.md) for voice matching and channel-specific decisions.
- Read [references/examples.md](references/examples.md) when a before/after model would help.
- Read [references/sources.md](references/sources.md) when maintaining or extending the skill's guidance.
- Run `scripts/lint_natural_writing.py` for a deterministic first-pass scan of longer English drafts. Treat its matches as review prompts, not verdicts.
- The per-document scan also reports `flat-declarative-run` (three or more consecutive sentences of the same length that none of them turns) and `stacked-precision` (three or more consecutive sentences each landing an exact figure). Both are review prompts: a deliberate staccato beat and a paragraph whose whole job is quantification can be right as they are.
- Add `--spoken` for a talk track, narration or demo script. It adds three narrow checks that only make sense out loud: `compressed-mechanism` (a mechanism flattened into "a clock, a warning when…, and an escalation when…"), `stacked-object-pronouns` ("hand it that"), and `paragraph-opens-on-pronoun`. All three were measured against a 40-piece corpus before shipping and fired only on true positives. They cover the narrow shapes, not the judgment: the wider compression call stays with your ear and step 8.
- Add `--set` when the job is many pieces rather than one: it measures the set against itself and flags an opening word, closing pair, or connective shared by more than a fifth of it. This is the check that catches what your own edit installed.
- Some patterns are judgment only and are marked that way in the catalog. When a check cannot be made reliable, say so with the evidence and hand over the manual test instead. A noisy check is worse than no check: it trains the next reader to skip the output. Measure any new check against a real corpus and report its false-positive rate before shipping it.
- Use [tests/cases.md](tests/cases.md) to forward-test behavior after changing this skill.
