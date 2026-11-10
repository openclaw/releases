"""Test test-build admission and workflow boundaries without signing credentials."""
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import plistlib
import stat
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('macos_test_build', ROOT / 'scripts/macos-test-build.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)
WORKFLOW = (ROOT / '.github/workflows/openclaw-macos-test-build.yml').read_text()
ENV = dict(GITHUB_REPOSITORY='openclaw/releases', GITHUB_REF='refs/heads/main',
           GITHUB_EVENT_NAME='workflow_dispatch', SOURCE_SHA='a' * 40, VERSION_OVERRIDE='2611000191')
FEED = b'<rss xmlns:sparkle="http://www.andymatuschak.org/xml-namespaces/sparkle"><channel><item><sparkle:version>2611000190</sparkle:version><enclosure url="https://example.invalid/app.zip" /></item><item><sparkle:version>2610001090</sparkle:version><enclosure /></item></channel></rss>'


class TestBuildTests(unittest.TestCase):
    def test_inputs_and_stable_floor_fail_closed(self):
        self.assertEqual(build.stable_floor(FEED), 2611000190)
        with patch.object(build, 'urlopen', return_value=io.BytesIO(FEED)):
            build.admit(ENV)
        for update in [dict(SOURCE_SHA='main'), dict(SOURCE_SHA='a' * 39),
                       dict(SOURCE_SHA='a' * 40 + '\n'), dict(SOURCE_SHA='$(echo unsafe)'),
                       dict(VERSION_OVERRIDE='2026.11.1'), dict(VERSION_OVERRIDE='0'),
                       dict(VERSION_OVERRIDE='01'), dict(VERSION_OVERRIDE='9' * 16),
                       dict(GITHUB_REF='refs/heads/topic'), dict(GITHUB_REPOSITORY='fork/releases'),
                       dict(GITHUB_EVENT_NAME='pull_request')]:
            with self.subTest(update=update), self.assertRaises(ValueError):
                build.inputs(ENV | update)
        for version in ['2611000190', '2611000189']:
            with patch.object(build, 'urlopen', return_value=io.BytesIO(FEED)), self.assertRaises(ValueError):
                build.admit(ENV | dict(VERSION_OVERRIDE=version))
        for feed in [b'<rss/>', FEED.replace(b'2611000190', b''), FEED.replace(b'2611000190', b'latest')]:
            with self.subTest(feed=feed), self.assertRaises(ValueError):
                build.stable_floor(feed)
        with patch.object(build, 'urlopen', side_effect=OSError('offline')), self.assertRaises(OSError):
            build.admit(ENV)

    def archive(self, entries):
        data = io.BytesIO()
        with zipfile.ZipFile(data, 'w') as archive:
            for name, mode, content in entries:
                info = zipfile.ZipInfo(name)
                info.external_attr = mode << 16
                archive.writestr(info, content)
        data.seek(0)
        return zipfile.ZipFile(data)

    def test_archive_admits_framework_links_but_not_escapes(self):
        valid = [('OpenClaw.app/Contents/Frameworks/F.framework/Versions/A/F', stat.S_IFREG, b'fixture'),
                 ('OpenClaw.app/Contents/Frameworks/F.framework/Versions/Current', stat.S_IFLNK, b'A'),
                 ('OpenClaw.app/Contents/Frameworks/F.framework/F', stat.S_IFLNK, b'Versions/Current/F')]
        with self.archive(valid) as archive:
            build.validate_archive(archive)
        invalid = [[('../escape', stat.S_IFREG, b'')],
                   [('/OpenClaw.app/evil', stat.S_IFREG, b'')],
                   [('OpenClaw.app/../escape', stat.S_IFREG, b'')],
                   [('OpenClaw.app/link', stat.S_IFLNK, b'/etc')],
                   [('OpenClaw.app/link', stat.S_IFLNK, b'../../etc')],
                   [('OpenClaw.app/pipe', stat.S_IFIFO, b'')],
                   [('OpenClaw.app/link', stat.S_IFLNK, b'Contents'),
                    ('OpenClaw.app/link/file', stat.S_IFREG, b'')]]
        for entries in invalid:
            with self.subTest(entries=entries), self.archive(entries) as archive, self.assertRaises(ValueError):
                build.validate_archive(archive)

    def fixture_app(self, root):
        app = root / 'OpenClaw.app'
        contents = app / 'Contents'
        contents.mkdir(parents=True)
        info = dict(CFBundleIdentifier='ai.openclaw.mac', CFBundleVersion=ENV['VERSION_OVERRIDE'],
                    CFBundleShortVersionString='2026.11.1', OpenClawGitCommit=ENV['SOURCE_SHA'],
                    OpenClawBuildTimestamp='2026-11-10T19:00:00.000Z', OpenClawRuntimeBuildID='fixture')
        (contents / 'Info.plist').write_bytes(plistlib.dumps(info))
        runtime = contents / 'Resources/runtime/lib/node_modules/openclaw/dist/build-info.json'
        runtime.parent.mkdir(parents=True)
        runtime.write_text(json.dumps(dict(version=info['CFBundleShortVersionString'],
                                          commit=info['OpenClawGitCommit'], builtAt=info['OpenClawBuildTimestamp'],
                                          buildId=info['OpenClawRuntimeBuildID'])))
        return app, info

    def test_metadata_binds_build_and_runtime_before_signing(self):
        with tempfile.TemporaryDirectory() as temp:
            app, info = self.fixture_app(Path(temp))
            build.verify_metadata(app, ENV['SOURCE_SHA'], ENV['VERSION_OVERRIDE'])
            for field in ['CFBundleIdentifier', 'CFBundleVersion', 'OpenClawGitCommit',
                          'CFBundleShortVersionString', 'OpenClawBuildTimestamp', 'OpenClawRuntimeBuildID']:
                (app / 'Contents/Info.plist').write_bytes(plistlib.dumps(info | {field: 'wrong'}))
                with self.subTest(field=field), self.assertRaises(ValueError):
                    build.verify_metadata(app, ENV['SOURCE_SHA'], ENV['VERSION_OVERRIDE'])

    def test_signer_removes_credentials_on_success_and_failure(self):
        for fail, wrong_identity in [(False, False), (True, False), (False, True)]:
            with self.subTest(fail=fail, wrong_identity=wrong_identity), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                app, _ = self.fixture_app(root)
                calls = []

                def run(argv, **kwargs):
                    calls.append(argv)
                    self.assertNotIn('MACOS_DEVELOPER_ID_P12_PASSWORD', kwargs['env'])
                    self.assertNotIn('MACOS_DEVELOPER_ID_P12_BASE64', kwargs['env'])
                    self.assertNotIn('GITHUB_TOKEN', kwargs['env'])
                    if argv[0] == '/bin/bash' and fail:
                        raise subprocess.CalledProcessError(17, argv)
                    return subprocess.CompletedProcess(argv, 0)

                def output(argv, **kwargs):
                    if 'list-keychains' in argv:
                        return '"/original/login.keychain-db"\n'
                    if 'find-identity' in argv:
                        return f'1) abc "{build.IDENTITY if not wrong_identity else "Other"}"\n'
                    return f'Authority={build.IDENTITY}\nTeamIdentifier={build.TEAM}\n'

                env = dict(HOME=temp, RUNNER_TEMP=temp, MACOS_DEVELOPER_ID_P12_BASE64='dGVzdA==',
                           MACOS_DEVELOPER_ID_P12_PASSWORD='fixture-password', GITHUB_TOKEN='fixture-token')
                with patch.object(build.subprocess, 'run', side_effect=run), \
                     patch.object(build.subprocess, 'check_output', side_effect=output), \
                     patch('builtins.print'):
                    if fail or wrong_identity:
                        with self.assertRaises((subprocess.CalledProcessError, ValueError)):
                            build.sign(app, root / 'trusted-signer.sh', env)
                    else:
                        build.sign(app, root / 'trusted-signer.sh', env)
                self.assertTrue(any('delete-keychain' in call for call in calls))
                self.assertEqual(calls[-1], ['/usr/bin/security', 'list-keychains', '-d', 'user',
                                             '-s', '/original/login.keychain-db'])
                self.assertEqual(list(root.glob('macos-test-sign-*')), [])
                if wrong_identity:
                    self.assertFalse(any(call[0] == '/bin/bash' for call in calls))

    def test_manifest_records_exact_bytes_and_inputs(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'OpenClaw-native-test.zip').write_bytes(b'fixture signed zip')
            build.manifest(root, ENV)
            digest = hashlib.sha256(b'fixture signed zip').hexdigest()
            self.assertEqual((root / 'SHA256SUMS').read_text(), f'{digest}  OpenClaw-native-test.zip\n')
            self.assertEqual((root / 'source-sha.txt').read_text(), ENV['SOURCE_SHA'] + '\n')
            self.assertEqual((root / 'build-version.txt').read_text(), ENV['VERSION_OVERRIDE'] + '\n')

    def test_workflow_separates_candidate_execution_from_keys_and_release_paths(self):
        build_job, sign_job = WORKFLOW.split('  sign:\n')
        self.assertNotIn('secrets.', build_job)
        self.assertNotIn('environment: mac-release', build_job)
        self.assertIn('environment: mac-release', sign_job)
        self.assertIn('needs: build', sign_job)
        # Failed-job reruns consume the successful producer's ID, not a new attempt name.
        self.assertIn('unsigned_artifact_id: ${{ steps.unsigned.outputs.artifact-id }}', build_job)
        self.assertIn('id: unsigned', build_job)
        self.assertIn('artifact-ids: ${{ needs.build.outputs.unsigned_artifact_id }}', sign_job)
        self.assertIn('merge-multiple: true', sign_job)
        download = sign_job.split("      - name: Download this run's unsigned app\n")[1].split('      - name:', 1)[0]
        self.assertNotIn('github.run_attempt', download)
        self.assertIn('ref: 0409efbc343c579f3d711f723811c58fa9497f05', sign_job)
        for forbidden in ['release:check', 'release:openclaw:npm:check', 'package-mac-dist.sh',
                          'make_appcast', 'notarytool', 'gh release', 'openclaw-macos-publish.yml',
                          'actions/cache', 'NOTARY', 'SPARKLE_PRIVATE', 'MACOS_PUBLISHER', 'contents: write']:
            self.assertNotIn(forbidden, WORKFLOW)
        self.assertNotIn('      tag:', WORKFLOW)
        for required in ['OPENCLAW_IROH_NATIVE: "1"', 'BUILD_CONFIG: release', 'BUILD_ARCHS: arm64',
                         'BUNDLE_ID: ai.openclaw.mac', 'APP_BUILD: ${{ inputs.version_override }}',
                         'scripts/generate-bindings.sh', 'scripts/build-apple.sh',
                         'scripts/package-mac-app.sh', 'package-manager-cache: false', 'retention-days: 7']:
            self.assertIn(required, build_job if required != 'retention-days: 7' else sign_job)
        self.assertNotIn('package-mac-app.sh', sign_job)
        self.assertLess(sign_job.index('Admit app archive'), sign_job.index('secrets.MACOS_DEVELOPER'))
        self.assertLess(sign_job.index('Sign with Foundation'), sign_job.index('Upload signed test'))
        self.assertEqual(sign_job.count('secrets.'), 2)
        # Syntax-check the actual delivered inline scripts without executing macOS commands.
        import re
        for match in re.finditer(r'        run: \|\n((?:          .*\n|\n)+)', WORKFLOW):
            script = '\n'.join(line[10:] for line in match[1].splitlines())
            subprocess.run(['bash', '-n'], input=script, text=True, check=True)


if __name__ == '__main__':
    unittest.main()
