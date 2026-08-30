"""Exercise macOS release workflow failure propagation without Apple services."""
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def workflow(name):
    return (ROOT / '.github/workflows' / name).read_text()


def step_script(source, name):
    step = source.split(f'      - name: {name}\n', 1)[1].split('\n      - name:', 1)[0]
    script = step.split('        run: |\n', 1)[1]
    return '\n'.join(line[10:] for line in script.splitlines()) + '\n'


class MacOSWorkflowTests(unittest.TestCase):
    def test_complete_isolated_suite_and_failure_propagation(self):
        script = step_script(workflow('openclaw-macos-validate.yml'), 'Swift test')
        # A failed build, failed profile, or timed-out profile must never upload
        # successful validation proof or proceed to later test profiles.
        for failed_phase, exit_code, expected in [
            ('', 0, ['build', 'default', 'named']),
            ('build', 1, ['build']),
            ('default', 124, ['build', 'default']),
            ('named', 1, ['build', 'default', 'named']),
        ]:
            with self.subTest(failed_phase=failed_phase), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                stub = '#!/usr/bin/env python3\n' + (
                    'import json,os,sys\n'
                    'phase="build" if sys.argv[0].endswith("swift") else sys.argv[2]\n'
                    'with open(os.environ["CALLS"],"a") as f: f.write(json.dumps({"phase":phase,"args":sys.argv[1:]})+"\\n")\n'
                    'sys.exit(int(os.environ["FAIL_CODE"]) if phase==os.environ["FAIL_PHASE"] else 0)\n'
                )
                for binary in ['swift', 'node']:
                    path = root / binary
                    path.write_text(stub)
                    path.chmod(0o755)
                env = dict(os.environ, PATH=f'{root}:{os.environ["PATH"]}',
                           CALLS=str(root / 'calls'), FAIL_PHASE=failed_phase, FAIL_CODE=str(exit_code))
                result = subprocess.run(['bash', '-c', script], env=env, capture_output=True, text=True)
                self.assertEqual(result.returncode, exit_code, result.stderr)
                calls = [json.loads(line) for line in (root / 'calls').read_text().splitlines()]
                self.assertEqual([call['phase'] for call in calls], expected)
                for call in calls[1:]:
                    self.assertEqual(call['args'][0], 'scripts/test-macos-native.mts')
                    self.assertIn('--skip-build', call['args'])
                    self.assertIn('--no-parallel', call['args'])
                if len(calls) == 3:
                    self.assertEqual(calls[1]['args'][-2:], ['--skip', 'AppStateIsolationTests'])
                    self.assertEqual(calls[2]['args'][-2:], ['--filter', 'AppStateIsolationTests'])

    def test_preparation_needs_tag_but_release_page_only_for_promotion(self):
        publish = workflow('openclaw-macos-publish.yml')
        validate = workflow('openclaw-macos-validate.yml')
        build, promote = publish.split('  promote_release_artifacts:', 1)
        for preparation in [build, validate]:
            self.assertNotIn('gh release view', preparation)
            clone = step_script(preparation, 'Clone selected public source')
            self.assertIn('git -C source rev-parse --verify "refs/tags/${RELEASE_TAG}^{commit}"', clone)
        self.assertIn('gh release view', promote)
        self.assertIn('environment: mac-release', build)
        self.assertIn('environment: mac-release', promote)
        self.assertIn('if: ${{ !inputs.preflight_only && !inputs.smoke_test_only }}', promote)


if __name__ == '__main__':
    unittest.main()
