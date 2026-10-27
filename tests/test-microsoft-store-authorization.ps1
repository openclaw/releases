Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
Import-Module (Join-Path $PSScriptRoot '../scripts/MicrosoftStore.psm1') -Force
$root = Join-Path ([IO.Path]::GetTempPath()) "store-authority-$([guid]::NewGuid().ToString('N'))"
$passed = 0

function Assert-Fails([scriptblock]$Action, [string]$Pattern) {
    try { & $Action | Out-Null } catch {
        if ($_.Exception.Message -notmatch $Pattern) { throw "Unexpected failure: $($_.Exception.Message)" }
        return
    }
    throw "Expected rejection matching: $Pattern"
}

function Test-Case([string]$Name, [scriptblock]$Action) {
    try { & $Action; $script:passed++ } catch { throw "${Name}: $($_.Exception.Message)" }
}

function Write-Bundle($Fixture, [string]$Identity = '', [switch]$Signed, [string]$Version = '2026.10.6.0') {
    if (Test-Path $Fixture.bundle) { Remove-Item -LiteralPath $Fixture.bundle }
    $config = Get-MicrosoftStoreProduct $Fixture.product
    if (-not $Identity) { $Identity = $config.identityName }
    $archive = [IO.Compression.ZipFile]::Open($Fixture.bundle, [IO.Compression.ZipArchiveMode]::Create)
    try {
        $entry = $archive.CreateEntry('AppxMetadata/AppxBundleManifest.xml')
        $writer = [IO.StreamWriter]::new($entry.Open())
        try { $writer.Write("<Bundle><Identity Name='$Identity' Publisher='$($config.publisher)' Version='$Version'/></Bundle>") } finally { $writer.Dispose() }
        if ($Signed) { [void]$archive.CreateEntry('AppxSignature.p7x') }
    } finally { $archive.Dispose() }
}

function New-Fixture([string]$Product, [switch]$Promotion) {
    $config = Get-MicrosoftStoreProduct $Product
    $directory = Join-Path $root ([guid]::NewGuid().ToString('N'))
    [void][IO.Directory]::CreateDirectory($directory)
    $gateway = $Product -ceq 'gateway'
    $sha = 'a' * 40
    $pipeline = 'b' * 40
    $run = [pscustomobject]@{
        id = 41; run_attempt = 1; status = 'completed'; conclusion = 'success'
        repository = [pscustomobject]@{ full_name = $config.repository }
        head_repository = [pscustomobject]@{ full_name = $config.repository }
        path = if ($gateway) { '.github/workflows/gateway-msix.yml' } elseif ($Promotion) { '.github/workflows/promote-alpha-release.yml' } else { '.github/workflows/ci.yml' }
        event = if ($gateway -or $Promotion) { 'workflow_dispatch' } else { 'push' }
        head_branch = if ($gateway -or $Promotion) { 'main' } else { 'v2026.10.6' }
        head_sha = if ($gateway -or $Promotion) { $pipeline } else { $sha }
    }
    $source = if ($gateway) {
        [pscustomobject]@{
            repository = 'https://github.com/openclaw/openclaw'; packageVersion = '2026.10.6'; resolvedCommit = $sha
            workflowRunId = '41'; packagingCommit = $pipeline
            workflowRef = 'openclaw/openclaw-windows-packaging/.github/workflows/gateway-msix.yml@refs/heads/main'
            githubRef = 'refs/heads/main'; eventName = 'workflow_dispatch'; signingMode = 'store'
            releaseIdentitySource = [pscustomobject]@{
                repository = 'https://github.com/openclaw/openclaw'; channel = 'stable'
                releaseTag = 'v2026.10.6'; packageVersion = '2026.10.6'; resolvedCommit = $sha
            }
        }
    } else { [pscustomobject]@{ runId = '41'; runAttempt = 1; releaseTag = 'v2026.10.6'; sourceSha = $sha; bundleSha256 = '' } }
    $fixture = [pscustomobject]@{
        product = $Product; directory = $directory; run = $run; source = $source; tagCommit = $sha; draft = $false
        bundle = Join-Path $directory $(if ($gateway) { 'OpenClawGateway-2026.10.6-msix.0-store.msixbundle' } else { 'OpenClaw.msixbundle' })
        artifacts = @(
            [pscustomobject]@{ id = 51; name = $config.artifactName; expired = $false },
            [pscustomobject]@{ id = 52; name = $(if ($gateway) { 'openclaw-source-resolution' } else { 'store-release-source-1' }); expired = $false }
        )
        environment = [pscustomobject]@{
            can_admins_bypass = $false
            protection_rules = @([pscustomobject]@{ type = 'required_reviewers'; reviewers = @([pscustomobject]@{ type = 'Team'; reviewer = [pscustomobject]@{ id = 16590423 } }) })
            deployment_branch_policy = [pscustomobject]@{ custom_branch_policies = $true; protected_branches = $false }
        }
        branches = @([pscustomobject]@{ name = 'main'; type = 'branch' })
    }
    Write-Bundle $fixture
    if (-not $gateway) { $source.bundleSha256 = (Get-FileHash $fixture.bundle -Algorithm SHA256).Hash.ToLowerInvariant() }
    $state = $fixture
    $fixture | Add-Member api ({
        param($Repository, $Path)
        if ($Path -like '*/deployment-branch-policies') { return [pscustomobject]@{ total_count = $state.branches.Count; branch_policies = $state.branches } }
        if ($Path -like 'environments/*') { return $state.environment }
        if ($Path -eq 'actions/runs/41') { return $state.run }
        if ($Path -like 'actions/runs/41/artifacts?*') { return [pscustomobject]@{ total_count = $state.artifacts.Count; artifacts = $state.artifacts } }
        if ($Path -like 'releases/tags/*') { return [pscustomobject]@{ tag_name = $Path.Substring('releases/tags/'.Length); draft = $state.draft; prerelease = $false } }
        if ($Path -like 'git/ref/tags/*') { return [pscustomobject]@{ object = [pscustomobject]@{ type = 'tag'; sha = 'c' * 40 } } }
        if ($Path -like 'git/tags/*') { return [pscustomobject]@{ tag = 'v2026.10.6'; object = [pscustomobject]@{ type = 'commit'; sha = $state.tagCommit }; verification = [pscustomobject]@{ verified = $true } } }
        if ($Path -like 'commits/*') { return [pscustomobject]@{ sha = $state.tagCommit } }
        throw "Unexpected external API request: $Repository/$Path"
    }.GetNewClosure())
    $fixture | Add-Member download ({
        param($Repository, $Id, $Name, $Destination)
        $filename = if ($state.product -ceq 'gateway') { 'source-resolution.json' } else { 'store-source.json' }
        [IO.File]::WriteAllText((Join-Path $Destination $filename), ($state.source | ConvertTo-Json -Depth 20))
    }.GetNewClosure())
    $fixture
}

function Get-Source($Fixture) {
    Get-AuthorizedStoreSource -Product $Fixture.product -RunId 41 -Directory (Join-Path $Fixture.directory 'provenance') -ApiInvoker $Fixture.api -DownloadInvoker $Fixture.download
}

try {
    Test-Case 'Noncanonical product casing is rejected' {
        Assert-Fails { Get-MicrosoftStoreProduct 'GATEWAY' } 'ValidateSet|not belong|validation'
    }
    foreach ($product in @('gateway', 'companion')) {
        Test-Case "$product allowed exact source and bytes" {
            $fixture = New-Fixture $product
            Assert-MicrosoftStoreEnvironment -Product $product -ApiInvoker $fixture.api
            $source = Get-Source $fixture
            $approved = Confirm-AuthorizedStoreBundle -Source $source -Directory $fixture.directory
            $fresh = Confirm-AuthorizedStoreBundle -Source (Get-Source $fixture) -Directory $fixture.directory -ApprovedSource $approved
            if ($fresh.bundleSha256 -cne (Get-FileHash $fixture.bundle -Algorithm SHA256).Hash.ToLowerInvariant()) { throw 'Bundle was not hash-bound.' }
        }
        foreach ($scenario in @('foreign repository', 'foreign workflow', 'cancelled run', 'expired bundle', 'missing witness', 'unpublished release', 'moved tag')) {
            Test-Case "$product rejects $scenario" {
                $fixture = New-Fixture $product
                switch ($scenario) {
                    'foreign repository' { $fixture.run.head_repository.full_name = 'foreign/repository' }
                    'foreign workflow' { $fixture.run.path = '.github/workflows/other.yml' }
                    'cancelled run' { $fixture.run.conclusion = 'cancelled' }
                    'expired bundle' { $fixture.artifacts[0].expired = $true }
                    'missing witness' { $fixture.artifacts = @($fixture.artifacts[0]) }
                    'unpublished release' { $fixture.draft = $true }
                    'moved tag' { $fixture.tagCommit = 'd' * 40 }
                }
                Assert-Fails { Get-Source $fixture } 'canonical|workflow|expired|witness|published|tag'
            }
        }
        foreach ($scenario in @('missing reviewers', 'foreign team', 'administrator bypass', 'tag deployment', 'wildcard deployment')) {
            Test-Case "$product rejects $scenario" {
                $fixture = New-Fixture $product
                switch ($scenario) {
                    'missing reviewers' { $fixture.environment.protection_rules = @() }
                    'foreign team' { $fixture.environment.protection_rules[0].reviewers[0].reviewer.id = 1 }
                    'administrator bypass' { $fixture.environment.can_admins_bypass = $true }
                    'tag deployment' { $fixture.branches[0].type = 'tag' }
                    'wildcard deployment' { $fixture.branches[0].name = '*' }
                }
                Assert-Fails { Assert-MicrosoftStoreEnvironment -Product $product -ApiInvoker $fixture.api } 'release-manager|bypass|exact main'
            }
        }
    }
    Test-Case 'Companion promotion preserves its release witness' {
        $fixture = New-Fixture companion -Promotion
        if ((Get-Source $fixture).releaseTag -cne 'v2026.10.6') { throw 'Promotion was not authorized.' }
    }
    Test-Case 'Companion stale attempt is rejected' {
        $fixture = New-Fixture companion
        $fixture.source.runAttempt = 2
        Assert-Fails { Get-Source $fixture } 'attempt'
    }
    Test-Case 'Gateway separately selected identity is checked' {
        $fixture = New-Fixture gateway
        $fixture.source.releaseIdentitySource.channel = 'beta'
        Assert-Fails { Get-Source $fixture } 'stable release identity'
    }
    foreach ($field in @('runAttempt', 'artifactId', 'pipelineSha', 'sourceSha')) {
        Test-Case "Changed $field while awaiting approval is rejected" {
            $fixture = New-Fixture gateway
            $source = Get-Source $fixture
            $approved = Confirm-AuthorizedStoreBundle -Source $source -Directory $fixture.directory
            $source.$field = if ($field -ceq 'runAttempt') { 2 } else { '9' * 40 }
            Assert-Fails { Confirm-AuthorizedStoreBundle -Source $source -Directory $fixture.directory -ApprovedSource $approved } 'changed while awaiting approval'
        }
    }
    Test-Case 'Gateway bytes changed after approval are rejected' {
        $fixture = New-Fixture gateway
        $source = Get-Source $fixture
        $approved = Confirm-AuthorizedStoreBundle -Source $source -Directory $fixture.directory
        Write-Bundle $fixture -Version '2026.10.6.1'
        Assert-Fails { Confirm-AuthorizedStoreBundle -Source $source -Directory $fixture.directory -ApprovedSource $approved } 'changed while awaiting approval'
    }
    Test-Case 'Companion bytes must match its source witness' {
        $fixture = New-Fixture companion
        $source = Get-Source $fixture
        Write-Bundle $fixture -Version '2026.10.6.1'
        Assert-Fails { Confirm-AuthorizedStoreBundle -Source $source -Directory $fixture.directory } 'differs from its release witness'
    }
    foreach ($scenario in @('foreign identity', 'signed bundle', 'invalid version')) {
        Test-Case "Reject $scenario" {
            $fixture = New-Fixture gateway
            $source = Get-Source $fixture
            switch ($scenario) {
                'foreign identity' { Write-Bundle $fixture -Identity 'Foreign.Product' }
                'signed bundle' { Write-Bundle $fixture -Signed }
                'invalid version' { Write-Bundle $fixture -Version '70000.1.1.1' }
            }
            Assert-Fails { Confirm-AuthorizedStoreBundle -Source $source -Directory $fixture.directory } 'foreign|unsigned|bounds'
        }
    }
    Write-Host "$passed Store authorization scenarios passed."
} finally { if (Test-Path $root) { Remove-Item -LiteralPath $root -Recurse -Force } }
