"""Run the actual promotion workflow shell against an isolated registry fixture."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = (ROOT / '.github/workflows/openclaw-npm-dist-tags.yml').read_text()
JOB = WORKFLOW.split('\n  promote_extended_stable:\n', 1)[1]
STEPS = ('Validate extended-stable promotion request',
         'Verify extended-stable promotion target exists',
         'Promote and verify extended-stable npm tag')


def script(name, job=JOB):
    step = job.split(f'      - name: {name}\n', 1)[1].split('\n      - name:', 1)[0]
    return '\n'.join(line[10:] for line in step.split('        run: |\n', 1)[1].splitlines())


FAKE_NPM = r'''#!/usr/bin/env python3
import json, os, pathlib, sys
state_path = pathlib.Path('state.json')
state = json.loads(state_path.read_text())
a = sys.argv[1:]
with open('calls', 'a') as f:
    f.write(json.dumps(a) + '\n')
if a[0] == 'whoami' or a[:2] == ['dist-tag', 'add']:
    config = pathlib.Path(os.environ['NPM_CONFIG_USERCONFIG'])
    assert config.stat().st_mode & 0o777 == 0o600
    assert config.read_text() == '//registry.npmjs.org/:_authToken=fixture-token\n'
    assert os.environ['NPM_CONFIG_REGISTRY'] == 'https://registry.npmjs.org/'
    assert 'NODE_AUTH_TOKEN' not in os.environ
    pathlib.Path('config-path').write_text(str(config))
if a == ['whoami']:
    print('fixture-user')
elif a[0] == 'view' and a[2] == 'version':
    if state.get('missing_version'):
        sys.exit(1)
    version = state.get('version_response', os.environ['RELEASE_VERSION'])
    print(json.dumps([version] if state.get('array') else version))
elif a[0] == 'view' and a[1:3] == ['openclaw', 'dist-tags']:
    if state.get('written') and state.get('read_errors', 0):
        state['read_errors'] -= 1
        state_path.write_text(json.dumps(state))
        sys.exit(1)
    tags = state['tags'].copy()
    if state.get('written') and (state.get('never_converge') or state.get('stale', 0)):
        tags['extended-stable'] = '2026.7.33'
        state['stale'] = max(0, state.get('stale', 0) - 1)
        state_path.write_text(json.dumps(state))
    print(json.dumps([tags] if state.get('array') else tags))
elif a[:2] == ['dist-tag', 'add'] and a[3] == 'extended-stable':
    assert a[2].startswith('openclaw@')
    state['tags']['extended-stable'] = a[2].split('@')[1]
    state['written'] = True
    state_path.write_text(json.dumps(state))
    if state.get('write_error'):
        sys.exit(1)  # An unsuccessful response can still follow a successful write.
else:
    raise AssertionError('unexpected npm operation: ' + repr(a))
'''


class ExtendedStablePromotionTests(unittest.TestCase):
    def run_workflow(self, tag='v2026.6.35', ref='refs/heads/main', token='fixture-token', **changes):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            bin_dir = root / 'bin'
            bin_dir.mkdir()
            state = dict(tags={'latest': '2026.9.4', 'beta': '2026.9.5-beta.1',
                               'alpha': '2026.9.5-alpha.1', 'extended-stable': '2026.7.33'})
            state.update(changes)
            (root / 'state.json').write_text(json.dumps(state))
            stubs = {'npm': FAKE_NPM, 'sleep': '#!/bin/sh\nexit 0\n',
                     'git': '#!/bin/sh\n[ "$1" = ls-remote ] || exit 2\n'
                            '[ "$2" = --exit-code ] || exit 2\n'
                            '[ "$3" = --refs ] || exit 2\n'
                            '[ "$4" = https://github.com/openclaw/openclaw.git ] || exit 2\n'
                            '[ "$5" = "refs/tags/$RELEASE_TAG" ] || exit 2\n'
                            'test "$MISSING_GIT_TAG" != 1\n'}
            for name, body in stubs.items():
                (bin_dir / name).write_text(body)
                (bin_dir / name).chmod(0o755)
            env = dict(os.environ, PATH=str(bin_dir) + os.pathsep + os.environ['PATH'],
                       WORKFLOW_REF=ref, RELEASE_TAG=tag, OPENCLAW_REPOSITORY='openclaw/openclaw',
                       GITHUB_ENV=str(root / 'github-env'), GITHUB_STEP_SUMMARY=str(root / 'summary'),
                       MISSING_GIT_TAG='1' if changes.get('missing_git_tag') else '0')
            env.pop('NODE_AUTH_TOKEN', None)
            env.pop('NPM_CONFIG_USERCONFIG', None)
            for step in STEPS:
                if step == STEPS[-1]:
                    env['NODE_AUTH_TOKEN'] = token
                result = subprocess.run(['bash', '-c', script(step)], cwd=root, env=env,
                                        capture_output=True, text=True, timeout=30)
                if result.returncode:
                    break
                if (root / 'github-env').exists():
                    for line in (root / 'github-env').read_text().splitlines():
                        key, value = line.split('=', 1)
                        env[key] = value
            calls = [json.loads(line) for line in (root / 'calls').read_text().splitlines()] if (root / 'calls').exists() else []
            if (root / 'config-path').exists():
                self.assertFalse(Path((root / 'config-path').read_text()).exists(), 'npm credentials not cleaned up')
            return (result, json.loads((root / 'state.json').read_text()), calls,
                    (root / 'summary').read_text() if (root / 'summary').exists() else '')

    def test_rollback_and_forward_retag_only_write_extended_stable(self):
        for tag in ('v2026.6.35', 'v2026.8.33', 'v2026.8.34', 'v2026.8.100'):
            for array in (False, True):
                with self.subTest(tag=tag, array=array):
                    result, state, calls, summary = self.run_workflow(tag, array=array, stale=2, read_errors=1)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(state['tags'], {'latest': '2026.9.4', 'beta': '2026.9.5-beta.1',
                                                    'alpha': '2026.9.5-alpha.1', 'extended-stable': tag[1:]})
                    writes = [a for a in calls if a[0] != 'view' and a[0] != 'whoami']
                    self.assertEqual(writes, [['dist-tag', 'add', 'openclaw@' + tag[1:], 'extended-stable']])
                    self.assertIn('Result: verified', summary)
                    self.assertIn('2026.7.33', summary)

    def test_noop_does_not_write(self):
        result, _, calls, _ = self.run_workflow('v2026.7.33')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(any(a[0] == 'dist-tag' for a in calls))

    def test_ref_and_tag_admission(self):
        cases = [('v2026.6.35', 'refs/heads/feature'), ('v2026.6.35', 'refs/tags/main')]
        cases += [(tag, 'refs/heads/main') for tag in ('', 'latest', '2026.6.35', 'v2026.6.35-beta.1',
                                                       'v2026.6.35+build', 'v2026.13.35', 'v2026.06.35',
                                                       'v2026.6.0', 'v2026.6.1', 'v2026.6.32', 'v2026.6.32-1',
                                                       'v2026.6.35;touch injected')]
        for tag, ref in cases:
            with self.subTest(tag=tag, ref=ref):
                result, _, calls, _ = self.run_workflow(tag, ref)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(calls, [])

    def test_missing_target_and_credentials_fail_before_write(self):
        for changes in ({'missing_git_tag': True}, {'missing_version': True},
                        {'version_response': '2026.7.33'}, {'token': ''}):
            with self.subTest(changes=changes):
                result, _, calls, _ = self.run_workflow(**changes)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(any(a[0] == 'dist-tag' for a in calls))

    def test_write_error_is_not_retried(self):
        result, _, calls, summary = self.run_workflow(write_error=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(sum(a[0] == 'dist-tag' for a in calls), 1)
        self.assertIn('write failed or unconfirmed', summary)

    def test_readback_failure_is_bounded_and_never_republishes(self):
        result, _, calls, summary = self.run_workflow(never_converge=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(sum(a[0] == 'dist-tag' for a in calls), 1)
        self.assertEqual(sum(a[:3] == ['view', 'openclaw', 'dist-tags'] for a in calls), 62)
        self.assertIn('write may have succeeded', summary)

    def test_manual_mode_does_not_trigger_beta_floor(self):
        self.assertIn('          - promote_extended_stable\n', WORKFLOW)
        self.assertIn("github.event_name == 'workflow_dispatch' && inputs.mode == 'promote_extended_stable'", JOB)
        self.assertIn('group: openclaw-npm-dist-tags\n  cancel-in-progress: false', WORKFLOW)
        floor = WORKFLOW.split('  sync_beta_to_stable:\n', 1)[1].split('    runs-on:', 1)[0]
        self.assertNotIn('promote_extended_stable', floor)
        self.assertNotIn('latest_published', JOB)


class RegularChannelAdmissionTests(unittest.TestCase):
    def test_dist_tag_maintenance_cannot_promote_regular_stable(self):
        # These public dispatch modes bypass the source repository's qualification gates.
        for mode in ('promote_beta_to_latest', 'sync_stable_dist_tags'):
            self.assertNotIn(mode, WORKFLOW)
        self.assertNotRegex(WORKFLOW, r'npm dist-tag add[^\n]+ latest(?:\s|$)')

    def test_scheduled_sync_rejects_extended_stable_latest_before_git_lookup(self):
        job = WORKFLOW.split('\n  sync_beta_to_stable:\n', 1)[1].split('\n  promote_extended_stable:', 1)[0]
        for version, allowed in (('2026.9.32', True), ('2026.9.32-1', True),
                                 ('2026.9.33', False), ('2026.9.34', False),
                                 ('2026.9.100', False), ('2026.9.33-beta.1', False)):
            with self.subTest(version=version), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                for name, body in {'npm': '#!/bin/sh\nprintf "%s" "$TEST_VERSION"\n',
                                   'git': '#!/bin/sh\ntouch git-called\n'}.items():
                    (root / name).write_text(body)
                    (root / name).chmod(0o755)
                result = subprocess.run(['bash', '-c', script('Validate latest release tag exists in public repo', job)],
                                        cwd=root, env=dict(os.environ, PATH=td + os.pathsep + os.environ['PATH'],
                                                          TEST_VERSION=version, OPENCLAW_REPOSITORY='openclaw/openclaw'),
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode == 0, allowed, result.stderr)
                self.assertEqual((root / 'git-called').exists(), allowed)


if __name__ == '__main__':
    unittest.main()
