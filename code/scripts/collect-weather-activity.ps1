param(
    [string]$Date,
    [string]$RepositoryRoot,
    [string]$Latitude,
    [string]$Longitude,
    [string]$LocationLabel,
    [string]$Timezone = "Asia/Tokyo"
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}
if ([string]::IsNullOrWhiteSpace($Date)) {
    $Date = [DateTimeOffset]::UtcNow.ToOffset([TimeSpan]::FromHours(9)).ToString("yyyy-MM-dd")
}
if ([string]::IsNullOrWhiteSpace($Latitude)) {
    $Latitude = [Environment]::GetEnvironmentVariable("WEATHER_LATITUDE", "User")
}
if ([string]::IsNullOrWhiteSpace($Longitude)) {
    $Longitude = [Environment]::GetEnvironmentVariable("WEATHER_LONGITUDE", "User")
}
if ([string]::IsNullOrWhiteSpace($LocationLabel)) {
    $LocationLabel = [Environment]::GetEnvironmentVariable("WEATHER_LOCATION_LABEL", "User")
}
if ([string]::IsNullOrWhiteSpace($LocationLabel)) {
    $LocationLabel = "自宅周辺"
}

function Write-UnavailableWeather {
    param([string]$Reason)

    $outDir = Join-Path $RepositoryRoot "records\inbox\weather"
    if (-not (Test-Path -LiteralPath $outDir)) {
        New-Item -ItemType Directory -Path $outDir | Out-Null
    }

    $payload = @{
        date = $Date
        available = $false
        reason = $Reason
        location_label = $LocationLabel
        source = "Open-Meteo"
        collected_at = [DateTimeOffset]::UtcNow.ToString("o")
    }
    $outPath = Join-Path $outDir "$Date.json"
    $payload | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $outPath -Encoding UTF8
    Write-Warning $Reason
    Write-Host "Wrote unavailable weather record: $outPath"
}

function ConvertTo-InvariantDouble {
    param([string]$Value)

    $result = 0.0
    if ([double]::TryParse($Value, [Globalization.NumberStyles]::Float, [Globalization.CultureInfo]::InvariantCulture, [ref]$result)) {
        return $result
    }
    if ([double]::TryParse($Value, [Globalization.NumberStyles]::Float, [Globalization.CultureInfo]::CurrentCulture, [ref]$result)) {
        return $result
    }
    return $null
}

function Get-WeatherLabel {
    param([int]$Code)

    switch ($Code) {
        0 { return "快晴" }
        1 { return "晴れ" }
        2 { return "薄曇り" }
        3 { return "曇り" }
        45 { return "霧" }
        48 { return "霧氷/霧" }
        51 { return "弱い霧雨" }
        53 { return "霧雨" }
        55 { return "強い霧雨" }
        56 { return "弱い着氷性霧雨" }
        57 { return "着氷性霧雨" }
        61 { return "小雨" }
        63 { return "雨" }
        65 { return "強い雨" }
        66 { return "弱い着氷性雨" }
        67 { return "着氷性雨" }
        71 { return "小雪" }
        73 { return "雪" }
        75 { return "強い雪" }
        77 { return "雪粒" }
        80 { return "にわか雨" }
        81 { return "強いにわか雨" }
        82 { return "激しいにわか雨" }
        85 { return "にわか雪" }
        86 { return "強いにわか雪" }
        95 { return "雷雨" }
        96 { return "雷雨/小さい雹" }
        99 { return "雷雨/雹" }
        default { return "天気コード$Code" }
    }
}

function Format-Number {
    param(
        [Nullable[double]]$Value,
        [int]$Digits = 1
    )

    if ($null -eq $Value) { return "" }
    return ([double]$Value).ToString("F$Digits", [Globalization.CultureInfo]::InvariantCulture)
}

function Get-ValueAt {
    param(
        [object]$Array,
        [int]$Index
    )

    if ($null -eq $Array -or $Index -lt 0 -or $Index -ge $Array.Count) {
        return $null
    }
    return $Array[$Index]
}

$lat = ConvertTo-InvariantDouble -Value $Latitude
$lon = ConvertTo-InvariantDouble -Value $Longitude
if ($null -eq $lat -or $null -eq $lon) {
    Write-UnavailableWeather -Reason "WEATHER_LATITUDE / WEATHER_LONGITUDE is not configured."
    exit 0
}

$outDir = Join-Path $RepositoryRoot "records\inbox\weather"
if (-not (Test-Path -LiteralPath $outDir)) {
    New-Item -ItemType Directory -Path $outDir | Out-Null
}

$query = [ordered]@{
    latitude = $lat.ToString([Globalization.CultureInfo]::InvariantCulture)
    longitude = $lon.ToString([Globalization.CultureInfo]::InvariantCulture)
    hourly = "weather_code,temperature_2m,relative_humidity_2m,precipitation,rain,showers,cloud_cover,wind_speed_10m"
    daily = "temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max"
    timezone = $Timezone
    start_date = $Date
    end_date = $Date
}
$queryText = ($query.GetEnumerator() | ForEach-Object {
    [Uri]::EscapeDataString([string]$_.Key) + "=" + [Uri]::EscapeDataString([string]$_.Value)
}) -join "&"
$uri = "https://api.open-meteo.com/v1/forecast?$queryText"

try {
    $response = Invoke-RestMethod -Uri $uri -Method Get -TimeoutSec 30
} catch {
    Write-UnavailableWeather -Reason ("Weather API request failed: " + $_.Exception.Message)
    exit 0
}

if ($null -eq $response.hourly -or $null -eq $response.hourly.time -or $response.hourly.time.Count -eq 0) {
    Write-UnavailableWeather -Reason "Weather API returned no hourly data."
    exit 0
}

$hours = New-Object 'System.Collections.Generic.List[object]'
for ($i = 0; $i -lt $response.hourly.time.Count; $i++) {
    $codeValue = Get-ValueAt -Array $response.hourly.weather_code -Index $i
    if ($null -eq $codeValue) { continue }
    $timeText = [string](Get-ValueAt -Array $response.hourly.time -Index $i)
    if (-not $timeText.StartsWith($Date)) { continue }
    $code = [int]$codeValue
    $hours.Add([pscustomobject]@{
        time = $timeText
        hour = [int]([DateTime]::Parse($timeText, [Globalization.CultureInfo]::InvariantCulture).Hour)
        weather_code = $code
        weather = Get-WeatherLabel -Code $code
        temperature_c = Get-ValueAt -Array $response.hourly.temperature_2m -Index $i
        humidity_percent = Get-ValueAt -Array $response.hourly.relative_humidity_2m -Index $i
        precipitation_mm = Get-ValueAt -Array $response.hourly.precipitation -Index $i
        rain_mm = Get-ValueAt -Array $response.hourly.rain -Index $i
        showers_mm = Get-ValueAt -Array $response.hourly.showers -Index $i
        cloud_cover_percent = Get-ValueAt -Array $response.hourly.cloud_cover -Index $i
        wind_speed_kmh = Get-ValueAt -Array $response.hourly.wind_speed_10m -Index $i
    })
}

if ($hours.Count -eq 0) {
    Write-UnavailableWeather -Reason "Weather API returned no hourly data for $Date."
    exit 0
}

$segments = New-Object 'System.Collections.Generic.List[object]'
$current = $null
foreach ($hour in ($hours | Sort-Object hour)) {
    if ($null -eq $current -or $current.weather_code -ne $hour.weather_code) {
        if ($null -ne $current) { $segments.Add($current) }
        $precipitation = if ($null -eq $hour.precipitation_mm) { 0.0 } else { [double]$hour.precipitation_mm }
        $current = [pscustomobject]@{
            start_hour = $hour.hour
            end_hour = $hour.hour
            weather_code = $hour.weather_code
            weather = $hour.weather
            precipitation_mm = $precipitation
            temperatures = New-Object 'System.Collections.Generic.List[double]'
        }
    } else {
        $current.end_hour = $hour.hour
        if ($null -ne $hour.precipitation_mm) {
            $current.precipitation_mm += [double]$hour.precipitation_mm
        }
    }
    if ($null -ne $hour.temperature_c) {
        $current.temperatures.Add([double]$hour.temperature_c)
    }
}
if ($null -ne $current) { $segments.Add($current) }

$segmentTexts = New-Object 'System.Collections.Generic.List[string]'
foreach ($segment in $segments) {
    $range = if ($segment.start_hour -eq $segment.end_hour) {
        "{0:00}時" -f $segment.start_hour
    } else {
        "{0:00}-{1:00}時" -f $segment.start_hour, $segment.end_hour
    }
    $tempText = ""
    if ($segment.temperatures.Count -gt 0) {
        $tempMin = ($segment.temperatures | Measure-Object -Minimum).Minimum
        $tempMax = ($segment.temperatures | Measure-Object -Maximum).Maximum
        $tempText = " / " + (Format-Number -Value $tempMin) + "-" + (Format-Number -Value $tempMax) + "℃"
    }
    $rainText = ""
    if ([double]$segment.precipitation_mm -gt 0) {
        $rainText = " / 降水" + (Format-Number -Value ([double]$segment.precipitation_mm)) + "mm"
    }
    $segmentTexts.Add("$range $($segment.weather)$tempText$rainText")
}

$temps = @($hours | Where-Object { $null -ne $_.temperature_c } | ForEach-Object { [double]$_.temperature_c })
$precip = @($hours | Where-Object { $null -ne $_.precipitation_mm } | ForEach-Object { [double]$_.precipitation_mm })
$winds = @($hours | Where-Object { $null -ne $_.wind_speed_kmh } | ForEach-Object { [double]$_.wind_speed_kmh })
$tempMinDay = if ($temps.Count -gt 0) { ($temps | Measure-Object -Minimum).Minimum } else { $null }
$tempMaxDay = if ($temps.Count -gt 0) { ($temps | Measure-Object -Maximum).Maximum } else { $null }
$precipSum = if ($precip.Count -gt 0) { ($precip | Measure-Object -Sum).Sum } else { 0.0 }
$windMax = if ($winds.Count -gt 0) { ($winds | Measure-Object -Maximum).Maximum } else { $null }

$transitionText = ($segmentTexts.ToArray() -join " → ")
$weatherCounts = @{}
foreach ($hour in $hours) {
    $label = [string]$hour.weather
    if ([string]::IsNullOrWhiteSpace($label)) { continue }
    if (-not $weatherCounts.ContainsKey($label)) { $weatherCounts[$label] = 0 }
    $weatherCounts[$label]++
}
$dominantWeather = @($weatherCounts.GetEnumerator() | Sort-Object Value -Descending | Select-Object -First 1)
$weatherLabel = if ($dominantWeather.Count -gt 0) { [string]$dominantWeather[0].Key } else { "" }
if ([string]::IsNullOrWhiteSpace($weatherLabel)) {
    $weatherLabel = (($segments | ForEach-Object { $_.weather } | Where-Object { -not [string]::IsNullOrWhiteSpace($_) } | Select-Object -First 1) -join "")
}
if (-not [string]::IsNullOrWhiteSpace($weatherLabel) -and $segments.Count -gt 1) {
    $weatherLabel += "中心"
}
if (-not [string]::IsNullOrWhiteSpace($weatherLabel) -and [double]$precipSum -gt 0 -and $weatherLabel -notmatch "雨|雪|霧雨") {
    $weatherLabel += "（一時降水）"
}
$summary = if ([string]::IsNullOrWhiteSpace($weatherLabel)) { "天気記録あり" } else { "天気 " + $weatherLabel }
if ($null -ne $tempMinDay -and $null -ne $tempMaxDay) {
    $summary += " / 気温 " + (Format-Number -Value $tempMinDay) + "-" + (Format-Number -Value $tempMaxDay) + "℃"
}
$summary += " / 降水 " + (Format-Number -Value ([double]$precipSum)) + "mm"
if ($null -ne $windMax) {
    $summary += " / 最大風速 " + (Format-Number -Value $windMax) + "km/h"
}

$segmentRecords = New-Object 'System.Collections.Generic.List[object]'
foreach ($segment in $segments) {
    $segmentTempMin = $null
    $segmentTempMax = $null
    if ($segment.temperatures.Count -gt 0) {
        $segmentTempMin = ($segment.temperatures | Measure-Object -Minimum).Minimum
        $segmentTempMax = ($segment.temperatures | Measure-Object -Maximum).Maximum
    }
    $segmentRecords.Add(@{
        start = "{0:00}:00" -f $segment.start_hour
        end = "{0:00}:59" -f $segment.end_hour
        weather = $segment.weather
        weather_code = $segment.weather_code
        precipitation_mm = [double]$segment.precipitation_mm
        temperature_min_c = $segmentTempMin
        temperature_max_c = $segmentTempMax
    })
}

$payload = @{}
$payload["date"] = $Date
$payload["available"] = $true
$payload["location_label"] = $LocationLabel
$payload["source"] = "Open-Meteo Forecast API"
$payload["source_url"] = "https://open-meteo.com/"
$payload["timezone"] = $Timezone
$payload["collected_at"] = [DateTimeOffset]::UtcNow.ToString("o")
$payload["summary"] = $summary
$payload["transition"] = $transitionText
$payload["temperature_min_c"] = $tempMinDay
$payload["temperature_max_c"] = $tempMaxDay
$payload["precipitation_sum_mm"] = [double]$precipSum
$payload["wind_speed_max_kmh"] = $windMax
$payload["segments"] = @($segmentRecords.ToArray())
$payload["hourly"] = @($hours.ToArray())

$outPath = Join-Path $outDir "$Date.json"
$payload | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $outPath -Encoding UTF8
Write-Host "Weather summary: $summary"
Write-Host "Wrote weather record: $outPath"





