#!/usr/bin/env python3
"""One-off runner-only content proof. Never execute the recovered application."""
import hashlib
import json
import os
from pathlib import Path
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
        script = self.command("installer-download", [
            "curl", "--fail", "--silent", "--show-error", "--location", "--max-time", "60",
            f"https://raw.githubusercontent.com/cachix/install-nix-action/{INSTALLER_SHA}/install-nix.sh",
        ])
        self.stage = "installer-digest"
        assert digest(script) == INSTALLER_HASH
        env = dict(os.environ, INPUT_ENABLE_KVM="false", INPUT_SET_AS_TRUSTED_USER="true",
                   INPUT_INSTALL_OPTIONS="", INPUT_GITHUB_ACCESS_TOKEN="",
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

    def prove(self):
        config = json.loads(self.command("nix-config", ["nix", "config", "show", "--json"]).read_text())
        self.stage = "effective-config"
        assert config["always-allow-substitutes"]["value"] is False
        assert not config["post-build-hook"]["value"] and not config["builders"]["value"]
        assert not config["access-tokens"]["value"]
        version = self.command("nix-version", ["nix", "--version"]).read_text().strip()
        assert version == "nix (Nix) 2.35.2"
        args = ["--file", str(Path(__file__).with_suffix(".nix")), "--impure",
                "--argstr", "originalZip", str(self.directory / ZIP_NAME)]
        identity = json.loads(self.command("nix-identity", ["nix", "eval", "--json", *args,
                                                           "identity"]).read_text())
        self.stage = "identity-projection"
        target = identity["recoveredOutPath"]
        assert re.fullmatch(r"/nix/store/[0-9a-z]{32}-[A-Za-z0-9+._?=-]+", target)
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
                          "normalizer": "locked native Linux fetchzip", "applicationExecuted": False}))


def main():
    os.umask(0o077)
    directory = Path(os.environ["RUNNER_TEMP"]) / "original-nar-proof"
    directory.mkdir(mode=0o700, exist_ok=True)
    probe = Probe(directory)
    try:
        assert os.environ["GITHUB_ACTIONS"] == "true" and sys.platform == "linux"
        assert os.environ["GITHUB_REPOSITORY"] == "openclaw/releases"
        assert os.environ["GITHUB_EVENT_NAME"] == "workflow_dispatch"
        assert os.environ["GITHUB_REF"] == "refs/heads/test/nix-original-artifact-nar-20260909"
        phase = sys.argv[1]
        assert phase in ("install", "download", "prove")
        if phase != "download":
            assert not os.environ.get("GH_TOKEN") and not os.environ.get("GITHUB_TOKEN")
        head = probe.command(f"{phase}-head", ["git", "rev-parse", "HEAD"]).read_text().strip()
        assert re.fullmatch(r"[0-9a-f]{40}", head) and head == os.environ["GITHUB_SHA"]
        print(f"recipeHead={head}", flush=True)
        getattr(probe, phase)()
    except Exception as error:
        with (directory / f"{probe.stage}.failure").open("w") as output:
            traceback.print_exc(file=output)
        code = error.returncode if isinstance(error, subprocess.CalledProcessError) else 1
        print(f"NAR proof blocked: stage={probe.stage} exit={code}", flush=True)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
