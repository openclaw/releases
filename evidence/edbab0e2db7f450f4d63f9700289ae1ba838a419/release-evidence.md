# OpenClaw Release Evidence: edbab0e2db7f450f4d63f9700289ae1ba838a419

Generated: 2026-04-27T10:20:59.257Z
Release ref: `edbab0e2db7f450f4d63f9700289ae1ba838a419`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 2 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `edbab0e2db7f` | [24986063557](https://github.com/openclaw/openclaw/actions/runs/24986063557) | 0 |
| pass | blocking | `normal-ci` | CI | `main` | `edbab0e2db7f` | [24986103118](https://github.com/openclaw/openclaw/actions/runs/24986103118) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `edbab0e2db7f` | [24986103510](https://github.com/openclaw/openclaw/actions/runs/24986103510) | 21 |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/24986063557
  - Run release/live/Docker/QA validation: failure - https://github.com/openclaw/openclaw/actions/runs/24986063557/job/73159648224
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24986063557/job/73171154513
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/24986103510
  - live_and_e2e_release_checks / validate_live_provider_suites (live-all, pnpm test:live, pnpm test:live, 180, false): failure - https://github.com/openclaw/openclaw/actions/runs/24986103510/job/73159884951
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/24986103510/job/73171051029

## Notes

Automatically requested by Full Release Validation 24986063557 after child workflows completed.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

