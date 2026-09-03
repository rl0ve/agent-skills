# Examples

These examples model the decision, not phrases to reuse. Each one shows the before, the after, and why; where the obvious edit is the wrong one, it shows that too. The catalog row names the pattern and the repair in a line; come here when the line is not enough to see the move.

Every fact in an "after" is present in its "before." That is the constraint that makes the examples testable, and it is the constraint the skill works under.

## Cut importance framing, keep the fact

Before:

> The launch represents a transformative milestone, underscoring our commitment to an ever-evolving customer landscape.

After:

> This is our first release that lets customers export their own audit history.

Why: the available fact carries the significance. If “first release” or the export feature were not in the source, the editor must not invent them.

## Keep uncertainty that belongs to the author

Before:

> I think the migration is probably safe, but the retry behavior still makes me nervous.

Bad edit:

> The migration is safe, although retry behavior remains a concern.

Better edit:

> I think the migration is safe. The retry behavior still makes me nervous.

Why: the hedge and emotion are part of the claim and the voice.

## Replace vague authority

Before:

> Industry experts agree that the new workflow significantly improves productivity.

After when no source exists:

> The draft does not provide evidence for the productivity claim.

Why: a natural rewrite cannot manufacture a source or result.

## Prefer a real mechanism

Before:

> The dashboard streamlines collaboration and empowers teams to move faster.

After:

> The dashboard puts review comments, owners, and due dates on one screen.

Why: use this repair only when those features appear in the source.

## Preserve technical repetition

Before:

> The worker reads the queue. The assistant validates each item before the tool writes it.

After:

> The worker reads the queue, validates each item, and then writes it.

Why: one stable term is clearer than three decorative synonyms.

## Diagnose without pretending to detect authorship

Text:

> Here's what nobody tells you: great onboarding isn't just documentation. It's a journey that empowers every user.

Report:

- **Manufactured insight:** “Here's what nobody tells you” claims exclusivity without evidence. Start with the onboarding claim.
- **Binary template:** “isn't just documentation” delays the actual comparison. Name what onboarding includes.
- **Abstract praise:** “journey that empowers every user” gives no mechanism or outcome. Add supported specifics or cut it.

## Default to a typed dash

Before:

> The rollout went smoothly — better than expected — and nobody paged on-call.

After:

> The rollout went smoothly, better than expected, and nobody paged on-call.

Why: neither aside earns an em dash. Commas carry both without loss. Keep the em dash only for the rare case where a comma or parenthesis would blur the break the writer intends.

## Break a run of the same sentence shape

Before:

> The migration might slip, although the team is confident. It may still land Friday, which would be a relief. The risk, arguably, is the integration test, which is flaky. Support could see a spike, since the change touches billing.

After:

> The migration might slip, although the team is confident. It may still land Friday. The integration test is the risk - it is flaky. A billing change like this one can spike support tickets.

Why: four hedged, subordinate-clause sentences in a row read as one long qualification instead of four separate points. Recasting two of them as direct statements lets the real hedges (“might,” “may still”) carry their own weight.

## Keep a deliberate fragment

Before:

> We had one hour left. No backup. And the customer was already in the room.

After:

> We had one hour left. No backup. The customer was already in the room.

Why: the fragment creates pressure and fits the story. Remove only the decorative conjunction.

## Lead with the point, then the condition

Before:

> Because the estimate and the approval now sit on one record, the reviewer no longer has to rebuild the file from three systems, so the claim closes on the day it is approved.

After:

> The claim closes on the day it is approved. The reviewer sees the estimate and the approval together and no longer rebuilds the file from three systems.

Why: **deferred point** and **mechanism-speak** together. The reader wanted the consequence; the sentence made them wait through where the data lives to get it. The mechanism survives, one sentence later, said as what a person now sees.

## Say what it is, not what it is not

Before:

> This is not a dashboard. Instead of charts, it is a queue of decisions rather than a picture of the work.

After:

> It is a queue of decisions. Each row is one thing a person has to approve, reject, or send back.

Why: **contrastive definition** three times in two sentences, and no positive statement until the third clause. The second "after" sentence is drawn from what a queue of decisions is, not invented; if the source had not said what a row holds, the edit would stop after the first sentence.

## Cut the spec-sheet coda

Before:

> The summary goes to the adjuster the moment the site visit ends. Plain language, no jargon, ready to use as it stands.

After:

> The summary goes to the adjuster the moment the site visit ends, written so they can forward it to the customer without editing it.

Why: **spec-sheet coda**. Three verbless qualities read as a product blurb. One of them, turned into a consequence for the reader, does the work of all three. "Forward it without editing" is what "ready to use" meant; no new claim.

## Name the people, not the department

Before:

> Product quality gets the failure record and learns which supplier batch caused it. Compliance hears about it the same afternoon.

After:

> The product engineers get the failure record and can see which supplier batch caused it. The compliance officer is told the same afternoon.

Why: **org-chart actor**. A function can own or approve; it cannot hear or learn. The reader pictures nobody until a person appears. "Engineers" and "officer" are the roles the source named for those functions; do not invent a title the source does not have.

## Say what happens in the reader's world

Before:

> The process has read-only access to the equipment and acts as the system of record for every human-in-the-loop decision.

After:

> The process looks at the equipment and never operates it. Every decision a person makes is kept, with who made it and when.

Why: **insider jargon**. "Read-only," "system of record," and "human-in-the-loop" describe the system to its builders. The reader is a plant manager; each term becomes what they would see. Keep the terms if the audience owns them.

## Give the screen's verb back to a person

Before:

> The app keeps score on itself. The map admits what it does not know, and each one says who owns it.

After:

> The app shows its own accuracy, month by month. Where the map has no data, it shows a gap rather than a guess, and every process on it names an owner.

Why: **interface as narrator**. Screens show, list and mark; they do not admit or keep score. The tell is attitude. The after says what is on screen. "Month by month" and "names an owner" were in the source's surrounding text; the edit borrows from the piece, not from imagination.

## Cut the rating, keep the evidence

Before:

> The ledger is empty when the map is published, and it is honest about that. The useful thing about it is what it admits.

After:

> The ledger is empty when the map is published. Every entry that appears afterwards was made by a person, with their reason attached.

Why: **announced virtue**. "It is honest" and "the useful thing about it" rate the subject. The second sentence of the after is the evidence the rating was standing in for; it was in the source. If it had not been, the rating was the only claim and the paragraph had nothing to say.

## Deliver the finding instead of nominating it

Before:

> Look at the owner column. That is the point. What matters is how many of these run every day.

After:

> Half of these processes run every day, and none of them has an owner.

Why: **nominated significance**. "That is the point" and "what matters is" tell the reader something matters without saying what. The after states the finding. It sounds less confident and says more. If the finding cannot be stated, the sentence has nothing to nominate.

## Let each clause stand on its own

Before:

> The team built the intake form for exactly that. It runs the way the map said it could, in a week where nothing made them wait.

After:

> The team built the intake form to catch a missing policy number before the claim is filed. It went live in a week, and no approval was pending on it at any point.

Why: **backwards-facing clause**. "Exactly that," "the way the map said it could," and "where nothing made them wait" each point at an earlier sentence the reader must hold in memory. The after names the subject in the sentence that needs it. In speech this is the difference between following and losing the thread. The specifics ("missing policy number," "no approval pending") come from the source paragraph.

## Walk a mechanism through when it will be said aloud

Before (a talk track):

> Each main stage carries a clock, a warning when it is at risk and an escalation when it breaches. Thirteen stages, thirty-nine tasks, eighty-nine rules. Recurrence confirmed, gates closure.

After:

> Now, each main stage has an SLA, and when that SLA is at risk of being breached, Maestro Case escalates it to the right person automatically. There are thirteen stages in this case and, call it, ninety rules behind them. And this line here, **recurrence confirmed**, is the one that stops the case closing until somebody has ruled on whether it will happen again.

Why: three spoken-only patterns in three sentences. **Telegraphic speech**: the first sentence is a spec line nobody can say at speed; the after is longer on purpose and uses the product's own word, SLA. **Stacked precision**: three exact figures in a row cannot be heard; the point rests on thirteen, so that stays exact and eighty-nine is rounded audibly. **Label read cold**: "recurrence confirmed, gates closure" is a screen cell; the after says what it means and who acts on it. Applied to written prose, every one of these edits would be wrong. See [spoken-register.md](spoken-register.md).

## Measure what the fix installed

A set of forty one-line captions each opened with a verb, and the note said to vary them. The pass varied the verbs. The linter's `--set` mode then reported that sixteen of forty now opened on "The", and twelve ended on the same two-word shape, "at once."

The second pass fixed what the first one installed: openings moved to the subject, the actor, or the number the caption rests on, and the closing shape was allowed to vary with the point being made.

Why: **Editing a set**. A standard applied across many items becomes the next pattern, and the writer of the set is the last person able to see it. Measure after every pass, not only after the first.

## Offer approaches, not rewordings

The author asked for a stronger opening paragraph on a memo. Correctness had one answer; the opening had several. The response offered three, each stating the same facts:

- Lead with the decision the reader must make by Friday. Trades away the context a first-time reader needs.
- Lead with the one number that changed since the last memo. Trades away breadth; the reader may think the memo is only about that number.
- Lead with the customer's own words from the escalation. Trades away neutrality; it frames the memo as a response rather than a plan.

The recommendation was the first, because the reader was a single decision-maker who already knew the context. The author chose the third "stylistically" and asked for the quote to be shorter. The next draft shortened the quote. It did not hand back the same paragraph.

Why: **options when the call is taste**, and what "stylistically" means. Three approaches, not three phrasings of one; each with its cost; one recommended; and the flaw the author named was fixed in the option they chose.

## Return a draft that already passes

Before:

> The migration finishes Tuesday. Support will see the new export screen Wednesday morning, and the old one goes away a week later. If the rollback runs, both screens stay until we say otherwise.

After:

> Unchanged. The paragraph passes every check: facts intact, actors named, no framing, the ending on the last useful fact.

Why: eval check 27. A pass that finds nothing is a result. Swapping a word to prove the pass happened is the failure the minimum-edit rule exists to prevent.

## State both facts instead of staging a contrast

Before:

> The new pipeline isn't just faster — it's cheaper. And it's not about the tooling. It's about trust.

After:

> The new pipeline runs in forty minutes instead of three hours and costs a third as much per run. The team trusts it because every run leaves a log they can read.

Why: **binary template** and **correction-first argument**, the most complained-about shape in every 2026 survey of AI prose. "Not X but Y" fakes an insight by rejecting a claim nobody made. The after states both facts and gives the trust claim its mechanism. Every number is from the source; if the source had none, the after would say "faster and cheaper" and stop.

## Keep the number of items the subject has

Before:

> The rollout was fast, simple, and effective. Teams saw fewer tickets, quicker approvals, and happier customers.

After:

> The rollout took two weeks. Support tickets about approvals fell by half in the first month.

Why: **forced completeness**. Two triplets in two sentences, six qualities, one fact. The source had two facts, so the after has two. One adjective with proof beats three without.

## Keep the one qualifier that matches the evidence

Before:

> The change could potentially reduce onboarding time somewhat, and it may possibly be worth noting that some teams might see a benefit.

After:

> The change should reduce onboarding time. Two of the five pilot teams saw it.

Why: **qualification pileup**. Six hedges cover one tentative claim and hide the evidence that would let the reader judge it. The after keeps one qualifier ("should") and gives the number the hedging was standing in for. If the pilot count were not in the source, the after would end after the first sentence.

## Turn the bold-term list back into prose

Before:

> - **Speed:** The new parser is faster.
> - **Reliability:** It fails less often.
> - **Cost:** It runs on smaller machines.

After:

> The new parser is faster, fails less often, and runs on smaller machines, so the batch that used to need the large instance now runs on the standard one.

Why: **decorative emphasis** and **list reflex**. Three bullets with bold labels present three thin sentences as a framework. They belong together, so they are one sentence, and the consequence at the end is the reason the reader cared. Keep bullets for sequence or comparison.

## Cut the announcement of candor

Before:

> Honestly? The honest answer is that the pilot is not ready. Here's where I'd push back: the vendor's number is six months old.

After:

> The pilot is not ready. The vendor's number is six months old.

Why: **candor announcement**. Three phrases announce frankness before any frank thing is said, and the reader now wonders what the rest of the memo was. The two facts carry the bluntness by themselves.

## Name the relation

Before:

> The foundation is associated with the university and has been linked to several regional hospitals.

After:

> The university founded the foundation in 1998, and it funds three regional hospitals.

Why: **vague connection**. "Associated with" and "linked to" refuse to say what the relation is when the source says it. If the source only said "associated," the vagueness is the source's and must stay.

## Cut the intensifiers and see what is left

Before:

> This is genuinely hard. The teams really do struggle with it, and it truly matters that we actually fix it this quarter.

After:

> Three of the five teams missed the deadline because of it. The fix is scheduled for this quarter.

Why: **intensifier padding**. Four intensifiers promise a sincerity the sentences never earn; strip them and the before says almost nothing. The after replaces the promise with the evidence the source had. The skill does not ban adverbs; one "genuinely" in a paragraph is a word.

## Use the quantity the evidence supports

Before:

> Everyone skips the onboarding video. Nobody reads the manual, and teams always find out the hard way.

After:

> Most of the teams we asked skipped the onboarding video, and four of the six had not opened the manual.

Why: **universal quantifier**. "Everyone," "nobody" and "always" are claims about every case. The source was a survey of six teams, so the after says so. If the source supported the universal, it would stay.

## Let the paragraph end where the content ends

Before:

> The rota has two people on it and one of them is on leave until March. Coverage is a fiction.
>
> The alerts route to a channel with forty members and no owner. Everyone is responsible, so nobody is.
>
> The runbook was last edited in 2023. Documentation is where good intentions go to die.

After:

> The rota has two people on it and one of them is on leave until March. The alerts route to a channel with forty members and no owner, and the runbook was last edited in 2023, so the person who picks up the page has nothing current to work from.

Why: **quotable closer**. Three paragraphs each land on a line built to be lifted out, and by the third the reader hears it coming. The facts belong together; the after keeps them and ends on the consequence for the person paged. Keep one closer when it earns its place.
