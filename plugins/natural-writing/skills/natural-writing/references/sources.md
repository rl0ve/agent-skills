# Source basis

This skill synthesizes editing principles rather than reproducing any source's rule list or wording. Maintain the following distinctions when extending it.

## Primary influences

- [blader/humanizer](https://github.com/blader/humanizer): use observable pattern clusters, preserve facts, calibrate to a writer sample, protect genuine human texture, and run a second integrity pass. The repository is MIT-licensed.
- [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) and its [skills.sh entry](https://www.skills.sh/petergyang/no-ai-slop/no-ai-slop): make the minimum effective edit, separate diagnose from edit mode, use the portability test, protect voice, and evaluate the result against explicit checks. The repository is MIT-licensed.
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing): treat common patterns as editorial observations with false-positive risk, not as a reliable authorship detector.

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
3. Keep authorship detection outside the skill's claims. The goal is better prose.
4. Write original examples whose facts make the editorial decision testable.
5. Preserve the priority order: integrity, user intent, audience, author voice, then generic style rules.
