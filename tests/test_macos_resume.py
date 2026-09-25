"""Exercise checkpoint discovery with exact GitHub API fixtures and no network."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SHA = 'a' * 40
TAG = 'v2026.8.2'
VARIANTS = ['universal', 'arm64', 'x86_64']
API = 'repos/openclaw/releases/actions/'


def listing(variant):
    return f'{API}artifacts?name=macos-resume-{TAG}-{variant}-{SHA}&per_page=100'


class MacOSResumeTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / 'source/scripts').mkdir(parents=True)
        (self.root / 'source/scripts/package-mac-dist.sh').write_text('--checkpoint-only) ;;\n')
        git = self.root / 'git'
        git.write_text(f'#!/bin/sh\n[ "$*" = "-C source rev-parse HEAD" ] || exit 1\necho {SHA}\n')
        git.chmod(0o755)
        gh = self.root / 'gh'
        gh.write_text('''#!/usr/bin/env python3
import io, json, os, sys, zipfile
with open(os.environ['CALLS'], 'a') as calls:
    calls.write(json.dumps(sys.argv[1:]) + '\\n')
assert sys.argv[1] == 'api' and len(sys.argv) == 3
with open(os.environ['FIXTURE']) as fixture:
    result = json.load(fixture)[sys.argv[2]]
if 'error' in result:
    sys.exit(result['error'])
if 'zip' in result:
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w') as archive:
        for name, value in result['zip'].items():
            archive.writestr(name, json.dumps(value))
    sys.stdout.buffer.write(output.getvalue())
elif 'raw' in result:
    sys.stdout.write(result['raw'])
else:
    print(json.dumps(result))
''')
        gh.chmod(0o755)
        self.fixture = {listing(v): dict(total_count=0, artifacts=[]) for v in VARIANTS}
        self.env = dict(os.environ, PATH=f'{self.root}:{os.environ["PATH"]}',
                        FIXTURE=str(self.root / 'fixture.json'), CALLS=str(self.root / 'calls'),
                        GITHUB_REPOSITORY='openclaw/releases', GITHUB_OUTPUT=str(self.root / 'output'),
                        RELEASE_TAG=TAG, RESUME_RUN_ID='', RESUME_RUN_ATTEMPT='', RESUME_VARIANT='universal',
                        IGNORE_CHECKPOINTS='false', PREFLIGHT_ONLY='true', SMOKE_TEST_ONLY='false',
                        PRETAG_SOURCE_SHA='', WORKFLOW_REF='refs/heads/main')

    def candidate(self, variant='universal', run_id=123, artifact_id=10, created='2026-09-23T12:00:00Z',
                  prefix='macos-notarization', run_changes=None, index_changes=None, artifact_changes=None):
        suffix = '' if variant == 'universal' else f'-{variant}'
        checkpoint = f'{prefix}-{TAG}{suffix}-{run_id}-2'
        paths = [f'{API}runs/{run_id}', f'{API}artifacts/{artifact_id}/zip',
                 f'{API}runs/{run_id}/artifacts?name={checkpoint}']
        artifact = dict(id=artifact_id, expired=False, created_at=created,
                        workflow_run=dict(id=run_id, head_branch='main'))
        artifacts = self.fixture[listing(variant)]['artifacts']
        artifacts.append(artifact | (artifact_changes or {}))
        self.fixture[listing(variant)]['total_count'] = len(artifacts)
        self.fixture[paths[0]] = dict(id=run_id, path='.github/workflows/openclaw-macos-publish.yml',
                                    event='workflow_dispatch', head_branch='main', status='completed',
                                    conclusion='failure') | (run_changes or {})
        self.fixture[paths[1]] = {'zip': {'resume.json': dict(
            schemaVersion=1, releaseTag=TAG, variant=variant, sourceSha=SHA, checkpointArtifact=checkpoint,
            artifactPrefix=prefix, producerRunId=run_id, producerRunAttempt=2,
            producerWorkflowSha='b' * 40) | (index_changes or {})}}
        self.fixture[paths[2]] = dict(artifacts=[dict(name=checkpoint, expired=False)])
        return paths

    def execute(self, changes=None, accepted=True):
        (self.root / 'fixture.json').write_text(json.dumps(self.fixture))
        for filename in ['output', 'calls']:
            (self.root / filename).unlink(missing_ok=True)
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/resume-macos-checkpoints.py')],
                                cwd=self.root, env=self.env | (changes or {}), capture_output=True, text=True)
        self.assertEqual(result.returncode == 0, accepted, result.stderr)
        calls = self.root / 'calls'
        self.calls = [json.loads(line) for line in calls.read_text().splitlines()] if calls.exists() else []
        self.stdout = result.stdout
        if not accepted:
            self.assertFalse((self.root / 'output').exists())
            return
        values = dict(line.split('=', 1) for line in (self.root / 'output').read_text().splitlines())
        self.assertEqual(values['sha'], SHA)
        self.assertEqual(values['supported'], 'true')
        plan = json.loads(values['resume_plan'])
        fresh = json.loads(values['build_matrix'])['include']
        self.assertEqual([v['variant'] for v in fresh], [v for v in VARIANTS if v not in plan])
        self.assertEqual(values['build_needed'], str(bool(fresh)).lower())
        expected = []
        for variant in VARIANTS:
            suffix = '' if variant == 'universal' else f'-{variant}'
            expected.append(dict(variant=variant, build_archs='all' if variant == 'universal' else variant,
                                 artifact_suffix=suffix, appcast_name=f'appcast{suffix}.xml',
                                 feed_url=f'https://raw.githubusercontent.com/openclaw/openclaw/main/appcast{suffix}.xml'))
        self.assertEqual(json.loads(values['package_matrix']), {'include': expected})
        return plan

    def assert_calls(self, paths):
        self.assertEqual(self.calls, [['api', path] for path in paths])

    def test_newest_failed_checkpoint_selected_independently_for_every_variant(self):
        expected, calls = {}, []
        for number, variant in enumerate(VARIANTS):
            self.candidate(variant, run_id=100 + number, artifact_id=number, created='2026-09-22T12:00:00Z')
            paths = self.candidate(variant, run_id=200 + number, artifact_id=10 + number)
            expected[variant] = dict(runId=str(200 + number), attempt='2', prefix='macos-notarization')
            calls.extend([listing(variant), *paths])
        self.assertEqual(self.execute(), expected)
        self.assert_calls(calls)
        for variant, data in expected.items():
            suffix = '' if variant == 'universal' else f'-{variant}'
            self.assertIn(f'Resuming {variant} from run {data["runId"]} attempt 2 '
                          f'(macos-notarization-{TAG}{suffix}-{data["runId"]}-2)', self.stdout)

    def test_ineligible_newer_producer_is_skipped_for_older_valid_checkpoint(self):
        older = self.candidate(created='2026-09-22T12:00:00Z')
        for changes in [dict(conclusion='success'), dict(status='in_progress'), dict(head_branch='feature'),
                        dict(path='another.yml'), dict(event='push'), dict(conclusion='timed_out')]:
            with self.subTest(changes=changes):
                self.fixture[listing('universal')]['artifacts'] = self.fixture[listing('universal')]['artifacts'][:1]
                newer = self.candidate(run_id=456, artifact_id=11, run_changes=changes)
                self.assertEqual(self.execute(), {'universal': dict(runId='123', attempt='2', prefix='macos-notarization')})
                self.assert_calls([listing('universal'), newer[0], *older, listing('arm64'), listing('x86_64')])

    def test_cancelled_producer_and_signed_checkpoint_are_resumable(self):
        paths = self.candidate(prefix='macos-signed', run_changes=dict(conclusion='cancelled'))
        self.assertEqual(self.execute(), {'universal': dict(runId='123', attempt='2', prefix='macos-signed')})
        self.assert_calls([listing('universal'), *paths, listing('arm64'), listing('x86_64')])

    def test_expired_or_non_main_index_is_skipped_without_download(self):
        self.candidate()
        artifact = self.fixture[listing('universal')]['artifacts'][0]
        for changes in [dict(expired=True), dict(workflow_run=dict(id=123, head_branch='feature'))]:
            with self.subTest(changes=changes):
                self.fixture[listing('universal')]['artifacts'] = [artifact | changes]
                self.assertEqual(self.execute(), {})
                self.assert_calls([listing(v) for v in VARIANTS])
                self.assertIn(f'Building universal: no resumable checkpoint for {TAG} at {SHA}', self.stdout)

    def test_missing_expired_or_wrong_checkpoint_is_skipped(self):
        paths = self.candidate()
        checkpoint = self.fixture[paths[-1]]['artifacts'][0]
        for artifacts in [[], [checkpoint | dict(expired=True)], [checkpoint | dict(name='wrong')]]:
            with self.subTest(artifacts=artifacts):
                self.fixture[paths[-1]] = dict(artifacts=artifacts)
                self.assertEqual(self.execute(), {})
                self.assert_calls([listing('universal'), *paths, listing('arm64'), listing('x86_64')])

    def test_index_binding_mismatches_are_skipped(self):
        paths = self.candidate()
        original = self.fixture[paths[1]]['zip']['resume.json']
        for changes in [dict(sourceSha='c' * 40), dict(schemaVersion=2), dict(schemaVersion=True),
                        dict(releaseTag='v2026.8.1'), dict(variant='arm64'), dict(producerRunId=456),
                        dict(producerRunAttempt=0), dict(producerRunAttempt='2'),
                        dict(artifactPrefix='other'), dict(checkpointArtifact='macos-notarization-*')]:
            with self.subTest(changes=changes):
                self.fixture[paths[1]] = {'zip': {'resume.json': original | changes}}
                self.assertEqual(self.execute(), {})
                self.assert_calls([listing('universal'), *paths[:2], listing('arm64'), listing('x86_64')])

    def test_unreadable_or_malformed_index_is_skipped(self):
        paths = self.candidate()
        for archive in [{'raw': 'invalid zip'}, {'zip': {}}, {'zip': {'resume.json': None}},
                        {'zip': {'resume.json': 'invalid schema'}}]:
            with self.subTest(archive=archive):
                self.fixture[paths[1]] = archive
                self.assertEqual(self.execute(), {})
                self.assert_calls([listing('universal'), *paths[:2], listing('arm64'), listing('x86_64')])

    def test_explicit_selector_pins_one_variant_and_discovers_the_others(self):
        universal = self.candidate()
        arm64 = self.candidate('arm64', run_id=456, artifact_id=11)
        self.candidate('x86_64', run_id=789, artifact_id=12)
        expected = {v: dict(runId=run_id, attempt=attempt, prefix='macos-notarization')
                    for v, run_id, attempt in [('universal', '123', '2'), ('arm64', '456', '2'), ('x86_64', '999', '4')]}
        self.assertEqual(self.execute(dict(RESUME_RUN_ID='999', RESUME_RUN_ATTEMPT='4', RESUME_VARIANT='x86_64')), expected)
        self.assert_calls([listing('universal'), *universal, listing('arm64'), *arm64])

    def test_discovery_gates_force_fresh_builds_without_api_calls(self):
        self.candidate()
        for changes in [dict(IGNORE_CHECKPOINTS='true'), dict(SMOKE_TEST_ONLY='true'),
                        dict(PRETAG_SOURCE_SHA=SHA), dict(WORKFLOW_REF='refs/heads/feature'),
                        dict(PREFLIGHT_ONLY='false')]:
            with self.subTest(changes=changes):
                self.assertEqual(self.execute(changes), {})
                self.assert_calls([])

    def test_explicit_selectors_are_preserved_when_discovery_is_disabled(self):
        self.assertEqual(self.execute(dict(IGNORE_CHECKPOINTS='true', RESUME_RUN_ID='999',
                                           RESUME_RUN_ATTEMPT='4', RESUME_VARIANT='all')),
                         {v: dict(runId='999', attempt='4', prefix='macos-notarization') for v in VARIANTS})
        self.assert_calls([])

    def test_every_github_failure_is_fatal_without_fresh_build_outputs(self):
        paths = [listing('universal'), *self.candidate()]
        for index, path in enumerate(paths):
            with self.subTest(path=path):
                original = self.fixture[path]
                self.fixture[path] = dict(error=1)
                self.execute(accepted=False)
                self.assert_calls(paths[:index + 1])
                self.fixture[path] = original


if __name__ == '__main__':
    unittest.main()
