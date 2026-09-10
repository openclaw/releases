import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import fs from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";

const [root, sourceCommit, sourceManifestPath] = process.argv.slice(2);
const readJson = (relative) => JSON.parse(fs.readFileSync(path.join(root, relative), "utf8"));
const requireFile = (relative) => {
  assert.ok(relative.startsWith("./") && !relative.split("/").includes(".."));
  const file = path.join(root, relative);
  assert.ok(fs.statSync(file).isFile(), `missing runtime artifact: ${relative}`);
  assert.ok(fs.statSync(file).size > 0, `empty runtime artifact: ${relative}`);
  return file;
};
const manifest = readJson("package.json");
const selected = JSON.parse(fs.readFileSync(sourceManifestPath, "utf8"));
assert.equal(selected.name, "openclaw");
assert.equal(selected.version, "2026.9.3");
assert.equal(manifest.name, selected.name);
assert.equal(manifest.version, selected.version);
assert.deepEqual(
  manifest.exports,
  selected.exports,
  "installed exports differ from selected source",
);
assert.deepEqual(manifest.bin, selected.bin, "installed CLI bin differs from selected source");
assert.equal(selected.exports["./cli-entry"], "./openclaw.mjs");
for (const file of Object.values(selected.bin)) requireFile(`./${file}`);
for (const file of ["./openclaw.mjs", "./node-version.mjs", "./dist/index.js"]) requireFile(file);
let targets = 0;
const checkExport = (target) => {
  if (typeof target === "string") {
    requireFile(target);
    targets++;
  } else {
    for (const value of Object.values(target)) checkExport(value);
  }
};
checkExport(manifest.exports);
assert.ok(targets > 0);
assert.equal(
  createRequire(path.join(root, "package.json")).resolve("openclaw/cli-entry"),
  path.join(root, "openclaw.mjs"),
);
const buildInfo = readJson("dist/build-info.json");
assert.equal(buildInfo.version, manifest.version);
assert.ok(
  buildInfo.commit === null || buildInfo.commit === sourceCommit,
  "wrong embedded source commit",
);
assert.ok(!Object.hasOwn(manifest, "gitHead") || manifest.gitHead === sourceCommit);
assert.ok(!fs.existsSync(path.join(root, ".git")));

const uiManifest = readJson("dist/control-ui/asset-manifest.json");
assert.equal(uiManifest.version, 1);
assert.ok(uiManifest.assets.length > 0);
// The selected Vite producer inventories assets/ only, excluding source maps.
const assetsRoot = path.join(root, "dist/control-ui/assets");
const inventory = fs
  .readdirSync(assetsRoot, { recursive: true, withFileTypes: true })
  .filter((entry) => !entry.isDirectory() && !entry.name.endsWith(".map"))
  .map((entry) => {
    assert.ok(entry.isFile() && !entry.isSymbolicLink(), "unsafe Control UI asset");
    return `assets/${path.relative(assetsRoot, path.join(entry.parentPath, entry.name))}`;
  });
assert.deepEqual(
  uiManifest.assets.map((entry) => entry.path).sort(),
  inventory.sort(),
  "UI manifest differs from the eligible output inventory",
);
const generation = createHash("sha256");
for (const asset of uiManifest.assets) {
  const bytes = fs.readFileSync(requireFile(`./dist/control-ui/${asset.path}`));
  assert.equal(bytes.length, asset.size);
  assert.equal(createHash("sha256").update(bytes).digest("hex"), asset.sha256);
  generation.update(`${asset.path}\0${asset.size}\0${asset.sha256}\n`);
}
assert.equal(generation.digest("hex"), uiManifest.generation);
requireFile("./dist/control-ui/index.html");
requireFile("./dist/control-ui/sw.js");
for (const directory of ["node_modules", "dist-runtime"]) {
  const base = path.join(root, directory);
  assert.ok(fs.statSync(base).isDirectory());
  for (const entry of fs.readdirSync(base, { recursive: true, withFileTypes: true })) {
    if (entry.isSymbolicLink()) fs.statSync(path.join(entry.parentPath, entry.name));
  }
}
console.log(
  JSON.stringify({
    exports: targets,
    uiAssets: uiManifest.assets.length,
    embeddedCommit: buildInfo.commit,
  }),
);
