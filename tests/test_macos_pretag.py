"""Exercise pretag source admission with real Git and synthetic GitHub metadata."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
GIT = shutil.which('git')


class PretagSourceTests(unittest.TestCase):
    def test_admits_only_matching_signed_canonical_source_before_checkout(self):
        cases = [({}, True), ({'signature': False}, False), ({'reason': 'unsigned'}, False),
                 ({'api_sha': 'a' * 40}, False), ({'api_failure': True}, False),
                 ({'version': '2026.9.2'}, False), ({'name': 'other'}, False),
                 ({'tag_other': True}, False), ({'tag_same': True}, True),
                 ({'branch_advanced': True}, False), ({'sha': 'a' * 40}, False),
                 ({'sha': 'main'}, False), ({'workflow': 'refs/heads/feature'}, False),
                 ({'preflight': 'false'}, False), ({'smoke': 'true'}, False),
                 ({'source_ref': 'main'}, False), ({'resume': '123'}, False),
                 ({'branch': 'main'}, False), ({'tag': 'v2026.9.3-beta.1'}, False)]
        for changes, accepted in cases:
            with self.subTest(changes=changes), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                repo = root / 'remote'
                repo.mkdir()
                def git(*args):
                    return subprocess.check_output([GIT, '-C', str(repo), *args], text=True,
                                                   stderr=subprocess.DEVNULL).strip()
                git('init', '-b', 'release/2026.9.3')
                git('config', 'user.name', 'Fixture')
                git('config', 'user.email', 'fixture@example.invalid')
                git('config', 'commit.gpgsign', 'false')
                (repo / 'package.json').write_text(json.dumps({
                    'name': changes.get('name', 'openclaw'), 'version': changes.get('version', '2026.9.3')}))
                # This marker must never become checked-out source before admission succeeds.
                (repo / 'source-marker').write_text('synthetic source')
                git('add', '.')
                git('commit', '-m', 'fixture')
                sha = git('rev-parse', 'HEAD')
                if changes.get('tag_same'):
                    git('tag', 'v2026.9.3')
                if changes.get('branch_advanced') or changes.get('tag_other'):
                    git('commit', '--allow-empty', '-m', 'later source')
                    if changes.get('tag_other'):
                        git('tag', 'v2026.9.3')
                        git('checkout', '-B', 'release/2026.9.3', sha)
                bin_dir = root / 'bin'
                bin_dir.mkdir()
                shim = bin_dir / 'git'
                shim.write_text('''#!/usr/bin/env python3
import os, subprocess, sys
args = sys.argv[1:]
args = [os.environ['FIXTURE_REPO'] if a == 'https://github.com/openclaw/openclaw.git' else a for a in args]
sys.exit(subprocess.call([os.environ['REAL_GIT'], *args]))
''')
                shim.chmod(0o755)
                gh = bin_dir / 'gh'
                gh.write_text('''#!/usr/bin/env python3
import os, sys
if os.environ['API_FAILURE'] == 'true': sys.exit(1)
print(os.environ['COMMIT_JSON'])
''')
                gh.chmod(0o755)
                commit = {'sha': changes.get('api_sha', sha), 'commit': {'verification': {
                    'verified': changes.get('signature', True), 'reason': changes.get('reason', 'valid')}}}
                env = dict(os.environ, PATH=f'{bin_dir}:{os.environ["PATH"]}', REAL_GIT=GIT,
                           FIXTURE_REPO=str(repo), COMMIT_JSON=json.dumps(commit),
                           API_FAILURE=str(changes.get('api_failure', False)).lower(),
                           PRETAG_SOURCE_SHA=changes.get('sha', sha), RELEASE_TAG=changes.get('tag', 'v2026.9.3'),
                           PUBLIC_RELEASE_BRANCH=changes.get('branch', 'release/2026.9.3'),
                           WORKFLOW_REF=changes.get('workflow', 'refs/heads/main'),
                           PREFLIGHT_ONLY=changes.get('preflight', 'true'),
                           SMOKE_TEST_ONLY=changes.get('smoke', 'false'),
                           SOURCE_REF=changes.get('source_ref', ''), RESUME_RUN_ID=changes.get('resume', ''))
                result = subprocess.run(['python3', str(ROOT / 'scripts/checkout-macos-pretag.py')],
                                        cwd=root, env=env, capture_output=True, text=True)
                self.assertEqual(result.returncode == 0, accepted, result.stderr)
                self.assertEqual((root / 'source/source-marker').exists(), accepted)
                if accepted:
                    actual = subprocess.check_output([GIT, '-C', str(root / 'source'), 'rev-parse', 'HEAD'], text=True).strip()
                    self.assertEqual(actual, sha)


if __name__ == '__main__':
    unittest.main()
