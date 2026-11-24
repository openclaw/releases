"""Execute CI's real artifact consumer against immutable upload receipts."""
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = (ROOT / '.github/workflows/ci.yml').read_text()
STEP = WORKFLOW.split('      - name: Download and verify uploaded proof\n', 1)[1]
SCRIPT = '\n'.join(line[10:] for line in STEP.split('        run: |\n', 1)[1].splitlines())


class ArtifactProofTests(unittest.TestCase):
    def run_proof(self, entries=None, digest=None, artifact_id='12345', api_exit=0):
        archive = io.BytesIO()
        with zipfile.ZipFile(archive, 'w') as z:
            for name, content in entries or [('proof.txt', b'release action round-trip proof\n')]:
                z.writestr(name, content)
        data = archive.getvalue()
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / 'artifact.zip').write_bytes(data)
            # No inventory exists in this fixture. Only the exact upload ID can
            # be downloaded, even when a name/list discovery would be empty.
            (root / 'gh').write_text(f'#!{sys.executable}\n' + '''import json, os, pathlib, sys
args = sys.argv[1:]
with open('calls.jsonl', 'a') as calls:
    calls.write(json.dumps(args) + '\\n')
assert args == ['api', 'repos/fixture/releases/actions/artifacts/12345/zip']
assert os.environ['GH_TOKEN'] == 'synthetic-read-token'
if int(os.environ['API_EXIT']):
    sys.exit(int(os.environ['API_EXIT']))
sys.stdout.buffer.write(pathlib.Path('artifact.zip').read_bytes())
''')
            (root / 'gh').chmod(0o755)
            # Render the real workflow env wiring, not a parallel test contract.
            context = {'github.token': 'synthetic-read-token',
                       'steps.proof.outputs.artifact-id': artifact_id,
                       'steps.proof.outputs.artifact-digest': digest if digest is not None else hashlib.sha256(data).hexdigest()}
            env = {key: re.sub(r'\$\{\{ (.*?) \}\}', lambda m: context[m[1]], value)
                   for key, value in re.findall(r'^          ([A-Z_]+): (.*)$', STEP.split('        run:', 1)[0], re.M)}
            result = subprocess.run(['bash', '-e', '-c', SCRIPT], cwd=root,
                                    env=dict(os.environ, **env, GITHUB_REPOSITORY='fixture/releases',
                                             PATH=f'{root}{os.pathsep}{os.environ["PATH"]}', API_EXIT=str(api_exit)),
                                    capture_output=True, text=True, timeout=10)
            calls = [json.loads(line) for line in (root / 'calls.jsonl').read_text().splitlines()] if (root / 'calls.jsonl').exists() else []
            return result, calls

    def test_direct_upload_receipt_succeeds_without_inventory(self):
        result, calls = self.run_proof()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(calls, [['api', 'repos/fixture/releases/actions/artifacts/12345/zip']])
        self.assertIn('Cache and artifact round trips passed.', result.stdout)

    def test_invalid_upload_outputs_fail_before_download(self):
        for changes in [{'artifact_id': ''}, {'artifact_id': '../12345'}, {'artifact_id': '0'},
                        {'digest': ''}, {'digest': 'not-a-hash'}]:
            with self.subTest(changes=changes):
                result, calls = self.run_proof(**changes)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(calls, [])

    def test_api_failure_is_not_retried_or_accepted(self):
        result, calls = self.run_proof(api_exit=1)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(len(calls), 1)
        self.assertNotIn('round trips passed', result.stdout)

    def test_mismatched_archive_digest_is_rejected(self):
        result, _ = self.run_proof(digest='0' * 64)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('differs from the uploaded artifact digest', result.stderr)

    def test_wrong_or_extra_content_is_rejected_even_with_matching_digest(self):
        for entries in [[('proof.txt', b'wrong')], [('other.txt', b'release action round-trip proof\n')],
                        [('proof.txt', b'release action round-trip proof\n'), ('extra', b'')]]:
            with self.subTest(entries=entries):
                result, _ = self.run_proof(entries=entries)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('round-trip content differs', result.stderr)
