# OpenClaw Release Evidence: octopool-0.6.3

Generated: 2026-09-08T07:40:40.211Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.6.3` |
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
| pass | blocking | `ci` | CI | `main` | `8f427935dd12` | 5m 32s | 8m 59s | 4s | [34197600180](https://github.com/openclaw/octopool/actions/runs/34197600180) | 0 |
| pass | blocking | `release` | release | `v0.6.3` | `8f427935dd12` | 1m 13s | 1m 10s | 2s | [34197602205](https://github.com/openclaw/octopool/actions/runs/34197602205) | 0 |
| pass | blocking | `homebrew` | Update octopool for v0.6.3 (request-id=octopool-063-8f42793-20260908; source-tag-object=e972772380b7cd643c950f99bb08d75438b800a6; source-tag-commit=8f427935dd12698d72bd0dc1914ca5c8b47476cd) | `main` | `55535526358a` | 1m 18s | 1m 10s | 7s | [34198755419](https://github.com/openclaw/homebrew-tap/actions/runs/34198755419) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 29s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/34197600180/job/101968710206) |
| 3m 30s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/34197600180/job/101968710441) |
| 1m 10s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/34197602205/job/101968715862) |
| 1m 10s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/34198755419/job/101972452449) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 7s | 1m 10s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/34198755419/job/101972452449) |
| 4s | 3m 30s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/34197600180/job/101968710441) |
| 2s | 5m 29s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/34197600180/job/101968710206) |
| 2s | 1m 10s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/34197602205/job/101968715862) |

## Notes

# Octopool 0.6.3 verified release

Release: https://github.com/openclaw/octopool/releases/tag/v0.6.3
Source commit: `8f427935dd12698d72bd0dc1914ca5c8b47476cd`. Signed annotated tag object: `e972772380b7cd643c950f99bb08d75438b800a6`; GitHub reports verified/valid.
Implementation: https://github.com/openclaw/octopool/pull/128

The existing protection now supports explicit CLI and REST PR base edits. Branch values retain structural validation and are never rewritten; supplied bodies still use sanitized snapshots. Base-only edits preserve unrelated content.

Local validation passed 983 unit tests, 958 Worker integration tests, Go tests/vet, formatting/types, documentation build, and the compiled CLI-to-local-Worker cache smoke test. New regression cases fail against 0.6.2 and pass with the fix, including portable preparation coverage. A Foundation-signed candidate successfully retargeted steipete/CodexBar#3486 to main; a real REST base update also succeeded through the active policy. Independent review found no actionable issues through P2.

Both Darwin binaries were signed with the OpenClaw Foundation Developer ID, notarized by Apple, then re-downloaded from the public release and verified with strict codesign and Gatekeeper (`Notarized Developer ID`). Linux and Windows archive bytes were preserved. All six public archives match the final checksums below. The public arm64 binary reports 0.6.3 with source commit 8f42793 and passes a relay-only repository read.

The canonical Homebrew workflow published `bd9bba7af53181eee068d6770b088eaa3fb26adb`. Its formula blob `6347b9189ef2be2c22dc1c00083d6f20e5689797` is byte-identical to the independently reviewed candidate and uses the final four platform hashes. Both hosted endpoints, https://octopool.openclaw.ai and https://octopool.dev, passed post-deployment smoke tests from the release commit. No database migration was required.

## Final archive checksums

```text
4dc2265eca53b7ba972e5e427b988290d07e2e220f2b45543f9abedfd120613d  octopool_0.6.3_darwin_amd64.tar.gz
a20d9d7be96673a6d9d0409abe450c33008e982c5b85dcc27aa99d3b68dfbd2c  octopool_0.6.3_darwin_arm64.tar.gz
1485303dc71970fc2c6d2a215c0a06b07b1280ebfed9c651dfb36d565255cebf  octopool_0.6.3_linux_amd64.tar.gz
44f6cfd604935bce8060bb19a120a920b2662ba30abbbf4c81e738e8de7903bd  octopool_0.6.3_linux_arm64.tar.gz
3878323b0602e67668d0863e75166e5aaa7ea9d799f2e93849edb7db7f332437  octopool_0.6.3_windows_amd64.zip
2d9a256e32624a6fc009a37b813020d7690376bd860d9c8f6e8d59a5bc9ff6e0  octopool_0.6.3_windows_arm64.zip
```

## Finalized changelog

## 0.6.3 - 2026-09-08

### Fixes

- Support protected PR base changes with `gh pr edit --base` / `-B` and REST pull-request updates, including base-only edits, while retaining branch validation, authoritative rewrite checks, host pinning, and body sanitization.

### Upgrade notes

- Upgrade the CLI to use protected PR base edits. Existing server policies remain in force and no database migration is required.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

