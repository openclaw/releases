"""Supervisor ownership and bounded teardown for the disposable HM instance."""

import configparser
from contextlib import contextmanager
import json
import os
from pathlib import Path
import plistlib
import re
import signal
import subprocess
import time

LABEL = "org.openclaw.nix.source-qualification"
UNIT = "openclaw-source-qualification.service"
COMMAND_TERM_GRACE = 5
COMMAND_REAP_TIMEOUT = 5
COMMAND_CLEANUP_BUDGET = COMMAND_TERM_GRACE + COMMAND_REAP_TIMEOUT
STATE_TIMEOUT = 10
STOP_TIMEOUT = 15
VERIFY_TIMEOUT = 15
STATE_BUDGET = 2 * STATE_TIMEOUT + COMMAND_CLEANUP_BUDGET
# Observe (including ps), stop, then verify; the last state call can cross the
# verification deadline. Allow one interrupted command to unwind before exit.
SERVICE_CLEANUP_BUDGET = 2 * STATE_BUDGET + STOP_TIMEOUT + COMMAND_CLEANUP_BUDGET + VERIFY_TIMEOUT + 1
PROBE_CLEANUP_BUDGET = COMMAND_CLEANUP_BUDGET + SERVICE_CLEANUP_BUDGET


def ignore_cancellation():
    # Block both signals while installing IGN so cancellation cannot interrupt
    # the transition before teardown starts. Preserve the caller's full mask.
    signals = (signal.SIGINT, signal.SIGTERM)
    mask = signal.pthread_sigmask(signal.SIG_BLOCK, signals)
    try:
        return {sig: signal.signal(sig, signal.SIG_IGN) for sig in signals}
    finally:
        signal.pthread_sigmask(signal.SIG_SETMASK, mask)


@contextmanager
def uninterrupted_cleanup():
    # Cancellation has already won. Later signals must not interrupt child reaping.
    handlers = ignore_cancellation()
    try:
        yield
    finally:
        for sig, handler in handlers.items():
            signal.signal(sig, handler)


def run(args, env, check=True, timeout=120, terminate_grace=COMMAND_TERM_GRACE,
        *, stdout=subprocess.PIPE, stderr=subprocess.PIPE):
    process = subprocess.Popen(
        [str(arg) for arg in args], env=env, start_new_session=True,
        stdout=stdout, stderr=stderr,
    )
    try:
        try:
            stdout, stderr = process.communicate(timeout=timeout)
        except BaseException as original:
            # Reap only this command's new process group, including on interruption.
            with uninterrupted_cleanup():
                try:
                    for sig, grace in ((signal.SIGTERM, terminate_grace), (signal.SIGKILL, COMMAND_REAP_TIMEOUT)):
                        deadline = time.monotonic() + grace
                        try:
                            os.killpg(process.pid, sig)
                        except ProcessLookupError:
                            pass
                        try:
                            process.communicate(timeout=max(0, deadline - time.monotonic()))
                            if sig == signal.SIGKILL:
                                break
                            # File-backed output does not keep communicate waiting for descendants.
                            # Keep the remaining grace for this command's group, even after leader exit.
                            while True:
                                os.killpg(process.pid, 0)
                                remaining = deadline - time.monotonic()
                                if remaining <= 0:
                                    break
                                time.sleep(min(0.05, remaining))
                        except ProcessLookupError:
                            break
                        except subprocess.TimeoutExpired:
                            pass
                except PermissionError as cleanup_error:
                    # Denial is not proof the group is gone; retain both failures.
                    raise original from cleanup_error
            raise
    finally:
        for stream in (process.stdout, process.stderr):
            if stream is not None:
                stream.close()
    result = subprocess.CompletedProcess(args, process.returncode, stdout, stderr)
    if check:
        result.check_returncode()
    return result


def alive(pid):
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False


class Service:
    def __init__(self, home, darwin, env):
        self.home, self.darwin, self.env = home, darwin, env
        self.target = f"gui/{os.getuid()}/{LABEL}"
        self.observed = set()

    def state(self):
        if self.darwin:
            result = run(["launchctl", "print", self.target], self.env, False, STATE_TIMEOUT)
            if result.returncode:
                if b"Could not find service" not in result.stderr:
                    raise RuntimeError("cannot determine fixture launchd registration")
                return {"registered": False, "pid": 0}
            text = result.stdout.decode()
            fields = dict(re.findall(r"^\s*([\w ]+) = ([^\n{]+)$", text, re.M))
            arguments = re.search(r"^\s*arguments = \{\n(.*?)^\s*\}", text, re.M | re.S)
            state = {
                "registered": True, "pid": int(fields.get("pid", "0")),
                "runs": int(fields.get("runs", "0")), "path": fields.get("path"),
                "arguments": [line.strip() for line in arguments[1].splitlines()] if arguments else [],
                "lastExit": fields.get("last exit code", "unknown"),
                "lastSignal": fields.get("last terminating signal", ""),
            }
        else:
            result = run([
                "systemctl", "--user", "show", UNIT, "-p", "MainPID", "-p", "NRestarts",
                "-p", "ActiveState", "-p", "Result", "-p", "LoadState",
                "-p", "FragmentPath", "-p", "ExecStart",
            ], self.env, False, STATE_TIMEOUT)
            fields = dict(line.split("=", 1) for line in result.stdout.decode().splitlines() if "=" in line)
            if fields.get("LoadState") == "not-found":
                return {"registered": False, "pid": 0, "active": "inactive"}
            result.check_returncode()
            state = {
                "registered": True, "pid": int(fields["MainPID"]),
                "runs": int(fields["NRestarts"]), "active": fields["ActiveState"],
                "result": fields["Result"], "path": fields["FragmentPath"],
                "execStart": fields["ExecStart"],
            }
        if state["pid"]:
            self.observed.add(state["pid"])
            identity = run(["ps", "-p", state["pid"], "-o", "uid=,lstart="],
                           self.env, timeout=STATE_TIMEOUT).stdout.decode().strip().split(maxsplit=1)
            if len(identity) != 2 or int(identity[0]) != os.getuid():
                raise RuntimeError("service PID has no matching owner/start identity")
            state["started"] = identity[1]
        return state

    def preflight(self):
        if self.darwin:
            run(["launchctl", "print", f"gui/{os.getuid()}"], self.env, timeout=10)
        if self.state()["registered"]:
            raise RuntimeError("fixture service already registered; refusing activation")

    def verify_loaded(self, generation, state):
        if self.darwin:
            relative = Path("Library/LaunchAgents") / f"{LABEL}.plist"
            expected = generation / "LaunchAgents" / f"{LABEL}.plist"
            installed = self.home / relative
            if installed.read_bytes() != expected.read_bytes():
                raise RuntimeError("installed plist differs from the selected generation")
            if not state["path"] or Path(state["path"]).resolve(strict=True) != installed.resolve(strict=True):
                raise RuntimeError("launchd loaded a different plist")
            if state["arguments"] != plistlib.loads(expected.read_bytes())["ProgramArguments"]:
                raise RuntimeError("loaded launchd arguments differ from the generation")
            # HM relinking may kickstart once; freeze the counter after activation.
            if state["runs"] not in (1, 2) or state["lastExit"] not in ("(never exited)", "0"):
                raise RuntimeError("unexpected launchd exits/restarts during activation")
            if state["lastSignal"] and not state["lastSignal"].endswith(": 9"):
                raise RuntimeError("unexpected launchd termination during activation")
        else:
            relative = Path(".config/systemd/user") / UNIT
            expected = (generation / "home-files" / relative).resolve(strict=True)
            if (not state["path"] or (self.home / relative).resolve(strict=True) != expected
                    or Path(state["path"]).resolve(strict=True) != expected):
                raise RuntimeError("systemd loaded a different unit")
            unit = configparser.ConfigParser(interpolation=None, strict=False)
            unit.read_string(expected.read_text())
            if f"argv[]={unit['Service']['ExecStart']} ;" not in state["execStart"]:
                raise RuntimeError("loaded systemd command differs from the generation")
            if state["runs"] != 0 or state["result"] != "success" or state["active"] != "active":
                raise RuntimeError("systemd service failed or restarted unexpectedly")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        # Observe failed-start PIDs too. A successful stop command alone is not cleanup.
        observation_error = None
        try:
            self.state()
        except Exception as error:
            observation_error = error
        command = ["launchctl", "bootout", self.target] if self.darwin else [
            "systemctl", "--user", "stop", UNIT,
        ]
        try:
            run(command, self.env, False, STOP_TIMEOUT)
        except subprocess.TimeoutExpired as error:
            observation_error = error
        deadline = time.monotonic() + VERIFY_TIMEOUT
        while True:
            state = self.state()
            inactive = not state["registered"] if self.darwin else (
                state.get("active") == "inactive" and not state["pid"]
            )
            if inactive and not any(alive(pid) for pid in self.observed):
                if observation_error:
                    raise RuntimeError("cleanup had an observation/stop failure") from observation_error
                print(json.dumps({"qualification": "cleanup", "verified": True}), flush=True)
                return False
            if time.monotonic() >= deadline:
                raise RuntimeError("fixture supervisor or observed PID survived cleanup")
            time.sleep(0.2)
