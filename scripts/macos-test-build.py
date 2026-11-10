#!/usr/bin/env python3
"""Admit and sign test apps without running candidate code in the signing job."""
import base64
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import plistlib
import posixpath
import re
import secrets
import shlex
import signal
import stat
import subprocess
import sys
import tempfile
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET
import zipfile

IDENTITY = 'Developer ID Application: OpenClaw Foundation (FWJYW4S8P8)'
TEAM = 'FWJYW4S8P8'
# Mirror release-managers-openclaw membership, plus the authorized test operator.
ALLOWED_ACTORS = ["vincentkoc", "steipete", "joshavant", "RomneyDa", "Patrick-Erichsen", "jalehman"]
FEED = 'https://raw.githubusercontent.com/openclaw/openclaw/main/appcast.xml'
SPARKLE = '{http://www.andymatuschak.org/xml-namespaces/sparkle}'


def inputs(env):
    """Require a trusted dispatch and shell/path-safe exact source/build inputs."""
    if (env.get('GITHUB_REPOSITORY') != 'openclaw/releases'
            or env.get('GITHUB_REF') != 'refs/heads/main'
            or env.get('GITHUB_EVENT_NAME') != 'workflow_dispatch'):
        raise ValueError('Test builds require an approved dispatch from openclaw/releases main')
    sha, version = env['SOURCE_SHA'], env['VERSION_OVERRIDE']
    if not re.fullmatch(r'[0-9a-f]{40}', sha):
        raise ValueError('source_sha must be exactly 40 lowercase hexadecimal characters')
    if not re.fullmatch(r'[1-9][0-9]{0,14}', version):
        raise ValueError('version_override must be a positive decimal CFBundleVersion (at most 15 digits)')
    return sha, version


def stable_floor(xml):
    """Use Sparkle's comparison version, not the marketing/package version."""
    items = ET.fromstring(xml).findall('./channel/item')
    versions = [item.findtext(SPARKLE + 'version', '') for item in items]
    if not versions or any(not re.fullmatch(r'[1-9][0-9]{0,14}', v) for v in versions):
        raise ValueError('Stable appcast must contain numeric Sparkle versions')
    return max(map(int, versions))


def admit(env):
    """Admit only approved actors, canonical branch heads and a safe build version."""
    sha, version = inputs(env)
    if any(env.get(key) not in ALLOWED_ACTORS
           for key in ('GITHUB_ACTOR', 'GITHUB_TRIGGERING_ACTOR')):
        raise ValueError('Both the original and triggering actors must be allowlisted')
    # A commit lookup alone can resolve fork-network commits. Require a current
    # branch head in the canonical repository, not a PR ref or merely a known SHA.
    request = Request(
        f'https://api.github.com/repos/openclaw/openclaw/commits/{sha}/branches-where-head',
        headers={'Accept': 'application/vnd.github+json',
                 'Authorization': 'Bearer ' + env['GH_TOKEN'],
                 'X-GitHub-Api-Version': '2022-11-28'})
    with urlopen(request, timeout=30) as response:
        branches = json.load(response)
    if not isinstance(branches, list) or not any(
            isinstance(branch, dict) and isinstance(branch.get('name'), str) and branch['name']
            and isinstance(branch.get('commit'), dict) and branch['commit'].get('sha') == sha
            for branch in branches):
        raise ValueError('source_sha must be a current branch head in openclaw/openclaw')
    with urlopen(FEED, timeout=30) as response:
        floor = stable_floor(response.read())
    if int(version) <= floor:
        raise ValueError(f'version_override must exceed stable CFBundleVersion {floor}')
    print(f'Test CFBundleVersion {version} exceeds stable {floor}; updates remain enabled')


def validate_archive(archive):
    """Reject extraction escapes and symlink parents before handing bytes to ditto."""
    paths, links = set(), set()
    for member in archive.infolist():
        name = member.filename.rstrip('/')
        parts = PurePosixPath(name).parts
        if (not parts or parts[0] != 'OpenClaw.app' or '..' in parts
                or '\\' in name or name != '/'.join(parts) or name in paths):
            raise ValueError('Archive must contain only unique paths inside OpenClaw.app')
        paths.add(name)
        mode = member.external_attr >> 16
        kind = stat.S_IFMT(mode)
        if kind not in (0, stat.S_IFREG, stat.S_IFDIR, stat.S_IFLNK):
            raise ValueError('Archive contains a special file')
        if stat.S_ISLNK(mode):
            links.add(name)
            target = archive.read(member).decode('utf-8')
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), target))
            if (target.startswith('/') or '\\' in target
                    or not resolved.startswith('OpenClaw.app/')):
                raise ValueError('Archive symlink escapes the app')
    for name in paths:
        if any(str(parent) in links for parent in PurePosixPath(name).parents):
            raise ValueError('Archive entry has a symlink parent')


def verify_metadata(app, sha, version):
    """Bind signed inputs to the requested source and existing runtime provenance."""
    with (app / 'Contents/Info.plist').open('rb') as source:
        info = plistlib.load(source)
    expected = {'CFBundleIdentifier': 'ai.openclaw.mac', 'CFBundleVersion': version,
                'OpenClawGitCommit': sha}
    if any(info.get(key) != value for key, value in expected.items()):
        raise ValueError('App identity, source SHA or build version does not match the request')
    # This is data-only admission: never run bundled Bun while signing keys exist.
    runtime = app / 'Contents/Resources/runtime/lib/node_modules/openclaw/dist/build-info.json'
    data = json.loads(runtime.read_text())
    for key, plist_key in [('commit', 'OpenClawGitCommit'), ('version', 'CFBundleShortVersionString'),
                           ('builtAt', 'OpenClawBuildTimestamp'), ('buildId', 'OpenClawRuntimeBuildID')]:
        if not data.get(key) or data[key] != info.get(plist_key):
            raise ValueError('Bundled runtime provenance mismatch: ' + key)


def unpack(archive_path, destination, env):
    """Validate the complete archive before extracting it into a fresh app path."""
    sha, version = inputs(env)
    app = destination / 'OpenClaw.app'
    if app.exists() or app.is_symlink():
        raise ValueError('Refusing to overwrite an existing signing input')
    with zipfile.ZipFile(archive_path) as archive:
        validate_archive(archive)
    subprocess.run(['/usr/bin/ditto', '-x', '-k', str(archive_path), str(destination)], check=True)
    verify_metadata(app, sha, version)


def sign(app, signer, env):
    """Expose the certificate only to trusted signing tools, then remove its keychain."""
    original = shlex.split(subprocess.check_output(
        ['/usr/bin/security', 'list-keychains', '-d', 'user'], text=True))
    with tempfile.TemporaryDirectory(prefix='macos-test-sign-', dir=env['RUNNER_TEMP']) as temp:
        cert, keychain = Path(temp) / 'identity.p12', Path(temp) / 'signing.keychain-db'
        cert.write_bytes(base64.b64decode(env['MACOS_DEVELOPER_ID_P12_BASE64'], validate=True))
        cert.chmod(0o600)
        password = secrets.token_hex(32)
        print('::add-mask::' + password, flush=True)
        # Do not propagate P12/password, Actions credentials, or candidate environment.
        clean = {key: env[key] for key in ('HOME', 'TMPDIR') if key in env}
        clean.update(PATH='/usr/bin:/bin:/usr/sbin:/sbin', SIGN_IDENTITY=IDENTITY,
                     CODESIGN_TIMESTAMP='on', PYTHONDONTWRITEBYTECODE='1')
        created = False
        try:
            def security(*args):
                result = subprocess.run(['/usr/bin/security', *map(str, args)],
                                        env=clean, capture_output=True)
                if result.returncode:
                    # CalledProcessError includes argv, which can contain passwords.
                    raise RuntimeError(f'security {args[0]} failed (exit {result.returncode})')
            security('create-keychain', '-p', password, keychain)
            created = True
            security('set-keychain-settings', '-lut', '3600', keychain)
            security('unlock-keychain', '-p', password, keychain)
            security('import', cert, '-k', keychain, '-P', env['MACOS_DEVELOPER_ID_P12_PASSWORD'],
                     '-T', '/usr/bin/codesign', '-T', '/usr/bin/security')
            security('list-keychains', '-d', 'user', '-s', keychain)
            security('set-key-partition-list', '-S', 'apple-tool:,apple:,codesign:',
                     '-s', '-k', password, keychain)
            identities = subprocess.check_output(
                ['/usr/bin/security', 'find-identity', '-p', 'codesigning', '-v', str(keychain)],
                env=clean, text=True)
            if re.findall(r'"([^"]+)"', identities) != [IDENTITY]:
                raise ValueError('Expected exactly the Foundation Developer ID identity')
            subprocess.run(['/bin/bash', str(signer.resolve()), str(app.resolve())], env=clean, check=True)
            subprocess.run(['/usr/bin/codesign', '--verify', '--deep', '--strict', str(app)],
                           env=clean, check=True)
            metadata = subprocess.check_output(
                ['/usr/bin/codesign', '-dv', '--verbose=4', str(app)],
                env=clean, stderr=subprocess.STDOUT, text=True).splitlines()
            if f'Authority={IDENTITY}' not in metadata or f'TeamIdentifier={TEAM}' not in metadata:
                raise ValueError('Signed app does not have the required Foundation identity')
        finally:
            # Cleanup failure fails the job before any signed artifact upload.
            try:
                if created:
                    security('delete-keychain', keychain)
            finally:
                security('list-keychains', '-d', 'user', '-s', *original)


def manifest(directory, env):
    """Publish only the zip digest and explicit request provenance alongside the app."""
    sha, version = inputs(env)
    archive = directory / 'OpenClaw-native-test.zip'
    digest = hashlib.sha256()
    with archive.open('rb') as source:
        for block in iter(lambda: source.read(1024 * 1024), b''):
            digest.update(block)
    (directory / 'SHA256SUMS').write_text(f'{digest.hexdigest()}  {archive.name}\n')
    (directory / 'source-sha.txt').write_text(sha + '\n')
    (directory / 'build-version.txt').write_text(version + '\n')


def main():
    """Expose only the four artifact-only operations used by this workflow."""
    command, *args = sys.argv[1:]
    if command == 'admit' and not args:
        admit(os.environ)
    elif command == 'unpack' and len(args) == 2:
        unpack(Path(args[0]), Path(args[1]), os.environ)
    elif command == 'sign' and len(args) == 2:
        sign(Path(args[0]), Path(args[1]), os.environ)
    elif command == 'manifest' and len(args) == 1:
        manifest(Path(args[0]), os.environ)
    else:
        raise ValueError('Expected admit, unpack ARCHIVE DIR, sign APP SIGNER, or manifest DIR')


if __name__ == '__main__':
    # Normal runner cancellation must unwind the signing keychain's finally block.
    def terminate(signum, _frame):
        raise SystemExit(128 + signum)
    signal.signal(signal.SIGTERM, terminate)
    main()
