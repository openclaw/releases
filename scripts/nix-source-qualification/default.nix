{
  system,
  sourcePath,
  depsHash,
}:

let
  identity = builtins.fromJSON (builtins.readFile ./hashes.json);
  packaging = builtins.getFlake "github:openclaw/nix-openclaw/${identity.packagingCommit}";
  pkgs = import packaging.inputs.nixpkgs {
    inherit system;
    overlays = [ packaging.overlays.default ];
  };
  inherit (pkgs) lib;
  darwin = system == "aarch64-darwin";
  username = if darwin then "runner" else "qualification";
  homeDirectory =
    if darwin then "/tmp/openclaw-source-qualification" else "/home/qualification/fixture";
  source = builtins.path {
    path = sourcePath;
    name = "openclaw-selected-source";
  };
  manifest = builtins.fromJSON (builtins.readFile "${source}/package.json");
  plugin = pkgs.runCommand "openclaw-nix-qualification-plugin" {
    NODE_BIN = "${pkgs.nodejs_24}/bin/node";
    SOURCE_ROOT = source;
  } "${pkgs.bash}/bin/bash ${./write-plugin.sh}";
  home = packaging.inputs.home-manager.lib.homeManagerConfiguration {
    inherit pkgs;
    modules = [
      packaging.homeManagerModules.openclaw
      {
        home = {
          inherit username homeDirectory;
          stateVersion = "23.11";
        };
        programs.openclaw = {
          enable = true;
          installApp = false;
          instances.qualification = {
            gatewayPath = toString source;
            gatewayPnpmDepsHash = depsHash;
            stateDir = "${homeDirectory}/.openclaw-qualification";
            configPath = "${homeDirectory}/.openclaw-qualification/openclaw.json";
            workspaceDir = "${homeDirectory}/.openclaw-qualification/workspace";
            gatewayPort = 18997;
            logPath = "${homeDirectory}/gateway.log";
            appDefaults.enable = false;
            launchd.label = "org.openclaw.nix.source-qualification";
            systemd.unitName = "openclaw-source-qualification";
            config = {
              logging.file = "${homeDirectory}/gateway-runtime.log";
              gateway = {
                mode = "local";
                bind = "loopback";
                auth.token = "qualification-fixture-only";
              };
              plugins = {
                allow = [ "nix-qualification" ];
                load.paths = [ (toString plugin) ];
                entries.nix-qualification.enabled = true;
                slots.memory = "none";
              };
            };
          };
        };
      }
    ];
  };
  # Consume the module's actual package, not a separately constructed source build.
  gateway = builtins.head home.config.home.packages;
  activation =
    assert !home.config.submoduleSupport.externalPackageInstall;
    home.activationPackage;
  defaultNpm = pkgs.openclaw-gateway;
  lazyNpm = defaultNpm.override {
    sourceInfo = (import "${packaging}/nix/sources/openclaw-source.nix") // {
      hash = throw "default npm evaluation forced the source fetch";
      pnpmMajor = throw "default npm evaluation forced the source package manager";
    };
  };
  metadata =
    assert manifest.name == "openclaw" && manifest.version == "2026.9.3";
    assert builtins.match "pnpm@12\\.3\\.4(\\+.*)?" manifest.packageManager != null;
    assert !(builtins.pathExists "${source}/.git");
    assert pkgs.nodejs_24.version == "24.19.0";
    assert gateway.version == manifest.version && gateway.pnpmMajor == "12";
    assert gateway.selectedPnpm.version == "12.3.4";
    assert gateway.pinnedRev == null && !(gateway.sourceInfo ? rev);
    assert gateway.sourceInfo.applyNixStorePluginOwnershipPatch;
    assert toString gateway.sourceInfo.nixStorePluginOwnershipPatch
      == "${packaging}/nix/patches/allow-nix-store-plugin-ownership-cached.patch";
    assert lazyNpm.drvPath == defaultNpm.drvPath;
    assert (import "${packaging}/nix/tests/source-override/metadata.nix" { inherit lib; }) == "ok";
    {
      inherit (identity) packagingCommit sourceCommit;
      inherit system;
      version = gateway.version;
      pnpm = gateway.selectedPnpm.version;
      node = pkgs.nodejs_24.version;
      pinnedRev = gateway.pinnedRev;
      defaultNpmLazy = true;
    };
  evidence = builtins.deepSeq metadata {
    inherit metadata homeDirectory username;
    gateway = gateway.outPath;
    activation = activation.outPath;
    plugin = plugin.outPath;
    node = "${pkgs.nodejs_24}/bin/node";
    pnpm = "${gateway.selectedPnpm}/bin/pnpm";
    homeManager = "${packaging.inputs.home-manager.packages.${system}.home-manager}/bin/home-manager";
    sourceManifest = "${source}/package.json";
  };
  inputs = pkgs.writeText "source-qualification-inputs.json" (builtins.toJSON evidence);
in
assert builtins.elem system [ "x86_64-linux" "aarch64-darwin" ];
{
  inherit metadata evidence activation inputs;
  dependencies = builtins.deepSeq metadata gateway.pnpmDeps;
  dependencyDrv = gateway.pnpmDeps.drvPath;
  cacheConfig = (import "${packaging}/flake.nix").nixConfig;
  loggingFixture = pkgs.stdenvNoCC.mkDerivation {
    name = "nix-source-logging-fixture";
    phases = [ "buildPhase" ];
    buildPhase = "${pkgs.bash}/bin/bash ${./logging-fixture.sh}";
    outputHashMode = "flat";
    outputHashAlgo = "sha256";
    outputHash = lib.fakeHash;
    preferLocalBuild = true;
    allowSubstitutes = false;
  };
  contents = pkgs.runCommand "openclaw-source-contents" {
    NODE_BIN = "${pkgs.nodejs_24}/bin/node";
    GATEWAY_ROOT = "${gateway}/lib/openclaw";
    SOURCE_COMMIT = identity.sourceCommit;
    SOURCE_MANIFEST = "${source}/package.json";
    CONTENTS_CHECK = ./artifacts.mjs;
  } "${pkgs.bash}/bin/bash ${./check-contents.sh}";
  ownership = pkgs.runCommand "openclaw-source-ownership" {
    NODE_BIN = "${pkgs.nodejs_24}/bin/node";
    GATEWAY_ROOT = "${gateway}/lib/openclaw";
    SOURCE_ROOT = source;
    PATCH_BIN = "${pkgs.gnupatch}/bin/patch";
    OWNERSHIP_PATCH = gateway.sourceInfo.nixStorePluginOwnershipPatch;
    OWNERSHIP_TEST = "${packaging}/nix/tests/source-override/ownership.mjs";
    DEPENDENCIES_CHECK = ./ownership-dependencies.mjs;
  } "${pkgs.bash}/bin/bash ${./check-ownership.sh}";
  linux = pkgs.testers.nixosTest {
    name = "openclaw-source-qualification";
    nodes.machine = {
      users.users.qualification = {
        isNormalUser = true;
        uid = 1000;
        home = homeDirectory;
        createHome = false;
      };
      systemd.tmpfiles.rules = [ "d /home/qualification 0700 qualification users -" ];
      # Standalone HM owns the isolated profile; do not import the NixOS HM module.
      virtualisation.writableStore = true;
      virtualisation.memorySize = 4096;
      environment.systemPackages = [ pkgs.python3 ];
      environment.etc = {
        "source-qualification/inputs.json".source = inputs;
        "source-qualification/probe".source = ./.;
      };
    };
    testScript = builtins.readFile ./linux.py;
  };
}
