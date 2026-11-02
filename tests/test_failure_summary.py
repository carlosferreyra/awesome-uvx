"""Check that failure summaries remain useful even when reports are incomplete."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class FailureSummaryTests(unittest.TestCase):
    def summarize(self, kind, files, **env):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            for name, text in files.items():
                (path / name).write_text(text)
            summary = path / 'summary.md'
            result = subprocess.run(
                [sys.executable, str(ROOT / 'scripts/actions_summary.py'), kind],
                cwd=path, env=dict(os.environ, GITHUB_STEP_SUMMARY=str(summary), **env),
                capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            return summary.read_text()

    def test_catalog_failure_does_not_claim_unrun_checks_passed(self):
        text = self.summarize('catalog', {'tools.json': '{'},
                              JOB_STATUS='failure', CATALOG_STATUS='failure')
        self.assertIn('| Catalog | failure |', text)
        self.assertIn('| Regression tests | not run |', text)
        self.assertIn('counts unavailable', text)

    def test_partial_install_log_is_not_a_success(self):
        text = self.summarize('installs', {'install.log': 'Testing 3 tool(s)...'},
                              JOB_STATUS='failure', INSTALLS_STATUS='failure')
        self.assertIn('did not produce a final count', text)
        self.assertIn('| Install validation | failure |', text)

    def test_malformed_failure_report_does_not_hide_original_failure(self):
        for report in ['{', '{}', '[{}]', '[null]']:
            with self.subTest(report=report):
                text = self.summarize('installs', {'output.log': report,
                    'install.log': 'Results: 2 passed, 1 failed'}, JOB_STATUS='failure')
                self.assertIn('malformed', text)
                self.assertIn('**1 failed**', text)

    def test_failure_details_are_kept(self):
        text = self.summarize('installs', {'output.log': json.dumps([
            {'package': 'fixture', 'reason': 'network'}]),
            'install.log': 'Results: 0 passed, 1 failed'}, JOB_STATUS='failure')
        self.assertIn('`fixture`: network', text)

    def test_no_added_tools_is_explicitly_reported(self):
        text = self.summarize('installs', {'install.log': 'No new tools to test.'},
                              JOB_STATUS='success', INSTALLS_STATUS='success')
        self.assertIn('No new tools', text)


if __name__ == '__main__':
    unittest.main()
