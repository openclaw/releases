# OpenClaw Release Evidence: d76f924be34d8a0f2b28cb55375c262e651b6443

Generated: 2026-04-27T08:34:05.395Z
Release ref: `d76f924be34d8a0f2b28cb55375c262e651b6443`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 3 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `d76f924be34d` | [24983859707](https://github.com/openclaw/openclaw/actions/runs/24983859707) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `d76f924be34d` | [24983895101](https://github.com/openclaw/openclaw/actions/runs/24983895101) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `d76f924be34d` | [24983895258](https://github.com/openclaw/openclaw/actions/runs/24983895258) | 21 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24983859707
  - Run normal full CI: failure - https://github.com/openclaw/openclaw/actions/runs/24983859707/job/73152300503
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/24983859707/job/73152300523
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24983859707/job/73155377759
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/24983895101
  - check-additional-runtime-topology-architecture: failure - https://github.com/openclaw/openclaw/actions/runs/24983895101/job/73152339461
  - check-docs: failure - https://github.com/openclaw/openclaw/actions/runs/24983895101/job/73152339508
  - checks-node-agentic-plugins: failure - https://github.com/openclaw/openclaw/actions/runs/24983895101/job/73152339678
  - checks-node-agentic-agents: failure - https://github.com/openclaw/openclaw/actions/runs/24983895101/job/73152339721
  - check-additional: failure - https://github.com/openclaw/openclaw/actions/runs/24983895101/job/73152676007
  - checks-node-core: failure - https://github.com/openclaw/openclaw/actions/runs/24983895101/job/73152794219
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24983895258
  - live_and_e2e_release_checks / validate_live_provider_suites (live-all, pnpm test:live, pnpm test:live, 180, false): cancelled - https://github.com/openclaw/openclaw/actions/runs/24983895258/job/73152601154
  - cross_os_release_checks / Windows / packaged fresh: failure - https://github.com/openclaw/openclaw/actions/runs/24983895258/job/73152876654
  - cross_os_release_checks / Windows / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/24983895258/job/73152876662
  - live_and_e2e_release_checks / Docker E2E (package/update): cancelled - https://github.com/openclaw/openclaw/actions/runs/24983895258/job/73153032689
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/24983895258/job/73155396874

## Notes

Automatically requested by Full Release Validation 24983859707 after child workflows completed.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

