"""Admit an exact-source FRV package without repacking a frozen release."""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys


def verify_bundle(directory, run, tag, sha):
    bundle = json.loads((directory / 'package-bundle.json').read_text())
    producer = bundle['producer']
    expected = {
        'schema': 'openclaw.npm-package-bundle/v1', 'releaseTag': tag,
        'releaseSha': sha, 'packageName': 'openclaw', 'packageVersion': tag[1:],
    }
    if any(bundle.get(key) != value for key, value in expected.items()):
        raise ValueError('Prepared npm package does not match the frozen release identity')
    if (producer.get('repository') != 'openclaw/openclaw'
            or producer.get('runId') != str(run['id'])
            or producer.get('runAttempt') != str(run['run_attempt'])
            or producer.get('workflowSha') != sha
            or producer.get('producerWorkflowPath') != '.github/workflows/openclaw-npm-preflight.yml'):
        raise ValueError('Prepared npm package producer provenance mismatch')
    entries = [bundle] + bundle['corePackageTarballs']
    for entry in entries:
        name = entry['tarballName']
        digest = entry['tarballSha256']
        if (Path(name).name != name or not name.endswith('.tgz')
                or not re.fullmatch(r'[0-9a-f]{64}', digest)
                or entry['packageVersion'] != tag[1:]):
            raise ValueError('Invalid prepared package tarball identity')
        if hashlib.sha256((directory / name).read_bytes()).hexdigest() != digest:
            raise ValueError('Prepared package tarball hash mismatch: ' + name)
    return entries


def main():
    run_id = os.environ['PREPARED_PACKAGE_RUN_ID']
    if not re.fullmatch(r'[1-9][0-9]*', run_id):
        raise ValueError('Prepared package requires a positive run id')
    sha = os.environ['SOURCE_SHA']
    tag = os.environ['RELEASE_TAG']
    run = json.loads(subprocess.check_output([
        'gh', 'api', f'repos/openclaw/openclaw/actions/runs/{run_id}',
    ]))
    if (run['status'] != 'completed' or run['conclusion'] != 'success'
            or run['head_sha'] != sha
            or run['path'] != '.github/workflows/full-release-artifacts.yml'):
        raise ValueError('Prepared package run must be successful FRV artifacts for this source SHA')
    directory = Path(sys.argv[1])
    directory.mkdir()
    subprocess.run([
        'gh', 'run', 'download', run_id, '--repo', 'openclaw/openclaw',
        '--name', f'openclaw-npm-package-{run_id}-{run["run_attempt"]}',
        '--dir', str(directory),
    ], check=True)
    entries = verify_bundle(directory, run, tag, sha)
    dependencies = directory / 'dependencies'
    dependencies.mkdir()
    for entry in entries[1:]:
        shutil.copyfile(directory / entry['tarballName'], dependencies / entry['tarballName'])
    shutil.copyfile(directory / entries[0]['tarballName'], directory / 'openclaw.tgz')
    print(f'Admitted FRV package for {tag} at {sha}: {entries[0]["tarballSha256"]}')


if __name__ == '__main__':
    main()
