# OpenClaw Release Evidence: 1cf68b9243aa2e8683cd2c920623e2b624250dfb

Generated: 2026-04-27T16:03:43.063Z
Release ref: `1cf68b9243aa2e8683cd2c920623e2b624250dfb`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 1 | 1 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `1cf68b9243aa` | [25004520392](https://github.com/openclaw/openclaw/actions/runs/25004520392) | 0 |
| pass | blocking | `normal-ci` | CI | `main` | `1cf68b9243aa` | [25004568615](https://github.com/openclaw/openclaw/actions/runs/25004568615) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `1cf68b9243aa` | [25004569652](https://github.com/openclaw/openclaw/actions/runs/25004569652) | 22 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25004520392
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/25004520392/job/73223629510
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/25004520392/job/73228262306
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/25004569652
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-gateway, Native live gateway, node scripts/test-li...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25004569652/job/73224481810
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-extensions-l-z, Native live plugins L-Z, node scripts/...: cancelled - https://github.com/openclaw/openclaw/actions/runs/25004569652/job/73224481820
  - cross_os_release_checks / Linux / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/25004569652/job/73224832129
  - live_and_e2e_release_checks / Docker E2E (package/update): cancelled - https://github.com/openclaw/openclaw/actions/runs/25004569652/job/73225360844
  - live_and_e2e_release_checks / Docker E2E (bundled channels): failure - https://github.com/openclaw/openclaw/actions/runs/25004569652/job/73225360976
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/25004569652/job/73228189518

## Notes

Automatically requested by Full Release Validation 25004520392 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

