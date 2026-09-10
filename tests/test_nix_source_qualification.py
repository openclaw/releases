"""Qualification admission and proof gates; no Nix or live supervisor operations."""

import base64
import contextlib
import io
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts/nix-source-qualification"
sys.path.insert(0, str(SCRIPTS))
import driver
import probe
import service

HASH = "sha256-" + base64.b64encode(bytes(range(32))).decode()
DRV = "/nix/store/fixture-openclaw-gateway-pnpm-deps.drv"
HOSTED = {
    "GITHUB_ACTIONS": "true", "RUNNER_ENVIRONMENT": "github-hosted",
    "GITHUB_REPOSITORY": "openclaw/releases", "GITHUB_EVENT_NAME": "workflow_dispatch",
    "GITHUB_REF": driver.BRANCH, "GITHUB_ACTOR": "vincentkoc",
    "GITHUB_TRIGGERING_ACTOR": "vincentkoc", "GITHUB_SHA": "a" * 40,
    "NIX_QUALIFIER_SYSTEM": "x86_64-linux",
}


class AdmissionTests(unittest.TestCase):
    def test_source_dispatch_excludes_upload_jobs_and_keeps_read_only_permissions(self):
        workflow = (ROOT / ".github/workflows/ci.yml").read_text()
        validate, native = workflow.split("\n  nix-source-qualification:\n", 1)
        self.assertIn("if: ${{ github.event_name != 'workflow_dispatch' || inputs.nix_source_phase == 'off' }}", validate)
        self.assertIn("github.ref == 'refs/heads/test/nix-source-qualification-driver-20260910'", native)
        self.assertIn("github.repository == 'openclaw/releases'", native)
        self.assertIn("github.actor == 'vincentkoc' && github.triggering_actor == 'vincentkoc'", native)
        self.assertIn("permissions:\n      contents: read", native)
        for forbidden in ("actions/cache", "actions/upload-artifact", "actions/download-artifact",
                          "secrets.", "contents: write", "actions: write", "persist-credentials: true"):
            self.assertNotIn(forbidden, native)

    def test_host_actor_branch_phase_platform_and_credentials_are_required(self):
        for changes, phase, accepted in [
            ({}, "install", True), ({}, "prefetch", True), ({}, "qualify", True),
            ({"GITHUB_ACTIONS": "false"}, "install", False),
            ({"RUNNER_ENVIRONMENT": "self-hosted"}, "install", False),
            ({"GITHUB_REPOSITORY": "other/releases"}, "install", False),
            ({"GITHUB_EVENT_NAME": "push"}, "install", False),
            ({"GITHUB_REF": "refs/heads/main"}, "install", False),
            ({"GITHUB_ACTOR": "other"}, "install", False),
            ({"GITHUB_TRIGGERING_ACTOR": "other"}, "install", False),
            ({"GITHUB_SHA": "main"}, "install", False),
            ({"NIX_QUALIFIER_SYSTEM": "aarch64-darwin"}, "install", False),
            ({"GH_TOKEN": "fixture"}, "install", False),
            ({"GITHUB_TOKEN": "fixture"}, "qualify", False),
            ({}, "publish", False),
        ]:
            with self.subTest(changes=changes, phase=phase), patch.dict(os.environ, HOSTED | changes, clear=True), \
                    patch.object(driver.sys, "platform", "linux"), patch.object(driver.platform, "machine", return_value="x86_64"):
                if accepted:
                    driver.runner_guard(phase)
                else:
                    with self.assertRaises(RuntimeError):
                        driver.runner_guard(phase)

    def test_no_local_execution_before_any_nix_or_file_operation(self):
        with patch.dict(os.environ, {}, clear=True), patch.object(sys, "argv", ["driver.py", "install"]), \
                patch.object(driver, "Driver") as constructor:
            with self.assertRaisesRegex(RuntimeError, "hosted"):
                driver.main()
            constructor.assert_not_called()

    def test_both_real_system_hashes_must_be_frozen(self):
        identity = {"systems": {"x86_64-linux": None, "aarch64-darwin": None}}
        with self.assertRaisesRegex(RuntimeError, "not frozen"):
            driver.frozen_hashes(identity, "x86_64-linux")
        valid = {"sourceHash": HASH, "pnpmDepsHash": HASH}
        for entry, accepted in [
            (valid, True), (None, False), ({**valid, "pnpmDepsHash": driver.FAKE_HASH}, False),
            ({**valid, "sourceHash": "not-a-hash"}, False), ({"pnpmDepsHash": HASH}, False),
        ]:
            with self.subTest(entry=entry):
                identity["systems"] = {"x86_64-linux": valid, "aarch64-darwin": entry}
                if accepted:
                    self.assertEqual(driver.frozen_hashes(identity, "x86_64-linux"), valid)
                else:
                    with self.assertRaises(RuntimeError):
                        driver.frozen_hashes(identity, "x86_64-linux")

    def test_source_and_packaging_identities_reject_mutable_refs_before_execution(self):
        valid = {"sourceCommit": "a" * 40, "packagingCommit": "b" * 40}
        for key in valid:
            for value in ("main", "v2026.9.3", "a" * 7, "a" * 39, None, 123):
                with self.subTest(key=key, value=value), tempfile.TemporaryDirectory() as td, \
                        patch.dict(os.environ, HOSTED), patch.object(driver, "HERE", Path(td)), \
                        patch.object(driver.Driver, "command") as command:
                    (Path(td) / "hashes.json").write_text(json.dumps(valid | {key: value}))
                    with self.assertRaisesRegex(RuntimeError, "immutable Git SHA"):
                        driver.Driver(Path(td))
                    command.assert_not_called()

    def test_only_exact_dependency_mismatch_is_discovery(self):
        log = f"error: hash mismatch in fixed-output derivation '{DRV}':\n  specified: {driver.FAKE_HASH}\n  got: {HASH}\n".encode()
        for status, output, accepted in [
            (1, log, True), (1, b"\xffunrelated\n" + log, True), (0, log, False),
            (1, log.replace(DRV.encode(), b"/nix/store/transitive.drv"), False),
            (1, log + log, False), (1, b"compilation failed", False),
            (1, log.replace(HASH.encode(), driver.FAKE_HASH.encode()), False),
        ]:
            with self.subTest(status=status, output=output):
                if accepted:
                    self.assertEqual(driver.dependency_mismatch(status, output, DRV), HASH)
                else:
                    with self.assertRaises(RuntimeError):
                        driver.dependency_mismatch(status, output, DRV)

    def test_receipts_require_order_cleanup_exit_success_and_closed_fields(self):
        cleanup = {"qualification": "cleanup", "verified": True}
        complete = {"qualification": "complete", "verified": True}
        for events, status, accepted in [
            ([cleanup, complete], 0, True), ([cleanup, complete], 1, False),
            ([complete], 0, False), ([complete, cleanup], 0, False),
            ([cleanup, complete, complete], 0, False),
            ([cleanup, complete | {"raw": "private"}], 0, False),
            ([cleanup, complete | {"verified": 1}], 0, False),
            ([cleanup, complete | {"verified": False}], 0, False),
        ]:
            with self.subTest(events=events, status=status), tempfile.TemporaryDirectory() as td:
                log = Path(td) / "bytes"
                log.write_bytes(b"\xffnoise\n" + b"".join(b"vm> " + json.dumps(item).encode() + b"\n" for item in events))
                self.assertEqual(driver.fixture_complete([log], status), accepted)

    def test_subprocess_failure_is_captured_as_bytes_not_forwarded(self):
        with tempfile.TemporaryDirectory() as td, patch.dict(os.environ, HOSTED):
            command = driver.Driver(Path(td))
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                result = command.command("failure", [sys.executable, "-c",
                    'import sys;sys.stdout.buffer.write(b"\\xffprivate");sys.exit(7)'], check=False)
            self.assertEqual(result.returncode, 7)
            self.assertEqual((Path(td) / "failure.stdout").read_bytes(), b"\xffprivate")
            self.assertEqual(output.getvalue(), "")

    def test_failure_receipt_keeps_bounded_errors_without_paths_or_credentials(self):
        log = (
            b"ordinary build output\n\x1b[31merror: attribute 'sourceInfo' missing\x1b[0m\n"
            b"error: token=fixture-sensitive\n"
            b"error: /home/operator/private/config.json failed on build.internal 192.0.2.40\n"
            b"error: https://private.invalid/path failed for person@example.invalid\n"
            b"error: " + b"x" * 1000 + b"\n"
        )
        result = driver.failure_diagnostic(subprocess.CalledProcessError(1, ["fixture"]), log)
        text = json.dumps(result)
        self.assertIn("attribute 'sourceInfo' missing", text)
        for private in ("fixture-sensitive", "/home/operator", "build.internal", "192.0.2.40",
                        "private.invalid", "person@example.invalid", "\\u001b"):
            self.assertNotIn(private, text)
        self.assertLessEqual(len(result), 6)
        self.assertTrue(all(len(line) <= 240 for line in result))
        many = driver.failure_diagnostic(RuntimeError("missing frozen hashes"), b"error: failed\n" * 100)
        self.assertEqual(len(many), 6)

    def test_prefetch_stops_at_classified_dependencies_never_package_or_activation(self):
        with tempfile.TemporaryDirectory() as td, patch.dict(os.environ, HOSTED):
            instance = driver.Driver(Path(td))
            metadata = {
                "packagingCommit": instance.identity["packagingCommit"],
                "sourceCommit": instance.identity["sourceCommit"], "system": "x86_64-linux",
                "version": "2026.9.3", "pnpm": "12.3.4", "node": "24.19.0",
                "pinnedRev": None, "defaultNpmLazy": True,
            }
            calls = []
            def nix(stage, command, *args, check=True):
                calls.append((stage, command, args))
                values = {
                    "source-prefetch": {"storePath": td, "hash": HASH},
                    "cache-config": {"extra-substituters": [], "extra-trusted-public-keys": []},
                    "metadata": metadata, "dependency-drv": DRV,
                }
                if stage == "dependency-prefetch":
                    log = f"hash mismatch in fixed-output derivation '{DRV}':\nspecified: {driver.FAKE_HASH}\ngot: {HASH}\n"
                    return subprocess.CompletedProcess([], 1, b"", log.encode())
                return subprocess.CompletedProcess([], 0, json.dumps(values[stage]).encode(), b"")
            config = {key: {"value": False if key in ("always-allow-substitutes", "accept-flake-config") else ""}
                      for key in ("always-allow-substitutes", "accept-flake-config", "post-build-hook", "builders", "access-tokens")}
            results = [subprocess.CompletedProcess([], 0, json.dumps(config).encode(), b""),
                       subprocess.CompletedProcess([], 0, b"nix (Nix) 2.35.2\n", b"")]
            output = io.StringIO()
            with patch.object(instance, "command", side_effect=results), patch.object(instance, "nix", side_effect=nix), \
                    contextlib.redirect_stdout(output):
                instance.native("prefetch")
            receipt = json.loads(output.getvalue())
            self.assertEqual(receipt["result"], "DISCOVERED")
            self.assertIs(receipt["packageProof"], False)
            self.assertEqual(receipt["pnpmDepsHash"], HASH)
            self.assertEqual([stage for stage, _, _ in calls],
                             ["source-prefetch", "cache-config", "metadata", "dependency-drv", "dependency-prefetch"])
            self.assertIn("https://github.com/openclaw/openclaw/archive/" + metadata["sourceCommit"] + ".tar.gz", calls[0][2])
            self.assertEqual(calls[-1][2][-1], "dependencies")


class IsolationTests(unittest.TestCase):
    def test_parent_timeout_and_signal_allow_real_probe_cleanup_before_reaping(self):
        for mode in ("timeout", "signal"):
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as td:
                directory = Path(td)
                child = subprocess.Popen([
                    sys.executable, ROOT / "tests/nix_source_process_fixture.py", mode, directory,
                ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True)
                try:
                    deadline = time.monotonic() + 10
                    events = directory / "events"
                    while not events.exists() or "ready" not in events.read_text().splitlines():
                        if child.poll() is not None or time.monotonic() >= deadline:
                            self.fail("probe did not reach its owned activation")
                        time.sleep(0.02)
                    if mode == "signal":
                        child.send_signal(signal.SIGTERM)
                    stdout, stderr = child.communicate(timeout=30)
                    self.assertEqual(child.returncode, 1, stderr.decode())
                    self.assertEqual(events.read_text().splitlines(), [
                        "ready", "cleanup-started", "stopped", "cleanup-verified",
                        "TimeoutExpired" if mode == "timeout" else "RuntimeError",
                    ])
                    self.assertNotIn(b'"result": "PASS"', stdout)
                    self.assertFalse(service.alive(int((directory / "probe.pid").read_text())))
                finally:
                    if child.poll() is None:
                        child.kill()
                        child.communicate()
                    pid_file = directory / "probe.pid"
                    if pid_file.exists():
                        try:
                            os.killpg(int(pid_file.read_text()), signal.SIGKILL)
                        except ProcessLookupError:
                            pass
                    child.stdout.close()
                    child.stderr.close()

    def test_uncooperative_command_is_killed_and_reaped_after_its_grace(self):
        with self.assertRaises(subprocess.TimeoutExpired) as failure:
            service.run([sys.executable, "-c",
                         "import os,signal;signal.signal(signal.SIGTERM,signal.SIG_IGN);"
                         "print(os.getpid(),flush=True);signal.pause()"],
                        os.environ, timeout=1, terminate_grace=0.05)
        self.assertFalse(service.alive(int(failure.exception.output.strip())))

    def test_global_profiles_and_dangling_gcroot_block_before_home_creation(self):
        for kind in ("fresh", "profile", "dangling-root", "existing-home"):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as td:
                base = Path(td)
                home, global_state = base / "home", base / "global"
                if kind == "profile":
                    marker = global_state / "profiles/per-user/fixture/home-manager-1-link"
                    marker.parent.mkdir(parents=True)
                    marker.symlink_to(base / "missing")
                if kind == "dangling-root":
                    marker = global_state / "gcroots/per-user/fixture/current-home"
                    marker.parent.mkdir(parents=True)
                    marker.symlink_to(base / "missing")
                if kind == "existing-home":
                    home.mkdir()
                if kind == "fresh":
                    profile = probe.prepare_home(home, "fixture", global_state)
                    self.assertEqual(profile, home / ".local/state/nix/profiles/home-manager")
                    self.assertTrue((home / ".nix-profile").is_symlink())
                else:
                    with self.assertRaises((RuntimeError, FileExistsError)):
                        probe.prepare_home(home, "fixture", global_state)
                    if kind != "existing-home":
                        self.assertFalse(home.exists())

    def test_instance_env_cannot_inherit_provenance_or_operator_state(self):
        with patch.dict(os.environ, {
            "HOME": "/operator", "OPENCLAW_STATE_DIR": "/operator/state",
            "OPENCLAW_PROFILE": "live", "GITHUB_SHA": "a" * 40, "GIT_COMMIT": "b" * 40,
            "GH_TOKEN": "fixture", "NODE_OPTIONS": "--import=other", "PATH": "/bin",
        }, clear=True):
            env = probe.isolated_env(Path("/fixture"), "fixture")
        self.assertEqual(env["HOME"], "/fixture")
        self.assertEqual(env["OPENCLAW_CONFIG_PATH"], "/fixture/.openclaw-qualification/openclaw.json")
        self.assertEqual(env["XDG_STATE_HOME"], "/fixture/.local/state")
        for key in ("GITHUB_SHA", "GIT_COMMIT", "OPENCLAW_PROFILE", "GH_TOKEN", "NODE_OPTIONS"):
            self.assertNotIn(key, env)

    def test_generation_listing_must_match_the_only_installed_profile(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td).resolve()
            generation = root / "generation"
            generation.mkdir()
            (root / "home-manager-1-link").symlink_to(generation)
            profile = root / "home-manager"
            profile.symlink_to("home-manager-1-link")
            valid = f"2026-09-10 12:00 : id 1 -> {generation}\n".encode()
            for output, accepted in [(valid, True), (valid + valid, False),
                                     (valid.replace(b"id 1", b"id 2"), False),
                                     (b"", False)]:
                with self.subTest(output=output), patch.object(probe, "run", return_value=subprocess.CompletedProcess([], 0, output)):
                    if accepted:
                        probe.verify_generation(profile, {"activation": str(generation), "homeManager": "fixture"}, {})
                    else:
                        with self.assertRaises(RuntimeError):
                            probe.verify_generation(profile, {"activation": str(generation), "homeManager": "fixture"}, {})

    def test_cleanup_cannot_pass_if_a_pid_survives_or_observation_fails(self):
        inactive = {"registered": False, "pid": 0, "active": "inactive"}
        for darwin, surviving, observation_error in [(False, False, False), (True, False, False),
                                                     (False, True, False), (True, False, True)]:
            with self.subTest(darwin=darwin, surviving=surviving, observation_error=observation_error):
                instance = service.Service(Path("/fixture"), darwin, {})
                instance.observed.add(123)
                states = [RuntimeError("unknown") if observation_error else inactive, inactive]
                output = io.StringIO()
                with patch.object(instance, "state", side_effect=states), patch.object(service, "run") as stop, \
                        patch.object(service, "alive", return_value=surviving), \
                        patch.object(service.time, "monotonic", side_effect=[0, 20]), \
                        contextlib.redirect_stdout(output):
                    if surviving or observation_error:
                        with self.assertRaises(RuntimeError):
                            instance.__exit__(None, None, None)
                        self.assertEqual(output.getvalue(), "")
                    else:
                        instance.__exit__(None, None, None)
                        self.assertEqual(json.loads(output.getvalue()), {"qualification": "cleanup", "verified": True})
                self.assertEqual(stop.call_count, 1)

    def test_cli_version_allows_unknown_commit_but_not_a_wrong_identity(self):
        sha = "1391f7cd2d40ab5bbcf2f5f831d3a64f520e72d7"
        for output, accepted in [(b"OpenClaw 2026.9.3\n", True), (b"OpenClaw 2026.9.3 (1391f7c)\n", True),
                                 (b"OpenClaw 2026.9.3 (4bd0453)\n", False), (b"OpenClaw 2026.7.1\n", False)]:
            with self.subTest(output=output):
                if accepted:
                    probe.verify_version(output, sha)
                else:
                    with self.assertRaises(RuntimeError):
                        probe.verify_version(output, sha)

    def test_ui_entry_comparison_accepts_gateway_rewriting_not_a_different_bundle(self):
        packaged = '<html><script type="module" src="./assets/app.js"></script><link rel="stylesheet" href="./assets/app.css"></html>'
        served = packaged.replace("<html>", '<html data-runtime="fixture">').replace("./assets/", "/assets/")
        self.assertEqual(probe.EntryAssets(packaged).assets, probe.EntryAssets(served).assets)
        self.assertNotEqual(probe.EntryAssets(packaged).assets,
                            probe.EntryAssets(served.replace("app.js", "other.js")).assets)


if __name__ == "__main__":
    unittest.main()
