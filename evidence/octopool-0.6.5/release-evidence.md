# OpenClaw Release Evidence: octopool-0.6.5

Generated: 2026-09-19T01:00:36.315Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.6.5` |
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
| Blocking | 2 | 0 | 0 | 0 |
| Advisory | 1 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `ci` | CI | `main` | `7ebc5005ffb4` | 4m 37s | 7m 59s | 4s | [35410712697](https://github.com/openclaw/octopool/actions/runs/35410712697) | 0 |
| pass | blocking | `release` | release | `v0.6.5` | `7ebc5005ffb4` | 1m 23s | 1m 19s | 3s | [35410714446](https://github.com/openclaw/octopool/actions/runs/35410714446) | 0 |
| pass | advisory | `codeql` | Push on main | `main` | `7ebc5005ffb4` | 1m 35s | 3m 26s | 6s | [35410711980](https://github.com/openclaw/octopool/actions/runs/35410711980) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 4m 32s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35410712697/job/105809651380) |
| 3m 27s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35410712697/job/105809651234) |
| 1m 28s | `codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/35410711980/job/105809650226) |
| 1m 19s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/35410714446/job/105809655515) |
| 1m 13s | `codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/35410711980/job/105809650150) |
| 45s | `codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/35410711980/job/105809650266) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 6s | 1m 28s | `codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/35410711980/job/105809650226) |
| 5s | 45s | `codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/35410711980/job/105809650266) |
| 4s | 3m 27s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35410712697/job/105809651234) |
| 4s | 4m 32s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35410712697/job/105809651380) |
| 4s | 1m 13s | `codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/35410711980/job/105809650150) |
| 3s | 1m 19s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/35410714446/job/105809655515) |

## Notes

Octopool 0.6.5 (CLI-only patch; Cloudflare Worker unchanged, no deploy and no D1 migration).

Verified locators:
- Tag: https://github.com/openclaw/octopool/releases/tag/v0.6.5 (annotated, SSH-signed, verified by GitHub)
- Commit: openclaw/octopool@7ebc5005ffb4ff6889ddf6c3a36fbee65e4bcb76 (chore(release): prepare Octopool 0.6.5)
- Release: https://github.com/openclaw/octopool/releases/tag/v0.6.5
- Release body matches the dated CHANGELOG.md 0.6.5 section exactly (workflow-enforced).

Signing and notarization (maintainer Mac, Foundation Developer ID):
- Identity: Developer ID Application: OpenClaw Foundation (FWJYW4S8P8); codesign --force --options runtime --timestamp.
- Notarization accepted: darwin arm64 submission acaacaf6-b3fb-4464-9069-52577e5f6cb4; darwin amd64 submission e0a661f8-2358-4848-b166-043fa8cd5305.
- Gatekeeper assessment on both repackaged binaries: source=Notarized Developer ID, origin=Developer ID Application: OpenClaw Foundation (FWJYW4S8P8).

Final published checksums (post-signing, checksums.txt re-uploaded with --clobber):
- 55130cc686cfd5f6522a94e6f4f8d4db75ab05a132aeeef01d3ab79c667ea0b3  octopool_0.6.5_darwin_arm64.tar.gz
- 3f49d6a8f9cba1203c17759e34fe8e7ac342ea53dc2a2de8641379a1424d1357  octopool_0.6.5_darwin_amd64.tar.gz
- c1f4a3b93c4d772ef4ea8f03b5ef02469dee01f7b0719d9d75d95da594f17e19  octopool_0.6.5_linux_arm64.tar.gz
- cf0a0e9ed35e3125f4aaa27f418c87e1bc2584f14d71074f4e5ea92f4484e890  octopool_0.6.5_linux_amd64.tar.gz
Re-downloaded published assets and recomputed all four digests: match.

Homebrew: openclaw/homebrew-tap@b8451e3 "octopool: update formula for v0.6.5" carries these four post-signing digests.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

