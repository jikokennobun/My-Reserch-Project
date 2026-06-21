param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$Username = "jikokennobun",
    [string]$BearerToken = $env:X_BEARER_TOKEN,
    [switch]$FetchApi,
    [string]$Text,
    [string]$Url,
    [string]$Kind = "manual",
    [string]$TimeZoneOffset = "+09:00",
    [string]$RepositoryRoot,
    [string]$OutPath
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}
if ([string]::IsNullOrWhiteSpace($OutPath)) {
    $OutPath = Join-Path $RepositoryRoot "records\inbox\twitter\$Date.jsonl"
}

if ([string]::IsNullOrWhiteSpace($BearerToken)) {
    $BearerToken = [Environment]::GetEnvironmentVariable("X_BEARER_TOKEN", "User")
}
if (-not [string]::IsNullOrWhiteSpace($BearerToken)) {
    $BearerToken = ([regex]::Replace($BearerToken, "\p{C}", "")).Trim()
}

function ConvertTo-JsonLine {
    param([object]$Value)
    return ($Value | ConvertTo-Json -Depth 16 -Compress)
}

function Invoke-XApiJson {
    param(
        [string]$Url,
        [string]$Token
    )

    $raw = & curl.exe -sS -H "Authorization: Bearer $Token" $Url
    if ($LASTEXITCODE -ne 0) { throw "curl.exe failed for X API." }
    $json = $raw | ConvertFrom-Json
    if ($json.PSObject.Properties.Name -contains "errors") {
        throw "X API error: $($raw)"
    }
    return $json
}

$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }

$records = New-Object 'System.Collections.Generic.List[object]'

if ($FetchApi) {
    if ([string]::IsNullOrWhiteSpace($BearerToken)) {
        throw "Set X_BEARER_TOKEN or pass -BearerToken to use -FetchApi."
    }

    $bases = @("https://api.x.com/2", "https://api.twitter.com/2")
    $user = $null
    $baseUsed = $null
    foreach ($base in $bases) {
        try {
            $encodedUser = [Uri]::EscapeDataString($Username)
            $userResponse = Invoke-XApiJson -Url "$base/users/by/username/$encodedUser" -Token $BearerToken
            if ($null -ne $userResponse.data.id) {
                $user = $userResponse.data
                $baseUsed = $base
                break
            }
        } catch {
            $user = $null
        }
    }
    if ($null -eq $user) {
        throw "Could not resolve X username @$Username. Check X_BEARER_TOKEN and API access."
    }

    $start = [DateTimeOffset]::Parse("$Date`T00:00:00$TimeZoneOffset").ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    $end = ([DateTimeOffset]::Parse("$Date`T00:00:00$TimeZoneOffset")).AddDays(1).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    $pagination = $null

    do {
        $urlParts = New-Object 'System.Collections.Generic.List[string]'
        $urlParts.Add("max_results=100")
        $urlParts.Add("start_time=$([Uri]::EscapeDataString($start))")
        $urlParts.Add("end_time=$([Uri]::EscapeDataString($end))")
        $urlParts.Add("tweet.fields=created_at,conversation_id,public_metrics,referenced_tweets")
        if (-not [string]::IsNullOrWhiteSpace($pagination)) {
            $urlParts.Add("pagination_token=$([Uri]::EscapeDataString($pagination))")
        }
        $tweetsUrl = "$baseUsed/users/$($user.id)/tweets?" + (($urlParts | ForEach-Object { $_ }) -join "&")
        $tweetResponse = Invoke-XApiJson -Url $tweetsUrl -Token $BearerToken
        foreach ($tweet in @($tweetResponse.data)) {
            $records.Add([ordered]@{
                date = $Date
                timestamp = $tweet.created_at
                source = "x-api"
                username = $Username
                kind = "post"
                id = $tweet.id
                text = $tweet.text
                url = "https://x.com/$Username/status/$($tweet.id)"
                public_metrics = $tweet.public_metrics
            })
        }
        $pagination = $tweetResponse.meta.next_token
    } while (-not [string]::IsNullOrWhiteSpace($pagination))
}

if (-not [string]::IsNullOrWhiteSpace($Text) -or -not [string]::IsNullOrWhiteSpace($Url)) {
    $records.Add([ordered]@{
        date = $Date
        timestamp = (Get-Date).ToString("o")
        source = "manual"
        username = $Username
        kind = $Kind
        text = $Text
        url = $Url
    })
}

if ($records.Count -eq 0) {
    Write-Host "No Twitter/X activity queued. Use -FetchApi with X_BEARER_TOKEN or pass -Text/-Url."
    exit 0
}

foreach ($record in $records) {
    ConvertTo-JsonLine -Value $record | Add-Content -LiteralPath $OutPath -Encoding UTF8
}

Write-Host "Queued $($records.Count) Twitter/X activity record(s): $OutPath"
