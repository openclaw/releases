# OpenClaw Release Evidence: bfdee5fa72ccf522fde3dde5e75b90179b95ed80

Generated: 2026-04-27T08:08:47.863Z
Release ref: `bfdee5fa72ccf522fde3dde5e75b90179b95ed80`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 3 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | blocking | `full-release-validation` | Full Release Validation | `main` | `bfdee5fa72cc` | [24982696730](https://github.com/openclaw/openclaw/actions/runs/24982696730) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `0286bb98178b` | [24982730868](https://github.com/openclaw/openclaw/actions/runs/24982730868) | 3 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `0286bb98178b` | [24982731964](https://github.com/openclaw/openclaw/actions/runs/24982731964) | 21 |

## Failures

- `full-release-validation`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24982696730
  - Run normal full CI: failure - https://github.com/openclaw/openclaw/actions/runs/24982696730/job/73148507323
  - Run release/live/Docker/QA validation: cancelled - https://github.com/openclaw/openclaw/actions/runs/24982696730/job/73148507350
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24982696730/job/73151889154
- `normal-ci`: failure - https://github.com/openclaw/openclaw/actions/runs/24982730868
  - check-docs: failure - https://github.com/openclaw/openclaw/actions/runs/24982730868/job/73148552760
  - checks-node-extensions-shard-5: failure - https://github.com/openclaw/openclaw/actions/runs/24982730868/job/73148552824
  - check-additional-boundaries: failure - https://github.com/openclaw/openclaw/actions/runs/24982730868/job/73148552992
  - check-additional: failure - https://github.com/openclaw/openclaw/actions/runs/24982730868/job/73148803587
  - checks-node-extensions: failure - https://github.com/openclaw/openclaw/actions/runs/24982730868/job/73148884711
- `release-checks`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24982731964
  - live_and_e2e_release_checks / validate_live_provider_suites (live-codex-harness-docker, Docker live Codex harness, pnpm test:do...: failure - https://github.com/openclaw/openclaw/actions/runs/24982731964/job/73148747496
  - live_and_e2e_release_checks / validate_live_provider_suites (live-all, pnpm test:live, pnpm test:live, 180, false): cancelled - https://github.com/openclaw/openclaw/actions/runs/24982731964/job/73148747510
  - cross_os_release_checks / Windows / packaged fresh: failure - https://github.com/openclaw/openclaw/actions/runs/24982731964/job/73149042538
  - cross_os_release_checks / Windows / installer fresh: failure - https://github.com/openclaw/openclaw/actions/runs/24982731964/job/73149042540
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/24982731964/job/73151898768

## Notes

Automatically requested by Full Release Validation 24982696730 after child workflows completed.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

