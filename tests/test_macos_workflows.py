"""Exercise macOS release workflow failure propagation without Apple services."""
import json
import os
import plistlib
from itertools import product
from pathlib import Path
import re
import subprocess
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def workflow(name):
    return (ROOT / '.github/workflows' / name).read_text()


def step_source(source, name):
    return source.split(f'      - name: {name}\n', 1)[1].split('\n      - name:', 1)[0]


def step_script(source, name):
    step = step_source(source, name)
    script = step.split('        run: |\n', 1)[1]
    return '\n'.join(line[10:] for line in script.splitlines()) + '\n'


def render_expressions(value, context):
    return re.sub(r'\$\{\{ (.*?) \}\}', lambda match: context[match[1]], value)


def step_environment(source, name, context):
    header = step_source(source, name).split('        run:', 1)[0]
    return {key: render_expressions(value, context)
            for key, value in re.findall(r'^          ([A-Z_]+): (.*)$', header, re.MULTILINE)}


class MacOSWorkflowTests(unittest.TestCase):
    def test_capture_provenance_uses_each_variant_step_environment(self):
        source = workflow('openclaw-macos-publish.yml')
        name = 'Capture release provenance'
        for variant in ['universal', 'arm64', 'x86_64']:
            with self.subTest(variant=variant), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                subprocess.run(['git', 'init', '-q', 'source'], cwd=root, check=True)
                subprocess.run(['git', '-C', 'source', '-c', 'user.name=Test',
                                '-c', 'user.email=test@example.invalid',
                                '-c', 'commit.gpgsign=false', 'commit', '--allow-empty',
                                '-qm', 'fixture'], cwd=root, check=True)
                source_sha = subprocess.check_output(
                    ['git', '-C', 'source', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
                output = root / 'output'
                env = {key: value for key, value in os.environ.items()
                       if key not in ['ARTIFACT_VARIANT', 'RELEASE_TAG']}
                env.update(RUNNER_TEMP=td, GITHUB_OUTPUT=str(output))
                env.update(step_environment(source, name, {
                    'inputs.tag': 'v2026.8.2', 'matrix.variant': variant}))
                result = subprocess.run(['/bin/bash', '-e', '-o', 'pipefail', '-c',
                                         step_script(source, name)], cwd=root, env=env,
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                artifact_dir = root / 'openclaw-macos-preflight'
                self.assertEqual({path.name: path.read_text() for path in artifact_dir.iterdir()}, {
                    f'release-tag-{variant}.txt': 'v2026.8.2\n',
                    f'release-sha-{variant}.txt': f'{source_sha}\n',
                })
                self.assertEqual(output.read_text(), f'dir={artifact_dir}\n')

    def test_generated_appcast_keeps_bytes_and_variant_name(self):
        source = workflow('openclaw-macos-publish.yml')
        name = 'Generate signed appcast artifact'
        for variant, suffix in [('universal', ''), ('arm64', '-arm64'),
                                ('x86_64', '-x86_64')]:
            for fail in [False, True]:
                with self.subTest(variant=variant, fail=fail), tempfile.TemporaryDirectory() as td:
                    root = Path(td)
                    scripts = root / 'scripts'
                    scripts.mkdir()
                    generator = scripts / 'make_appcast.sh'
                    generator.write_text('''#!/bin/bash
set -euo pipefail
printf '%s\\n' "$@" "$SPARKLE_DOWNLOAD_URL_PREFIX" "$SPARKLE_RELEASE_VERSION" > calls
if [[ "$FAIL_GENERATOR" == 1 ]]; then exit 31; fi
printf '%s\\n' '<rss>fixture signed enclosure</rss>' > appcast.xml
''')
                    generator.chmod(0o755)
                    appcast_name = f'appcast{suffix}.xml'
                    feed_url = f'https://raw.githubusercontent.com/openclaw/openclaw/main/{appcast_name}'
                    context = {'inputs.tag': 'v2026.8.2',
                               'steps.package_version.outputs.value': '2026.8.2',
                               'matrix.artifact_suffix': suffix, 'matrix.feed_url': feed_url,
                               'matrix.appcast_name': appcast_name}
                    env = dict(os.environ, FAIL_GENERATOR='1' if fail else '0')
                    env.update(step_environment(source, name, context))
                    result = subprocess.run(['/bin/bash', '-e', '-o', 'pipefail', '-c',
                                             render_expressions(step_script(source, name), context)],
                                            cwd=root, env=env, capture_output=True, text=True)
                    self.assertEqual(result.returncode, 31 if fail else 0, result.stderr)
                    self.assertEqual((root / 'calls').read_text().splitlines(), [
                        f'dist/OpenClaw-2026.8.2{suffix}.zip', feed_url,
                        'https://github.com/openclaw/openclaw/releases/download/v2026.8.2/',
                        '2026.8.2',
                    ])
                    self.assertEqual(sorted(path.name for path in root.glob('appcast*.xml')),
                                     [] if fail else [appcast_name])
                    if not fail:
                        self.assertEqual((root / appcast_name).read_bytes(),
                                         b'<rss>fixture signed enclosure</rss>\n')

    def test_variant_collector_requires_all_assets_and_matching_provenance(self):
        script = step_script(workflow('openclaw-macos-publish.yml'),
                             'Verify complete macOS artifact set')
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            collected = root / 'collected-artifacts'
            collected.mkdir()
            version = '2026.8.2'
            source_sha = 'a' * 40
            for variant, suffix in [('universal', ''), ('arm64', '-arm64'),
                                    ('x86_64', '-x86_64')]:
                for extension in ['zip', 'dmg', 'dSYM.zip']:
                    (collected / f'OpenClaw-{version}{suffix}.{extension}').touch()
                (collected / f'release-tag-{variant}.txt').write_text(f'v{version}\n')
                (collected / f'release-sha-{variant}.txt').write_text(f'{source_sha}\n')
            result = subprocess.run(['bash', '-c', script], cwd=root,
                                    env=dict(os.environ, RELEASE_TAG=f'v{version}'),
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((collected / 'release-sha.txt').read_text(), f'{source_sha}\n')
            (collected / 'release-sha-x86_64.txt').write_text(f'{"b" * 40}\n')
            mismatch = subprocess.run(['bash', '-c', script], cwd=root,
                                      env=dict(os.environ, RELEASE_TAG=f'v{version}'),
                                      capture_output=True, text=True)
            self.assertNotEqual(mismatch.returncode, 0)
            self.assertIn('built from different source commits', mismatch.stderr)
            (collected / f'OpenClaw-{version}-x86_64.zip').unlink()
            partial = subprocess.run(['/bin/bash', '-c', script], cwd=root,
                                     env=dict(os.environ, RELEASE_TAG=f'v{version}'),
                                     capture_output=True, text=True)
            self.assertNotEqual(partial.returncode, 0)
            self.assertIn('Missing macOS artifact variant:', partial.stderr)

    def test_release_build_is_owned_by_validation_before_metadata_and_skipped_on_resume(self):
        publish = workflow('openclaw-macos-publish.yml')
        phase = publish.split('      - name: Release packaging guards\n', 1)[1].split('      - name: Capture release provenance\n', 1)[0]
        steps = phase.split('      - name: ')[1:]
        for resume, fail, expected in [('', False, ['release:check', 'release:openclaw:npm:check']),
                                        ('', True, ['release:check']), ('123', False, [])]:
            with self.subTest(resume=resume, fail=fail), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                pnpm = root / 'pnpm'
                pnpm.write_text('''#!/usr/bin/env python3
import json, os, pathlib, sys
command = sys.argv[1]
with open('calls', 'a') as calls:
    calls.write(json.dumps({'command': command, 'heap': os.environ.get('NODE_OPTIONS')}) + '\\n')
if command in ('build', 'release:check'):
    if command == 'release:check' and os.environ['FAIL_BUILD'] == '1':
        sys.exit(23)
    pathlib.Path('dist/control-ui').mkdir(parents=True, exist_ok=True)
    pathlib.Path('dist/control-ui/index.html').write_text('built')
if command == 'release:openclaw:npm:check' and not pathlib.Path('dist/control-ui/index.html').exists():
    sys.exit(24)
''')
                pnpm.chmod(0o755)
                git = root / 'git'
                git.write_text('#!/bin/sh\nif [ "$1" = rev-parse ]; then printf "%040d\\n" 1; fi\n')
                git.chmod(0o755)
                result_code = 0
                for step in steps:
                    self.assertIn(
                        "if: ${{ steps.recovery_request.outputs.run_id == '' }}",
                        step,
                    )
                    if resume:
                        continue
                    run = step.split('        run: ', 1)[1]
                    script = ('\n'.join(line[10:] for line in run.splitlines()[1:])
                              if run.startswith('|\n') else run.splitlines()[0])
                    heap = re.search(r'NODE_OPTIONS: (.+)', step)
                    result = subprocess.run(['bash', '-c', script], cwd=root, capture_output=True, text=True,
                                            env=dict(os.environ, PATH=f'{root}:{os.environ["PATH"]}',
                                                     NODE_OPTIONS=heap.group(1) if heap else '',
                                                     FAIL_BUILD='1' if fail else '0', RELEASE_TAG='v2026.8.2',
                                                     PUBLIC_RELEASE_BRANCH='release/2026.8.2', RUNNER_TEMP=td,
                                                     ALLOW_LATE_CALVER_RECOVERY='false'))
                    result_code = result.returncode
                    if result_code:
                        break
                calls = [json.loads(line) for line in (root / 'calls').read_text().splitlines()] if (root / 'calls').exists() else []
                self.assertEqual([call['command'] for call in calls], expected)
                self.assertEqual(result_code, 23 if fail else 0)
                if calls:
                    self.assertEqual(calls[0]['heap'], '--max-old-space-size=8192')

    def test_appcast_retention_and_promotion_reject_stale_or_mismatched_artifacts(self):
        build, promote = workflow('openclaw-macos-publish.yml').split('  promote_release_artifacts:', 1)
        cases = [({}, True), ({'version': '2026.8.1'}, False),
                 ({'build': '202608010'}, False), ({'url_tag': 'v2026.8.1'}, False),
                 ({'length': '1'}, False), ({'signature': ''}, False),
                 ({'bundle_version': '2026.8.1'}, False)]
        for stage, source, directory in [('retention', build, 'source'), ('promotion', promote, 'promoted-appcast')]:
            script = step_script(source, 'Resolve appcast path')
            for changes, accepted in cases:
                with self.subTest(stage=stage, changes=changes), tempfile.TemporaryDirectory() as td:
                    root = Path(td)
                    (root / directory).mkdir()
                    (root / 'release-tools').symlink_to(ROOT, target_is_directory=True)
                    values = dict(version='2026.8.2', build='202608020', url_tag='v2026.8.2',
                                  signature='fixture-signature', bundle_version='2026.8.2') | changes
                    variants = [('universal', '', 'appcast.xml')]
                    if stage == 'promotion':
                        variants += [('arm64', '-arm64', 'appcast-arm64.xml'),
                                     ('x86_64', '-x86_64', 'appcast-x86_64.xml')]
                    packages = {}
                    for variant, suffix, appcast_name in variants:
                        package = root / f'OpenClaw-2026.8.2{suffix}.zip'
                        feed = f'https://raw.githubusercontent.com/openclaw/openclaw/main/{appcast_name}'
                        with zipfile.ZipFile(package, 'w') as archive:
                            archive.writestr('OpenClaw.app/Contents/Info.plist', plistlib.dumps({
                                'CFBundleShortVersionString': values['bundle_version'],
                                'CFBundleVersion': '202608020', 'SUFeedURL': feed}))
                        length = values.get('length', str(package.stat().st_size))
                        (root / directory / appcast_name).write_text(f'''<rss xmlns:sparkle="http://www.andymatuschak.org/xml-namespaces/sparkle"><channel><item>
                            <sparkle:shortVersionString>{values['version']}</sparkle:shortVersionString>
                            <sparkle:version>{values['build']}</sparkle:version>
                            <enclosure url="https://github.com/openclaw/openclaw/releases/download/{values['url_tag']}/{package.name}"
                              length="{length}" sparkle:edSignature="{values['signature']}"/>
                            </item></channel></rss>''')
                        packages[variant] = package
                    package = packages['universal']
                    env = dict(os.environ, RELEASE_TAG='v2026.8.2',
                               OPENCLAW_REPOSITORY='openclaw/openclaw', ZIP_PATH=str(package),
                               APPCAST_NAME='appcast.xml', ARTIFACT_VARIANT='universal',
                               UNIVERSAL_ZIP=str(packages['universal']),
                               ARM64_ZIP=str(packages.get('arm64', package)),
                               X86_64_ZIP=str(packages.get('x86_64', package)),
                               GITHUB_OUTPUT=str(root / 'output'))
                    result = subprocess.run(['bash', '-c', script], cwd=root,
                                            env=env,
                                            capture_output=True, text=True)
                    self.assertEqual(result.returncode == 0, accepted, result.stderr)
                    self.assertEqual((root / 'output').exists(), accepted)

    def test_notarization_recovery_requires_main_signed_preflight_and_exact_attempt(self):
        script = step_script(workflow('openclaw-macos-publish.yml'), 'Validate notarization recovery inputs')
        valid = dict(RESUME_RUN_ID='123', RESUME_RUN_ATTEMPT='2', PREFLIGHT_ONLY='true',
                     SMOKE_TEST_ONLY='false', WORKFLOW_REF='refs/heads/main', RESUME_VARIANT='universal')
        for changes, accepted in [({}, True), ({'RESUME_RUN_ID': ''}, False),
                                  ({'RESUME_RUN_ATTEMPT': ''}, False),
                                  ({'RESUME_RUN_ATTEMPT': '0'}, False),
                                  ({'RESUME_RUN_ID': '../123'}, False),
                                  ({'PREFLIGHT_ONLY': 'false'}, False),
                                  ({'SMOKE_TEST_ONLY': 'true'}, False),
                                  ({'WORKFLOW_REF': 'refs/heads/feature'}, False),
                                  ({'RESUME_VARIANT': 'arm64'}, True),
                                  ({'RESUME_VARIANT': 'x86_64'}, True),
                                  ({'RESUME_VARIANT': 'all'}, True),
                                  ({'RESUME_VARIANT': '../arm64'}, False),
                                  ({'RESUME_RUN_ID': '', 'RESUME_RUN_ATTEMPT': '',
                                    'RESUME_VARIANT': 'all'}, False),
                                  ({'RESUME_RUN_ID': '', 'RESUME_RUN_ATTEMPT': ''}, True)]:
            with self.subTest(changes=changes):
                result = subprocess.run(['bash', '-c', script], env=dict(os.environ, **(valid | changes)),
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode == 0, accepted, result.stderr)

    def test_recovery_rejects_wrong_workflow_attempt_or_successful_producer(self):
        script = step_script(workflow('openclaw-macos-publish.yml'), 'Verify notarization checkpoint producer')
        producer = dict(id=123, run_attempt=2, path='.github/workflows/openclaw-macos-publish.yml',
                        head_branch='main', head_sha='a' * 40, event='workflow_dispatch',
                        status='completed', conclusion='failure', repository={'full_name': 'openclaw/releases'})
        for changes, accepted in [({}, True), ({'conclusion': 'cancelled'}, True),
                                  ({'conclusion': 'success'}, False), ({'run_attempt': 1}, False),
                                  ({'head_branch': 'feature'}, False), ({'path': 'untrusted.yml'}, False),
                                  ({'repository': {'full_name': 'other/releases'}}, False),
                                  ({'status': 'in_progress'}, False), ({'id': 456}, False),
                                  ({'event': 'pull_request'}, False)]:
            with self.subTest(changes=changes), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                gh = root / 'gh'
                gh.write_text('#!/usr/bin/env python3\nimport os\nprint(os.environ["PRODUCER"])\n')
                gh.chmod(0o755)
                env = dict(os.environ, PATH=f'{root}:{os.environ["PATH"]}', RUNNER_TEMP=td,
                           GITHUB_REPOSITORY='openclaw/releases', RESUME_RUN_ID='123',
                           RESUME_RUN_ATTEMPT='2', PRODUCER=json.dumps(producer | changes))
                result = subprocess.run(['bash', '-c', script], env=env, capture_output=True, text=True)
                self.assertEqual(result.returncode == 0, accepted, result.stderr)

    def test_recovery_calls_resume_without_reentering_build_steps(self):
        publish = workflow('openclaw-macos-publish.yml')
        selection = 'Select notarization recovery checkpoint'
        packaging = 'Build, sign, notarize, and package macOS release'
        option = re.split(r'\n      \S', publish.split('      resume_notarization_variant:\n', 1)[1], maxsplit=1)[0]
        self.assertIn('default: universal', option)
        for selector, variant, run_id in product(['universal', 'arm64', 'x86_64', 'all'],
                                                 ['universal', 'arm64', 'x86_64'], ['', '123']):
            with self.subTest(selector=selector, variant=variant, run_id=run_id), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                output = root / 'selection'
                context = {'inputs.resume_notarization_run_id': run_id,
                           'inputs.resume_notarization_variant': selector, 'matrix.variant': variant}
                env = dict(os.environ, GITHUB_OUTPUT=str(output))
                env.update(step_environment(publish, selection, context))
                selected = subprocess.run(['/bin/bash', '-e', '-o', 'pipefail', '-c',
                                           step_script(publish, selection)], cwd=root, env=env,
                                          capture_output=True, text=True)
                self.assertEqual(selected.returncode, 0, selected.stderr)
                effective_run = run_id if selector in ['all', variant] else ''
                self.assertEqual(output.read_text(), f'run_id={effective_run}\n')
                (root / 'scripts').mkdir()
                package = root / 'scripts/package-mac-dist.sh'
                package.write_text('''#!/usr/bin/env python3
import json, os, pathlib, sys
pathlib.Path('packager-called').write_text(json.dumps(sys.argv[1:]))
sys.exit(int(os.environ['PACKAGE_EXIT']))
''')
                package.chmod(0o755)
                suffix = '' if variant == 'universal' else f'-{variant}'
                context.update({'steps.recovery_request.outputs.run_id': effective_run,
                                'steps.package_version.outputs.value': '2026.8.2',
                                'matrix.build_archs': 'all' if variant == 'universal' else variant,
                                'env.SIGN_IDENTITY': 'fixture-only',
                                'matrix.feed_url': f'https://example.invalid/appcast{suffix}.xml'})
                env.update(step_environment(publish, packaging, context))
                for status in ['0', '17']:
                    result = subprocess.run(['/bin/bash', '-e', '-o', 'pipefail', '-c',
                                             step_script(publish, packaging)], cwd=root,
                                            env=env | {'PACKAGE_EXIT': status}, capture_output=True, text=True)
                    self.assertEqual(result.returncode, int(status), result.stderr)
                    self.assertEqual(json.loads((root / 'packager-called').read_text()),
                                     ['--resume-notarization'] if effective_run else [])
        # Job scheduling is itself the contract: a resume must never install or compile.
        for name in ['Checkout submodules (retry)', 'Setup pnpm', 'Install dependencies',
                     'Prepare Apple Mermaid assets',
                     'Cache SwiftPM', 'Release packaging guards', 'Build and verify release contents',
                     'Validate release tag and package metadata']:
            self.assertIn("if: ${{ steps.recovery_request.outputs.run_id == '' }}",
                          step_source(publish, name))
        for name in ['Verify notarization checkpoint producer', 'Download notarization checkpoint',
                     'Verify notarization checkpoint release binding', 'Restore checkpointed Sparkle tools']:
            step = step_source(publish, name)
            self.assertIn("if: ${{ steps.recovery_request.outputs.run_id != '' }}", step)
            self.assertNotIn('continue-on-error', step)
        self.assertIn("(steps.recovery_request.outputs.run_id == '' || steps.recovery_verified.outcome == 'success')",
                      step_source(publish, 'Preserve notarization recovery checkpoint'))
        self.assertIn('environment: mac-release', publish.split('  build_sign_and_package:', 1)[1])

    def test_recovery_artifact_names_match_existing_variant_checkpoints(self):
        publish = workflow('openclaw-macos-publish.yml')
        for variant, suffix in [('universal', ''), ('arm64', '-arm64'), ('x86_64', '-x86_64')]:
            with self.subTest(variant=variant):
                context = {'inputs.tag': 'v2026.8.2', 'matrix.artifact_suffix': suffix,
                           'steps.recovery_request.outputs.run_id': '123',
                           'inputs.resume_notarization_run_attempt': '2',
                           'github.run_id': '123', 'github.run_attempt': '2'}
                for step in ['Download notarization checkpoint', 'Upload notarization recovery checkpoint']:
                    name = re.search(r'^          name: (.+)$', step_source(publish, step), re.MULTILINE)[1]
                    self.assertEqual(render_expressions(name, context),
                                     f'macos-notarization-v2026.8.2{suffix}-123-2')
        download = step_source(publish, 'Download notarization checkpoint')
        self.assertIn('run-id: ${{ steps.recovery_request.outputs.run_id }}', download)
        self.assertNotIn('pattern:', download)

    def test_checkpoint_binding_fails_before_packager_for_wrong_release_or_source(self):
        script = step_script(workflow('openclaw-macos-publish.yml'), 'Verify notarization checkpoint release binding')
        source_sha = 'b' * 40
        producer = dict(id=123, run_attempt=2, head_sha='a' * 40)
        envelope = dict(releaseTag='v2026.8.2', sourceSha=source_sha, producerRunId=123,
                        producerRunAttempt=2, producerWorkflowSha='a' * 40,
                        preflightOnly=True, smokeTestOnly=False)
        manifest = dict(schemaVersion=1, sourceSha=source_sha, version='2026.8.2',
                        skipDmg=False, skipDsym=False)
        cases = [({}, {}, '', True), ({'releaseTag': 'v2026.8.1'}, {}, '', False),
                 ({'producerRunId': 456}, {}, '', False), ({'producerRunAttempt': 1}, {}, '', False),
                 ({'producerWorkflowSha': 'c' * 40}, {}, '', False),
                 ({'smokeTestOnly': True}, {}, '', False), ({}, {'sourceSha': 'c' * 40}, '', False),
                 ({}, {'version': '2026.8.1'}, '', False), ({}, {'skipDmg': True}, '', False),
                 ({}, {}, 'wrong-feed', False), ({}, {}, 'missing-plist', False),
                 ({}, {}, 'missing-checkpoint', False), ({}, {}, 'missing-app', False),
                 ({}, {}, 'hash-rejection', False)]
        for variant, (envelope_changes, manifest_changes, failure, accepted) in product(
                ['universal', 'arm64', 'x86_64'], cases):
            with self.subTest(variant=variant, envelope=envelope_changes, manifest=manifest_changes,
                              failure=failure), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                (root / 'scripts/lib').mkdir(parents=True)
                package = root / 'scripts/package-mac-dist.sh'
                package.write_text('#!/bin/sh\n# --resume-notarization\ntouch packager-called\n')
                package.chmod(0o755)
                # The core helper owns SHA-256 verification. Its rejection must
                # propagate before the workflow reads metadata or calls packaging.
                (root / 'scripts/lib/mac-notarization-recovery.py').write_text('''import os, pathlib, sys
pathlib.Path('verified').touch()
sys.exit(19 if os.environ['FAIL_CHECKPOINT_HASH'] == '1' else 0)
''')
                (root / 'package.json').write_text(json.dumps({'version': '2026.8.2'}))
                checkpoint = root / 'dist/macos-notarization-recovery'
                checkpoint.mkdir(parents=True)
                # Keep the existing envelope format, including universal checkpoints
                # produced before variant selection; no new variant field is required.
                (checkpoint / 'workflow-release.json').write_text(json.dumps(envelope | envelope_changes))
                if failure != 'missing-checkpoint':
                    (checkpoint / 'manifest.json').write_text(json.dumps(manifest | manifest_changes))
                suffix = '' if variant == 'universal' else f'-{variant}'
                feed = f'https://raw.githubusercontent.com/openclaw/openclaw/main/appcast{suffix}.xml'
                if failure != 'missing-app':
                    with zipfile.ZipFile(checkpoint / 'app.zip', 'w') as archive:
                        if failure != 'missing-plist':
                            archive.writestr('OpenClaw.app/Contents/Info.plist', plistlib.dumps({
                                'SUFeedURL': 'https://example.invalid/wrong-feed.xml' if failure == 'wrong-feed' else feed,
                            }))
                (checkpoint / 'app-submission.json').write_text(json.dumps({
                    'submissionId': '11111111-2222-4333-8444-555555555555'}))
                before = {path.name: path.read_bytes() for path in checkpoint.iterdir()}
                (root / 'notarization-producer.json').write_text(json.dumps(producer))
                git = root / 'git'
                git.write_text(f'#!/bin/sh\nif [ "$1" = rev-parse ]; then echo {source_sha}; fi\n')
                git.chmod(0o755)
                result = subprocess.run(['/bin/bash', '-e', '-o', 'pipefail', '-c',
                                         script + '\nscripts/package-mac-dist.sh --resume-notarization\n'], cwd=root,
                                        env=dict(os.environ, PATH=f'{root}:{os.environ["PATH"]}',
                                                 RUNNER_TEMP=td, RELEASE_TAG='v2026.8.2',
                                                 EXPECTED_FEED_URL=feed,
                                                 FAIL_CHECKPOINT_HASH='1' if failure == 'hash-rejection' else '0',
                                                 PUBLIC_RELEASE_BRANCH='release/2026.8.2'),
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode == 0, accepted, result.stderr)
                self.assertEqual((root / 'packager-called').exists(), accepted)
                self.assertEqual({path.name: path.read_bytes() for path in checkpoint.iterdir()}, before)
                if accepted:
                    self.assertTrue((root / 'verified').exists())

    def test_complete_isolated_suite_and_failure_propagation(self):
        script = step_script(workflow('openclaw-macos-validate.yml'), 'Swift test')
        # A failed build, failed profile, or timed-out profile must never upload
        # successful validation proof or proceed to later test profiles.
        for failed_phase, exit_code, expected in [
            ('', 0, ['build', 'default', 'named']),
            ('build', 1, ['build']),
            ('default', 124, ['build', 'default']),
            ('named', 1, ['build', 'default', 'named']),
        ]:
            with self.subTest(failed_phase=failed_phase), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                stub = '#!/usr/bin/env python3\n' + (
                    'import json,os,sys\n'
                    'phase="build" if sys.argv[0].endswith("swift") else sys.argv[2]\n'
                    'with open(os.environ["CALLS"],"a") as f: f.write(json.dumps({"phase":phase,"args":sys.argv[1:]})+"\\n")\n'
                    'sys.exit(int(os.environ["FAIL_CODE"]) if phase==os.environ["FAIL_PHASE"] else 0)\n'
                )
                for binary in ['swift', 'node']:
                    path = root / binary
                    path.write_text(stub)
                    path.chmod(0o755)
                env = dict(os.environ, PATH=f'{root}:{os.environ["PATH"]}',
                           CALLS=str(root / 'calls'), FAIL_PHASE=failed_phase, FAIL_CODE=str(exit_code))
                result = subprocess.run(['bash', '-c', script], env=env, capture_output=True, text=True)
                self.assertEqual(result.returncode, exit_code, result.stderr)
                calls = [json.loads(line) for line in (root / 'calls').read_text().splitlines()]
                self.assertEqual([call['phase'] for call in calls], expected)
                for call in calls[1:]:
                    self.assertEqual(call['args'][0], 'scripts/test-macos-native.mts')
                    self.assertIn('--skip-build', call['args'])
                    self.assertIn('--no-parallel', call['args'])
                if len(calls) == 3:
                    self.assertEqual(calls[1]['args'][-2], '--skip')
                    self.assertEqual(calls[2]['args'][-2], '--filter')
                    # Launch profile is immutable: each fixture must run exactly once
                    # in the process that owns its defaults and lifecycle semantics.
                    for test, profile in [
                        ('AppStateIsolationTests/previewConstructor', 'named'),
                        ('ProfileChatPreferencesTests/testFullChatPreferencesBelongToNamedProfile', 'named'),
                        ('QuickChatCatalogPresentationTests/testRenderedPicker', 'default'),
                        ('WebChatModelPickerTests/testModelPicker', 'default'),
                    ]:
                        selected = [call['phase'] for call in calls[1:]
                                    if bool(re.search(call['args'][-1], test)) == (call['phase'] == 'named')]
                        self.assertEqual(selected, [profile], test)

    def test_preparation_needs_tag_but_release_page_only_for_promotion(self):
        publish = workflow('openclaw-macos-publish.yml')
        validate = workflow('openclaw-macos-validate.yml')
        build, promote = publish.split('  promote_release_artifacts:', 1)
        for preparation in [build, validate]:
            self.assertNotIn('gh release view', preparation)
            clone = step_script(preparation, 'Clone selected public source')
            self.assertIn('git -C source rev-parse --verify "refs/tags/${RELEASE_TAG}^{commit}"', clone)
        self.assertIn('gh release view', promote)
        self.assertIn('environment: mac-release', build)
        self.assertIn('environment: mac-release', promote)
        self.assertIn('if: ${{ !inputs.preflight_only && !inputs.smoke_test_only }}', promote)


if __name__ == '__main__':
    unittest.main()
