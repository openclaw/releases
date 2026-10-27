"""Exercise both evidence PR entry points against a real temporary Git remote."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ('openclaw-release-evidence.yml', 'openclaw-release-evidence-from-full-validation.yml')
BOT = 'openclaw-releases[bot]'


def git(cwd, *args):
    return subprocess.check_output(['git', *args], cwd=cwd, stderr=subprocess.PIPE, text=True).strip()


def publication_step(name):
    text = (ROOT / '.github/workflows' / name).read_text()
    step = text.split('      - name: Propose evidence pull request\n', 1)[1]
    return step.split('        run: ', 1)[1].splitlines()[0]


# Only GitHub's transport is substituted; every Git operation is real.
GH_STUB = '''#!/usr/bin/env python3
import json, os, pathlib, subprocess, sys
state_path = pathlib.Path(os.environ['GH_FIXTURE_STATE'])
state = json.loads(state_path.read_text())
args = sys.argv[1:]
method = args[args.index('--method') + 1]
fields = dict(arg.split('=', 1) for index, arg in enumerate(args) if index and args[index - 1] == '-f')
state['calls'].append(method)
def git(*args):
    return subprocess.check_output(['git', *args], cwd=os.environ['GH_FIXTURE_OTHER'], text=True, stderr=subprocess.PIPE).strip()
if method == 'POST':
    branch = fields['head']
    sha = git('ls-remote', 'origin', 'refs/heads/' + branch).split()[0]
    if state['mode'] != 'create-rejected':
        state['pr'] = {'number': 123, 'html_url': 'https://github.com/openclaw/releases/pull/123',
                       'state': 'open', 'user': {'login': 'openclaw-releases[bot]'},
                       'head': {'ref': branch, 'sha': sha, 'repo': {'full_name': 'openclaw/releases'}},
                       'base': {'ref': 'main', 'repo': {'full_name': 'openclaw/releases'}}}
    if state['mode'] == 'foreign':
        state['pr']['user']['login'] = 'foreign-writer'
    if state['mode'] == 'closed':
        state['pr']['state'] = 'closed'
    if state['mode'] == 'stale-sha':
        state['pr']['head']['sha'] = '0' * 40
elif state['mode'] in ('race-directory', 'race-unrelated') and not state.get('raced'):
    name = 'evidence/2026.9.1/other.json' if state['mode'] == 'race-directory' else 'unrelated.txt'
    path = pathlib.Path(os.environ['GH_FIXTURE_OTHER']) / name
    path.write_text('{"concurrent":true}\\n')
    git('add', name)
    git('commit', '-m', 'concurrent main write')
    git('push', 'origin', 'HEAD:main')
    state['raced'] = True
state_path.write_text(json.dumps(state))
if method == 'POST' and state['mode'] in ('create-rejected', 'create-ambiguous'):
    sys.exit(1)
print(json.dumps([state['pr']] if method == 'GET' and state.get('pr') else []))
'''


class ReleaseEvidencePublicationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.remote, self.worker, self.other = (self.root / name for name in ('remote.git', 'worker', 'other'))
        git(self.root, 'init', '--bare', '--initial-branch=main', str(self.remote))
        git(self.root, 'clone', str(self.remote), str(self.worker))
        self.configure(self.worker)
        self.evidence = self.worker / 'evidence/2026.9.1'
        self.evidence.mkdir(parents=True)
        (self.evidence / 'release-evidence.json').write_text('{"generation":1}\n')
        git(self.worker, 'add', '.')
        git(self.worker, 'commit', '-m', 'initial')
        git(self.worker, 'push', 'origin', 'HEAD:main')
        self.initial = git(self.remote, 'rev-parse', 'main')
        git(self.root, 'clone', str(self.remote), str(self.other))
        self.configure(self.other)
        self.bin = self.root / 'bin'
        self.bin.mkdir()
        gh = self.bin / 'gh'
        gh.write_text(GH_STUB)
        gh.chmod(0o755)
        self.state = self.root / 'github.json'
        self.state.write_text(json.dumps({'calls': [], 'mode': 'normal'}))
        self.summary = self.root / 'summary.md'

    def configure(self, path):
        git(path, 'config', 'user.name', 'Fixture')
        git(path, 'config', 'user.email', 'fixture@example.invalid')
        git(path, 'config', 'commit.gpgsign', 'false')

    def mode(self, mode):
        state = json.loads(self.state.read_text())
        state['mode'] = mode
        self.state.write_text(json.dumps(state))

    def generate(self):
        (self.evidence / 'release-evidence.json').write_text('{"generation":2}\n')

    def run_writer(self, workflow=WORKFLOWS[0], release_id='2026.9.1'):
        scripts = self.worker / 'scripts'
        if not scripts.exists():
            scripts.symlink_to(ROOT / 'scripts', target_is_directory=True)
        return subprocess.run(['bash', '-c', publication_step(workflow)], cwd=self.worker,
                              env=dict(os.environ, RELEASE_ID=release_id, EVIDENCE_APP_BOT=BOT,
                                       GH_FIXTURE_STATE=str(self.state), GH_FIXTURE_OTHER=str(self.other),
                                       GITHUB_STEP_SUMMARY=str(self.summary),
                                       PATH=str(self.bin) + os.pathsep + os.environ['PATH']),
                              capture_output=True, text=True)

    def assert_main_unchanged(self):
        self.assertEqual(git(self.remote, 'rev-parse', 'main'), self.initial)

    def fresh_worker(self):
        self.worker = self.root / ('worker-' + str(len(list(self.root.glob('worker*')))))
        git(self.root, 'clone', str(self.remote), str(self.worker))
        self.configure(self.worker)
        self.evidence = self.worker / 'evidence/2026.9.1'
        self.generate()

    def test_both_entrypoints_open_evidence_only_prs_without_writing_main(self):
        for workflow in WORKFLOWS:
            with self.subTest(workflow=workflow):
                self.generate()
                result = self.run_writer(workflow)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                state = json.loads(self.state.read_text())
                pr = state['pr']
                branch = pr['head']['ref']
                self.assertEqual(git(self.remote, 'show', f'{branch}:evidence/2026.9.1/release-evidence.json'),
                                 '{"generation":2}')
                self.assertEqual(git(self.remote, 'diff', '--name-only', f'main...{branch}'),
                                 'evidence/2026.9.1/release-evidence.json')
                self.assertIn('not yet in main', self.summary.read_text())
                self.assert_main_unchanged()
                first_sha = pr['head']['sha']
                self.fresh_worker()
        self.assertEqual(json.loads(self.state.read_text())['calls'].count('POST'), 1)
        self.assertEqual(json.loads(self.state.read_text())['pr']['head']['sha'], first_sha)

    def test_unchanged_record_is_verified_on_fresh_main(self):
        result = self.run_writer()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('already on origin/main', result.stdout)
        self.assertEqual(json.loads(self.state.read_text())['calls'], [])
        self.assertEqual(git(self.remote, 'for-each-ref', '--format=%(refname)', 'refs/heads'), 'refs/heads/main')
        self.assert_main_unchanged()

    def concurrent_main_update(self, path, *, unchanged=False, accepted=False):
        if not unchanged:
            self.generate()
        (self.other / path).write_text('{"remote":true}\n')
        git(self.other, 'add', '.')
        git(self.other, 'commit', '-m', 'concurrent update')
        git(self.other, 'push', 'origin', 'HEAD:main')
        before = git(self.remote, 'rev-parse', 'main')
        result = self.run_writer()
        self.assertEqual(result.returncode == 0, accepted, result.stdout + result.stderr)
        self.assertEqual(git(self.remote, 'rev-parse', 'main'), before)
        if not accepted:
            self.assertFalse(json.loads(self.state.read_text()).get('pr'))

    def test_unrelated_concurrent_update_is_rebased(self):
        self.concurrent_main_update('unrelated.txt', accepted=True)

    def test_same_directory_concurrent_addition_is_rejected(self):
        self.concurrent_main_update('evidence/2026.9.1/other.json')

    def test_stale_noop_is_rejected(self):
        self.concurrent_main_update('evidence/2026.9.1/other.json', unchanged=True)

    def test_conflicting_concurrent_update_is_rejected(self):
        self.concurrent_main_update('evidence/2026.9.1/release-evidence.json')

    def test_same_directory_race_after_push_is_rejected_before_pr_creation(self):
        self.generate()
        self.mode('race-directory')
        result = self.run_writer()
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('evidence directory', result.stderr)
        self.assertNotIn('POST', json.loads(self.state.read_text())['calls'])

    def test_unrelated_race_after_push_is_preserved(self):
        self.generate()
        self.mode('race-unrelated')
        result = self.run_writer()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(git(self.remote, 'show', 'main:unrelated.txt'), '{"concurrent":true}')
        self.assertEqual(git(self.remote, 'show', 'main:evidence/2026.9.1/release-evidence.json'), '{"generation":1}')

    def test_ambiguous_create_reuses_accepted_request_without_repeating(self):
        self.generate()
        self.mode('create-ambiguous')
        result = self.run_writer()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(self.state.read_text())['calls'].count('POST'), 1)
        self.assert_main_unchanged()

    def test_rejected_create_leaves_orphan_for_explicit_recovery(self):
        self.generate()
        self.mode('create-rejected')
        result = self.run_writer()
        self.assertNotEqual(result.returncode, 0)
        self.fresh_worker()
        result = self.run_writer()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('recover it manually', result.stderr)
        self.assertEqual(json.loads(self.state.read_text())['calls'].count('POST'), 1)
        self.assert_main_unchanged()

    def test_reused_branch_cannot_hide_a_sibling_record_deletion_as_a_rename(self):
        previous = self.other / 'evidence/previous'
        previous.mkdir()
        (previous / 'old.json').write_text('{"retained":true}\n')
        git(self.other, 'add', '.')
        git(self.other, 'commit', '-m', 'older evidence record')
        git(self.other, 'push', 'origin', 'HEAD:main')
        git(self.worker, 'fetch', 'origin', 'main')
        git(self.worker, 'merge', '--ff-only', 'origin/main')
        self.initial = git(self.remote, 'rev-parse', 'main')
        (self.evidence / 'other.json').write_text('{"retained":true}\n')
        git(self.worker, 'add', 'evidence/2026.9.1')
        tree = git(self.worker, 'write-tree')
        directory_tree = git(self.worker, 'rev-parse', f'{tree}:evidence/2026.9.1')
        git(self.worker, 'reset', '--', 'evidence/2026.9.1')
        branch = f'evidence/2026.9.1/{directory_tree}'
        git(self.other, 'checkout', '-b', branch)
        git(self.other, 'mv', 'evidence/previous/old.json', 'evidence/2026.9.1/other.json')
        git(self.other, 'commit', '-m', 'rename another release record')
        git(self.other, 'push', 'origin', f'HEAD:refs/heads/{branch}')
        self.assertEqual(git(self.remote, 'diff', '--name-only', f'main...{branch}'),
                         'evidence/2026.9.1/other.json')
        state = json.loads(self.state.read_text())
        state['pr'] = {'number': 123, 'html_url': 'https://github.com/openclaw/releases/pull/123',
                       'state': 'open', 'user': {'login': BOT},
                       'head': {'ref': branch, 'sha': git(self.other, 'rev-parse', 'HEAD'),
                                'repo': {'full_name': 'openclaw/releases'}},
                       'base': {'ref': 'main', 'repo': {'full_name': 'openclaw/releases'}}}
        self.state.write_text(json.dumps(state))
        result = self.run_writer()
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('unrelated changes', result.stderr)
        self.assert_main_unchanged()

    def test_foreign_closed_and_wrong_commit_requests_are_rejected(self):
        for mode in ('foreign', 'closed', 'stale-sha'):
            with self.subTest(mode=mode):
                self.generate()
                self.mode(mode)
                state = json.loads(self.state.read_text())
                state.pop('pr', None)
                self.state.write_text(json.dumps(state))
                # Distinct generated bytes give each case its own immutable branch.
                (self.evidence / 'release-evidence.json').write_text(json.dumps({'mode': mode}) + '\n')
                result = self.run_writer()
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('unexpected ownership', result.stderr)
                self.assert_main_unchanged()
                self.fresh_worker()

    def test_missing_record_bad_id_and_unrelated_staging_fail_before_writes(self):
        (self.evidence / 'release-evidence.json').unlink()
        self.assertNotEqual(self.run_writer().returncode, 0)
        self.generate()
        self.assertNotEqual(self.run_writer(release_id='../outside').returncode, 0)
        (self.worker / 'unrelated.txt').write_text('unrelated\n')
        git(self.worker, 'add', 'unrelated.txt')
        self.assertIn('unrelated staged', self.run_writer().stderr)
        self.assertEqual(json.loads(self.state.read_text())['calls'], [])
        self.assert_main_unchanged()


if __name__ == '__main__':
    unittest.main()
