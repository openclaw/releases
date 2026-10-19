"""The tagged packager keeps its read-only snapshot and writable staging contracts."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location(
    'image_tool', Path(__file__).resolve().parents[1] / 'scripts/macos27-hdiutil.py')
IMAGE_TOOL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(IMAGE_TOOL)


class ImageToolTests(unittest.TestCase):
    def test_readonly_apfs_snapshot(self):
        result = IMAGE_TOOL.command(['create', '-fs', 'APFS', '-format', 'UDRO',
                                     '-srcfolder', '/source with spaces', '-volname', 'Snapshot',
                                     '/output with spaces.dmg'])
        self.assertEqual(result, ['/usr/sbin/diskutil', 'image', 'create', 'from',
                                  '--format', 'UDRO', '--volumeName', 'Snapshot',
                                  '/source with spaces', '/output with spaces.dmg'])

    def test_writable_staging_and_explicit_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'staging.dmg'
            output.write_text('old image')
            arguments = ['create', '-volname', 'Stage', '-srcfolder', '/source',
                         '-format', 'UDRW', str(output)]
            with self.assertRaises(FileExistsError):
                IMAGE_TOOL.command(arguments)
            self.assertEqual(output.read_text(), 'old image')
            result = IMAGE_TOOL.command([*arguments, '-ov'])
            self.assertEqual(result[:6], ['/usr/sbin/diskutil', 'image', 'create', 'from',
                                         '--format', 'RAW'])
            self.assertFalse(output.exists())

    def test_overwrite_never_follows_a_symlink(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'retained'
            source.write_text('retained')
            output = Path(directory) / 'image.dmg'
            output.symlink_to(source)
            with self.assertRaises(ValueError):
                IMAGE_TOOL.command(['create', '-srcfolder', '/source', '-format', 'UDRW',
                                    '-ov', str(output)])
            self.assertEqual(source.read_text(), 'retained')

    def test_other_forms_retain_system_validation(self):
        for arguments in [
            ['attach', '-readonly', '-nobrowse', '/image.dmg'],
            ['detach', '-quiet', '/mount'],
            ['convert', '/image.dmg', '-format', 'UDZO', '-o', '/compressed.dmg'],
            ['create', '-size', '10m', '/blank.dmg'],
            ['create', '-fs', 'HFS+', '-format', 'UDRO', '-srcfolder', '/source', '/out'],
            ['create', '-format', 'UDRW', '-srcfolder', '/source', '-unknown', '/out'],
            ['create', '-format', 'UDRW', '-srcfolder', '/source', '/without-extension'],
        ]:
            with self.subTest(arguments=arguments):
                self.assertEqual(IMAGE_TOOL.command(arguments), ['/usr/bin/hdiutil', *arguments])


if __name__ == '__main__':
    unittest.main()
