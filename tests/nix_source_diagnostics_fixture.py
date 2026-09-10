"""Real driver entrypoint and child cancellation; external setup is stubbed."""

import json
from contextlib import nullcontext
import errno
import os
from pathlib import Path
import platform
import runpy
import signal
import subprocess
import sys
import time
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts/nix-source-qualification"
sys.path.insert(0, str(SCRIPTS))
import driver
import service

mode, directory = sys.argv[1], Path(sys.argv[2])
entry_mode = mode.endswith("-entry")

if mode in ("grandchild", "cooperative-grandchild"):
    signal.signal(signal.SIGTERM, (lambda signum, frame: sys.exit(0))
                  if mode == "cooperative-grandchild" else signal.SIG_IGN)
    (directory / "grandchild.pid").write_text(str(os.getpid()))
    (directory / "grandchild.pgid").write_text(str(os.getpgrp()))
    (directory / "ready").touch()
    while True:
        signal.pause()
elif mode in ("child", "child-tree", "cooperative-tree"):
    def stop(signum, frame):
        (directory / "teardown").write_text(str(time.monotonic()))
        time.sleep(0.5 if mode == "child" else 0.1 if mode == "cooperative-tree" else 0.01)
        sys.stderr.buffer.write(b"error: teardown complete\xfe\n")
        sys.stderr.buffer.flush()
        sys.exit(0)

    signal.signal(signal.SIGTERM, stop)
    sys.stdout.buffer.write(b"private stdout\xff\n")
    sys.stdout.buffer.flush()
    sys.stderr.buffer.write(b"error: private stderr\xfe\n")
    sys.stderr.buffer.flush()
    (directory / "child.pid").write_text(str(os.getpid()))
    if mode != "child":
        subprocess.Popen([sys.executable, __file__,
                          "cooperative-grandchild" if mode == "cooperative-tree" else "grandchild", directory])
    else:
        (directory / "ready").touch()
    while True:
        signal.pause()
else:
    event = directory / "event.json"
    event.write_text(json.dumps({"inputs": {"nix_source_phase": "prefetch"}}))
    env = {
        **os.environ, "GITHUB_ACTIONS": "true", "RUNNER_ENVIRONMENT": "github-hosted",
        "GITHUB_REPOSITORY": "openclaw/releases", "GITHUB_EVENT_NAME": "workflow_dispatch",
        "GITHUB_REF": driver.BRANCH, "GITHUB_ACTOR": "vincentkoc",
        "GITHUB_TRIGGERING_ACTOR": "vincentkoc", "GITHUB_SHA": "a" * 40,
        "NIX_QUALIFIER_SYSTEM": driver.SYSTEMS[(sys.platform, platform.machine())],
        "RUNNER_TEMP": str(directory), "GITHUB_EVENT_PATH": str(event),
    }
    env.pop("GH_TOKEN", None)
    env.pop("GITHUB_TOKEN", None)
    actual_run = service.run

    def external_command(args, env, check=True, timeout=120,
                         terminate_grace=service.COMMAND_TERM_GRACE, **kwargs):
        if args[0] == "git":
            text = "a" * 40 if args[1] == "rev-parse" else ""
            args = [sys.executable, "-c", f"print({text!r},end='')"]
        elif args[0] == "curl":
            child_mode = {"descendant": "child-tree", "cooperative": "cooperative-tree",
                          "cooperative-denial": "cooperative-tree"}.get(mode, "child")
            args = [sys.executable, __file__, child_mode, directory]
            timeout = 1 if mode in ("timeout", "descendant", "cooperative", "cooperative-denial", "cleanup-entry") else 20
            if mode in ("descendant", "cooperative", "cooperative-denial"):
                terminate_grace = 0.25
        else:
            raise AssertionError("fixture attempted native setup")
        return actual_run(args, env, check, timeout, terminate_grace, **kwargs)

    killpg = os.killpg
    def denied_group_probe(group, sig):
        if sig == 0:
            raise PermissionError(errno.EPERM, "fixture process-group observation denied")
        return killpg(group, sig)

    # Deterministic XNU-supported error boundary; TERM/KILL and child lifecycles stay real.
    denial = patch.object(service.os, "killpg", denied_group_probe) if mode == "cooperative-denial" else nullcontext()
    actual_signal = signal.signal
    registered, entries = {}, []
    injected = False

    def install_handler(sig, handler):
        global injected
        if sig in (signal.SIGINT, signal.SIGTERM) and callable(handler) and sig not in registered:
            def observed(signum, frame, target=handler):
                entries.append(signal.Signals(signum).name)
                return target(signum, frame)
            registered[sig] = handler = observed
        previous = actual_signal(sig, handler)
        if sig == signal.SIGINT and handler == signal.SIG_IGN and not injected:
            injected = True
            signal.raise_signal(signal.SIGTERM)
        return previous

    prior_mask = signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGUSR1}) if entry_mode else None
    try:
        with denial, patch.dict(os.environ, env, clear=True), patch.object(service, "run", external_command), \
                patch("shutil.which", return_value=None), \
                patch.object(sys, "argv", ["driver.py", "install"]), \
                (patch.object(signal, "signal", install_handler) if entry_mode else nullcontext()):
            runpy.run_path(str(SCRIPTS / "driver.py"), run_name="__main__")
    finally:
        if entry_mode:
            (directory / "signal-state.json").write_text(json.dumps({
                "injected": injected, "entries": entries,
                "maskPreserved": signal.pthread_sigmask(signal.SIG_BLOCK, set()) == prior_mask | {signal.SIGUSR1},
                "handlersRestored": all(signal.getsignal(sig) == handler for sig, handler in registered.items()),
            }))
            signal.pthread_sigmask(signal.SIG_SETMASK, prior_mask)
