# OpenClaw Release Evidence: octopool-0.9.6

Generated: 2026-10-06T17:19:34.856Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.9.6` |
| Release ref input | not recorded |
| Release ref status | not-recorded |
| Release ref kind | unknown |
| Release ref name | unknown |
| Release ref SHA | not resolved |
| Runs at release SHA | none |
| Package spec | not recorded |
| npm status | not-recorded |
| npm note | No package spec was recorded for this evidence run; npm release matching cannot be proven from this report. |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `ci` | CI | `release/octopool-v0.9.6-20261006` | `09fbaa9695fc` | 9m 48s | 15m 10s | 21s | [37476364368](https://github.com/openclaw/octopool/actions/runs/37476364368) | 0 |
| pass | blocking | `tag-ci` | CI | `main` | `bd677428d6bd` | 8m 56s | 13m 46s | 3s | [37477844440](https://github.com/openclaw/octopool/actions/runs/37477844440) | 0 |
| pass | blocking | `release` | release | `v0.9.6` | `bd677428d6bd` | 1m 41s | 1m 37s | 3s | [37477910949](https://github.com/openclaw/octopool/actions/runs/37477910949) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 9m 27s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/37476364368/job/112312827102) |
| 8m 52s | `tag-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/37477844440/job/112317865295) |
| 5m 43s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/37476364368/job/112312826685) |
| 4m 54s | `tag-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/37477844440/job/112317865648) |
| 1m 37s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/37477910949/job/112318099706) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 21s | 5m 43s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/37476364368/job/112312826685) |
| 21s | 9m 27s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/37476364368/job/112312827102) |
| 3s | 8m 52s | `tag-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/37477844440/job/112317865295) |
| 3s | 4m 54s | `tag-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/37477844440/job/112317865648) |
| 3s | 1m 37s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/37477910949/job/112318099706) |

## Notes

Octopool v0.9.6: https://github.com/openclaw/octopool/releases/tag/v0.9.6
Release commit: bd677428d6bdab39d90fd47454ce1c0cd8ba4098; annotated tag object: 15e33487bf96a60750eea8ad60e12d72a114f4de.
Release preparation: https://github.com/openclaw/octopool/pull/232. Reviewed/tested head09fbaa9695fc5e9475f49c7e934af45bd0882da2 and landed release commit share tree5f8ca7852a7e82509c0dc6697ac41d7267eeeb08. Manual CI includes the successful CLI-to-Worker token-free miss plus D1/edge hit gate and pinned GoReleaser six-platform snapshot.
Both Darwin binaries were signed by Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), with hardened runtime and secure timestamp. Both passed strict signature, Foundation requirement and notarized requirement checks after Apple acceptance.
Accepted notarizations: arm64 246ffb1d-0c1b-4974-a319-a53620d93542; amd64 43c116aa-ff22-42c9-b720-74e849344d55.
Final archive SHA256 values:
63dfabad21b7a3a3ab80e2d8f0400ce6e82b5f6f54fde2dd93cd795192bf8b46  octopool_0.9.6_darwin_amd64.tar.gz
1f7dc34f03ecf4c28f5028aa43608bc7901f4ff3e0cf222e481869d3e9e89109  octopool_0.9.6_darwin_arm64.tar.gz
8d7d7c2d666e5d643fb1d8995de13c63f6be70c430de4e5986dcecb220d2b707  octopool_0.9.6_linux_amd64.tar.gz
f04ffda65b18fba2aabbdf48bd55978186319d658bde62ede51dc0341e2f43c5  octopool_0.9.6_linux_arm64.tar.gz
6cb626e4534b60ed84d9d6bc5ac40324a61eda6fa7dcd2446d8627d4b8114532  octopool_0.9.6_windows_amd64.zip
846530fdd949d47facb23a23829353d6e99f30f692706ca06bb05987a2d3093e  octopool_0.9.6_windows_arm64.zip
Final checksums.txt SHA256: 106398fff0e04c5c24bcee667a43cbeeede2a1d592125d98d4d8273c901d53d6.
Only Darwin archives and their checksum entries changed during signing; Linux/Windows bytes retained from the successful native release build.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

