#!/usr/bin/env python3
"""Keep tagged packagers' two folder-image forms working on macOS 27.

All other hdiutil commands retain their system implementation. Read-only APFS
snapshots use UDRO; writable staging images use RAW before the packager's normal
conversion to its final compressed format.
"""
import os
from pathlib import Path
import stat
import sys


def command(arguments):
    original = ['/usr/bin/hdiutil', *arguments]
    if not arguments or arguments[0] != 'create':
        return original
    values, overwrite, destination = {}, False, None
    iterator = iter(arguments[1:])
    for argument in iterator:
        if argument in ('-srcfolder', '-volname', '-format', '-fs'):
            if argument in values:
                return original
            value = next(iterator, None)
            if value is None:
                return original
            values[argument] = value
        elif argument == '-ov' and not overwrite:
            overwrite = True
        elif not argument.startswith('-') and destination is None:
            destination = argument
        else:
            return original
    image_format = values.get('-format')
    known_form = ((image_format == 'UDRO' and values.get('-fs') == 'APFS')
                  or (image_format == 'UDRW' and '-fs' not in values))
    if (not known_form or '-srcfolder' not in values or not destination
            or not destination.endswith('.dmg')):
        return original
    output = Path(destination)
    if output.is_symlink():
        raise ValueError('Refusing to replace a symbolic-link image destination')
    if output.exists():
        if not overwrite:
            raise FileExistsError('Image destination already exists: ' + destination)
        if not stat.S_ISREG(output.stat().st_mode):
            raise ValueError('Image destination is not a regular file: ' + destination)
        output.unlink()
    result = ['/usr/sbin/diskutil', 'image', 'create', 'from', '--format',
              'UDRO' if image_format == 'UDRO' else 'RAW']
    if '-volname' in values:
        result += ['--volumeName', values['-volname']]
    return [*result, values['-srcfolder'], destination]


def main():
    try:
        arguments = command(sys.argv[1:])
        os.execv(arguments[0], arguments)
    except (OSError, ValueError) as error:
        print('macOS image creation: ' + str(error), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
