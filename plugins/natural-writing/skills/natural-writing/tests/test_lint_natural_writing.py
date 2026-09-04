import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "lint_natural_writing.py"
SPEC = importlib.util.spec_from_file_location("lint_natural_writing", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ScanTests(unittest.TestCase):
    def test_flags_multiple_named_patterns(self):
        text = (
            "Here's the thing: this pivotal moment showcases our progress, "
            "underscoring its significance."
        )
        names = {finding["pattern"] for finding in MODULE.scan(text)}
        self.assertIn("throat-clearing", names)
        self.assertIn("importance-inflation", names)
        self.assertIn("superficial-interpretation", names)

    def test_one_dash_is_not_a_cluster(self):
        self.assertEqual([], MODULE.scan("One useful aside — then the point."))

    def test_two_dashes_are_a_cluster(self):
        findings = MODULE.scan("One — two — three.")
        self.assertEqual(2, len(findings))
        self.assertTrue(all(item["pattern"] == "dash-cluster" for item in findings))

    def test_plain_text_passes(self):
        self.assertEqual([], MODULE.scan("The team shipped the fix Tuesday."))

    def test_flags_validation_preamble(self):
        findings = MODULE.scan("You're absolutely right. The pilot should run for two weeks.")
        self.assertIn("validation-preamble", {item["pattern"] for item in findings})

    def test_flags_collaboration_theater(self):
        findings = MODULE.scan(
            "One thing I want to push on gently: the pricing claim lacks evidence."
        )
        self.assertIn("collaboration-theater", {item["pattern"] for item in findings})

    def test_flags_question_answer_pivot(self):
        findings = MODULE.scan("The result? A complete reset.")
        self.assertIn("question-answer-pivot", {item["pattern"] for item in findings})


    def test_flags_frequency_patterns(self):
        text = (
            "The estimate and the decision sit on one record, so a reviewer can "
            "trace it rather than rebuilding it."
        )
        names = {finding["pattern"] for finding in MODULE.scan(text)}
        self.assertIn("contrastive-definition", names)
        self.assertIn("deferred-point", names)
        self.assertIn("mechanism-speak", names)

    def test_frequency_patterns_do_not_fire_on_plain_prose(self):
        text = "The adjuster rules on cause of loss and agrees scope with the restoration firm."
        names = {finding["pattern"] for finding in MODULE.scan(text)}
        self.assertNotIn("contrastive-definition", names)
        self.assertNotIn("deferred-point", names)
        self.assertNotIn("mechanism-speak", names)

class SpecSheetCodaTests(unittest.TestCase):
    """A finished sentence followed by a verbless list of qualities."""

    def names(self, text):
        return {finding["pattern"] for finding in MODULE.scan(text)}

    def test_flags_an_attribute_list(self):
        text = (
            "The opening paragraph says what the process does. "
            "Plain language, no jargon, ready to use as it stands."
        )
        self.assertIn("spec-sheet-coda", self.names(text))

    def test_flags_a_bare_adjective_triad(self):
        text = "The scheduler coordinates the work. Fast, governed, auditable."
        self.assertIn("spec-sheet-coda", self.names(text))

    def test_leaves_a_real_sentence_alone(self):
        text = (
            "The opening paragraph says what the process does. "
            "It is written to be used word for word."
        )
        self.assertNotIn("spec-sheet-coda", self.names(text))

    def test_leaves_a_list_inside_a_sentence_alone(self):
        text = "Open one when you need the process, the systems, and the value story."
        self.assertNotIn("spec-sheet-coda", self.names(text))

class OrgChartActorTests(unittest.TestCase):
    def names(self, text):
        return {finding["pattern"] for finding in MODULE.scan(text)}

    def test_flags_a_department_with_a_human_verb(self):
        self.assertIn("org-chart-actor", self.names("When the claim closes, product quality gets the failure record."))

    def test_leaves_named_people_alone(self):
        self.assertNotIn("org-chart-actor", self.names("The product engineers get the failure record."))

    def test_leaves_functions_doing_function_things_alone(self):
        self.assertNotIn("org-chart-actor", self.names("Finance approves the write-off and posts the adjustment."))


class InsiderJargonTests(unittest.TestCase):
    def names(self, text):
        return {finding["pattern"] for finding in MODULE.scan(text)}

    def test_flags_systems_vocabulary(self):
        self.assertIn("insider-jargon", self.names("Telemetry comes in as read-only evidence of what the machine did."))

    def test_leaves_plain_descriptions_alone(self):
        self.assertNotIn("insider-jargon", self.names("The process looks at the equipment and never operates it."))


class EmDashOveruseTests(unittest.TestCase):
    def test_one_em_dash_does_not_fire(self):
        self.assertEqual([], MODULE.scan_em_dash("One useful aside — then the point, made in full."))

    def test_dense_em_dash_use_fires(self):
        text = (
            "The team shipped the fix — on time — and the customer noticed. "
            "The rollout went smoothly — better than expected — and nobody paged on-call. "
            "Support closed the ticket — quietly — and moved on to the next one."
        )
        findings = MODULE.scan_em_dash(text)
        self.assertEqual(1, len(findings))
        self.assertEqual("em-dash-overuse", findings[0]["pattern"])

    def test_plain_text_does_not_fire(self):
        self.assertEqual([], MODULE.scan_em_dash("The team shipped the fix Tuesday."))


class SentenceShapeRunTests(unittest.TestCase):
    def test_four_hedged_sentences_in_a_row_fire(self):
        text = (
            "The rollout might slip, although the team is confident. "
            "It may still land Friday, which would be a relief. "
            "The risk, arguably, is the integration test, which is flaky. "
            "Support could see a spike, since the change touches billing."
        )
        findings = MODULE.scan_sentence_shape(text)
        names = {f["pattern"] for f in findings}
        self.assertIn("sentence-shape-run", names)
        self.assertEqual("compound", findings[0]["shape"])

    def test_four_short_sentences_in_a_row_fire(self):
        text = "The fix shipped. The tests passed. Support closed the ticket. Nobody paged on-call."
        findings = MODULE.scan_sentence_shape(text)
        self.assertTrue(any(f["shape"] == "simple" for f in findings))

    def test_mixed_shapes_do_not_fire(self):
        text = (
            "The fix shipped Tuesday. It slipped a day, although the team had buffered for that. "
            "Support closed the ticket. The rollout, which touched three services, went smoothly."
        )
        self.assertEqual([], MODULE.scan_sentence_shape(text))

    def test_short_paragraph_below_threshold_does_not_fire(self):
        text = "The fix shipped. The tests passed. Support closed the ticket."
        self.assertEqual([], MODULE.scan_sentence_shape(text))


class InterfaceAsNarratorTests(unittest.TestCase):
    def names(self, text):
        return {f["pattern"] for f in MODULE.scan(text)}

    def test_flags_an_app_with_attitude(self):
        self.assertIn("interface-as-narrator", self.names("And under the brief, the app keeps score on itself."))

    def test_flags_a_map_that_admits(self):
        self.assertIn("interface-as-narrator", self.names("The useful part is that the map admits what it does not know."))

    def test_leaves_showing_and_listing_alone(self):
        self.assertNotIn("interface-as-narrator", self.names("The screen shows autonomy at 93% and lists the heaviest stage."))

    def test_leaves_a_person_doing_the_verb_alone(self):
        self.assertNotIn("interface-as-narrator", self.names("Sarah says the split has to be decided here."))


class SpokenRegisterTests(unittest.TestCase):
    def names(self, text):
        return {f["pattern"] for f in MODULE.scan(text)}

    def test_flags_circular_assertion(self):
        self.assertIn("circular-assertion", self.names("The rules the owners gave the map are these rules."))

    def test_leaves_a_real_definition_alone(self):
        self.assertNotIn("circular-assertion", self.names("The rules from the mapping are running now."))

    def test_flags_furniture_inventory(self):
        self.assertIn("furniture-inventory", self.names("And under the brief, three cards: autonomy, SLA, and the slowest stage."))

    def test_leaves_pointing_at_one_element_alone(self):
        self.assertNotIn("furniture-inventory", self.names("Look at the autonomy tile: ninety-three percent."))

    def test_flags_speaker_meta(self):
        self.assertIn("speaker-meta", self.names("Now, two different agents, and they are easy to mix up."))

    def test_leaves_plain_distinctions_alone(self):
        self.assertNotIn("speaker-meta", self.names("Two agents touched this, and they do different jobs."))


class TrailerCadenceTests(unittest.TestCase):
    def names(self, text):
        return {f["pattern"] for f in MODULE.scan(text)}

    def test_flags_one_glance_and(self):
        self.assertIn("trailer-cadence", self.names("One glance and Sarah has the case."))

    def test_flags_artifact_splitting(self):
        self.assertIn("interface-as-narrator", self.names("The recommendation splits the claim by cause."))

    def test_leaves_a_person_at_normal_speed_alone(self):
        names = self.names("Sarah opens it, and the whole case is in front of her.")
        self.assertNotIn("trailer-cadence", names)
        self.assertNotIn("interface-as-narrator", names)


class AnnouncedVirtueTests(unittest.TestCase):
    def names(self, text):
        return {f["pattern"] for f in MODULE.scan(text)}

    def test_flags_a_rating(self):
        self.assertIn("announced-virtue", self.names("This is the starting point, and it is honest."))

    def test_flags_the_useful_thing(self):
        self.assertIn("announced-virtue", self.names("Here is the map, and the useful thing about it is the gaps."))

    def test_leaves_the_evidence_alone(self):
        self.assertNotIn("announced-virtue", self.names("Seven processes are on the map, and none of them are mapped."))


class ScanSetTests(unittest.TestCase):
    """The failure this mode exists for: a pass that varies the verbs across a
    large set and leaves every piece opening on the same article, which nobody
    editing the set can see from inside any one piece."""

    def names(self, text):
        return {finding["pattern"] for finding in MODULE.scan_set(text)}

    def test_flags_a_shared_opening_article(self):
        pieces = [
            "The survey is 62% complete and every gap is marked.",
            "The rules the owners wrote are running in production now.",
            "The trail says what rerouted it and who signed off.",
            "The business changes a rule and it takes a sentence.",
            "The director opens this on a Monday and gets a ranked list.",
            "The owner answers the last open question.",
            "Three items reach the reviewer and each says why.",
            "Six months on, the worst-covered area leads the list.",
            "The agent asks only what the source cannot answer.",
            "The analysis is done, and the spec gets written.",
        ]
        self.assertIn("set-uniform-opening", self.names("\n\n".join(pieces)))

    def test_leaves_a_varied_set_alone(self):
        pieces = [
            "Whoever owns it answers the last open question.",
            "Three items reach the reviewer and each says why.",
            "Six months on, the worst-covered area leads the list.",
            "Agents ask only what the source cannot answer.",
            "Analysis is done, and the spec gets written.",
            "Same rules the owners wrote, now running in production.",
            "A rule changes, and it takes a sentence, not a project.",
            "Fifty-eight items it has not reached, listed by name.",
            "One artifact: the design, the rules, and an empty ledger.",
            "Two teams, one picture, and the gap left visible.",
        ]
        self.assertEqual(set(), self.names("\n\n".join(pieces)))

    def test_ignores_a_set_too_small_to_measure(self):
        self.assertEqual([], MODULE.scan_set("The one.\n\nThe two.\n\nThe three."))

    def test_flags_a_shared_closing_shape(self):
        pieces = ["Piece %d ends on the same note." % n for n in range(10)]
        self.assertIn("set-uniform-closing", self.names("\n\n".join(pieces)))

    def test_flags_a_connective_installed_by_the_last_pass(self):
        pieces = [
            "Approve the rule once instead of approving every claim.",
            "It routes it instead of asking a person.",
            "Say it plainly instead of reading the column.",
            "Name the owner instead of naming the system.",
            "Show the gap instead of smoothing it over.",
            "The owner answers and the boxes turn green.",
            "Three items reach the reviewer and each says why.",
            "Six months on, the worst-covered area leads the list.",
            "The agent asks what the source cannot answer.",
            "Two departments, one picture, gap left visible.",
        ]
        self.assertIn("set-uniform-connective", self.names("\n\n".join(pieces)))

    def test_does_not_measure_length(self):
        pieces = ["Word " * (8 + n % 3) for n in range(12)]
        self.assertNotIn("set-uniform-length", self.names("\n\n".join(pieces)))


class BackwardsFacingClauseTests(unittest.TestCase):
    def test_flags_built_for_exactly_that(self):
        findings = MODULE.scan("A Maestro case is built for exactly that.")
        self.assertTrue(any(f["pattern"] == "backwards-facing-clause" for f in findings))

    def test_flags_the_way_the_map_said(self):
        findings = MODULE.scan("It runs the way the map said it could.")
        self.assertTrue(any(f["pattern"] == "backwards-facing-clause" for f in findings))

    def test_leaves_a_self_standing_clause_alone(self):
        findings = MODULE.scan("A Maestro case is built for messy work.")
        self.assertFalse(any(f["pattern"] == "backwards-facing-clause" for f in findings))


class FlatDeclarativeRunTests(unittest.TestCase):
    def test_flags_three_same_length_untuned_sentences(self):
        text = ("Somebody sends the evidence. Somebody approves the containment. "
                "Somebody authorizes the outcome.")
        self.assertTrue(MODULE.scan_flat_declarative_run(text))

    def test_a_turn_breaks_the_run(self):
        text = ("Somebody sends the evidence. Somebody approves the containment, but the "
                "outcome waits. Somebody authorizes the outcome.")
        self.assertFalse(MODULE.scan_flat_declarative_run(text))

    def test_varied_lengths_are_left_alone(self):
        text = ("A warranty claim waits on people. In four of the six main stages somebody "
                "has to say yes before anything moves at all in the case. It branches.")
        self.assertFalse(MODULE.scan_flat_declarative_run(text))


class StackedPrecisionTests(unittest.TestCase):
    def test_flags_three_exact_figures_in_a_row(self):
        text = ("Thirteen stages sit here. Thirty-nine tasks sit under them. "
                "Eighty-nine rules decide the path.")
        self.assertTrue(MODULE.scan_stacked_precision(text))

    def test_audible_rounding_is_the_fix_not_the_defect(self):
        text = ("Thirteen stages sit here. Call it forty tasks under them. "
                "Close to a hundred rules decide the path.")
        self.assertFalse(MODULE.scan_stacked_precision(text))

    def test_one_figure_alone_is_ordinary(self):
        text = "Thirteen stages sit here. The rest is detail. Nobody typed any of it."
        self.assertFalse(MODULE.scan_stacked_precision(text))


class StackedPrecisionTuningTests(unittest.TestCase):
    def test_pronominal_one_is_not_a_figure(self):
        text = ("Each one carries its evidence count. Not one of them was disagreed with. "
                "The one at the top is the rule.")
        self.assertFalse(MODULE.scan_stacked_precision(text))

    def test_identifier_is_not_a_figure(self):
        text = ("The rule is SR-440. The claim is WR-2026-0417. The iteration is IMP-0005.")
        self.assertFalse(MODULE.scan_stacked_precision(text))

    def test_elapsed_time_marker_is_not_a_figure(self):
        text = ("Six months on. Three months later the queue looks different. "
                "Two weeks ago nobody had seen it.")
        self.assertFalse(MODULE.scan_stacked_precision(text))

    def test_a_real_stack_still_fires(self):
        text = ("Thirteen stages sit here. Thirty-nine tasks sit under them. "
                "Eighty-nine rules decide the path.")
        self.assertTrue(MODULE.scan_stacked_precision(text))


class FlatDeclarativeTuningTests(unittest.TestCase):
    def test_a_fragment_breaks_the_run(self):
        text = ("The map draws itself. Two departments, stitched into one flow. "
                "The gap stays drawn as a gap.")
        self.assertFalse(MODULE.scan_flat_declarative_run(text))

    def test_an_imperative_breaks_the_run(self):
        text = ("The map draws itself. And look at substitution. It is drawn as a gap.")
        self.assertFalse(MODULE.scan_flat_declarative_run(text))

    def test_a_now_contrast_breaks_the_run(self):
        text = ("That loop ran on one process. Now it is running on all of them. "
                "The feed is the same feed.")
        self.assertFalse(MODULE.scan_flat_declarative_run(text))

    def test_three_calm_declaratives_still_fire(self):
        text = ("Here is what the VP of service opens on a Monday every week. "
                "Four things are ranked by what each is worth to the business. "
                "The one at the top is an ownership decision here.")
        self.assertTrue(MODULE.scan_flat_declarative_run(text))


class SpokenChecksTests(unittest.TestCase):
    def test_compressed_mechanism_fires(self):
        text = ("Each main stage carries a clock, a warning when it is at risk and an "
                "escalation when it breaches.")
        names = {f["pattern"] for f in MODULE.scan_spoken(text)}
        self.assertIn("compressed-mechanism", names)

    def test_walked_mechanism_is_clean(self):
        text = ("Now, each main stage has an SLA, and when that SLA is at risk of being "
                "breached, it escalates to the right person automatically.")
        names = {f["pattern"] for f in MODULE.scan_spoken(text)}
        self.assertNotIn("compressed-mechanism", names)

    def test_stacked_object_pronouns_fire(self):
        names = {f["pattern"] for f in MODULE.scan_spoken("So hand it that.")}
        self.assertIn("stacked-object-pronouns", names)

    def test_named_object_is_clean(self):
        names = {f["pattern"] for f in MODULE.scan_spoken("So hand the coding agent the document.")}
        self.assertNotIn("stacked-object-pronouns", names)

    def test_paragraph_opening_on_pronoun_fires(self):
        text = "The case agent picks that up.\n\nIt checks the photos against the finding."
        names = {f["pattern"] for f in MODULE.scan_spoken(text)}
        self.assertIn("paragraph-opens-on-pronoun", names)

    def test_first_paragraph_may_open_however_it_likes(self):
        text = "It starts here.\n\nThe case agent picks that up."
        names = {f["pattern"] for f in MODULE.scan_spoken(text)}
        self.assertNotIn("paragraph-opens-on-pronoun", names)

    def test_spoken_checks_are_opt_in(self):
        # scan() must not carry them: they are wrong for written prose
        names = {f["pattern"] for f in MODULE.scan("So hand it that.")}
        self.assertNotIn("stacked-object-pronouns", names)


if __name__ == "__main__":
    unittest.main()


class NominatedSignificanceTests(unittest.TestCase):
    def test_flags_is_the_point(self):
        names = {f["pattern"] for f in MODULE.scan("Same survey as a table, and the owner column is the point.")}
        self.assertIn("nominated-significance", names)

    def test_flags_what_matters_is(self):
        names = {f["pattern"] for f in MODULE.scan("Here is what came back, and what matters is how faithful it is.")}
        self.assertIn("nominated-significance", names)

    def test_stating_the_finding_is_clean(self):
        names = {f["pattern"] for f in MODULE.scan("The same survey as a table, and work that runs every day has no owner.")}
        self.assertNotIn("nominated-significance", names)

    def test_ordinary_use_of_point_is_left_alone(self):
        names = {f["pattern"] for f in MODULE.scan("She can point at exactly which claims moved and why.")}
        self.assertNotIn("nominated-significance", names)


class InterfaceActsOnItselfTests(unittest.TestCase):
    def test_flags_the_map_seeds_itself(self):
        names = {f["pattern"] for f in MODULE.scan("Pick a few processes and the map seeds itself.")}
        self.assertIn("interface-acts-on-itself", names)

    def test_flags_a_gapped_reflexive(self):
        names = {f["pattern"] for f in MODULE.scan("The app keeps score on itself.")}
        self.assertIn("interface-acts-on-itself", names)

    def test_emphatic_itself_is_left_alone(self):
        names = {f["pattern"] for f in MODULE.scan("The frame shows the record itself.")}
        self.assertNotIn("interface-acts-on-itself", names)

    def test_naming_the_actor_is_clean(self):
        names = {f["pattern"] for f in MODULE.scan("Nobody drew this. Cartographer did.")}
        self.assertNotIn("interface-acts-on-itself", names)

    def test_a_process_may_improve_itself(self):
        names = {f["pattern"] for f in MODULE.scan("The map made the process, and the process improved itself.")}
        self.assertNotIn("interface-acts-on-itself", names)


class NarratorNoiseTests(unittest.TestCase):
    """1.13.0: the narrator rule stopped firing on ordinary English."""

    def names(self, text):
        return {f["pattern"] for f in MODULE.scan(text)}

    def test_a_report_may_say_something(self):
        self.assertNotIn("interface-as-narrator", self.names("The report says the queue is empty."))

    def test_a_bare_pronoun_is_not_an_interface(self):
        self.assertNotIn("interface-as-narrator", self.names("She told me it decides who goes first."))

    def test_attitude_still_fires(self):
        self.assertIn("interface-as-narrator", self.names("The map admits what it does not know."))


class FrequencyAggregationTests(unittest.TestCase):
    def test_below_threshold_is_silent(self):
        text = "We chose Postgres rather than MySQL. The rest of the stack is unchanged."
        self.assertEqual([], MODULE.summarize_frequency(MODULE.scan(text), text))

    def test_at_threshold_reports_one_line_with_a_count(self):
        text = ("We chose Postgres rather than MySQL.\nWe cache in Redis instead of Memcached.\n"
                "We deploy nightly rather than weekly.")
        summary = MODULE.summarize_frequency(MODULE.scan(text), text)
        self.assertEqual(1, len(summary))
        self.assertEqual("contrastive-definition", summary[0]["pattern"])
        self.assertEqual(3, summary[0]["count"])
        self.assertEqual([1, 2, 3], summary[0]["lines"])

    def test_scan_still_returns_every_match(self):
        text = "A rather than B. C instead of D."
        self.assertEqual(2, len([f for f in MODULE.scan(text) if f["pattern"] == "contrastive-definition"]))


class ProseParagraphTests(unittest.TestCase):
    def test_lists_headings_tables_and_fences_are_skipped(self):
        text = ("---\ntitle: x\n---\n\n# Heading\n\n1. one item;\n2. two items;\n3. three items.\n\n"
                "| a | b |\n|---|---|\n| c | d |\n\n```\ncode = 1\n```\n\n"
                "This paragraph is prose. It stays in.")
        kept = MODULE.prose_paragraphs(text)
        self.assertEqual(1, len(kept))
        self.assertTrue(kept[0][1].startswith("This paragraph is prose."))

    def test_blockquote_prose_is_kept_without_the_marker(self):
        kept = MODULE.prose_paragraphs("> Quoted prose here.\n> Second line.")
        self.assertEqual([(1, "Quoted prose here. Second line.")], kept)

    def test_paragraph_index_counts_the_raw_split(self):
        kept = MODULE.prose_paragraphs("# Title\n\n- item\n\nThird block is prose.")
        self.assertEqual(3, kept[0][0])

    def test_numbered_list_is_not_a_flat_declarative_run(self):
        text = "1. The first step is short.\n2. The second step is short.\n3. The third step is short."
        self.assertEqual([], MODULE.scan_flat_declarative_run(text))

    def test_line_scan_skips_fenced_code(self):
        text = "```\nhere's the thing: code\n```\nHere's the thing: prose."
        findings = [f for f in MODULE.scan(text) if f["pattern"] == "throat-clearing"]
        self.assertEqual([4], [f["line"] for f in findings])


class CandorAnnouncementTests(unittest.TestCase):
    def names(self, text):
        return {f["pattern"] for f in MODULE.scan(text)}

    def test_flags_honestly_question(self):
        self.assertIn("candor-announcement", self.names("Honestly? The pilot is not ready."))

    def test_flags_the_honest_answer(self):
        self.assertIn("candor-announcement", self.names("Two teams asked. The honest answer is that nobody owns it."))

    def test_flags_push_back(self):
        self.assertIn("candor-announcement", self.names("Here's where I'd push back: the number is stale."))

    def test_adverb_mid_sentence_is_ordinary(self):
        self.assertNotIn("candor-announcement", self.names("She honestly thought the export had shipped."))

    def test_direct_speech_about_a_person_is_ordinary(self):
        self.assertNotIn("candor-announcement", self.names("The reviewer was direct with the team."))


class InterpretiveMetadiscourseTests(unittest.TestCase):
    def names(self, text):
        return {f["pattern"] for f in MODULE.scan(text)}

    def test_as_you_can_see_is_nominated_significance(self):
        self.assertIn("nominated-significance", self.names("As you can see, the queue drains by noon."))

    def test_the_key_insight_is(self):
        self.assertIn("nominated-significance", self.names("The key insight is that nobody owns the nightly run."))

    def test_stating_the_finding_is_clean(self):
        self.assertNotIn("nominated-significance", self.names("Nobody owns the nightly run."))

    def test_emphasis_crutches_are_nominated_significance(self):
        self.assertIn("nominated-significance", self.names("Half of them have no owner. Let that sink in."))
        self.assertIn("nominated-significance", self.names("Make no mistake, the queue is growing."))

    def test_a_mistake_is_still_a_word(self):
        self.assertNotIn("nominated-significance", self.names("The team made no mistake in the rollout."))
