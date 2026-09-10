#!/usr/bin/env python3
"""Hosted-only source hash discovery and native package qualification."""

import base64
import fcntl
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import signal
import sys
import traceback

from service import COMMAND_TERM_GRACE, PROBE_CLEANUP_BUDGET, run

HERE = Path(__file__).resolve().parent
BRANCH = "refs/heads/test/nix-source-qualification-driver-20260910"
SYSTEMS = {("linux", "x86_64"): "x86_64-linux", ("darwin", "arm64"): "aarch64-darwin"}
INSTALLER_SHA = "13d8dd58da0234aa297dedd986986ccb8e7f3e24"
INSTALLER_HASH = "836671507d9b4ea84252f968bd0622c5c2fa72f5deea93f5764f1c60821062f6"
FAKE_HASH = "sha256-" + base64.b64encode(bytes(32)).decode()


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def runner_guard(phase):
    env = os.environ
    require(
        env.get("GITHUB_ACTIONS") == "true" and env.get("RUNNER_ENVIRONMENT") == "github-hosted"
        and env.get("GITHUB_REPOSITORY") == "openclaw/releases"
        and env.get("GITHUB_EVENT_NAME") == "workflow_dispatch" and env.get("GITHUB_REF") == BRANCH
        and env.get("GITHUB_ACTOR") == env.get("GITHUB_TRIGGERING_ACTOR") == "vincentkoc",
        "only the approved hosted branch/actor may run this driver",
    )
    require(phase in ("install", "prefetch", "qualify"), "unknown phase")
    require(not env.get("GH_TOKEN") and not env.get("GITHUB_TOKEN"), "credentials must not reach the driver")
    native = SYSTEMS.get((sys.platform, platform.machine()))
    require(native is not None and env.get("NIX_QUALIFIER_SYSTEM") == native, "native runner mismatch")
    require(re.fullmatch(r"[0-9a-f]{40}", env.get("GITHUB_SHA", "")), "workflow SHA must be immutable")


def valid_hash(value):
    if not isinstance(value, str) or not re.fullmatch(r"sha256-[A-Za-z0-9+/]{43}=", value):
        return False
    return value != FAKE_HASH and len(base64.b64decode(value[7:], validate=True)) == 32


def frozen_hashes(identity, system):
    require(set(identity["systems"]) == set(SYSTEMS.values()), "wrong qualification systems")
    for entry in identity["systems"].values():
        require(isinstance(entry, dict) and set(entry) == {"sourceHash", "pnpmDepsHash"}
                and all(valid_hash(value) for value in entry.values()), "native hashes are not frozen")
    require(len({entry["sourceHash"] for entry in identity["systems"].values()}) == 1,
            "systems disagree on selected source bytes")
    return identity["systems"][system]


def dependency_mismatch(status, log, drv):
    require(status != 0, "prefetch unexpectedly succeeded with a placeholder")
    # A transitive fetch or compilation failure is not this dependency hash.
    pattern = (
        rb"hash mismatch in fixed-output derivation '" + re.escape(drv.encode()) + rb"':\s*"
        rb"specified:\s*(sha256-[A-Za-z0-9+/=]+)\s*got:\s*(sha256-[A-Za-z0-9+/=]+)"
    )
    matches = re.findall(pattern, log)
    require(len(matches) == 1 and matches[0][0].decode() == FAKE_HASH,
            "expected one classified selected dependency mismatch")
    value = matches[0][1].decode()
    require(valid_hash(value), "invalid discovered dependency hash")
    return value


def fixture_complete(paths, status):
    events = []
    # Logs are bytes. Only these exact, closed receipts may escape the runner.
    for path in paths:
        if not path.exists():
            continue
        with path.open("rb") as lines:
            for line in lines:
                try:
                    value = json.loads(line[line.index(b"{"):])
                except ValueError:
                    continue
                if (isinstance(value, dict) and set(value) == {"qualification", "verified"}
                        and value["qualification"] in ("cleanup", "complete") and value["verified"] is True):
                    events.append(value["qualification"])
    return status == 0 and events == ["cleanup", "complete"]


def failure_diagnostic(error, stderr):
    lines = [str(error)] if not hasattr(error, "returncode") else []
    for line in stderr.decode("utf-8", errors="replace").splitlines():
        line = re.sub(r"\x1b\[[0-9;]*[A-Za-z]", "", line).strip()
        if re.search(r"(?i)(?:\berror\b|\bfailed\b|\bmissing:|\bTS\d{4}:)", line):
            lines.append(line)
    diagnostics = []
    for line in lines[-6:]:
        if re.search(r"(?i)(?:token|password|secret|authorization|bearer|private.key|gh[pousr]_|sk-)", line):
            line = "<credential-bearing diagnostic redacted>"
        line = re.sub(r"https?://\S+", "<url>", line)
        line = re.sub(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b", "<email>", line)
        line = re.sub(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", "<address>", line)
        line = re.sub(r"\b(?:[0-9a-fA-F]{1,4}:){2,}[0-9a-fA-F:]+\b", "<address>", line)
        line = re.sub(r"(?<![\w])/(?:[^\s'\"<>()[\]{}:,]+/?)+", "<path>", line)
        line = re.sub(r"\b[\w-]+\.(?:local|internal|lan)\b", "<host>", line)
        diagnostics.append(line[:240])
    return diagnostics or ["no recognized diagnostic; see failing stage and exit status"]


class Driver:
    def __init__(self, directory):
        self.directory = directory
        self.stage = "identity"
        self.identity = json.loads((HERE / "hashes.json").read_text())
        for key in ("sourceCommit", "packagingCommit"):
            value = self.identity.get(key)
            require(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{40}", value),
                    f"{key} must be a full immutable Git SHA")
        self.system = os.environ["NIX_QUALIFIER_SYSTEM"]
        self.env = dict(os.environ)
        self.nix_options = [
            "--extra-experimental-features", "nix-command flakes",
            "--option", "accept-flake-config", "false",
            "--option", "always-allow-substitutes", "false",
            "--option", "post-build-hook", "", "--option", "builders", "",
            "--option", "access-tokens", "",
        ]

    def command(self, stage, args, check=True, env=None, timeout=3600,
                terminate_grace=COMMAND_TERM_GRACE):
        self.stage = stage
        result = run(args, self.env if env is None else env, False, timeout, terminate_grace)
        (self.directory / f"{stage}.stdout").write_bytes(result.stdout)
        (self.directory / f"{stage}.stderr").write_bytes(result.stderr)
        if check:
            result.check_returncode()
        return result

    def nix(self, stage, command, *args, check=True):
        return self.command(stage, ["nix", *self.nix_options, command, *args], check)

    def install(self):
        require(shutil.which("nix") is None, "refusing an existing Nix installation")
        result = self.command("installer-download", [
            "curl", "--fail", "--silent", "--show-error", "--location", "--max-time", "60",
            f"https://raw.githubusercontent.com/cachix/install-nix-action/{INSTALLER_SHA}/install-nix.sh",
        ])
        require(hashlib.sha256(result.stdout).hexdigest() == INSTALLER_HASH, "installer digest mismatch")
        # The action wrapper injects/persists github.token. Invoke only its exact script.
        env = dict(self.env, INPUT_ENABLE_KVM="true" if sys.platform == "linux" else "false",
                   INPUT_SET_AS_TRUSTED_USER="true", INPUT_INSTALL_OPTIONS="", INPUT_INSTALL_URL="",
                   INPUT_GITHUB_ACCESS_TOKEN="", INPUT_EXTRA_NIX_CONFIG=(
                       "always-allow-substitutes = false\npost-build-hook =\nbuilders =\n"
                       "accept-flake-config = false\naccess-tokens ="))
        self.command("installer", ["bash", self.directory / "installer-download.stdout"], env=env)

    def native(self, phase):
        config = json.loads(self.command("effective-config", ["nix", "config", "show", "--json"]).stdout)
        require(config["always-allow-substitutes"]["value"] is False
                and config["accept-flake-config"]["value"] is False
                and all(not config[key]["value"] for key in ("post-build-hook", "builders", "access-tokens")),
                "unsafe effective Nix configuration")
        require(self.command("nix-version", ["nix", "--version"]).stdout.strip() == b"nix (Nix) 2.35.2",
                "unexpected Nix version")
        frozen = frozen_hashes(self.identity, self.system) if phase == "qualify" else None
        if phase == "qualify" and sys.platform == "linux":
            self.stage = "kvm-access"
            with open("/dev/kvm", "rb+", buffering=0) as device:
                require(fcntl.ioctl(device.fileno(), 0xAE00) == 12, "KVM API unavailable")
        # Do not let the driver/workflow identity masquerade as application provenance.
        self.env = {key: value for key, value in self.env.items()
                    if not key.startswith(("GIT_", "GITHUB_", "OPENCLAW_"))
                    and key not in ("NODE_OPTIONS", "NODE_PATH")}
        url = f"https://github.com/openclaw/openclaw/archive/{self.identity['sourceCommit']}.tar.gz"
        args = ["prefetch-file", "--unpack", "--json", url]
        if frozen:
            args.extend(["--expected-hash", frozen["sourceHash"]])
        source = json.loads(self.nix("source-prefetch", "store", *args).stdout)
        require(valid_hash(source["hash"]), "invalid source hash")
        source_path = Path(source["storePath"])
        require(source_path.is_dir() and not (source_path / ".git").exists(), "source must be a Git-free archive")
        if frozen:
            require(source["hash"] == frozen["sourceHash"], "selected source hash changed")
        self.args = [
            "--file", str(HERE / "default.nix"), "--impure", "--argstr", "system", self.system,
            "--argstr", "sourcePath", str(source_path), "--argstr", "depsHash",
            frozen["pnpmDepsHash"] if frozen else FAKE_HASH,
        ]
        cache = json.loads(self.nix("cache-config", "eval", "--json", *self.args, "cacheConfig").stdout)
        self.nix_options.extend([
            "--option", "extra-substituters", " ".join(cache["extra-substituters"]),
            "--option", "extra-trusted-public-keys", " ".join(cache["extra-trusted-public-keys"]),
        ])
        metadata = json.loads(self.nix("metadata", "eval", "--json", *self.args, "metadata").stdout)
        require(metadata == {
            "packagingCommit": self.identity["packagingCommit"], "sourceCommit": self.identity["sourceCommit"],
            "system": self.system, "version": "2026.9.3", "pnpm": "12.3.4", "node": "24.19.0",
            "pinnedRev": None, "defaultNpmLazy": True,
        }, "unexpected source metadata")
        if phase == "prefetch":
            drv = json.loads(self.nix("dependency-drv", "eval", "--json", *self.args, "dependencyDrv").stdout)
            result = self.build("dependency-prefetch", "dependencies", check=False)
            deps_hash = dependency_mismatch(result.returncode, result.stderr, drv)
            print(json.dumps({
                "result": "DISCOVERED", "packageProof": False, **metadata,
                "sourceHash": source["hash"], "pnpmDepsHash": deps_hash,
            }), flush=True)
            return
        self.build("package-contents", "contents")
        self.build("native-ownership", "ownership")
        if sys.platform == "linux":
            result = self.build("qualification", "linux", check=False)
        else:
            self.build("activation", "activation")
            inputs = self.build("inputs", "inputs").stdout.decode().strip()
            result = self.command("qualification", [sys.executable, HERE / "probe.py", inputs], False,
                                  timeout=600, terminate_grace=PROBE_CLEANUP_BUDGET)
        require(fixture_complete([self.directory / "qualification.stdout",
                                  self.directory / "qualification.stderr"], result.returncode),
                "native package/plugin qualification or cleanup incomplete")
        print(json.dumps({
            "result": "PASS", "scope": "source-package-only", **metadata,
            **frozen, "cleanup": "verified",
        }), flush=True)

    def build(self, stage, attribute, check=True):
        return self.nix(stage, "build", "--no-link", "--print-out-paths", "--print-build-logs",
                        "--log-format", "raw", *self.args, attribute, check=check)


def main():
    phase = sys.argv[1] if len(sys.argv) == 2 else ""
    runner_guard(phase)
    os.umask(0o077)
    directory = Path(os.environ["RUNNER_TEMP"]) / "nix-source-qualification"
    directory.mkdir(mode=0o700, exist_ok=True)
    driver = Driver(directory)
    try:
        head = driver.command(f"{phase}-driver-head", ["git", "rev-parse", "HEAD"]).stdout.decode().strip()
        require(head == os.environ["GITHUB_SHA"], "checkout does not match the dispatch SHA")
        require(not driver.command(f"{phase}-driver-status", ["git", "status", "--porcelain"]).stdout,
                "driver checkout must be clean")
        print(json.dumps({"driverCommit": head, "phase": phase, "system": driver.system}), flush=True)
        driver.install() if phase == "install" else driver.native(phase)
    except Exception as error:
        with (directory / f"{driver.stage}.failure").open("w") as output:
            traceback.print_exc(file=output)
        stderr = directory / f"{driver.stage}.stderr"
        print(json.dumps({
            "result": "BLOCKED", "stage": driver.stage, "exception": type(error).__name__,
            "exit": getattr(error, "returncode", 1),
            "diagnostic": failure_diagnostic(error, stderr.read_bytes() if stderr.exists() else b""),
        }), flush=True)
        return 1
    return 0


if __name__ == "__main__":
    def interrupted(signum, frame):
        raise RuntimeError("hosted driver interrupted")

    signal.signal(signal.SIGTERM, interrupted)
    sys.exit(main())
