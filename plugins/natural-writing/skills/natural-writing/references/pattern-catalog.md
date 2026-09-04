# Pattern catalog and repair heuristics

Use this catalog to diagnose repeated problems, not to fingerprint authorship. A single word, dash, short sentence, or polished paragraph proves nothing. Look for clusters, frequency, and effect.

Each table is followed by a worked example for every row in it, headed by the row's exact name, so the rule and its example are found by the same words. Every fact in an example's "after" is present in its "before"; that constraint is what makes the examples testable, and it is the constraint the skill works under. Where a heading names two rows, they arrive together in real drafts. `tests/test_catalog_structure.py` fails if a row has no example.

## Content problems

| Pattern | Signal | Better move |
|---|---|---|
| Importance inflation | Ordinary facts “mark a pivotal moment” or “underscore significance”; or a bare declaration of weight with nothing under it: “the stakes are high,” “the implications are significant,” “the reasons are structural” | State the fact and its supported consequence. Let the reader judge its weight. **Linted:** `importance-inflation`. |
| Sales varnish | “Vibrant,” “groundbreaking,” “renowned,” or “seamless” replaces evidence | Use the feature, result, constraint, or sensory detail already available. |
| Vague authority | “Experts say,” “studies show,” or “industry leaders agree” | Name the source and claim. If no source exists, cut or qualify the claim. **Linted:** `vague-authority`. |
| Superficial interpretation | A trailing `-ing` clause announces what a fact “highlights” or “showcases” | Explain a real mechanism or consequence, or end after the fact. **Linted:** `superficial-interpretation`. |
| Portability filler | A sentence could describe almost any company, person, city, or product | Replace it with subject-specific evidence or remove it. |
| Generic forecast | A challenges/future section predicts continued growth without evidence | Keep only dated plans, known constraints, or concrete next steps. |
| Unsupported certainty | Smooth prose quietly strengthens a tentative source | Restore the original scope, probability, and attribution. |
| Universal quantifier | “Everyone does this,” “nobody reads the manual,” “always,” “never,” where the source supports “most,” “the teams we asked,” or a number | Use the quantity the evidence supports. A universal is a claim about every case; if that is not what is known, it is not what should be said. **Judgment only.** |
| Vague connection | A relation is named without saying what it is: “associated with,” “in connection with,” “linked to,” “involved in” where the source gives the actual role | Say the role: founded, funded, sued, worked for, was born in. If the source does not say, keep the vagueness and know that it is the source's. **Judgment only:** the same phrases are correct when the relation genuinely is loose. |

### Importance inflation

Before:

> The launch represents a transformative milestone, underscoring our commitment to an ever-evolving customer landscape.

After:

> This is our first release that lets customers export their own audit history.

Why: the available fact carries the significance. If “first release” or the export feature were not in the source, the editor must not invent them.

### Sales varnish

Before:

> Our vibrant, groundbreaking platform delivers a seamless experience that customers love.

After:

> The platform lets a customer file a claim from their phone in under five minutes, and 82% of the ones who tried it finished without calling us.

Why: Four adjectives and no evidence. The after uses the two facts the source had, the time and the completion rate. If neither had been in the source, the after would be one plain sentence saying what the platform does.

### Vague authority

Before:

> Industry experts agree that the new workflow significantly improves productivity.

After when no source exists:

> The draft does not provide evidence for the productivity claim.

Why: a natural rewrite cannot manufacture a source or result.

### Superficial interpretation

Before:

> Revenue in the region grew 12% last year, highlighting the strength of the team and showcasing our commitment to growth.

After:

> Revenue in the region grew 12% last year, most of it from two enterprise renewals that closed in Q4.

Why: The trailing -ing clauses announce what the fact means without knowing. The after gives the mechanism the source had. If the source had no mechanism, the sentence ends after "last year."

### Portability filler

Before:

> Based in a thriving city with a rich history, the company is committed to innovation and to serving its customers with excellence.

After:

> The company makes brake sensors for freight trains in Tartu, and has done since 1996.

Why: The before could describe any company in any city. Every clause is portable. The after is only true of this one, using the product, place and date the source had.

### Generic forecast

Before:

> Looking ahead, the team is poised for continued growth as it navigates an evolving landscape and embraces new opportunities.

After:

> The team plans to open the Warsaw office in March and hire six engineers for it by June.

Why: A challenges-and-future paragraph that predicts nothing checkable. The after keeps only the dated plans the source had. No dated plan in the source means no forecast paragraph.

### Unsupported certainty

Before:

> I think the migration is probably safe, but the retry behavior still makes me nervous.

Bad edit:

> The migration is safe, although retry behavior remains a concern.

Better edit:

> I think the migration is probably safe, but the retry behavior still makes me nervous.

Why: unchanged. Both hedges and the feeling are the claim, at the confidence the author has, and the sentence is short enough to carry its own conjunction. Splitting it in two and dropping "probably" would be a taste change and a certainty change dressed as a repair. If the author wants it tighter, that is an option to offer, not an edit to make.

### Universal quantifier

Before:

> Everyone skips the onboarding video. Nobody reads the manual, and teams always find out the hard way.

After:

> Most of the teams we asked skipped the onboarding video, and four of the six had not opened the manual.

Why: **universal quantifier**. "Everyone," "nobody" and "always" are claims about every case. The source was a survey of six teams, so the after says so. If the source supported the universal, it would stay.

### Vague connection

Before:

> The foundation is associated with the university and has been linked to several regional hospitals.

After:

> The university founded the foundation in 1998, and it funds several regional hospitals.

Why: **vague connection**. "Associated with" and "linked to" refuse to say what the relation is when the source says it. If the source only said "associated," the vagueness is the source's and must stay.

## Structural problems

| Pattern | Signal | Better move |
|---|---|---|
| Throat clearing | “Here is the thing,” “It is worth noting,” “In today's world” | Start with the useful statement unless the setup adds voice or context. **Linted:** `throat-clearing`. |
| Manufactured insight | “What everyone misses” or “The deeper truth” precedes an ordinary claim | State the claim and earn its importance with evidence. |
| Binary template | Repeated “not X, but Y” or “not only X” constructions | Say Y directly or explain the real comparison. Keep genuine distinctions. **Linted:** `binary-template`. |
| Fake alternative | The text invents an option only to reject it immediately | Remove the abandoned drafting path and state the governing constraint. |
| Forced completeness | Ideas repeatedly arrive in sets of three | Keep the number of items the subject actually requires. |
| Recap ending | The last paragraph repeats the piece or predicts a bright future | End on the last concrete consequence, decision, image, or next action. |
| Quotable closer | Every paragraph lands on a pull-quote: short, aphoristic, built to be lifted out. “Technology is manageable. People aren't.” Once is a beat; every time is a cadence the reader starts to hear coming | Let paragraphs end where their content ends, on a fact, a consequence, or a transition. Keep one closer that earns it. Sibling of **Recap ending**, which is the same move at the scale of the piece. |
| Header scaffolding | Many headings introduce one or two thin sentences | Merge related material. Use headings only when readers need navigation. |
| Heading echo | The first sentence merely restates the heading | Delete the echo and begin with new information. |

### Throat clearing

Before:

> Here's the thing. It's worth noting that in today's world, teams need to move fast. So let's dive in: the deploy takes forty minutes.

After:

> The deploy takes forty minutes.

Why: Three throat-clearing phrases and one platitude precede the only fact. Keep setup only when it adds voice or context the reader needs; none of this did.

### Manufactured insight

Before:

> What everyone misses about onboarding is this: the deeper truth is that users churn in the first week. Here's what nobody tells you.

After:

> Users who do not finish setup in the first week churn at three times the rate of those who do.

Why: Three announcements of a hidden insight wrapped around an ordinary finding. The after states the finding with the number the source had and lets the reader decide how deep it is.

### Binary template and Correction-first argument

Before:

> The new pipeline isn't just faster — it's cheaper. And it's not about the tooling. It's about trust.

After:

> The new pipeline runs in forty minutes instead of three hours and costs a third as much per run. What changed for the team is that they trust it.

Why: **binary template** and **correction-first argument**, the most complained-about shape in every 2026 survey of AI prose. "Not X but Y" fakes an insight by rejecting a claim nobody made. The after states both facts and keeps the trust claim as the source made it, without inventing a mechanism for it. Every number is from the source; if the source had none, the after would say "faster and cheaper" and stop.

### Fake alternative

Before:

> We could have rebuilt the whole pipeline from scratch, but that would have taken months, so instead we patched the scheduler.

After:

> We patched the scheduler.

Why: The rejected option was never a live choice; it is a drafting path left in the text so the real choice looks considered. If the source shows the rebuild was genuinely weighed, keep it with the reason it lost.

### Forced completeness

Before:

> The rollout was fast, simple, and effective. Teams saw fewer tickets, quicker approvals, and happier customers.

After:

> The rollout took two weeks. Support tickets about approvals fell by half in the first month.

Why: **forced completeness**. Two triplets in two sentences, six qualities, one fact. The source had two facts, so the after has two. One adjective with proof beats three without.

### Recap ending

Before:

> The migration finishes Tuesday and support gets the new screen Wednesday. In summary, this change brings faster exports and a cleaner interface, and positions us well for a bright future of continued improvement.

After:

> The migration finishes Tuesday and support gets the new screen Wednesday.

Why: The last sentence repeats the piece and predicts the weather. End on the last concrete fact or the next action. If a summary is genuinely needed for a long document, it says something the body did not.

### Quotable closer

Before:

> The rota has two people on it and one of them is on leave until March. Coverage is a fiction.
>
> The alerts route to a channel with forty members and no owner. Everyone is responsible, so nobody is.
>
> The runbook was last edited in 2023. Documentation is where good intentions go to die.

After:

> The rota has two people on it and one of them is on leave until March. The alerts route to a channel with forty members and no owner, and the runbook was last edited in 2023, so the person who picks up the page has nothing current to work from.

Why: **quotable closer**. Three paragraphs each land on a line built to be lifted out, and by the third the reader hears it coming. The facts belong together; the after keeps them and ends on the consequence for the person paged. Keep one closer when it earns its place.

### Header scaffolding

Before:

> ## Background
>
> The API was slow.
>
> ## Problem
>
> Requests took four seconds.
>
> ## Solution
>
> We added a cache.
>
> ## Result
>
> Requests take 200 milliseconds.

After:

> Requests to the API took four seconds. We added a cache, and they now take 200 milliseconds.

Why: Four headings over four sentences. Headings are for navigation; a reader cannot get lost in two sentences. Keep headings when a reader will jump between sections.

### Heading echo

Before:

> ## Why the cache matters
>
> The cache matters because it reduces load on the database and speeds up responses.

After:

> ## Why the cache matters
>
> Every request used to hit the database; now nine in ten are served from memory, and response time fell from four seconds to 200 milliseconds.

Why: The first sentence restated the heading and added nothing. The after begins with the information the heading promised.

## Sentence and language problems

Patterns that only fail out loud (label read cold, speaker meta, trailer cadence, telegraphic speech, stacked precision) live in [spoken-register.md](spoken-register.md), because each is harmless in written prose.

| Pattern | Signal | Better move |
|---|---|---|
| Fake-strong verb | “Serves as,” “acts as,” or “boasts” avoids `is`, `has`, or a precise action | Use the plain verb or name what the subject does. |
| Nominalization fog | “Conducted an evaluation of” hides the action | Prefer “evaluated.” Keep domain nouns when the noun itself matters. |
| Missing actor | “A decision was made” leaves responsibility unclear | Name the actor when known and relevant. Passive voice is valid when it is not. |
| Synonym cycling | One subject becomes “the platform,” “the solution,” and “the tool” — or the prose switches away from the label the reader can see (“reasons” on screen, “causes” in the walk) | Repeat the clearest term, and when a screen or document is in view, use its word. Controlled repetition improves coherence. |
| Abstract business language | “Leverage robust capabilities to drive outcomes” | Name the user, action, mechanism, and result. |
| Stock vocabulary | “Delve,” “tapestry,” “landscape,” “robust,” “seamless,” “leverage,” “multifaceted,” “full stop”: the words readers have learned to associate with machine prose. The list dates fast; the 2026 additions are in the **Assistant residue** note | Use the ordinary word, and check whether the sentence still says anything without it. One such word is a word; a cluster is evidence, and the fix is the sentence. **Linted:** `stock-vocabulary`, a short dated list, a review prompt only. |
| Canned transitions | Every paragraph begins “Additionally,” “Moreover,” or “Ultimately” | Use the logical relation, a topic sentence, or no transition. |
| Colon reveal | A label plus colon creates artificial drama: “The payoff: it learns.” | Write a sentence. Keep colons for real lists, labels, explanations, and quotations. |
| Dramatic fragments | Several clipped lines manufacture urgency or a mic-drop | Combine them unless the writer's established cadence earns the fragments. |
| Spec-sheet coda | A finished sentence is followed by a verbless list of qualities: “Plain language, no jargon, ready to use as it stands.” | Cut it, or make one of the qualities a sentence that says why it matters to the reader. **Linted:** `spec-sheet-coda`. |
| Org-chart actor | A department performs a human verb: "product quality gets the failure record." The reader pictures nobody. | Name the people: "the product engineers get the failure record." A function can own or approve; it cannot hear, learn, or remember. **Linted:** `org-chart-actor`. |
| Interface as narrator | A screen, app, map, record, row - or a derived artifact like a recommendation, finding, or proposal - performs a human verb, often with a vague pronoun carrying the sentence: "the app keeps score on itself," "the map admits what it does not know," "the recommendation splits the claim." | Say what is on screen, or name the actor: "the agent recommends 9,690 on us." A screen can show, list, or mark; it cannot admit, refuse, or keep score, and a recommendation cannot split anything - the agent that made it can. The tell is attitude or agency, and the noun list is open-ended: any artifact doing an actor's verb qualifies. **Partly linted:** `interface-acts-on-itself` catches the reflexive slice ("the map seeds itself", "the map draws itself"), which is the part a regex can hold. The general case stays judgment, because the noun and verb lists are open. |
| Circular assertion | The sentence defines a thing as itself: "the rules the owners gave the map are these rules," "the plan is the plan we agreed." | Say the content instead: name one or two of the rules. If there is nothing to name, the sentence had nothing to say. **Linted:** `circular-assertion`. |
| Furniture inventory | The prose counts UI containers instead of reading them: "three cards:", "two panels:", "a strip of tiles". | Read what is in them: "autonomy at 93%, SLA posture improving, coverage review slowest." Pointing at one named element while walking it is fine; taking inventory is not. **Linted:** `furniture-inventory`. |
| Nominated significance | The line names what matters instead of delivering it: "the owner column **is the point**," "the re-render **is the point**," "**what matters is** how faithful it is," "the thing to notice is…," "**as you can see**," "**this distinction matters**," "**the key point is**," "**let that sink in**," "**make no mistake**," and the pseudo-cleft opener "**what makes this hard is**…" It steps outside the subject to tell the reader what to notice. It reads as confident and is doing the reader's noticing for them, which is why it survives edits that catch announced virtue: it sounds structural rather than boastful | Say the finding. "The owner column is the point" becomes "work that runs every day has no owner." If you cannot state the finding, the line has no point to nominate and the problem is the content. Distinct from **Announced virtue**, which rates the subject; this one ranks it. **Linted:** `nominated-significance`. |
| Announced virtue | The prose rates its subject instead of showing it: "and it is honest," "the useful thing about it is what it admits," "that matters more than it sounds," "because a picture is not a receipt." | Cut the rating and let the next sentence do the work. If the evidence is already there, the reader supplies the judgment; if it is not there, the rating is the only claim being made. **Linted:** `announced-virtue`. |
| Insider jargon | A term that describes the system to its builders, not the work to its readers: "read-only evidence," "system of record," "human-in-the-loop." | Say what happens in the reader's world: "the process looks at the equipment and never operates it." Keep a term of art only when the audience owns it. **Linted:** `insider-jargon`. |
| Uniform rhythm | Similar sentence lengths and paragraph shapes repeat | Recast around the ideas. Vary pace where emphasis or complexity changes. |
| Dash and parenthesis dependency | Dashes and parenthetical asides repeatedly substitute for sentence decisions; an audit of one writer's 11,700 words found 78 dashes and 67 asides, and readers ranked the asides the stronger tell | Decide whether the aside is a sentence, a clause, or nothing. Keep dashes and parentheses when the writer uses them well. **Linted:** `dash-cluster`. |
| Em dash default | The em dash (—) is the reflexive choice for every aside, where normal typing would produce a hyphen. Once a generic tell; by mid-2026 most models had suppressed it and Claude was the one still above professional writers' rate | Default to a typed dash - a bare hyphen, or a hyphen with a space on each side - and keep the em dash for the rare case it is the clearly better mark, not the first one reached for. |
| Clause-shape monotony | Three or more sentences in a row share a shape: all hedged ("although," "which," "may"), or all flat declaratives (subject, verb, object, full stop, repeat). The flat run is the one writers miss, because every sentence in it is individually good | Do not add clauses back in. Give one sentence a turn - a contrast, a repeat that lands, a piece of ordinary speech - and let its neighbours run shorter or longer than it does. Test by reading aloud: if three neighbouring sentences could trade places without loss, rewrite one. |
| Qualification pileup | “Could potentially perhaps” blurs the actual confidence level | Keep the one qualifier that matches the evidence. |
| Intensifier padding | “Really,” “genuinely,” “actually,” “truly,” “fundamentally,” “deeply” cluster in a piece, each promising a sincerity the sentence should carry by itself | Cut the intensifier and check whether the sentence still says something; if it does not, the intensifier was the claim. Twin of **Qualification pileup**. **Judgment only:** one “genuinely” in a paragraph is a word; a blanket adverb ban flattens voice, and this skill does not impose one. |
| Negative tail and runway | “No friction. No guessing.” replaces a complete consequence; or a run of negations delays the point: “Not a tool. Not a platform. A partner.” | State what the design lets the reader do, or say what the thing is first. The reader does not need a runway. |
| Backwards-facing clause | A clause is completed by an earlier one instead of standing up on its own: "built for exactly **that**," "runs the way the map **said it could**," "where nothing **made them wait**." Pointer words carry the structure, and a colon re-explains the thing it just pointed at. The listener has to hold the previous clause in memory to parse this one | Name the subject in the sentence that needs it. Define a thing by what it does, not by the absence of something or by a claim made earlier. Unaffordable in speech, where nobody can look back; see [spoken-register.md](spoken-register.md). **Linted:** `backwards-facing-clause`. |
| Deferred point | The claim arrives after its setup: “[condition], so [what actually happens]” | Lead with the claim. Put the condition, mechanism, or consequence after it. **Linted:** `deferred-point`. |
| Contrastive definition | The subject is fixed by what it is not: “X rather than Y,” “instead of,” “not a Z” | State what it is. Keep the contrast only when the reader would otherwise assume the wrong thing. **Linted:** `contrastive-definition`. |
| Mechanism-speak | Prose describes where data lives — “the estimate and the decision sit on one record” | Say what a person can now see, decide, or stop repeating. **Linted:** `mechanism-speak`. |
| Unglossed shorthand | An acronym or internal term appears cold for a reader outside the team | Expand on first use, or name the thing plainly and put the acronym in parentheses. |
| Generic second-person | “Whether you're a beginner or expert” pretends universal relevance | Name the real audience or remove the claim. |

### Fake-strong verb

Before:

> The dashboard serves as the central hub for the team and boasts a real-time view of every open incident.

After:

> The dashboard is where the team works, and it shows every open incident in real time.

Why: "Serves as" and "boasts" avoid "is" and "shows" because they sound stronger. They are not; they are longer. Use the plain verb or name what the thing does.

### Nominalization fog

Before:

> The team conducted an evaluation of the vendor's proposal and reached a determination that a rejection was warranted.

After:

> The team evaluated the vendor's proposal and rejected it.

Why: Three actions hidden in nouns: evaluation, determination, rejection. The verbs were there all along. Keep a noun when the noun itself is the subject, as "the evaluation" would be in a sentence about how long it took.

### Missing actor

Before:

> A decision was made to postpone the launch. Concerns were raised about the payment flow, and it was agreed that a fix would be prioritised.

After:

> The product lead postponed the launch after the QA team raised concerns about the payment flow, and the product lead and the QA team agreed to fix it first.

Why: Three passives, no one responsible. The after names the actors the source named. Passive stays when the actor is unknown or genuinely irrelevant: "the server was restarted at 03:00" needs no name.

### Synonym cycling

Before (the source's glossary says worker, assistant and tool all name the same process):

> The worker reads the queue. The assistant validates each item before the tool writes it.

After:

> The worker reads the queue, validates each item, and then writes it.

Why: one stable term is clearer than three decorative synonyms.

### Abstract business language

Before:

> The dashboard streamlines collaboration and empowers teams to move faster.

After:

> The dashboard puts review comments, owners, and due dates on one screen.

Why: use this repair only when those features appear in the source.

### Stock vocabulary

Before:

> We delve into a rich tapestry of multifaceted challenges across the ever-evolving landscape, leveraging robust, seamless solutions. Full stop.

After:

> We looked at four problems the finance team reported and fixed the two that recur.

Why: Eight of the words readers have learned to associate with machine prose, in two sentences. The fix is never the word; it is the sentence, which here had no content until the facts were put back. One such word in a paragraph is a word.

### Canned transitions

Before:

> The API is slow. Additionally, the docs are out of date. Moreover, the SDK has not been updated. Furthermore, the team is small. Ultimately, adoption has stalled.

After:

> The API is slow, the docs are out of date, and the SDK has not been updated. The team is small, and adoption has stalled.

Why: Every sentence opens on a connector that means "and." The after says "and" and lets the facts sit as a list. If the source had said the small team is why nothing gets fixed, "so" would be the right word; it did not, so no connector may claim it.

### Colon reveal

Before:

> The team tried three approaches. The one that worked: caching. The payoff: response times fell by 95%.

After:

> The team tried three approaches, and caching was the one that worked. Response times fell by 95%.

Why: Two label-plus-colon constructions manufacture drama around ordinary facts. Write the sentence. Keep colons for lists, labels, explanations and quotations.

### Dramatic fragments (kept)

Before:

> We had one hour left. No backup. And the customer was already in the room.

After:

> We had one hour left. No backup. The customer was already in the room.

Why: the fragment creates pressure and fits the story. Remove only the decorative conjunction.

### Spec-sheet coda

Before:

> The summary goes to the adjuster the moment the site visit ends. Plain language, no jargon, ready to use as it stands.

After:

> The summary goes to the adjuster the moment the site visit ends, written so they can use it without editing it.

Why: **spec-sheet coda**. Three verbless qualities read as a product blurb. One of them, turned into a consequence for the reader, does the work of all three. "Use it without editing" is what "ready to use as it stands" meant; no new claim.

### Org-chart actor

Before:

> Product quality gets the failure record and learns which supplier batch caused it. Compliance hears about it the same afternoon.

After:

> The product engineers get the failure record and learn which supplier batch caused it. The compliance officer is told the same afternoon.

Why: **org-chart actor**. A function can own or approve; it cannot hear or learn. The reader pictures nobody until a person appears. "Engineers" and "officer" are the roles the source named for those functions; do not invent a title the source does not have.

### Interface as narrator

Before:

> The app keeps score on itself. The map admits what it does not know, and each one says who owns it.

After:

> The app shows its own accuracy, month by month. Where the map has no data, it shows a gap, and every process on it names an owner.

Why: **interface as narrator**. Screens show, list and mark; they do not admit or keep score. The tell is attitude. The after says what is on screen. "Month by month" and "names an owner" were in the source's surrounding text; the edit borrows from the piece, not from imagination.

### Circular assertion

Before:

> The rules the owners gave the map are these rules. The process we follow is the process we agreed.

After:

> The owners gave the map two rules: nothing runs without a named owner, and nothing runs without a rollback.

Why: Both sentences define a thing as itself. The after names the rules and stops; a closing "that is the process" would point back at them and say nothing new. If the source had not said what the rules were, the sentences had nothing to say and should go.

### Furniture inventory

Before:

> The overview screen has three cards: a status card, a metrics card and an alerts card. Below them sit two panels.

After:

> The overview shows autonomy at 93%, SLA posture improving for the third week, and coverage review as the slowest stage, with the four open alerts listed underneath.

Why: The before counts containers. The after reads what is in them, using the values the source gave. Pointing at one named element while walking through it is fine; taking inventory is not.

### Nominated significance

Before:

> Look at the owner column. That is the point. What matters is how many of these run every day.

After:

> Half of these processes run every day, and none of them has an owner.

Why: **nominated significance**. "That is the point" and "what matters is" tell the reader something matters without saying what. The after states the finding. It sounds less confident and says more. If the finding cannot be stated, the sentence has nothing to nominate.

### Announced virtue

Before:

> The ledger is empty when the map is published, and it is honest about that. The useful thing about it is what it admits.

After:

> The ledger is empty when the map is published. Every entry that appears afterwards was made by a person, with their reason attached.

Why: **announced virtue**. "It is honest" and "the useful thing about it" rate the subject. The second sentence of the after is the evidence the rating was standing in for; it was in the source. If it had not been, the rating was the only claim and the paragraph had nothing to say.

### Insider jargon

Before:

> The process has read-only access to the equipment and acts as the system of record for every human-in-the-loop decision.

After:

> The process looks at the equipment and never operates it. Every decision a person makes is kept, with who made it and when.

Why: **insider jargon**. "Read-only," "system of record," and "human-in-the-loop" describe the system to its builders. The reader is a plant manager; each term becomes what they would see. Keep the terms if the audience owns them.

### Uniform rhythm

Before:

> The team met on Monday to review the plan. They found two risks in the payment flow. They agreed to fix the first one this week. They deferred the second one to next sprint. The plan was updated the same afternoon.

After:

> The team met on Monday and found two risks in the payment flow. The first gets fixed this week. The second waits for next sprint, and the plan was updated that afternoon to say so.

Why: Five sentences of nine to eleven words, each subject-verb-object. Nothing is wrong with any one of them. The after varies length where the ideas vary: the deferred risk gets the longer sentence because it carries the follow-up.

### Dash and parenthesis dependency

Before:

> The rollout (which took three weeks — longer than planned) went smoothly — mostly — and nobody (to our surprise) paged on-call.

After:

> The rollout took three weeks, longer than planned. It went mostly smoothly, and nobody paged on-call, which surprised us.

Why: Five asides in one sentence, each a decision the writer did not make. The after decides: two facts become two sentences, the surprise becomes a clause, and the hedge on "smoothly" stays where it was. Keep a dash or a parenthesis when the aside genuinely interrupts.

### Em dash default

Before:

> The rollout went smoothly — better than expected — and nobody paged on-call.

After:

> The rollout went smoothly, better than expected, and nobody paged on-call.

Why: neither aside earns an em dash. Commas carry both without loss. Keep the em dash only for the rare case where a comma or parenthesis would blur the break the writer intends.

### Clause-shape monotony

Before:

> The migration might slip, although the team is confident. It may still land Friday, which would be a relief. The risk, arguably, is the integration test, which is flaky. Support could see a spike, since the change touches billing.

After:

> The migration might slip, although the team is confident. It may still land Friday. The integration test is flaky, and it is the risk. Support could see a spike, because the change touches billing.

Why: four hedged, subordinate-clause sentences in a row read as one long qualification instead of four separate points. Recasting two of them as direct statements lets the real hedges (“might,” “may still”) carry their own weight.

### Qualification pileup

Before:

> The change could potentially reduce onboarding time somewhat, and it may possibly be worth noting that some teams might see a benefit.

After:

> The change could reduce onboarding time. Two of the five pilot teams saw it.

Why: **qualification pileup**. Six hedges cover one tentative claim and hide the evidence that would let the reader judge it. The after keeps one of the Before's own qualifiers ("could") and gives the number the hedging was standing in for. If the pilot count were not in the source, the after would end after the first sentence.

### Intensifier padding

Before:

> This is genuinely hard. The teams really do struggle with it, and it truly matters that we actually fix it this quarter.

After:

> Three of the five teams missed the deadline because of it, and it has to be fixed this quarter.

Why: **intensifier padding**. Four intensifiers promise a sincerity the sentences never earn; strip them and the before says almost nothing. The after replaces the promise with the evidence the source had. The skill does not ban adverbs; one "genuinely" in a paragraph is a word.

### Negative tail and runway

Before:

> Not a tool. Not a platform. Not another dashboard. A partner. No friction. No guessing.

After:

> Ledgerline reconciles invoices and flags every mismatch above £5, so the finance team stops re-keying figures from three systems.

Why: Three negations before the noun and two after it. The reader does not need a runway. The after says what the thing is and what it lets the reader stop doing, using the facts the source had.

### Backwards-facing clause

Before:

> The team built the intake form for exactly that. It runs the way the map said it could, in a week where nothing made them wait.

After:

> The team built the intake form to catch a missing policy number before the claim is filed. It went live in a week, and no approval was pending on it at any point.

Why: **backwards-facing clause**. "Exactly that," "the way the map said it could," and "where nothing made them wait" each point at an earlier sentence the reader must hold in memory. The after names the subject in the sentence that needs it. In speech this is the difference between following and losing the thread. The specifics ("missing policy number," "no approval pending") come from the source paragraph.

### Deferred point and Mechanism-speak

Before:

> Because the estimate and the approval now sit on one record, the reviewer no longer has to rebuild the file from three systems, so the claim closes on the day it is approved.

After:

> The claim closes on the day it is approved. The reviewer sees the estimate and the approval together and no longer rebuilds the file from three systems.

Why: **deferred point** and **mechanism-speak** together. The reader wanted the consequence; the sentence made them wait through where the data lives to get it. The mechanism survives, one sentence later, said as what a person now sees.

### Contrastive definition

Before:

> This is not a dashboard. Instead of charts, it is a queue of decisions rather than a picture of the work.

After:

> It is a queue of decisions. Each row is one thing a person has to approve, reject, or send back.

Why: **contrastive definition** three times in two sentences, and no positive statement until the third clause. The second "after" sentence is drawn from what a queue of decisions is, not invented; if the source had not said what a row holds, the edit would stop after the first sentence.

### Unglossed shorthand

Before:

> The SoR sync runs nightly and pushes deltas to the CDP, with HITL review on any record over the threshold.

After:

> The nightly sync copies the day's changes from the master record into the customer data platform, and a person reviews any record over the threshold before it goes.

Why: Three acronyms cold, for a reader outside the team. The after says each thing plainly. For a reader who owns the terms, keep them; the register decides.

### Generic second-person

Before:

> Whether you're a seasoned CFO or just starting out in finance, Ledgerline has something for you.

After:

> Ledgerline is built for finance teams of two to twenty people who close the books monthly.

Why: "Whether you're X or Y" pretends universal relevance and names no one. The after names the audience the source named. If the source named no audience, cut the sentence.

## Formatting problems

| Pattern | Signal | Better move |
|---|---|---|
| Decorative emphasis | Emoji headings, bold labels on every bullet, or bold mid-sentence | Use hierarchy only to help scanning. |
| List reflex | Prose becomes bullets although sequence or comparison is absent | Use sentences when the ideas belong together. |

### Decorative emphasis and List reflex

Before:

> - **Speed:** The new parser is faster.
> - **Reliability:** It fails less often.
> - **Cost:** It runs on smaller machines.

After:

> The new parser is faster, fails less often, and runs on smaller machines, so the batch that used to need the large instance now runs on the standard one.

Why: **decorative emphasis** and **list reflex**. Three bullets with bold labels present three thin sentences as a framework. They belong together, so they are one sentence, and the consequence at the end is the reason the reader cared. Keep bullets for sequence or comparison.

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

### Chatbot residue

Before:

> The migration finishes Tuesday and support gets the new screen Wednesday. I hope this helps! Let me know if you'd like me to expand on any of this.

After:

> The migration finishes Tuesday and support gets the new screen Wednesday.

Why: The artifact ended two sentences before the text did. A standalone document has no chat turn to keep open.

### Process narration

Before:

> In this memo I will explore the causes of the outage, break down the timeline, and then walk through the remediation steps.

After:

> The outage began at 02:14 when the primary database ran out of disk.

Why: The before describes the memo; the after begins it. Present the content. A table of contents is navigation and can stay; a sentence announcing that content is coming cannot.

### Validation preamble

Before:

> Great question, and you're absolutely right to focus on onboarding. That's exactly the key distinction. I would recommend a two-week pilot with the Lisbon team.

After:

> Run a two-week pilot with the Lisbon team.

Why: Two sentences of praise for the reader's framing before the recommendation. In a standalone document the acknowledgment carries nothing; in a conversation where the relationship matters, one sincere sentence can stay.

### Prompt echo

Before:

> You asked me to summarise the three risks in the Q3 plan and suggest which to address first. Here is that summary. The three risks are…

After:

> The Q3 plan carries three risks, and the payment-flow risk should be fixed first.

Why: The opening restates the request before doing it. Start with the result. The reason for the priority, if the source had one, would follow; none is invented here.

### Collaboration theater

Before:

> Three things you improved, and one thing I want to push on gently, which may be hard to see from inside: the pricing argument still has no evidence behind it.

After:

> The pricing argument has no evidence behind it.

Why: The before stages the posture of a careful colleague; the after delivers the judgment. State the observation in proportion to the evidence and leave out the choreography.

### Unsupported defense

Before:

> To be clear, I'm not saying the team is at fault, and this shouldn't be read as criticism of the process. The rota has two people on it.

After:

> The rota has two people on it.

Why: Two sentences answer an objection nobody raised. Remove the imaginary objection. Keep a defense when a named person actually made the objection or the reader plainly will.

### Question-answer pivot

Before:

> What if I told you the fix was one line? Think about it. The result? A 95% drop in response time.

After:

> The fix was one line, and response time fell by 95%.

Why: Three staged questions and a one-word answer. Write the claim as a sentence. A question stays when it creates real suspense or asks the reader something.

### Taxonomy reflex

Before:

> There are three lenses here: the strategic lens, the operational lens, and the human lens. Strategically, we lack a buyer. Operationally, we lack an owner. Through the human lens, the team is tired.

After:

> We have no buyer, no owner, and a tired team.

Why: Three named lenses for three facts that needed no framework. Keep categories when they change a decision or help a reader compare; here they only delayed the facts.

### Balanced-by-default stance

Before:

> The cache cut response time by 95%, although it does add operational complexity. The team is pleased, though some may feel differently. On balance it is probably positive, but there are trade-offs.

After:

> The cache cut response time by 95% and adds one more service to run. The team is pleased with it.

Why: Every claim came with a counterweight so the paragraph would sound fair, and it ended up saying nothing. The after keeps the one real cost the source named and drops the ritual qualifications.

### Local recap

Before:

> …so the cache serves nine in ten requests from memory.
>
> The takeaway: caching matters.
>
> ## Deployment
>
> …and the rollout finished Tuesday.
>
> Why this matters: shipping on time builds trust.

After:

> …so the cache serves nine in ten requests from memory.
>
> ## Deployment
>
> …and the rollout finished Tuesday.

Why: Each section ended on a miniature conclusion restating itself. Let sections end at different depths and state the consequence once, where it lands.

### Uniform helpfulness

Before:

> The vendor's estimate may be somewhat optimistic, and there could be room to explore alternatives, though their team has been very responsive and the relationship remains strong.

After:

> The vendor's estimate is a third below what the last two projects actually cost, and we should not sign it as it stands.

Why: Every edge rounded, the disagreement softened to nothing, the paragraph resolving cleanly. The source's author thought the estimate was wrong; the after lets them say so with the number they had.

### Abstract personification

Before:

> The strategy unlocks new markets, the platform wants to scale, and the data invites us to reconsider pricing.

After:

> The sales team can now sell in Poland and Czechia, the platform handles ten times the current load, and last quarter's churn numbers are the reason we are reconsidering pricing.

Why: Strategies, platforms and data performing human verbs with no actor. The after names who does what, using the facts the source had. Sibling of Interface as narrator and Org-chart actor.

### Candor announcement

Before:

> Honestly? The honest answer is that the pilot is not ready. Here's where I'd push back: the vendor's number is six months old.

After:

> The pilot is not ready. The vendor's number is six months old.

Why: **candor announcement**. Three phrases announce frankness before any frank thing is said, and the reader now wonders what the rest of the memo was. The two facts carry the bluntness by themselves.

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

### Pace compression

Before:

> The door screamed on its hinges. Rain knifed the glass. Her heart was a fist. Every shadow held a verdict. She crossed to the desk like a woman walking into the sea.

After:

> The door was loud on its hinges and the rain had not let up. She crossed to the desk.

Why: Five sentences straining to be quotable, so none of them lands. The after lets three plain sentences carry the room so the one moment that matters, the walk to the desk, has contrast. No story fact added.

### Device saturation

Before:

> The city breathed beneath a bruised sky, its streets veins of amber light, the towers standing sentinel like patient gods, the wind whispering secrets through the iron lungs of the trains.

After:

> The streets were lit amber and the towers were dark. A train went through below, loud enough to feel.

Why: Personification, metaphor and simile in one sentence, each because it sounded literary. The after keeps the images the scene needs, the amber and the train, and drops the ones that only decorate.

### Abstract-concrete image formula

Before:

> A bruised silence. A timestamp like a scar. Grief the shape of an unanswered call.

After:

> The phone showed the missed call at 02:14 and nothing after it.

Why: Three images built on the same template, an abstraction bolted to a concrete noun. The after uses one detail that belongs to this character and this night, the time on the phone, and lets it do the work.

### Explained subtext

Before:

> He set two cups on the table, then remembered she was gone, and a wave of grief washed over him as he realised how deeply he still missed her.

After:

> He set two cups on the table, then remembered, and put one back.

Why: The action already carried the emotion; the second half of the sentence explained it to a reader who had understood. "Put one back" is drawn from the scene, not added to it.

### Psychological tidiness

Before:

> Mara understood at once that her anger at her sister was really grief for their mother, forgave her, and felt the weight lift.

After:

> Mara told her sister she was fine, and then did not call her for a month.

Why: The character diagnosed herself in one sentence and resolved. The after keeps the contradiction and the delay, which is how people behave. The estrangement is in the source; the tidy insight was not.

### Convergent mood

Before:

> The abandoned server room hummed with ghost light, screens flickering with the echoes of forgotten users, a soft apocalypse of dust and melancholy code.

After:

> The server room was still running, though nobody had logged in since March. The fans were the only sound, and there was dust on the racks.

Why: Ghosts, echoes, flicker, melancholy technology, soft apocalypse: the default atmosphere every model reaches for. The after picks details that belong to this room and no other.

## Editing a set

Editing many pieces to one standard installs the standard as a new pattern. A phrasing that reads well once reads as a template at the fiftieth repetition, and the writer of the set is the last person able to see it.

Work in two passes. Fix the diagnosed problem first, then measure what the fix put in its place across the whole set: opening words, sentence counts, connectives, the shape of the closing clause. Treat any construction appearing in more than roughly a fifth of the set as a finding, whatever its quality in isolation.

Substitution is the usual failure. Removing mechanism-speak invites agentless passive. Varying the phrasing leaves every piece at the same sentence count. Banning three opening verbs leaves sixty pieces opening with the same article. Each pass must be measured, not assumed.

Count words rather than sentences when a length target matters. Sentence counts hide uniformity that word counts expose, and layout constrains words, not sentences.

`scripts/lint_natural_writing.py --set <file>` does the counting on a set of blank-line separated pieces: it reports any opening word, closing pair, or connective shared by more than a fifth of them. Run it after the fix pass, not instead of one — it measures what the fix installed and knows nothing about whether the fix was right.

### Editing a set

A set of forty one-line captions each opened with a verb, and the note said to vary them. The pass varied the verbs. The linter's `--set` mode then reported that sixteen of forty now opened on "The", and twelve ended on the same two-word shape, "at once."

The second pass fixed what the first one installed: openings moved to the subject, the actor, or the number the caption rests on, and the closing shape was allowed to vary with the point being made.

Why: **Editing a set**. A standard applied across many items becomes the next pattern, and the writer of the set is the last person able to see it. Measure after every pass, not only after the first.

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

## Workflow examples

The mode and workflow rules in SKILL.md and eval.md, shown once each.

### Ask before a substantial pass: stated assumptions

Draft (an executive update):

> You're absolutely right to focus on the Q3 rollout. The migration isn't just a technical change, it's a shift in how the whole organisation thinks about data. The cutover finished on 14 August, two days late.

Two correct edits, depending on a question the draft cannot answer:

> Edited as a status report to the VP. The cutover finished on 14 August, two days late.

> Edited as the case for the migration, your judgments kept. The cutover finished on 14 August, two days late, and the change is bigger than the engineering: it moves the whole organisation onto one view of its data.

Why: the framing claim is a fact to cut in a report and a stance to keep in an argument, and nothing in the draft says which the author meant. Two editors following this skill produced one each. The repair is not a better guess; it is the first line of the note, which names the assumption so the author can correct it before reading on. When the pass is large enough, ask instead, with the default attached.

### Diagnose mode: Manufactured insight, Binary template, Sales varnish

Text:

> Here's what nobody tells you: great onboarding isn't just documentation. It's a journey that empowers every user.

Report:

- **Manufactured insight:** “Here's what nobody tells you” claims exclusivity without evidence. Start with the onboarding claim.
- **Binary template:** “isn't just documentation” delays the actual comparison. Name what onboarding includes.
- **Sales varnish:** “journey that empowers every user” gives no mechanism or outcome. Add supported specifics or cut it.

### Offer options when the call is taste

The author asked for a stronger opening paragraph on a memo. Correctness had one answer; the opening had several. The response offered three, each stating the same facts:

- Lead with the decision the reader must make by Friday. Trades away the context a first-time reader needs.
- Lead with the one number that changed since the last memo. Trades away breadth; the reader may think the memo is only about that number.
- Lead with the customer's own words from the escalation. Trades away neutrality; it frames the memo as a response rather than a plan.

The recommendation was the first, because the reader was a single decision-maker who already knew the context. The author chose the third "stylistically" and asked for the quote to be shorter. The next draft shortened the quote. It did not hand back the same paragraph.

Why: **options when the call is taste**, and what "stylistically" means. Three approaches, not three phrasings of one; each with its cost; one recommended; and the flaw the author named was fixed in the option they chose.

### Exit check 27: a passing draft is returned unchanged

Before:

> The migration finishes Tuesday. Support will see the new export screen Wednesday morning, and the old one goes away a week later. If the rollback runs, both screens stay until we say otherwise.

After:

> Unchanged. The paragraph passes every check, so it goes back as it came.

Why: eval check 27. A pass that finds nothing is a result. Swapping a word to prove the pass happened is the failure the minimum-edit rule exists to prevent.

