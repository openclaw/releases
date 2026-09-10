import assert from "node:assert/strict";
import fs from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";

const require = createRequire(path.join(process.cwd(), "package.json"));
assert.equal(process.version, "v24.19.0");
for (const [name, version] of [
  ["acorn", "8.18.0"],
  ["@openclaw/fs-safe", "0.8.5"],
]) {
  const manifest = JSON.parse(fs.readFileSync(`node_modules/${name}/package.json`));
  assert.equal(manifest.version, version);
  const entry = name === "@openclaw/fs-safe" ? `${name}/path` : name;
  assert.ok(fs.realpathSync(require.resolve(entry)).startsWith(`${process.env.GATEWAY_ROOT}/`));
}
