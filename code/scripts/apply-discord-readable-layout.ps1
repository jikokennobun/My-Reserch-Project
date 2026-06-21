param(
    [string]$GuildId = $env:DISCORD_GUILD_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [switch]$Apply,
    [switch]$StoreInUserEnvironment,
    [switch]$PostGuideMessages
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

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

function ConvertTo-JsonBodyFile {
    param([object]$Body)

    $tmp = [IO.Path]::GetTempFileName()
    $json = $Body | ConvertTo-Json -Depth 24
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
    $args = @(
        "-sS",
        "--connect-timeout", "8",
        "--max-time", "20",
        "-X", $methodName,
        "-H", "Authorization: Bot $BotToken",
        "-H", "Content-Type: application/json; charset=utf-8"
    )
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

function Set-UserEnvIfRequested {
    param([string]$Name, [string]$Value)

    if (-not $StoreInUserEnvironment -or [string]::IsNullOrWhiteSpace($Name)) { return }
    [Environment]::SetEnvironmentVariable($Name, $Value, "User")
}

function Convert-DisplayNameSeparator {
    param(
        [string]$Name,
        [switch]$TextChannel
    )

    if ([string]::IsNullOrWhiteSpace($Name)) { return $Name }
    if ($Name -match "^([^・]+)・(.+)$") {
        $separator = if ($TextChannel) { "" } else { " " }
        return "$($Matches[1])$separator$($Matches[2])"
    }
    return $Name
}

function Rename-Channel {
    param(
        [object]$Channel,
        [string]$TargetName,
        [string]$Topic = "",
        [string]$IdEnv = "",
        [string]$NameEnv = ""
    )

    if ($null -eq $Channel) { return }
    $isTextLike = ($Channel.type -eq 0 -or $Channel.type -eq 5 -or $Channel.type -eq 15)
    $TargetName = Convert-DisplayNameSeparator -Name $TargetName -TextChannel:$isTextLike
    Set-UserEnvIfRequested -Name $IdEnv -Value ([string]$Channel.id)
    Set-UserEnvIfRequested -Name $NameEnv -Value $TargetName

    $body = [ordered]@{}
    if ([string]$Channel.name -ne $TargetName) { $body.name = $TargetName }
    if (-not [string]::IsNullOrWhiteSpace($Topic) -and ($Channel.type -eq 0 -or $Channel.type -eq 5 -or $Channel.type -eq 15)) {
        $body.topic = $Topic
    }

    if ($body.Count -eq 0) {
        Write-Host "Already named '$TargetName'."
        return
    }

    if ($Apply) {
        try {
            [void](Invoke-DiscordJson -Method Patch -Path "/channels/$($Channel.id)" -Body $body)
            Write-Host "Updated '$($Channel.name)' -> '$TargetName'."
        } catch {
            Write-Warning "Could not update '$($Channel.name)' -> '$TargetName': $($_.Exception.Message)"
        }
    } else {
        Write-Host "Would update '$($Channel.name)' -> '$TargetName'."
    }
}

function Ensure-TextChannel {
    param(
        [object[]]$Channels,
        [string]$Name,
        [string[]]$Aliases = @(),
        [string]$ParentId,
        [string]$Topic,
        [string]$GuideMessage = "",
        [string]$Marker = ""
    )

    $originalName = $Name
    $Name = Convert-DisplayNameSeparator -Name $Name -TextChannel
    $legacyHyphenNames = New-Object 'System.Collections.Generic.List[string]'
    foreach ($candidate in @($originalName) + @($Aliases)) {
        $candidateText = [string]$candidate
        if ($candidateText -match "^([^・]+)・(.+)$") {
            $legacyHyphenNames.Add("$($Matches[1])-$($Matches[2])") | Out-Null
        }
    }
    $Aliases = @(
        @($Aliases) + @($originalName) + @($legacyHyphenNames.ToArray()) + @($Aliases | ForEach-Object { Convert-DisplayNameSeparator -Name ([string]$_) -TextChannel })
    ) | Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) } | Select-Object -Unique

    $channel = $null
    foreach ($candidate in @($Name) + @($Aliases)) {
        if ([string]::IsNullOrWhiteSpace($candidate)) { continue }
        $channel = $Channels | Where-Object { $_.type -eq 0 -and [string]$_.name -eq $candidate } | Select-Object -First 1
        if ($null -ne $channel) { break }
    }

    if ($null -eq $channel) {
        if ($Apply) {
            $body = [ordered]@{ name = $Name; type = 0; topic = $Topic }
            if (-not [string]::IsNullOrWhiteSpace($ParentId)) { $body.parent_id = $ParentId }
            $channel = Invoke-DiscordJson -Method Post -Path "/guilds/$GuildId/channels" -Body $body
            Write-Host "Created '$Name'."
        } else {
            Write-Host "Would create '$Name'."
            return $null
        }
    } else {
        Rename-Channel -Channel $channel -TargetName $Name -Topic $Topic
    }

    if ($Apply -and $PostGuideMessages -and -not [string]::IsNullOrWhiteSpace($GuideMessage)) {
        $alreadyPosted = $false
        if (-not [string]::IsNullOrWhiteSpace($Marker)) {
            try {
                $messages = @(Invoke-DiscordJson -Method Get -Path "/channels/$($channel.id)/messages?limit=25")
                $alreadyPosted = $null -ne ($messages | Where-Object { [string]$_.content -like "*$Marker*" } | Select-Object -First 1)
            } catch {
                $alreadyPosted = $false
            }
        }
        if (-not $alreadyPosted) {
            [void](Invoke-DiscordJson -Method Post -Path "/channels/$($channel.id)/messages" -Body ([ordered]@{ content = $GuideMessage }))
            Write-Host "Posted guide message to '$Name'."
        }
    }

    return $channel
}

$channels = @(Invoke-DiscordJson -Method Get -Path "/guilds/$GuildId/channels")
$byId = @{}
foreach ($channel in $channels) {
    $byId[[string]$channel.id] = $channel
}

$categorySpecs = @(
    @{ Id = "1514540748232720495"; Name = "🚪・雑談・入口"; IdEnv = "DISCORD_GENERAL_CATEGORY_ID"; NameEnv = "DISCORD_GENERAL_CATEGORY_NAME" },
    @{ Id = "1515810076999422122"; Name = "📔・日報・月次"; IdEnv = "DISCORD_DAILY_REPORT_CATEGORY_ID"; NameEnv = "DISCORD_DAILY_REPORT_CATEGORY_NAME" },
    @{ Id = "1516906267400999013"; Name = "🧾・生活ログ"; IdEnv = "DISCORD_LIFE_LOG_CATEGORY_ID"; NameEnv = "DISCORD_LIFE_LOG_CATEGORY_NAME" },
    @{ Id = "1516906330655293470"; Name = "AI・自動化"; IdEnv = "DISCORD_AI_AUTOMATION_CATEGORY_ID"; NameEnv = "DISCORD_AI_AUTOMATION_CATEGORY_NAME" },
    @{ Id = "1517192623062913106"; Name = "📰・AI・数学ニュース"; IdEnv = "DISCORD_NEWS_CATEGORY_ID"; NameEnv = "DISCORD_NEWS_CATEGORY_NAME" },
    @{ Id = "1515853497176817763"; Name = "🔔・通知・予定"; IdEnv = "DISCORD_MAIL_ANNOUNCEMENT_CATEGORY_ID"; NameEnv = "DISCORD_MAIL_ANNOUNCEMENT_CATEGORY_NAME" },
    @{ Id = "1515294260440731809"; Name = "🧠・研究関連"; IdEnv = "DISCORD_RESEARCH_CATEGORY_ID"; NameEnv = "DISCORD_RESEARCH_CATEGORY_NAME" },
    @{ Id = "1516164506554863767"; Name = "🎓・大学・仕事"; IdEnv = "DISCORD_UNIVERSITY_WORK_CATEGORY_ID"; NameEnv = "DISCORD_UNIVERSITY_WORK_CATEGORY_NAME" },
    @{ Id = "1515858169526620270"; Name = "🎨・趣味・創作"; IdEnv = "DISCORD_HOBBY_CREATIVE_CATEGORY_ID"; NameEnv = "DISCORD_HOBBY_CREATIVE_CATEGORY_NAME" },
    @{ Id = "1515859982711656509"; Name = "🌐・SNS・外部"; IdEnv = "DISCORD_SNS_EXTERNAL_CATEGORY_ID"; NameEnv = "DISCORD_SNS_EXTERNAL_CATEGORY_NAME" },
    @{ Id = "1514542190876037170"; Name = "📝・下書き"; IdEnv = "DISCORD_DRAFT_CATEGORY_ID"; NameEnv = "DISCORD_DRAFT_CATEGORY_NAME" },
    @{ Id = "1514540748232720496"; Name = "🎙️・ボイス"; IdEnv = "DISCORD_VOICE_CATEGORY_ID"; NameEnv = "DISCORD_VOICE_CATEGORY_NAME" }
)

foreach ($spec in $categorySpecs) {
    if ($byId.ContainsKey([string]$spec.Id)) {
        Rename-Channel -Channel $byId[[string]$spec.Id] -TargetName ([string]$spec.Name) -IdEnv ([string]$spec.IdEnv) -NameEnv ([string]$spec.NameEnv)
    }
}

$entryCategoryId = if ($byId.ContainsKey("1514540748232720495")) { "1514540748232720495" } else { "" }

$rulesMessage = @(
    "**このサーバーの使い方**",
    "",
    "- 生活の記録、研究メモ、日報素材、通知を分けて置く。",
    "- 個人情報・秘密鍵・APIキー・Webhook URLは投稿しない。",
    "- 日報素材は細かくてOK。あとでBotとCodexが拾う。",
    "- 研究メモは未完成でOK。後からObsidianに整理する。",
    "- Botが変な動きをしたら、自己満足文かcodex-commandではなく、この入口側で止める/相談する。",
    "",
    "<!--codex-rules-guide-v1-->"
) -join "`n"

$channelsRolesMessage = @(
    "**チャンネル&ロール案内**",
    "",
    "主要カテゴリ:",
    "- 🚪 雑談・入口: rules、案内、普通の雑談",
    "- 🧾 生活ログ: 食事、起床、気分、活動、視聴などの日報素材",
    "- AI 自動化: 自己満足文、Codex命令、Botテスト",
    "- 🔔 通知・予定: メール、予定、締切タイムライン",
    "- 🧠 研究関連: 数学メモ、preprint、研究成果、私的議論",
    "- 🎓 大学・仕事: 課題、大学の勉強、インターン情報",
    "- 🎨 趣味・創作: アニメ、小説、試作品、アイデア、DTM/音楽制作",
    "- 🌐 SNS・外部: X/Twitterや外部サーバー由来のメモ",
    "",
    "ロール運用は、通知が増えてきたら `通知:大学` / `通知:塾` / `研究` / `生活ログ` のように分ける。",
    "Discord公式の「チャンネル&ロール」画面はサーバー設定側で手動調整が必要な場合がある。",
    "",
    "<!--codex-channel-role-guide-v1-->"
) -join "`n"

[void](Ensure-TextChannel -Channels $channels -Name "📜・rules" -Aliases @("rules", "rulus", "ルール") -ParentId $entryCategoryId -Topic "サーバー全体のルールと運用方針。" -GuideMessage $rulesMessage -Marker "codex-rules-guide-v1")
[void](Ensure-TextChannel -Channels $channels -Name "🧭・チャンネルとロール" -Aliases @("チャンネル&ロール", "channels-and-roles", "channel-and-roles") -ParentId $entryCategoryId -Topic "各チャンネルの用途と通知ロールの案内。" -GuideMessage $channelsRolesMessage -Marker "codex-channel-role-guide-v1")

$channelSpecs = @(
    @{ Id = "1514540748232720497"; Name = "💬・一般"; Topic = "雑談、入口、まだ置き場が決まっていない話。" },
    @{ Id = "1514540748232720498"; Name = "🎙️・一般"; Topic = "" },
    @{ Id = "1515930089982791690"; Name = "🔔・カレンダー通知"; Topic = "Google CalendarとDiscord scheduled eventから作る予定通知。" ; IdEnv = "DISCORD_CALENDAR_CHANNEL_ID"; NameEnv = "DISCORD_CALENDAR_CHANNEL_NAME" },
    @{ Id = "1516582846846734376"; Name = "🧾・活動ログ"; Topic = "日報素材になる日中の活動メモ。タイムスタンプ付きで拾う。" ; IdEnv = "DISCORD_ACTIVITY_CHANNEL_ID"; NameEnv = "DISCORD_ACTIVITY_CHANNEL_NAME" },
    @{ Id = "1516511507804848139"; Name = "✅・やった"; Topic = "完了したこと、成果、達成ログ。" },
    @{ Id = "1515866211559145482"; Name = "💭・思った"; Topic = "今日思ったこと、感想、短い内省。" },
    @{ Id = "1515825949055127625"; Name = "🍽️・食"; Topic = "食事画像と食事メモ。日報にタイムスタンプ付きで入る。" ; IdEnv = "DISCORD_FOOD_CHANNEL_ID"; NameEnv = "DISCORD_FOOD_CHANNEL_NAME" },
    @{ Id = "1515841392075866294"; Name = "🎬・視聴ログ"; Topic = "見た動画、アニメ、配信、講義URL。タイトルとチャンネル名も補完する。" ; IdEnv = "DISCORD_WATCH_CHANNEL_ID"; NameEnv = "DISCORD_WATCH_CHANNEL_NAME" },
    @{ Id = "1515930094927872131"; Name = "📌・見たいもの"; Topic = "見たい動画、読みたい記事、欲しいもの、あとで確認したいもの。" ; IdEnv = "DISCORD_WATCHLIST_CHANNEL_ID"; NameEnv = "DISCORD_WATCHLIST_CHANNEL_NAME" },
    @{ Id = "1515844263173165298"; Name = "🌗・気分ログ"; Topic = "朝昼晩の気分、点数、短い理由。" ; IdEnv = "DISCORD_MOOD_CHANNEL_ID"; NameEnv = "DISCORD_MOOD_CHANNEL_NAME" },
    @{ Id = "1515844267698819223"; Name = "🌅・起床ログ"; Topic = "起床・睡眠・活動開始の記録。" ; IdEnv = "DISCORD_WAKE_CHANNEL_ID"; NameEnv = "DISCORD_WAKE_CHANNEL_NAME" },
    @{ Id = "1515844270991343667"; Name = "🪞・振り返り"; Topic = "夜の振り返り、今日のよかったこと、明日に回すこと。" ; IdEnv = "DISCORD_REFLECTION_CHANNEL_ID"; NameEnv = "DISCORD_REFLECTION_CHANNEL_NAME" },
    @{ Id = "1515860953558810634"; Name = "ai・codex-command"; Topic = "Codexへの簡易命令。!todo、!watch、!mood、!researchなど。" ; IdEnv = "DISCORD_COMMAND_CHANNEL_ID"; NameEnv = "DISCORD_COMMAND_CHANNEL_NAME" },
    @{ Id = "1516169109409104075"; Name = "ai・ai-chat"; Topic = "旧AIチャット/テスト用。通常は自己満足文を使う。" },
    @{ Id = "1516830527687098388"; Name = "ir・自己満足文"; Topic = "数学的ぼやき、研究相談、短いAI会話。OpenAI modeならここで自動返信。" ; IdEnv = "DISCORD_AI_CHAT_CHANNEL_ID"; NameEnv = "DISCORD_AI_CHAT_CHANNEL_NAME" },
    @{ Id = "1515853501790556301"; Name = "🔔・大学メール通知"; Topic = "大学メール由来の課題、締切、履修、面談などの通知。" ; IdEnv = "DISCORD_UNIVERSITY_MAIL_CHANNEL_ID"; NameEnv = "DISCORD_UNIVERSITY_MAIL_CHANNEL_NAME" },
    @{ Id = "1515853510988796046"; Name = "🔔・塾講師メール通知"; Topic = "塾講師バイト用メール由来のシフト、返信、確認などの通知。" ; IdEnv = "DISCORD_TUTORING_MAIL_CHANNEL_ID"; NameEnv = "DISCORD_TUTORING_MAIL_CHANNEL_NAME" },
    @{ Id = "1516169206004187388"; Name = "🔔・mail-timeline"; Topic = "大学/塾メール由来の今日やることタイムライン。" ; IdEnv = "DISCORD_MAIL_TIMELINE_CHANNEL_ID"; NameEnv = "DISCORD_MAIL_TIMELINE_CHANNEL_NAME" },
    @{ Id = "1515294310247960576"; Name = "📝・memo"; Topic = "研究・数学まわりの軽いメモ置き場。" },
    @{ Id = "1515812956095385610"; Name = "✨・最近の興味"; Topic = "最近気になっている主題、読みたい方向性、調査候補。" },
    @{ Id = "1515844491414605904"; Name = "📄・preprint"; Topic = "preprint、論文URL、読むべき文献候補。" },
    @{ Id = "1515873183545294928"; Name = "🏁・研究成果"; Topic = "形になった研究成果、証明、まとめ、公開物。" },
    @{ Id = "1516841301117632523"; Name = "🔒・私的議論"; Topic = "privateな研究議論や未公開メモ。" },
    @{ Id = "1514542756092055673"; Name = "🧮・comm-math-for-ai"; Topic = "AIと数学コミュニケーション関連。" },
    @{ Id = "1515262028586025061"; Name = "📚・下剋上院進"; Topic = "院進、勉強、下剋上関連の素材。" },
    @{ Id = "1515436298779754656"; Name = "🎓・大学の勉強"; Topic = "大学講義、勉強、理解メモ。" },
    @{ Id = "1516164653670207620"; Name = "📚・課題"; Topic = "大学課題、提出物、締切。" },
    @{ Id = "1515870405221683350"; Name = "💼・インターン情報"; Topic = "インターン、就活、応募、面談情報。" },
    @{ Id = "1515873340416331796"; Name = "🧪・試作品"; Topic = "試作、プロトタイプ、作品の途中経過。" },
    @{ Id = "1515873538362441829"; Name = "💡・アイデア"; Topic = "創作・研究・自動化のアイデア。" },
    @{ Id = "1517874899891519505"; Name = "🎹・DTM"; Topic = "DTM、音楽制作、作曲、音素材、制作メモ。" },
    @{ Id = "1515870553016238290"; Name = "📺・アニメ"; Topic = "見たアニメ、見たいアニメ、感想。" },
    @{ Id = "1515870703608401920"; Name = "📖・小説"; Topic = "小説、プロット、読書、創作メモ。" },
    @{ Id = "1515863956286341160"; Name = "✍️・tweet-memo"; Topic = "X/Twitter投稿候補、SNSメモ。" },
    @{ Id = "1515935242463088690"; Name = "↪️・転送"; Topic = "外部から転送したメモやログ。" },
    @{ Id = "1515850076126449806"; Name = "🌐・others"; Topic = "分類未定の外部/SNS系メモ。" },
    @{ Id = "1517192687101546697"; Name = "📰・ai-news"; Topic = "AIニュース、モデル公開、ツール更新、政策変更。" ; IdEnv = "DISCORD_AI_NEWS_CHANNEL_ID"; NameEnv = "DISCORD_AI_NEWS_CHANNEL_NAME" },
    @{ Id = "1517193050105843875"; Name = "📰・math-news"; Topic = "数学ニュース、論文、セミナー、サーベイ。" ; IdEnv = "DISCORD_MATH_NEWS_CHANNEL_ID"; NameEnv = "DISCORD_MATH_NEWS_CHANNEL_NAME" }
)

foreach ($spec in $channelSpecs) {
    if ($byId.ContainsKey([string]$spec.Id)) {
        Rename-Channel -Channel $byId[[string]$spec.Id] -TargetName ([string]$spec.Name) -Topic ([string]$spec.Topic) -IdEnv ([string]$spec.IdEnv) -NameEnv ([string]$spec.NameEnv)
    } else {
        Write-Warning "Channel id $($spec.Id) for '$($spec.Name)' was not found."
    }
}

if (-not $Apply) {
    Write-Host "Dry run only. Re-run with -Apply to change Discord."
}
