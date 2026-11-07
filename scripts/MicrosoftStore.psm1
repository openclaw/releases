Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Get-MicrosoftStoreProduct {
    param([Parameter(Mandatory)][ValidateSet('gateway', 'companion', IgnoreCase = $false)][string]$Product)
    $gateway = $Product -ceq 'gateway'
    [pscustomobject]@{
        product = $Product
        repository = if ($gateway) { 'openclaw/openclaw-windows-packaging' } else { 'openclaw/openclaw-windows-node' }
        environment = "microsoft-store-$Product"
        identityName = if ($gateway) { 'OpenClawFoundation.OpenClawGateway' } else { 'OpenClawFoundation.OpenClaw' }
        publisher = 'CN=4BA40A7A-B719-4C40-BF91-84AF4F1136FC'
        artifactName = if ($gateway) { 'openclaw-gateway-msix-store-submission' } else { 'openclaw-msix-store-unsigned-bundle' }
    }
}

function Invoke-StoreGitHubApi {
    param([string]$Repository, [string]$Path)
    $result = & gh api "repos/$Repository/$Path"
    if ($LASTEXITCODE -ne 0) { throw 'Unable to read Microsoft Store publication authority from GitHub.' }
    $result | ConvertFrom-Json -Depth 50
}

function Assert-MicrosoftStoreEnvironment {
    param(
        [Parameter(Mandatory)][ValidateSet('gateway', 'companion', IgnoreCase = $false)][string]$Product,
        [scriptblock]$ApiInvoker = ${function:Invoke-StoreGitHubApi}
    )
    $config = Get-MicrosoftStoreProduct $Product
    $environment = & $ApiInvoker 'openclaw/releases' "environments/$($config.environment)"
    $rules = @($environment.protection_rules | Where-Object type -CEQ 'required_reviewers')
    $reviewers = @($rules | ForEach-Object { $_.reviewers })
    if ($rules.Count -ne 1 -or $reviewers.Count -ne 1 -or $reviewers[0].type -cne 'Team' -or
        $reviewers[0].reviewer.id -ne 16590423 -or $environment.can_admins_bypass -ne $false) {
        throw "Configure $($config.environment) with only the OpenClaw release-manager team and no administrator bypass."
    }
    if ($environment.deployment_branch_policy.custom_branch_policies -ne $true -or
        $environment.deployment_branch_policy.protected_branches -ne $false) {
        throw 'Store publication requires an explicit main-only deployment policy.'
    }
    $policies = & $ApiInvoker 'openclaw/releases' "environments/$($config.environment)/deployment-branch-policies"
    $branches = @($policies.branch_policies)
    if ($policies.total_count -ne 1 -or $branches.Count -ne 1 -or
        $branches[0].name -cne 'main' -or $branches[0].type -cne 'branch') {
        throw 'Store publication permits only the exact main branch, not tags or wildcard branches.'
    }
}

function Assert-PublishedStoreSource {
    param([string]$Repository, [string]$Tag, [string]$Commit, [bool]$RequireSignedTag, [scriptblock]$ApiInvoker, [bool]$Prerelease = $false)
    $pattern = if ($Prerelease) { '^v[0-9]{4}\.[0-9]+\.[0-9]+-beta\.[1-9][0-9]*$' } else { '^v[0-9]+\.[0-9]+\.[0-9]+(?:-[0-9]+)?$' }
    if ($Tag -cnotmatch $pattern -or $Commit -cnotmatch '^[0-9a-f]{40}$') {
        throw 'Store publication requires an exact stable or beta release tag and source commit.'
    }
    $release = & $ApiInvoker $Repository "releases/tags/$Tag"
    if ($release.tag_name -cne $Tag -or $release.draft -ne $false -or $release.prerelease -ne $Prerelease) {
        throw 'Store source must be an already published release of the selected channel.'
    }
    if ($RequireSignedTag) {
        $ref = & $ApiInvoker $Repository "git/ref/tags/$Tag"
        if ($ref.object.type -cne 'tag') { throw 'Gateway Store source requires an annotated signed tag.' }
        $tagObject = & $ApiInvoker $Repository "git/tags/$($ref.object.sha)"
        if ($tagObject.tag -cne $Tag -or $tagObject.object.type -cne 'commit' -or
            $tagObject.object.sha -cne $Commit -or $tagObject.verification.verified -ne $true) {
            throw 'Gateway signed tag does not match the selected source.'
        }
    } else {
        $resolved = & $ApiInvoker $Repository "commits/$Tag"
        if ($resolved.sha -cne $Commit) { throw 'Companion release tag no longer matches its Store witness.' }
    }
}

function Get-AuthorizedStoreSource {
    param(
        [Parameter(Mandatory)][ValidateSet('gateway', 'companion', IgnoreCase = $false)][string]$Product,
        [Parameter(Mandatory)][ValidatePattern('^[1-9][0-9]*$')][string]$RunId,
        [Parameter(Mandatory)][string]$Directory,
        [ValidateSet('production', 'development')][string]$Channel = 'production',
        [string]$DevelopmentFlightId,
        [bool]$Automatic = $false,
        [string]$DevelopmentEnabled,
        [scriptblock]$ApiInvoker = ${function:Invoke-StoreGitHubApi},
        [scriptblock]$DownloadInvoker
    )
    $config = Get-MicrosoftStoreProduct $Product
    $Channel = $Channel.ToLowerInvariant()
    $development = $Channel -ceq 'development'
    $flightId = ''
    if ($development) {
        if ($Automatic -and $DevelopmentEnabled -ine 'true') {
            throw 'Automatic Gateway Development delivery is disabled. Qualify the flight manually before enabling it.'
        }
        $parsedFlight = [guid]::Empty
        if ($Product -cne 'gateway' -or -not [guid]::TryParse($DevelopmentFlightId, [ref]$parsedFlight) -or $parsedFlight -eq [guid]::Empty) {
            throw 'Gateway Development publication requires the configured flight GUID.'
        }
        $flightId = $parsedFlight.ToString()
    }
    if ($null -eq $DownloadInvoker) {
        $DownloadInvoker = {
            param($Repository, $Id, $Name, $Destination)
            & gh run download $Id --repo $Repository --name $Name --dir $Destination
            if ($LASTEXITCODE -ne 0) { throw 'Unable to download the authorized Store source witness.' }
        }
    }
    $run = & $ApiInvoker $config.repository "actions/runs/$RunId"
    if ($run.repository.full_name -cne $config.repository -or $run.head_repository.full_name -cne $config.repository -or
        [string]$run.id -cne $RunId -or $run.status -cne 'completed' -or $run.conclusion -cne 'success' -or
        $run.head_sha -cnotmatch '^[0-9a-f]{40}$' -or [int]$run.run_attempt -lt 1) {
        throw 'Store publication requires a successful, completed run in the canonical source repository.'
    }
    $gateway = $Product -ceq 'gateway'
    $tagRun = $run.path -ceq '.github/workflows/ci.yml' -and
        $run.event -cin @('push', 'workflow_dispatch') -and
        $run.head_branch -cmatch '^v[0-9]+\.[0-9]+\.[0-9]+(?:-[0-9]+)?$'
    $promotionRun = $run.path -ceq '.github/workflows/promote-alpha-release.yml' -and
        $run.event -ceq 'workflow_dispatch' -and $run.head_branch -ceq 'main'
    $gatewayRun = $run.path -ceq '.github/workflows/gateway-msix.yml' -and
        $run.event -ceq 'workflow_dispatch' -and $run.head_branch -ceq 'main'
    if (($gateway -and -not $gatewayRun) -or (-not $gateway -and -not ($tagRun -or $promotionRun))) {
        throw 'The selected source workflow, event, or ref cannot authorize a Store publication.'
    }
    if ($gatewayRun -or $promotionRun) {
        # Run head_branch is unqualified: a tag named main is not evidence of
        # protected branch review. Authenticate ancestry through GitHub instead.
        $main = & $ApiInvoker $config.repository 'git/ref/heads/main'
        if ($main.object.type -cne 'commit' -or $main.object.sha -cnotmatch '^[0-9a-f]{40}$') {
            throw 'Unable to resolve protected main history.'
        }
        $comparison = & $ApiInvoker $config.repository "compare/$($run.head_sha)...$($main.object.sha)"
        if ($comparison.status -cnotin @('ahead', 'identical') -or
            $comparison.base_commit.sha -cne $run.head_sha -or $comparison.merge_base_commit.sha -cne $run.head_sha) {
            throw 'Store source pipeline does not belong to protected main history.'
        }
    }

    $artifacts = [Collections.Generic.List[object]]::new()
    for ($page = 1; ; $page++) {
        $result = & $ApiInvoker $config.repository "actions/runs/$RunId/artifacts?per_page=100&page=$page"
        foreach ($artifact in @($result.artifacts)) { $artifacts.Add($artifact) }
        if ($artifacts.Count -ge $result.total_count) { break }
        if (@($result.artifacts).Count -eq 0) { throw 'Store artifact inventory is incomplete.' }
    }
    $metadataName = "store-release-source-$($run.run_attempt)"
    $bundleArtifactName = if ($gateway) { "$($config.artifactName)-$($run.run_attempt)" } else { $config.artifactName }
    $selected = @($artifacts | Where-Object name -CEQ $bundleArtifactName)
    $metadata = @($artifacts | Where-Object name -CEQ $metadataName)
    if ($selected.Count -ne 1 -or $metadata.Count -ne 1) { throw 'Store bundle or source witness is missing or ambiguous.' }
    foreach ($artifact in @($selected[0], $metadata[0])) {
        if ($artifact.expired -ne $false -or [string]$artifact.id -cnotmatch '^[1-9][0-9]*$') {
            throw 'Store bundle or source witness is missing, ambiguous, or expired.'
        }
    }
    [void][IO.Directory]::CreateDirectory($Directory)
    & $DownloadInvoker $config.repository $RunId $metadataName $Directory | Out-Null
    $witness = Get-Content -LiteralPath (Join-Path $Directory 'store-source.json') -Raw | ConvertFrom-Json -Depth 20
    if ([string]$witness.runId -cne $RunId -or [int]$witness.runAttempt -ne [int]$run.run_attempt -or
        $witness.bundleSha256 -cnotmatch '^[0-9a-f]{64}$') {
        throw 'Store witness does not match this release run and attempt.'
    }
    $expectedHash = [string]$witness.bundleSha256
    $bundleName = 'OpenClaw.msixbundle'
    $resolutionArtifactId = ''
    if ($gateway) {
        $resolution = @($artifacts | Where-Object name -CEQ 'openclaw-source-resolution')
        if ($resolution.Count -ne 1 -or $resolution[0].expired -ne $false -or [string]$resolution[0].id -cnotmatch '^[1-9][0-9]*$') {
            throw 'Gateway source resolution is missing, ambiguous, or expired.'
        }
        $resolutionArtifactId = [string]$resolution[0].id
        & $DownloadInvoker $config.repository $RunId 'openclaw-source-resolution' $Directory | Out-Null
        $source = Get-Content -LiteralPath (Join-Path $Directory 'source-resolution.json') -Raw | ConvertFrom-Json -Depth 20
        $identity = $source.releaseIdentitySource
        $releaseChannel = if ($development) { 'beta' } else { 'stable' }
        if ($source.repository -cne 'https://github.com/openclaw/openclaw' -or
            $source.workflowRunId -cne $RunId -or $source.packagingCommit -cne $run.head_sha -or
            $source.workflowRef -cne 'openclaw/openclaw-windows-packaging/.github/workflows/gateway-msix.yml@refs/heads/main' -or
            $source.githubRef -cne 'refs/heads/main' -or $source.eventName -cne 'workflow_dispatch' -or
            $source.signingMode -cnotin @('store', 'official') -or
            ($development -and $source.signingMode -cne 'official') -or
            $source.releaseChannel -cne $releaseChannel -or $witness.releaseChannel -cne $releaseChannel -or
            $witness.packagingCommit -cne $run.head_sha -or
            $identity.repository -cne $source.repository -or $identity.channel -cne $releaseChannel -or
            $identity.releaseTag -cne "v$($identity.packageVersion)") {
            throw 'Gateway source snapshot or witness does not match the selected channel and release identity.'
        }
        $releaseTag = "v$($source.packageVersion)"
        $sourceSha = [string]$source.resolvedCommit
        $identityTag = [string]$identity.releaseTag
        $identitySha = [string]$identity.resolvedCommit
        Assert-PublishedStoreSource 'openclaw/openclaw' $releaseTag $sourceSha $true $ApiInvoker $development
        if ($identityTag -cne $releaseTag -or $identitySha -cne $sourceSha) {
            Assert-PublishedStoreSource 'openclaw/openclaw' $identityTag $identitySha $true $ApiInvoker $development
        }
        if ($witness.releaseTag -cnotmatch ("^" + [regex]::Escape($identityTag) + '-msix\.[0-9]$') -or
            $witness.bundleName -cne "OpenClawGateway-$($witness.releaseTag.Substring(1))-store.msixbundle") {
            throw 'Gateway Store witness contains an invalid packaging release tag or bundle name.'
        }
        $bundleName = [string]$witness.bundleName
        if ($development) {
            $release = & $ApiInvoker $config.repository "releases/tags/$($witness.releaseTag)"
            $packagingCommit = & $ApiInvoker $config.repository "commits/$($witness.releaseTag)"
            if ($release.tag_name -cne $witness.releaseTag -or $release.draft -ne $false -or $release.prerelease -ne $true -or
                -not $release.published_at -or $packagingCommit.sha -cne $run.head_sha) {
                throw 'Development delivery requires the published packaging GitHub prerelease at this pipeline commit.'
            }
        }
    } else {
        $source = $witness
        if ($tagRun -and ($source.releaseTag -cne $run.head_branch -or $source.sourceSha -cne $run.head_sha)) {
            throw 'Companion Store witness does not match this release run and attempt.'
        }
        $releaseTag = [string]$source.releaseTag
        $sourceSha = [string]$source.sourceSha
        $identityTag = $releaseTag
        $identitySha = $sourceSha
        Assert-PublishedStoreSource $config.repository $releaseTag $sourceSha $false $ApiInvoker
    }
    [pscustomobject][ordered]@{
        product = $Product
        repository = $config.repository
        environment = $config.environment
        channel = $Channel
        flightId = $flightId
        automatic = $Automatic
        runId = $RunId
        runAttempt = [int]$run.run_attempt
        pipelineSha = [string]$run.head_sha
        releaseTag = $releaseTag
        sourceSha = $sourceSha
        releaseIdentityTag = $identityTag
        releaseIdentitySha = $identitySha
        artifactId = [string]$selected[0].id
        witnessArtifactId = [string]$metadata[0].id
        resolutionArtifactId = $resolutionArtifactId
        expectedBundleName = $bundleName
        expectedBundleSha256 = $expectedHash
    }
}

function Confirm-AuthorizedStoreBundle {
    param([Parameter(Mandatory)][psobject]$Source, [Parameter(Mandatory)][string]$Directory, [psobject]$ApprovedSource)
    $config = Get-MicrosoftStoreProduct $Source.product
    $bundles = @(Get-ChildItem -LiteralPath $Directory -File -Filter '*.msixbundle')
    if ($bundles.Count -ne 1 -or $bundles[0].Name -cne $Source.expectedBundleName) { throw 'Expected exactly the authorized product Store bundle.' }
    $bundle = $bundles[0]
    $hash = (Get-FileHash -LiteralPath $bundle.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($Source.expectedBundleSha256 -and $Source.expectedBundleSha256 -cne $hash) { throw 'Store bundle differs from its release witness.' }
    $archive = [IO.Compression.ZipFile]::OpenRead($bundle.FullName)
    try {
        $entries = @($archive.Entries | Where-Object FullName -CEQ 'AppxMetadata/AppxBundleManifest.xml')
        if ($entries.Count -ne 1 -or $null -ne $archive.GetEntry('AppxSignature.p7x')) { throw 'Store source must be an unsigned, unambiguous MSIX bundle.' }
        $settings = [Xml.XmlReaderSettings]::new()
        $settings.DtdProcessing = [Xml.DtdProcessing]::Prohibit
        $reader = [Xml.XmlReader]::Create($entries[0].Open(), $settings)
        try { $manifest = [Xml.XmlDocument]::new(); $manifest.Load($reader) } finally { $reader.Dispose() }
        if ([string]$manifest.Bundle.Identity.Name -cne $config.identityName -or
            [string]$manifest.Bundle.Identity.Publisher -cne $config.publisher -or
            [string]$manifest.Bundle.Identity.Version -cnotmatch '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$') {
            throw 'Store bundle has a foreign product identity, publisher, or invalid package version.'
        }
        $version = [version]$manifest.Bundle.Identity.Version
        if (@($version.Major, $version.Minor, $version.Build, $version.Revision | Where-Object { $_ -gt 65535 }).Count -gt 0) {
            throw 'Store package version exceeds the MSIX component bounds.'
        }
        if ($version.Revision -ne 0) { throw 'Store package version must reserve its fourth component as zero.' }
    } finally { $archive.Dispose() }
    $record = $Source | Select-Object *
    $record | Add-Member -NotePropertyName bundleName -NotePropertyValue $bundle.Name
    $record | Add-Member -NotePropertyName bundleSha256 -NotePropertyValue $hash
    $record | Add-Member -NotePropertyName packageVersion -NotePropertyValue $version.ToString()
    if ($null -ne $ApprovedSource) {
        foreach ($field in $record.PSObject.Properties.Name) {
            if ($ApprovedSource.PSObject.Properties.Name -notcontains $field -or [string]$record.$field -cne [string]$ApprovedSource.$field) {
                throw "Store authority or artifact changed while awaiting approval: $field. Request a fresh approval."
            }
        }
    }
    $record
}

Export-ModuleMember -Function Get-MicrosoftStoreProduct, Assert-MicrosoftStoreEnvironment, Get-AuthorizedStoreSource, Confirm-AuthorizedStoreBundle
