"""Report the real source-packager boundary without printing signing arguments."""
import argparse
import os
from pathlib import Path
import subprocess
import time

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('mode', choices=['checkpoint', 'package', 'resume'])
args = parser.parse_args()
phase, options = {
    'checkpoint': ('build and sign checkpoint; no Apple submission', ['--checkpoint-only']),
    'package': ('legacy build, sign, notarize and package', []),
    'resume': ('resume notarization and package; no compilation', ['--resume-notarization']),
}[args.mode]
if os.environ.get('SKIP_NOTARIZE') == '1' and args.mode != 'checkpoint':
    phase = ('legacy build, ad-hoc sign and package; no Apple submission' if args.mode == 'package'
             else 'package smoke checkpoint; no Apple submission or compilation')
arch = {'all': 'universal', 'arm64': 'arm64', 'x86_64': 'x86_64'}[os.environ['BUILD_ARCHS']]
started = time.monotonic()


def report(status):
    message = f'macOS {arch}: {phase}: {status} ({int(time.monotonic() - started)}s elapsed)'
    print(message, flush=True)
    # Append at start as well: runner cancellation can prevent the final report.
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        try:
            with Path(os.environ['GITHUB_STEP_SUMMARY']).open('a') as summary:
                summary.write(f'- {message}\n')
        except OSError:
            print('::warning::Unable to append macOS phase to the job summary.', flush=True)


report('started')
result = subprocess.run(['scripts/package-mac-dist.sh', *options])
report('completed' if result.returncode == 0 else f'failed (exit {result.returncode})')
raise SystemExit(result.returncode if result.returncode >= 0 else 128 - result.returncode)
