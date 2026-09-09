{ originalZip }:
let
  baseline = builtins.getFlake "github:openclaw/nix-openclaw/5f849be411261d4b5d4e06ca0becc4d23526ffda";
  lock = builtins.fromJSON (builtins.readFile "${baseline.outPath}/flake.lock");
  pkgs = import baseline.inputs.nixpkgs { system = "aarch64-darwin"; };
  original = baseline.packages.aarch64-darwin.openclaw-app.src;
  expectedHash = "sha256-9/r9AfggsxtVfaJB0/7g4Q3xz24nundH0w6t4DKivhU=";
  zip = builtins.path {
    path = builtins.toPath originalZip;
    name = "OpenClaw-2026.7.1.zip";
  };
  nativeFetchzip = pkgs.fetchzip.override {
    fetchurl = pkgs.fetchurl.override { hashedMirrors = [ ]; };
  };
  transported = (pkgs.callPackage "${baseline.outPath}/nix/packages/openclaw-app.nix" {
    fetchzip = args: nativeFetchzip (args // {
      url = "file://${zip}";
      name = original.name;
    });
  }).src;
  # No hashed-mirror output may bypass the original native postFetch normalizer,
  # including mirrors supplied by the daemon rather than the client environment.
  recoveredSrc = transported.overrideAttrs (old: {
    allowSubstitutes = false;
    impureEnvVars = builtins.filter (name: name != "NIX_HASHED_MIRRORS") old.impureEnvVars;
  });
in
assert lock.nodes.root.inputs.nixpkgs == "nixpkgs_2";
assert lock.nodes.nixpkgs_2.locked.rev == "e7a3ca8092b61ff85b6a45bf863ea2b2d6a661b3";
assert baseline.inputs.nixpkgs.rev == lock.nodes.nixpkgs_2.locked.rev;
assert original.hash == expectedHash && original.outputHash == expectedHash;
assert original.stripRoot == false && original.outputHashMode == "recursive";
assert recoveredSrc.hash == original.hash && recoveredSrc.outputHash == original.outputHash;
assert recoveredSrc.stripRoot == original.stripRoot;
assert recoveredSrc.outputHashMode == original.outputHashMode;
assert recoveredSrc.name == original.name && recoveredSrc.outPath == original.outPath;
assert recoveredSrc.system == "aarch64-darwin";
assert recoveredSrc.allowSubstitutes == false;
assert !(builtins.elem "NIX_HASHED_MIRRORS" recoveredSrc.impureEnvVars);
assert recoveredSrc.postFetch == transported.postFetch;
{
  inherit recoveredSrc;
  identity = {
    baseline = baseline.rev;
    nixpkgs = baseline.inputs.nixpkgs.rev;
    originalOutPath = original.outPath;
    recoveredOutPath = recoveredSrc.outPath;
    inherit (recoveredSrc) drvPath name system outputHash outputHashMode stripRoot allowSubstitutes;
    transport = "file://${zip}";
    normalizerUnchanged = recoveredSrc.postFetch == transported.postFetch;
    daemonHashedMirrorsAllowed = builtins.elem "NIX_HASHED_MIRRORS" recoveredSrc.impureEnvVars;
  };
}
