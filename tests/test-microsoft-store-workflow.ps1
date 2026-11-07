[CmdletBinding()]
param()
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$repository = Split-Path $PSScriptRoot -Parent
$workflow = Get-Content (Join-Path $repository '.github/workflows/windows-store-publish.yml') -Raw
$step = [regex]::Match($workflow, '(?ms)^      - name: Submit and commit the approved Store update\r?\n.*?^        run: \|\r?\n(?<script>(?:^ {10}[^\r\n]*\r?\n|^\r?\n)+)')
if (-not $step.Success) { throw 'Unable to locate the Store publisher workflow entry point.' }
$invoke = [scriptblock]::Create([regex]::Replace($step.Groups['script'].Value, '(?m)^ {10}', ''))
$fixture = Join-Path ([IO.Path]::GetTempPath()) "central-store-workflow-$([guid]::NewGuid().ToString('N'))"
$location = Get-Location
$names = @('STORE_PRODUCT', 'APPROVED_SOURCE', 'MSSTORE_APPLICATION_ID', 'MSSTORE_TENANT_ID', 'MSSTORE_CLIENT_ID', 'MSSTORE_ASSERTION_FILE')
$original = @{}
foreach ($name in $names) { $original[$name] = [Environment]::GetEnvironmentVariable($name) }
try {
    [void][IO.Directory]::CreateDirectory((Join-Path $fixture 'scripts'))
    [void][IO.Directory]::CreateDirectory((Join-Path $fixture 'evidence'))
    Copy-Item (Join-Path $repository 'scripts/MicrosoftStore.psm1') (Join-Path $fixture 'scripts/MicrosoftStore.psm1')
    # Run the real workflow argument wiring and product owner. Replace only the
    # external publisher so this proof cannot authenticate or create a draft.
    [IO.File]::WriteAllText((Join-Path $fixture 'scripts/Submit-MicrosoftStore.ps1'), @'
param([string]$Channel, [string]$FlightId, [string]$BundlePath, [string]$PackageIdentityName, [string]$Publisher,
      [string]$ApplicationId, [string]$TenantId, [string]$ClientId, [string]$ClientAssertionFile, [string]$EvidencePath)
[IO.File]::WriteAllText((Join-Path $PWD 'called.json'), (@{
    channel = $Channel; flightId = $FlightId; bundle = [IO.Path]::GetFileName($BundlePath); identity = $PackageIdentityName
} | ConvertTo-Json))
'@)
    Set-Location $fixture
    $env:MSSTORE_APPLICATION_ID = 'fixture'
    $env:MSSTORE_TENANT_ID = '11111111-1111-1111-1111-111111111111'
    $env:MSSTORE_CLIENT_ID = '22222222-2222-2222-2222-222222222222'
    $env:MSSTORE_ASSERTION_FILE = 'fixture.jwt'
    foreach ($case in @(
        @{ product = 'gateway'; channel = 'production'; flightId = ''; bundleName = 'OpenClawGateway-2026.11.1-msix.0-store.msixbundle'; identity = 'OpenClawFoundation.OpenClawGateway' },
        @{ product = 'gateway'; channel = 'development'; flightId = '33333333-3333-3333-3333-333333333333'; bundleName = 'OpenClawGateway-2026.11.1-beta.2-msix.0-store.msixbundle'; identity = 'OpenClawFoundation.OpenClawGateway' },
        @{ product = 'companion'; channel = 'production'; flightId = ''; bundleName = 'OpenClaw.msixbundle'; identity = 'OpenClawFoundation.OpenClaw' }
    )) {
        $env:STORE_PRODUCT = $case.product
        $env:APPROVED_SOURCE = $case | ConvertTo-Json -Compress
        & $invoke
        $called = Get-Content called.json -Raw | ConvertFrom-Json
        foreach ($property in @('channel', 'flightId', 'identity')) {
            if ($called.$property -cne $case.$property) { throw "Workflow changed the approved destination: $property" }
        }
        if ($called.bundle -cne $case.bundleName) { throw 'Workflow changed the approved bundle.' }
        $retained = Get-Content evidence/approved-source.json -Raw | ConvertFrom-Json
        if ($retained.flightId -cne $case.flightId -or $retained.channel -cne $case.channel) {
            throw 'Workflow lost the approved Store destination from its receipt.'
        }
        Remove-Item called.json
    }
    Write-Host 'Store workflow destination handoff: 3 scenarios passed.'
} finally {
    Set-Location $location
    foreach ($name in $names) { [Environment]::SetEnvironmentVariable($name, $original[$name]) }
    Remove-Item $fixture -Recurse -Force -ErrorAction SilentlyContinue
}
