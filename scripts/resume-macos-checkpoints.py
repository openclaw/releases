"""Select exact signed macOS checkpoints before building fresh variants."""
import io
import json
import os
from pathlib import Path
import subprocess
import zipfile


def main():
    e = os.environ
    sha = subprocess.check_output(['git', '-C', 'source', 'rev-parse', 'HEAD'], text=True).strip()
    supported = '--checkpoint-only)' in Path('source/scripts/package-mac-dist.sh').read_text()
    tag = e['RELEASE_TAG']
    variants, plan = [], {}
    discover = (e.get('PREFLIGHT_ONLY') == 'true' and e.get('SMOKE_TEST_ONLY') == 'false'
                and e.get('PRETAG_SOURCE_SHA', '') == '' and e.get('WORKFLOW_REF') == 'refs/heads/main'
                and e.get('IGNORE_CHECKPOINTS') != 'true')

    def api(path):
        return subprocess.check_output(['gh', 'api', f'repos/{e["GITHUB_REPOSITORY"]}/actions/{path}'])

    for variant in ['universal', 'arm64', 'x86_64']:
        suffix = '' if variant == 'universal' else f'-{variant}'
        appcast = f'appcast{suffix}.xml'
        variants.append(dict(variant=variant, build_archs='all' if variant == 'universal' else variant,
                             artifact_suffix=suffix, appcast_name=appcast,
                             feed_url=f'https://raw.githubusercontent.com/openclaw/openclaw/main/{appcast}'))
        if e.get('RESUME_RUN_ID') and e.get('RESUME_VARIANT') in ['all', variant]:
            plan[variant] = dict(runId=e['RESUME_RUN_ID'], attempt=e['RESUME_RUN_ATTEMPT'],
                                 prefix='macos-notarization')
        if variant in plan or not discover:
            continue
        name = f'macos-resume-{tag}-{variant}-{sha}'
        artifacts = json.loads(api(f'artifacts?name={name}&per_page=100'))['artifacts']
        candidates = sorted((a for a in artifacts if a.get('expired') is False
                             and a.get('workflow_run', {}).get('head_branch') == 'main'),
                            key=lambda a: a['created_at'], reverse=True)
        for candidate in candidates:
            run_id = candidate['workflow_run']['id']
            run = json.loads(api(f'runs/{run_id}'))
            expected = dict(path='.github/workflows/openclaw-macos-publish.yml', event='workflow_dispatch',
                            head_branch='main', status='completed')
            if (any(run.get(key) != value for key, value in expected.items())
                    or run.get('conclusion') not in ['failure', 'cancelled']):
                continue
            archive = api(f'artifacts/{candidate["id"]}/zip')
            try:
                with zipfile.ZipFile(io.BytesIO(archive)) as index:
                    data = json.loads(index.read('resume.json'))
            except (zipfile.BadZipFile, KeyError, ValueError):
                continue
            if not isinstance(data, dict):
                continue
            prefix, attempt = data.get('artifactPrefix'), data.get('producerRunAttempt')
            expected = dict(schemaVersion=1, releaseTag=tag, variant=variant, sourceSha=sha,
                            producerRunId=run_id)
            if (any(data.get(key) != value for key, value in expected.items())
                    or type(data.get('schemaVersion')) is not int
                    or type(data.get('producerRunId')) is not int
                    or type(attempt) is not int or attempt < 1
                    or prefix not in ['macos-signed', 'macos-notarization']):
                continue
            checkpoint = f'{prefix}-{tag}{suffix}-{run_id}-{attempt}'
            if data.get('checkpointArtifact') != checkpoint:
                continue
            retained = json.loads(api(f'runs/{run_id}/artifacts?name={checkpoint}'))['artifacts']
            if not any(a.get('name') == checkpoint and a.get('expired') is False for a in retained):
                continue
            plan[variant] = dict(runId=str(run_id), attempt=str(attempt), prefix=prefix)
            print(f'Resuming {variant} from run {run_id} attempt {attempt} ({checkpoint})')
            break
        if variant not in plan:
            print(f'Building {variant}: no resumable checkpoint for {tag} at {sha}')

    fresh = [v for v in variants if v['variant'] not in plan]
    with open(e['GITHUB_OUTPUT'], 'a') as output:
        output.write(f'sha={sha}\nsupported={str(supported).lower()}\n')
        output.write(f'build_matrix={json.dumps({"include": fresh})}\n')
        output.write(f'package_matrix={json.dumps({"include": variants})}\n')
        output.write(f'build_needed={str(bool(fresh)).lower()}\nresume_plan={json.dumps(plan)}\n')


if __name__ == '__main__':
    main()
