# OpenClaw Release Evidence: octopool-0.6.6

Generated: 2026-09-19T22:34:37.535Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.6.6` |
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
| pass | blocking | `source-ci` | CI | `main` | `91d9c4c0f2c3` | 4m 19s | 8m 1s | 2s | [35472036375](https://github.com/openclaw/octopool/actions/runs/35472036375) | 0 |
| pass | blocking | `release` | release | `v0.6.6` | `91d9c4c0f2c3` | 1m 30s | 1m 27s | 2s | [35472259637](https://github.com/openclaw/octopool/actions/runs/35472259637) | 0 |
| pass | blocking | `homebrew` | Update octopool for v0.6.6 (request-id=octopool-0.6.6-18cf84d5; source-tag-object=18cf84d5c0aa6423ae8d22b348dea660b10f0cd3; source-tag-commit=91d9c4c0f2c360c97b126253194bd2822218ec42) | `main` | `e2d0ebd35474` | 1m 25s | 1m 16s | 8s | [35472980727](https://github.com/openclaw/homebrew-tap/actions/runs/35472980727) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 4m 16s | `source-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35472036375/job/105974623781) |
| 3m 45s | `source-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35472036375/job/105974623729) |
| 1m 27s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/35472259637/job/105975231934) |
| 1m 16s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/35472980727/job/105977243424) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 8s | 1m 16s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/35472980727/job/105977243424) |
| 2s | 3m 45s | `source-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35472036375/job/105974623729) |
| 2s | 4m 16s | `source-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35472036375/job/105974623781) |
| 2s | 1m 27s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/35472259637/job/105975231934) |

## Notes

Octopool v0.6.6 is a Go CLI release. No npm package resolution applies.

- PR: https://github.com/openclaw/octopool/pull/146
- Release: https://github.com/openclaw/octopool/releases/tag/v0.6.6
- Release commit: `91d9c4c0f2c360c97b126253194bd2822218ec42`
- Signed annotated tag object: `18cf84d5c0aa6423ae8d22b348dea660b10f0cd3`; GitHub verification is valid.
- Final release body exactly matches the dated 0.6.6 changelog section.
- Homebrew publication commit: `a8c042656426cd37e7bd091c60771acc9b05774c`; all four platform hashes match the final public archives.
- Both Darwin binaries are signed by OpenClaw Foundation (FWJYW4S8P8), notarized by Apple, and accepted as Notarized Developer ID after downloading the public release again.
- Linux and Windows archive bytes are unchanged from GoReleaser. All six final public archive hashes and GitHub asset digests were verified.
- Worker `octopool` version `d739acf9-5ea9-4bb3-a3a8-a3ea1da4cd43` and public proxy version `75886861-77e9-4944-8e86-2a4fe4c24349` were deployed from the release commit with existing vars preserved. Both post-deployment smoke suites and an authenticated relay-only read passed. No database migration or TTL change was required.
- The compiled CLI-to-local-Worker release gate passed. PR evidence contains bounded Workerd/D1/DO before/after proofs using real GitHub REST transport, with controlled failure injection explicitly identified.

### Final public archive SHA-256

- `octopool_0.6.6_darwin_amd64.tar.gz`: `c73f07d286bdb85b457e8d3dad3ffe0d89a37a8a1981481096b553dbea74c27e`
- `octopool_0.6.6_darwin_arm64.tar.gz`: `88c2c3b1842457b0c78825948168d749d1cef21c8bf8a1e1c012393166554e2e`
- `octopool_0.6.6_linux_amd64.tar.gz`: `8d82b81bfd96c34a640147132d76b2c06d0b1cee893fe0c818c664dbec8d0824`
- `octopool_0.6.6_linux_arm64.tar.gz`: `5ec0a0a473d33aa7141910cc6b0fa1c4841993b35797dd2753e0c639725fb5f9`
- `octopool_0.6.6_windows_amd64.zip`: `8955b9d5b4cb794d7ced68d828fcd8868f4a80b003df239513d72746f0fbbd41`
- `octopool_0.6.6_windows_arm64.zip`: `19ab8a5aad882cf33123fb8864f79dc4b13d422525869341c16abae7567d64b0`

### Apple notarization

- `darwin_amd64`: `3419848e-db7b-4337-a818-667f69f47671`, `Accepted`
- `darwin_arm64`: `814383fd-d495-4ed0-8456-f5fc4bc1ddab`, `Accepted`

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

