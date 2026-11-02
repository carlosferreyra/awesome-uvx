"""Exercise failure propagation through the actual validation shell pipelines."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def step_body(file, name):
    text = (ROOT / '.github/workflows' / file).read_text()
    step = text.split('      - name: ' + name + '\n', 1)[1].split('\n      - name:', 1)[0]
    command = step.split('        run: ', 1)[1]
    if not command.startswith('|\n'):
        return command.strip()
    return '\n'.join(line[10:] for line in command[2:].splitlines())


class WorkflowShellTests(unittest.TestCase):
    def test_validation_failures_survive_log_capture(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            for name in ['uv', 'bun', 'cargo', 'python3', 'git']:
                binary = path / name
                binary.write_text('#!/bin/sh\necho "fixture permission denied" >&2\nexit 17\n')
                binary.chmod(0o755)
            env = dict(os.environ, PATH=str(path) + os.pathsep + os.environ['PATH'],
                       GITHUB_EVENT_NAME='pull_request', PR_BASE='fixture', MANUAL_BASE='')
            for file, name in [('ci.yml', 'Validate catalog'),
                               ('ci.yml', 'Test maintenance scripts'),
                               ('ci.yml', 'Check README freshness'),
                               ('validate_installs.yml', 'Test tool installations')]:
                with self.subTest(file=file, step=name):
                    result = subprocess.run(['bash', '-eo', 'pipefail', '-c', step_body(file, name)],
                                            cwd=path, env=env, capture_output=True, text=True)
                    self.assertEqual(result.returncode, 17, result.stdout + result.stderr)
                    self.assertIn('permission denied', result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
