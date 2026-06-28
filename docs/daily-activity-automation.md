# Daily Activity Automation

This document defines the daily-report inputs and the current automation level.

## Current Sources

| Source | Status | Notes |
| --- | --- | --- |
| Obsidian research notes | Automatic | `code/scripts/index-obsidian-research.ps1` indexes research-related folders only. |
| Repository activity | Automatic | `code/scripts/new-daily-report.ps1` includes Git status and research log tail. |
| Monthly daily channels | Automatic | `code/scripts/ensure-discord-monthly-daily-channel.ps1` creates/uses monthly channels such as `2026-6` and updates the daily webhook. |
| Wake-up time | Automatic estimate | `new-daily-report.ps1` fills blank `起床` from the earliest reliable activity timestamp, preserving an existing value. |
| Todo | Automatic | `records/tasks/todo.md` is included in the daily source packet. |
| Discord daily channel | Bot required | `code/scripts/export-discord-channel-messages.ps1` can export messages after `DISCORD_BOT_TOKEN` and `DISCORD_DAILY_CHANNEL_ID` are set. |
| Discord command bot | Bot required | `code/scripts/process-discord-codex-commands.ps1` turns `!todo`, `!watch`, `!mood`, and `!research` posts into local Markdown/JSONL records. |
| Discord AI chat | Event-driven queue / optional API | `code/scripts/watch-discord-message-events.ps1` detects `自己満足文` posts as Discord Gateway events. `QueueOnly` mode has no API billing and queues replies for Codex/manual handling; `OpenAI` mode replies immediately through the paid OpenAI API. |
| External Discord servers | Bot required | `code/scripts/export-discord-external-activity.ps1` records readable servers except the primary `DISCORD_GUILD_ID`. |
| Discord data package | Manual export | `code/scripts/import-discord-data-package.ps1` imports your own Discord data export when a bot cannot be invited. |
| Discord posting | Configured | Daily and research webhooks are stored in the Windows user environment, not in Git. |
| Food photos | Bot required | Images posted in the food channel are downloaded into the Obsidian daily-report attachment folder and embedded in the detailed daily report. |
| Watch log | Bot required | `code/scripts/export-discord-watch-activity.ps1` captures anime, video, stream, and lecture posts from the Discord watch-log channel. |
| Watchlist | Bot required | `code/scripts/export-discord-watchlist-activity.ps1` captures unwatched or want-to-watch items from the `見たいもの` channel. |
| Video metadata | Automatic | `code/scripts/enrich-video-metadata.ps1` adds YouTube titles and channel names to watch-log and YouTube inbox records when oEmbed is available. |
| Wake log | Bot required | `code/scripts/export-discord-log-channel.ps1 -LogKind wake` captures wake/sleep posts from `起床ログ`; this is preferred over inferred wake time. |
| Mood log | Bot required | `code/scripts/export-discord-log-channel.ps1 -LogKind mood` captures morning/noon/night mood posts from `気分ログ`. |
| Reflection log | Deprecated | Separate life-log reflection is no longer part of the daily report contract because it overlaps with the daily report's own reflection prose. |
| Twitter/X | Optional API/manual | `code/scripts/import-twitter-activity.ps1` can queue manual records or fetch via X API when `X_BEARER_TOKEN` is available. |
| Generated AI activity | Manual/API-ready | `code/scripts/import-ai-activity.ps1` queues Codex, ChatGPT, Claude, Gemini, or other AI-session summaries. |
| Gmail task mail | Label/export based | Gmail labels `Codex/大学タスク` and `Codex/塾講師タスク` are exported by `code/apps-script/gmail-university-task-export.gs`, then imported by `code/scripts/import-gmail-task-export.ps1`. |
| Gmail announcements | Automatic after import | `code/scripts/post-gmail-task-announcements.ps1` posts short task notices to the dedicated Discord mail channels. |
| Mail deadline reminders | Automatic after import | `code/scripts/sync-mail-deadline-reminders.ps1` writes an Obsidian deadline list and can post 3-day/1-day/today reminders to Discord. |
| Mail action timeline | Automatic after import | `code/scripts/new-mail-action-timeline.ps1` combines new Gmail candidates and detected deadlines into a compact Discord timeline and Obsidian note. |
| Calendar events | Optional iCal/API | `code/scripts/sync-calendar-notifications.ps1` imports Google Calendar iCal events when `GOOGLE_CALENDAR_ICAL_URL` is configured and reads Discord scheduled events. |
| Weather | Automatic after setup | `code/scripts/collect-weather-activity.ps1` fetches hourly Open-Meteo weather for `WEATHER_LATITUDE` / `WEATHER_LONGITUDE` and fills the daily report's `天気` line plus `天気の移り変わり`. |
| ChatGPT Pro ideas | Export/manual | `code/scripts/import-chatgpt-pro-ideas.ps1` imports ChatGPT export ZIPs, copied notes, or manual snippets into research idea candidates. |
| YouTube videos | Semi-automatic | Add watched URLs with `code/scripts/import-youtube-activity.ps1`; captions can be fetched if `yt-dlp` is installed. |
| TODO candidates | Automatic | `code/scripts/extract-todo-candidates.ps1` writes review-only candidates under `records/tasks/candidates/`. |
| Research triage | Automatic | `code/scripts/classify-research-activity.ps1` groups daily material into definitions, propositions, proof plans, questions, literature, and ideas. |
| Proof obligations | Automatic | `code/scripts/extract-proof-obligations.ps1` scans `research/` for TODO, conjecture, and proof-obligation markers. |
| Weekly/monthly reports | Automatic | `code/scripts/new-periodic-report.ps1` summarizes daily reports into `records/periodic/`. |
| Activity correspondence | Automatic | `code/scripts/build-activity-correspondence.ps1` links watch/video/AI activity to research follow-up candidates. |
| Morning/night prompts | Automatic | Codex automations post a morning brief. The daily report itself now carries the reflection prose, so separate life-log reflection prompts should stay disabled unless explicitly needed. |
| Browser or YouTube watch history | Not enabled | This needs explicit browser/Google history access. Do not enable it silently. |

## Automation Health and Recovery

The daily wrapper now repairs local state, runs a preflight health check, runs
the normal collection/report pipeline, and then runs a postflight health check.

Manual repair plus health check:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\repair-automation-state.ps1 -Date YYYY-MM-DD -RunHealthCheck
```

Health check only:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\test-automation-health.ps1 -Date YYYY-MM-DD -WriteReport
```

The health check writes local-only reports:

```text
records/health/YYYY-MM-DD.md
records/health/YYYY-MM-DD.json
```

The full daily wrapper also appends one JSONL row per run:

```text
records/logs/automation-runs/YYYY-MM-DD.jsonl
```

That row records start/end time, step status, critical/degraded/optional
failures, output presence, and redacted environment readiness. Environment
values are never written; only `set(process)`, `set(user)`, or `missing`.

The wrapper also uses a local lock file while it runs:

```text
records/logs/automation-runs/daily-research-report.lock
```

This prevents overlapping daily-report runs. A lock older than 6 hours is
treated as stale and removed by the next run.

Severity rules:

- `critical`: local state repair and daily report generation. A failure exits
  the wrapper with a nonzero status.
- `degraded`: Discord channel setup and health checks. A failure means the
  local report may still exist, but some notification/capture feature needs
  attention.
- `optional`: individual imports such as Twitter/X, Gmail export, calendar,
  video metadata, and derived reports. Missing optional settings should not
  block the daily report.

Typical recovery commands:

```powershell
# Backfill yesterday locally, then inspect records/health/YYYY-MM-DD.md.
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\run-daily-research-report.ps1 -Date YYYY-MM-DD

# Regenerate only the report after fixing source files.
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\new-daily-report.ps1 -Date YYYY-MM-DD

# Re-run health after a manual fix.
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\test-automation-health.ps1 -Date YYYY-MM-DD -WriteReport
```

When the health report says `FAIL`, fix that first. When it says only `WARN`,
the daily system is usually usable, but one integration is missing, paused, or
waiting for new source data.

## Bot Token Setup

Do not paste a bot token into chat or commit it to Git.

Use this local prompt to store the token in the Windows user environment:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\set-discord-bot-config.ps1 -ChannelId "<daily channel id>" -GuildId "<guild id>"
```

Store your Discord user id so wake-up estimates and personal activity summaries
do not accidentally use other people's messages:

```powershell
[Environment]::SetEnvironmentVariable("DISCORD_SELF_USER_ID", "<your user id>", "User")
```

After the token is stored, list channels available to the bot:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\list-discord-channels.ps1
```

Export a day's messages:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\export-discord-channel-messages.ps1 -Date YYYY-MM-DD
```

Create or switch to the month-specific daily-report channel:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\ensure-discord-monthly-daily-channel.ps1 -Date YYYY-MM-DD -CreateWebhook -StoreInUserEnvironment
```

For example, a date in June 2026 uses `2026-6`. The script updates
`DISCORD_DAILY_CHANNEL_ID`, `DISCORD_DAILY_CHANNEL_NAME`, and
`DISCORD_DAILY_WEBHOOK_URL` in the Windows user environment.

Export activity from Discord servers other than the primary server:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\export-discord-external-activity.ps1 -Date YYYY-MM-DD
```

The external capture defaults to excluding `DISCORD_GUILD_ID`. Invite the bot to
each additional server you want recorded, and give it `View Channel`, `Read
Message History`, and Message Content intent access where needed.

If you are not an administrator of a server, request Discord's official data
package and import your own sent messages:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\import-discord-data-package.ps1 -SourcePath "C:\path\to\discord-package.zip" -GuildId 1498117779575013547 -StartDate YYYY-MM-DD -EndDate YYYY-MM-DD
```

## Food Photo Capture

The food-photo channel id is stored as:

```powershell
[Environment]::SetEnvironmentVariable("DISCORD_FOOD_CHANNEL_ID", "1515825949055127625", "User")
```

Collect food images for a date:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\collect-discord-food-images.ps1 -Date YYYY-MM-DD
```

Images are saved under the Obsidian daily-report folder:

```text
C:\Users\20010215fjii\Documents\Mr.Jikokennobun\日報\_attachments\food\YYYY-MM-DD
```

The detailed Obsidian report embeds those local images in its `Food` section.
The raw Discord food manifest is ignored by Git.

If exported messages have empty `content`, enable the Message Content intent in
the Discord Developer Portal and confirm the bot has permission to view the
channel and read message history.

## Watch Log Capture

Create or find the watch-log channel:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\ensure-discord-watch-channel.ps1 -StoreInUserEnvironment
```

If the bot lacks channel-management permission, create a Discord text channel
named `視聴ログ` manually under the `daily-report` category, then store its id:

```powershell
[Environment]::SetEnvironmentVariable("DISCORD_WATCH_CHANNEL_ID", "<channel id>", "User")
[Environment]::SetEnvironmentVariable("DISCORD_WATCH_CHANNEL_NAME", "視聴ログ", "User")
```

Post anime titles, YouTube URLs, streams, lectures, or short notes there. The
Discord posting time becomes the timestamp in `#読んだ/見た/知った`.

Status rules:

- empty URL-only posts, `みた`, `見た`, or `視聴済`: `watched`
- `部分`, `途中`, or `partial`: `partial`
- `みたい`, `見たい`, `見てない`, `未視聴`, `まだ`, or `watch later`: `want_to_watch`

Create or find the separate want-to-watch channel:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\ensure-discord-watchlist-channel.ps1 -StoreInUserEnvironment -PostUsageMessage
```

Collect watch-log messages for a date:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\export-discord-watch-activity.ps1 -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\export-discord-watchlist-activity.ps1 -Date YYYY-MM-DD
```

## Life Log Capture

Create or find the wake and mood channels. The old `振り返り` channel is no
longer required for daily-report generation because the daily report already
contains its own prose reflection.

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\ensure-discord-life-log-channels.ps1 -StoreInUserEnvironment
```

Use them like this:

- `起床ログ`: `起床 08:15`, `睡眠 6h`, `活動開始 09:00`
- `気分ログ`: `朝: 60 眠い`, `昼: 70 集中できた`, `夜: 45 疲れ`

Export those logs for a date:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\export-discord-log-channel.ps1 -LogKind wake -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\export-discord-log-channel.ps1 -LogKind mood -Date YYYY-MM-DD
```

## Weather Capture

Store the home-area coordinates in the Windows user environment. Keep the
label broad enough for privacy, because the generated daily report only needs a
weather context, not an exact address.

```powershell
[Environment]::SetEnvironmentVariable("WEATHER_LATITUDE", "<latitude>", "User")
[Environment]::SetEnvironmentVariable("WEATHER_LONGITUDE", "<longitude>", "User")
[Environment]::SetEnvironmentVariable("WEATHER_LOCATION_LABEL", "自宅周辺", "User")
```

Collect weather for a date:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\collect-weather-activity.ps1 -Date YYYY-MM-DD
```

The script writes `records/inbox/weather/YYYY-MM-DD.json`. The daily report
then fills a blank `- 天気:` line, adds `#天気の移り変わり`, and includes a
short weather line in the Discord digest.

## Discord Command Bot

Create or find the dedicated command channel:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\ensure-discord-command-channel.ps1 -StoreInUserEnvironment -PostUsageMessage
```

Post commands in `codex-command`:

```text
!todo submit the report by Friday
!done submit report
!watch https://youtu.be/... | short memo
!later https://youtu.be/... | want to watch
!mood morning: 70 focused
!mood noon: 55 tired
!mood night: 60 calm
!research title | idea memo
```

The command body can be Japanese. The command names are intentionally ASCII so
they are easy to parse reliably from Discord exports.

Natural-language command pickup can also be enabled with `-NaturalLanguage`.
This is deliberately conservative: it only acts on messages that clearly look
like commands, such as:

```text
TODO: レポートを書く
レポートを書くをTODOに追加して
TODO完了: レポートを書く
研究メモ: この構成は自己嫌悪文の分析に使えそう
夜の気分: 6 少し落ち着いた
見た: https://youtu.be/...
あとで見る: https://youtu.be/...
```

The hourly `discord-command-poller` automation scans both the dedicated
`codex-command` channel and Bot-readable ordinary Discord logs from the
configured self user. Ordinary logs are processed with `-NaturalLanguage`, so
casual messages like `入浴` are not turned into tasks.

Process commands for a date:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\process-discord-codex-commands.ps1 -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\process-discord-codex-commands.ps1 -Date YYYY-MM-DD -SourcePath records\inbox\discord\recent-YYYY-MM-DD-YYYY-MM-DD.jsonl -NaturalLanguage
```

Effects:

- `!todo` inserts an unchecked item under `records/tasks/todo.md` `## Now`.
- `!done` marks the first matching unchecked item in `records/tasks/todo.md` as done.
- `!watch` appends a watched/partial/want-to-watch record to `records/inbox/watch/YYYY-MM-DD.jsonl`.
- `!later` appends a `want_to_watch` record to `records/inbox/watch/YYYY-MM-DD.jsonl`.
- `!mood` appends to `records/inbox/mood/YYYY-MM-DD.jsonl`.
- `!research` inserts a memo into `research/ideas/inbox.md`.

Only the configured `DISCORD_SELF_USER_ID` is processed by default. Pass
`-AllowAnyAuthor` only for testing or shared workflows.

## Discord AI Chat

Create or find the AI chat channel:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\ensure-discord-ai-chat-channel.ps1 -StoreInUserEnvironment -PostUsageMessage
```

### Event-driven no-API mode

This mode does not use `OPENAI_API_KEY` and does not create separate OpenAI API
billing. It detects Discord posts immediately and appends them to:

```text
records/inbox/ai-chat/YYYY-MM-DD-pending.jsonl
```

Start the event listener:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\start-self-manzokubun-event-responder.ps1 -ReplyMode QueueOnly
```

The convenience launcher for a visible console is:

```text
code\scripts\start-self-manzokubun-event-responder.cmd
```

QueueOnly mode is the recommended default when avoiding API billing. The Gateway
listener captures messages immediately, writes the pending JSONL queue, and
updates `records/inbox/ai-chat/pending-trigger.json`. Codex can then consume the
pending queue through the existing self-manzokubun workflow, or you can ask
Codex to answer queued pending messages manually. The realtime heartbeat should
inspect `run-self-manzokubun-realtime-heartbeat.ps1` first and avoid Discord
history polling when there is no local trigger.

### Event-driven live OpenAI mode

This mode replies immediately when a message is posted, but it uses the paid
OpenAI API. Do not enable it unless you intentionally want live API-backed
replies.

Store an OpenAI API key in the Windows user environment. Do not paste API keys
into chat, Discord, or Git:

```powershell
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "<OpenAI API key>", "User")
[Environment]::SetEnvironmentVariable("OPENAI_AI_CHAT_MODEL", "gpt-5.5", "User")
[Environment]::SetEnvironmentVariable("DISCORD_AI_REPLY_MODE", "OpenAI", "User")
```

Start the event-driven live responder:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\start-self-manzokubun-event-responder.ps1 -ReplyMode OpenAI -SaveResearchMusings
```

Use only one AI-chat mode at a time:

- `QueueOnly`: event detection only; no API billing.
- `OpenAI`: event detection plus immediate reply; paid API.
- Legacy `respond-discord-ai-chat.ps1 -Loop`: REST polling fallback; do not run
  it at the same time as `OpenAI` event mode.

The event listener reads `DISCORD_AI_CHAT_CHANNEL_ID`, ignores bot messages,
and only processes the configured `DISCORD_SELF_USER_ID` by default. Pass
`-AllowAnyAuthor` only if you intentionally want the assistant to reply to other
users too.

Discord bot requirements:

- Bot is invited to the server.
- Bot can `View Channel`, `Send Messages`, and `Read Message History` in
  `自己満足文`.
- Message Content intent is enabled in the Discord Developer Portal.

If posted messages are detected but their content is empty, check Message
Content intent and channel permissions.

## Calendar Capture

Create or find the calendar notification channel:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\ensure-discord-calendar-channel.ps1 -CreateWebhook -StoreInUserEnvironment -PostUsageMessage
```

Google Calendar uses a read-only iCal URL:

```powershell
[Environment]::SetEnvironmentVariable("GOOGLE_CALENDAR_ICAL_URL", "<secret iCal URL>", "User")
```

Then sync calendar events and Discord scheduled events:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\sync-calendar-notifications.ps1 -Date YYYY-MM-DD -IncludeDiscordEvents -SyncObsidian -PostDiscordDigest
```

The output goes to `records/tasks/calendar/YYYY-MM-DD.md` and Obsidian
`Tasks/カレンダー/YYYY-MM-DD.md`.

Discord calendar reminders are deduplicated in
`records/logs/calendar-notification-state.csv`. By default, reminders are posted
3 days before, 1 day before, and on the event date.

Google's help says the read-only iCal link is under Calendar settings,
`Integrate calendar`, then `Secret address in iCal format`. Keep that URL
private; anyone with it can view the calendar.

## Mail Announcement Capture

Create or repair the mail announcement category and webhooks:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\ensure-discord-mail-announcement-channels.ps1 -CreateWebhooks -StoreInUserEnvironment
```

After the Gmail Apps Script export has been imported, post compact task notices:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\post-gmail-task-announcements.ps1 -Date YYYY-MM-DD
```

Build the Obsidian deadline list and send due-date reminders:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\sync-mail-deadline-reminders.ps1 -Date YYYY-MM-DD -SyncObsidian -PostDiscordReminders
```

Build the combined mail action timeline:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\new-mail-action-timeline.ps1 -Date YYYY-MM-DD -SyncObsidian -PostDiscord
```

These notices are intentionally short. Full snippets and task candidates remain
in `records/tasks/mail/` and Obsidian `Tasks/メール/`.

## Daily Run

The manual full run is:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\ensure-discord-monthly-daily-channel.ps1 -Date YYYY-MM-DD -CreateWebhook -StoreInUserEnvironment
powershell -ExecutionPolicy Bypass -File .\code\scripts\ensure-discord-life-log-channels.ps1 -StoreInUserEnvironment
powershell -ExecutionPolicy Bypass -File .\code\scripts\ensure-discord-command-channel.ps1 -StoreInUserEnvironment
powershell -ExecutionPolicy Bypass -File .\code\scripts\ensure-discord-watchlist-channel.ps1 -StoreInUserEnvironment
powershell -ExecutionPolicy Bypass -File .\code\scripts\ensure-discord-calendar-channel.ps1 -CreateWebhook -StoreInUserEnvironment
powershell -ExecutionPolicy Bypass -File .\code\scripts\export-discord-channel-messages.ps1 -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\export-discord-recent-activity.ps1 -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\export-discord-external-activity.ps1 -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\collect-discord-food-images.ps1 -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\export-discord-watch-activity.ps1 -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\export-discord-watchlist-activity.ps1 -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\process-discord-codex-commands.ps1 -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\enrich-video-metadata.ps1 -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\sync-calendar-notifications.ps1 -Date YYYY-MM-DD -IncludeDiscordEvents -SyncObsidian -PostDiscordDigest
powershell -ExecutionPolicy Bypass -File .\code\scripts\export-discord-log-channel.ps1 -LogKind wake -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\export-discord-log-channel.ps1 -LogKind mood -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\import-gmail-task-export.ps1 -Date YYYY-MM-DD -SyncObsidian
powershell -ExecutionPolicy Bypass -File .\code\scripts\post-gmail-task-announcements.ps1 -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\sync-mail-deadline-reminders.ps1 -Date YYYY-MM-DD -SyncObsidian -PostDiscordReminders
powershell -ExecutionPolicy Bypass -File .\code\scripts\import-chatgpt-pro-ideas.ps1 -Date YYYY-MM-DD -SyncObsidian
powershell -ExecutionPolicy Bypass -File .\code\scripts\index-obsidian-research.ps1
powershell -ExecutionPolicy Bypass -File .\code\scripts\new-daily-report.ps1 -Date YYYY-MM-DD -UseCodex -SyncObsidian -PostDiscordDigest
powershell -ExecutionPolicy Bypass -File .\code\scripts\extract-todo-candidates.ps1 -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\classify-research-activity.ps1 -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\extract-proof-obligations.ps1
powershell -ExecutionPolicy Bypass -File .\code\scripts\build-activity-correspondence.ps1 -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\new-periodic-report.ps1 -Period week -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\new-periodic-report.ps1 -Period month -Date YYYY-MM-DD
```

If Discord bot configuration is not available yet, skip the first line. The
report will still include Obsidian, todo, repository activity, and manually
queued YouTube items.

## Daily Report Layout Rules

- `起床` is filled only when blank. If an existing report already has a wake-up
  time, the script preserves it.
- Blank `起床` uses `起床ログ` first, then the earliest reliable activity timestamp
  as an automatic estimate.
- Food, SNS, generated-AI, watch-log, and watched video entries must include a JST
  timestamp.
- Mood values are filled from `気分ログ` when available; otherwise the template
  keeps morning/noon/night placeholders.
- `SNSでの活動` and `生成AIでの活動` are inserted after
  `#読んだ/見た/知った` and before `#精神状態`.

## Derived Reports

After the daily report is written, the automation also generates:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\extract-todo-candidates.ps1 -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\classify-research-activity.ps1 -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\extract-proof-obligations.ps1
powershell -ExecutionPolicy Bypass -File .\code\scripts\build-activity-correspondence.ps1 -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\new-periodic-report.ps1 -Period week -Date YYYY-MM-DD
powershell -ExecutionPolicy Bypass -File .\code\scripts\new-periodic-report.ps1 -Period month -Date YYYY-MM-DD
```

These outputs are review material. Move only confirmed tasks into
`records/tasks/todo.md`.

## YouTube Capture

Add a video with notes:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\import-youtube-activity.ps1 -Url "https://www.youtube.com/watch?v=..." -Notes "What I learned or why it mattered"
```

With `yt-dlp` installed:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\import-youtube-activity.ps1 -Url "https://www.youtube.com/watch?v=..." -FetchMetadata -FetchTranscript
```

Raw YouTube transcript files and raw daily source packets are ignored by Git.

## Twitter/X Capture

Manual queue:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\import-twitter-activity.ps1 -Text "posted about ..." -Url "https://x.com/jikokennobun/status/..."
```

API queue, if your X API access supports reading user posts:

```powershell
[Environment]::SetEnvironmentVariable("X_BEARER_TOKEN", "<token>", "User")
powershell -ExecutionPolicy Bypass -File .\code\scripts\import-twitter-activity.ps1 -FetchApi -Date YYYY-MM-DD
```

## Generated AI Capture

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\import-ai-activity.ps1 -Tool Codex -Summary "What the AI session did" -Details "Optional detail."
```

This keeps AI-session summaries in the daily source packet without storing
private exported chat histories in Git.





