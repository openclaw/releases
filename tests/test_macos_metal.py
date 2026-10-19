"""A selected Xcode may lack its separately downloaded Metal compiler."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/prepare-macos-metal.sh'


class MetalToolchainTests(unittest.TestCase):
    def run_toolchain(self, available=False, download_fails=False, remains_missing=False):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            ready = root / 'ready'
            if available:
                ready.touch()
            (root / 'xcrun').write_text('#!/bin/bash\necho "xcrun $*" >> "$TRACE"\ntest -f "$READY"\n')
            (root / 'xcodebuild').write_text(
                '#!/bin/bash\necho "xcodebuild $*" >> "$TRACE"\n'
                'if [[ "$DOWNLOAD_FAILS" == 1 ]]; then exit 7; fi\n'
                'if [[ "$REMAINS_MISSING" == 0 ]]; then touch "$READY"; fi\n')
            for tool in ('xcrun', 'xcodebuild'):
                (root / tool).chmod(0o755)
            trace = root / 'trace'
            result = subprocess.run(['/bin/bash', str(SCRIPT)], capture_output=True, text=True,
                                    env=dict(os.environ, PATH=f'{root}:/usr/bin:/bin', READY=str(ready),
                                             TRACE=str(trace), DOWNLOAD_FAILS=str(int(download_fails)),
                                             REMAINS_MISSING=str(int(remains_missing))))
            return result.returncode, trace.read_text().splitlines()

    def test_installed_component_needs_no_download(self):
        code, calls = self.run_toolchain(available=True)
        self.assertEqual(code, 0)
        self.assertNotIn('xcodebuild -downloadComponent MetalToolchain', calls)

    def test_missing_component_is_installed_and_verified(self):
        code, calls = self.run_toolchain()
        self.assertEqual(code, 0)
        self.assertEqual(calls, ['xcrun metal --version',
                                 'xcodebuild -downloadComponent MetalToolchain',
                                 'xcrun metal --version'])

    def test_download_failure_blocks_packaging(self):
        code, calls = self.run_toolchain(download_fails=True)
        self.assertEqual(code, 7)
        self.assertEqual(len(calls), 2)

    def test_unusable_download_still_blocks_packaging(self):
        code, _ = self.run_toolchain(remains_missing=True)
        self.assertNotEqual(code, 0)


if __name__ == '__main__':
    unittest.main()
