#!/usr/bin/env python3
"""One-off hosted proof: original Darwin content, then isolated installed rollback."""
import fcntl
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import traceback
import zipfile

ARTIFACT = 8298152467
RUN = 29293062505
WORKFLOW_SHA = "6f98273937b614869a77d09c73ea0f8beddc00eb"
SOURCE_SHA = "2b294a0fcf4390d7b0fc2d20c00b06299b8f0112"
OUTER_SIZE = 145200534
OUTER_HASH = "116a938ff23f0a20fc52cd658af6f0441a7c3462cdf7fa177ace3ef68a6d44be"
ZIP_NAME = "OpenClaw-2026.7.1.zip"
ZIP_MEMBER = f"releases/releases/source/dist/{ZIP_NAME}"
ZIP_SIZE = 59038286
ZIP_HASH = "99ade467abeb32db26242b35527867b0d41a2db6852c4b5b94c3be6a1160a0e3"
NAR_HASH = "sha256-9/r9AfggsxtVfaJB0/7g4Q3xz24nundH0w6t4DKivhU="
SOURCE_PATH = "/nix/store/75gc2jianhal0qg1g510fvaqhwsrqxi4-source"
INSTALLER_SHA = "13d8dd58da0234aa297dedd986986ccb8e7f3e24"
INSTALLER_HASH = "836671507d9b4ea84252f968bd0622c5c2fa72f5deea93f5764f1c60821062f6"


def digest(path):
    with path.open("rb") as source:
        return hashlib.file_digest(source, "sha256").hexdigest()


def extract_original(archive_path, directory):
    # The full digest binds the already audited five-member archive. Do not
    # repeat its parser audit or extract the unrelated DMG and symbols.
    assert archive_path.stat().st_size == OUTER_SIZE
    assert digest(archive_path) == OUTER_HASH
    with zipfile.ZipFile(archive_path) as archive:
        assert len(archive.infolist()) == 5
        for name, expected in (
            ("release-tag.txt", "v2026.7.1"),
            ("release-sha.txt", SOURCE_SHA),
        ):
            data = archive.read(f"_temp/openclaw-macos-preflight/{name}")
            assert data == (expected + "\n").encode()
            (directory / name).write_bytes(data)
        entry = archive.getinfo(ZIP_MEMBER)
        assert entry.file_size == ZIP_SIZE
        with archive.open(entry) as source, (directory / ZIP_NAME).open("xb") as output:
            shutil.copyfileobj(source, output, 1024 * 1024)
    assert (directory / ZIP_NAME).stat().st_size == ZIP_SIZE
    assert digest(directory / ZIP_NAME) == ZIP_HASH


def local_fetch_evidence(log, transport):
    lines = [re.sub(r"^[^ >]+> ", "", line).strip() for line in log.splitlines()]
    assert f"trying {transport}" in lines
    filename = transport.rsplit("/", 1)[1]
    assert any(re.fullmatch(r"unpacking source archive /[^\r\n]+/" + re.escape(filename), line)
               for line in lines)
    return [f"trying {transport}", f"unpacking source archive <build-temp>/{filename}"]


def runner_guard(phase):
    assert os.environ["GITHUB_ACTIONS"] == "true"
    assert os.environ["RUNNER_ENVIRONMENT"] == "github-hosted"
    assert os.environ["GITHUB_REPOSITORY"] == "openclaw/releases"
    assert os.environ["GITHUB_EVENT_NAME"] == "workflow_dispatch"
    assert os.environ["GITHUB_REF"] == "refs/heads/test/nix-installed-upgrade-driver-20260909"
    assert os.environ["GITHUB_ACTOR"] == os.environ["GITHUB_TRIGGERING_ACTOR"] == "vincentkoc"
    native = {
        ("linux", "x86_64"): "x86_64-linux",
        ("darwin", "arm64"): "aarch64-darwin",
    }[(sys.platform, platform.machine())]
    assert os.environ["NIX_QUALIFIER_SYSTEM"] == native
    assert phase in ("install", "download", "prove", "qualify")
    assert not os.environ.get("GITHUB_TOKEN")
    if phase == "download":
        assert sys.platform == "darwin" and os.environ.get("GH_TOKEN")
    else:
        assert not os.environ.get("GH_TOKEN")
    if phase == "prove":
        assert sys.platform == "darwin"


def kvm_preflight():
    # Opening the device proves access; the stable KVM_GET_API_VERSION ioctl
    # proves it is usable, rather than trusting the installer's best-effort rule.
    with open("/dev/kvm", "rb+", buffering=0) as device:
        assert fcntl.ioctl(device.fileno(), 0xAE00) == 12
    print("KVM read/write access and API version 12 verified", flush=True)


def fixture_event(event):
    if not isinstance(event, dict):
        return False
    keys = event.keys()
    phase = event.get("phase") in ("old", "current", "rollback")
    if keys == {"phase", "postActivation"}:
        return phase and isinstance(event["postActivation"], dict)
    if keys == {"phase", "profile", "bundle", "hm"}:
        return phase and isinstance(event["profile"], dict)
    if keys == {"loadedService", "definition"}:
        return isinstance(event["loadedService"], dict) and isinstance(event["definition"], (dict, str))
    if keys == {"activationTransition"}:
        transition = event["activationTransition"]
        return isinstance(transition, dict) and transition.keys() == {"before", "after"}
    if keys == {"persistedWitness", "noRun"}:
        job = event["persistedWitness"]
        return (
            event["noRun"] is True and isinstance(job, dict)
            and job.get("name") == "installed-upgrade-witness" and job.get("enabled") is False
            and job.get("payload") == {"kind": "systemEvent", "text": "installed-upgrade-witness"}
        )
    if keys == {"pid", "started", "node", "nodeVersion", "health"}:
        return isinstance(event["health"], dict) and event["health"].get("ok") is True
    if keys == {"cleanup", "service", "observedPids"}:
        state = event["service"]
        return (
            event["cleanup"] == "verified" and isinstance(state, dict) and state.get("pid") == 0
            and (state.get("registered") is False or state.get("active") == "inactive")
            and isinstance(event["observedPids"], list)
            and all(isinstance(pid, int) and pid > 0 for pid in event["observedPids"])
        )
    if keys == {"result", "scope", "witnessId", "generations", "cleanup", "trackB"}:
        return (
            event["result"] == "PASS" and event["scope"] == "installed-upgrade-rollback"
            and event["cleanup"] == "verified" and isinstance(event["generations"], list)
            and len(event["generations"]) == 3
        )
    return False


def scrub_fixture(event):
    replacements = [
        ("/tmp/openclaw-installed-baseline", "<fixture-home>"),
        ("/home/baseline/qualification", "<fixture-home>"),
        (os.environ.get("RUNNER_TEMP", ""), "<runner-temp>"),
        (os.environ.get("GITHUB_WORKSPACE", ""), "<workspace>"),
        (os.environ.get("HOME", ""), "<runner-home>"),
    ]
    if isinstance(event, str):
        for path, replacement in sorted(replacements, key=lambda item: len(item[0]), reverse=True):
            if path and path != "/":
                event = event.replace(path, replacement)
        return event
    if isinstance(event, list):
        return [scrub_fixture(value) for value in event]
    if isinstance(event, dict):
        return {key: scrub_fixture(value) for key, value in event.items()}
    return event


class Probe:
    def __init__(self, directory):
        self.directory = directory
        self.stage = "identity"

    def command(self, stage, args, env=None):
        self.stage = stage
        stdout = self.directory / f"{stage}.stdout"
        with stdout.open("xb") as out, (self.directory / f"{stage}.stderr").open("xb") as err:
            subprocess.run(args, stdout=out, stderr=err, env=env, check=True)
        return stdout

    def install(self):
        # v31.11.1's composite action injects/persists github.token. Invoke its
        # exact unchanged script without that wrapper or any token instead.
        assert shutil.which("nix") is None
        script = self.command("installer-download", [
            "curl", "--fail", "--silent", "--show-error", "--location", "--max-time", "60",
            f"https://raw.githubusercontent.com/cachix/install-nix-action/{INSTALLER_SHA}/install-nix.sh",
        ])
        self.stage = "installer-digest"
        assert digest(script) == INSTALLER_HASH
        env = dict(os.environ, INPUT_ENABLE_KVM="true" if sys.platform == "linux" else "false",
                   INPUT_SET_AS_TRUSTED_USER="true", INPUT_INSTALL_OPTIONS="",
                   INPUT_INSTALL_URL="", INPUT_GITHUB_ACCESS_TOKEN="",
                   INPUT_EXTRA_NIX_CONFIG="always-allow-substitutes = false\n"
                   "post-build-hook =\nbuilders =\naccept-flake-config = false\naccess-tokens =")
        self.command("installer", ["bash", str(script)], env)
        print(f"installer=cachix/install-nix-action@v31.11.1 sha256={INSTALLER_HASH}")

    def download(self):
        def api(label, endpoint):
            return self.command(label, ["gh", "api", "--method", "GET",
                                        f"repos/openclaw/releases/actions/{endpoint}"])

        metadata = json.loads(api("artifact-metadata", f"artifacts/{ARTIFACT}").read_text())
        self.stage = "artifact-identity"
        assert metadata["id"] == ARTIFACT and metadata["name"] == "macos-preflight-v2026.7.1"
        assert metadata["size_in_bytes"] == OUTER_SIZE and metadata["expired"] is False
        assert metadata["digest"] == f"sha256:{OUTER_HASH}"
        assert metadata["workflow_run"] == {
            "id": RUN, "repository_id": 1189978876, "head_repository_id": 1189978876,
            "head_branch": "main", "head_sha": WORKFLOW_SHA,
        }
        run = json.loads(api("producer-attempt", f"runs/{RUN}/attempts/2").read_text())
        self.stage = "producer-identity"
        assert run["id"] == RUN and run["run_attempt"] == 2 and run["workflow_id"] == 250420707
        assert run["head_sha"] == WORKFLOW_SHA and run["head_branch"] == "main"
        assert run["path"] == ".github/workflows/openclaw-macos-publish.yml"
        assert run["event"] == "workflow_dispatch"
        assert run["status"] == "completed" and run["conclusion"] == "success"
        archive = api("artifact-download", f"artifacts/{ARTIFACT}/zip")
        self.stage = "archive-binding"
        extract_original(archive, self.directory)
        print(json.dumps({"artifact": ARTIFACT, "run": RUN, "attempt": 2,
                          "workflowSha": WORKFLOW_SHA, "applicationSourceSha": SOURCE_SHA,
                          "tag": "v2026.7.1", "outerBytes": OUTER_SIZE, "outerSha256": OUTER_HASH,
                          "zipBytes": ZIP_SIZE, "zipSha256": ZIP_HASH}))

    def nix_preflight(self, phase):
        config = json.loads(self.command(f"{phase}-config", ["nix", "config", "show", "--json"]).read_text())
        self.stage = "effective-config"
        assert config["always-allow-substitutes"]["value"] is False
        assert not config["post-build-hook"]["value"] and not config["builders"]["value"]
        assert not config["access-tokens"]["value"]
        version = self.command(f"{phase}-version", ["nix", "--version"]).read_text().strip()
        assert version == "nix (Nix) 2.35.2"
        return version

    def prove(self):
        version = self.nix_preflight("nar")
        args = ["--file", str(Path(__file__).with_suffix(".nix")), "--impure",
                "--argstr", "originalZip", str(self.directory / ZIP_NAME)]
        identity = json.loads(self.command("nix-identity", ["nix", "eval", "--json", *args,
                                                           "identity"]).read_text())
        self.stage = "identity-projection"
        target = identity["recoveredOutPath"]
        assert target == SOURCE_PATH and identity["system"] == "aarch64-darwin"
        assert identity["originalOutPath"] == target
        self.stage = "target-absent"
        assert not os.path.lexists(target)
        print(json.dumps({"nix": version, "targetAbsent": True, "identity": identity}))
        result = self.command("nix-build", [
            "nix", "build", "--no-link", "--print-out-paths", "--print-build-logs",
            "--log-format", "raw", "--option", "always-allow-substitutes", "false",
            "--option", "post-build-hook", "", "--option", "builders", "",
            *args, "recoveredSrc",
        ])
        self.stage = "built-path"
        assert result.read_text().strip() == target
        log = self.command("local-target-log", ["nix", "log", "--option", "substituters", "",
                                               identity["drvPath"]]).read_text()
        self.stage = "local-fetch-unpack"
        proof = local_fetch_evidence(log, identity["transport"])
        measured = self.command("independent-nar", ["nix", "hash", "path", "--type", "sha256",
                                                   "--format", "sri", target]).read_text().strip()
        self.stage = "nar-match"
        assert measured == NAR_HASH
        for line in proof:
            print(line)
        print(json.dumps({"result": "PASS", "outPath": target, "narHash": measured,
                          "allowSubstitutes": False, "alwaysAllowSubstitutes": False,
                          "normalizer": "locked native Darwin fetchzip", "applicationExecuted": False}))

    def qualify(self):
        self.nix_preflight("qualifier")
        if sys.platform == "linux":
            self.stage = "kvm-access"
            kvm_preflight()
        else:
            self.stage = "recovered-source-present"
            assert Path(SOURCE_PATH).is_dir()
        sha = os.environ["NIX_QUALIFIER_SHA"]
        self.stage = "qualifier-sha"
        assert re.fullmatch(r"[0-9a-f]{40}", sha)
        checkout = self.directory / "nix-qualifier"
        checkout.mkdir()
        git = ["git", "-C", str(checkout), "-c", "credential.helper="]
        self.command("qualifier-init", [*git, "init"])
        self.command("qualifier-remote", [*git, "remote", "add", "origin",
                                        "https://github.com/openclaw/nix-openclaw.git"])
        self.command("qualifier-fetch", [*git, "fetch", "--depth=1", "origin", sha])
        self.command("qualifier-checkout", [*git, "checkout", "--detach", "FETCH_HEAD"])
        head = self.command("qualifier-head", [*git, "rev-parse", "HEAD"]).read_text().strip()
        assert head == sha
        assert not self.command("qualifier-clean", [*git, "status", "--porcelain"]).read_text()
        print(json.dumps({"qualifierHead": head, "system": os.environ["NIX_QUALIFIER_SYSTEM"]}), flush=True)
        try:
            result = self.command("installed-upgrade", [
                "bash", str(checkout / "maintainers/scripts/qualify-installed-baseline.sh"),
                os.environ["NIX_QUALIFIER_SYSTEM"],
            ])
        except subprocess.CalledProcessError as error:
            self.forward_fixture(error.returncode)
            raise
        self.stage = "qualifier-result"
        with result.open("rb") as lines:
            passed = any(
                b"PASS installed-upgrade Node22 -> Node24 -> rollback; cleanup verified" in line
                for line in lines
            )
        completed = self.forward_fixture(0 if passed else 1)
        assert passed and completed
        print(json.dumps({"result": "PASS", "scope": "installed-upgrade-rollback",
                          "qualifierHead": sha, "cleanup": "verified",
                          "trackB": "DEFERRED: source patch applicability"}), flush=True)

    def forward_fixture(self, status):
        # Build logs are byte streams, not UTF-8 documents. Decode only candidate
        # receipts; unrelated bytes must not hide cleanup or replace a failure.
        cleanup = False
        completed = None
        for name in ("installed-upgrade.stdout", "installed-upgrade.stderr"):
            path = self.directory / name
            if not path.exists():
                continue
            with path.open("rb") as lines:
                for line in lines:
                    blocked = re.search(
                        rb"\bBLOCKED installed-upgrade phase=(old|current|rollback|inputs|build|installed-upgrade)"
                        rb"(?: status=(\d+))?; no fallback\s*$", line,
                    )
                    if blocked:
                        print(json.dumps({"fixtureBlocked": {
                            "phase": blocked[1].decode("ascii"), "status": int(blocked[2]) if blocked[2] else status,
                        }}), flush=True)
                        continue
                    try:
                        receipt = json.loads(line[line.index(b"{"):])
                    except ValueError:
                        continue
                    if not fixture_event(receipt):
                        continue
                    if "result" in receipt:
                        completed = receipt
                        continue
                    if receipt.keys() == {"cleanup", "service", "observedPids"}:
                        cleanup = True
                    print(json.dumps(scrub_fixture(receipt)), flush=True)
        if status == 0 and cleanup and completed:
            print(json.dumps(scrub_fixture(completed)), flush=True)
            return True
        return False


def main():
    os.umask(0o077)
    directory = Path(os.environ["RUNNER_TEMP"]) / "original-nar-proof"
    directory.mkdir(mode=0o700, exist_ok=True)
    probe = Probe(directory)
    try:
        phase = sys.argv[1]
        runner_guard(phase)
        head = probe.command(f"{phase}-recipe-head", ["git", "rev-parse", "HEAD"]).read_text().strip()
        assert re.fullmatch(r"[0-9a-f]{40}", head) and head == os.environ["GITHUB_SHA"]
        print(f"recipeHead={head}", flush=True)
        getattr(probe, phase)()
    except Exception as error:
        with (directory / f"{probe.stage}.failure").open("w") as output:
            traceback.print_exc(file=output)
        code = error.returncode if isinstance(error, subprocess.CalledProcessError) else 1
        print(f"Installed proof blocked: stage={probe.stage} exit={code} "
              f"exception={type(error).__name__}", flush=True)
        return code
    return 0


if __name__ == "__main__":
    sys.exit(main())
