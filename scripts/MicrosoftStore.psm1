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
    param([string]$Repository, [string]$Tag, [string]$Commit, [bool]$RequireSignedTag, [scriptblock]$ApiInvoker)
    if ($Tag -cnotmatch '^v[0-9]+\.[0-9]+\.[0-9]+(?:-[0-9]+)?$' -or $Commit -cnotmatch '^[0-9a-f]{40}$') {
        throw 'Store publication requires an exact final release tag and source commit.'
    }
    $release = & $ApiInvoker $Repository "releases/tags/$Tag"
    if ($release.tag_name -cne $Tag -or $release.draft -ne $false -or $release.prerelease -ne $false) {
        throw 'Store source must be an already published, final release.'
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
        [scriptblock]$ApiInvoker = ${function:Invoke-StoreGitHubApi},
        [scriptblock]$DownloadInvoker
    )
    $config = Get-MicrosoftStoreProduct $Product
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

    $artifacts = [Collections.Generic.List[object]]::new()
    for ($page = 1; ; $page++) {
        $result = & $ApiInvoker $config.repository "actions/runs/$RunId/artifacts?per_page=100&page=$page"
        foreach ($artifact in @($result.artifacts)) { $artifacts.Add($artifact) }
        if ($artifacts.Count -ge $result.total_count) { break }
        if (@($result.artifacts).Count -eq 0) { throw 'Store artifact inventory is incomplete.' }
    }
    $metadataName = if ($gateway) { 'openclaw-source-resolution' } else { "store-release-source-$($run.run_attempt)" }
    $selected = @($artifacts | Where-Object name -CEQ $config.artifactName)
    $metadata = @($artifacts | Where-Object name -CEQ $metadataName)
    if ($selected.Count -ne 1 -or $metadata.Count -ne 1) { throw 'Store bundle or source witness is missing or ambiguous.' }
    foreach ($artifact in @($selected[0], $metadata[0])) {
        if ($artifact.expired -ne $false -or [string]$artifact.id -cnotmatch '^[1-9][0-9]*$') {
            throw 'Store bundle or source witness is missing, ambiguous, or expired.'
        }
    }
    [void][IO.Directory]::CreateDirectory($Directory)
    & $DownloadInvoker $config.repository $RunId $metadataName $Directory | Out-Null
    $metadataFile = if ($gateway) { 'source-resolution.json' } else { 'store-source.json' }
    $source = Get-Content -LiteralPath (Join-Path $Directory $metadataFile) -Raw | ConvertFrom-Json -Depth 20
    $expectedHash = ''
    if ($gateway) {
        $identity = if ($source.PSObject.Properties.Name -contains 'releaseIdentitySource') { $source.releaseIdentitySource } else { $source }
        if ($source.repository -cne 'https://github.com/openclaw/openclaw' -or
            $source.workflowRunId -cne $RunId -or $source.packagingCommit -cne $run.head_sha -or
            $source.workflowRef -cne 'openclaw/openclaw-windows-packaging/.github/workflows/gateway-msix.yml@refs/heads/main' -or
            $source.githubRef -cne 'refs/heads/main' -or $source.eventName -cne 'workflow_dispatch' -or
            $source.signingMode -cnotin @('store', 'official') -or
            $identity.repository -cne $source.repository -or $identity.channel -cne 'stable' -or
            $identity.releaseTag -cne "v$($identity.packageVersion)") {
            throw 'Gateway source snapshot does not match the successful authorized build and stable release identity.'
        }
        $releaseTag = "v$($source.packageVersion)"
        $sourceSha = [string]$source.resolvedCommit
        $identityTag = [string]$identity.releaseTag
        $identitySha = [string]$identity.resolvedCommit
        Assert-PublishedStoreSource 'openclaw/openclaw' $releaseTag $sourceSha $true $ApiInvoker
        if ($identityTag -cne $releaseTag -or $identitySha -cne $sourceSha) {
            Assert-PublishedStoreSource 'openclaw/openclaw' $identityTag $identitySha $true $ApiInvoker
        }
    } else {
        if ([string]$source.runId -cne $RunId -or [int]$source.runAttempt -ne [int]$run.run_attempt -or
            $source.bundleSha256 -cnotmatch '^[0-9a-f]{64}$' -or
            ($tagRun -and ($source.releaseTag -cne $run.head_branch -or $source.sourceSha -cne $run.head_sha))) {
            throw 'Companion Store witness does not match this release run and attempt.'
        }
        $releaseTag = [string]$source.releaseTag
        $sourceSha = [string]$source.sourceSha
        $identityTag = $releaseTag
        $identitySha = $sourceSha
        $expectedHash = [string]$source.bundleSha256
        Assert-PublishedStoreSource $config.repository $releaseTag $sourceSha $false $ApiInvoker
    }
    [pscustomobject][ordered]@{
        product = $Product
        repository = $config.repository
        environment = $config.environment
        runId = $RunId
        runAttempt = [int]$run.run_attempt
        pipelineSha = [string]$run.head_sha
        releaseTag = $releaseTag
        sourceSha = $sourceSha
        releaseIdentityTag = $identityTag
        releaseIdentitySha = $identitySha
        artifactId = [string]$selected[0].id
        witnessArtifactId = [string]$metadata[0].id
        expectedBundleSha256 = $expectedHash
    }
}

function Confirm-AuthorizedStoreBundle {
    param([Parameter(Mandatory)][psobject]$Source, [Parameter(Mandatory)][string]$Directory, [psobject]$ApprovedSource)
    $config = Get-MicrosoftStoreProduct $Source.product
    $bundles = @(Get-ChildItem -LiteralPath $Directory -File -Filter '*.msixbundle')
    $pattern = if ($Source.product -ceq 'gateway') { '^OpenClawGateway-[0-9]+\.[0-9]+\.[0-9]+(?:-[0-9]+)?-msix\.[0-9]+-store\.msixbundle$' } else { '^OpenClaw\.msixbundle$' }
    if ($bundles.Count -ne 1 -or $bundles[0].Name -cnotmatch $pattern) { throw 'Expected exactly the authorized product Store bundle.' }
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
