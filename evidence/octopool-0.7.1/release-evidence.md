# OpenClaw Release Evidence: octopool-0.7.1

Generated: 2026-09-21T19:35:34.443Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.7.1` |
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
| pass | blocking | `ci` | CI | `main` | `7ab9b348c99a` | 5m 55s | 8m 38s | 43s | [35643994397](https://github.com/openclaw/octopool/actions/runs/35643994397) | 0 |
| pass | blocking | `release` | release | `v0.7.1` | `7ab9b348c99a` | 1m 29s | 1m 23s | 5s | [35643996509](https://github.com/openclaw/octopool/actions/runs/35643996509) | 0 |
| pass | blocking | `homebrew` | Update octopool for v0.7.1 (octopool-0.7.1-d9d7c778-4e0b-4c76-ac73-05003396342f) | `main` | `2fae7f2f3b9f` | 1m 21s | 1m 13s | 8s | [35645313539](https://github.com/openclaw/homebrew-tap/actions/runs/35645313539) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 5m 13s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35643994397/job/106480095824) |
| 3m 25s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35643994397/job/106480096112) |
| 1m 23s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/35643996509/job/106479884681) |
| 1m 13s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/35645313539/job/106484221630) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 43s | 3m 25s | `ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35643994397/job/106480096112) |
| 42s | 5m 13s | `ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35643994397/job/106480095824) |
| 8s | 1m 13s | `homebrew` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/35645313539/job/106484221630) |
| 5s | 1m 23s | `release` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/35643996509/job/106479884681) |

## Notes

# Octopool 0.7.1 verification

Release: https://github.com/openclaw/octopool/releases/tag/v0.7.1
Source commit: `7ab9b348c99a7be4fdc82c75cb06ebce44e0007e`.
Signed annotated tag object: `a94ba5106c0c75c6ba40cda72b7b3e71d6cda4c6`; local SSH verification and GitHub verification both pass.
CLI version: `octopool 0.7.1 (7ab9b34, 2026-09-21T19:18:42Z)`.

The release includes protected native auto-merge support, request-scoped pending Worker configuration lookups, and the single-argument native command repair from https://github.com/openclaw/octopool/pull/181. The regression fails before the repair, then passes along with unsafe-input rejection cases. The published signed shim passes bare `gh browse` in an OpenClaw checkout and a fresh relay-only repository read.

Full CI passes at the release commit, including `pnpm check`, the native Windows Go suite, docs generation, and a release snapshot build. The compiled CLI-to-local-Worker/D1/Durable Objects release gate passes against public GitHub with a token-free miss followed by a cache hit. All six published release archives were downloaded independently and matched the finalized checksums. Linux and Windows retain their CI-produced bytes.

Both independently downloaded Darwin binaries pass strict codesign verification with Developer ID Application: OpenClaw Foundation (`FWJYW4S8P8`) and Gatekeeper assessment reports `Notarized Developer ID`.

- Darwin amd64 notarization: `61d196ef-c8fb-47db-bc90-57d572105c9f` (`Accepted`).
- Darwin arm64 notarization: `3e9d5d44-3fe0-45f3-9d67-2ed2e3382cc7` (`Accepted`).

| Target | Archive SHA-256 | Binary SHA-256 |
| --- | --- | --- |
| darwin_amd64 | `7c25707fd2cb7c31ed35b93d9481987318f2045c310abf8d3045a4d42d9e7697` | `3c915f1acf87cf2125df06bb78b650c45f8d8206633d2066d52aa131e49eaba2` |
| darwin_arm64 | `cf0fb8dd79928a12172e1e575af0a3fd338ab836bc83469cebda491c46a279aa` | `2d732a74133cc68481b453afc630c7ca6651ad5a613931ad777c3bc6b1b17d7e` |
| linux_amd64 | `f2e3ecfb9f43bdd84e91d8e5b465d261a1352a2c0adc7f7eb4b4e98dcca6833a` | `ee2494f2ff691ba8e8b658f77e028fb62ff029f845bde920f33344e8188dc7bc` |
| linux_arm64 | `a85d915105c8d68dee6b9a07c0a83b9f3fe8bcd61fa61635963fd7aae1f5fcbe` | `10df09d1d01f772260cc4efc58883c03bd56644bcb66974ea0a54e093b2fcbfa` |
| windows_amd64 | `94d03776568e73aeaaec25a29ed27ee4a4ef0eb9e4401f0792d7efc5715f513a` | `537a44d3de58bb716b54851ffe90c4d0ba56628b10da86fbd2a775ab8d609bc5` |
| windows_arm64 | `db6ae2eb6706b1d397a99ceec7d8e0d4c745139dc35d7afd3741273ed5094c04` | `a8dc2bfd3bb54236b88dd9a86c1ada4eeee863be3d09569ea928acff804a89fb` |

Final `checksums.txt` SHA-256: `a266c8b3a1e26aad2677683bd9f5231ba71834d4aeda62d85f77672cd4ea3b1b`.

Both production Workers serve the release source at 100%: authoritative `7a1ef941-0c4d-44b0-bcc9-e50b1ec96dd6`, public proxy `642d941b-2ebf-43d8-9ba1-6121d9c6fdac`. Version metadata binds `v0.7.1` and the exact source commit; both public smoke suites pass. No migration, re-login, or cache purge is required.

Homebrew promotion succeeded: https://github.com/openclaw/homebrew-tap/actions/runs/35645313539. Tap commit `ca82c71b720f6990dcc2ca6fe9b123595f660fce` publishes the exact reviewed final formula; formula SHA-256 is `a503d92ce4d54ac08144077148452921ab51b08cfe252d8c4cc4fb5a75d1ff56`. All four formula hashes match the finalized public archives.

The published release body exactly matches the following finalized changelog:

## 0.7.1 - 2026-09-21

### Fixes

- Keep pending configuration and caller-membership lookups within one Worker request, preventing unrelated policy reads from hanging on abandoned loads while preserving the shared 30-second cache of settled values.
- Allow single-argument native commands such as `gh browse` through guarded fallback, fixing repository discovery in OpenClaw's `scripts/pr review-init` while retaining string rewriting and unsafe-input rejection.
- Allow protected `gh pr merge --auto --squash` with a full submission head SHA and explicitly sanitized subject/body, retaining private body snapshots, final policy checks, native exit codes, and distinguishable pre-dispatch diagnostics.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

