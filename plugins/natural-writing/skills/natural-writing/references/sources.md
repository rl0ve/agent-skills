# Source basis

This skill synthesizes editing principles rather than reproducing any source's rule list or wording. Maintain the following distinctions when extending it.

## Primary influences

- [blader/humanizer](https://github.com/blader/humanizer): use observable pattern clusters, preserve facts, calibrate to a writer sample, protect genuine human texture, and run a second integrity pass. The repository is MIT-licensed.
- [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) and its [skills.sh entry](https://www.skills.sh/petergyang/no-ai-slop/no-ai-slop): make the minimum effective edit, separate diagnose from edit mode, use the portability test, protect voice, and evaluate the result against explicit checks. The repository is MIT-licensed.
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing): treat common patterns as editorial observations with false-positive risk, not as a reliable authorship detector.

## Field reports on AI prose, 2025-2026

Used to rank which patterns readers actually complain about, and to check that the catalog's emphasis matches. None of these is a detector and the skill does not cite them as one.

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), revisions to 2026-09-03: added **vague expression of connection or association** (2026-08-19), and a note that by mid-2026 only Claude still used em dashes above professional writers' rate.
- [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) PR #34 (2026-08-06): **interpretive metadiscourse**, lines that step outside the subject to tell the reader what to notice. Folded into **Nominated significance**.
- [anthropics/claude-code issue #3382](https://github.com/anthropics/claude-code/issues/3382) and [#77136](https://github.com/anthropics/claude-code/issues/77136), plus Hacker News threads through 2026: "You're absolutely right," "here's where I'd push back," "the honest caveat," and the lexical tells named in the catalog's **Assistant residue** table. Source of **Candor announcement**.
- [PCWorld, Claude ranked my sounds-like-AI habits](https://www.pcworld.com/article/3179916/claude-ranked-my-sounds-like-ai-writing-habits.html): 78 dashes and 67 parenthetical asides in 11,700 words, asides ranked the stronger tell. Source of the parenthesis half of **Dash and parenthesis dependency**.
- [aicheckr.io, AI slop examples](https://www.aicheckr.io/blog/ai-slop-examples) and [Matthew Vollmer, I asked the machine to tell on itself](https://matthewvollmer.substack.com/p/i-asked-the-machine-to-tell-on-itself): before/after pairs whose moves (fact-backed distinction for not-X-but-Y, one adjective plus proof for a triplet, a named audience for "whether you're a…") informed the 1.13.0 examples. The examples themselves are original.

- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) (newest change 2026-01-13): eight rules, twelve quick checks, a phrase list by category. Source of **Intensifier padding**, **Universal quantifier**, **Quotable closer**, and the widened signals on **Nominated significance** (emphasis crutches, the pseudo-cleft opener), **Question-answer pivot** (rhetorical setups), **Negative tail and runway**, and **Importance inflation** (vague declaratives). Three of its rules were read and not adopted: a ban on all adverbs (this skill treats intensifiers as evidence in clusters and protects voice), a direct-address stance for every register (a register decision, not a defect), and a five-dimension score with a revise threshold (this skill's eval is a checklist of failures, not a score, so a passing draft can be returned unchanged).

Source repos were last checked 2026-09-03. blader/humanizer (v2.11.2, 2026-08-19), dbohdan/unslop (2026-06-30), jpeggdev/humanize-writing (2026-03-14) and kimhons/humanize (2026-05-08) had added no pattern the catalog lacks.

## General writing guidance

- [Google Technical Writing: active voice](https://developers.google.com/tech-writing/one/active-voice): make actors and actions clear because active constructions are usually shorter and easier to process. Retain passive voice when the actor is unknown, irrelevant, or properly backgrounded.
- [Google Technical Writing: words](https://developers.google.com/tech-writing/one/words): prefer precise verbs and concrete terms, reduce needless complexity, and define unfamiliar language for the audience.
- [GOV.UK: use the right tone](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/tone-of-voice/right-tone/): aim for clear, concise, human, non-pompous prose suited to the reader.
- [GOV.UK: use clear language](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-language/): use plain language even for specialists, keep necessary domain terms, and express requirements with the correct level of force.
- [jpeggdev/humanize-writing](https://github.com/jpeggdev/humanize-writing): repair repeated section architecture before surface vocabulary and consolidate overlapping flags instead of inflating a diagnosis.
- [dbohdan/unslop](https://github.com/dbohdan/unslop): in fiction, modulate pace, earn literary devices, leave subtext unstated, and prefer story-specific detail over convergent “literary AI” aesthetics.
- [obra/the-elements-of-style](https://github.com/obra/the-elements-of-style): prefer concrete language, active construction where useful, coherent paragraphs, and omission of needless words. Use selectively; the full historical reference is much broader than this skill needs.
- [kimhons/humanize](https://github.com/kimhons/humanize): apply domain-specific carve-outs so academic methods, documentation, blogs, and commits are not edited as one register.

## Maintenance rules

1. Prefer principles supported across sources over a growing blacklist of fashionable words.
2. Add a pattern only when it identifies a repeatable editing failure and includes a false-positive guardrail.
   A new catalog row ships with a worked example under its table, headed by the row's exact name, and a forward test in `tests/cases.md`, the same way a new lint check ships with a measured false-positive rate and an entry in the linter's `ROW_FOR` map. `tests/test_catalog_structure.py` fails on a row without an example, a check without a row, or a case that names a row that does not exist.
3. Keep authorship detection outside the skill's claims. The goal is better prose.
6. One home per rule. A pattern lives in one catalog table (or in `spoken-register.md` if it only fails out loud); SKILL.md and the register files point at it rather than restating it. Duplicated guidance drifts.
4. Write original examples whose facts make the editorial decision testable.
5. Preserve the priority order: integrity, user intent, audience, author voice, then generic style rules.
