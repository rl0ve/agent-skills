from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'plugins/work-router/skills/route-ai-work/scripts/sync_agent_profiles.py'
SOURCE = SCRIPT.parent.parent / 'assets/agent-profiles/luna-builder.toml'


class AgentProfileSyncTests(unittest.TestCase):
    def run_sync(self, destination, apply=False):
        args = [sys.executable, str(SCRIPT), '--destination', str(destination),
                '--profile', 'luna-builder']
        if apply:
            args.append('--apply')
        return subprocess.run(args, check=True, capture_output=True, text=True).stdout

    def test_existing_backups_migrate_even_with_current_profile(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / 'agents'
            old = dest / 'backups/old/luna-builder.toml'
            old.parent.mkdir(parents=True)
            old.write_bytes(SOURCE.read_bytes())
            active = dest / SOURCE.name
            active.write_bytes(SOURCE.read_bytes())
            self.assertIn('relocate', self.run_sync(dest))
            self.assertTrue(old.exists())
            self.assertFalse(dest.with_name('agents-backups').exists())
            self.run_sync(dest, True)
            self.assertFalse((dest / 'backups').exists())
            self.assertEqual(list(dest.rglob('*.toml')), [active])
            saved = list(dest.with_name('agents-backups').rglob('*.toml'))
            self.assertEqual(len(saved), 1)
            self.assertEqual(saved[0].read_bytes(), SOURCE.read_bytes())
            self.assertIn('0 profile operation', self.run_sync(dest))

    def test_update_preserves_previous_profile_outside_discovery(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / 'agents'
            dest.mkdir()
            active = dest / SOURCE.name
            active.write_text('old content')
            unrelated = dest / 'unrelated.toml'
            unrelated.write_text('unrelated')
            self.run_sync(dest, True)
            self.assertEqual(active.read_bytes(), SOURCE.read_bytes())
            self.assertEqual(unrelated.read_text(), 'unrelated')
            saved = list(dest.with_name('agents-backups').rglob('*.toml'))
            self.assertEqual(len(saved), 1)
            self.assertEqual(saved[0].read_text(), 'old content')
            self.assertFalse((dest / 'backups').exists())


if __name__ == '__main__':
    unittest.main()
