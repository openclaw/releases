Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$root = Join-Path ([IO.Path]::GetTempPath()) "store-recovery-$([guid]::NewGuid().ToString('N'))"
[void][IO.Directory]::CreateDirectory($root)
[IO.File]::WriteAllText((Join-Path $root 'assertion'), 'synthetic-assertion')
$old = '33333333-3333-3333-3333-333333333333'
$new = '44444444-4444-4444-4444-444444444444'
$base = 'https://manage.devcenter.microsoft.com/v1.0/my/applications/TESTPRODUCT'
$passed = 0
function Reset-Fixture([string]$Operation, [string]$Scenario) {
    $global:Recovery = @{
        operation = $Operation; scenario = $Scenario; deleted = $false; reads = 0
        calls = [Collections.Generic.List[string]]::new()
    }
}
function Flight([string]$Id) {
    [pscustomobject]@{
        flightId = $Id; friendlyName = 'Development'; groupIds = @('123')
        pendingFlightSubmission = if ($global:Recovery.operation -eq 'discard-draft' -and -not $global:Recovery.deleted) { [pscustomobject]@{ id = '456' } } else { $null }
        lastPublishedFlightSubmission = $null
    }
}
$http = {
    param($Method, $Uri, $Headers, $Body, $ContentType)
    $global:Recovery.calls.Add("$Method $Uri")
    if ($Uri -like 'https://login.microsoftonline.com/*') { return [pscustomobject]@{ access_token = 'synthetic'; expires_in = 3600 } }
    if ($Uri -ceq $base -and $Method -eq 'Get') {
        return [pscustomobject]@{ id = 'TESTPRODUCT'; packageIdentityName = $(if ($global:Recovery.scenario -eq 'foreign-product') { 'foreign' } else { 'OpenClawFoundation.OpenClaw' }); publisherName = 'CN=4BA40A7A-B719-4C40-BF91-84AF4F1136FC' }
    }
    if ($Uri -ceq "$base/listflights?top=100" -and $Method -eq 'Get') {
        $items = @(if ($global:Recovery.operation -ne 'create' -or $global:Recovery.scenario -eq 'existing-flight') { Flight $old })
        if ($global:Recovery.scenario -eq 'same-name') { $items = @(Flight $new) }
        return [pscustomobject]@{ value = $items; totalCount = $(if ($global:Recovery.scenario -eq 'incomplete') { 101 } else { $items.Count }) }
    }
    if ($Method -eq 'Post' -and $Uri -ceq "$base/flights") {
        $request = $Body | ConvertFrom-Json
        if ($request.friendlyName -cne 'Development' -or @($request.groupIds).Count -ne 1 -or $request.groupIds[0] -cne '123') { throw 'Wrong creation target.' }
        if ($global:Recovery.scenario -eq 'lost-create') { throw 'Lost create response.' }
        return Flight $new
    }
    if ($Method -eq 'Get' -and $Uri -in @("$base/flights/$old", "$base/flights/$new")) {
        $global:Recovery.reads++
        if ($global:Recovery.deleted -and $global:Recovery.scenario -eq 'removed-flight') { throw 'Flight missing after deletion.' }
        $result = Flight ($Uri.Split('/')[-1])
        switch ($global:Recovery.scenario) {
            'wrong-group' { $result.groupIds = @('999') }
            'published' { $result.lastPublishedFlightSubmission = [pscustomobject]@{ id = 'published' } }
            'foreign-draft' { $result.pendingFlightSubmission = [pscustomobject]@{ id = '999' } }
            'replaced-draft' { if ($global:Recovery.reads -ge 2) { $result.pendingFlightSubmission = [pscustomobject]@{ id = '999' } } }
        }
        return $result
    }
    if ($Method -eq 'Get' -and $Uri -ceq "$base/flights/$old/submissions/456") {
        return [pscustomobject]@{ id = '456'; flightId = $old; status = $(if ($global:Recovery.scenario -eq 'committed') { 'CommitStarted' } else { 'PendingCommit' }); flightPackages = @(if ($global:Recovery.scenario -eq 'nonempty') { @{ fileName = 'owned-by-someone-else.msixbundle' } }) }
    }
    if ($Method -eq 'Delete' -and $Uri -ceq "$base/flights/$old/submissions/456") {
        $global:Recovery.deleted = $true
        if ($global:Recovery.scenario -eq 'lost-delete') { throw 'Lost delete response.' }
        return
    }
    throw "Unexpected API call: $Method $Uri"
}
function Invoke-Fixture([string]$Operation) {
    $draft = @{}
    if ($Operation -eq 'discard-draft') { $draft.SubmissionId = '456' }
    & (Join-Path $PSScriptRoot '../scripts/Repair-MicrosoftStoreFlight.ps1') -Operation $Operation -Product companion `
        -ApplicationId TESTPRODUCT -FlightId $old -GroupId 123 @draft `
        -TenantId '11111111-1111-1111-1111-111111111111' -ClientId '22222222-2222-2222-2222-222222222222' `
        -ClientAssertionFile (Join-Path $root 'assertion') -EvidencePath (Join-Path $root 'evidence.json') -HttpInvoker $http
}
try {
    foreach ($operation in @('inspect', 'create', 'discard-draft')) {
        Reset-Fixture $operation ''
        Invoke-Fixture $operation
        $record = Get-Content (Join-Path $root 'evidence.json') -Raw | ConvertFrom-Json
        $expected = if ($operation -eq 'inspect') { 'inspected' } else { 'verified' }
        if ($record.status -cne $expected) { throw "Missing $operation receipt." }
        if ($operation -eq 'create' -and $record.flightId -cne $new) { throw 'Replacement GUID lost.' }
        if ($operation -eq 'discard-draft' -and $record.flightId -cne $old) { throw 'Flight not preserved.' }
        if ($global:Recovery.calls -match '^(Post|Delete).*applications/TESTPRODUCT/submissions') { throw 'Production mutated.' }
        $passed++
    }
    foreach ($case in @(
        @('create', 'foreign-product', 'approved identity'), @('create', 'existing-flight', 'already exists'),
        @('create', 'same-name', 'already exists'), @('create', 'incomplete', 'incomplete'),
        @('create', 'lost-create', 'Lost create'), @('create', 'wrong-group', 'tester group'),
        @('discard-draft', 'wrong-group', 'tester group'), @('discard-draft', 'published', 'published flight'),
        @('discard-draft', 'foreign-draft', 'approved submission'), @('discard-draft', 'nonempty', 'empty, uncommitted'),
        @('discard-draft', 'committed', 'empty, uncommitted'), @('discard-draft', 'replaced-draft', 'changed'),
        @('discard-draft', 'lost-delete', 'Lost delete'), @('discard-draft', 'removed-flight', 'missing after deletion')
    )) {
        Reset-Fixture $case[0] $case[1]
        $failed = $false
        try { Invoke-Fixture $case[0] } catch {
            if ($_.Exception.Message -notmatch $case[2]) { throw }
            $failed = $true
        }
        if (-not $failed) { throw "Expected rejection: $($case[1])" }
        $writes = @($global:Recovery.calls | Where-Object { $_ -match '^(Post|Delete) https://manage' })
        $mayWrite = $case[1] -in @('lost-create', 'lost-delete', 'removed-flight') -or ($case[0] -eq 'create' -and $case[1] -eq 'wrong-group')
        if ($writes.Count -gt 1 -or (-not $mayWrite -and $writes.Count)) { throw 'Unexpected or repeated mutation.' }
        if ($mayWrite) {
            $record = Get-Content (Join-Path $root 'evidence.json') -Raw | ConvertFrom-Json
            if ($record.status -notin @('create-requested', 'discard-requested')) { throw 'Lost ambiguous-mutation evidence.' }
        }
        $passed++
    }
    # Execute the real workflow argument wiring against a synthetic recovery command.
    $workflow = Get-Content (Join-Path $PSScriptRoot '../.github/workflows/windows-store-flight-recovery.yml') -Raw
    $step = [regex]::Match($workflow, '(?ms)^      - name: Execute only the approved recovery operation\r?\n.*?^        run: \|\r?\n(?<script>(?:^ {10}[^\r\n]*\r?\n|^\r?\n)+)')
    if (-not $step.Success) { throw 'Recovery workflow entry point missing.' }
    $invoke = [scriptblock]::Create([regex]::Replace($step.Groups['script'].Value, '(?m)^ {10}', ''))
    [void][IO.Directory]::CreateDirectory((Join-Path $root 'scripts'))
    [void][IO.Directory]::CreateDirectory((Join-Path $root 'evidence'))
    [IO.File]::WriteAllText((Join-Path $root 'scripts/Repair-MicrosoftStoreFlight.ps1'), @'
param($Operation, $Product, $ApplicationId, $FlightId, $GroupId, $SubmissionId, $TenantId, $ClientId, $ClientAssertionFile, $EvidencePath)
[IO.File]::WriteAllText((Join-Path $PWD $EvidencePath), (@{ operation=$Operation; product=$Product; flightId=$FlightId; groupId=$GroupId; submissionId=$SubmissionId } | ConvertTo-Json))
'@)
    $names = @('STORE_PRODUCT', 'OPERATION', 'FLIGHT_ID', 'GROUP_ID', 'SUBMISSION_ID', 'MSSTORE_TENANT_ID', 'MSSTORE_CLIENT_ID', 'MSSTORE_APPLICATION_ID', 'ASSERTION_PATH', 'GITHUB_STEP_SUMMARY')
    $original = @{}
    $location = Get-Location
    try {
        foreach ($name in $names) { $original[$name] = [Environment]::GetEnvironmentVariable($name) }
        Set-Location $root
        $env:FLIGHT_ID=$old; $env:GROUP_ID='123'; $env:MSSTORE_TENANT_ID='fixture'; $env:MSSTORE_CLIENT_ID='fixture'
        $env:MSSTORE_APPLICATION_ID='TESTPRODUCT'; $env:ASSERTION_PATH='assertion'; $env:GITHUB_STEP_SUMMARY=Join-Path $root 'summary'
        foreach ($product in @('gateway', 'companion')) {
            foreach ($operation in @('inspect', 'create', 'discard-draft')) {
                $env:STORE_PRODUCT=$product; $env:OPERATION=$operation
                $env:SUBMISSION_ID=if ($operation -eq 'discard-draft') { '456' } else { '' }
                & $invoke
                $called=Get-Content ./evidence/flight-recovery.json -Raw | ConvertFrom-Json
                if ($called.operation -cne $operation -or $called.product -cne $product -or $called.flightId -cne $old -or
                    $called.groupId -cne '123' -or [string]$called.submissionId -cne $env:SUBMISSION_ID) { throw 'Recovery workflow changed approved inputs.' }
                $passed++
            }
        }
    } finally {
        Set-Location $location
        foreach ($name in $names) { [Environment]::SetEnvironmentVariable($name, $original[$name]) }
    }
    Write-Host "$passed flight recovery scenarios passed."
} finally {
    Remove-Variable -Name Recovery -Scope Global -ErrorAction SilentlyContinue
    Remove-Item $root -Recurse -Force
}
