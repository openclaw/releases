"""Propose prepared feeds without taking over another writer's branch."""
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

FEEDS = ('appcast.xml', 'appcast-arm64.xml', 'appcast-x86_64.xml')


def run(*args, cwd=None):
    return subprocess.check_output(args, cwd=cwd, text=True).strip()


def propose(repository, version, app_slug, sources, body_file):
    if not re.fullmatch(r'[0-9]{4}\.[1-9][0-9]*\.[1-9][0-9]*(?:-[1-9][0-9]*)?', version):
        raise ValueError('Stable appcast requires an exact stable version')
    branch = f'automation/macos-appcast-{version}'
    bot = f'{app_slug}[bot]'
    owner = repository.split('/')[0]
    endpoint = f'repos/{repository}/pulls?state=open&head={owner}:{branch}'

    def pull_request():
        prs = json.loads(run('gh', 'api', endpoint))
        if not prs:
            return None
        if len(prs) != 1:
            raise ValueError(f'Ambiguous appcast PRs for {branch}; inspect before retrying')
        pr = prs[0]
        if (pr['user']['login'] != bot or pr['base']['ref'] != 'main'
                or pr['base']['repo']['full_name'] != repository
                or pr['head']['ref'] != branch or pr['head']['repo']['full_name'] != repository):
            raise ValueError(f'Appcast branch collision: {branch} is not owned by this publisher PR')
        return pr

    with tempfile.TemporaryDirectory(prefix='macos-appcast-') as directory:
        checkout = Path(directory) / 'source'
        run('git', 'clone', '--filter=blob:none', '--single-branch', '--branch', 'main',
            '--no-tags', f'https://github.com/{repository}.git', str(checkout))

        def git(*args):
            return run('git', *args, cwd=checkout)

        def remote_head():
            value = git('ls-remote', '--heads', 'origin', f'refs/heads/{branch}')
            return value.split()[0] if value else None

        expected = remote_head()
        pr = pull_request()
        if bool(expected) != bool(pr):
            raise ValueError(f'Orphan appcast branch or PR at {branch}; inspect ownership before retrying')
        if pr:
            git('fetch', '--no-tags', 'origin', f'refs/heads/{branch}')
            if git('rev-parse', 'FETCH_HEAD') != expected or pr['head']['sha'] != expected:
                raise ValueError('Appcast branch moved during admission; inspect before retrying')
            git('checkout', '-b', branch, expected)
            # Check every branch-only commit, not just the final diff: an
            # unrelated change followed by a revert is still foreign history.
            paths = set(git('log', '--format=', '--name-only', f'origin/main..{branch}').splitlines()) - {''}
            paths.update(git('diff', '--name-only', f'origin/main...{branch}').splitlines())
            if not paths <= set(FEEDS):
                raise ValueError('Appcast branch contains unrelated history; refusing takeover')
        else:
            git('checkout', '-b', branch)

        user = json.loads(run('gh', 'api', f'users/{bot}'))
        git('config', 'user.name', bot)
        git('config', 'user.email', f'{user["id"]}+{bot}@users.noreply.github.com')
        if pr:
            # Preserve newer main changes without rewriting the admitted PR head.
            git('merge', '--no-edit', 'origin/main')
        for name, source in zip(FEEDS, sources, strict=True):
            shutil.copyfile(source, checkout / name)
        git('add', '--', *FEEDS)
        if git('diff', '--cached', '--name-only'):
            git('commit', '-m', f'chore(release): update appcast for {version}')
        head = git('rev-parse', 'HEAD')
        if remote_head() != expected:
            raise ValueError('Appcast branch moved before push; refusing concurrent update')
        if not pr and not git('diff', '--name-only', 'origin/main', 'HEAD'):
            return f'Public main already has every macOS appcast for v{version}.'
        if head != expected:
            # Credentials stay in GH_TOKEN and the helper, never the remote URL.
            git('-c', 'credential.helper=', '-c', 'credential.helper=!gh auth git-credential',
                'push', 'origin', f'HEAD:refs/heads/{branch}')
        if remote_head() != head:
            raise ValueError('Appcast branch moved after push; inspect before retrying')
        current = pull_request()
        if (pr and (not current or current['number'] != pr['number']
                    or current['head']['sha'] != head)) or (not pr and current):
            raise ValueError('Appcast PR changed during publication; inspect before retrying')
        try:
            if pr:
                run('gh', 'pr', 'edit', str(pr['number']), '--repo', repository,
                    '--body-file', str(body_file))
            else:
                run('gh', 'pr', 'create', '--repo', repository, '--head', branch, '--base', 'main',
                    '--title', f'chore(release): update appcast for {version}',
                    '--body-file', str(body_file))
            result = pull_request()
            if not result or result['head']['sha'] != head or result['body'] != body_file.read_text():
                raise ValueError('Appcast PR readback does not match the proposed head and evidence')
        except (subprocess.CalledProcessError, ValueError) as error:
            raise ValueError(f'Appcast PR publication failed for {branch}; branch may exist. '
                             'Inspect the branch and PR before retrying; no takeover was attempted.') from error
        return f'Stable feeds pending merge: {result["html_url"]}'


def main():
    result = propose(os.environ['OPENCLAW_REPOSITORY'], os.environ['VERSION'],
                     os.environ['PUBLISHER_APP_SLUG'],
                     [Path(os.environ[f'{variant}_APPCAST']).resolve()
                      for variant in ('UNIVERSAL', 'ARM64', 'X86_64')], Path(sys.argv[1]).resolve())
    print(result)
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
            summary.write(f'\n{result}\n')


if __name__ == '__main__':
    main()
