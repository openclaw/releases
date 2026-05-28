# OpenClaw Release Evidence: 32bbb5b18fb1ee6fc003d9b204b2854c598732fb

Generated: 2026-04-27T15:37:19.333Z
Release ref: `32bbb5b18fb1ee6fc003d9b204b2854c598732fb`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `56fa69a48a03` | [25004127627](https://github.com/openclaw/openclaw/actions/runs/25004127627) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `56fa69a48a03` | [25004179234](https://github.com/openclaw/openclaw/actions/runs/25004179234) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `56fa69a48a03` | [25004181437](https://github.com/openclaw/openclaw/actions/runs/25004181437) | 0 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25004127627
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25004127627/job/73222218277
  - Run normal full CI: cancelled - https://github.com/openclaw/openclaw/actions/runs/25004127627/job/73222218306
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25004127627/job/73223473879
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25004179234
  - checks-windows-node-test: cancelled - https://github.com/openclaw/openclaw/actions/runs/25004179234/job/73222283620
  - check-lint: cancelled - https://github.com/openclaw/openclaw/actions/runs/25004179234/job/73222283845
  - checks-node-core-support-boundary: failure - https://github.com/openclaw/openclaw/actions/runs/25004179234/job/73222638524
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/25004179234/job/73222712822
  - check: cancelled - https://github.com/openclaw/openclaw/actions/runs/25004179234/job/73223362801
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25004181437
  - resolve_target: cancelled - https://github.com/openclaw/openclaw/actions/runs/25004181437/job/73222256363
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25004181437/job/73223366814
  - Run QA Lab parity gate: cancelled - https://github.com/openclaw/openclaw/actions/runs/25004181437/job/73223366823
  - Run QA Lab live Telegram lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25004181437/job/73223366975
  - Run QA Lab live Matrix lane: cancelled - https://github.com/openclaw/openclaw/actions/runs/25004181437/job/73223367088

## Notes

Automatically requested by Full Release Validation 25004127627 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

