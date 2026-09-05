# OpenClaw Release Evidence: octopool-0.5.9

Generated: 2026-08-29T02:40:18.278Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.5.9` |
| Release ref input | `v0.5.9` |
| Release ref status | not-found |
| Release ref kind | unknown |
| Release ref name | unknown |
| Release ref SHA | not resolved |
| Runs at release SHA | none |
| Package spec | `octopool@0.5.9` |
| npm status | invalid |
| npm error | only openclaw package specs are supported |

## Summary

| Class | Passed | Failed | Skipped | Incomplete |
| --- | ---: | ---: | ---: | ---: |
| Blocking | 3 | 0 | 0 | 0 |
| Advisory | 0 | 0 | 0 | 0 |

## Runs

| Result | Class | Label | Workflow | Ref | SHA | Duration | Job Time | Max Queue | Run | Artifacts |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: |
| pass | blocking | `release` | release | `v0.5.9` | `b95ae653e17f` | 1m 10s | 1m 8s | 2s | [33225542541](https://github.com/openclaw/octopool/actions/runs/33225542541) | 0 |
| pass | blocking | `check` | CI | `main` | `b95ae653e17f` | 3m 36s | 3m 31s | 5s | [33225517546](https://github.com/openclaw/octopool/actions/runs/33225517546) | 0 |
| pass | blocking | `homebrew` | Update octopool for v0.5.9 (request-id=octopool-0.5.9-20260828-uvnv4q; source-tag-object=2b578d90e36e3f247a5e9ba3dcd2f824790d679f; source-tag-commit=b95ae653e17f50ec29e064810d798cdbba74a5e6) | `main` | `ad6348abcb88` | 36s | 31s | 4s | [33226092782](https://github.com/openclaw/homebrew-tap/actions/runs/33226092782) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 3m 31s | `check` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/33225517546/job/99028385880) |
| 1m 8s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/33225542541/job/99028456948) |
| 31s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/33226092782/job/99030042366) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 5s | 3m 31s | `check` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/33225517546/job/99028385880) |
| 4s | 31s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/33226092782/job/99030042366) |
| 2s | 1m 8s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/33225542541/job/99028456948) |

## Notes

Octopool 0.5.9 is a Go CLI/GitHub Release, not an npm publication. The generic collector resolves release refs against openclaw/openclaw and accepts only OpenClaw npm specs; its Octopool ref/package statuses are expected limitations, not failures of this release. The authoritative Octopool provenance is recorded below.

Release: [Octopool v0.5.9](https://github.com/openclaw/octopool/releases/tag/v0.5.9)

The GitHub-verified signed annotated tag object is `2b578d90e36e3f247a5e9ba3dcd2f824790d679f`, peeling to source commit `b95ae653e17f50ec29e064810d798cdbba74a5e6`. The release workflow and release-commit CI both succeeded. Published release notes exactly match the dated 0.5.9 changelog section, including the migration/Worker-before-CLI upgrade requirement.

Both Darwin architectures were signed with the OpenClaw Foundation Developer ID (team `FWJYW4S8P8`), accepted by Apple notarization, and assessed as `Notarized Developer ID`. All six public archives and `checksums.txt` were downloaded and verified against their final SHA-256 values and GitHub asset digests. Final `checksums.txt` SHA-256: `6a376bfb6e8e4b00694b9c5884c008f0f89cfab7e997db27aef594e82d762255`.

The protected Homebrew verified-hash workflow succeeded as run `33226092782`. Tap commit `459a0607201ab7c13896c00b4226ff2259722334` is a direct child of the dispatched protected head and records the exact source-tag object/commit plus request ID `octopool-0.5.9-20260828-uvnv4q`. Its four platform checksums match the final release, and all four public Homebrew archives plus the checksum manifest were downloaded and verified again after tap publication.

The Worker was already deployed and live-tested from runtime-identical merged commit `e8bbc89e1b4d42266a445fdb14d43535eb9de08c`; the release commit changes only the changelog. Both public hosts served the compatible policy endpoint. Sixteen real Cloudflare/GitHub checks passed, including actual file/stdin/inline rewriting and purging, server denials, freshness, and a corrupt-policy failure that left the GitHub comment unchanged ([live proof](https://github.com/openclaw/octopool/pull/66#issuecomment-5459050383)). The published, signed 0.5.9 binary also independently blocked a task-local synthetic rule without echoing the matched text. No private-name rules were enabled for these proofs.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

