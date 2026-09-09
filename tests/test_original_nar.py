"""Exercise digest-before-inspection, provenance, and the public log boundary."""
import hashlib
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

SPEC = importlib.util.spec_from_file_location(
    "probe_original_nar", Path(__file__).resolve().parents[1] / "scripts/probe-original-nar.py")
PROBE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PROBE)


class OriginalNarTests(unittest.TestCase):
    def test_outer_digest_precedes_zip_inspection(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "unbound.zip"
            path.write_bytes(b"not a zip")
            with patch.object(PROBE, "OUTER_SIZE", path.stat().st_size):
                with self.assertRaises(AssertionError):
                    PROBE.extract_original(path, path.parent)
            self.assertEqual(list(path.parent.iterdir()), [path])

    def test_extracts_only_original_zip_and_matching_provenance(self):
        for scenario in ("valid", "wrong-source", "wrong-tag", "wrong-inner-hash"):
            with self.subTest(scenario=scenario), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                archive = root / "outer.zip"
                output = root / "selected"
                output.mkdir()
                payload = b"opaque original ZIP fixture, never opened or executed"
                with zipfile.ZipFile(archive, "w") as container:
                    container.writestr(PROBE.ZIP_MEMBER, payload)
                    container.writestr("_temp/openclaw-macos-preflight/release-sha.txt",
                                       ("0" * 40 if scenario == "wrong-source" else PROBE.SOURCE_SHA) + "\n")
                    container.writestr("_temp/openclaw-macos-preflight/release-tag.txt",
                                       ("v2026.7.2" if scenario == "wrong-tag" else "v2026.7.1") + "\n")
                    container.writestr("unused.dmg", b"do not extract")
                    container.writestr("unused.dSYM.zip", b"do not extract")
                values = dict(OUTER_SIZE=archive.stat().st_size, OUTER_HASH=PROBE.digest(archive),
                              ZIP_SIZE=len(payload), ZIP_HASH=hashlib.sha256(payload).hexdigest())
                if scenario == "wrong-inner-hash":
                    values["ZIP_HASH"] = "0" * 64
                with patch.multiple(PROBE, **values):
                    if scenario == "valid":
                        PROBE.extract_original(archive, output)
                        self.assertEqual((output / PROBE.ZIP_NAME).read_bytes(), payload)
                        self.assertEqual({p.name for p in output.iterdir()},
                                         {PROBE.ZIP_NAME, "release-sha.txt", "release-tag.txt"})
                    else:
                        with self.assertRaises(AssertionError):
                            PROBE.extract_original(archive, output)

    def test_only_exact_local_fetch_and_unpack_evidence_is_public(self):
        filename = "a" * 32 + "-OpenClaw-2026.7.1.zip"
        transport = f"file:///nix/store/{filename}"
        log = (f"source> trying {transport}\n"
               f"source> unpacking source archive /build/private-fixture/{filename}\n"
               "unrelated signed URL or raw diagnostic must not be forwarded\n")
        self.assertEqual(PROBE.local_fetch_evidence(log, transport),
                         [f"trying {transport}", f"unpacking source archive <build-temp>/{filename}"])
        for changed in (log.replace(transport, "https://example.invalid/cache"),
                        log.replace(f"/build/private-fixture/{filename}", "/build/other.zip")):
            with self.assertRaises(AssertionError):
                PROBE.local_fetch_evidence(changed, transport)

    def test_failed_subprocess_retains_raw_streams_without_emitting_them(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            probe = PROBE.Probe(root)
            with self.assertRaises(subprocess.CalledProcessError) as failure:
                probe.command("fixture", [sys.executable, "-c",
                              "import sys; print('raw-out'); print('raw-err', file=sys.stderr); sys.exit(7)"])
            self.assertEqual(failure.exception.returncode, 7)
            self.assertEqual(probe.stage, "fixture")
            self.assertEqual((root / "fixture.stdout").read_text(), "raw-out\n")
            self.assertEqual((root / "fixture.stderr").read_text(), "raw-err\n")


if __name__ == "__main__":
    unittest.main()
