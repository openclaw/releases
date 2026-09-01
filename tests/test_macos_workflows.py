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
    def test_notarization_recovery_requires_main_signed_preflight_and_exact_attempt(self):
        script = step_script(workflow('openclaw-macos-publish.yml'), 'Validate notarization recovery inputs')
        valid = dict(RESUME_RUN_ID='123', RESUME_RUN_ATTEMPT='2', PREFLIGHT_ONLY='true',
                     SMOKE_TEST_ONLY='false', WORKFLOW_REF='refs/heads/main')
        for changes, accepted in [({}, True), ({'RESUME_RUN_ID': ''}, False),
                                  ({'RESUME_RUN_ATTEMPT': ''}, False),
                                  ({'RESUME_RUN_ATTEMPT': '0'}, False),
                                  ({'RESUME_RUN_ID': '../123'}, False),
                                  ({'PREFLIGHT_ONLY': 'false'}, False),
                                  ({'SMOKE_TEST_ONLY': 'true'}, False),
                                  ({'WORKFLOW_REF': 'refs/heads/feature'}, False),
                                  ({'RESUME_RUN_ID': '', 'RESUME_RUN_ATTEMPT': ''}, True)]:
            with self.subTest(changes=changes):
                result = subprocess.run(['bash', '-c', script], env=dict(os.environ, **(valid | changes)),
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode == 0, accepted, result.stderr)

    def test_recovery_rejects_wrong_workflow_attempt_or_successful_producer(self):
        script = step_script(workflow('openclaw-macos-publish.yml'), 'Verify notarization checkpoint producer')
        producer = dict(id=123, run_attempt=2, path='.github/workflows/openclaw-macos-publish.yml',
                        head_branch='main', head_sha='a' * 40, event='workflow_dispatch',
                        status='completed', conclusion='failure', repository={'full_name': 'openclaw/releases'})
        for changes, accepted in [({}, True), ({'conclusion': 'cancelled'}, True),
                                  ({'conclusion': 'success'}, False), ({'run_attempt': 1}, False),
                                  ({'head_branch': 'feature'}, False), ({'path': 'untrusted.yml'}, False),
                                  ({'repository': {'full_name': 'other/releases'}}, False),
                                  ({'status': 'in_progress'}, False), ({'id': 456}, False),
                                  ({'event': 'pull_request'}, False)]:
            with self.subTest(changes=changes), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                gh = root / 'gh'
                gh.write_text('#!/usr/bin/env python3\nimport os\nprint(os.environ["PRODUCER"])\n')
                gh.chmod(0o755)
                env = dict(os.environ, PATH=f'{root}:{os.environ["PATH"]}', RUNNER_TEMP=td,
                           GITHUB_REPOSITORY='openclaw/releases', RESUME_RUN_ID='123',
                           RESUME_RUN_ATTEMPT='2', PRODUCER=json.dumps(producer | changes))
                result = subprocess.run(['bash', '-c', script], env=env, capture_output=True, text=True)
                self.assertEqual(result.returncode == 0, accepted, result.stderr)

    def test_recovery_calls_resume_without_reentering_build_steps(self):
        publish = workflow('openclaw-macos-publish.yml')
        script = step_script(publish, 'Build, sign, notarize, and package macOS release')
        for run_id, expected in [('', []), ('123', ['--resume-notarization'])]:
            with self.subTest(run_id=run_id), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                (root / 'scripts').mkdir()
                package = root / 'scripts/package-mac-dist.sh'
                package.write_text('#!/usr/bin/env python3\nimport json,sys\nprint(json.dumps(sys.argv[1:]))\n')
                package.chmod(0o755)
                result = subprocess.run(['bash', '-c', script], cwd=root,
                                        env=dict(os.environ, RESUME_RUN_ID=run_id), capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(json.loads(result.stdout), expected)
        # Job scheduling is itself the contract: a resume must never install or compile.
        for name in ['Checkout submodules (retry)', 'Setup pnpm', 'Install dependencies',
                     'Cache SwiftPM', 'Release packaging guards', 'Build',
                     'Build Control UI if missing', 'Validate release tag and package metadata', 'Verify release contents']:
            step = publish.split(f'      - name: {name}\n', 1)[1].split('\n      - name:', 1)[0]
            self.assertIn("if: ${{ inputs.resume_notarization_run_id == '' }}", step)
        self.assertIn('environment: mac-release', publish.split('  build_sign_and_package:', 1)[1])

    def test_checkpoint_binding_fails_before_packager_for_wrong_release_or_source(self):
        script = step_script(workflow('openclaw-macos-publish.yml'), 'Verify notarization checkpoint release binding')
        source_sha = 'b' * 40
        producer = dict(id=123, run_attempt=2, head_sha='a' * 40)
        envelope = dict(releaseTag='v2026.8.2', sourceSha=source_sha, producerRunId=123,
                        producerRunAttempt=2, producerWorkflowSha='a' * 40,
                        preflightOnly=True, smokeTestOnly=False)
        manifest = dict(schemaVersion=1, sourceSha=source_sha, version='2026.8.2',
                        skipDmg=False, skipDsym=False)
        cases = [({}, {}, True), ({'releaseTag': 'v2026.8.1'}, {}, False),
                 ({'producerRunAttempt': 1}, {}, False), ({'producerWorkflowSha': 'c' * 40}, {}, False),
                 ({'smokeTestOnly': True}, {}, False), ({}, {'sourceSha': 'c' * 40}, False),
                 ({}, {'version': '2026.8.1'}, False), ({}, {'skipDmg': True}, False)]
        for envelope_changes, manifest_changes, accepted in cases:
            with self.subTest(envelope=envelope_changes, manifest=manifest_changes), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                (root / 'scripts/lib').mkdir(parents=True)
                (root / 'scripts/package-mac-dist.sh').write_text('# --resume-notarization\n')
                (root / 'scripts/lib/mac-notarization-recovery.py').write_text('import pathlib\npathlib.Path("verified").touch()\n')
                (root / 'package.json').write_text(json.dumps({'version': '2026.8.2'}))
                checkpoint = root / 'dist/macos-notarization-recovery'
                checkpoint.mkdir(parents=True)
                (checkpoint / 'workflow-release.json').write_text(json.dumps(envelope | envelope_changes))
                (checkpoint / 'manifest.json').write_text(json.dumps(manifest | manifest_changes))
                (root / 'notarization-producer.json').write_text(json.dumps(producer))
                git = root / 'git'
                git.write_text(f'#!/bin/sh\nif [ "$1" = rev-parse ]; then echo {source_sha}; fi\n')
                git.chmod(0o755)
                result = subprocess.run(['bash', '-c', script], cwd=root,
                                        env=dict(os.environ, PATH=f'{root}:{os.environ["PATH"]}',
                                                 RUNNER_TEMP=td, RELEASE_TAG='v2026.8.2',
                                                 PUBLIC_RELEASE_BRANCH='release/2026.8.2'),
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode == 0, accepted, result.stderr)
                self.assertEqual((root / 'verified').exists(), accepted)

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
