# Discord, Obsidian, and Codex Bridge

This document defines a practical bridge for daily reports, todo grooming, and
research synthesis across Discord, Obsidian, and Codex.

## Roles

- Discord: fast capture and notification surface.
- Obsidian: human writing surface over Markdown notes.
- Repository: durable research ledger and automation source of truth.
- Codex: scheduled organizer, summarizer, checker, and publisher.

Keep the repository as the canonical automation target. Obsidian and Discord
can feed it, but automated research outputs should land in Git-tracked files
before being mirrored elsewhere.

The monthly daily-report channel such as `2026-6` is for final daily digests and
short report-related requests. Daytime capture should go to dedicated channels
such as `やった`, `思った`, `視聴ログ`, `食`, `気分ログ`, `起床ログ`, or
`codex-command`.

## Discord Category Layout

- `🚪 雑談・入口`: `📜rules`, `🧭チャンネルとロール`, and general entry
  discussion.
- `📔 日報・月次`: monthly final report channels such as `2026-6` and legacy
  yearly report channels.
- `🧾 生活ログ`: raw daily-life capture channels such as `🧾活動ログ`,
  `✅やった`, `💭思った`, `🍽️食`, `🎬視聴ログ`, `🌗気分ログ`,
  and `🌅起床ログ`. The old separate `振り返り` channel is deprecated because
  the daily report now carries the reflection prose itself.
- `AI 自動化`: bot control and AI conversation channels such as
  `aicodex-command`, `aiai-chat`, and `ir自己満足文`.
  Discord normalizes ASCII channel-name prefixes to lowercase and strips
  punctuation such as `.` in text channels, so `IR.` is represented as `ir`.
  Text-channel spaces are normalized to hyphens, so text channels use no
  separator after the icon/prefix.
- `🔔 通知・予定`: calendar, university mail, tutoring mail, and combined mail
  timeline notifications. Notification channels use the unified `🔔` prefix.
- `📰 AI・数学ニュース`: AI general news and mathematics news channels such as
  `📰ai-news` and `📰math-news`.
- `研究関連`: research discussion, preprints, memo, and research-output
  channels. This category may need manual Discord permission fixes before the
  bot can rename it or move private draft channels.
- `🎓 大学・仕事`: university study, assignments, and internship/job channels.
- `🌐 SNS・外部`: Twitter/X notes, external-server forwarding, and miscellaneous
  imported items.
- `🎨 趣味・創作`: prototypes, ideas, DTM/music production, anime, fiction, and other creative
  interests.

Use `code/scripts/organize-discord-channels.ps1 -Apply` to re-apply the layout
without deleting channels. Empty old categories should be removed manually only
after checking that no permissions or old links depend on them.

Use `code/scripts/apply-discord-readable-layout.ps1 -Apply -StoreInUserEnvironment
-PostGuideMessages` to apply the emoji-readable channel names and create the
entry guide channels. Do not add emoji prefixes to monthly date channels such as
`2026-6`; the rollover script intentionally keeps those exact names.

## Recommended Data Flow

```text
Discord daily digest channel
  -> monthly channel rollover, e.g. 2026-6
  -> records/inbox/discord/YYYY-MM-DD.jsonl
Discord command channel
  -> records/inbox/discord-commands/YYYY-MM-DD.jsonl
  -> records/tasks/todo.md
  -> records/inbox/watch/YYYY-MM-DD.jsonl
  -> records/inbox/mood/YYYY-MM-DD.jsonl
  -> research/ideas/inbox.md
Discord AI chat channel `自己満足文`
  -> code/scripts/watch-discord-message-events.ps1
  -> code/scripts/invoke-discord-ai-chat-pending.ps1
  -> QueueOnly: pending queue for Codex/manual no-API replies
  -> OpenAI: immediate Discord replies in the same channel
  -> research/ideas/inbox.md for math-musing candidates
  -> records/research-triage/discord-ai-chat-YYYY-MM-DD.md
Readable Discord channels in the primary server
  -> code/scripts/collect-discord-math-musings.ps1
  -> records/inbox/discord/recent-YYYY-MM-DD-YYYY-MM-DD.jsonl
  -> research/ideas/inbox.md for self-authored math/research musings
  -> code/scripts/new-discord-discussion-summary.ps1
  -> records/discussions/daily/YYYY-MM-DD.md
Discord Gateway event listener
  -> code/scripts/watch-discord-message-events.ps1
  -> records/inbox/discord/events-YYYY-MM-DD.jsonl
  -> records/inbox/ai-chat/YYYY-MM-DD-pending.jsonl for `自己満足文`
  -> research/ideas/inbox.md for self-authored math/research musings
External Discord servers
  -> records/inbox/discord-external/YYYY-MM-DD.jsonl
Twitter/X and generated-AI sessions
  -> records/inbox/twitter/YYYY-MM-DD.jsonl
  -> records/inbox/ai/YYYY-MM-DD.jsonl
Gmail labels `Codex/大学タスク` and `Codex/塾講師タスク`
  -> Apps Script / Drive export
  -> records/inbox/gmail/YYYY-MM-DD.jsonl
  -> records/tasks/mail/YYYY-MM-DD.md
  -> records/tasks/deadlines/mail-deadlines.md
  -> Discord mail announcement channels
ChatGPT Pro export or copied conversation notes
  -> records/inbox/chatgpt/YYYY-MM-DD.jsonl
Watch-log Discord channel
  -> records/inbox/watch/YYYY-MM-DD.jsonl
  -> code/scripts/enrich-video-metadata.ps1
Watchlist Discord channel
  -> records/inbox/watch/YYYY-MM-DD.jsonl with status `want_to_watch`
Google Calendar iCal and Discord scheduled events
  -> records/inbox/calendar/YYYY-MM-DD.jsonl
  -> records/tasks/calendar/YYYY-MM-DD.md
  -> Discord calendar notification channel
Open-Meteo weather
  -> records/inbox/weather/YYYY-MM-DD.json
  -> daily report weather line and weather-transition section
Automation health checks
  -> code/scripts/test-automation-health.ps1
  -> records/health/YYYY-MM-DD.md and YYYY-MM-DD.json
Daily automation wrapper
  -> code/scripts/run-daily-research-report.ps1
  -> records/logs/automation-runs/YYYY-MM-DD.jsonl
AI and mathematics news channels
  -> code/scripts/ensure-discord-news-channels.ps1
  -> Discord `ai-news` and `math-news`
  -> optional future curated news digest
Wake/mood Discord channels
  -> records/inbox/activity/YYYY-MM-DD.jsonl
  -> records/inbox/wake/YYYY-MM-DD.jsonl
  -> records/inbox/mood/YYYY-MM-DD.jsonl
  -> Codex triage
  -> records/tasks/todo.md
  -> records/daily/YYYY-MM-DD.md
  -> records/tasks/candidates/YYYY-MM-DD.md
  -> records/research-triage/YYYY-MM-DD.md
  -> records/links/YYYY-MM-DD.md
  -> records/periodic/week-*.md and month-*.md
  -> research/ideas/inbox.md or research/notes/<topic>.md
  -> optional Discord digest

Obsidian vault
  -> code/scripts/index-obsidian-research.ps1
  -> research/notes/obsidian-research-index.md
  -> daily report section `Obsidianメモ変更履歴`
  -> Codex synthesis
  -> repository updates and daily report
```

## File Contracts

- `records/inbox/discord/YYYY-MM-DD.jsonl`: raw Discord messages captured by a
  bot or export script. Each line should include timestamp, channel, author,
  message id, content, and attachment URLs.
- `records/inbox/discord-commands/YYYY-MM-DD.jsonl`: processed command-channel
  entries from `!todo`, `!done`, `!watch`, `!later`, `!mood`, and `!research`.
- `records/research-triage/discord-ai-chat-YYYY-MM-DD.md`: AI-chat math
  musings and replies captured from `自己満足文`.
- `records/inbox/discord/recent-YYYY-MM-DD-YYYY-MM-DD.jsonl`: recent readable
  primary-server messages used for daily context and light musing scans. The
  general-channel scan should only act on the configured self user unless
  `-AllowAnyAuthor` is passed deliberately.
- `records/inbox/discord/events-YYYY-MM-DD.jsonl`: live Discord Gateway events
  captured only when a message is posted. This avoids repeatedly scanning every
  readable channel. It still requires a local listener process to stay running.
- `records/discussions/daily/YYYY-MM-DD.md`: app-like daily discussion cards
  built from readable Discord logs. Each card keeps timestamp, channel, tags,
  the claim or musing, and the next action for source-backed research triage.
- `records/inbox/discord-external/YYYY-MM-DD.jsonl`: raw Discord messages from
  readable servers other than the primary server.
- `records/inbox/twitter/YYYY-MM-DD.jsonl`: Twitter/X activity for
  `@jikokennobun`, queued manually or by X API.
- `records/inbox/ai/YYYY-MM-DD.jsonl`: generated-AI work-session summaries.
- `records/inbox/activity/YYYY-MM-DD.jsonl`: general daytime activity notes
  from the `活動ログ` Discord channel. These feed the daily report's `#やった`
  section rather than the SNS section.
- `records/inbox/gmail/YYYY-MM-DD.jsonl`: university and tutoring-job mail task
  candidates exported from labelled Gmail messages.
- `records/inbox/chatgpt/YYYY-MM-DD.jsonl`: ChatGPT Pro conversation snippets
  that may become research ideas.
- `records/inbox/watch/YYYY-MM-DD.jsonl`: anime, video, stream, lecture, and
  other watched-media notes captured from Discord. Entries may include `status`
  values such as `watched`, `partial`, and `want_to_watch`.
- `records/inbox/calendar/YYYY-MM-DD.jsonl`: Google Calendar iCal events and
  Discord scheduled events.
- `records/inbox/weather/YYYY-MM-DD.json`: hourly weather summary for the
  configured home-area coordinates. The daily report uses this to fill `天気`
  and `天気の移り変わり`.
- `records/health/YYYY-MM-DD.md`: local operator-facing health report for the
  automation system. It records only booleans, counts, statuses, and file names;
  it must not contain bot tokens, webhook URLs, iCal URLs, API keys, or exact
  private coordinates.
- `records/health/YYYY-MM-DD.json`: machine-readable version of the same health
  report, ignored by Git.
- `records/logs/automation-runs/YYYY-MM-DD.jsonl`: one redacted run-ledger row
  per daily wrapper execution, including step statuses and output presence.
- `records/logs/automation-runs/daily-research-report.lock`: transient lock
  file used to prevent overlapping daily-report runs. It is local-only and
  ignored by Git.
- `records/inbox/wake/YYYY-MM-DD.jsonl`: wake/sleep/activity-start records from
  the `起床ログ` Discord channel.
- `records/inbox/mood/YYYY-MM-DD.jsonl`: morning/noon/night mood records from
  the `気分ログ` Discord channel.
- `records/tasks/todo.md`: active todo list grouped by Now, Next, Waiting, and
  Someday.
- `records/tasks/candidates/YYYY-MM-DD.md`: review-only todo candidates.
- `records/daily/YYYY-MM-DD.md`: daily report generated from repository
  changes, Discord captures, Obsidian memo changes, and Obsidian research-note
  changes.
- `records/research-triage/YYYY-MM-DD.md`: daily research classification.
- `records/research-triage/proof-obligations.md`: keyword scan for unresolved
  proof obligations and research questions.
- `records/links/YYYY-MM-DD.md`: correspondence between watched items, AI
  sessions, and research follow-up candidates.
- `records/periodic/`: weekly and monthly summaries generated from daily notes.
- `research/ideas/inbox.md`: raw research ideas that still need classification.
- `records/logs/research-log.md`: durable chronological research log.

Do not store Discord bot tokens, webhook URLs, or Obsidian local API tokens in
the repository. Use environment variables or a local ignored config file.

## Minimum Viable Automation

Start with an outbound-only Discord webhook. This gives a useful daily digest
without granting Codex permission to read or mutate Discord state.

### Discord setup

An invite URL is useful for identifying the server, but creating channels and
reading messages requires a bot that has been added to the server with the
needed permissions.

Resolve an invite locally:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\resolve-discord-invite.ps1 -InviteUrl "<discord invite url>"
```

Then set local-only environment variables:

```powershell
$env:DISCORD_GUILD_ID = "<guild id>"
$env:DISCORD_BOT_TOKEN = "<bot token>"
```

Create or find the daily-report channel:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\create-discord-daily-channel.ps1 -ChannelName "daily-report" -CreateWebhook
```

Store the returned channel id and webhook URL locally:

```powershell
$env:DISCORD_DAILY_CHANNEL_ID = "<channel id>"
$env:DISCORD_DAILY_WEBHOOK_URL = "<webhook url>"
```

For scheduled runs, store the webhook in the Windows user environment rather
than in the repository:

```powershell
[Environment]::SetEnvironmentVariable("DISCORD_DAILY_WEBHOOK_URL", "<webhook url>", "User")
```

For a separate research channel, store a second webhook:

```powershell
[Environment]::SetEnvironmentVariable("DISCORD_RESEARCH_WEBHOOK_URL", "<research webhook url>", "User")
powershell -ExecutionPolicy Bypass -File .\code\scripts\post-discord-webhook.ps1 -WebhookEnvVar DISCORD_RESEARCH_WEBHOOK_URL -Content "Research channel connected."
```

Do not put bot tokens, webhook URLs, or private invite links in Git-tracked
files.

The Obsidian daily-report destination is:

```text
C:\Users\20010215fjii\Documents\Mr.Jikokennobun\日報
```

1. Refresh the Obsidian research index:

   ```powershell
   powershell -ExecutionPolicy Bypass -File .\code\scripts\index-obsidian-research.ps1
   ```

2. Ask Codex, or a Codex automation, to generate:

   - today's completed work
   - changed research notes
   - unresolved proof obligations
   - next todos
   - publication or PDF artifacts created

3. Append the durable result to:

   - `records/daily/YYYY-MM-DD.md`
   - `records/logs/research-log.md`
   - `records/tasks/todo.md` when todos change

4. Post a short digest to Discord with a webhook script.

   ```powershell
   $env:DISCORD_DAILY_WEBHOOK_URL = "<local webhook url>"
   powershell -ExecutionPolicy Bypass -File .\code\scripts\post-discord-webhook.ps1 -ContentPath .\records\daily\YYYY-MM-DD.md -SectionHeading "Discord Digest"
   ```

Only after this is stable, add inbound Discord capture.

### AI research chat

The `自己満足文` Discord channel is for lightweight conversation with the AI
research companion. The preferred detector is the Discord Gateway listener,
which receives `MESSAGE_CREATE` events instead of repeatedly polling channel
history.

Create or find the channel:

```powershell
$channelName = -join ([char[]](0x81EA,0x5DF1,0x6E80,0x8DB3,0x6587))
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\ensure-discord-ai-chat-channel.ps1 -ChannelName $channelName -StoreInUserEnvironment
```

There are two operating modes. Run only one at a time.

QueueOnly mode does not use `OPENAI_API_KEY` or the paid OpenAI API. It detects
posts immediately and appends them to
`records/inbox/ai-chat/YYYY-MM-DD-pending.jsonl`. It also refreshes
`records/inbox/ai-chat/pending-trigger.json`, which is the lightweight local
signal used by the Codex heartbeat. Codex or a manual run can then consume that
queue and post replies with `post-discord-ai-chat-reply.ps1`. This avoids
separate API billing, but Codex itself is not woken directly by Discord events.

Start QueueOnly mode:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\start-self-manzokubun-event-responder.ps1 -ReplyMode QueueOnly
```

OpenAI live mode replies immediately from the same event stream, but it requires
API billing that is separate from ChatGPT subscriptions. If you use it, set the
API key in the Windows user environment. Do not paste API keys into Discord,
Git, or chat logs.

```powershell
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "<api key>", "User")
[Environment]::SetEnvironmentVariable("DISCORD_AI_REPLY_MODE", "OpenAI", "User")
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\start-self-manzokubun-event-responder.ps1 -ReplyMode OpenAI -SaveResearchMusings
```

For math/research questions, the reply style should use short LaTeX-style
formulas such as `$T \vdash \varphi$` or
`$\Box(\Box A \to A) \to \Box A$`, and include source links only when they have
been checked. Prefer arXiv, DOI, journal/publisher pages, author pages, and
reliable survey entries such as SEP. If a reference has not been checked, label
it as a search keyword or reading candidate rather than a citation.

The legacy `respond-discord-ai-chat.ps1 -Loop` path is a REST polling fallback.
Do not run it at the same time as event-driven OpenAI mode, or duplicate replies
may occur.

### Event-driven Discord capture

Codex heartbeat automations wake up on a schedule, so they cannot be triggered
directly by Discord message events. To avoid frequent Discord polling, run a
local Gateway listener instead:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\watch-discord-message-events.ps1
```

The listener stays connected to Discord and records messages only when
`MESSAGE_CREATE` arrives. By default it accepts messages from the configured
`DISCORD_SELF_USER_ID` in bot-readable channels, appends raw events to
`records/inbox/discord/events-YYYY-MM-DD.jsonl`, queues `自己満足文` messages in
`records/inbox/ai-chat/YYYY-MM-DD-pending.jsonl`, and sends math-like musings
through `process-discord-codex-commands.ps1`. The supervisor script restarts the
listener after Gateway reconnect or invalid-session exits.

To limit it to a small set of channels, pass channel IDs:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\watch-discord-message-events.ps1 -WatchChannelIds @("<channel id>","<channel id>")
```

This replaces Discord-side polling, but it does not by itself make the Codex app
wake up instantly. Immediate AI replies require event-driven OpenAI mode or
another live local AI backend. QueueOnly mode is still event-driven for
detection and is the no-extra-billing default.

For the no-extra-billing setup, keep the Gateway listener running and let the
Codex heartbeat inspect only the local trigger:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\run-self-manzokubun-realtime-heartbeat.ps1 -Date 2026-06-20
```

If `needs_response` is `false`, the heartbeat should return `DONT_NOTIFY` and do
nothing else. If it is `true`, the heartbeat should answer the selected records
and post through `post-discord-ai-chat-reply.ps1`. This keeps ordinary zero-item
checks quiet and avoids repeated Discord history polling.

Suggested reply shape for `自己満足文`:

1. `見立て`: one or two sentences explaining the mathematical shape.
2. `式でいうと`: compact formulas or a small derivation.
3. `接続先`: related theories, theorem families, or keywords.
4. `出典候補`: verified links when available; otherwise mark as unverified.
5. `次の一手`: one concrete Codex/Obsidian follow-up.

### AI and mathematics news channels

Use a dedicated news category so external news does not get mixed into daily
life logs or research-musing threads:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\ensure-discord-news-channels.ps1 -CreateWebhooks -StoreInUserEnvironment
```

This creates or finds the `📰 AI・数学ニュース` category and the channels
`ai-news` and `math-news`. The script stores channel IDs and webhook URLs in
the Windows user environment:

- `DISCORD_AI_NEWS_CHANNEL_ID`
- `DISCORD_AI_NEWS_WEBHOOK_URL`
- `DISCORD_MATH_NEWS_CHANNEL_ID`
- `DISCORD_MATH_NEWS_WEBHOOK_URL`

Keep this curated. Good candidates are model releases, AI product/policy
changes, arXiv or journal announcements, seminar links, survey papers, and
mathematical research news with a clear source URL.

### Daily report command

After the Discord channel and webhook are configured, the normal local sequence
is:

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

Food images posted to channel `1515825949055127625` are collected into the
Obsidian daily-report attachment folder and embedded in the detailed Obsidian
report. Discord receives only the short `Discord Digest` section.

The monthly rollover script creates or reuses channels named like `2026-6`,
then stores the matching channel id and webhook URL in the Windows user
environment. The daily automation runs it first, so month changes are handled
without manual channel switching.

The life-log setup script creates or reuses:

- `起床ログ`: wake/sleep/activity-start notes
- `気分ログ`: morning/noon/night mood notes

The daily report preserves an existing `起床` value. If it is blank, it uses
`起床ログ` first and then falls back to the earliest reliable activity timestamp.
Every food, SNS, AI, watch, and video item should keep a timestamp. Reflection
belongs in the daily report's prose section rather than a separate life-log
channel.

External Discord capture excludes the primary `DISCORD_GUILD_ID` by default.
Invite the bot to other servers when their activity should be recorded.

If a YouTube video should be included:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\import-youtube-activity.ps1 -Url "https://www.youtube.com/watch?v=..." -Notes "Why this mattered today"
```

If `yt-dlp` is installed and network access is available, add `-FetchMetadata`
or `-FetchTranscript` so the daily-report pass can summarize from metadata and
captions.

If Twitter/X or generated-AI activity should be included:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\import-twitter-activity.ps1 -Text "posted about ..." -Url "https://x.com/jikokennobun/status/..."
powershell -ExecutionPolicy Bypass -File .\code\scripts\import-ai-activity.ps1 -Tool Codex -Summary "Daily automation work"
```

## Full Discord Bot Loop

Use a bot only when commands are needed:

- `/todo <text>`: append a task candidate.
- `/research <text>`: append a research idea.
- `/daily`: request the latest daily digest.
- `/focus <topic>`: set the next Codex synthesis focus.

The bot should write raw captures first, then let Codex classify them. This
keeps irreversible decisions out of the Discord event handler.

## Codex Integration Options

- Codex app automations: best for recurring daily/weekly reports from this
  repository.
- `codex exec`: best for scripts that need a final Markdown or JSON result.
- MCP server: best once Discord and Obsidian operations are stable enough to
  expose as tools such as `discord_fetch_recent`, `discord_post_digest`,
  `obsidian_search`, and `obsidian_append_note`.
- Skill: best for packaging the daily-report and research-triage workflow so
  automations can invoke it consistently.

## Suggested Scheduled Jobs

- Morning todo review: read `records/tasks/todo.md`, recent Discord captures,
  and recent Obsidian research changes; produce a compact task list for today.
- Evening daily report: summarize completed work, new notes, blocked items,
  generated artifacts, and the best next research action.
- Nightly reflection: keep it inside the daily report prose unless the user
  explicitly asks for a separate prompt.
- Weekly research synthesis: update open problems, definitions, and research
  questions from the week's notes and discussions.

For unattended runs, keep the sandbox at the least permission level that works.
Prefer workspace-write with narrow command allow rules over broad full-access
automation.

## Daily Report Prompt

```text
Generate today's research daily report.

Inputs:
- records/tasks/todo.md
- records/logs/research-log.md
- records/inbox/discord/<today>.jsonl if present
- research/notes/obsidian-research-index.md
- changed files in research/, records/, code/, and artifacts/

Output:
1. Append records/daily/YYYY-MM-DD.md.
2. Update records/tasks/todo.md only for concrete todo status changes.
3. Add a short entry to records/logs/research-log.md.
4. Produce a Discord-ready digest under 1800 characters.

Rules:
- Separate research claims from todo management.
- Do not index or summarize personal Obsidian daily notes.
- Mark uncertain mathematical claims as conjectures or questions.
- Do not invent bibliographic facts.
```

## Todo Grooming Shape

```markdown
# Todo

## Now

- [ ] ...

## Next

- [ ] ...

## Waiting

- [ ] ...

## Someday

- [ ] ...

## Done Archive

### YYYY-MM-DD

- [x] ...
```

## Implementation Order

1. Add `records/tasks/todo.md` and `records/daily/`.
2. Create a local Discord webhook poster script.
3. Create a daily-report Codex prompt or project automation.
4. Add Discord inbound capture only after the output format is stable.
5. Convert the bot/webhook scripts into an MCP server if direct Codex tool use
   becomes valuable.




