# OpenClaw Release Evidence: 4ebec8b5dc8318260efab5fc41cd3ab83cdd3db0

Generated: 2026-04-27T14:11:49.283Z
Release ref: `4ebec8b5dc8318260efab5fc41cd3ab83cdd3db0`

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 0 | 2 | 0 | 0 |
| Advisory | 0 | 1 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| fail | advisory | `full-release-validation` | Full Release Validation | `main` | `4c544e649c74` | [24998349719](https://github.com/openclaw/openclaw/actions/runs/24998349719) | 0 |
| fail | blocking | `normal-ci` | CI | `main` | `4c544e649c74` | [24998395588](https://github.com/openclaw/openclaw/actions/runs/24998395588) | 0 |
| fail | blocking | `release-checks` | OpenClaw Release Checks | `main` | `4c544e649c74` | [24998397587](https://github.com/openclaw/openclaw/actions/runs/24998397587) | 22 |

## Failures

- `full-release-validation`: failure - https://github.com/openclaw/openclaw/actions/runs/24998349719
  - Verify full validation: failure - https://github.com/openclaw/openclaw/actions/runs/24998349719/job/73207431169
- `normal-ci`: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588
  - build-artifacts: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201463668
  - checks-windows-node-test: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201463700
  - checks-node-extensions-shard-5: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201463728
  - macos-swift: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201463772
  - checks-node-extensions-shard-4: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201463792
  - checks-node-extensions-shard-3: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201463796
  - android-test-third-party: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201463799
  - checks-node-extensions-shard-1: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201463837
  - checks-node-extensions-shard-2: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201463857
  - android-test-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201463906
  - android-build-play: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201463914
  - check-lint: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201463979
  - checks-node-core-runtime-media-ui: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201464040
  - checks-node-agentic-agents: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201464060
  - checks-node-agentic-plugin-sdk: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201464109
  - checks-node-core-runtime-infra: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201464121
  - checks-node-core-fast-support: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201464188
  - check-additional: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201783665
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201783790
  - checks-node-extensions: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201783835
  - build-smoke: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201783903
  - matrix.check_name: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201784028
  - check: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201784132
  - checks-node-core: cancelled - https://github.com/openclaw/openclaw/actions/runs/24998395588/job/73201948372
- `release-checks`: failure - https://github.com/openclaw/openclaw/actions/runs/24998397587
  - live_and_e2e_release_checks / validate_special_e2e (openai-ws-stream-live-e2e, OpenAI WebSocket live E2E, pnpm test:e2e src/age...: failure - https://github.com/openclaw/openclaw/actions/runs/24998397587/job/73203587994
  - live_and_e2e_release_checks / validate_repo_e2e: failure - https://github.com/openclaw/openclaw/actions/runs/24998397587/job/73203588036
  - live_and_e2e_release_checks / validate_live_provider_suites (native-live-src-agents, Native live agents, node scripts/test-live...: failure - https://github.com/openclaw/openclaw/actions/runs/24998397587/job/73203588279
  - Verify release checks: failure - https://github.com/openclaw/openclaw/actions/runs/24998397587/job/73207342348

## Notes

Automatically requested by Full Release Validation 24998349719 after child workflows completed; the parent summary re-checks current child run conclusions.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

