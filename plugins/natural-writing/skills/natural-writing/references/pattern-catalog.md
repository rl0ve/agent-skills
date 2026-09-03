# Pattern catalog and repair heuristics

Use this catalog to diagnose repeated problems, not to fingerprint authorship. A single word, dash, short sentence, or polished paragraph proves nothing. Look for clusters, frequency, and effect.

## Content problems

| Pattern | Signal | Better move |
|---|---|---|
| Importance inflation | Ordinary facts “mark a pivotal moment” or “underscore significance”; or a bare declaration of weight with nothing under it: “the stakes are high,” “the implications are significant,” “the reasons are structural” | State the fact and its supported consequence. Let the reader judge its weight. |
| Sales varnish | “Vibrant,” “groundbreaking,” “renowned,” or “seamless” replaces evidence | Use the feature, result, constraint, or sensory detail already available. |
| Vague authority | “Experts say,” “studies show,” or “industry leaders agree” | Name the source and claim. If no source exists, cut or qualify the claim. |
| Superficial interpretation | A trailing `-ing` clause announces what a fact “highlights” or “showcases” | Explain a real mechanism or consequence, or end after the fact. |
| Portability filler | A sentence could describe almost any company, person, city, or product | Replace it with subject-specific evidence or remove it. |
| Generic forecast | A challenges/future section predicts continued growth without evidence | Keep only dated plans, known constraints, or concrete next steps. |
| Unsupported certainty | Smooth prose quietly strengthens a tentative source | Restore the original scope, probability, and attribution. |
| Universal quantifier | “Everyone does this,” “nobody reads the manual,” “always,” “never,” where the source supports “most,” “the teams we asked,” or a number | Use the quantity the evidence supports. A universal is a claim about every case; if that is not what is known, it is not what should be said. **Judgment only.** |
| Vague connection | A relation is named without saying what it is: “associated with,” “in connection with,” “linked to,” “involved in” where the source gives the actual role | Say the role: founded, funded, sued, worked for, was born in. If the source does not say, keep the vagueness and know that it is the source's. **Judgment only:** the same phrases are correct when the relation genuinely is loose. |

## Structural problems

| Pattern | Signal | Better move |
|---|---|---|
| Throat clearing | “Here is the thing,” “It is worth noting,” “In today's world” | Start with the useful statement unless the setup adds voice or context. |
| Manufactured insight | “What everyone misses” or “The deeper truth” precedes an ordinary claim | State the claim and earn its importance with evidence. |
| Binary template | Repeated “not X, but Y” or “not only X” constructions | Say Y directly or explain the real comparison. Keep genuine distinctions. |
| Fake alternative | The text invents an option only to reject it immediately | Remove the abandoned drafting path and state the governing constraint. |
| Forced completeness | Ideas repeatedly arrive in sets of three | Keep the number of items the subject actually requires. |
| Recap ending | The last paragraph repeats the piece or predicts a bright future | End on the last concrete consequence, decision, image, or next action. |
| Quotable closer | Every paragraph lands on a pull-quote: short, aphoristic, built to be lifted out. “Technology is manageable. People aren't.” Once is a beat; every time is a cadence the reader starts to hear coming | Let paragraphs end where their content ends, on a fact, a consequence, or a transition. Keep one closer that earns it. Sibling of **Recap ending**, which is the same move at the scale of the piece. |
| Header scaffolding | Many headings introduce one or two thin sentences | Merge related material. Use headings only when readers need navigation. |
| Heading echo | The first sentence merely restates the heading | Delete the echo and begin with new information. |

## Sentence and language problems

Patterns that only fail out loud (label read cold, speaker meta, trailer cadence, telegraphic speech, stacked precision) live in [spoken-register.md](spoken-register.md), because each is harmless in written prose.

| Pattern | Signal | Better move |
|---|---|---|
| Fake-strong verb | “Serves as,” “acts as,” or “boasts” avoids `is`, `has`, or a precise action | Use the plain verb or name what the subject does. |
| Nominalization fog | “Conducted an evaluation of” hides the action | Prefer “evaluated.” Keep domain nouns when the noun itself matters. |
| Missing actor | “A decision was made” leaves responsibility unclear | Name the actor when known and relevant. Passive voice is valid when it is not. |
| Synonym cycling | One subject becomes “the platform,” “the solution,” and “the tool” — or the prose switches away from the label the reader can see (“reasons” on screen, “causes” in the walk) | Repeat the clearest term, and when a screen or document is in view, use its word. Controlled repetition improves coherence. |
| Abstract business language | “Leverage robust capabilities to drive outcomes” | Name the user, action, mechanism, and result. |
| Canned transitions | Every paragraph begins “Additionally,” “Moreover,” or “Ultimately” | Use the logical relation, a topic sentence, or no transition. |
| Colon reveal | A label plus colon creates artificial drama: “The payoff: it learns.” | Write a sentence. Keep colons for real lists, labels, explanations, and quotations. |
| Dramatic fragments | Several clipped lines manufacture urgency or a mic-drop | Combine them unless the writer's established cadence earns the fragments. |
| Spec-sheet coda | A finished sentence is followed by a verbless list of qualities: “Plain language, no jargon, ready to use as it stands.” | Cut it, or make one of the qualities a sentence that says why it matters to the reader. |
| Org-chart actor | A department performs a human verb: "product quality gets the failure record." The reader pictures nobody. | Name the people: "the product engineers get the failure record." A function can own or approve; it cannot hear, learn, or remember. |
| Interface as narrator | A screen, app, map, record, row - or a derived artifact like a recommendation, finding, or proposal - performs a human verb, often with a vague pronoun carrying the sentence: "the app keeps score on itself," "the map admits what it does not know," "the recommendation splits the claim." | Say what is on screen, or name the actor: "the agent recommends 9,690 on us." A screen can show, list, or mark; it cannot admit, refuse, or keep score, and a recommendation cannot split anything - the agent that made it can. The tell is attitude or agency, and the noun list is open-ended: any artifact doing an actor's verb qualifies. **Partly linted:** `interface-acts-on-itself` catches the reflexive slice ("the map seeds itself", "the map draws itself"), which is the part a regex can hold. The general case stays judgment, because the noun and verb lists are open. |
| Circular assertion | The sentence defines a thing as itself: "the rules the owners gave the map are these rules," "the plan is the plan we agreed." | Say the content instead: name one or two of the rules. If there is nothing to name, the sentence had nothing to say. |
| Furniture inventory | The prose counts UI containers instead of reading them: "three cards:", "two panels:", "a strip of tiles". | Read what is in them: "autonomy at 93%, SLA posture improving, coverage review slowest." Pointing at one named element while walking it is fine; taking inventory is not. |
| Nominated significance | The line names what matters instead of delivering it: "the owner column **is the point**," "the re-render **is the point**," "**what matters is** how faithful it is," "the thing to notice is…," "**as you can see**," "**this distinction matters**," "**the key point is**," "**let that sink in**," "**make no mistake**," and the pseudo-cleft opener "**what makes this hard is**…" It steps outside the subject to tell the reader what to notice. It reads as confident and is doing the reader's noticing for them, which is why it survives edits that catch announced virtue: it sounds structural rather than boastful | Say the finding. "The owner column is the point" becomes "work that runs every day has no owner." If you cannot state the finding, the line has no point to nominate and the problem is the content. Distinct from **Announced virtue**, which rates the subject; this one ranks it. |
| Announced virtue | The prose rates its subject instead of showing it: "and it is honest," "the useful thing about it is what it admits," "that matters more than it sounds," "because a picture is not a receipt." | Cut the rating and let the next sentence do the work. If the evidence is already there, the reader supplies the judgment; if it is not there, the rating is the only claim being made. |
| Insider jargon | A term that describes the system to its builders, not the work to its readers: "read-only evidence," "system of record," "human-in-the-loop." | Say what happens in the reader's world: "the process looks at the equipment and never operates it." Keep a term of art only when the audience owns it. |
| Uniform rhythm | Similar sentence lengths and paragraph shapes repeat | Recast around the ideas. Vary pace where emphasis or complexity changes. |
| Dash and parenthesis dependency | Dashes and parenthetical asides repeatedly substitute for sentence decisions; an audit of one writer's 11,700 words found 78 dashes and 67 asides, and readers ranked the asides the stronger tell | Decide whether the aside is a sentence, a clause, or nothing. Keep dashes and parentheses when the writer uses them well. |
| Em dash default | The em dash (—) is the reflexive choice for every aside, where normal typing would produce a hyphen. Once a generic tell; by mid-2026 most models had suppressed it and Claude was the one still above professional writers' rate | Default to a typed dash - a bare hyphen, or a hyphen with a space on each side - and keep the em dash for the rare case it is the clearly better mark, not the first one reached for. |
| Clause-shape monotony | Three or more sentences in a row share a shape: all hedged ("although," "which," "may"), or all flat declaratives (subject, verb, object, full stop, repeat). The flat run is the one writers miss, because every sentence in it is individually good | Do not add clauses back in. Give one sentence a turn - a contrast, a repeat that lands, a piece of ordinary speech - and let its neighbours run shorter or longer than it does. Test by reading aloud: if three neighbouring sentences could trade places without loss, rewrite one. |
| Qualification pileup | “Could potentially perhaps” blurs the actual confidence level | Keep the one qualifier that matches the evidence. |
| Intensifier padding | “Really,” “genuinely,” “actually,” “truly,” “fundamentally,” “deeply” cluster in a piece, each promising a sincerity the sentence should carry by itself | Cut the intensifier and check whether the sentence still says something; if it does not, the intensifier was the claim. Twin of **Qualification pileup**. **Judgment only:** one “genuinely” in a paragraph is a word; a blanket adverb ban flattens voice, and this skill does not impose one. |
| Negative tail and runway | “No friction. No guessing.” replaces a complete consequence; or a run of negations delays the point: “Not a tool. Not a platform. A partner.” | State what the design lets the reader do, or say what the thing is first. The reader does not need a runway. |
| Backwards-facing clause | A clause is completed by an earlier one instead of standing up on its own: "built for exactly **that**," "runs the way the map **said it could**," "where nothing **made them wait**." Pointer words carry the structure, and a colon re-explains the thing it just pointed at. The listener has to hold the previous clause in memory to parse this one | Name the subject in the sentence that needs it. Define a thing by what it does, not by the absence of something or by a claim made earlier. Unaffordable in speech, where nobody can look back; see [spoken-register.md](spoken-register.md). |
| Deferred point | The claim arrives after its setup: “[condition], so [what actually happens]” | Lead with the claim. Put the condition, mechanism, or consequence after it. |
| Contrastive definition | The subject is fixed by what it is not: “X rather than Y,” “instead of,” “not a Z” | State what it is. Keep the contrast only when the reader would otherwise assume the wrong thing. |
| Mechanism-speak | Prose describes where data lives — “the estimate and the decision sit on one record” | Say what a person can now see, decide, or stop repeating. |
| Unglossed shorthand | An acronym or internal term appears cold for a reader outside the team | Expand on first use, or name the thing plainly and put the acronym in parentheses. |
| Generic second-person | “Whether you're a beginner or expert” pretends universal relevance | Name the real audience or remove the claim. |

## Formatting problems

| Pattern | Signal | Better move |
|---|---|---|
| Decorative emphasis | Emoji headings, bold labels on every bullet, or bold mid-sentence | Use hierarchy only to help scanning. |
| List reflex | Prose becomes bullets although sequence or comparison is absent | Use sentences when the ideas belong together. |

## Assistant residue

The manners of a helpful collaborator carried into prose that should stand alone, and the scaffolding of visible reasoning left in the final text. These are tendencies of Claude and of other models, not fingerprints, and they change as models change. For a changing model quirk, update the examples and forward tests before expanding this table.

Lexical tells are the fastest-moving layer and the least reliable. Readers in 2026 named "load-bearing," "genuinely," "full stop," "key insight," "root cause," "the trap," and "prose" for "text" as Claude habits; "delve" and "tapestry" were the 2024 list. Any one of them is a word. A cluster in one piece is evidence, and the fix is still the sentence, not the word.

| Pattern | Signal | Better move |
|---|---|---|
| Chatbot residue | “I hope this helps,” “Let me know,” or an unrequested offer closes the artifact | End with the artifact's final useful line. **Linted:** `chatbot-residue`. |
| Process narration | The prose explains that it will “explore” or “break down” the topic | Present the content itself. |
| Validation preamble | “Great question,” “You're absolutely right,” or praise of the user's framing precedes the answer | Keep acknowledgment only when it carries real relational meaning; otherwise answer. **Linted:** `validation-preamble`. |
| Prompt echo | The opening restates the user's request before doing it | Start with the result, decision, or artifact. |
| Collaboration theater | The assistant announces how it will “push gently,” names a fixed number of observations, or narrates what the user cannot see “from inside” | State the disagreement or observation in proportion to the evidence. **Linted:** `collaboration-theater`. |
| Unsupported defense | “To be clear, I'm not saying…” answers an objection no one raised | Remove the imaginary objection. Keep named or genuinely likely objections. |
| Question-answer pivot | “The result? A complete reset.” asks and answers a staged question; or a setup that announces an insight instead of delivering it: “What if I told you…,” “Think about it:” | Write the claim as a sentence unless the question creates real suspense or interaction. **Linted:** `question-answer-pivot`. |
| Taxonomy reflex | The response invents several named buckets, matrices, or “lenses” for a simple point | Keep only categories that change a decision or aid retrieval. |
| Balanced-by-default stance | Every claim receives a matching caveat or symmetrical counterpoint, so the piece sounds fair and says nothing | Match qualification to the evidence. Let a supported claim stand without a partner. |
| Correction-first argument | The prose says what a point is not before saying what it is: "This isn't about speed. It's about trust." | State the positive claim first. Keep the contrast only when the rejected reading is plausible and important. Sibling of **Binary template** and **Contrastive definition**. |
| Local recap | Each section ends with "The takeaway," "Why this matters," or a miniature conclusion | Integrate the consequence once. Let sections end at different depths. |
| Uniform helpfulness | Every edge is rounded, every disagreement softened, every paragraph resolves cleanly | Preserve warranted bluntness, ambiguity and unresolved tension. |
| Abstract personification | Strategies "unlock," systems "want," ideas "invite," with no actor or mechanism | Use the human or organisational actor when one exists. Sibling of **Interface as narrator** and **Org-chart actor**. |
| Candor announcement | The prose announces it is about to be frank: "Honestly?", "The honest answer is," "worth stating plainly," "I'll be direct," "here's where I'd push back," "the honest caveat." The frankness is asserted, not shown, and the reader now wonders what the rest was | Cut the announcement and say the thing. Distinct from **Announced virtue**, which rates the subject; this rates the speaker. **Linted:** `candor-announcement`. |

## Creative and narrative prose

Apply these only to fiction, memoir, narrative essays and brand storytelling. In every other register the fix for a vivid line is usually to keep it.

| Pattern | Signal | Better move |
|---|---|---|
| Pace compression | Every sentence strains to be vivid, revealing or quotable | Allow plain connective sentences so the important moments have contrast. |
| Device saturation | Metaphor, personification, juxtaposition and sensory detail appear because they sound literary | Keep each device only when it changes meaning, mood or point of view. |
| Abstract-concrete image formula | "Bruised silence," "a timestamp like a scar": a clever surface pattern repeated | Prefer one image anchored in this character and this scene. |
| Explained subtext | The narrator names every emotion, silence and thematic connection | Remove the explanations the action, detail or dialogue already carries. |
| Psychological tidiness | Characters understand themselves too quickly and behave consistently | Preserve believable contradiction, evasion, misdirection and delayed recognition. |
| Convergent mood | Ghosts, echoes, flickering light, melancholy technology and soft apocalypse as default atmosphere | Choose details that belong to this setting and no other. |

## Editing a set

Editing many pieces to one standard installs the standard as a new pattern. A phrasing that reads well once reads as a template at the fiftieth repetition, and the writer of the set is the last person able to see it.

Work in two passes. Fix the diagnosed problem first, then measure what the fix put in its place across the whole set: opening words, sentence counts, connectives, the shape of the closing clause. Treat any construction appearing in more than roughly a fifth of the set as a finding, whatever its quality in isolation.

Substitution is the usual failure. Removing mechanism-speak invites agentless passive. Varying the phrasing leaves every piece at the same sentence count. Banning three opening verbs leaves sixty pieces opening with the same article. Each pass must be measured, not assumed.

Count words rather than sentences when a length target matters. Sentence counts hide uniformity that word counts expose, and layout constrains words, not sentences.

`scripts/lint_natural_writing.py --set <file>` does the counting on a set of blank-line separated pieces: it reports any opening word, closing pair, or connective shared by more than a fifth of them. Run it after the fix pass, not instead of one — it measures what the fix installed and knows nothing about whether the fix was right.

## False-positive guardrails

Preserve these when they work:

- precise technical or academic vocabulary;
- passive voice that properly backgrounds the actor;
- one well-placed transition, fragment, or group of three; an em dash used once, deliberately, where a typed dash would lose something real;
- deliberate repetition used for rhythm, logic, or persuasion;
- genuine ambivalence, self-correction, asides, slang, profanity, humor, and dated references;
- necessary disclaimers, named objections, real alternatives, and version-specific change language;
- sincere acknowledgment in a conversation where the relationship matters;
- quotations, titles, proper names, code, commands, and interface labels.

## Repair sequence

1. Identify the sentence's actual job.
2. Keep the supported claim and the author's attitude toward it.
3. Remove framing that only announces importance, novelty, honesty, or depth.
4. Put an actor next to a precise action when the evidence allows it.
5. Add a concrete detail only if it already exists in the source.
6. Rebuild the paragraph so the fix sounds native, not patched.
7. Compare the rewrite with the source for lost or strengthened claims.
