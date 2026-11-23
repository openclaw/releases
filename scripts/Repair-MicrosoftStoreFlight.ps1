[CmdletBinding()]
param(
    [Parameter(Mandatory)][ValidateSet('inspect', 'create', 'replace-empty-flight')][string]$Operation,
    [Parameter(Mandatory)][ValidateSet('gateway', 'companion')][string]$Product,
    [Parameter(Mandatory)][ValidatePattern('^[A-Z0-9]+$')][string]$ApplicationId,
    [Parameter(Mandatory)][guid]$FlightId,
    [Parameter(Mandatory)][ValidatePattern('^[1-9][0-9]*$')][string]$GroupId,
    [ValidatePattern('^[1-9][0-9]*$')][string]$SubmissionId,
    [Parameter(Mandatory)][guid]$TenantId,
    [Parameter(Mandatory)][guid]$ClientId,
    [Parameter(Mandatory)][string]$ClientAssertionFile,
    [Parameter(Mandatory)][string]$EvidencePath,
    [scriptblock]$HttpInvoker
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
Import-Module (Join-Path $PSScriptRoot 'MicrosoftStore.psm1') -Force
if ($FlightId -eq [guid]::Empty) { throw 'Expected flight ID must not be empty.' }
if (($Operation -eq 'replace-empty-flight') -ne (-not [string]::IsNullOrEmpty($SubmissionId))) {
    throw 'Only replace-empty-flight requires an exact submission ID.'
}
$config = Get-MicrosoftStoreProduct $Product
if ($null -eq $HttpInvoker) {
    $HttpInvoker = {
        param($Method, $Uri, $Headers, $Body, $ContentType)
        $parameters = @{ Method = $Method; Uri = $Uri; ErrorAction = 'Stop'; ContentType = $ContentType }
        if ($null -ne $Headers) { $parameters.Headers = $Headers }
        if ($null -ne $Body) { $parameters.Body = $Body }
        Invoke-RestMethod @parameters
    }
}
$assertion = [IO.File]::ReadAllText((Resolve-Path -LiteralPath $ClientAssertionFile).Path).Trim()
$headers = New-MicrosoftStoreAccessHeaders -TenantId $TenantId -ClientId $ClientId -Assertion $assertion `
    -MinimumLifetimeSeconds 300 -HttpInvoker $HttpInvoker
$applicationPath = "/v1.0/my/applications/$ApplicationId"
function Invoke-Api([string]$Method, [string]$Path, $Body = $null) {
    $json = if ($null -eq $Body) { $null } else { $Body | ConvertTo-Json -Depth 10 -Compress }
    & $HttpInvoker $Method ("https://manage.devcenter.microsoft.com" + $Path) $headers $json 'application/json'
}
function Optional($Object, [string]$Name) {
    if ($null -eq $Object) { return $null }
    $property = $Object.PSObject.Properties[$Name]
    if ($null -ne $property) { $property.Value }
}
function Assert-Flight($Flight, [guid]$ExpectedId) {
    if ([guid]$Flight.flightId -ne $ExpectedId -or $Flight.friendlyName -cne 'Development' -or
        @($Flight.groupIds).Count -ne 1 -or [string]$Flight.groupIds[0] -cne $GroupId) {
        throw 'Flight identity, name, or tester group differs from approval.'
    }
    if ($null -ne (Optional $Flight 'lastPublishedFlightSubmission')) {
        throw 'Recovery must not modify a previously published flight.'
    }
}
$record = [ordered]@{ schemaVersion = 1; operation = $Operation; product = $Product; applicationId = $ApplicationId
    expectedFlightId = $FlightId.ToString(); groupId = $GroupId; submissionId = $SubmissionId; status = 'inspecting' }
$evidence = [IO.Path]::GetFullPath($EvidencePath, $PWD.Path)
[void][IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($evidence))
function Save-Evidence { [IO.File]::WriteAllText($evidence, ($record | ConvertTo-Json -Depth 10)) }
Save-Evidence
$app = Invoke-Api Get $applicationPath
if ($app.id -cne $ApplicationId -or $app.packageIdentityName -cne $config.identityName -or $app.publisherName -cne $config.publisher) {
    throw 'Store product does not match the approved identity.'
}
# Refuse incomplete enumeration rather than follow an untrusted continuation URL.
$list = Invoke-Api Get "$applicationPath/listflights?top=100"
$flights = @($list.value)
if ($flights.Count -ne [int]$list.totalCount -or (Optional $list '@nextLink')) { throw 'Flight inventory is incomplete.' }
$matches = @($flights | Where-Object { [guid]$_.flightId -eq $FlightId })
$record.flightIds = @($flights | ForEach-Object { [string]$_.flightId })
Save-Evidence
if ($Operation -eq 'inspect') {
    $record.status = 'inspected'
    $record.flights = @($flights | ForEach-Object { [ordered]@{
        flightId = $_.flightId; friendlyName = $_.friendlyName; groupIds = $_.groupIds
        pendingSubmissionId = (Optional (Optional $_ 'pendingFlightSubmission') 'id')
    } })
    Save-Evidence
    return
}
if ($Operation -eq 'create') {
    if ($matches.Count -ne 0 -or @($flights | Where-Object friendlyName -IEQ 'Development').Count -ne 0) {
        throw 'Expected old flight or Development flight already exists; inspect instead of creating another.'
    }
} else {
    if ($matches.Count -ne 1 -or @($flights | Where-Object friendlyName -IEQ 'Development').Count -ne 1) {
        throw 'Expected flight is missing or ambiguous.'
    }
    $path = "$applicationPath/flights/$FlightId"
    $flight = Invoke-Api Get $path
    Assert-Flight $flight $FlightId
    $pending = Optional $flight 'pendingFlightSubmission'
    if ($null -eq $pending -or [string]$pending.id -cne $SubmissionId) { throw 'Pending draft differs from the approved submission.' }
    $draft = Invoke-Api Get "$path/submissions/$SubmissionId"
    if ([string]$draft.id -cne $SubmissionId -or [guid]$draft.flightId -ne $FlightId -or
        $draft.status -cne 'PendingCommit' -or @($draft.flightPackages).Count -ne 0) {
        throw 'Only the exact empty, uncommitted bootstrap flight may be replaced.'
    }
    $fresh = Invoke-Api Get $path
    Assert-Flight $fresh $FlightId
    if ([string](Optional $fresh 'pendingFlightSubmission').id -cne $SubmissionId) { throw 'Pending draft changed.' }
    $record.status = 'replace-requested'; Save-Evidence
    # Initial drafts and their flights share a lifetime. Replace the explicitly approved
    # empty flight, not its portal-owned draft, then preserve the API-created initial draft.
    Invoke-Api Delete $path | Out-Null
    $remaining = Invoke-Api Get "$applicationPath/listflights?top=100"
    if (@($remaining.value).Count -ne [int]$remaining.totalCount -or (Optional $remaining '@nextLink') -or
        @($remaining.value | Where-Object { [guid]$_.flightId -eq $FlightId -or $_.friendlyName -ieq 'Development' }).Count) {
        throw 'Flight removal was not verified; inspect instead of retrying.'
    }
}
$record.status = 'create-requested'; Save-Evidence
$created = Invoke-Api Post "$applicationPath/flights" @{ friendlyName = 'Development'; groupIds = @($GroupId) }
$newId = [guid]$created.flightId
if ($newId -eq [guid]::Empty -or $newId -eq $FlightId) { throw 'Store returned an invalid replacement flight ID.' }
$record.flightId = $newId.ToString(); Save-Evidence
$initialId = [string](Optional (Optional $created 'pendingFlightSubmission') 'id')
if ($initialId -cnotmatch '^[1-9][0-9]*$') { throw 'Created flight did not identify its initial submission.' }
$record.initialSubmissionId = $initialId; Save-Evidence
$verified = Invoke-Api Get "$applicationPath/flights/$newId"
Assert-Flight $verified $newId
if ([string](Optional (Optional $verified 'pendingFlightSubmission') 'id') -cne $initialId) {
    throw 'Created flight initial submission changed.'
}
$initial = Invoke-Api Get "$applicationPath/flights/$newId/submissions/$initialId"
if ([string]$initial.id -cne $initialId -or [guid]$initial.flightId -ne $newId -or
    $initial.status -cne 'PendingCommit' -or @($initial.flightPackages).Count -ne 0) {
    throw 'Created flight initial submission is not empty and uncommitted.'
}
$record.status = 'verified'; Save-Evidence
