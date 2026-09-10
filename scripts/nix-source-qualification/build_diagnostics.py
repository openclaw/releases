"""Bounded projection of Nix 2.35.2 activity records, never build authority."""

import json
import os
import re
import stat
import time

SCAN_LIMIT = 16 * 1024 * 1024
RECORD_LIMIT = 64 * 1024
ACTIVITY_LIMIT = 256
ROW_LIMIT = 8
OUTPUT_LIMIT = 4 * 1024
TIME_LIMIT = 2
PHASES = frozenset((
    "unpackPhase", "patchPhase", "configurePhase", "buildPhase", "checkPhase",
    "installPhase", "fixupPhase", "installCheckPhase", "distPhase",
))


def scrub_diagnostic(line):
    if re.search(r"(?i)(?:token|password|secret|authorization|bearer|private.key|gh[pousr]_|sk-)", line):
        line = "<credential-bearing diagnostic redacted>"
    line = re.sub(r"https?://\S+", "<url>", line)
    line = re.sub(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b", "<email>", line)
    line = re.sub(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", "<address>", line)
    line = re.sub(r"\b(?:[0-9a-fA-F]{1,4}:){2,}[0-9a-fA-F:]+\b", "<address>", line)
    line = re.sub(r"(?<![\w])/(?:[^\s'\"<>()[\]{}:,]+/?)+", "<path>", line)
    line = re.sub(r"\b[\w-]+\.(?:local|internal|lan)\b", "<host>", line)
    return line[:240]


def public_derivation_name(value):
    # Only the authoritative actBuild field from these frozen public inputs is eligible.
    match = re.fullmatch(r"/nix/store/([0-9abcdfghijklmnpqrsvwxyz]{32}-[A-Za-z0-9][A-Za-z0-9+._?=-]{0,159}\.drv)", value)
    name = match[1] if match else "unknown"
    return name if scrub_diagnostic(name) == name else "unknown"


def uint(value):
    return type(value) is int and 0 <= value < 2**64


def unique_fields(pairs):
    value = dict(pairs)
    if len(value) != len(pairs):
        raise ValueError("duplicate JSON fields")
    return value


def activity_diagnostic(path, selected_drv):
    # Nix logging.hh: actBuild=105, resSetPhase=104, resProgress=105.
    # Only actBuild's own first field identifies a derivation; parents are not a dependency graph.
    end = time.monotonic() + TIME_LIMIT
    activities, gaps = {}, set()
    private_capture = False
    scanned = 0
    try:
        with path.open("rb") as source:
            mode = os.fstat(source.fileno()).st_mode
            private_capture = (stat.S_ISREG(mode) and stat.S_IMODE(mode) == 0o600
                               and stat.S_IMODE(path.parent.stat().st_mode) == 0o700)
            size = source.seek(0, 2)
            source.seek(0)
            while scanned < size:
                if time.monotonic() >= end:
                    gaps.add("time-limit")
                    break
                if scanned >= SCAN_LIMIT:
                    gaps.add("scan-limit")
                    break
                record = source.readline(min(RECORD_LIMIT, SCAN_LIMIT - scanned))
                scanned += len(record)
                if not record.endswith(b"\n"):
                    gaps.add("incomplete-record")
                    break
                event = json.loads(record, object_pairs_hook=unique_fields)
                if not isinstance(event, dict):
                    raise ValueError("invalid record")
                action = event.get("action")
                if action == "msg":
                    continue
                ident = event.get("id")
                if not uint(ident) or ident == 0:
                    raise ValueError("invalid activity")
                if action == "start":
                    kind, parent, fields = event.get("type"), event.get("parent"), event.get("fields", [])
                    if not uint(kind) or not uint(parent) or not isinstance(fields, list) or ident in activities:
                        raise ValueError("invalid start")
                    classification, name = "unknown", "unknown"
                    if kind == 105:
                        if (len(fields) != 4 or not isinstance(fields[0], str)
                                or not fields[0].startswith("/nix/store/") or not fields[0].endswith(".drv")
                                or not isinstance(fields[1], str) or not all(uint(item) for item in fields[2:])):
                            raise ValueError("invalid build fields")
                        classification = "selected" if fields[0] == selected_drv else "other"
                        name = public_derivation_name(fields[0])
                    if len(activities) == ACTIVITY_LIMIT:
                        activities.pop(next(iter(activities)))
                        gaps.add("activity-eviction")
                    activities[ident] = {
                        "id": ident, "parent": parent, "type": kind, "derivation": classification, "derivationName": name,
                        "stop": "unknown", "lastPhase": "unknown", "progress": "unknown",
                    }
                elif action in ("result", "stop"):
                    row = activities.pop(ident, None)
                    if row is None:
                        gaps.add("missing-start")
                        continue
                    activities[ident] = row
                    if action == "stop":
                        row["stop"] = "observed"
                        continue
                    kind, fields = event.get("type"), event.get("fields", [])
                    if not uint(kind) or not isinstance(fields, list):
                        raise ValueError("invalid result")
                    if kind == 104 and row["type"] == 105:
                        if len(fields) != 1 or not isinstance(fields[0], str):
                            raise ValueError("invalid phase")
                        row["lastPhase"] = fields[0] if fields[0] in PHASES else "unknown"
                    elif kind == 105:
                        if len(fields) != 4 or not all(uint(item) for item in fields):
                            raise ValueError("invalid progress")
                        row["progress"] = dict(zip(("done", "expected", "running", "failed"), fields))
                else:
                    raise ValueError("invalid action")
            if source.seek(0, 2) != size:
                gaps.add("changing-capture")
    except (OSError, ValueError, RecursionError):
        gaps.add("unreadable-or-malformed")
    for row in activities.values():
        parent, seen = row["parent"], {row["id"]}
        while parent:
            if parent not in activities or parent in seen:
                gaps.add("missing-or-invalid-parent")
                break
            seen.add(parent)
            parent = activities[parent]["parent"]
    if not activities:
        gaps.add("no-observed-activities")
    if len(activities) > ROW_LIMIT:
        gaps.add("row-limit")
    if time.monotonic() >= end:
        gaps.add("time-limit")
    rows = sorted(activities.values(), key=lambda row: row["derivation"] == "selected")[-ROW_LIMIT:]
    result = {"coverage": "unknown" if gaps else "observed-records",
              "privateCapture": private_capture, "gaps": sorted(gaps), "activities": rows}
    while len(json.dumps(result).encode()) > OUTPUT_LIMIT - 128:
        rows.pop(0)
        result["coverage"] = "unknown"
        result["gaps"] = sorted(gaps | {"output-limit"})
    return result
