"""Guard the one-off installed proof without installing Nix or fetching artifacts."""
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import mock_open, patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("installed_driver", ROOT / "scripts/probe-original-nar.py")
driver = importlib.util.module_from_spec(spec)
spec.loader.exec_module(driver)

CLEANUP = {"cleanup": "verified", "service": {"registered": False, "pid": 0}, "observedPids": [10]}
COMPLETED = {
    "result": "PASS", "scope": "installed-upgrade-rollback", "witnessId": "fixture-job",
    "generations": [{}, {}, {}], "cleanup": "verified", "trackB": "DEFERRED: source patch applicability",
}


class RunnerGuardTests(unittest.TestCase):
    def environment(self, system):
        return {
            "GITHUB_ACTIONS": "true", "RUNNER_ENVIRONMENT": "github-hosted",
            "GITHUB_REPOSITORY": "openclaw/releases", "GITHUB_EVENT_NAME": "workflow_dispatch",
            "GITHUB_REF": "refs/heads/test/nix-installed-upgrade-driver-20260909",
            "GITHUB_ACTOR": "vincentkoc", "GITHUB_TRIGGERING_ACTOR": "vincentkoc",
            "NIX_QUALIFIER_SYSTEM": system,
        }

    def test_native_platform_phase_and_token_boundary(self):
        for native, machine, system in (
            ("linux", "x86_64", "x86_64-linux"), ("darwin", "arm64", "aarch64-darwin"),
        ):
            for phase in ("install", "download", "prove", "qualify"):
                for token in ("", "fixture-token"):
                    accepted = (
                        (phase == "download" and native == "darwin" and bool(token))
                        or (phase != "download" and not token and (phase != "prove" or native == "darwin"))
                    )
                    env = self.environment(system) | {"GH_TOKEN": token}
                    with self.subTest(native=native, phase=phase, token=bool(token)), \
                         patch.dict(os.environ, env, clear=True), patch.object(driver.sys, "platform", native), \
                         patch.object(driver.platform, "machine", return_value=machine):
                        if accepted:
                            driver.runner_guard(phase)
                        else:
                            with self.assertRaises(AssertionError):
                                driver.runner_guard(phase)

    def test_non_hosted_wrong_actor_ref_repo_platform_and_implicit_token_rejected(self):
        for changes in (
            {"GITHUB_ACTIONS": "false"}, {"RUNNER_ENVIRONMENT": "self-hosted"},
            {"GITHUB_REF": "refs/heads/main"}, {"GITHUB_REF": "refs/heads/other"},
            {"GITHUB_REPOSITORY": "fixture/releases"}, {"GITHUB_EVENT_NAME": "push"},
            {"GITHUB_ACTOR": "fixture"}, {"GITHUB_TRIGGERING_ACTOR": "fixture"},
            {"NIX_QUALIFIER_SYSTEM": "aarch64-darwin"}, {"GITHUB_TOKEN": "fixture-token"},
        ):
            with self.subTest(changes=changes), \
                 patch.dict(os.environ, self.environment("x86_64-linux") | changes, clear=True), \
                 patch.object(driver.sys, "platform", "linux"), \
                 patch.object(driver.platform, "machine", return_value="x86_64"):
                with self.assertRaises(AssertionError):
                    driver.runner_guard("install")


class InstallerTests(unittest.TestCase):
    def test_unchanged_digest_pinned_script_enables_kvm_only_on_linux_without_tokens(self):
        for native in ("linux", "darwin"):
            with self.subTest(native=native), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                script = root / "installer"
                script.write_text("fixture installer, never executed")
                probe = driver.Probe(root)
                with patch.dict(os.environ, {}, clear=True), patch.object(driver.sys, "platform", native), \
                     patch.object(driver.shutil, "which", return_value=None), \
                     patch.object(driver, "digest", return_value=driver.INSTALLER_HASH), \
                     patch.object(probe, "command", return_value=script) as execute, \
                     contextlib.redirect_stdout(io.StringIO()):
                    probe.install()
                download, install = execute.call_args_list
                self.assertEqual(download.args[1][-1],
                                 f"https://raw.githubusercontent.com/cachix/install-nix-action/"
                                 f"{driver.INSTALLER_SHA}/install-nix.sh")
                self.assertEqual(install.args[1], ["bash", str(script)])
                env = install.args[2]
                self.assertEqual(env["INPUT_ENABLE_KVM"], "true" if native == "linux" else "false")
                self.assertEqual(env["INPUT_GITHUB_ACCESS_TOKEN"], "")
                self.assertEqual(env["INPUT_INSTALL_URL"], "")
                self.assertNotIn("GH_TOKEN", env)
                self.assertNotIn("GITHUB_TOKEN", env)
                self.assertIn("access-tokens =", env["INPUT_EXTRA_NIX_CONFIG"])
                self.assertIn("post-build-hook =", env["INPUT_EXTRA_NIX_CONFIG"])
                self.assertEqual(script.read_text(), "fixture installer, never executed")

    def test_wrong_installer_digest_never_executes(self):
        probe = driver.Probe(Path("/fixture"))
        with patch.object(driver.shutil, "which", return_value=None), \
             patch.object(driver, "digest", return_value="wrong"), \
             patch.object(probe, "command", return_value=Path("/fixture/download")) as execute:
            with self.assertRaises(AssertionError):
                probe.install()
            self.assertEqual(execute.call_count, 1)

    def test_existing_nix_is_not_reconfigured(self):
        probe = driver.Probe(Path("/fixture"))
        with patch.object(driver.shutil, "which", return_value="/fixture/nix"), \
             patch.object(probe, "command") as execute:
            with self.assertRaises(AssertionError):
                probe.install()
            execute.assert_not_called()

    def test_kvm_access_and_api_are_both_required(self):
        for api in (12, 0):
            with self.subTest(api=api), patch("builtins.open", mock_open()) as opened, \
                 patch.object(driver.fcntl, "ioctl", return_value=api) as ioctl, \
                 contextlib.redirect_stdout(io.StringIO()):
                if api == 12:
                    driver.kvm_preflight()
                else:
                    with self.assertRaises(AssertionError):
                        driver.kvm_preflight()
                opened.assert_called_once_with("/dev/kvm", "rb+", buffering=0)
                self.assertEqual(ioctl.call_args.args[1], 0xAE00)
        with patch("builtins.open", side_effect=PermissionError), patch.object(driver.fcntl, "ioctl") as ioctl:
            with self.assertRaises(PermissionError):
                driver.kvm_preflight()
            ioctl.assert_not_called()

    def test_effective_tokens_export_hook_remote_builder_or_wrong_nix_block_qualification(self):
        valid = {
            "always-allow-substitutes": {"value": False}, "post-build-hook": {"value": ""},
            "builders": {"value": ""}, "access-tokens": {"value": {}},
        }
        for key in (*valid, "version"):
            with self.subTest(key=key), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                config, version = root / "config", root / "version"
                values = valid | ({key: {"value": "unexpected"}} if key != "version" else {})
                config.write_text(json.dumps(values))
                version.write_text("nix (Nix) 2.35.1" if key == "version" else "nix (Nix) 2.35.2")
                probe = driver.Probe(root)
                with patch.object(probe, "command", side_effect=[config, version]):
                    with self.assertRaises(AssertionError):
                        probe.nix_preflight("qualifier")


class WorkflowBoundaryTests(unittest.TestCase):
    def test_mixed_byte_logs_keep_sentinel_completion_and_cleanup_gates(self):
        sha = "a" * 40
        for mixed_stream in ("stdout", "stderr"):
            for missing in (None, "sentinel", "completed", "cleanup"):
                with self.subTest(mixed_stream=mixed_stream, missing=missing), \
                     tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    probe = driver.Probe(root)
                    output = io.StringIO()

                    def command(stage, args):
                        result = root / f"{stage}.stdout"
                        if stage != "installed-upgrade":
                            result.write_text(sha if stage == "qualifier-head" else "")
                            return result
                        stdout = b"" if missing == "sentinel" else (
                            b"PASS installed-upgrade Node22 -> Node24 -> rollback; cleanup verified\n"
                        )
                        if missing != "completed":
                            stdout += b"VM> " + json.dumps(COMPLETED).encode() + b"\n"
                        stderr = b"" if missing == "cleanup" else json.dumps(CLEANUP).encode() + b"\n"
                        for stream, data in (("stdout", stdout), ("stderr", stderr)):
                            if stream == mixed_stream:
                                data = (
                                    b"\xff raw-private-log\nVM> {malformed JSON}\n"
                                    b'VM> {"foreign":"\xff"}\n\xff VM> ' + data + b"\xff raw-trailer\n"
                                )
                            (root / f"{stage}.{stream}").write_bytes(data)
                        return result

                    with patch.dict(os.environ, {"NIX_QUALIFIER_SHA": sha,
                                                "NIX_QUALIFIER_SYSTEM": "x86_64-linux"}, clear=True), \
                         patch.object(driver.sys, "platform", "linux"), \
                         patch.object(probe, "nix_preflight"), patch.object(driver, "kvm_preflight"), \
                         patch.object(probe, "command", side_effect=command), \
                         contextlib.redirect_stdout(output):
                        if missing:
                            with self.assertRaises(AssertionError):
                                probe.qualify()
                            self.assertNotIn('"result": "PASS"', output.getvalue())
                        else:
                            probe.qualify()
                            self.assertIn('"result": "PASS"', output.getvalue())
                            self.assertIn('"cleanup": "verified"', output.getvalue())
                    for private in ("raw-private-log", "raw-trailer", "foreign", "malformed"):
                        self.assertNotIn(private, output.getvalue())

    def test_exact_checkout_and_successful_cleanup_receipt_are_required(self):
        sha = "a" * 40
        for changed in ("", "head", "dirty", "receipt", "failure"):
            with self.subTest(changed=changed), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                probe = driver.Probe(root)
                calls = []
                output = io.StringIO()

                def command(stage, args):
                    calls.append((stage, args))
                    result = root / f"{stage}.stdout"
                    value = ""
                    if stage == "qualifier-head":
                        value = "b" * 40 if changed == "head" else sha
                    if stage == "qualifier-clean" and changed == "dirty":
                        value = " M fixture.py"
                    if stage == "installed-upgrade":
                        if changed == "failure":
                            raise driver.subprocess.CalledProcessError(7, args)
                        value = "" if changed == "receipt" else (
                            'PASS installed-upgrade Node22 -> Node24 -> rollback; cleanup verified\n'
                            + json.dumps(COMPLETED) + "\n"
                        )
                        (root / "installed-upgrade.stderr").write_text(
                            "unexported raw build log\n" + json.dumps(CLEANUP) + "\n"
                        )
                    result.write_text(value)
                    return result

                with patch.dict(os.environ, {"NIX_QUALIFIER_SHA": sha,
                                            "NIX_QUALIFIER_SYSTEM": "x86_64-linux"}, clear=True), \
                     patch.object(driver.sys, "platform", "linux"), \
                     patch.object(probe, "nix_preflight"), patch.object(driver, "kvm_preflight"), \
                     patch.object(probe, "command", side_effect=command), \
                     contextlib.redirect_stdout(output):
                    if changed:
                        with self.assertRaises((AssertionError, driver.subprocess.CalledProcessError)):
                            probe.qualify()
                        self.assertNotIn('"result": "PASS"', output.getvalue())
                    else:
                        probe.qualify()
                        self.assertIn('"cleanup": "verified"', output.getvalue())
                        self.assertIn('"qualifierHead": "' + sha + '"', output.getvalue())
                        self.assertNotIn("unexported raw build log", output.getvalue())
                fetch = next(args for stage, args in calls if stage == "qualifier-fetch")
                self.assertEqual(fetch[-4:], ["fetch", "--depth=1", "origin", sha])
                self.assertIn("credential.helper=", fetch)
                if changed in ("head", "dirty"):
                    self.assertNotIn("installed-upgrade", [stage for stage, _ in calls])

    def test_failure_forwards_only_fixture_receipts_from_both_streams_and_keeps_original_exit(self):
        for cleanup in (CLEANUP, CLEANUP | {"cleanup": "failed"}, None):
            with self.subTest(cleanup=cleanup), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                probe = driver.Probe(root)
                output = io.StringIO()
                sha = "a" * 40
                error = subprocess.CalledProcessError(7, ["private-command-value"])

                def command(stage, args):
                    path = root / f"{stage}.stdout"
                    if stage == "qualifier-head":
                        path.write_text(sha)
                    elif stage == "installed-upgrade":
                        path.write_bytes(
                            b'\xff raw-private-log\nVM> {malformed JSON}\nVM> {"foreign":"\xff"}\n'
                            + (
                                '{"phase":"current","postActivation":{"path":"/runner/temp/unit"}}\n'
                                '{"phase":"current","private":"unrelated-json"}\n'
                                '{"scope":"other","private":"unrelated-json"}\n'
                                'raw-private-log\n' + json.dumps(COMPLETED) + "\n"
                            ).encode()
                        )
                        (root / "installed-upgrade.stderr").write_bytes(
                            b"\xff VM> " + (
                                "BLOCKED installed-upgrade phase=current; no fallback\n"
                                "BLOCKED installed-upgrade phase=build status=7; no fallback\n"
                                + (json.dumps(cleanup) + "\n" if cleanup else "")
                            ).encode() + b"\xff raw-trailer\n"
                        )
                        raise error
                    else:
                        path.write_text("")
                    return path

                with patch.dict(os.environ, {"NIX_QUALIFIER_SHA": sha, "RUNNER_TEMP": "/runner/temp",
                                            "NIX_QUALIFIER_SYSTEM": "x86_64-linux"}, clear=True), \
                     patch.object(driver.sys, "platform", "linux"), \
                     patch.object(probe, "nix_preflight"), patch.object(driver, "kvm_preflight"), \
                     patch.object(probe, "command", side_effect=command), \
                     contextlib.redirect_stdout(output):
                    with self.assertRaises(subprocess.CalledProcessError) as raised:
                        probe.qualify()
                self.assertIs(raised.exception, error)
                self.assertEqual(raised.exception.returncode, 7)
                emitted = output.getvalue()
                self.assertIn('"path": "<runner-temp>/unit"', emitted)
                self.assertIn('"fixtureBlocked": {"phase": "current", "status": 7}', emitted)
                self.assertIn('"fixtureBlocked": {"phase": "build", "status": 7}', emitted)
                self.assertEqual('"cleanup": "verified"' in emitted, cleanup == CLEANUP)
                for value in ("PASS", "private-command-value", "unrelated-json", "raw-private-log", "/runner/temp"):
                    self.assertNotIn(value, emitted)

    def test_exact_event_shapes_and_recursive_path_scrubbing(self):
        for unrelated in (
            {"phase": "current"}, {"scope": "installed-upgrade-rollback"},
            {"cleanup": "verified"}, {"phase": "other", "postActivation": {}},
            {"phase": "old", "postActivation": {}, "extra": "private"},
            CLEANUP | {"service": {"registered": True, "pid": 10, "active": "active"}},
        ):
            with self.subTest(unrelated=unrelated):
                self.assertFalse(driver.fixture_event(unrelated))
        with patch.dict(os.environ, {"RUNNER_TEMP": "/runner/temp", "GITHUB_WORKSPACE": "/runner/work",
                                    "HOME": "/runner/home"}, clear=True):
            event = driver.scrub_fixture({
                "definition": "/tmp/openclaw-installed-baseline/config",
                "nested": ["/home/baseline/qualification/profile", "/runner/temp/file",
                           "/runner/work/checkout", "/runner/home/file", "/nix/store/fixture-node/bin/node"],
            })
        self.assertEqual(event, {"definition": "<fixture-home>/config", "nested": [
            "<fixture-home>/profile", "<runner-temp>/file", "<workspace>/checkout",
            "<runner-home>/file", "/nix/store/fixture-node/bin/node",
        ]})

    def test_prefixture_failure_exposes_only_stage_exit_and_exception_class(self):
        for error, code in ((subprocess.CalledProcessError(7, ["private-command"]), 7),
                            (RuntimeError("private-message"), 1)):
            with self.subTest(error=type(error).__name__), tempfile.TemporaryDirectory() as directory:
                output = io.StringIO()
                with patch.dict(os.environ, {"RUNNER_TEMP": directory}, clear=True), \
                     patch.object(driver.sys, "argv", ["probe", "install"]), \
                     patch.object(driver, "runner_guard", side_effect=error), \
                     contextlib.redirect_stdout(output):
                    self.assertEqual(driver.main(), code)
                self.assertEqual(output.getvalue(), f"Installed proof blocked: stage=identity exit={code} "
                                                   f"exception={type(error).__name__}\n")

    def test_dispatch_skips_exporting_validator_but_preserves_normal_ci(self):
        workflow = (ROOT / ".github/workflows/ci.yml").read_text()
        validate, proof = workflow.split("  installed_upgrade:\n")
        self.assertIn("branches: [main]", validate)
        self.assertIn("pull_request:", validate)
        self.assertIn("if: ${{ github.event_name != 'workflow_dispatch' || !inputs.qualify_installed_upgrade }}",
                      validate)
        self.assertIn("uses: actions/cache/save@", validate)
        self.assertIn("uses: actions/upload-artifact@", validate)
        self.assertNotIn("uses:", proof)
        self.assertIn("github.ref == 'refs/heads/test/nix-installed-upgrade-driver-20260909'", proof)
        self.assertIn("contents: read\n      actions: read", proof)
        self.assertNotIn(": write", proof)
        self.assertNotIn("secrets.", proof)
        self.assertIn("system: x86_64-linux", proof)
        self.assertEqual(proof.count("          - os:"), 1)
        self.assertNotIn("system: aarch64-darwin", proof)
        self.assertRegex(proof, r"NIX_QUALIFIER_SHA: [0-9a-f]{40}\n")
        steps = proof.split("      - name: ")[1:]
        token_steps = [step for step in steps if "github.token" in step or "GH_TOKEN" in step]
        self.assertEqual(len(token_steps), 1)
        self.assertIn("if: ${{ runner.os == 'macOS' }}", token_steps[0])
        self.assertIn("probe-original-nar.py download", token_steps[0])
        prove = next(step for step in steps if "probe-original-nar.py prove" in step)
        self.assertIn("if: ${{ runner.os == 'macOS' }}", prove)


if __name__ == "__main__":
    unittest.main()
