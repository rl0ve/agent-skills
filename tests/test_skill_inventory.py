from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest

from test_packages import ROOT, load_module


SCRIPT = ROOT / 'plugins/work-router/skills/deduplicate-skills/scripts/inventory_skills.py'
audit = load_module('skill_inventory', SCRIPT)


class SkillInventoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def skill(self, path, name='shared', resource=None):
        path.mkdir(parents=True)
        (path / 'SKILL.md').write_text(f'---\nname: {name}\ndescription: A bounded test skill\n---\nDo the task.\n')
        if resource is not None:
            (path / 'helper.py').write_text(resource)
        return path

    def run_inventory(self, root=None, **kwargs):
        return audit.inventory([{'label': 'fixture', 'path': str(root or self.root)}], **kwargs)

    def test_identical_entrypoints_do_not_hide_resource_differences(self):
        self.skill(self.root / 'a', resource='print(1)')
        self.skill(self.root / 'b', resource='print(2)')
        kinds = {g['kind'] for g in self.run_inventory()['groups']}
        self.assertIn('same-entrypoint', kinds)
        self.assertIn('same-name', kinds)
        self.assertNotIn('same-local-bundle', kinds)

    def test_identical_complete_bundles_are_copy_candidates(self):
        self.skill(self.root / 'a', resource='print(1)')
        self.skill(self.root / 'b', resource='print(1)')
        self.assertIn('same-local-bundle', {g['kind'] for g in self.run_inventory()['groups']})

    def test_windows_line_endings_preserve_skill_identity(self):
        skill = self.skill(self.root / 'folder-name', name='declared-name')
        p = skill / 'SKILL.md'
        p.write_bytes(p.read_bytes().replace(b'\n', b'\r\n'))
        report = self.run_inventory()
        self.assertEqual(report['skills'][0]['name'], 'declared-name')
        self.assertFalse(report['warnings'])

    def test_alias_and_cycle_do_not_become_independent_copies(self):
        self.skill(self.root / 'a')
        (self.root / 'alias').symlink_to(self.root / 'a', target_is_directory=True)
        (self.root / 'cycle').symlink_to(self.root, target_is_directory=True)
        report = self.run_inventory()
        self.assertEqual(len(report['skills']), 2)
        self.assertEqual({g['kind'] for g in report['groups']}, {'path-alias'})
        self.assertTrue(any('cycle' in w for w in report['warnings']))

    def test_incomplete_fingerprints_cannot_prove_copy_equality(self):
        for name in ['a', 'b']:
            skill = self.skill(self.root / name)
            (skill / 'large.bin').write_bytes(b'x' * (audit.MAX_FILE_BYTES + 1))
        report = self.run_inventory()
        self.assertTrue(all(r['bundle_sha256'] is None for r in report['skills']))
        self.assertNotIn('same-local-bundle', {g['kind'] for g in report['groups']})

    def test_disabled_path_is_separate_from_other_same_name(self):
        a = self.skill(self.root / 'a')
        self.skill(self.root / 'b')
        report = self.run_inventory(disabled=[{'path': str(a / 'SKILL.md'), 'enabled': False}])
        self.assertEqual([r['activity'] for r in report['skills']],
                         ['disabled-in-inventory', 'candidate-not-session-verified'])

    def test_plugin_uses_listed_version_not_newest_cache(self):
        for version in ['1.0', '99.0']:
            package = self.root / 'plugins/cache/market/tool' / version
            self.skill(package / 'skills/example', name=version)
        snapshot = {'installed': [{'pluginId': 'tool@market', 'version': '1.0',
                                   'installed': True, 'enabled': False}]}
        warnings = []
        report = audit.inventory(audit.plugin_roots(snapshot, self.root, warnings))
        self.assertEqual([r['name'] for r in report['skills']], ['1.0'])
        self.assertEqual(report['skills'][0]['activity'], 'disabled-in-inventory')
        self.assertFalse(warnings)

    def test_unknown_plugin_material_and_missing_root_report_coverage_gap(self):
        warnings = []
        roots = audit.plugin_roots({'installed': [{'pluginId': 'missing@market', 'version': '1',
                                                   'installed': True}]}, self.root, warnings)
        self.assertEqual(roots, [])
        report = self.run_inventory(self.root / 'absent', warnings=warnings)
        self.assertEqual(report['skills'], [])
        self.assertEqual(len(report['warnings']), 2)

    def test_cli_preserves_inputs_and_refuses_to_overwrite_output(self):
        skill = self.skill(self.root / 'skills/a', resource='print(1)')
        before = {p: p.read_bytes() for p in skill.iterdir()}
        output = self.root / 'report.json'
        cmd = [sys.executable, str(SCRIPT), '--root', f'fixture={skill.parent}', '--output', str(output)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(json.loads(output.read_text())['skills']), 1)
        self.assertEqual(output.stat().st_mode & 0o777, 0o600)
        saved = output.read_bytes()
        self.assertNotEqual(subprocess.run(cmd, capture_output=True).returncode, 0)
        self.assertEqual(output.read_bytes(), saved)
        self.assertEqual(before, {p: p.read_bytes() for p in skill.iterdir()})


if __name__ == '__main__':
    unittest.main()
