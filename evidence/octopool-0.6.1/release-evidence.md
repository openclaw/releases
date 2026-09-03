# OpenClaw Release Evidence: octopool-0.6.1

Generated: 2026-09-03T04:15:00.077Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.6.1` |
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
| pass | blocking | `release` | release | `v0.6.1` | `863ec96f74f0` | 1m 35s | 1m 31s | 3s | [33711940408](https://github.com/openclaw/octopool/actions/runs/33711940408) | 0 |
| pass | blocking | `normal-ci` | CI | `main` | `863ec96f74f0` | 5m 8s | 8m 13s | 4s | [33711423709](https://github.com/openclaw/octopool/actions/runs/33711423709) | 0 |
| pass | blocking | `homebrew` | Update octopool for v0.6.1 (octopool-061-863ec96-final) | `main` | `74e366ad2b22` | 50s | 44s | 5s | [33713189299](https://github.com/openclaw/homebrew-tap/actions/runs/33713189299) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 5s | `normal-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/33711423709/job/100511551921) |
| 3m 8s | `normal-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/33711423709/job/100511551848) |
| 1m 31s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/33711940408/job/100513114084) |
| 44s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/33713189299/job/100516831535) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 5s | 44s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/33713189299/job/100516831535) |
| 4s | 3m 8s | `normal-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/33711423709/job/100511551848) |
| 3s | 1m 31s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/33711940408/job/100513114084) |
| 2s | 5m 5s | `normal-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/33711423709/job/100511551921) |

## Notes

# Octopool 0.6.1 release verification

Octopool is a Go CLI, not an npm package. The shared evidence workflow's OpenClaw-only npm/ref resolvers are intentionally omitted; product-specific provenance was independently verified below.

- Release: https://github.com/openclaw/octopool/releases/tag/v0.6.1
- Signed annotated tag: `v0.6.1`, object `15f2e4602e956a3416574de848933fca8978d090`. GitHub reports its signature verified with reason `valid`.
- Release commit: https://github.com/openclaw/octopool/commit/863ec96f74f0432b7ce4f397b9b6b1fb166f5719
- Preparation PR: https://github.com/openclaw/octopool/pull/125 . Reviewed PR head `a99ccfcdadf1ef2bfcdf1c7011295b517dc306bd` and the release commit have the identical complete tree `61c88d82c3138847fba92c5c9446675d91a44611`.
- Release-commit CI passed Ubuntu checks and the native Windows Go/release-asset suite. Preparation PR CodeQL passed. No CI retry was required. Focused host-selector, PR-read and merge-subject tests, Go vet, documentation formatting, and the docs-site build passed; scoped Codex autoreview was clean at P0.
- All six platform archives were re-downloaded and matched the final public checksums: https://github.com/openclaw/octopool/releases/download/v0.6.1/checksums.txt . The checksums file SHA-256 is `507c3a88b31daef2e61eefe6e897d58901f1fcb8f4181b847b4eeeb440a329c3`.
- Both Darwin binaries were signed with `Developer ID Application: OpenClaw Foundation (FWJYW4S8P8)`, accepted by Apple notarization, and verified after public re-download with strict codesign and Gatekeeper install assessment reporting `Notarized Developer ID`. Linux and Windows archive bytes were unchanged by signing.
- Darwin arm64 archive SHA-256: `46a917de5c34b3e60031f5a030aa01a618664d1f3149c4e6ae4c2ad63bf0ccd8`; binary SHA-256: `3779c4cabb61b9a41ef6b3d4352d31bd989ca00df28cbfd5e6363580f5c725c1`.
- Darwin amd64 archive SHA-256: `a64d6a6be98570c9de57654112e5613e48e39154a4b30e960d186f70e6229a7a`; binary SHA-256: `1976cf9c0d90635e5b99759e860ecdde2435c19865b846e0c6c942f3eea99967`.
- The public arm64 executable reports `octopool 0.6.1 (863ec96, 2026-09-03T03:36:03Z)` and passed 14 live-policy smoke cases: all four host-qualified repository flag spellings, GitHub.com pinning against conflicting ambient host/repository settings, frozen note/asset preservation and snapshot cleanup, six unsafe-input refusals, and real read-only GitHub release/repository/merged-PR reads. Release-create smoke cases used only synthetic fixtures and a capture-only child.
- A fresh relay-only lookup of the new v0.6.1 release returned the typed `web_only_unavailable` fallback signal. Normal guarded native fallback returned the correct release; separate no-fallback repository and host-qualified merged-PR reads passed. This transport limitation is not represented as a passing relay-only release test.
- Homebrew update: https://github.com/openclaw/homebrew-tap/actions/runs/33713189299 . The protected updater independently downloaded the four public Darwin/Linux archives, verified their exact hashes, and passed its validation gates. Tap commit `3419c49b360519bcda976a0fb8b6451caf131022` contains formula blob `261d8e52881e67c31c4b4afae50fdff69c1b6bf7`, byte-identical to the reviewed candidate.
- This patch changes only the CLI and documentation. No Worker deployment, migration, or server-policy change was required or performed.

## Finalized changelog

## 0.6.1 - 2026-09-02

### Fixes

- Accept explicit `github.com/OWNER/REPO` selectors in protected releases and shared repository parsing while preserving GitHub.com host pinning and outbound rewrite checks.
- Allow protected PR branch and current-branch reads through checked native fallback, preserving GitHub CLI lookup, output, and exit semantics without loosening numeric relay or lifecycle-write rules.
- Support `gh pr merge --subject` / `-t` with bounded text rewriting and private snapshots while retaining exact-head, immediate squash-only merge restrictions.

### Upgrade notes

- This is a CLI-only patch release; no Worker deployment or database migration is required.

No credentials, policy contents, private fleet topology, signing material, or agent transcripts are included in this evidence.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

