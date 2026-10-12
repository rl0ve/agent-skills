"""Checks for the 1.19.0 3D route split: skill shape, local links/anchors, installer scope."""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UI = ROOT / "plugins" / "ui-router"
SKILLS = UI / "skills"
LINK = re.compile(r"\]\(([^)\s]+)\)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)


def slug(text: str) -> str:
    text = re.sub(r"[`*_]", "", text.strip().lower())
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors(path: Path) -> set[str]:
    return {slug(h[1]) for h in HEADING.findall(path.read_text(encoding="utf-8"))}


def markdown_files() -> list[Path]:
    # Every Markdown file in the repo, so a pointer moved between READMEs, docs and
    # skills cannot dangle (the 1.9.0 Work Router README pointer did).
    return [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]


class Route3DTests(unittest.TestCase):
    def test_route_3d_skill_has_frontmatter_and_is_short(self):
        text = (SKILLS / "route-3d-work" / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\nname: route-3d-work\ndescription: "))
        self.assertLessEqual(len(text.split()), 900)

    def test_local_links_and_anchors_resolve(self):
        broken = []
        for md in markdown_files():
            for target in LINK.findall(md.read_text(encoding="utf-8")):
                if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                    continue
                file_part, _, anchor = target.partition("#")
                dest = (md.parent / file_part).resolve()
                if not dest.exists():
                    broken.append(f"{md.relative_to(ROOT)} -> {target}")
                elif anchor and dest.suffix == ".md" and anchor not in anchors(dest):
                    broken.append(f"{md.relative_to(ROOT)} -> {target} (anchor)")
        self.assertEqual(broken, [])

    def test_moved_references_keep_redirect_stubs(self):
        refs = SKILLS / "route-ui-work" / "references"
        for name in ("interactive-worlds.md", "spatial-realism.md", "interaction-contracts.md"):
            self.assertIn("route-3d-work", (refs / name).read_text(encoding="utf-8"))
        self.assertIn("fidelity-execution-gate", anchors(refs / "upstream-skills.md"))

    def test_multi_skill_packs_install_named_skills_only(self):
        catalog = json.loads(
            (SKILLS / "route-ui-work" / "references" / "optional-skills.json").read_text(encoding="utf-8")
        )
        items = {s["key"]: s for s in catalog["skills"]}
        self.assertEqual(
            items["claudedesignskills"]["skills"],
            ["gsap-scrolltrigger", "threejs-webgl", "blender-web-pipeline"],
        )
        self.assertNotIn("awwwards-3d", catalog["profiles"]["creative"])
        for key in catalog["profiles"]["3d"]:
            self.assertTrue(items[key].get("skills"), key)

    def test_codex_installer_copies_both_routers(self):
        script = (UI / "scripts" / "install-into-codex-skills.sh").read_text(encoding="utf-8")
        self.assertIn("skill_names=(route-ui-work route-3d-work)", script)


if __name__ == "__main__":
    unittest.main()
