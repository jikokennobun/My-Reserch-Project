param(
    [string]$GuildId = $env:DISCORD_GUILD_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string]$PlanPath,
    [string]$RepositoryRoot,
    [switch]$Apply,
    [switch]$StoreInUserEnvironment
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}
if ([string]::IsNullOrWhiteSpace($PlanPath)) {
    $PlanPath = Join-Path $RepositoryRoot "config\discord-channel-organization.json"
}
if ([string]::IsNullOrWhiteSpace($GuildId)) {
    $GuildId = [Environment]::GetEnvironmentVariable("DISCORD_GUILD_ID", "User")
}
if ([string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = [Environment]::GetEnvironmentVariable("DISCORD_BOT_TOKEN", "User")
}
if (-not [string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = ([regex]::Replace($BotToken, "\p{C}", "")).Trim()
}
if ([string]::IsNullOrWhiteSpace($GuildId)) { throw "Set DISCORD_GUILD_ID or pass -GuildId." }
if ([string]::IsNullOrWhiteSpace($BotToken)) { throw "Set DISCORD_BOT_TOKEN or pass -BotToken." }
if (-not (Test-Path -LiteralPath $PlanPath)) { throw "Plan file not found: $PlanPath" }

$plan = Get-Content -LiteralPath $PlanPath -Raw -Encoding UTF8 | ConvertFrom-Json

function ConvertTo-JsonBodyFile {
    param([object]$Body)

    $tmp = [IO.Path]::GetTempFileName()
    $json = $Body | ConvertTo-Json -Depth 16
    [IO.File]::WriteAllText($tmp, $json, [Text.UTF8Encoding]::new($false))
    return $tmp
}

function Invoke-DiscordJson {
    param(
        [string]$Method,
        [string]$Path,
        [object]$Body = $null
    )

    $methodName = $Method.ToUpperInvariant()
    $uri = "https://discord.com/api/v10$Path"
    $args = @("-sS", "--connect-timeout", "8", "--max-time", "20", "-X", $methodName, "-H", "Authorization: Bot $BotToken", "-H", "Content-Type: application/json; charset=utf-8")
    $bodyFile = $null
    if ($null -ne $Body) {
        $bodyFile = ConvertTo-JsonBodyFile -Body $Body
        $args += @("--data-binary", "@$bodyFile")
    }
    $args += $uri

    try {
        $raw = & curl.exe @args
    } finally {
        if (-not [string]::IsNullOrWhiteSpace($bodyFile) -and (Test-Path -LiteralPath $bodyFile)) {
            Remove-Item -LiteralPath $bodyFile -Force
        }
    }

    if ($LASTEXITCODE -ne 0) { throw "curl.exe failed for $methodName $Path." }
    if ([string]::IsNullOrWhiteSpace($raw)) { return $null }
    $json = $raw | ConvertFrom-Json
    if ($json.PSObject.Properties.Name -contains "code" -and $json.PSObject.Properties.Name -contains "message" -and -not ($json.PSObject.Properties.Name -contains "id")) {
        throw "Discord API error for $methodName $Path`: $($json.message) ($($json.code))"
    }
    return $json
}

function Save-CategoryEnvironment {
    param(
        [string]$Prefix,
        [string]$Id,
        [string]$Name,
        [bool]$Enabled = $false
    )
    if (-not $Enabled -or [string]::IsNullOrWhiteSpace($Prefix)) { return }
    [Environment]::SetEnvironmentVariable("${Prefix}_ID", $Id, "User")
}

$channels = @(Invoke-DiscordJson -Method Get -Path "/guilds/$GuildId/channels")
$categoryByName = @{}
foreach ($channel in $channels) {
    if ($channel.type -eq 4) {
        $categoryByName[[string]$channel.name] = [string]$channel.id
    }
}

foreach ($rename in @($plan.categoryRenames)) {
    $existing = $channels | Where-Object { [string]$_.id -eq [string]$rename.id } | Select-Object -First 1
    if ($null -eq $existing) {
        Write-Warning "Category id $($rename.id) for '$($rename.name)' was not found."
        continue
    }

    if ([string]$existing.name -ne [string]$rename.name) {
        if ($Apply) {
            try {
                [void](Invoke-DiscordJson -Method Patch -Path "/channels/$($rename.id)" -Body ([ordered]@{ name = $rename.name }))
                Write-Host "Renamed category '$($existing.name)' -> '$($rename.name)'."
            } catch {
                Write-Warning "Could not rename category '$($existing.name)' -> '$($rename.name)': $($_.Exception.Message)"
            }
        } else {
            Write-Host "Would rename category '$($existing.name)' -> '$($rename.name)'."
        }
    } else {
        Write-Host "Category already named '$($rename.name)'."
    }
    $categoryByName[[string]$rename.name] = [string]$rename.id
    Save-CategoryEnvironment -Prefix ([string]$rename.envPrefix) -Id ([string]$rename.id) -Name ([string]$rename.name) -Enabled ([bool]$StoreInUserEnvironment)
}

foreach ($category in @($plan.ensureCategories)) {
    $name = [string]$category.name
    if ($categoryByName.ContainsKey($name)) {
        Write-Host "Found category '$name'."
        Save-CategoryEnvironment -Prefix ([string]$category.envPrefix) -Id ([string]$categoryByName[$name]) -Name $name -Enabled ([bool]$StoreInUserEnvironment)
        continue
    }

    if ($Apply) {
        try {
            $created = Invoke-DiscordJson -Method Post -Path "/guilds/$GuildId/channels" -Body ([ordered]@{
                name = $name
                type = 4
            })
            $categoryByName[$name] = [string]$created.id
            Write-Host "Created category '$name' with id $($created.id)."
            Save-CategoryEnvironment -Prefix ([string]$category.envPrefix) -Id ([string]$created.id) -Name $name -Enabled ([bool]$StoreInUserEnvironment)
        } catch {
            Write-Warning "Could not create category '$name': $($_.Exception.Message)"
        }
    } else {
        Write-Host "Would create category '$name'."
    }
}

foreach ($move in @($plan.moves)) {
    $targetName = [string]$move.category
    if (-not $categoryByName.ContainsKey($targetName)) {
        Write-Warning "Target category '$targetName' is not available for channel '$($move.name)'."
        continue
    }
    $targetId = [string]$categoryByName[$targetName]
    $channel = $channels | Where-Object { [string]$_.id -eq [string]$move.id } | Select-Object -First 1
    if ($null -eq $channel) {
        Write-Warning "Channel id $($move.id) '$($move.name)' was not found."
        continue
    }
    if ([string]$channel.parent_id -eq $targetId) {
        Write-Host "Channel '$($channel.name)' is already under '$targetName'."
        continue
    }

    if ($Apply) {
        try {
            [void](Invoke-DiscordJson -Method Patch -Path "/channels/$($channel.id)" -Body ([ordered]@{
                parent_id = $targetId
            }))
            Write-Host "Moved channel '$($channel.name)' -> '$targetName'."
        } catch {
            Write-Warning "Could not move channel '$($channel.name)' -> '$targetName': $($_.Exception.Message)"
        }
    } else {
        Write-Host "Would move channel '$($channel.name)' -> '$targetName'."
    }
}

if (-not $Apply) {
    Write-Host "Dry run only. Re-run with -Apply to change Discord."
}
