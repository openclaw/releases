# OpenClaw Release Evidence: 9b4c1f0fa3f454b543bb78cd303b6996222a0c05

Generated: 2026-04-27T14:31:17.705Z
Release ref: `9b4c1f0fa3f454b543bb78cd303b6996222a0c05`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 1 | 0 | 1 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `9b4c1f0fa3f4` | [25000454420](https://github.com/openclaw/openclaw/actions/runs/25000454420) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `9b4c1f0fa3f4` | [25000500182](https://github.com/openclaw/openclaw/actions/runs/25000500182) | 3 |
| running | blocking | `release-checks` | OpenClaw Release Checks | `main` | `9b4c1f0fa3f4` | [25000502193](https://github.com/openclaw/openclaw/actions/runs/25000502193) | 20 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000454420
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25000454420/job/73208968340
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25000454420/job/73211064639
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/25000500182
  - checks-node-core-fast-support: failure - https://github.com/openclaw/openclaw/actions/runs/25000500182/job/73209032477
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25000500182/job/73210124313

## Notes

Automatically requested by Full Release Validation 25000454420 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

