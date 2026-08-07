#!/usr/bin/env node
import { spawnSync } from "node:child_process";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import {
  fullValidationRunEntries,
  loadFullValidationSource,
} from "./openclaw-release-evidence-contract.mjs";
const OPTIONS = new Map([
  ["--full-validation-run-id", "fullValidationRunId"],
  ["--full-validation-run-attempt", "fullValidationRunAttempt"],
  ["--release-id", "releaseId"],
  ["--release-ref", "releaseRef"],
  ["--package-spec", "packageSpec"],
  ["--notes-file", "notesFile"],
  ["--output-root", "outputRoot"],
]);
function parseArgs(argv) {
  const args = { outputRoot: "evidence" };
  for (let index = 0; index < argv.length; index += 1) {
    if (argv[index] === "--help" || argv[index] === "-h") {
      console.log(
        "Usage: openclaw-release-evidence-from-full-validation.mjs --full-validation-run-id <id> [--full-validation-run-attempt <attempt>] --release-id <version> --release-ref <ref> --package-spec <spec> [--notes-file <file>] [--output-root <dir>]",
      );
      process.exit(0);
    }
    const key = OPTIONS.get(argv[index]);
    if (!key || !argv[index + 1]) {
      throw new Error(`Invalid argument: ${argv[index]}`);
    }
    args[key] = argv[++index];
  }
  if (!/^[1-9][0-9]*$/u.test(args.fullValidationRunId ?? "")) {
    throw new Error("--full-validation-run-id must be numeric");
  }
  if (
    args.fullValidationRunAttempt !== undefined &&
    !/^[1-9][0-9]*$/u.test(args.fullValidationRunAttempt)
  ) {
    throw new Error("--full-validation-run-attempt must be a positive integer");
  }
  return args;
}
async function main() {
  const args = parseArgs(process.argv.slice(2));
  const source = await loadFullValidationSource(args);
  const dir = await fs.mkdtemp(path.join(os.tmpdir(), "openclaw-release-evidence-"));
  const runsFile = path.join(dir, "runs.txt");
  const sourceFile = path.join(dir, "full-validation-source.json");
  const notesFile = args.notesFile || path.join(dir, "notes.md");
  await fs.writeFile(
    runsFile,
    `${fullValidationRunEntries(source)
      .map((entry) =>
        `${entry.label} ${entry.repo} ${entry.runId} ${entry.blocking ? "blocking" : "advisory"}`,
      )
      .join("\n")}\n`,
  );
  await fs.writeFile(sourceFile, `${JSON.stringify(source, null, 2)}\n`);
  if (!args.notesFile) {
    const reuse = source.manifest.evidenceReuse;
    await fs.writeFile(
      notesFile,
      `Automatically ingested from Full Release Validation ${source.parentRun.runId}, attempt ${source.parentRun.runAttempt}.${
        reuse ? ` Reused ${reuse.policy} evidence from run ${reuse.runId}.` : ""
      }\n`,
    );
  }
  const result = spawnSync(
    process.execPath,
    [
      "scripts/openclaw-release-evidence.mjs",
      "--release-id", args.releaseId,
      "--release-ref", args.releaseRef,
      "--package-spec", args.packageSpec,
      "--runs-file", runsFile,
      "--notes-file", notesFile,
      "--full-validation-source-file", sourceFile,
      "--output-root", args.outputRoot,
    ],
    { stdio: "inherit", env: process.env },
  );
  if (result.status !== 0) {
    process.exit(result.status ?? 1);
  }
}
main().catch((error) => {
  console.error(error instanceof Error ? error.message : error);
  process.exit(1);
});
