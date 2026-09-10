"""Exercise the actual source package installed by one isolated HM generation."""

import json
from html.parser import HTMLParser
import os
from pathlib import Path
import platform
import pwd
import re
import signal
import sys
import time
import urllib.request
from urllib.parse import quote, urlsplit

from service import Service, UNIT, run

PORT = "18997"
EXPECTED = {"ok": True, "version": "0.0.1"}


def prepare_home(home, username, global_state=Path("/nix/var/nix")):
    # Locked HM migrates global profiles even with an isolated HOME.
    profiles = global_state / "profiles/per-user" / username
    roots = global_state / "gcroots/per-user" / username
    if list(profiles.glob("home-manager*")) or os.path.lexists(roots / "current-home"):
        raise RuntimeError("existing global Home Manager ownership; refusing activation")
    home.mkdir(mode=0o700)
    profiles = home / ".local/state/nix/profiles"
    profiles.mkdir(parents=True)
    (home / ".nix-profile").symlink_to(profiles / "profile")
    return profiles / "home-manager"


def isolated_env(home, username):
    env = {
        key: value for key, value in os.environ.items()
        if not key.startswith(("OPENCLAW_", "HOME_MANAGER_", "NIX_STATE", "GIT_", "GITHUB_"))
        and key not in {"DRY_RUN", "SKIP_SANITY_CHECKS", "NIX_PROFILES", "GH_TOKEN", "NODE_OPTIONS", "NODE_PATH"}
    }
    env.update(HOME=str(home), USER=username, LOGNAME=username, LC_ALL="C", NO_COLOR="1",
               OPENCLAW_STATE_DIR=str(home / ".openclaw-qualification"),
               OPENCLAW_CONFIG_PATH=str(home / ".openclaw-qualification/openclaw.json"),
               OPENCLAW_NIX_MODE="1", OPENCLAW_DISABLE_PERSISTED_PLUGIN_REGISTRY="1")
    for name, suffix in {
        "XDG_STATE_HOME": ".local/state", "XDG_DATA_HOME": ".local/share",
        "XDG_CONFIG_HOME": ".config", "XDG_CACHE_HOME": ".cache",
    }.items():
        env[name] = str(home / suffix)
    return env


def verify_generation(profile, stage, env):
    listing = run([stage["homeManager"], "generations"], env).stdout.decode().splitlines()
    if len(listing) != 1:
        raise RuntimeError("qualification requires exactly one fresh HM generation")
    match = re.search(r": id (\d+) -> (\S+)(?: \(current\))?$", listing[0])
    if (not match or os.readlink(profile) != f"home-manager-{match[1]}-link"
            or match[2] != stage["activation"] or str(profile.resolve(strict=True)) != stage["activation"]):
        raise RuntimeError("HM listing, installed profile and selected generation disagree")


def verify_version(output, source_commit):
    match = re.fullmatch(r"OpenClaw 2026\.9\.3(?: \(([0-9a-f]{7,40})\))?", output.decode().strip())
    if not match or (match[1] is not None and not source_commit.startswith(match[1])):
        raise RuntimeError("CLI version/source identity differs from selected source")


def observe(stage, executable, service):
    deadline = time.monotonic() + 90
    while time.monotonic() < deadline:
        state = service.state()
        if state["pid"]:
            result = run([executable, "gateway", "health", "--port", PORT, "--json", "--timeout", "3000"],
                         service.env, False, 15)
            if result.returncode == 0 and json.loads(result.stdout).get("ok") is True:
                break
        time.sleep(1)
    else:
        raise RuntimeError("gateway did not become healthy")
    if service.state() != state:
        raise RuntimeError("service identity changed during health probe")
    service.verify_loaded(Path(stage["activation"]), state)
    if service.darwin:
        mappings = run(["lsof", "-a", "-p", state["pid"], "-d", "txt", "-Fn"], service.env).stdout.decode()
        nodes = [line[1:] for line in mappings.splitlines()
                 if line.startswith("n/nix/store/") and line.endswith("/bin/node")]
        if nodes != [stage["node"]]:
            raise RuntimeError("gateway is not executing the locked Node runtime")
    elif str(Path(f"/proc/{state['pid']}/exe").resolve(strict=True)) != stage["node"]:
        raise RuntimeError("gateway is not executing the locked Node runtime")
    return state


class EntryAssets(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.assets = set()
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        target = (attrs.get("src") if tag == "script" else
                  attrs.get("href") if tag == "link" and attrs.get("rel") == "stylesheet" else None)
        if target:
            self.assets.add(urlsplit(target).path.removeprefix("./").removeprefix("/"))


def verify_ui(root):
    # Bypass ambient HTTP proxies; compare served bytes with the actual output.
    client = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    client.addheaders = [("Accept-Encoding", "identity")]
    ui = root / "dist/control-ui"
    manifest = json.loads((ui / "asset-manifest.json").read_text())
    assets = [entry["path"] for entry in manifest["assets"]]
    for suffix in (".js", ".css"):
        if not any(name.endswith(suffix) for name in assets):
            raise RuntimeError("Control UI is missing executable/style assets")
    with client.open(f"http://127.0.0.1:{PORT}/", timeout=10) as response:
        if response.status != 200 or response.headers.get_content_type() != "text/html":
            raise RuntimeError("Control UI document did not load")
        served = EntryAssets(response.read().decode()).assets
    expected = EntryAssets((ui / "index.html").read_text()).assets
    if not expected or served != expected:
        raise RuntimeError("served Control UI entry points differ from the package")
    # Index is compared structurally above. Include public/root output omitted
    # by the assets-only manifest; maps and negotiated sidecars are not direct proof.
    installed = {file.relative_to(ui).as_posix() for file in ui.rglob("*") if file.is_file()}
    for name in sorted(installed | expected):
        if name == "index.html" or name.endswith((".map", ".br", ".gz")):
            continue
        with client.open(f"http://127.0.0.1:{PORT}/{quote(name)}", timeout=10) as response:
            if response.status != 200 or response.read() != (ui / name).read_bytes():
                raise RuntimeError("served Control UI differs from the packaged artifact")


def main():
    stage = json.loads(Path(sys.argv[1]).read_text())
    home = Path(stage["homeDirectory"])
    darwin = platform.system() == "Darwin"
    username = pwd.getpwuid(os.getuid()).pw_name
    expected_home = Path("/tmp/openclaw-source-qualification" if darwin else "/home/qualification/fixture")
    if home != expected_home or username != ("runner" if darwin else "qualification"):
        raise RuntimeError("probe requires its disposable runner user and HOME")
    for key in ("activation", "gateway", "node", "pnpm", "plugin", "homeManager", "sourceManifest"):
        value = Path(stage[key]).resolve(strict=True)
        if not str(value).startswith("/nix/store/"):
            raise RuntimeError("fixture artifacts must be realized store paths")
        stage[key] = str(value)
    source_commit = stage["metadata"]["sourceCommit"]
    env = isolated_env(home, username)
    service = Service(home, darwin, env)
    service.preflight()
    profile = prepare_home(home, username)
    with service:
        generation = Path(stage["activation"])
        # Match locked HM's doSwitch profile ownership and driver contract.
        run(["nix-env", "--profile", profile, "--set", generation], env)
        run([generation / "activate", "--driver-version", "1"], env)
        if not darwin and service.state().get("active") == "inactive":
            run(["systemctl", "--user", "start", UNIT], env)
        verify_generation(profile, stage, env)
        executable = home / ".nix-profile/bin/openclaw"
        root = Path(stage["gateway"]) / "lib/openclaw"
        if executable.resolve(strict=True) != (Path(stage["gateway"]) / "bin/openclaw").resolve(strict=True):
            raise RuntimeError("installed command differs from the actual HM source package")
        if run([stage["node"], "--version"], env).stdout.strip() != b"v24.19.0":
            raise RuntimeError("wrong native Node version")
        if run([stage["pnpm"], "--version"], env).stdout.strip() != b"12.3.4":
            raise RuntimeError("wrong native pnpm version")
        run([stage["node"], Path(__file__).with_name("artifacts.mjs"), root,
             source_commit, stage["sourceManifest"]], env)
        verify_version(run([executable, "--version"], env).stdout, source_commit)
        export_import = (
            'import {createRequire} from "node:module"; import {pathToFileURL} from "node:url";'
            'const file=createRequire(process.argv[1]+"/package.json").resolve("openclaw/cli-entry");'
            'process.argv=[process.execPath,file,"--version"]; await import(pathToFileURL(file));'
        )
        verify_version(run([stage["node"], "--input-type=module", "--eval", export_import, root], env).stdout,
                       source_commit)
        state = observe(stage, executable, service)
        verify_ui(root)
        for _ in range(3):
            cli = json.loads(run([executable, "nix-qualification", "ping"], env).stdout)
            rpc = json.loads(run([executable, "gateway", "call", "nix.qualification.ping",
                                  "--port", PORT, "--params", "{}", "--json"], env).stdout)
            if cli != EXPECTED or rpc != EXPECTED:
                raise RuntimeError("packaged plugin CLI/RPC action returned the wrong result")
            if service.state() != state:
                raise RuntimeError("service restarted during package/plugin observation")
            time.sleep(1)
    print(json.dumps({"qualification": "complete", "verified": True}), flush=True)


if __name__ == "__main__":
    def interrupted(signum, frame):
        raise RuntimeError("fixture interrupted")

    signal.signal(signal.SIGTERM, interrupted)
    main()
