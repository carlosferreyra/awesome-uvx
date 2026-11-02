"""Keep partial registry failures from being published as a successful sync."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('latest_release', ROOT / 'scripts/latest_release.py')
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class ReleaseFailureTests(unittest.TestCase):
    def test_partial_fetch_preserves_failed_metadata_and_returns_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'tools.json'
            old = {'version': '1.0', 'last_release': '2025-01-01'}
            path.write_text(json.dumps({'categories': [{'tools': {
                'ok': dict(old), 'unavailable': dict(old), 'no-date': dict(old),
                'ignored': dict(old, pypi=False)}}]}))
            def fetch(name):
                return {'ok': ('2.0', '2026-10-01'), 'unavailable': None,
                        'no-date': ('2.0', None)}[name]
            with patch.object(release, 'TOOLS_JSON', path), patch.object(
                    release, 'fetch_latest', side_effect=fetch):
                self.assertEqual(release.main(), 1)
            tools = json.loads(path.read_text())['categories'][0]['tools']
            self.assertEqual(tools['unavailable'], old)
            self.assertEqual(tools['ok']['version'], '2.0')
            self.assertEqual(tools['no-date']['last_release'], old['last_release'])
            self.assertEqual(tools['ignored'], dict(old, pypi=False))

    def test_registry_permission_failure_is_not_a_valid_release(self):
        with patch.object(release.httpx, 'get', side_effect=release.httpx.HTTPStatusError(
                '403 Forbidden', request=release.httpx.Request('GET', 'https://pypi.org'),
                response=release.httpx.Response(403))):
            self.assertIsNone(release.fetch_latest('fixture'))


if __name__ == '__main__':
    unittest.main()
