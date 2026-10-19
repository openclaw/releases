"""Exercise publisher ownership and reruns against real local Git branches."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('appcast', ROOT / 'scripts/update-macos-appcast.py')
appcast = importlib.util.module_from_spec(spec)
spec.loader.exec_module(appcast)
BRANCH = 'automation/macos-appcast-2026.8.2'
REPO = 'openclaw/openclaw'
BOT = 'openclaw-macos-publisher[bot]'


class AppcastTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.remote = self.root / 'remote.git'
        self.seed = self.root / 'seed'
        self.actual_run = appcast.run
        self.actual_run('git', 'init', '--bare', '--initial-branch=main', str(self.remote))
        self.actual_run('git', 'clone', str(self.remote), str(self.seed))
        self.git('config', 'user.name', 'Fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        for name in appcast.FEEDS:
            (self.seed / name).write_text('previous feed\n')
        (self.seed / 'unrelated.txt').write_text('preserve\n')
        self.commit('initial')
        self.git('push', 'origin', 'main')
        self.main_sha = self.git('rev-parse', 'HEAD')
        self.sources = []
        for index, name in enumerate(appcast.FEEDS):
            source = self.root / name
            source.write_text(f'prepared feed {index}\n')
            self.sources.append(source)
        self.body = self.root / 'body.md'
        self.body.write_text('## Evidence\nprepared bytes\n')
        self.pr = None
        self.fail = ''
        self.calls = []
        self.push_race = False
        self.mutated = False
        self.addCleanup(patch.stopall)
        patch.object(appcast, 'run', self.command).start()

    def git(self, *args):
        return self.actual_run('git', *args, cwd=self.seed)

    def commit(self, message):
        self.git('add', '.')
        self.git('commit', '-m', message)

    def remote_sha(self):
        value = self.git('ls-remote', '--heads', 'origin', f'refs/heads/{BRANCH}')
        return value.split()[0] if value else None

    def command(self, *args, cwd=None):
        self.calls.append(args)
        if args[:2] == ('git', 'clone'):
            args = (*args[:-2], str(self.remote), args[-1])
        if args[0] != 'gh':
            if 'push' in args and self.push_race:
                self.git('fetch', 'origin', BRANCH)
                self.git('checkout', '-B', BRANCH, 'FETCH_HEAD')
                (self.seed / 'unrelated.txt').write_text('concurrent writer\n')
                self.commit('concurrent writer')
                self.git('push', 'origin', BRANCH)
                self.mutated = True
                self.push_race = False
            return self.actual_run(*args, cwd=cwd)
        if args[1:3] == ('api', f'users/{BOT}'):
            return json.dumps({'id': 123})
        if args[1] == 'api':
            if self.pr:
                return json.dumps([dict(self.pr, head=dict(self.pr['head'], sha=self.remote_sha()))])
            return '[]'
        operation = args[2]
        if self.fail == operation:
            raise subprocess.CalledProcessError(1, args)
        body = Path(args[args.index('--body-file') + 1]).read_text()
        self.pr = self.make_pr(body)
        return self.pr['html_url']

    def make_pr(self, body='original evidence'):
        return {'number': 123, 'user': {'login': BOT}, 'body': body,
                'html_url': 'https://github.com/openclaw/openclaw/pull/123',
                'head': {'ref': BRANCH, 'sha': self.remote_sha(), 'repo': {'full_name': REPO}},
                'base': {'ref': 'main', 'repo': {'full_name': REPO}}}

    def propose(self):
        return appcast.propose(REPO, '2026.8.2', 'openclaw-macos-publisher', self.sources, self.body)

    def branch_file(self, name):
        return self.actual_run('git', '--git-dir', str(self.remote), 'show', f'{BRANCH}:{name}')

    def test_new_pr_then_unchanged_and_changed_reruns_preserve_main(self):
        result = self.propose()
        first = self.remote_sha()
        self.assertIn('pending merge:', result)
        self.assertEqual(self.propose(), result)
        self.assertEqual(self.remote_sha(), first)
        self.sources[1].write_text('updated prepared feed\n')
        self.assertEqual(self.propose(), result)
        second = self.remote_sha()
        self.assertNotEqual(second, first)
        self.actual_run('git', '--git-dir', str(self.remote), 'merge-base', '--is-ancestor', first, second)
        self.assertEqual(self.branch_file('appcast-arm64.xml'), 'updated prepared feed')
        self.assertEqual(self.branch_file('unrelated.txt'), 'preserve')
        self.assertEqual(self.git('ls-remote', 'origin', 'refs/heads/main').split()[0], self.main_sha)
        for call in self.calls:
            self.assertFalse(any('--force' in arg or 'x-access-token:' in arg for arg in call))
            if 'push' in call:
                self.assertEqual(call[-1], f'HEAD:refs/heads/{BRANCH}')

    def test_already_current_main_does_not_create_branch_or_pr(self):
        for source, name in zip(self.sources, appcast.FEEDS):
            source.write_bytes((self.seed / name).read_bytes())
        self.assertIn('main already has', self.propose())
        self.assertIsNone(self.remote_sha())
        self.assertIsNone(self.pr)

    def test_rerun_preserves_new_main_commits(self):
        self.propose()
        (self.seed / 'unrelated.txt').write_text('new main work\n')
        self.commit('main update')
        self.git('push', 'origin', 'main')
        self.propose()
        self.assertEqual(self.branch_file('unrelated.txt'), 'new main work')
        self.propose()

    def test_existing_branch_requires_matching_open_bot_pr(self):
        self.propose()
        original = self.remote_sha()
        valid = self.pr
        for kind in ['orphan', 'author', 'base', 'repository']:
            with self.subTest(kind=kind):
                self.pr = json.loads(json.dumps(valid))
                if kind == 'orphan':
                    self.pr = None
                elif kind == 'author':
                    self.pr['user']['login'] = 'another-writer'
                elif kind == 'base':
                    self.pr['base']['ref'] = 'release/2026.8.2'
                else:
                    self.pr['head']['repo']['full_name'] = 'other/repo'
                with self.assertRaisesRegex(ValueError, 'Orphan|collision'):
                    self.propose()
                self.assertEqual(self.remote_sha(), original)

    def test_reverted_unrelated_branch_history_is_not_taken_over(self):
        self.propose()
        self.git('fetch', 'origin', BRANCH)
        self.git('checkout', '-b', BRANCH, 'FETCH_HEAD')
        (self.seed / 'unrelated.txt').write_text('foreign change\n')
        self.commit('foreign')
        self.git('revert', '--no-edit', 'HEAD')
        self.git('push', 'origin', BRANCH)
        original = self.remote_sha()
        with self.assertRaisesRegex(ValueError, 'unrelated history'):
            self.propose()
        self.assertEqual(self.remote_sha(), original)

    def test_concurrent_push_is_rejected_without_overwriting_writer(self):
        self.propose()
        self.sources[0].write_text('changed feed\n')
        self.push_race = True
        with self.assertRaises(subprocess.CalledProcessError):
            self.propose()
        self.assertTrue(self.mutated)
        self.assertEqual(self.branch_file('unrelated.txt'), 'concurrent writer')
        self.assertNotEqual(self.branch_file('appcast.xml'), 'changed feed')

    def test_failed_pr_creation_leaves_explicit_orphan_then_refuses_takeover(self):
        self.fail = 'create'
        with self.assertRaisesRegex(ValueError, 'publication failed.*branch may exist'):
            self.propose()
        original = self.remote_sha()
        self.assertIsNotNone(original)
        self.fail = ''
        with self.assertRaisesRegex(ValueError, 'Orphan'):
            self.propose()
        self.assertEqual(self.remote_sha(), original)

    def test_failed_pr_refresh_is_visible(self):
        self.propose()
        self.fail = 'edit'
        with self.assertRaisesRegex(ValueError, 'publication failed'):
            self.propose()


if __name__ == '__main__':
    unittest.main()
