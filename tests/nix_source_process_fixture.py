"""Real parent/probe signals with native setup and supervisor commands stubbed."""

import base64
import builtins
import json
import os
from pathlib import Path
import pwd
import runpy
import signal
import subprocess
import sys
import time
from types import SimpleNamespace
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts/nix-source-qualification"
sys.path.insert(0, str(SCRIPTS))
import driver
import service

mode, directory = sys.argv[1], Path(sys.argv[2])


def event(name):
    with (directory / "events").open("a") as output:
        output.write(name + "\n")


if mode == "probe":
    (directory / "probe.pid").write_text(str(os.getpid()))
    home = Path("/tmp/openclaw-source-qualification")
    stage = {
        "homeDirectory": str(home),
        "metadata": {"sourceCommit": "a" * 40},
        **{key: "/nix/store/fixture-" + key for key in (
            "activation", "gateway", "node", "pnpm", "plugin", "homeManager", "sourceManifest",
        )},
    }
    inputs = directory / "inputs.json"
    inputs.write_text(json.dumps(stage))

    def external_command(args, env, check=True, timeout=120):
        if args[0] == "nix-env":
            event("ready")
            signal.pause()
            raise AssertionError("activation was not interrupted")
        if args[:2] == ["launchctl", "bootout"]:
            event("cleanup-started")
            # Longer than the old parent's five-second SIGTERM escalation.
            time.sleep(6)
            event("stopped")
            return subprocess.CompletedProcess(args, 0, b"", b"")
        if args[:2] == ["launchctl", "print"]:
            if args[-1].endswith(service.LABEL):
                return subprocess.CompletedProcess(args, 1, b"", b"Could not find service")
            return subprocess.CompletedProcess(args, 0, b"", b"")
        raise AssertionError(f"unexpected native command: {args[0]}")

    original_resolve = Path.resolve
    original_print = builtins.print

    def output(*args, **kwargs):
        original_print(*args, **kwargs)
        if args == (json.dumps({"qualification": "cleanup", "verified": True}),):
            event("cleanup-verified")

    def resolve(path, strict=False):
        if str(path).startswith("/nix/store/fixture-"):
            return path
        return original_resolve(path, strict=strict)

    with patch.object(service, "run", side_effect=external_command), \
            patch("platform.system", return_value="Darwin"), \
            patch.object(pwd, "getpwuid", return_value=SimpleNamespace(pw_name="runner")), \
            patch.object(Path, "resolve", resolve), patch.object(Path, "glob", return_value=[]), \
            patch("os.path.lexists", return_value=False), patch.object(Path, "mkdir"), \
            patch.object(Path, "symlink_to"), patch.object(builtins, "print", side_effect=output), \
            patch.object(sys, "argv", ["probe.py", str(inputs)]):
        runpy.run_path(str(SCRIPTS / "probe.py"), run_name="__main__")
else:
    def interrupted(signum, frame):
        raise RuntimeError("parent interrupted")

    signal.signal(signal.SIGTERM, interrupted)
    os.environ["NIX_QUALIFIER_SYSTEM"] = "aarch64-darwin"

    class FixtureDriver(driver.Driver):
        def command(self, stage, args, check=True, env=None, timeout=3600, **kwargs):
            if stage == "qualification":
                return super().command(stage, [
                    sys.executable, __file__, "probe", directory,
                ], check, env, timeout=2 if mode == "timeout" else 20, **kwargs)
            if stage == "effective-config":
                value = {key: {"value": False if key in (
                    "always-allow-substitutes", "accept-flake-config",
                ) else ""} for key in (
                    "always-allow-substitutes", "accept-flake-config",
                    "post-build-hook", "builders", "access-tokens",
                )}
                return subprocess.CompletedProcess(args, 0, json.dumps(value).encode(), b"")
            if stage == "nix-version":
                return subprocess.CompletedProcess(args, 0, b"nix (Nix) 2.35.2\n", b"")
            raise AssertionError(f"unexpected command stage: {stage}")

        def nix(self, stage, command, *args, check=True):
            values = {
                "source-prefetch": {"storePath": str(directory), "hash": source_hash},
                "cache-config": {"extra-substituters": [], "extra-trusted-public-keys": []},
                "metadata": {
                    **{key: self.identity[key] for key in ("sourceCommit", "packagingCommit")},
                    "system": self.system, "version": "2026.9.3", "pnpm": "12.3.4",
                    "node": "24.19.0", "pinnedRev": None, "defaultNpmLazy": True,
                },
            }
            if stage in values:
                return subprocess.CompletedProcess(args, 0, json.dumps(values[stage]).encode(), b"")
            if stage in ("package-contents", "native-ownership", "activation", "inputs"):
                return subprocess.CompletedProcess(args, 0, b"fixture-inputs\n", b"")
            raise AssertionError(f"unexpected Nix stage: {stage}")

    instance = FixtureDriver(directory)
    source_hash = "sha256-" + base64.b64encode(bytes(range(32))).decode()
    instance.identity["systems"] = {
        system: {"sourceHash": source_hash, "pnpmDepsHash": source_hash}
        for system in driver.SYSTEMS.values()
    }
    try:
        with patch.object(driver.sys, "platform", "darwin"):
            instance.native("qualify")
    except Exception as error:
        event(type(error).__name__)
        sys.exit(1)
    raise AssertionError("interrupted qualification cannot pass")
