import { execFileSync } from "node:child_process";
import { readdirSync, readFileSync } from "node:fs";
import { resolve } from "node:path";
import { pathToFileURL } from "node:url";

function parseVersion(version) {
  const match =
    typeof version === "string" &&
    version.match(
      /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$/,
    );
  if (!match) throw new Error(`Invalid npm version: ${JSON.stringify(version)}`);
  const prerelease = match[4]?.split(".") ?? [];
  if (prerelease.some((part) => /^0\d+$/.test(part))) {
    throw new Error(`Invalid npm prerelease: ${version}`);
  }
  return { core: match.slice(1, 4).map(BigInt), prerelease };
}

function compareVersions(left, right) {
  const a = parseVersion(left);
  const b = parseVersion(right);
  for (let i = 0; i < 3; i++) {
    if (a.core[i] !== b.core[i]) return a.core[i] < b.core[i] ? -1 : 1;
  }
  if (a.prerelease.length === 0 || b.prerelease.length === 0) {
    return a.prerelease.length === b.prerelease.length ? 0 : a.prerelease.length === 0 ? 1 : -1;
  }
  for (let i = 0; i < Math.max(a.prerelease.length, b.prerelease.length); i++) {
    const x = a.prerelease[i];
    const y = b.prerelease[i];
    if (x === y) continue;
    if (x === undefined || y === undefined) return x === undefined ? -1 : 1;
    const xn = /^\d+$/.test(x);
    const yn = /^\d+$/.test(y);
    if (xn !== yn) return xn ? -1 : 1;
    return (xn ? BigInt(x) < BigInt(y) : x < y) ? -1 : 1;
  }
  return 0;
}

export function betaFloorTarget(tags) {
  if (!tags || typeof tags !== "object" || Array.isArray(tags)) {
    throw new Error("npm dist-tags must be an object.");
  }
  if (tags.latest === undefined) return undefined;
  // Never propagate an extended-stable train into either regular channel,
  // including plugin selectors and a latest value changed after workflow admission.
  for (const channel of ["latest", "beta"]) {
    if (tags[channel] !== undefined && parseVersion(tags[channel]).core[2] >= 33n) {
      throw new Error(`npm ${channel} must use a release with patch below 33.`);
    }
  }
  return tags.beta === undefined || compareVersions(tags.beta, tags.latest) < 0
    ? tags.latest
    : undefined;
}

function npm(args) {
  return execFileSync("npm", args, {
    encoding: "utf8",
    stdio: ["ignore", "pipe", "pipe"],
    timeout: 120_000,
    maxBuffer: 1024 * 1024,
  }).trim();
}

function readTags(packageName) {
  let raw;
  try {
    raw = npm(["view", packageName, "dist-tags", "--json", "--prefer-online"]);
  } catch (error) {
    if (typeof error.stdout === "string") {
      let result;
      try {
        result = JSON.parse(error.stdout);
      } catch {
        /* Report the npm failure below. */
      }
      if (result?.error?.code === "E404" && packageName !== "openclaw") return undefined;
    }
    throw error;
  }
  const parsed = JSON.parse(raw);
  // npm 12 wraps single-package `view --json` output in a one-element array.
  return Array.isArray(parsed) && parsed.length === 1 ? parsed[0] : parsed;
}

const READBACK_ATTEMPTS = 10;
const READBACK_DELAY_MS = 3_000;

// A successful dist-tag mutation can lag the registry's read path by several
// seconds (observed live on 2026-09-10), so verify convergence within a bounded window.
async function readConvergedTags(packageName) {
  for (let attempt = 1; ; attempt++) {
    const tags = readTags(packageName);
    if (tags?.latest !== undefined && betaFloorTarget(tags) === undefined) return tags;
    if (attempt === READBACK_ATTEMPTS)
      throw new Error("beta floor did not converge after mutation.");
    await new Promise((resolve) => setTimeout(resolve, READBACK_DELAY_MS));
  }
}

function readJson(path, { optional = false } = {}) {
  try {
    return JSON.parse(readFileSync(path, "utf8"));
  } catch (error) {
    if (optional && error.code === "ENOENT") return undefined;
    throw error;
  }
}

// openclaw/openclaw owns its core npm package inventory; apply the same inclusion
// rule its release planner uses so every published core package is floored.
function corePackageNames(sourceDir) {
  const root = readJson(resolve(sourceDir, "package.json"));
  const policy = readJson(resolve(sourceDir, "scripts/lib/npm-core-release-packages.json"));
  if (!Array.isArray(policy) || policy.length === 0) {
    throw new Error("Invalid core npm package policy.");
  }
  return policy.flatMap((entry) => {
    if (
      typeof entry?.path !== "string" ||
      !/^packages\/[a-z0-9-]+$/.test(entry.path) ||
      typeof entry.name !== "string" ||
      !/^@openclaw\/[a-z0-9-]+$/.test(entry.name)
    ) {
      throw new Error("Invalid core npm package policy.");
    }
    if (entry.dependency !== undefined) {
      if (typeof root.dependencies?.[entry.dependency] !== "string") return [];
    } else {
      const pkg = readJson(resolve(sourceDir, entry.path, "package.json"), { optional: true });
      if (pkg?.openclaw?.release?.publishToNpm !== true) return [];
    }
    return [entry.name];
  });
}

function packageNames(sourceDir) {
  const packages = new Set(["openclaw", ...corePackageNames(sourceDir)]);
  const extensions = resolve(sourceDir, "extensions");
  // Read source manifests as data; never execute source code with the npm token.
  for (const entry of readdirSync(extensions, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    const pkg = readJson(resolve(extensions, entry.name, "package.json"), { optional: true });
    if (pkg === undefined) continue;
    if (pkg.openclaw?.release?.publishToNpm !== true || pkg.openclaw?.build?.bundledDist === true)
      continue;
    if (
      pkg.private === true ||
      typeof pkg.name !== "string" ||
      !/^@openclaw\/[a-z0-9][a-z0-9._-]*$/.test(pkg.name)
    ) {
      throw new Error(`Invalid publishable plugin manifest: ${entry.name}`);
    }
    packages.add(pkg.name);
  }
  return [...packages].sort();
}

async function main() {
  if (process.argv.length !== 3)
    throw new Error("Usage: node scripts/release-npm-beta-floor.mjs <source-dir>");
  const failures = [];
  for (const packageName of packageNames(process.argv[2])) {
    try {
      const tags = readTags(packageName);
      if (tags === undefined || tags.latest === undefined) {
        if (packageName === "openclaw") throw new Error("npm latest is missing.");
        console.log(`${packageName}: no published latest; skipped`);
        continue;
      }
      const target = betaFloorTarget(tags);
      if (target === undefined) {
        console.log(`${packageName}: beta=${tags.beta} >= latest=${tags.latest}; unchanged`);
        continue;
      }
      npm(["dist-tag", "add", `${packageName}@${target}`, "beta"]);
      await readConvergedTags(packageName);
      console.log(`${packageName}: beta ${tags.beta ?? "<missing>"} -> ${target}`);
    } catch (error) {
      failures.push(`${packageName}: ${error.message}`);
    }
  }
  if (failures.length > 0) throw new Error(failures.join("\n"));
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  main().catch((error) => {
    console.error(error.message);
    process.exitCode = 1;
  });
}
