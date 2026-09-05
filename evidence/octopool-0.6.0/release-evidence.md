# OpenClaw Release Evidence: octopool-0.6.0

Generated: 2026-09-02T00:42:35.212Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.6.0` |
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
| pass | blocking | `release` | release | `v0.6.0` | `231ce460f6fd` | 1m 26s | 1m 22s | 3s | [33574651417](https://github.com/openclaw/octopool/actions/runs/33574651417) | 0 |
| pass | blocking | `normal-ci` | CI | `steipete/release-validation-0901` | `1cc83aca526b` | 5m 19s | 8m 27s | 7s | [33568590029](https://github.com/openclaw/octopool/actions/runs/33568590029) | 0 |
| pass | blocking | `homebrew` | Update octopool for v0.6.0 (octopool-060-231ce46-final) | `main` | `549fdfb08e7a` | 47s | 42s | 5s | [33576034744](https://github.com/openclaw/homebrew-tap/actions/runs/33576034744) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 12s | `normal-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/33568590029/job/100057344993) |
| 3m 15s | `normal-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/33568590029/job/100057345143) |
| 1m 22s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/33574651417/job/100075840698) |
| 42s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/33576034744/job/100080093867) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 7s | 5m 12s | `normal-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/33568590029/job/100057344993) |
| 5s | 3m 15s | `normal-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/33568590029/job/100057345143) |
| 5s | 42s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/33576034744/job/100080093867) |
| 3s | 1m 22s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/33574651417/job/100075840698) |

## Notes

# Octopool 0.6.0 release verification

Octopool is a Go CLI, not an npm package. The shared evidence workflow's optional OpenClaw-only npm/ref resolvers are intentionally omitted; product-specific provenance was independently verified below.

- Release: https://github.com/openclaw/octopool/releases/tag/v0.6.0
- Signed annotated tag: `v0.6.0`; GitHub reports its signature verified and valid.
- Release commit: https://github.com/openclaw/octopool/commit/231ce460f6fd00705606fd762bced3c0ad634122
- Reviewed CI head `1cc83aca526b9ebc5a451b794be9054ca2cd2989` has an identical complete tree to the release commit. Preparation PR: https://github.com/openclaw/octopool/pull/120
- Release notes exactly match the finalized `0.6.0` changelog section. Highlights are ordered by user impact; historical sections were preserved; no future Unreleased section was added.
- Six public platform archives were downloaded and verified against the final public `checksums.txt`: https://github.com/openclaw/octopool/releases/download/v0.6.0/checksums.txt
- Both Darwin binaries were signed with OpenClaw Foundation Developer ID, accepted by Apple notarization, and assessed as `Notarized Developer ID`. These checks were repeated on the re-downloaded public archives. Linux and Windows archive bytes were unchanged by the signing step.
- The canonical OpenClaw Homebrew formula is 0.6.0 and matches the reviewed generated update byte-for-byte, with all four final Darwin/Linux hashes. Protected updater run: https://github.com/openclaw/homebrew-tap/actions/runs/33576034744 ; tap commit: https://github.com/openclaw/homebrew-tap/commit/4087ade135301b4fdee1de5d1cf6ca4d67490b4c . The updater independently downloaded and checked the public assets and passed its tests/style gates.
- The published Linux amd64 archive was independently downloaded and checksum-verified in a non-root clean Linux environment, extracted, and executed. It reported `octopool 0.6.0 (231ce46, 2026-09-02T00:16:40Z)` and passed an actual CLI → local Worker/D1 → public GitHub read with a token-free miss followed by a cache hit.
- Full validation included 983 unit tests, 958 native Workerd integration tests, the complete Go suite, and full native Windows CI. The expanded exact-head live matrix covered 16 distinct cases across positive and selected continuation runs: real miss/hit/304/restart behavior, stable PR/issue/run/job parity, exact release Markdown, four-way immutable-content reads with observed coalescing, raw diff bytes, typed negative/native boundaries, and protected asset preparation.
- The confirmed workflow-job bug was reproduced at the actual compiled CLI boundary: duplicate IDs and foreign run/head records falsely completed in the baseline; the fixed candidate exits 1 without a final job summary or native child. A real completed-run watch also passed with native fallback forbidden.
- Asset tests used an active synthetic policy and a capture-only native child. Four opaque files retained names/order/digests, notes and empty stdin were preserved, private modes and cleanup were verified, invalid filenames were rejected, and a nonzero child exit was preserved. No synthetic release content was uploaded to an unapproved GitHub destination.
- The authorized hosted rollout applied and verified migrations 0017–0020, then deployed both Workers from the release commit at full traffic. Existing credentials and rules were not rewritten; the policy revision remained unchanged. All ten post-rollout production read checks and a no-fallback watch passed, including restored exact raw release Markdown.
- Initial validation interruptions were infrastructure/harness assumptions, not hidden product fixes: a missing remote Go toolchain, package-manager probe context, and the intentional 424/no-identity audit outcome after anonymous 404 probes. The pinned deployment checkout's dependencies were installed and both Worker bundles prebuilt before the successful deployment retry.

No raw logs, credentials, policy contents, private provider payloads, signing material, or agent transcripts are included in this evidence.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

