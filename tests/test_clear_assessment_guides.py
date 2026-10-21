import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "plugins" / "clear-assessment-guides" / "skills" / "clear-assessment-guides"


class ClearAssessmentGuidesTests(unittest.TestCase):
    def test_template_evidence_kinds_match_documentation(self):
        template = (SKILL / "assets" / "review-template.html").read_text()
        kinds = re.search(r"const evidenceKinds = \[(.*?)\];", template).group(1)
        kinds = [k.strip().strip("'") for k in kinds.split(",")]
        doc = " ".join((SKILL / "references" / "issue-format.md").read_text().split())
        self.assertIn("`kind` (" + ", ".join(kinds[:-1]) + " or " + kinds[-1] + ")", doc)

    def test_before_after_boundary_remains_explicit(self):
        hub = " ".join((SKILL / "SKILL.md").read_text().split())
        for phrase in ("use Visual Version Review", "matched pair", "a crop cannot show relative prominence",
                       "missing access is not proof of absence"):
            self.assertIn(phrase, hub)


if __name__ == "__main__":
    unittest.main()
