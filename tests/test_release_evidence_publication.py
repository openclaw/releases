"""Exercise both publication entry points against a real temporary Git remote."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ('openclaw-release-evidence.yml', 'openclaw-release-evidence-from-full-validation.yml')


def git(cwd, *args):
    return subprocess.check_output(['git', *args], cwd=cwd, stderr=subprocess.PIPE, text=True).strip()


def publication_step(name):
    text = (ROOT / '.github/workflows' / name).read_text()
    step = text.split('      - name: Commit evidence to main\n', 1)[1]
    run = step.split('        run: ', 1)[1]
    if run.startswith('|\n'):
        return '\n'.join(line[10:] for line in run.splitlines()[1:])
    return run.splitlines()[0]


class ReleaseEvidencePublicationTests(unittest.TestCase):
    def test_remote_publication_and_concurrent_updates(self):
        for workflow in WORKFLOWS:
            for scenario in ('publish', 'noop', 'unrelated', 'same-directory', 'stale-noop', 'conflict', 'missing'):
                with self.subTest(workflow=workflow, scenario=scenario), tempfile.TemporaryDirectory() as td:
                    root = Path(td)
                    remote, worker, other = (root / name for name in ('remote.git', 'worker', 'other'))
                    git(root, 'init', '--bare', '--initial-branch=main', str(remote))
                    git(root, 'clone', str(remote), str(worker))
                    git(worker, 'config', 'user.name', 'Fixture')
                    git(worker, 'config', 'user.email', 'fixture@example.invalid')
                    evidence = worker / 'evidence/2026.9.1'
                    evidence.mkdir(parents=True)
                    (evidence / 'release-evidence.json').write_text('{"generation":1}\n')
                    git(worker, 'add', '.')
                    git(worker, 'commit', '-m', 'initial')
                    git(worker, 'push', 'origin', 'HEAD:main')
                    initial = git(worker, 'rev-parse', 'HEAD')
                    git(root, 'clone', str(remote), str(other))
                    git(other, 'config', 'user.name', 'Fixture')
                    git(other, 'config', 'user.email', 'fixture@example.invalid')
                    if scenario not in ('noop', 'stale-noop'):
                        (evidence / 'release-evidence.json').write_text('{"generation":2}\n')
                    if scenario == 'missing':
                        (evidence / 'release-evidence.json').unlink()
                    remote_change = {
                        'unrelated': 'unrelated.txt',
                        'same-directory': 'evidence/2026.9.1/other.json',
                        'stale-noop': 'evidence/2026.9.1/other.json',
                        'conflict': 'evidence/2026.9.1/release-evidence.json',
                    }.get(scenario)
                    if remote_change:
                        (other / remote_change).write_text('{"remote":true}\n')
                        git(other, 'add', '.')
                        git(other, 'commit', '-m', 'concurrent update')
                        git(other, 'push', 'origin', 'HEAD:main')
                    before = git(remote, 'rev-parse', 'main')
                    # Production invokes the shared script relative to the checkout.
                    (worker / 'scripts').symlink_to(ROOT / 'scripts', target_is_directory=True)
                    result = subprocess.run(['bash', '-c', publication_step(workflow)], cwd=worker,
                                            env=dict(os.environ, RELEASE_ID='2026.9.1'),
                                            capture_output=True, text=True)
                    accepted = scenario in ('publish', 'noop', 'unrelated')
                    self.assertEqual(result.returncode == 0, accepted, result.stdout + result.stderr)
                    if accepted:
                        self.assertEqual(git(remote, 'show', 'main:evidence/2026.9.1/release-evidence.json'),
                                         (evidence / 'release-evidence.json').read_text().strip())
                        if scenario == 'noop':
                            self.assertEqual(git(remote, 'rev-parse', 'main'), initial)
                        if scenario == 'unrelated':
                            self.assertEqual(git(remote, 'show', 'main:unrelated.txt'), '{"remote":true}')
                    else:
                        self.assertEqual(git(remote, 'rev-parse', 'main'), before)
                        if scenario in ('same-directory', 'stale-noop'):
                            self.assertIn('evidence directory', result.stdout)


if __name__ == '__main__':
    unittest.main()
