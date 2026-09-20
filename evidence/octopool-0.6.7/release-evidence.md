# OpenClaw Release Evidence: octopool-0.6.7

Generated: 2026-09-20T01:15:09.991Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.6.7` |
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
| pass | blocking | `ci` | CI | `main` | `5a75431ba354` | 5m 40s | 8m 59s | 3s | [35479572683](https://github.com/openclaw/octopool/actions/runs/35479572683) | 0 |
| pass | blocking | `release` | release | `v0.6.7` | `5a75431ba354` | 1m 35s | 1m 32s | 2s | [35479794977](https://github.com/openclaw/octopool/actions/runs/35479794977) | 0 |
| pass | blocking | `homebrew` | Update octopool for v0.6.7 (request-id=octopool-0.6.7-c538020c; source-tag-object=c538020c7ff850ef18cd432c59ac70e53c81bef4; source-tag-commit=5a75431ba354c39ffe02403beb88320f225a58e8) | `main` | `e331027db108` | 1m 19s | 1m 11s | 7s | [35480630546](https://github.com/openclaw/homebrew-tap/actions/runs/35480630546) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 36s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35479572683/job/105994813468) |
| 3m 23s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35479572683/job/105994813435) |
| 1m 32s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/35479794977/job/105995423269) |
| 1m 11s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/35480630546/job/105997663165) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 7s | 1m 11s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/35480630546/job/105997663165) |
| 3s | 3m 23s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35479572683/job/105994813435) |
| 3s | 5m 36s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35479572683/job/105994813468) |
| 2s | 1m 32s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/35479794977/job/105995423269) |

## Notes

Octopool 0.6.7 is published at https://github.com/openclaw/octopool/releases/tag/v0.6.7 .

Source commit: 5a75431ba354c39ffe02403beb88320f225a58e8. Signed annotated tag object: c538020c7ff850ef18cd432c59ac70e53c81bef4 (GitHub signature verification: valid). The release body matches the finalized 0.6.7 changelog section.

Both Darwin binaries were signed with Developer ID Application: OpenClaw Foundation (FWJYW4S8P8). Notarization submissions were Accepted: amd64 5e8032c0-dffb-4612-8186-917531439913; arm64 d7581e54-d0f3-4673-af69-543a309e5a89. Freshly downloaded public archives match final checksums. Both Darwin binaries pass strict codesign verification and spctl install assessment as Notarized Developer ID. Linux and Windows archives retain the CI-produced bytes.

Version output: octopool 0.6.7 (5a75431, 2026-09-20T00:50:07Z).

Final archive SHA-256 values:

- octopool_0.6.7_darwin_amd64.tar.gz: bce608f0bc16cd6250b28dfacdfe5ae5dedf723718019e451c5ecb0e0fa53437
- octopool_0.6.7_darwin_arm64.tar.gz: 1a0dd966ef242803eb4c5ecb56d9a2a0b4f1d26911f037bbed0bb59849a408a3
- octopool_0.6.7_linux_amd64.tar.gz: e15074baaa9b3d1d8b79e2fff2defe9cf8d6af9ab21a391e2c1c2d4dc5ca589d
- octopool_0.6.7_linux_arm64.tar.gz: 0ef2c09cbd428a286d329203f2da0014012c847665c88a49933d32cb6e63bc70
- octopool_0.6.7_windows_amd64.zip: a4dfe9ce76579a6bc2488b52c1af7a03134067219eff37c6b0545968b4dcc3f3
- octopool_0.6.7_windows_arm64.zip: de8164607ce47781a118d447b5aba7dacd67aed8c1fcd8aa95a03d5d2a8b9cd3

Final extracted binary SHA-256 values:

- octopool_0.6.7_darwin_amd64.tar.gz: 5963bb71c1e3d2dd1276bb0d20a7dac2d60b4b3eab0e3a873e9c596346c156d1
- octopool_0.6.7_darwin_arm64.tar.gz: 15dce2c9acc5687b771660a0e8445f7bba7f098c0a574238512658c9df939e8d
- octopool_0.6.7_linux_amd64.tar.gz: 16600175f65ca3ebc116de49142a9f4b7e698f660051e6fe3e059d8a79a329fe
- octopool_0.6.7_linux_arm64.tar.gz: d7268f4bf464fcb9e4f92ebd2206f04b02551a79dfd3e6e7d7cd3a81fdbd0f92
- octopool_0.6.7_windows_amd64.zip: 950603d3185759cc20720aa2fc2aa811299b29e6c9ae387324ebf19302431e17
- octopool_0.6.7_windows_arm64.zip: 37a259a288f03988c64dc08e3d817e1e9c0e754ec56884044678c7fca8420787

Homebrew promotion: https://github.com/openclaw/homebrew-tap/commit/2595e82773861621b75a14e6b7eb88bf9952ac17 . Formula SHA-256: e7649aebe413a6c2bd13652b8ea45c5a3798328ff61f7beb9ff5a9e7d9864c21. All four archive hashes match final publication; provenance names the exact tag object and commit.

Both Cloudflare Workers deployed from the release commit and verified at 100% traffic: authoritative version 93d8971c-a3eb-46fc-84fa-1b4069eed030; public proxy version 264034e7-448d-46cc-a154-d7d3760dae0f. Public smoke suites and an authenticated no-fallback relay read passed. Deployment completed 2026-09-20T01:03:11Z. No schema migration was required.

Changes landed in https://github.com/openclaw/octopool/pull/147 and https://github.com/openclaw/octopool/pull/148 . Targeted live filtered-cache reproduction reduced actual anonymous GitHub fetches from two to zero with identical results. This is scoped reproduction evidence, not a fleet-wide quota estimate.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

