"""The reference files are data. These tests keep them consistent.

Every catalog row (and every spoken-register row) has a worked example headed by
its exact name in the same file; every lint check maps to a row that exists; every
forward case that names a row names a real one. Derived from the files, never
hardcoded, so a rename in one place fails here instead of drifting.
"""
import importlib.util
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
CATALOG = ROOT / "references" / "pattern-catalog.md"
SPOKEN = ROOT / "references" / "spoken-register.md"
CASES = ROOT / "tests" / "cases.md"
SCRIPT = ROOT / "scripts" / "lint_natural_writing.py"

SPEC = importlib.util.spec_from_file_location("lint_natural_writing", SCRIPT)
LINT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(LINT)

ROW = re.compile(r"^\| ([A-Z][^|]+?) \|", re.M)
EXAMPLE_HEADING = re.compile(r"^### (.+)$", re.M)
SECTION_NAMES = {"Editing a set"}  # sections that carry checks but are not table rows


def rows(path: Path) -> list[str]:
    return [m.group(1).strip() for m in ROW.finditer(path.read_text()) if m.group(1).strip() != "Pattern"]


def example_headings(path: Path) -> list[str]:
    return [m.group(1).strip() for m in EXAMPLE_HEADING.finditer(path.read_text())]


def known_rows() -> set[str]:
    return set(rows(CATALOG)) | set(rows(SPOKEN)) | SECTION_NAMES


def names_in(heading: str, known: set[str] | None = None) -> set[str]:
    """Row names a heading refers to, matched by containment so that row names
    which themselves contain " and " ("Dash and parenthesis dependency") are
    not split apart. Longest names are matched first and removed."""
    known = known if known is not None else known_rows()
    head = heading.split(":")[0]
    head = re.sub(r"\s*\([^)]*\)$", "", head)
    found = set()
    for name in sorted(known, key=len, reverse=True):
        if name in head:
            found.add(name)
            head = head.replace(name, " ")
    leftover = re.sub(r"[\s,]+|\band\b", " ", head).strip()
    if leftover:
        found.add(leftover)  # an unknown name surfaces as a finding in the tests
    return found


class EveryRowHasAnExample(unittest.TestCase):
    def check(self, path):
        covered = set().union(*(names_in(h) for h in example_headings(path)))
        missing = [r for r in rows(path) if r not in covered]
        self.assertEqual([], missing, f"{path.name}: rows without an example: {missing}")

    def test_catalog(self):
        self.check(CATALOG)

    def test_spoken_register(self):
        self.check(SPOKEN)

    def test_no_duplicate_row_names(self):
        all_rows = rows(CATALOG) + rows(SPOKEN)
        dupes = {r for r in all_rows if all_rows.count(r) > 1}
        self.assertEqual(set(), dupes)

    def test_every_example_heading_names_a_row(self):
        known = known_rows()
        for path in (CATALOG, SPOKEN):
            for h in example_headings(path):
                if h.startswith(("Diagnose mode", "Exit check", "Offer options")):
                    continue  # workflow examples name a SKILL.md or eval section
                unknown = names_in(h, known) - known
                self.assertEqual(set(), unknown, f"{path.name}: example heading names no row: {h}")


class LintChecksMapToRows(unittest.TestCase):
    def test_every_mapped_row_exists(self):
        known = set(rows(CATALOG)) | set(rows(SPOKEN)) | SECTION_NAMES
        missing = {k: v for k, v in LINT.ROW_FOR.items() if v not in known}
        self.assertEqual({}, missing)

    def test_every_check_is_mapped(self):
        names = set(LINT.PATTERNS) | set(LINT.SPOKEN_PATTERNS) | {
            "em-dash-overuse", "sentence-shape-run", "flat-declarative-run", "stacked-precision",
            "paragraph-opens-on-pronoun", "set-uniform-opening", "set-uniform-closing", "set-uniform-connective",
        }
        self.assertEqual(set(), names - set(LINT.ROW_FOR), "lint checks with no catalog row")

    def test_linted_rows_say_so(self):
        """A row whose check exists should carry a **Linted:** marker or be the
        documented partial case, so the reader knows a machine looks for it."""
        text = CATALOG.read_text() + SPOKEN.read_text()
        for check, row in LINT.ROW_FOR.items():
            if row in SECTION_NAMES or row in ("Clause-shape monotony", "Em dash default", "Telegraphic speech", "Interface as narrator"):
                continue  # documented in prose rather than a marker
            line = next((l for l in text.splitlines() if l.startswith(f"| {row} |")), None)
            self.assertIsNotNone(line, row)
            self.assertTrue("**Linted:**" in line or "**Partly linted" in line, f"{row} has check {check} but no Linted marker")


class ForwardCasesNameRealRows(unittest.TestCase):
    def test_case_headings(self):
        known = known_rows()
        for m in re.finditer(r"^## (\d+)\. (.+)$", CASES.read_text(), re.M):
            n, title = int(m.group(1)), m.group(2)
            if n <= 22 or title.startswith(("Eval check", "Exit check", "Offer options", "Ask before")):
                continue  # legacy behavioural cases and workflow cases keep their titles
            unknown = names_in(title, known) - known
            self.assertEqual(set(), unknown, f"case {n} names no row: {title}")


if __name__ == "__main__":
    unittest.main()
