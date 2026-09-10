"""Qualification admission and proof gates; no Nix or live supervisor operations."""

import base64
import contextlib
import io
import json
import os
from pathlib import Path
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import re
import signal
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from urllib.error import HTTPError
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts/nix-source-qualification"
sys.path.insert(0, str(SCRIPTS))
import driver
import build_diagnostics
import probe
import service

HASH = "sha256-" + base64.b64encode(bytes(range(32))).decode()
DRV = "/nix/store/fixture-openclaw-gateway-pnpm-deps.drv"
LOGGING_DRV = "/nix/store/fixture-logging.drv"
LOGGING_HASH = "sha256-" + base64.b64encode(driver.hashlib.sha256(b"nix-source-logging-fixture\n").digest()).decode()
LOGGING_MARKER = b'{"nixLoggingFixture":"builder-marker"}\n'
HOSTED = {
    "GITHUB_ACTIONS": "true", "RUNNER_ENVIRONMENT": "github-hosted",
    "GITHUB_REPOSITORY": "openclaw/releases", "GITHUB_EVENT_NAME": "workflow_dispatch",
    "GITHUB_REF": driver.BRANCH, "GITHUB_ACTOR": "vincentkoc",
    "GITHUB_TRIGGERING_ACTOR": "vincentkoc", "GITHUB_SHA": "a" * 40,
    "NIX_QUALIFIER_SYSTEM": "x86_64-linux",
}


def build_activity(ident, drv=DRV, parent=0):
    return {"action": "start", "id": ident, "parent": parent, "type": 105, "fields": [drv, "", 1, 1]}


def journal_bytes(events):
    return b"".join(json.dumps(event).encode() + b"\n" for event in events)


class AdmissionTests(unittest.TestCase):
    def test_source_dispatch_routes_darwin_continuation_without_upload_jobs(self):
        workflow = (ROOT / ".github/workflows/ci.yml").read_text()
        validate, native = workflow.split("\n  nix-source-qualification:\n", 1)
        include = re.search(r"include: >-\n(.*?)\n    runs-on:", native, re.S)
        self.assertIsNotNone(include, "prefetch requires a phase-dependent native matrix")
        expressions = {
            "validate": re.search(r"if: \$\{\{ (.*?) \}\}", validate).group(1),
            "native": re.search(r"if: >-\n(.*?)\n    permissions:", native, re.S).group(1),
            "matrix": include.group(1).strip().removeprefix("${{").removesuffix("}}").strip(),
        }
        github = {
            "event_name": "workflow_dispatch", "repository": "openclaw/releases",
            "ref": "refs/heads/test/nix-source-qualification-driver-20260910",
            "actor": "vincentkoc", "triggering_actor": "vincentkoc",
        }
        darwin = [{"os": "macos-26", "system": "aarch64-darwin"}]
        both = [{"os": "ubuntu-24.04", "system": "x86_64-linux"}, *darwin]
        cases = [
            ({}, {"nix_source_phase": "prefetch"}, True, False, darwin),
            ({}, {"nix_source_phase": "diagnostic"}, True, False, both),
            ({}, {"nix_source_phase": "qualify"}, True, False, both),
            ({}, {"nix_source_phase": "off"}, False, True, both),
            ({}, {"nix_source_phase": "invalid"}, False, False, both),
            ({}, {}, False, False, both),
            ({}, {"nix_source_phase": None}, False, False, both),
        ]
        for key, value in (
            ("event_name", "push"), ("event_name", "pull_request"),
            ("repository", "other/releases"), ("ref", "refs/heads/main"),
            ("actor", "other"), ("triggering_actor", "other"),
            ("actor", None), ("triggering_actor", None),
        ):
            cases.append(({key: value}, {"nix_source_phase": "prefetch"},
                          False, key == "event_name", darwin))
        # These predicates use string equality/boolean operators; execute their
        # actual text with Node, without copying the router or emulating Actions.
        result = subprocess.run(["node", "-e", """
const fs = require('node:fs'), vm = require('node:vm');
const {expressions, cases} = JSON.parse(fs.readFileSync(0, 'utf8'));
console.log(JSON.stringify(cases.map(context => Object.fromEntries(
  Object.entries(expressions).map(([key, expression]) =>
    [key, vm.runInNewContext(expression, {...context, fromJSON: JSON.parse}, {timeout: 100})])
))));
"""], input=json.dumps({
            "expressions": expressions,
            "cases": [{"github": github | changes, "inputs": inputs}
                      for changes, inputs, *_ in cases],
        }), text=True, capture_output=True, check=True)
        observed = json.loads(result.stdout)
        self.assertEqual(len(observed), len(cases))
        for case, actual in zip(cases, observed):
            changes, inputs, admitted, uploads, matrix = case
            with self.subTest(changes=changes, inputs=inputs):
                self.assertEqual(actual, {"native": admitted, "validate": uploads, "matrix": matrix})

    def test_source_dispatch_excludes_upload_jobs_and_keeps_read_only_permissions(self):
        workflow = (ROOT / ".github/workflows/ci.yml").read_text()
        validate, native = workflow.split("\n  nix-source-qualification:\n", 1)
        self.assertIn("if: ${{ github.event_name != 'workflow_dispatch' || inputs.nix_source_phase == 'off' }}", validate)
        self.assertIn("github.ref == 'refs/heads/test/nix-source-qualification-driver-20260910'", native)
        self.assertIn("github.repository == 'openclaw/releases'", native)
        self.assertIn("github.actor == 'vincentkoc' && github.triggering_actor == 'vincentkoc'", native)
        self.assertIn("permissions:\n      contents: read", native)
        self.assertIn("timeout-minutes: ${{ inputs.nix_source_phase == 'diagnostic' && 10 || 60 }}", native)
        self.assertIn("- name: Checkout exact public driver without credentials\n        timeout-minutes: 1", native)
        for forbidden in ("actions/cache", "actions/upload-artifact", "actions/download-artifact",
                          "secrets.", "contents: write", "actions: write", "persist-credentials: true"):
            self.assertNotIn(forbidden, native)

    def test_host_actor_branch_phase_platform_and_credentials_are_required(self):
        for changes, phase, accepted in [
            ({}, "install", True), ({}, "diagnostic", True), ({}, "prefetch", True), ({}, "qualify", True),
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
        tail = b"error: Cannot build '/nix/store/helper.drv'.\nLast 3 log lines:\n" + b"".join(
            b"> " + line + b"\n" for line in log.splitlines())
        for status, output, accepted in [
            (1, log, True), (1, b"\xffunrelated\n" + log, True), (0, log, False),
            (1, log.replace(DRV.encode(), b"/nix/store/transitive.drv"), False),
            (1, log + log, False), (1, b"compilation failed", False),
            (1, log.replace(HASH.encode(), driver.FAKE_HASH.encode()), False),
            (1, log + tail, True), (1, tail, False),
            (1, log.replace(DRV.encode(), b"/nix/store/transitive.drv") + tail, False),
            (1, log + log + tail, False),
        ]:
            with self.subTest(status=status, output=output):
                if accepted:
                    self.assertEqual(driver.dependency_mismatch(status, output, DRV), HASH)
                else:
                    with self.assertRaises(RuntimeError):
                        driver.dependency_mismatch(status, output, DRV)

    def test_all_shared_builds_request_unsuppressed_builder_logs(self):
        with tempfile.TemporaryDirectory() as td, patch.dict(os.environ, HOSTED):
            instance = driver.Driver(Path(td))
            instance.args = ["--file", "fixture.nix"]
            for stage, attribute in (("dependency-prefetch", "dependencies"),
                                     ("package-contents", "contents"), ("native-ownership", "ownership"),
                                     ("qualification", "linux"), ("activation", "activation"), ("inputs", "inputs")):
                with self.subTest(stage=stage), patch.object(instance, "command") as command:
                    instance.build(stage, attribute)
                    argv = command.call_args.args[1]
                    self.assertEqual(argv[argv.index("--log-format") + 1], "raw-with-logs")
                    self.assertNotIn("--print-build-logs", argv)
                    self.assertNotIn("-L", argv)
                    self.assertNotIn("json-log-path", argv)
                    self.assertEqual(argv[-1], attribute)

    def test_timeout_diagnostic_uses_duration_without_inspecting_argv(self):
        error = subprocess.TimeoutExpired(
            ["nix", "--option", "access-tokens", "", "https://example.invalid/private", "secret-canary"], 12.5)
        fields = vars(error).copy()
        with patch.object(subprocess.TimeoutExpired, "__str__", side_effect=AssertionError("argv disclosure")):
            self.assertEqual(driver.failure_diagnostic(error, b""), ["TimeoutExpired after 12.5 seconds"])
            verbose = driver.failure_diagnostic(error, b"error: failed\n" * 20)
            self.assertEqual(verbose[0], "TimeoutExpired after 12.5 seconds")
            self.assertEqual(len(verbose), 6)
        self.assertEqual(vars(error), fields)

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

    def test_subprocess_bytes_and_normal_return_contract_are_preserved(self):
        for code, check in ((0, True), (7, False), (7, True)):
            with self.subTest(code=code, check=check), tempfile.TemporaryDirectory() as td, \
                    patch.dict(os.environ, HOSTED):
                command = driver.Driver(Path(td))
                output = io.StringIO()
                args = [sys.executable, "-c",
                        'import sys;sys.stdout.buffer.write(b"\\xffprivate");'
                        f'sys.stderr.buffer.write(b"\\xfediagnostic");sys.exit({code})']
                with contextlib.redirect_stdout(output):
                    if code and check:
                        with self.assertRaises(subprocess.CalledProcessError) as failure:
                            command.command("fixture", args)
                        result = failure.exception
                        self.assertEqual(result.cmd, args)
                    else:
                        result = command.command("fixture", args, check=check)
                        self.assertEqual(result.args, args)
                self.assertEqual(result.returncode, code)
                self.assertEqual(result.stdout, b"\xffprivate")
                self.assertEqual(result.stderr, b"\xfediagnostic")
                self.assertEqual((Path(td) / "fixture.stdout").read_bytes(), result.stdout)
                self.assertEqual((Path(td) / "fixture.stderr").read_bytes(), result.stderr)
                events = [json.loads(line) for line in output.getvalue().splitlines()]
                self.assertEqual(events, [
                    {"stage": "fixture", "status": "started"},
                    ({"stage": "fixture", "status": "failed", "exception": "CalledProcessError"}
                     if code and check else {"stage": "fixture", "status": "completed", "exit": code}),
                ])

    def test_capture_preserves_the_original_exception_without_attaching_output(self):
        error = RuntimeError("fixture failure")
        with tempfile.TemporaryDirectory() as td, patch.dict(os.environ, HOSTED):
            instance = driver.Driver(Path(td))
            def failure(*args, stdout, stderr):
                stdout.write(b"\xffbefore")
                stderr.write(b"\xfeinterrupted")
                raise error
            with patch.object(driver, "run", side_effect=failure), contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaises(RuntimeError) as caught:
                    instance.command("fixture", ["fixture"])
            self.assertIs(caught.exception, error)
            self.assertEqual(vars(error), {})
            self.assertEqual((Path(td) / "fixture.stdout").read_bytes(), b"\xffbefore")
            self.assertEqual((Path(td) / "fixture.stderr").read_bytes(), b"\xfeinterrupted")

    def test_failure_stderr_tail_is_bounded_without_truncating_private_capture(self):
        with tempfile.TemporaryDirectory() as td, patch.dict(os.environ, HOSTED):
            instance = driver.Driver(Path(td))
            data = b"error: excluded prefix\n" + b"x" * (2 * build_diagnostics.RECORD_LIMIT) + b"\nerror: retained\n"
            def failure(args, env, check, timeout, grace, *, stdout, stderr):
                stderr.write(data)
                return subprocess.CompletedProcess(args, 7)
            with patch.object(driver, "run", failure), contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaises(subprocess.CalledProcessError) as caught:
                    instance.command("fixture", ["fixture"])
            path = Path(td) / "fixture.stderr"
            self.assertEqual(path.read_bytes(), data)
            self.assertEqual(caught.exception.stderr, b"error: retained\n")
            self.assertEqual(driver.stderr_tail(path), caught.exception.stderr)
            self.assertEqual(driver.failure_diagnostic(caught.exception, data), ["error: retained"])

    def test_shared_deadline_spends_remaining_time_and_stops_before_spawn(self):
        with tempfile.TemporaryDirectory() as td, patch.dict(os.environ, HOSTED):
            instance = driver.Driver(Path(td))
            instance.deadline = 150
            budgets = []
            def complete(args, env, check, timeout, grace, **streams):
                budgets.append(timeout)
                return subprocess.CompletedProcess(args, 0)
            with patch.object(driver.time, "monotonic", side_effect=[100, 110, 121]), \
                    patch.object(driver, "run", side_effect=complete) as run, \
                    contextlib.redirect_stdout(io.StringIO()):
                instance.command("first", ["fixture"])
                instance.command("second", ["fixture"])
                with self.assertRaisesRegex(TimeoutError, "deadline exhausted"):
                    instance.command("third", ["fixture"])
            self.assertEqual(budgets, [20, 10])
            self.assertEqual(run.call_count, 2)

    def test_qualification_reserves_longer_cleanup_within_shared_deadline(self):
        with tempfile.TemporaryDirectory() as td, patch.dict(os.environ, HOSTED):
            instance = driver.Driver(Path(td))
            instance.deadline = 500
            budgets = []
            def complete(args, env, check, timeout, grace, **streams):
                budgets.append(timeout)
                return subprocess.CompletedProcess(args, 0)
            with patch.object(driver.time, "monotonic", return_value=100), \
                    patch.object(driver, "run", side_effect=complete), \
                    contextlib.redirect_stdout(io.StringIO()):
                instance.command("ordinary", ["fixture"])
                instance.command("qualification", ["fixture"], timeout=600,
                                 terminate_grace=service.PROBE_CLEANUP_BUDGET)
                instance.command("short", ["fixture"], timeout=15,
                                 terminate_grace=service.PROBE_CLEANUP_BUDGET)
            self.assertEqual(budgets, [370, 264, 15])

    def test_install_and_all_native_phases_share_one_deadline_without_reset(self):
        for phase, budget in (("diagnostic", 480), ("prefetch", 3480), ("qualify", 3480)):
            with self.subTest(phase=phase):
                self.check_phase_deadline(phase, budget)

    def check_phase_deadline(self, native_phase, budget):
        with tempfile.TemporaryDirectory() as td, patch.dict(os.environ, HOSTED | {
            "RUNNER_TEMP": td, "GITHUB_EVENT_PATH": str(Path(td) / "event.json"),
        }, clear=True):
            (Path(td) / "event.json").write_text(json.dumps({"inputs": {"nix_source_phase": native_phase}}))
            instances = []
            commands = []
            def install(instance, timeout):
                instances.append(("install", instance.deadline, timeout))
            def native(instance, phase):
                instances.append((phase, instance.deadline, None))
            def command(instance, stage, args, **kwargs):
                commands.append(stage)
                return subprocess.CompletedProcess(args, 0, b"a" * 40 if args[1] == "rev-parse" else b"", b"")
            with patch.object(driver.Driver, "command", command), patch.object(driver.Driver, "install", install), \
                    patch.object(driver.Driver, "native", native), \
                    patch.object(driver.platform, "machine", return_value="x86_64"), \
                    patch.object(driver.sys, "platform", "linux"), contextlib.redirect_stdout(io.StringIO()):
                for phase, now in (("install", 100), (native_phase, 200)):
                    with patch.object(sys, "argv", ["driver.py", phase]), \
                            patch.object(driver.time, "monotonic", return_value=now):
                        self.assertEqual(driver.main(), 0)
                deadline = 100 + budget
                self.assertEqual(instances, [
                    ("install", deadline, 180 if native_phase == "diagnostic" else 3600),
                    (native_phase, deadline, None),
                ])
                deadline_path = Path(td) / "nix-source-qualification/phase-deadline"
                with patch.object(sys, "argv", ["driver.py", "install"]), \
                        patch.object(driver.time, "monotonic", return_value=250):
                    self.assertEqual(driver.main(), 1)
                self.assertEqual(float(deadline_path.read_text()), deadline)
                with patch.object(sys, "argv", ["driver.py", native_phase]), \
                        patch.object(driver.time, "monotonic", return_value=deadline + 1):
                    self.assertEqual(driver.main(), 1)
                deadline_path.unlink()
                with patch.object(sys, "argv", ["driver.py", native_phase]):
                    self.assertEqual(driver.main(), 1)
                self.assertEqual(len(instances), 2)
                self.assertEqual(len(commands), 4)

    def test_normal_installer_keeps_its_prior_budget_for_command_clipping(self):
        for deadline in (None, 500):
            with self.subTest(deadline=deadline), tempfile.TemporaryDirectory() as td, \
                    patch.dict(os.environ, HOSTED), patch.object(driver.shutil, "which", return_value=None):
                instance = driver.Driver(Path(td))
                instance.deadline = deadline
                installer = b"fixture installer"
                with patch.object(driver, "INSTALLER_HASH", driver.hashlib.sha256(installer).hexdigest()), \
                        patch.object(instance, "command", return_value=subprocess.CompletedProcess([], 0, installer, b"")) as command:
                    instance.install()
                self.assertEqual(command.call_args.kwargs["timeout"], 3600)

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

    def test_diagnostic_and_prefetch_stop_before_package_or_activation(self):
        for phase in ("diagnostic", "prefetch"):
            with self.subTest(phase=phase):
                self.check_discovery_phase(phase)

    def test_prefetch_stops_before_dependencies_when_logging_fixture_is_unproven(self):
        for failure in ("marker", "hash", "phase", "activity", "private", "timeout", "no-build"):
            with self.subTest(failure=failure):
                self.check_discovery_phase("prefetch", failure)

    def test_duplicate_fixture_marker_rendering_does_not_imply_another_build(self):
        self.check_discovery_phase("prefetch", "duplicate-marker")

    def check_discovery_phase(self, phase, fixture_failure=None):
        with tempfile.TemporaryDirectory() as td, patch.dict(os.environ, HOSTED):
            instance = driver.Driver(Path(td))
            instance.deadline = time.monotonic() + driver.SOURCE_PHASE_BUDGET
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
                    "metadata": metadata, "dependency-drv": DRV, "logging-fixture-drv": LOGGING_DRV,
                }
                if stage in ("dependency-prefetch", "logging-fixture"):
                    fixture = stage == "logging-fixture"
                    selected_drv, selected_hash = (LOGGING_DRV, LOGGING_HASH) if fixture else (DRV, HASH)
                    journal = Path(args[args.index("json-log-path") + 1])
                    self.assertEqual(journal.stat().st_mode & 0o777, 0o600)
                    self.assertEqual(journal.parent.stat().st_mode & 0o777, 0o700)
                    self.assertEqual(journal.read_bytes(), b"")
                    self.assertEqual(args[args.index("--log-format") + 1], "raw-with-logs")
                    events = [build_activity(1, selected_drv),
                              {"action": "result", "id": 1, "type": 104, "fields": ["buildPhase"]},
                              {"action": "stop", "id": 1}]
                    if fixture and fixture_failure == "activity":
                        events[0]["fields"][0] = "/nix/store/unrelated.drv"
                    if fixture and fixture_failure == "phase":
                        events[1]["id"] = 2
                    if fixture and fixture_failure == "no-build":
                        events = []
                    journal.write_bytes(journal_bytes(events))
                    if fixture and fixture_failure == "private":
                        journal.chmod(0o644)
                    if fixture and fixture_failure == "timeout":
                        raise subprocess.TimeoutExpired(["nix", "secret-canary"], 90)
                    if fixture and fixture_failure == "hash":
                        selected_hash = HASH
                    log = (f"hash mismatch in fixed-output derivation '{selected_drv}':\n"
                           f"specified: {driver.FAKE_HASH}\ngot: {selected_hash}\n").encode()
                    if fixture and fixture_failure != "marker":
                        log = LOGGING_MARKER + log
                    if fixture and fixture_failure == "duplicate-marker":
                        log = LOGGING_MARKER + log
                    (Path(td) / f"{stage}.stderr").write_bytes(log)
                    return subprocess.CompletedProcess([], 1, b"", log)
                if stage == "dependency-dry-run":
                    return subprocess.CompletedProcess([], 0, b'[{"drvPath":"fixture","outputs":{}}]', b"")
                return subprocess.CompletedProcess([], 0, json.dumps(values[stage]).encode(), b"")
            config = {key: {"value": False if key in ("always-allow-substitutes", "accept-flake-config") else ""}
                      for key in ("always-allow-substitutes", "accept-flake-config", "post-build-hook", "builders", "access-tokens")}
            results = [subprocess.CompletedProcess([], 0, json.dumps(config).encode(), b""),
                       subprocess.CompletedProcess([], 0, b"nix (Nix) 2.35.2\n", b"")]
            output = io.StringIO()
            with patch.object(instance, "command", side_effect=results), patch.object(instance, "nix", side_effect=nix), \
                    contextlib.redirect_stdout(output):
                if fixture_failure and fixture_failure != "duplicate-marker":
                    with self.assertRaises((RuntimeError, subprocess.TimeoutExpired)):
                        instance.native(phase)
                else:
                    instance.native(phase)
            events = [json.loads(line) for line in output.getvalue().splitlines()]
            self.assertEqual(events[0], {"stage": "metadata-contract", "status": "completed"})
            if fixture_failure and fixture_failure != "duplicate-marker":
                self.assertEqual(calls[-1][0], "logging-fixture")
                self.assertFalse(any(event.get("result") in ("DISCOVERED", "PASS") for event in events))
                return
            receipt = events[-1]
            self.assertIs(receipt["packageProof"], False)
            if phase == "prefetch":
                self.assertEqual(receipt["result"], "DISCOVERED")
                self.assertEqual(receipt["pnpmDepsHash"], HASH)
                self.assertEqual([stage for stage, _, _ in calls],
                                 ["source-prefetch", "cache-config", "metadata", "logging-fixture-drv",
                                  "logging-fixture", "dependency-drv", "dependency-prefetch"])
                self.assertIn({"stage": "logging-fixture-contract", "status": "completed", "packageProof": False}, events)
                captures = [event for event in events if "activityDiagnostic" in event]
                self.assertEqual([event["stage"] for event in captures], ["logging-fixture", "dependency-prefetch"])
            else:
                self.assertEqual(receipt["result"], "DIAGNOSTIC")
                self.assertNotIn("pnpmDepsHash", receipt)
                self.assertEqual([stage for stage, _, _ in calls],
                                 ["source-prefetch", "cache-config", "metadata", "dependency-dry-run"])
                self.assertEqual(calls[-1][1], "build")
                self.assertEqual(calls[-1][2][:3], ("--dry-run", "--json", "--no-link"))
                options = instance.nix_options
                self.assertEqual(options[options.index("allow-import-from-derivation") + 1], "false")
            self.assertIn("https://github.com/openclaw/openclaw/archive/" + metadata["sourceCommit"] + ".tar.gz", calls[0][2])
            self.assertEqual(calls[-1][2][-1], "dependencies")


class BuildDiagnosticsTests(unittest.TestCase):
    def project(self, records):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "journal"
            path.write_bytes(records)
            path.chmod(0o600)
            return build_diagnostics.activity_diagnostic(path, DRV)

    def test_interleaving_correlates_only_known_activity_ids_and_exact_derivations(self):
        events = [
            {"action": "start", "id": 1, "parent": 0, "type": 104},
            build_activity(2, parent=1), build_activity(3, "/nix/store/other.drv", parent=1),
            {"action": "start", "id": 4, "parent": 3, "type": 101, "fields": ["https://example.invalid/private"]},
            {"action": "result", "id": 2, "type": 104, "fields": ["unpackPhase"]},
            {"action": "result", "id": 3, "type": 104, "fields": ["buildPhase"]},
            {"action": "result", "id": 2, "type": 105, "fields": [1, 2, 3, 4]},
            {"action": "result", "id": 4, "type": 104, "fields": ["installPhase"]},
            {"action": "result", "id": 2, "type": 104, "fields": ["installPhase"]},
            {"action": "stop", "id": 3},
        ]
        result = self.project(journal_bytes(events))
        self.assertEqual(result["coverage"], "observed-records")
        rows = {row["id"]: row for row in result["activities"]}
        self.assertEqual(rows[2], {
            "id": 2, "parent": 1, "type": 105, "derivation": "selected", "stop": "unknown",
            "derivationName": "unknown",
            "lastPhase": "installPhase", "progress": {"done": 1, "expected": 2, "running": 3, "failed": 4},
        })
        self.assertEqual(rows[3]["derivation"], "other")
        self.assertEqual(rows[3]["stop"], "observed")
        self.assertEqual(rows[3]["lastPhase"], "buildPhase")
        self.assertEqual(rows[4]["derivation"], "unknown")
        self.assertEqual(rows[4]["lastPhase"], "unknown")
        self.assertNotIn("success", json.dumps(result))

    def test_arbitrary_fields_and_secret_canaries_never_escape(self):
        canary = "secret-canary https://example.invalid/private /home/operator/private token=fixture-sensitive"
        events = [
            build_activity(1) | {"text": canary, "argv": [canary], "env": {"key": canary}},
            {"action": "msg", "msg": canary, "raw_msg": canary},
            {"action": "result", "id": 1, "type": 101, "fields": [canary]},
            {"action": "result", "id": 1, "type": 104, "fields": [canary]},
        ]
        result = self.project(journal_bytes(events))
        text = json.dumps(result)
        self.assertEqual(result["activities"][0]["lastPhase"], "unknown")
        for private in (canary, "secret-canary", "example.invalid", "/home/", "fixture-sensitive", DRV):
            self.assertNotIn(private, text)

    def test_only_validated_public_derivation_basenames_escape(self):
        prefix = "/nix/store/" + "0" * 32 + "-"
        for value, expected in (
            (prefix + "bash-5.3p3.drv", "0" * 32 + "-bash-5.3p3.drv"),
            (prefix + "nodejs-24.19.0-aarch64-apple-darwin.drv",
             "0" * 32 + "-nodejs-24.19.0-aarch64-apple-darwin.drv"),
            ("/nix/store/short-hash-bash.drv", "unknown"),
            ("/nix/store/" + "e" * 32 + "-bash.drv", "unknown"),
            (prefix + "token-fixture-sensitive.drv", "unknown"),
            (prefix + "192.0.2.40.drv", "unknown"),
            (prefix + "server.internal.drv", "unknown"),
            (prefix + "person@example.invalid.drv", "unknown"),
            (prefix + "name with spaces.drv", "unknown"),
            (prefix + "x" * 161 + ".drv", "unknown"),
            (prefix + "nested/home/operator/private.drv", "unknown"),
            (prefix + "https://example.invalid/private.drv", "unknown"),
        ):
            with self.subTest(value=value):
                result = self.project(journal_bytes([build_activity(1, value)]))
                row = result["activities"][0]
                self.assertEqual(row["derivationName"], expected)
                self.assertNotIn(value, json.dumps(result))

    def test_projection_failure_preserves_original_exception_and_cleanup_cause(self):
        original = subprocess.TimeoutExpired(["nix", "secret-canary"], 12.5)
        cause = PermissionError("fixture cleanup denial")
        original.__cause__ = cause
        fields = vars(original).copy()
        with tempfile.TemporaryDirectory() as td, patch.dict(os.environ, HOSTED):
            instance = driver.Driver(Path(td))
            output = io.StringIO()
            with patch.object(instance, "build", side_effect=original), \
                    patch.object(driver, "activity_diagnostic", side_effect=RuntimeError("secret-canary")), \
                    contextlib.redirect_stdout(output):
                with self.assertRaises(subprocess.TimeoutExpired) as caught:
                    instance.prefetch_build("dependency-prefetch", "dependencies", DRV)
            self.assertIs(caught.exception, original)
            self.assertIs(original.__cause__, cause)
            self.assertEqual(vars(original), fields)
            diagnostic = json.loads(output.getvalue())["activityDiagnostic"]
            self.assertEqual(diagnostic["coverage"], "unknown")
            self.assertEqual(diagnostic["activities"], [])
            self.assertNotIn("secret-canary", output.getvalue())

    def test_malformed_incomplete_or_uncorrelated_records_are_explicitly_unknown(self):
        start = journal_bytes([build_activity(1)])
        for data in (
            b"", b"{", start[:-1], start + b"\xff\n", start + b"[]\n",
            start + b'{"action":"stop","id":1,"id":2}\n',
            journal_bytes([build_activity(True)]),
            journal_bytes([build_activity(1, parent=2)]),
            journal_bytes([build_activity(1, parent=1)]),
            journal_bytes([build_activity(1), build_activity(1)]),
            journal_bytes([{"action": "stop", "id": 2}]),
            start + journal_bytes([{"action": "result", "id": 1, "type": 105, "fields": [True, 0, 0, 0]}]),
            start + journal_bytes([{"action": "result", "id": 1, "type": 104, "fields": []}]),
            journal_bytes([build_activity(1) | {"fields": ["secret-canary", "", 1, 1]}]),
        ):
            with self.subTest(data=data):
                result = self.project(data)
                self.assertEqual(result["coverage"], "unknown")
                self.assertTrue(result["gaps"])
                self.assertNotIn("secret-canary", json.dumps(result))
        missing = build_diagnostics.activity_diagnostic(Path("/nonexistent-fixture-journal"), DRV)
        self.assertEqual(missing["coverage"], "unknown")

    def test_real_processing_caps_bound_projection_and_keep_positive_selected_rows(self):
        oversized = b'{"action":"msg","msg":"' + b"x" * build_diagnostics.RECORD_LIMIT + b'"}\n'
        message = journal_bytes([{"action": "msg", "msg": "x" * 60000}])
        cases = [
            oversized,
            message * (build_diagnostics.SCAN_LIMIT // len(message) + 1),
            journal_bytes([build_activity(index, "/nix/store/other.drv") for index in range(1, 258)]),
        ]
        for records in cases:
            with self.subTest(size=len(records)):
                result = self.project(records)
                self.assertEqual(result["coverage"], "unknown")
                self.assertLessEqual(len(result["activities"]), 8)
                self.assertLessEqual(len(json.dumps({"stage": "dependency-prefetch", "activityDiagnostic": result})), 4096)
        events = [build_activity(1), {"action": "result", "id": 1, "type": 104, "fields": ["buildPhase"]}]
        events.extend(build_activity(index, "/nix/store/other.drv") for index in range(2, 30))
        result = self.project(journal_bytes(events))
        self.assertEqual(result["gaps"], ["row-limit"])
        self.assertEqual(result["activities"][-1]["derivation"], "selected")
        maximal = []
        for ident in range(1, 9):
            maximal.extend([
                build_activity(ident, "/nix/store/" + "0" * 32 + "-" + "x" * 160 + ".drv"),
                {"action": "result", "id": ident, "type": 105, "fields": [2**64 - 1] * 4},
            ])
        result = self.project(journal_bytes(maximal))
        self.assertLessEqual(len(json.dumps({"stage": "dependency-prefetch", "activityDiagnostic": result})), 4096)
        with patch.object(build_diagnostics.time, "monotonic", side_effect=[0, 2, 2]):
            result = self.project(journal_bytes([build_activity(1)]))
        self.assertIn("time-limit", result["gaps"])

    def test_prefetch_captures_are_private_fresh_and_never_supply_hash_authority(self):
        with tempfile.TemporaryDirectory() as td, patch.dict(os.environ, HOSTED):
            instance = driver.Driver(Path(td))
            captures = []
            error = subprocess.TimeoutExpired(["nix", "secret-canary"], 1)
            fields = vars(error).copy()
            def build(stage, attribute, check, journal):
                captures.append(journal)
                self.assertEqual(journal.read_bytes(), b"")
                self.assertEqual(journal.stat().st_mode & 0o777, 0o600)
                self.assertEqual(journal.parent.stat().st_mode & 0o777, 0o700)
                journal.write_bytes(journal_bytes([
                    build_activity(1), {"action": "result", "id": 1, "type": 104, "fields": ["buildPhase"]},
                    {"action": "stop", "id": 1},
                ]))
                if len(captures) == 1:
                    raise error
                return subprocess.CompletedProcess([], 1, b"", b"compilation failed")
            output = io.StringIO()
            old_mask = os.umask(0o022)
            try:
                with patch.object(instance, "build", build), contextlib.redirect_stdout(output):
                    with self.assertRaises(subprocess.TimeoutExpired) as caught:
                        instance.prefetch_build("dependency-prefetch", "dependencies", DRV)
                    self.assertIs(caught.exception, error)
                    with self.assertRaisesRegex(RuntimeError, "classified selected"):
                        instance.prefetch_build("dependency-prefetch", "dependencies", DRV)
            finally:
                os.umask(old_mask)
            self.assertEqual(vars(error), fields)
            self.assertNotEqual(captures[0], captures[1])
            self.assertEqual(captures[0].read_bytes(), captures[1].read_bytes())
            receipts = [json.loads(line) for line in output.getvalue().splitlines()]
            self.assertEqual(len(receipts), 2)
            self.assertTrue(all(event["activityDiagnostic"]["privateCapture"] for event in receipts))
            self.assertFalse(any("result" in event for event in receipts))
            with patch.object(driver.tempfile, "mkdtemp", return_value=str(captures[0].parent)), \
                    patch.object(instance, "build") as build:
                with self.assertRaises(FileExistsError):
                    instance.prefetch_build("dependency-prefetch", "dependencies", DRV)
                build.assert_not_called()

    def test_phase_script_emits_known_marker_and_output_bytes(self):
        with tempfile.TemporaryDirectory() as td:
            output = Path(td) / "out"
            result = subprocess.run(["bash", SCRIPTS / "logging-fixture.sh"],
                                    env={"PATH": os.environ["PATH"], "out": str(output)},
                                    capture_output=True, check=True, cwd=td)
            self.assertEqual(result.stderr, LOGGING_MARKER)
            self.assertEqual(result.stdout, b"")
            self.assertEqual(output.read_bytes(), b"nix-source-logging-fixture\n")

    def test_fixture_deadline_includes_evaluation_build_and_reporting_without_reset(self):
        for global_deadline in (1100, 5000):
            with self.subTest(global_deadline=global_deadline), tempfile.TemporaryDirectory() as td, \
                    patch.dict(os.environ, HOSTED):
                instance = driver.Driver(Path(td))
                instance.deadline = global_deadline
                instance.args = ["--file", "fixture.nix"]
                now = [1000]
                observed = []
                def nix(*args):
                    observed.append(instance.deadline)
                    now[0] += 10
                    return subprocess.CompletedProcess([], 0, json.dumps(LOGGING_DRV).encode(), b"")
                def prefetch(*args):
                    observed.append(instance.deadline)
                    now[0] += 10
                    (Path(td) / "logging-fixture.stderr").write_bytes(LOGGING_MARKER)
                    return LOGGING_HASH, {
                        "privateCapture": True, "gaps": [],
                        "activities": [{"type": 105, "derivation": "selected", "lastPhase": "buildPhase"}],
                    }
                with patch.object(driver.time, "monotonic", side_effect=lambda: now[0]), \
                        patch.object(instance, "nix", nix), patch.object(instance, "prefetch_build", prefetch), \
                        contextlib.redirect_stdout(io.StringIO()):
                    instance.verify_build_logging()
                    self.assertEqual(observed, [min(global_deadline, 1120)] * 2)
                    self.assertEqual(instance.deadline, global_deadline)
                    now[0] = global_deadline
                    with self.assertRaisesRegex(RuntimeError, "deadline exhausted"):
                        instance.verify_build_logging()
                    self.assertEqual(instance.deadline, global_deadline)


class IsolationTests(unittest.TestCase):
    def test_cleanup_denials_preserve_original_cause_bytes_and_blocked_receipt(self):
        for index, denied_signal in enumerate((signal.SIGTERM, 0, signal.SIGKILL)):
            with self.subTest(denied_signal=denied_signal), tempfile.TemporaryDirectory() as td:
                directory = Path(td)
                event = directory / "event.json"
                event.write_text(json.dumps({"inputs": {"nix_source_phase": "diagnostic"}}))
                original = subprocess.TimeoutExpired(["fixture"], 0)
                original_fields = vars(original).copy()
                denied = PermissionError("fixture cleanup denied")
                process = Mock(pid=12345, stdout=None, stderr=None)
                process.communicate.side_effect = [original, (None, None)]
                observed, signals = [], []

                def killpg(group, sig):
                    self.assertEqual(group, process.pid)
                    self.assertEqual(signal.getsignal(signal.SIGINT), signal.SIG_IGN)
                    self.assertEqual(signal.getsignal(signal.SIGTERM), signal.SIG_IGN)
                    signals.append(sig)
                    if sig == denied_signal:
                        raise denied

                def command(args, env, check, timeout, grace, *, stdout, stderr):
                    if args[0] == "git":
                        stdout.write(b"a" * 40 if args[1] == "rev-parse" else b"")
                        return subprocess.CompletedProcess(args, 0)
                    stdout.write(b"\xffbefore")
                    stderr.write(b"\xfebefore")
                    try:
                        return service.run(args, env, check, timeout, grace, stdout=stdout, stderr=stderr)
                    except BaseException as error:
                        observed.append(error)
                        raise

                def install(instance, **kwargs):
                    instance.command("fixture", ["fixture"], timeout=0, terminate_grace=0)

                receipts = io.StringIO()
                with patch.dict(os.environ, HOSTED | {"RUNNER_TEMP": td, "GITHUB_EVENT_PATH": str(event)}, clear=True), \
                        patch.object(driver.sys, "platform", "linux"), \
                        patch.object(driver.platform, "machine", return_value="x86_64"), \
                        patch.object(sys, "argv", ["driver.py", "install"]), \
                        patch.object(driver.Driver, "install", install), \
                        patch.object(driver, "run", command), \
                        patch.object(service.subprocess, "Popen", return_value=process), \
                        patch.object(service.os, "killpg", killpg), contextlib.redirect_stdout(receipts):
                    self.assertEqual(driver.main(), 1)
                self.assertEqual(len(observed), 1)
                self.assertIs(observed[0], original)
                self.assertIs(original.__cause__, denied)
                self.assertEqual(vars(original), original_fields)
                self.assertEqual(signals, [signal.SIGTERM, 0, signal.SIGKILL][:index + 1])
                logs = directory / "nix-source-qualification"
                self.assertEqual((logs / "fixture.stdout").read_bytes(), b"\xffbefore")
                self.assertEqual((logs / "fixture.stderr").read_bytes(), b"\xfebefore")
                events = [json.loads(line) for line in receipts.getvalue().splitlines()]
                self.assertEqual(events[-2], {"stage": "fixture", "status": "failed", "exception": "TimeoutExpired"})
                self.assertEqual(events[-1], {
                    "result": "BLOCKED", "stage": "fixture", "exception": "TimeoutExpired",
                    "exit": 1, "diagnostic": ["TimeoutExpired after 0 seconds"], "cleanupException": "PermissionError",
                })

    def test_service_pipe_defaults_and_caller_owned_files(self):
        args = [sys.executable, "-c", 'import sys;sys.stdout.buffer.write(b"\\xffout");sys.stderr.buffer.write(b"\\xfeerr")']
        result = service.run(args, os.environ)
        self.assertEqual((result.stdout, result.stderr), (b"\xffout", b"\xfeerr"))
        with tempfile.TemporaryFile() as stdout, tempfile.TemporaryFile() as stderr:
            result = service.run(args, os.environ, stdout=stdout, stderr=stderr)
            self.assertEqual((result.stdout, result.stderr), (None, None))
            self.assertFalse(stdout.closed or stderr.closed)
            stdout.seek(0)
            stderr.seek(0)
            self.assertEqual((stdout.read(), stderr.read()), (b"\xffout", b"\xfeerr"))

    def test_driver_preserves_interrupted_bytes_receipts_and_reaps_child(self):
        for mode in ("timeout", "sigterm", "sigint", "descendant", "cooperative", "cooperative-denial",
                     "cleanup-entry", "sigterm-entry", "sigint-entry"):
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as td:
                directory = Path(td)
                with (directory / "receipts").open("wb") as receipts:
                    parent = subprocess.Popen([
                        sys.executable, ROOT / "tests/nix_source_diagnostics_fixture.py", mode, directory,
                    ], stdout=receipts, stderr=subprocess.PIPE, start_new_session=True)
                try:
                    deadline = time.monotonic() + 10
                    while not (directory / "ready").exists():
                        if parent.poll() is not None or time.monotonic() >= deadline:
                            self.fail("diagnostic child did not become ready")
                        time.sleep(0.02)
                    started = (directory / "receipts").read_bytes()
                    timed_out = mode in ("timeout", "descendant", "cooperative", "cooperative-denial", "cleanup-entry")
                    if not timed_out:
                        parent.send_signal(signal.SIGTERM if mode.startswith("sigterm") else signal.SIGINT)
                    while not (directory / "teardown").exists():
                        if parent.poll() is not None:
                            break
                        if time.monotonic() >= deadline:
                            self.fail("diagnostic child did not enter teardown")
                        time.sleep(0.02)
                    # A later runner cancellation must not replace the first failure.
                    if parent.poll() is None:
                        parent.send_signal(signal.SIGINT)
                        parent.send_signal(signal.SIGTERM)
                    _, stderr = parent.communicate(timeout=10)
                    logs = directory / "nix-source-qualification"
                    events = [json.loads(line) for line in (directory / "receipts").read_bytes().splitlines()]
                    failure = "TimeoutExpired" if timed_out else "RuntimeError"
                    self.assertIn({"stage": "installer-download", "status": "failed", "exception": failure}, events,
                                  (logs / "installer-download.failure").read_text())
                    if mode.endswith("-entry"):
                        state = json.loads((directory / "signal-state.json").read_text())
                        self.assertEqual(state, {
                            "injected": True,
                            "entries": [] if timed_out else ["SIGTERM" if mode.startswith("sigterm") else "SIGINT"],
                            "maskPreserved": True, "handlersRestored": timed_out,
                        })
                    self.assertEqual((logs / "installer-download.stdout").read_bytes(), b"private stdout\xff\n")
                    self.assertEqual((logs / "installer-download.stderr").read_bytes(),
                                     b"error: private stderr\xfe\nerror: teardown complete\xfe\n")
                    self.assertIn({"stage": "installer-download", "status": "started"},
                                  [json.loads(line) for line in started.splitlines()])
                    self.assertEqual(events[-1]["result"], "BLOCKED")
                    self.assertEqual(events[-1]["exception"], failure)
                    if mode == "cooperative-denial":
                        self.assertEqual(events[-1]["cleanupException"], "PermissionError")
                    self.assertEqual(parent.returncode, 1, stderr.decode())
                    self.assertEqual(stderr, b"")
                    self.assertNotIn(b"private stdout", (directory / "receipts").read_bytes())
                    self.assertFalse(service.alive(int((directory / "child.pid").read_text())))
                    if mode in ("descendant", "cooperative", "cooperative-denial"):
                        group = (directory / "child.pid").read_text()
                        self.assertEqual((directory / "grandchild.pgid").read_text(), group)
                        # Only the direct child is waitpid-owned. Orphan zombies are not executing.
                        deadline = time.monotonic() + 5
                        while True:
                            states = subprocess.run(["ps", "-axo", "pgid=,stat="], check=True,
                                                    capture_output=True, text=True).stdout.splitlines()
                            running = [line for line in states if line.split()[0] == group
                                       and not line.split()[1].startswith("Z")]
                            if not running or time.monotonic() >= deadline:
                                break
                            time.sleep(0.02)
                        self.assertEqual(running, [])
                        if mode == "descendant":
                            self.assertGreaterEqual(time.monotonic() - float((directory / "teardown").read_text()), 0.2)
                finally:
                    if parent.poll() is None:
                        parent.kill()
                        parent.communicate()
                    pid_file = directory / "child.pid"
                    if pid_file.exists():
                        try:
                            os.killpg(int(pid_file.read_text()), signal.SIGKILL)
                        except ProcessLookupError:
                            pass
                    parent.stderr.close()

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
        handlers = {sig: signal.getsignal(sig) for sig in (signal.SIGINT, signal.SIGTERM)}
        with self.assertRaises(subprocess.TimeoutExpired) as failure:
            service.run([sys.executable, "-c",
                         "import os,signal;signal.signal(signal.SIGTERM,signal.SIG_IGN);"
                         "print(os.getpid(),flush=True);signal.pause()"],
                        os.environ, timeout=1, terminate_grace=0.05)
        self.assertFalse(service.alive(int(failure.exception.output.strip())))
        self.assertEqual({sig: signal.getsignal(sig) for sig in handlers}, handlers)

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


class UiParityTests(unittest.TestCase):
    def test_public_roots_and_nested_outputs_must_be_served_unchanged(self):
        document = b'<html><script src="./assets/app.js"></script><link rel="stylesheet" href="./assets/app.css"></html>'
        files = {
            "index.html": document,
            "assets/app.js": b"built script",
            "assets/app.css": b"built style",
            "assets/app.js.br": b"negotiated sidecar",
            "assets/app.js.gz": b"negotiated sidecar",
            "assets/app.js.map": b"diagnostic",
            "root.map": b"diagnostic",
            "sw.js": b"built service worker",
            "manifest.webmanifest": b'{"name":"built manifest"}',
            "favicon.ico": b"icon",
            "fonts/demo.css": b"built font stylesheet",
            "fonts/demo.woff2": b"font bytes",
            "provider-icons/ATTRIBUTION.md": b"public attribution",
            "asset-manifest.json": json.dumps({"assets": [
                {"path": name} for name in
                ("assets/app.js", "assets/app.css", "assets/app.js.br", "assets/app.js.gz")
            ]}).encode(),
        }
        served_files = {name: body for name, body in files.items()
                        if name != "index.html" and not name.endswith((".map", ".br", ".gz"))}
        served_files[""] = document.replace(b"<html>", b'<html data-runtime="fixture">').replace(b"./assets/", b"/assets/")
        requests = []
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                name = self.path.removeprefix("/")
                requests.append((name, self.headers.get("Accept-Encoding")))
                body = served_files.get(name)
                self.send_response(200 if body is not None else 404)
                self.send_header("Content-Type", "text/html" if name == "" else "application/octet-stream")
                self.end_headers()
                if body is not None:
                    self.wfile.write(body)

            def log_message(self, *args):
                pass

        with tempfile.TemporaryDirectory() as td, ThreadingHTTPServer(("127.0.0.1", 0), Handler) as server:
            root = Path(td)
            for name, body in files.items():
                target = root / "dist/control-ui" / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(body)
            thread = threading.Thread(target=server.serve_forever, kwargs={"poll_interval": 0.01})
            thread.start()
            try:
                with patch.object(probe, "PORT", str(server.server_port)):
                    with self.subTest(complete=True):
                        probe.verify_ui(root)
                        self.assertEqual({name for name, _ in requests}, set(served_files))
                        self.assertTrue(all(encoding == "identity" for _, encoding in requests))
                    for name in ("sw.js", "manifest.webmanifest", "asset-manifest.json", "favicon.ico",
                                 "fonts/demo.css", "fonts/demo.woff2", "provider-icons/ATTRIBUTION.md",
                                 "assets/app.js", "assets/app.css"):
                        for failure in ("wrong", "missing"):
                            with self.subTest(name=name, failure=failure):
                                if failure == "missing":
                                    served_files.pop(name)
                                else:
                                    served_files[name] = b"wrong served bytes"
                                try:
                                    with self.assertRaises((RuntimeError, HTTPError)) as failure_result:
                                        probe.verify_ui(root)
                                    if isinstance(failure_result.exception, HTTPError):
                                        failure_result.exception.close()
                                finally:
                                    served_files[name] = files[name]
            finally:
                server.shutdown()
                thread.join(timeout=5)
                self.assertFalse(thread.is_alive())


if __name__ == "__main__":
    unittest.main()
