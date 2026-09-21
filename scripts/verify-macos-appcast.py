#!/usr/bin/env python3
"""Bind a retained or promoted Sparkle entry to its exact packaged app."""
import argparse
from pathlib import Path
import plistlib
import xml.etree.ElementTree as ET
import zipfile

SPARKLE = '{http://www.andymatuschak.org/xml-namespaces/sparkle}'
VARIANTS = {
    'universal': ('', 'appcast.xml'),
    'arm64': ('-arm64', 'appcast-arm64.xml'),
    'x86_64': ('-x86_64', 'appcast-x86_64.xml'),
}


def verify(appcast, package, tag, repository, variant='universal'):
    version = tag.removeprefix('v')
    if variant not in VARIANTS:
        raise ValueError(f'Unknown macOS artifact variant: {variant}')
    suffix, appcast_name = VARIANTS[variant]
    if package.name != f'OpenClaw-{version}{suffix}.zip':
        raise ValueError('Packaged ZIP filename does not match the release tag')
    with zipfile.ZipFile(package) as archive:
        plist_path = 'OpenClaw.app/Contents/Info.plist'
        if archive.namelist().count(plist_path) != 1:
            raise ValueError('Packaged ZIP must contain one OpenClaw Info.plist')
        info = plistlib.loads(archive.read(plist_path))
    if info.get('CFBundleShortVersionString') != version:
        raise ValueError('Packaged app version does not match the release tag')
    expected_feed = f'https://raw.githubusercontent.com/{repository}/main/{appcast_name}'
    if info.get('SUFeedURL') != expected_feed:
        raise ValueError('Packaged app feed does not match its artifact variant')
    build = info.get('CFBundleVersion', '')
    if not isinstance(build, str) or not build.isdecimal():
        raise ValueError('Packaged app build must be numeric')
    items = [item for item in ET.parse(appcast).findall('./channel/item')
             if item.findtext(f'{SPARKLE}shortVersionString') == version]
    if len(items) != 1:
        raise ValueError(f'Appcast must contain exactly one release {version}')
    item = items[0]
    if item.findtext(f'{SPARKLE}version') != build:
        raise ValueError('Appcast build does not match the packaged app')
    enclosures = item.findall('enclosure')
    if len(enclosures) != 1:
        raise ValueError('Appcast release must contain exactly one enclosure')
    enclosure = enclosures[0]
    expected_url = f'https://github.com/{repository}/releases/download/{tag}/{package.name}'
    if enclosure.get('url') != expected_url:
        raise ValueError('Appcast download URL does not match the release ZIP')
    if enclosure.get('length') != str(package.stat().st_size):
        raise ValueError('Appcast download length does not match the release ZIP')
    # Signing belongs to the producer. This boundary verifies identity and
    # signature presence; it does not claim cryptographic verification.
    if not enclosure.get(f'{SPARKLE}edSignature', '').strip():
        raise ValueError('Appcast release is missing its Ed25519 signature')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('appcast', type=Path)
    parser.add_argument('package', type=Path)
    parser.add_argument('tag')
    parser.add_argument('repository')
    parser.add_argument('variant', choices=VARIANTS, nargs='?', default='universal')
    args = parser.parse_args()
    try:
        verify(args.appcast, args.package, args.tag, args.repository, args.variant)
    except (ValueError, OSError, ET.ParseError, zipfile.BadZipFile) as error:
        parser.exit(1, f'Invalid macOS appcast: {error}\n')
    print(f'Appcast matches {args.tag} and {args.package.name}')
