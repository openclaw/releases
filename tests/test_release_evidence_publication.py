"""Exercise both publication entry points against a real temporary Git remote."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ('openclaw-release-evidence.yml', 'openclaw-release-evidence-from-full-validation.yml')

GH_FIXTURE = '''#!/usr/bin/env python3
import json
import os
from pathlib import Path
import subprocess
import sys

root = Path(os.environ['FIXTURE_ROOT'])
scenario = os.environ['FIXTURE_SCENARIO']
state_file = root / 'pr.json'
history_file = root / 'prs.json'
remote = root / 'remote.git'
merger = root / 'other'
branch = os.environ['FIXTURE_BRANCH']
evidence_path = 'evidence/' + os.environ['RELEASE_ID']

def git(cwd, *args):
    return subprocess.check_output(['git', *args], cwd=cwd, stderr=subprocess.PIPE, text=True).strip()

def save(state):
    state_file.write_text(json.dumps(state))
    history = json.loads(history_file.read_text()) if history_file.exists() else {}
    history[state['branch']] = state
    history_file.write_text(json.dumps(history))

operation = sys.argv[1:3]
if sys.argv[1] == 'api':
    path = sys.argv[2]
    if path == 'apps/github-actions':
        response = {'id': 15368}
    elif '/rules/branches/main' in path:
        response = [] if scenario == 'missing-gate' else [
            {'type': 'non_fast_forward', 'ruleset_id': 1},
            {'type': 'required_status_checks', 'ruleset_id': 1, 'parameters': {
                'strict_required_status_checks_policy': True,
                'required_status_checks': [{'context': 'Publication merge admission', 'integration_id': 15368}]}}]
    elif '/rulesets/1?' in path:
        response = {'enforcement': 'active', 'bypass_actors': [{'actor_id': 1}] if scenario == 'bypass-gate' else []}
    elif '/pulls/' in path:
        state = json.loads(state_file.read_text())
        response = {'state': state['state'].lower(), 'head': {'sha': state['head'], 'ref': branch, 'repo': {'full_name': 'example/releases'}},
                    'base': {'sha': git(remote, 'rev-parse', 'main'), 'ref': 'main', 'repo': {'full_name': 'example/releases'}}}
    elif path.endswith('/git/ref/heads/main'):
        response = {'object': {'sha': git(remote, 'rev-parse', 'main')}}
    elif '/git/commits/' in path:
        sha = path.rsplit('/', 1)[1]
        response = {'sha': sha, 'tree': {'sha': git(remote, 'rev-parse', sha + '^{tree}')},
                    'parents': [{'sha': parent} for parent in git(remote, 'show', '-s', '--format=%P', sha).split()]}
    elif '/git/trees/' in path:
        sha = path.rsplit('/', 1)[1].split('?')[0]
        entries = []
        for line in git(remote, 'ls-tree', '-r', '-t', sha).splitlines():
            metadata, name = line.split('\\t', 1)
            mode, kind, oid = metadata.split()
            entries.append({'mode': mode, 'type': kind, 'sha': oid, 'path': name})
        response = {'truncated': False, 'tree': entries}
    elif '/statuses/' in path:
        fields = dict(arg.split('=', 1) for arg in sys.argv[3:] if '=' in arg)
        fields['sha'] = path.rsplit('/', 1)[1]
        (root / 'status.json').write_text(json.dumps(fields))
        response = fields
    else:
        raise AssertionError(path)
    print(json.dumps(response))
elif operation == ['pr', 'list']:
    requested = sys.argv[sys.argv.index('--head') + 1]
    history = json.loads(history_file.read_text()) if history_file.exists() else {}
    state = history.get(requested)
    if not state and state_file.exists():
        current = json.loads(state_file.read_text())
        state = current if current['branch'] == requested else None
    matches = state and state['head'] == git(remote, 'rev-parse', requested)
    if 'state' in sys.argv[sys.argv.index('--json') + 1].split(','):
        print('true' if matches and state['state'] == 'MERGED' else 'false')
    else:
        print('1' if matches else '')
elif operation == ['pr', 'create']:
    if scenario == 'create-failed':
        sys.exit(1)
    state = {'head': git(remote, 'rev-parse', branch), 'branch': branch, 'state': 'OPEN', 'merged': ''}
    save(state)
    if scenario == 'uncertain-create':
        sys.exit(1)
    print('https://github.com/example/releases/pull/1')
elif operation == ['pr', 'view']:
    state = json.loads(state_file.read_text())
    head = '0' * 40 if scenario == 'moved-head' else state['head']
    attested = (root / 'status.json').exists() and json.loads((root / 'status.json').read_text())['state'] == 'success'
    status = 'BLOCKED' if scenario == 'pending' or not attested else 'CLEAN'
    print('\\t'.join([head, 'CLOSED' if scenario == 'closed-pr' else state['state'], status, state['merged']]))
elif operation == ['pr', 'merge']:
    state = json.loads(state_file.read_text())
    assert sys.argv[sys.argv.index('--match-head-commit') + 1] == state['head']
    assert '--squash' in sys.argv and '--admin' not in sys.argv
    if scenario == 'merge-failed':
        sys.exit(1)
    git(merger, 'fetch', 'origin', 'main', branch)
    git(merger, 'checkout', 'main')
    git(merger, 'reset', '--hard', 'origin/main')
    if scenario == 'merge-base-race':
        (merger / evidence_path / 'concurrent.json').write_text('{}')
        git(merger, 'add', '.')
        git(merger, 'commit', '-m', 'Concurrent addition after final client check')
        git(merger, 'push', 'origin', 'HEAD:main')
    status = json.loads((root / 'status.json').read_text())
    assert status['sha'] == state['head'] and status['context'] == 'Publication merge admission' and status['state'] == 'success'
    # Emulate the server's strict required-status up-to-date admission.
    if git(remote, 'show', '-s', '--format=%P', state['head']) != git(remote, 'rev-parse', 'main'):
        sys.exit(1)
    git(merger, 'merge', '--squash', state['head'])
    if scenario == 'wrong-merged-tree':
        (merger / evidence_path / 'extra.json').write_text('{}')
        git(merger, 'add', '.')
    git(merger, 'commit', '-m', 'Squashed evidence PR')
    state['merged'] = git(merger, 'rev-parse', 'HEAD')
    assert state['merged'] != state['head']
    state['state'] = 'MERGED'
    git(merger, 'push', 'origin', 'HEAD:main')
    save(state)
    if scenario == 'uncertain-merge':
        sys.exit(1)
else:
    raise AssertionError(sys.argv)
'''

GIT_RACE_FIXTURE = '''#!/usr/bin/env python3
import os
from pathlib import Path
import subprocess
import sys

root = Path(os.environ['FIXTURE_ROOT'])
real_git = os.environ['FIXTURE_GIT']
# Preserve the caller's Git guard without letting it rediscover this fixture.
os.environ['PATH'] = os.environ['FIXTURE_PATH']
if sys.argv[1:] == ['fetch', 'origin', 'main']:
    counter = root / 'fetch-count'
    count = int(counter.read_text()) + 1 if counter.exists() else 1
    counter.write_text(str(count))
    if count == 2:
        other = root / 'other'
        (other / 'evidence' / os.environ['RELEASE_ID'] / 'late.json').write_text('{}')
        for args in [['add', '.'], ['commit', '-m', 'Concurrent evidence'], ['push', 'origin', 'HEAD:main']]:
            subprocess.run([real_git, *args], cwd=other, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
os.execv(real_git, [real_git, *sys.argv[1:]])
'''


def git(cwd, *args):
    return subprocess.check_output(['git', *args], cwd=cwd, stderr=subprocess.PIPE, text=True).strip()


def branch_for(worker, release_id):
    git(worker, 'add', '--', f'evidence/{release_id}')
    tree = git(worker, 'rev-parse', f'{git(worker, "write-tree")}:evidence/{release_id}')
    key = subprocess.check_output(['git', 'hash-object', '--stdin'], cwd=worker,
                                  input=release_id, text=True).strip()
    base = git(worker, 'ls-remote', 'origin', 'refs/heads/main').split()[0]
    return f'automation/release-evidence/{key}-{tree}-{base}'


def publication_step(name):
    text = (ROOT / '.github/workflows' / name).read_text()
    step = text.split('      - name: Commit evidence to main\n', 1)[1]
    run = step.split('        run: ', 1)[1]
    if run.startswith('|\n'):
        return '\n'.join(line[10:] for line in run.splitlines()[1:])
    return run.splitlines()[0]


class ReleaseEvidencePublicationTests(unittest.TestCase):
    def test_remote_publication_and_concurrent_updates(self):
        self.exercise_publication(('publish', 'noop', 'unrelated', 'same-directory', 'stale-noop',
                                   'conflict', 'missing', 'pending', 'moved-head', 'uncertain-create',
                                   'uncertain-merge', 'create-failed', 'merge-failed', 'wrong-merged-tree',
                                   'existing-branch', 'divergent-branch', 'unrelated-branch', 'closed-pr',
                                   'repeat-release', 'return-to-prior-payload', 'pending-generation',
                                   'unusual-release-id', 'fetch-race', 'missing-gate', 'bypass-gate', 'merge-base-race'))

    def test_cross_directory_rename_retains_other_release_evidence(self):
        self.exercise_publication(('cross-directory-rename',))

    def exercise_publication(self, scenarios):
        for workflow in WORKFLOWS:
            for scenario in scenarios:
                with self.subTest(workflow=workflow, scenario=scenario), tempfile.TemporaryDirectory() as td:
                    root = Path(td)
                    remote, worker, other = (root / name for name in ('remote.git', 'worker', 'other'))
                    git(root, 'init', '--bare', '--initial-branch=main', str(remote))
                    git(root, 'clone', str(remote), str(worker))
                    git(worker, 'config', 'user.name', 'Fixture')
                    git(worker, 'config', 'user.email', 'fixture@example.invalid')
                    git(worker, 'config', 'commit.gpgsign', 'false')
                    release_id = '2026..test.' if scenario == 'unusual-release-id' else '2026.9.1'
                    evidence_path = f'evidence/{release_id}'
                    evidence = worker / evidence_path
                    evidence.mkdir(parents=True)
                    (evidence / 'release-evidence.json').write_text('{"generation":1}\n')
                    if scenario == 'cross-directory-rename':
                        (worker / 'evidence/prior').mkdir()
                        (worker / 'evidence/prior/proof.json').write_text('{"prior":"retained"}\n')
                    git(worker, 'add', '.')
                    git(worker, 'commit', '-m', 'initial')
                    git(worker, 'push', 'origin', 'HEAD:main')
                    initial = git(worker, 'rev-parse', 'HEAD')
                    git(root, 'clone', str(remote), str(other))
                    git(other, 'config', 'user.name', 'Fixture')
                    git(other, 'config', 'user.email', 'fixture@example.invalid')
                    git(other, 'config', 'commit.gpgsign', 'false')
                    if scenario not in ('noop', 'stale-noop'):
                        (evidence / 'release-evidence.json').write_text('{"generation":2}\n')
                    if scenario == 'missing':
                        (evidence / 'release-evidence.json').unlink()
                    if scenario == 'cross-directory-rename':
                        (evidence / 'moved.json').write_text('{"prior":"retained"}\n')
                    remote_change = {
                        'unrelated': 'unrelated.txt',
                        'same-directory': f'{evidence_path}/other.json',
                        'stale-noop': f'{evidence_path}/other.json',
                        'conflict': f'{evidence_path}/release-evidence.json',
                    }.get(scenario)
                    if remote_change:
                        (other / remote_change).write_text('{"remote":true}\n')
                        git(other, 'add', '.')
                        git(other, 'commit', '-m', 'concurrent update')
                        git(other, 'push', 'origin', 'HEAD:main')
                    branch = branch_for(worker, release_id) if scenario != 'missing' else 'unused'
                    existing_head = None
                    if scenario in ('existing-branch', 'divergent-branch', 'unrelated-branch', 'closed-pr', 'cross-directory-rename'):
                        (other / evidence_path / 'release-evidence.json').write_text(
                            '{"generation":9}\n' if scenario == 'divergent-branch' else '{"generation":2}\n')
                        if scenario == 'unrelated-branch':
                            (other / 'unrelated.txt').write_text('foreign branch content')
                        if scenario == 'cross-directory-rename':
                            (other / 'evidence/prior/proof.json').rename(other / evidence_path / 'moved.json')
                        git(other, 'add', '.')
                        git(other, 'commit', '-m', 'Pending evidence')
                        if scenario == 'cross-directory-rename':
                            renamed = git(other, 'diff', '--find-renames', '--name-only', 'origin/main...HEAD')
                            self.assertNotIn('evidence/prior/proof.json', renamed)
                            self.assertIn(f'{evidence_path}/moved.json', renamed)
                        existing_head = git(other, 'rev-parse', 'HEAD')
                        git(other, 'push', 'origin', f'HEAD:{branch}')
                        if scenario == 'closed-pr':
                            (root / 'pr.json').write_text(json.dumps(
                                {'head': existing_head, 'branch': branch, 'state': 'CLOSED', 'merged': ''}))
                    if scenario == 'pending-generation':
                        (other / evidence_path / 'release-evidence.json').write_text('{"generation":9}\n')
                        prior_branch = branch_for(other, release_id)
                        git(other, 'commit', '-m', 'Prior pending generation')
                        git(other, 'push', 'origin', f'HEAD:{prior_branch}')
                    before = git(remote, 'rev-parse', 'main')
                    # Use real entrypoint paths: Node resolves symlinks before its CLI guard.
                    (worker / 'scripts').mkdir()
                    for script in ('publish-release-evidence.sh', 'publication-source.mjs'):
                        shutil.copy2(ROOT / 'scripts' / script, worker / 'scripts' / script)
                    binary = root / 'bin'
                    binary.mkdir()
                    (binary / 'gh').write_text(GH_FIXTURE)
                    (binary / 'gh').chmod(0o755)
                    (binary / 'sleep').write_text('#!/bin/sh\nexit 0\n')
                    (binary / 'sleep').chmod(0o755)
                    if scenario == 'fetch-race':
                        (binary / 'git').write_text(GIT_RACE_FIXTURE)
                        (binary / 'git').chmod(0o755)
                    env = dict(os.environ, RELEASE_ID=release_id,
                               PATH=f'{binary}{os.pathsep}{os.environ["PATH"]}',
                               GITHUB_REPOSITORY='example/releases', FIXTURE_ROOT=str(root),
                               FIXTURE_SCENARIO=scenario, FIXTURE_BRANCH=branch,
                               FIXTURE_GIT=shutil.which('git'), FIXTURE_PATH=os.environ['PATH'])
                    result = subprocess.run(['bash', '-c', publication_step(workflow)], cwd=worker,
                                            env=env,
                                            capture_output=True, text=True)
                    accepted = scenario in ('publish', 'noop', 'unrelated', 'uncertain-create',
                                            'uncertain-merge', 'existing-branch', 'repeat-release',
                                            'return-to-prior-payload', 'unusual-release-id')
                    self.assertEqual(result.returncode == 0, accepted, result.stdout + result.stderr)
                    if accepted:
                        self.assertEqual(git(remote, 'show', f'main:{evidence_path}/release-evidence.json'),
                                         (evidence / 'release-evidence.json').read_text().strip())
                        if scenario == 'noop':
                            self.assertEqual(git(remote, 'rev-parse', 'main'), initial)
                        if scenario == 'unrelated':
                            self.assertEqual(git(remote, 'show', 'main:unrelated.txt'), '{"remote":true}')
                        if scenario != 'noop':
                            state = json.loads((root / 'pr.json').read_text())
                            self.assertEqual(state['state'], 'MERGED')
                            self.assertNotEqual(state['head'], state['merged'])
                            self.assertEqual(git(remote, 'rev-parse', 'main'), state['merged'])
                    else:
                        if scenario == 'wrong-merged-tree':
                            self.assertIn('Merged evidence directory differs', result.stdout)
                        elif scenario == 'fetch-race':
                            self.assertEqual(git(remote, 'show', f'main:{evidence_path}/late.json'), '{}')
                            self.assertFalse((root / 'pr.json').exists())
                            self.assertIn('Remote evidence directory changed', result.stdout)
                        elif scenario == 'merge-base-race':
                            self.assertEqual(git(remote, 'show', f'main:{evidence_path}/concurrent.json'), '{}')
                            self.assertEqual(git(remote, 'show', f'main:{evidence_path}/release-evidence.json'), '{"generation":1}')
                            self.assertEqual(json.loads((root / 'pr.json').read_text())['state'], 'OPEN')
                        else:
                            self.assertEqual(git(remote, 'rev-parse', 'main'), before)
                        if scenario in ('same-directory', 'stale-noop'):
                            self.assertIn('evidence directory', result.stdout)
                        if scenario == 'cross-directory-rename':
                            self.assertIn('outside', result.stdout)
                            self.assertEqual(git(remote, 'show', 'main:evidence/prior/proof.json'),
                                             '{"prior":"retained"}')
                        if scenario in ('pending', 'moved-head', 'create-failed', 'merge-failed'):
                            self.assertTrue(git(remote, 'rev-parse', branch))
                        if scenario in ('pending', 'closed-pr', 'create-failed', 'merge-failed'):
                            self.assertIn('https://github.com/example/releases/', result.stdout)
                    if existing_head:
                        self.assertEqual(git(remote, 'rev-parse', branch), existing_head)
                    if scenario in ('repeat-release', 'return-to-prior-payload'):
                        prior_head = git(remote, 'rev-parse', branch)
                        git(worker, 'fetch', 'origin', 'main')
                        git(worker, 'reset', '--hard', 'origin/main')
                        (evidence / 'release-evidence.json').write_text('{"generation":3}\n')
                        next_branch = branch_for(worker, release_id)
                        self.assertNotEqual(branch, next_branch)
                        repeated = subprocess.run(['bash', '-c', publication_step(workflow)], cwd=worker,
                                                  env=dict(env, FIXTURE_BRANCH=next_branch),
                                                  capture_output=True, text=True)
                        self.assertEqual(repeated.returncode, 0, repeated.stdout + repeated.stderr)
                        self.assertEqual(git(remote, 'show', f'main:{evidence_path}/release-evidence.json'),
                                         '{"generation":3}')
                        self.assertEqual(git(remote, 'rev-parse', branch), prior_head)
                        if scenario == 'return-to-prior-payload':
                            git(worker, 'fetch', 'origin', 'main')
                            git(worker, 'reset', '--hard', 'origin/main')
                            (evidence / 'release-evidence.json').write_text('{"generation":2}\n')
                            return_branch = branch_for(worker, release_id)
                            self.assertNotIn(return_branch, (branch, next_branch))
                            returned = subprocess.run(['bash', '-c', publication_step(workflow)], cwd=worker,
                                                      env=dict(env, FIXTURE_BRANCH=return_branch),
                                                      capture_output=True, text=True)
                            self.assertEqual(returned.returncode, 0, returned.stdout + returned.stderr)
                            self.assertEqual(git(remote, 'show', f'main:{evidence_path}/release-evidence.json'),
                                             '{"generation":2}')


if __name__ == '__main__':
    unittest.main()
