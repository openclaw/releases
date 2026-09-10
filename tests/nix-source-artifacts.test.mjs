import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const checker = fileURLToPath(
  new URL("../scripts/nix-source-qualification/artifacts.mjs", import.meta.url),
);
const contentsOwner = fileURLToPath(
  new URL("../scripts/nix-source-qualification/check-contents.sh", import.meta.url),
);
const sha = "1391f7cd2d40ab5bbcf2f5f831d3a64f520e72d7";

for (const [label, change, accepted] of [
  ["complete output with unknown source provenance", () => {}, true],
  [
    "intentional UI inventory exclusions",
    (root) => {
      fs.writeFileSync(path.join(root, "dist/control-ui/assets/app.js.map"), "diagnostic\n");
      fs.writeFileSync(path.join(root, "dist/control-ui/favicon.ico"), "public root asset\n");
    },
    true,
  ],
  [
    "selected embedded commit",
    (root) => json(root, "dist/build-info.json", { version: "2026.9.3", commit: sha }),
    true,
  ],
  ["missing root launcher", (root) => fs.unlinkSync(path.join(root, "openclaw.mjs")), false],
  [
    "missing launcher dependency",
    (root) => fs.unlinkSync(path.join(root, "node-version.mjs")),
    false,
  ],
  [
    "missing declarations",
    (root) => fs.unlinkSync(path.join(root, "dist/plugin-sdk/core.d.ts")),
    false,
  ],
  [
    "removed SDK export and declaration",
    (root) => {
      const manifest = JSON.parse(fs.readFileSync(path.join(root, "package.json")));
      delete manifest.exports["./plugin-sdk/core"];
      json(root, "package.json", manifest);
      fs.unlinkSync(path.join(root, "dist/plugin-sdk/core.d.ts"));
    },
    false,
  ],
  [
    "changed CLI bin declaration",
    (root) => {
      const manifest = JSON.parse(fs.readFileSync(path.join(root, "package.json")));
      manifest.bin.openclaw = "dist/index.js";
      json(root, "package.json", manifest);
    },
    false,
  ],
  [
    "wrong embedded recipe commit",
    (root) =>
      json(root, "dist/build-info.json", {
        version: "2026.9.3",
        commit: "4bd0453c7a324bb3d8bfd772d1d495c4729aa58a",
      }),
    false,
  ],
  [
    "corrupt UI asset",
    (root) => fs.appendFileSync(path.join(root, "dist/control-ui/assets/app.js"), "corrupt"),
    false,
  ],
  [
    "unlisted UI lazy chunk",
    (root) => fs.writeFileSync(path.join(root, "dist/control-ui/assets/lazy.js"), "chunk\n"),
    false,
  ],
  [
    "unlisted UI compressed sidecar",
    (root) => fs.writeFileSync(path.join(root, "dist/control-ui/assets/app.js.br"), "sidecar\n"),
    false,
  ],
  [
    "missing selected public root file",
    (root) => fs.unlinkSync(path.join(root, "dist/control-ui/favicon.ico")),
    false,
  ],
  [
    "missing selected nested public file",
    (root) => fs.unlinkSync(path.join(root, "dist/control-ui/fonts/demo.woff2")),
    false,
  ],
  [
    "excluded public source map",
    (root) => fs.writeFileSync(path.join(root, "ui/public/sw.js.map"), "diagnostic\n"),
    true,
  ],
  [
    "dangling pruned dependency",
    (root) => fs.symlinkSync("missing", path.join(root, "node_modules/broken")),
    false,
  ],
]) {
  test(label, () => {
    const root = fs.realpathSync(fs.mkdtempSync(path.join(os.tmpdir(), "source-artifacts-")));
    try {
      fixture(root);
      const sourceManifest = path.join(root, "selected-package.json");
      fs.copyFileSync(path.join(root, "package.json"), sourceManifest);
      change(root);
      const out = path.join(root, "checked");
      const result = spawnSync("bash", [contentsOwner], {
        encoding: "utf8",
        env: {
          ...process.env,
          NODE_BIN: process.execPath,
          CONTENTS_CHECK: checker,
          GATEWAY_ROOT: root,
          SOURCE_COMMIT: sha,
          SOURCE_MANIFEST: sourceManifest,
          out,
        },
      });
      assert.equal(result.status === 0, accepted, result.stderr);
      assert.equal(fs.existsSync(out), accepted);
      if (accepted)
        assert.deepEqual(Object.keys(JSON.parse(result.stdout)), [
          "exports",
          "uiAssets",
          "embeddedCommit",
        ]);
    } finally {
      fs.rmSync(root, { recursive: true, force: true });
    }
  });
}

function json(root, file, value) {
  fs.writeFileSync(path.join(root, file), JSON.stringify(value));
}

function fixture(root) {
  for (const directory of [
    "dist/plugin-sdk",
    "dist/control-ui/assets",
    "dist/control-ui/fonts",
    "ui/public/fonts",
    "node_modules",
    "dist-runtime",
  ])
    fs.mkdirSync(path.join(root, directory), { recursive: true });
  for (const file of [
    "openclaw.mjs",
    "node-version.mjs",
    "dist/index.js",
    "dist/plugin-sdk/core.d.ts",
    "dist/control-ui/index.html",
    "dist/control-ui/sw.js",
  ])
    fs.writeFileSync(path.join(root, file), "fixture\n");
  // Vite transforms these public files; only their output existence is source-bound.
  for (const file of [
    "sw.js",
    "manifest.webmanifest",
    "fonts/demo.css",
    "favicon.ico",
    "fonts/demo.woff2",
  ]) {
    fs.writeFileSync(path.join(root, "ui/public", file), "selected public input\n");
    fs.writeFileSync(path.join(root, "dist/control-ui", file), "postbuild public output\n");
  }
  json(root, "package.json", {
    name: "openclaw",
    version: "2026.9.3",
    bin: { openclaw: "openclaw.mjs" },
    exports: {
      "./cli-entry": "./openclaw.mjs",
      "./plugin-sdk/core": { types: "./dist/plugin-sdk/core.d.ts" },
    },
  });
  json(root, "dist/build-info.json", { version: "2026.9.3", commit: null });
  const bytes = Buffer.from("fixture script\n");
  const entry = {
    path: "assets/app.js",
    sha256: createHash("sha256").update(bytes).digest("hex"),
    size: bytes.length,
  };
  fs.writeFileSync(path.join(root, "dist/control-ui/assets/app.js"), bytes);
  json(root, "dist/control-ui/asset-manifest.json", {
    version: 1,
    assets: [entry],
    generation: createHash("sha256")
      .update(`${entry.path}\0${entry.size}\0${entry.sha256}\n`)
      .digest("hex"),
  });
}
