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
        self.assertIn("superficial-analysis", names)

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


if __name__ == "__main__":
    unittest.main()
