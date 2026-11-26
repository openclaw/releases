# OpenClaw Release Evidence: octopool-0.10.0

Generated: 2026-11-26T11:07:58.621Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.10.0` |
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
| Blocking | 4 | 0 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `main-ci` | CI | `main` | `406cfe6932a7` | 5m 34s | 17m 43s | 5m 29s | [45802606689](https://github.com/openclaw/octopool/actions/runs/45802606689) | 0 |
| pass | blocking | `manual-release-smoke` | CI | `release/octopool-0.10.0-20261126` | `2d0c79109356` | 4m 34s | 16m 36s | 4m 31s | [45801636345](https://github.com/openclaw/octopool/actions/runs/45801636345) | 0 |
| pass | blocking | `release-assets` | release | `v0.10.0` | `406cfe6932a7` | 1m 40s | 1m 37s | 3s | [45803517121](https://github.com/openclaw/octopool/actions/runs/45803517121) | 0 |
| pass | blocking | `homebrew-handoff` | Update octopool for v0.10.0 (request-id=octopool-0.10.0-ca303ff5-67ca-404d-ab39-4f2ffc876ab0; source-tag-object=490e9ca5359e407468b5394d4fd545f53b94da02; source-tag-commit=406cfe6932a7f3b5b31aabb2c0f7806670b1959e) | `main` | `e7c31580dce2` | 1m 38s | 1m 34s | 4s | [45807330779](https://github.com/openclaw/homebrew-tap/actions/runs/45807330779) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 23s | `main-ci` | macos-latest Go suite | success | [job](https://github.com/openclaw/octopool/actions/runs/45802606689/job/139849438029) |
| 4m 26s | `manual-release-smoke` | Worker checks | success | [job](https://github.com/openclaw/octopool/actions/runs/45801636345/job/139846086736) |
| 4m 13s | `main-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/45802606689/job/139849437571) |
| 4m 9s | `manual-release-smoke` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/45801636345/job/139846087235) |
| 3m 53s | `main-ci` | Worker checks | success | [job](https://github.com/openclaw/octopool/actions/runs/45802606689/job/139849438156) |
| 3m 49s | `manual-release-smoke` | ubuntu-latest Go suite | success | [job](https://github.com/openclaw/octopool/actions/runs/45801636345/job/139846086970) |
| 3m 30s | `manual-release-smoke` | macos-latest Go suite | success | [job](https://github.com/openclaw/octopool/actions/runs/45801636345/job/139846087176) |
| 3m 27s | `main-ci` | ubuntu-latest Go suite | success | [job](https://github.com/openclaw/octopool/actions/runs/45802606689/job/139849437961) |
| 1m 37s | `release-assets` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/45803517121/job/139852607497) |
| 1m 34s | `homebrew-handoff` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/45807330779/job/139865913249) |
| 42s | `main-ci` | Release snapshot | success | [job](https://github.com/openclaw/octopool/actions/runs/45802606689/job/139849438110) |
| 40s | `manual-release-smoke` | Release snapshot | success | [job](https://github.com/openclaw/octopool/actions/runs/45801636345/job/139846087381) |
| 5s | `main-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/45802606689/job/139852355328) |
| 2s | `manual-release-smoke` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/45801636345/job/139848505862) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 5m 29s | 5s | `main-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/45802606689/job/139852355328) |
| 4m 31s | 2s | `manual-release-smoke` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/45801636345/job/139848505862) |
| 4s | 1m 34s | `homebrew-handoff` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/45807330779/job/139865913249) |
| 3s | 5m 23s | `main-ci` | macos-latest Go suite | success | [job](https://github.com/openclaw/octopool/actions/runs/45802606689/job/139849438029) |
| 3s | 4m 26s | `manual-release-smoke` | Worker checks | success | [job](https://github.com/openclaw/octopool/actions/runs/45801636345/job/139846086736) |
| 3s | 3m 49s | `manual-release-smoke` | ubuntu-latest Go suite | success | [job](https://github.com/openclaw/octopool/actions/runs/45801636345/job/139846086970) |
| 3s | 3m 30s | `manual-release-smoke` | macos-latest Go suite | success | [job](https://github.com/openclaw/octopool/actions/runs/45801636345/job/139846087176) |
| 3s | 4m 9s | `manual-release-smoke` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/45801636345/job/139846087235) |
| 3s | 40s | `manual-release-smoke` | Release snapshot | success | [job](https://github.com/openclaw/octopool/actions/runs/45801636345/job/139846087381) |
| 3s | 1m 37s | `release-assets` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/45803517121/job/139852607497) |
| 2s | 4m 13s | `main-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/45802606689/job/139849437571) |
| 2s | 3m 27s | `main-ci` | ubuntu-latest Go suite | success | [job](https://github.com/openclaw/octopool/actions/runs/45802606689/job/139849437961) |
| 2s | 42s | `main-ci` | Release snapshot | success | [job](https://github.com/openclaw/octopool/actions/runs/45802606689/job/139849438110) |
| 2s | 3m 53s | `main-ci` | Worker checks | success | [job](https://github.com/openclaw/octopool/actions/runs/45802606689/job/139849438156) |

## Notes

Octopool 0.10.0 was published from commit 406cfe6932a7f3b5b31aabb2c0f7806670b1959e.
- Release: https://github.com/openclaw/octopool/releases/tag/v0.10.0
- Commit: https://github.com/openclaw/octopool/commit/406cfe6932a7f3b5b31aabb2c0f7806670b1959e
- Annotated tag object: 490e9ca5359e407468b5394d4fd545f53b94da02.
- The exact release tree passed the manual CLI-to-Worker smoke and merged-main CI.
- Both Darwin binaries are signed by Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), with hardened runtime and timestamp.
- Apple accepted notarization submissions 4a663df3-049a-43cc-9d53-30ca74573772 (amd64) and d0a7f330-0c83-4c76-8ceb-93335c58a35a (arm64).
- Independent final downloads passed every archive checksum, both strict signature checks and both explicit notarized-code requirements.
- The published release body exactly matches the dated changelog section.
- No Worker deployment or fleet rollout was performed.

Final archive SHA-256 values:
- octopool_0.10.0_darwin_amd64.tar.gz: e607be023c88003e6c6cec910a00e4829414968bb94747fa111b5dfa0e8c010a
- octopool_0.10.0_darwin_arm64.tar.gz: 2a67a975a3baf6a9bd2648c281d48569df943a491e3fe7b82033ff239b4def7f
- octopool_0.10.0_linux_amd64.tar.gz: caf4708e7b57e72bd2427dfc8e6f870f2cedb22024fe1a32e855b4167976e822
- octopool_0.10.0_linux_arm64.tar.gz: fcdbcf1f94159878b427d5f65629a23030bf7b6f67a6df792013304bf7651a48
- octopool_0.10.0_windows_amd64.zip: 75d79ccf60829d6aeac68892d2607a2b2ecb6d0c4081794731b755bdf67ee97f
- octopool_0.10.0_windows_arm64.zip: 0f6845617466a6add24e5dade323d49f580186ffa8adbfd1e53c889c7c28ac34

Homebrew handoff:
- Validated native workflow: https://github.com/openclaw/homebrew-tap/actions/runs/45807330779
- Formula commit: https://github.com/openclaw/homebrew-tap/commit/a93a8a27b8f01e843b375463d2d52e63f08cebd6
- Formula version and all four URLs/hashes match the final release archives. All four public archives were downloaded and rehashed after the update.
- The released arm64 CLI reports octopool 0.10.0 (406cfe6). A fresh Homebrew installation or fleet upgrade was not performed.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

