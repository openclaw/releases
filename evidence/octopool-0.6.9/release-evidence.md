# OpenClaw Release Evidence: octopool-0.6.9

Generated: 2026-09-20T20:18:18.293Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.6.9` |
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
| pass | blocking | `ci` | CI | `main` | `1fcf9fa1861c` | 5m 29s | 8m 49s | 4s | [35530629798](https://github.com/openclaw/octopool/actions/runs/35530629798) | 0 |
| pass | blocking | `release` | release | `v0.6.9` | `1fcf9fa1861c` | 2m 7s | 1m 28s | 38s | [35531225570](https://github.com/openclaw/octopool/actions/runs/35531225570) | 0 |
| pass | blocking | `homebrew` | Update octopool for v0.6.9 (request-id=octopool-069-7b1290a1c8ed; source-tag-object=8d0e115fe13c702cfa444ed681dc6daea8dc0cd0; source-tag-commit=1fcf9fa1861c336d9f26a48d6792bf545870ed40) | `main` | `44dccb10e7cd` | 1m 29s | 1m 20s | 8s | [35533915260](https://github.com/openclaw/homebrew-tap/actions/runs/35533915260) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 25s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35530629798/job/106130467979) |
| 3m 24s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35530629798/job/106130468057) |
| 1m 28s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/35531225570/job/106132048459) |
| 1m 20s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/35533915260/job/106139402428) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 38s | 1m 28s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/35531225570/job/106132048459) |
| 8s | 1m 20s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/35533915260/job/106139402428) |
| 4s | 3m 24s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35530629798/job/106130468057) |
| 3s | 5m 25s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35530629798/job/106130467979) |

## Notes

Octopool 0.6.9 is published at https://github.com/openclaw/octopool/releases/tag/v0.6.9.

Source commit: `1fcf9fa1861c336d9f26a48d6792bf545870ed40`. Signed annotated tag object: `8d0e115fe13c702cfa444ed681dc6daea8dc0cd0`. GitHub reports the tag signature as verified and valid. The published release body matches the finalized dated changelog below.

Both Darwin executables were signed with Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), accepted by Apple notarization, and verified for the Foundation signature, hardened runtime and Notarized Developer ID assessment. Version execution was verified separately after the signing owner returned. Fresh public downloads match all six final archive hashes and both Darwin signing checks. Independent archive inspection also confirms all six executable hashes. Linux and Windows archives retain their CI-produced bytes.

Verified CLI output: `octopool 0.6.9 (1fcf9fa, 2026-09-20T19:07:25Z)`.

Final checksums.txt SHA-256: `d81c6ef2b4d475019a74c39295467f8ac63b53ca50710c0e81201cd085869e16`.

Final archive SHA-256 values:

- octopool_0.6.9_darwin_amd64.tar.gz: `1bf43ded2e2ba67fa3fff284332a020c1f59b503c6ee93b69baf442b5c5c5bb7`
- octopool_0.6.9_darwin_arm64.tar.gz: `5c7081318a2206a31167465aa2a5cfea34c414bc47f248eb873fd515aa6b11a4`
- octopool_0.6.9_linux_amd64.tar.gz: `1b71a097f66dd804d4770e585cc122969cc2ce24e86cd771b426527620eff1f6`
- octopool_0.6.9_linux_arm64.tar.gz: `8f4be253b34e9dfaa26dae81ba5b9c535554a6e80551dce957342d9250578a8e`
- octopool_0.6.9_windows_amd64.zip: `133a5f7cc91e7e0be9721e09211840b6d322b9bc5039a036e3208aa02356b1d5`
- octopool_0.6.9_windows_arm64.zip: `15573585bcc3bba8796cbe65b23579e7dd22db9ecdd98aacf66b7072f7642d22`

Final executable SHA-256 values:

- darwin_amd64: `31ffe66e04e6fad51ab4be1f58cf5a1ee7d3a59346668c901512a3e182b3648e`
- darwin_arm64: `d45a2565740226b4b403e57682a1d089e5a8525494226b48d44708878b52e78a`
- linux_amd64: `d13a4899343c02872f7c0886cd736023d214ab810f2469b8bd521b8cbe0b8ff1`
- linux_arm64: `67dd3966cbf829bc5af0b941f40046c1cab2d068d5ba55de72bf1d0dc1379835`
- windows_amd64: `c9e9ac05ffb978a6f1e88b75a996806f27f7372e18bec011fbb0c93eb910560a`
- windows_arm64: `38d7b05b53fad5c04cb2587da740fccf6b044911d0d8ea84f60c6f02016cab11`

Apple notarization submissions:

- darwin_amd64: `6e988307-cbce-4e76-88c6-38e495ef469c` (Accepted)
- darwin_arm64: `18c06e79-9af3-43a3-88b3-b0db7da74abd` (Accepted)

Homebrew promotion: https://github.com/openclaw/homebrew-tap/commit/5819d1725537a68fc744d1ab1cd3f2af3a3d65dd. Formula SHA-256: `71ccb431e1020e2509ce1d44eaf72ba38448dbff3bdd352f8d8fe9cfcdc7e8e4`. The published formula matches the reviewed candidate and final four platform archive hashes.

The source CI, release publication and Homebrew promotion runs listed in this evidence all completed successfully. Source CI and release publication both ran at `1fcf9fa1861c336d9f26a48d6792bf545870ed40`. This release requires no database migration, re-login or cache purge.

Finalized changelog:

## 0.6.9 - 2026-09-20

### Fixes

- Route PR views requesting `mergeCommit` through the shared relay with fresh merge metadata, preserving native object/null output and avoiding personal-token GraphQL delegation for supported field combinations.
- Reuse fresh raw workflow-list metadata for numeric workflow views, avoiding repeated workflow-name hydration requests while preserving complete REST objects, source expiry, visibility, identity eligibility, and explicit freshness.

### Upgrade notes

- Upgrade the CLI for `mergeCommit` relay coverage and deploy the Workers for workflow-metadata cache reuse. No database migration, re-login, or cache purge is required.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

