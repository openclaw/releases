# OpenClaw Release Evidence: octopool-0.7.2

Generated: 2026-09-23T04:21:05.194Z

## Provenance

| Field | Value |
| --- | --- |
| Evidence id | `octopool-0.7.2` |
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
| pass | blocking | `release-commit-ci` | CI | `main` | `720b57adccff` | 6m 13s | 9m 50s | 6s | [35816439418](https://github.com/openclaw/octopool/actions/runs/35816439418) | 0 |
| pass | blocking | `release-commit-codeql` | Push on main | `main` | `720b57adccff` | 1m 25s | 3m 15s | 7s | [35816438922](https://github.com/openclaw/octopool/actions/runs/35816438922) | 0 |
| pass | blocking | `release-artifacts` | release | `v0.7.2` | `720b57adccff` | 1m 12s | 1m 6s | 5s | [35816904288](https://github.com/openclaw/octopool/actions/runs/35816904288) | 0 |
| pass | blocking | `homebrew-promotion` | Update octopool for v0.7.2 (request-id=octopool-0.7.2-ce0cdfeecb37; source-tag-object=8fea359d72af92416841a4c7eb7af61a37c50d9f; source-tag-commit=720b57adccff0fa0ef09ab7cfd5afb896528782d) | `main` | `a94a29aa60a5` | 1m 47s | 1m 28s | 18s | [35817403951](https://github.com/openclaw/homebrew-tap/actions/runs/35817403951) | 0 |

## Slowest Jobs

| Duration | Run | Job | Result | Link |
| ---: | --- | --- | --- | --- |
| 6m 6s | `release-commit-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35816439418/job/107038865990) |
| 3m 44s | `release-commit-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35816439418/job/107038865789) |
| 1m 28s | `homebrew-promotion` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/35817403951/job/107041793816) |
| 1m 18s | `release-commit-codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/35816438922/job/107038867226) |
| 1m 12s | `release-commit-codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/35816438922/job/107038867124) |
| 1m 6s | `release-artifacts` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/35816904288/job/107040250722) |
| 45s | `release-commit-codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/35816438922/job/107038866936) |

## Longest Queues

| Queue | Duration | Run | Job | Result | Link |
| ---: | ---: | --- | --- | --- | --- |
| 18s | 1m 28s | `homebrew-promotion` | update-formula | success | [job](https://github.com/openclaw/homebrew-tap/actions/runs/35817403951/job/107041793816) |
| 7s | 45s | `release-commit-codeql` | Analyze (actions) | success | [job](https://github.com/openclaw/octopool/actions/runs/35816438922/job/107038866936) |
| 7s | 1m 18s | `release-commit-codeql` | Analyze (go) | success | [job](https://github.com/openclaw/octopool/actions/runs/35816438922/job/107038867226) |
| 6s | 6m 6s | `release-commit-ci` | Check | success | [job](https://github.com/openclaw/octopool/actions/runs/35816439418/job/107038865990) |
| 6s | 1m 12s | `release-commit-codeql` | Analyze (javascript-typescript) | success | [job](https://github.com/openclaw/octopool/actions/runs/35816438922/job/107038867124) |
| 5s | 3m 44s | `release-commit-ci` | Windows Go suite and release asset helpers | success | [job](https://github.com/openclaw/octopool/actions/runs/35816439418/job/107038865789) |
| 5s | 1m 6s | `release-artifacts` | goreleaser | success | [job](https://github.com/openclaw/octopool/actions/runs/35816904288/job/107040250722) |

## Notes

Octopool 0.7.2 is published at https://github.com/openclaw/octopool/releases/tag/v0.7.2.

Source commit: `720b57adccff0fa0ef09ab7cfd5afb896528782d`. Signed annotated tag object: `8fea359d72af92416841a4c7eb7af61a37c50d9f`; GitHub reports a valid signature.

Both Darwin binaries are signed by Developer ID Application: OpenClaw Foundation (FWJYW4S8P8), notarized with Accepted results, and pass strict Team ID, hardened runtime and Gatekeeper checks after public redownload. All six public archives match the final checksums; Linux and Windows bytes are unchanged from CI. CLI version: `octopool 0.7.2 (720b57a, 2026-09-23T04:05:30Z)`.

Final checksums.txt SHA-256: `de7a7ba8e0c2df70f6cb26ba4a17ac554bb7c91fb4eddae24ad1bc70f90f98f7`. Homebrew promotion `c7a476cee74951ebbf4180b21800e70a45024494` matches the expected four-platform formula and final signed hashes.

| Asset | SHA-256 |
|---|---|
| octopool_0.7.2_darwin_amd64.tar.gz | `6a865c7a463b87ade5b3d6f8e1470b0ed74dc8459611600dc918784131b4ba53` |
| octopool_0.7.2_darwin_arm64.tar.gz | `70538bec076c520e464b127bd13ebe79bf7faa7339e2ec68a3102bb745de457e` |
| octopool_0.7.2_linux_amd64.tar.gz | `f24686a1b829fbdd4ae3723de7aacfe1ebf51767d85d011e183621a4c36a5e7a` |
| octopool_0.7.2_linux_arm64.tar.gz | `cd56f07fea48dc07704f8248af8edc34bb8407a7872450b4fb865ba6247154d0` |
| octopool_0.7.2_windows_amd64.zip | `1c206c9f05eb9b8ea2cf8d47a03f53cdfd847323874267d30a2434f6e13ec1c1` |
| octopool_0.7.2_windows_arm64.zip | `dca0d3973949511b71766f9f1a994dd46f3dd1c6ca2ac19f5699afa7c7284de3` |

Both Workers serve this release at 100%; pool health is 3/3. The published CLI passed real production reads demonstrating reuse across omitted/explicit default jobs filters and omitted/explicit default API versions, plus a forced-fresh exact run, a second run-list page and the native `--include` positive-page entrypoint. These bounded functional checks do not establish fleet performance or GitHub quota savings.

The isolated compiled CLI → Worker network gate also passed against real anonymous public GitHub. No database migration, re-login, cache purge or cache lifetime change was required.

The release body matches this finalized changelog:

## 0.7.2 - 2026-09-23

### Fixes

- Allow positive `page` query fields on workflow-run reads, including native `--include` calls, while preserving pagination validation, freshness headers, and string protection.
- Share cached workflow jobs and commit check runs between omitted filters and explicit `filter=latest`, preserving all-execution reads, pagination, identity eligibility and explicit freshness.
- Reuse cached responses across omitted and explicit default GitHub API versions, and serve active workflow filenames from complete cached catalogues while preserving source expiry, explicit freshness, identity eligibility and public visibility.
- Explain when JSON field bundles require native gh and when `--include` selects caller credentials, preserving routing, freshness, protection checks, and native output.

### Upgrade notes

- Upgrade the CLI and deploy both Workers for the pagination repair, routing explanations, and cache reuse improvements. No database migration, re-login, cache purge, or cache lifetime change is required.

## Storage Policy

This directory stores release summaries and evidence manifests only. Raw logs, provider payloads, channel transcripts, signing material, and secret-bearing config stay out of git.

