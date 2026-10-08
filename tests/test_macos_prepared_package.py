"""Reject prepared release packages whose identity or bytes changed."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location(
    'prepared_package', Path(__file__).resolve().parents[1] / 'scripts/prepare-macos-package.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PreparedPackageTests(unittest.TestCase):
    def test_frozen_identity_and_hashes(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            payload = b'exact prepared release bytes'
            (root / 'openclaw-2026.9.9.tgz').write_bytes(payload)
            bundle = {
                'schema': 'openclaw.npm-package-bundle/v1', 'releaseTag': 'v2026.9.9',
                'releaseSha': 'a' * 40, 'packageName': 'openclaw', 'packageVersion': '2026.9.9',
                'tarballName': 'openclaw-2026.9.9.tgz',
                'tarballSha256': hashlib.sha256(payload).hexdigest(), 'corePackageTarballs': [],
                'producer': {'repository': 'openclaw/openclaw', 'runId': '123', 'runAttempt': '1',
                             'workflowSha': 'a' * 40,
                             'producerWorkflowPath': '.github/workflows/openclaw-npm-preflight.yml'},
            }
            manifest = root / 'package-bundle.json'
            manifest.write_text(json.dumps(bundle))
            run = {'id': 123, 'run_attempt': 1}
            self.assertEqual(len(module.verify_bundle(root, run, 'v2026.9.9', 'a' * 40)), 1)
            for tag, sha, producer in [('v2026.9.8', 'a' * 40, run),
                                       ('v2026.9.9', 'b' * 40, run),
                                       ('v2026.9.9', 'a' * 40, {'id': 123, 'run_attempt': 2})]:
                with self.subTest(tag=tag, sha=sha, producer=producer), self.assertRaises(ValueError):
                    module.verify_bundle(root, producer, tag, sha)
            (root / bundle['tarballName']).write_bytes(b'changed package')
            with self.assertRaisesRegex(ValueError, 'hash mismatch'):
                module.verify_bundle(root, run, 'v2026.9.9', 'a' * 40)
