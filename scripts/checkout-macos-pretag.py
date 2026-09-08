"""Admit an exact signed public release candidate before executing its source."""
import json
import os
import re
import subprocess


def run(*args):
    return subprocess.check_output(args, text=True).strip()


def checkout():
    sha = os.environ['PRETAG_SOURCE_SHA']
    tag = os.environ['RELEASE_TAG']
    branch = os.environ['PUBLIC_RELEASE_BRANCH']
    if (os.environ['WORKFLOW_REF'] != 'refs/heads/main'
            or os.environ['PREFLIGHT_ONLY'] != 'true'
            or os.environ['SMOKE_TEST_ONLY'] != 'false'
            or os.environ.get('SOURCE_REF', '')
            or os.environ.get('RESUME_RUN_ID', '')):
        raise ValueError('Pretag admission requires a fresh signed artifact-only preflight from main')
    if not re.fullmatch(r'[0-9a-f]{40}', sha):
        raise ValueError('Pretag source must be an exact full commit SHA')
    if not re.fullmatch(r'v[0-9]{4}\.[1-9][0-9]*\.[1-9][0-9]*', tag):
        raise ValueError('Pretag admission currently supports stable release versions only')
    if branch != f'release/{tag[1:]}':
        raise ValueError('Pretag source requires the canonical release branch for its version')

    subprocess.run(['git', 'clone', '--filter=blob:none', '--no-checkout',
                    'https://github.com/openclaw/openclaw.git', 'source'], check=True)
    def git(*args):
        return run('git', '-C', 'source', *args)
    if git('rev-parse', f'refs/remotes/origin/{branch}') != sha:
        raise ValueError('Pretag source must equal the current canonical release branch head')
    commit = json.loads(run('gh', 'api', f'repos/openclaw/openclaw/commits/{sha}'))
    verification = commit.get('commit', {}).get('verification', {})
    if (commit.get('sha') != sha or verification.get('verified') is not True
            or verification.get('reason') != 'valid'):
        raise ValueError('Pretag source requires valid GitHub commit signature verification')
    package = json.loads(git('show', f'{sha}:package.json'))
    if package.get('name') != 'openclaw' or package.get('version') != tag[1:]:
        raise ValueError('Pretag source package identity does not match the requested release')
    # A tag created while this run queued is fine only when it freezes these bytes.
    existing = git('for-each-ref', '--format=%(refname)', f'refs/tags/{tag}')
    if f'refs/tags/{tag}' in existing.splitlines():
        if git('rev-parse', f'refs/tags/{tag}^{{commit}}') != sha:
            raise ValueError('Existing release tag selects a different source commit')
    git('checkout', '--detach', sha)
    if git('rev-parse', 'HEAD') != sha:
        raise ValueError('Checked-out source does not match the admitted commit')
    print(f'Admitted signed pretag source {sha} from {branch}; publication remains disabled.')


if __name__ == '__main__':
    checkout()
