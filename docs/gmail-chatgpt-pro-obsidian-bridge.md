# Gmail and ChatGPT Pro to Obsidian

This bridge is intentionally label/inbox based. It does not read all Gmail or
all ChatGPT history by default.

## Gmail Task Sources

Recommended rule:

- Gmail label: `Codex/大学タスク`
- Gmail label: `Codex/塾講師タスク`
- Processed label: `Codex/取込済み`
- Drive export folder: `Codex Gmail Task Export`
- Obsidian output: `Tasks/メール/YYYY-MM-DD.md`
- Address matching: `UNIVERSITY_ADDRESSES` in the Apps Script contains the two
  university addresses provided by the user and the personal Gmail forwarding
  alias `shibuyaiori2004+univ@gmail.com`.
- Address matching: `TUTORING_ADDRESSES` contains the tutoring-job Gmail address
  provided by the user.

Flow:

```text
Gmail labels `Codex/大学タスク` and `Codex/塾講師タスク`
  -> Apps Script export
  -> Google Drive folder `Codex Gmail Task Export`
  -> code/scripts/import-gmail-task-export.ps1
  -> records/inbox/gmail/YYYY-MM-DD.jsonl
  -> records/tasks/mail/YYYY-MM-DD.md
  -> Obsidian Tasks/メール/YYYY-MM-DD.md
```

The Apps Script source is:

```text
code/apps-script/gmail-university-task-export.gs
```

It does two things:

- exports messages already labelled `Codex/大学タスク`
- exports messages already labelled `Codex/塾講師タスク`
- auto-labels recent messages involving the configured university or tutoring
  addresses, so forwarded or received mail can become task candidates

Manual local import:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\import-gmail-task-export.ps1 -Date YYYY-MM-DD -SyncObsidian
```

The importer only converts exported JSON. Gmail authorization stays inside the
user-owned Apps Script.

## Google Apps Script Setup

This part must be done by the Google account owner in the browser.

1. Open <https://script.google.com/>.
2. Create a new Apps Script project.
3. Rename it to something like `Codex Gmail Task Export`.
4. Replace the default code with `code/apps-script/gmail-university-task-export.gs`.
5. Save the project.
6. In the function selector, choose `exportUniversityTasks`.
7. Click Run once.
8. Approve the Gmail and Drive permissions requested by Google.
9. Confirm that a Drive folder named `Codex Gmail Task Export` was created and
   contains `mail-tasks-YYYY-MM-DD.json`.
10. Open Triggers from the left sidebar.
11. Add a trigger for `exportUniversityTasks`.
12. Choose event source `Time-driven`.
13. Choose a schedule such as morning/noon/night. Use hourly only for periods
    when university deadlines need near-real-time monitoring. For tutoring mail
    that usually arrives weekly, daily or weekly is enough.
14. Save.

The trigger runs as the account that created it. If a different Google account
needs to export its mailbox, create and authorize a separate Apps Script project
from that account.

When the script code changes and new permissions are required, run
`exportUniversityTasks` manually once again to refresh authorization.

The importer and Apps Script both ignore obvious test messages and job-board
mail such as Indeed/T-news recommendations, so the Discord mail channels stay
focused on actual university/tutoring actions.

## Discord Mail Announcements

Discord mail announcements use a dedicated category:

```text
🔔 通知・予定
  - 🔔大学メール通知
  - 🔔塾講師メール通知
  - 🔔mail-timeline
```

The `mail-timeline` Discord post is skipped when there are no due items, no
upcoming deadlines, and no new mail candidates. The Obsidian timeline note is
still written for traceability.

Current Discord IDs:

- Category `🔔 通知・予定`: `1515853497176817763`
- Channel `🔔大学メール通知`: `1515853501790556301`
- Channel `🔔塾講師メール通知`: `1515853510988796046`
- Channel `🔔mail-timeline`: stored in `DISCORD_MAIL_TIMELINE_CHANNEL_ID` after
  running the setup command again

Setup/repair command:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\ensure-discord-mail-announcement-channels.ps1 -CreateWebhooks -StoreInUserEnvironment
```

Post new Gmail task candidates to the dedicated Discord channels:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\post-gmail-task-announcements.ps1 -Date YYYY-MM-DD
```

Only short task announcements are posted. Full mail snippets stay in local
Markdown/Obsidian.

Create an Obsidian deadline list and optionally post deadline reminders:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\sync-mail-deadline-reminders.ps1 -Date YYYY-MM-DD -SyncObsidian -PostDiscordReminders
```

The reminder script scans Gmail task candidates for dates such as `YYYY-MM-DD`,
`YYYY年M月D日`, `M月D日`, `M/D`, `今日`, and `明日`. It posts at 3 days before,
1 day before, and on the due date by default, while keeping a local duplicate
prevention state file under `records/logs/`.

Create a compact "what should I do next" timeline:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\new-mail-action-timeline.ps1 -Date YYYY-MM-DD -SyncObsidian -PostDiscord
```

This combines today's imported Gmail task candidates and detected due dates into
`records/tasks/mail/timeline-YYYY-MM-DD.md`, Obsidian
`Tasks/メール/timeline-YYYY-MM-DD.md`, and a short Discord post.

## ChatGPT Pro Ideas

Preferred sources, in order:

1. ChatGPT data export ZIP or `conversations.json`
2. copied `.md` / `.txt` conversation notes
3. individual manual snippets with `-Text`
4. shared links already tracked by `check-chatgpt-shares.ps1`

Default local source folder:

```text
C:\Users\20010215fjii\マイドライブ\ChatGPT Pro Inbox\My-Reserch-Project
```

You can override it with the Windows user environment variable
`CHATGPT_PRO_IDEA_SOURCE`.

Flow:

```text
ChatGPT Pro export or copied conversation note
  -> code/scripts/import-chatgpt-pro-ideas.ps1
  -> records/inbox/chatgpt/YYYY-MM-DD.jsonl
  -> records/research-triage/chatgpt-pro-ideas-YYYY-MM-DD.md
  -> Obsidian Research-memo/研究アイデアInbox.md
```

Manual import examples:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\import-chatgpt-pro-ideas.ps1 -SourcePath "C:\path\to\chatgpt-export.zip" -Date YYYY-MM-DD -SyncObsidian
```

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\import-chatgpt-pro-ideas.ps1 -Title "APS idea" -Text "Copied idea from ChatGPT Pro..." -Date YYYY-MM-DD -SyncObsidian
```

Private ChatGPT conversations should not be committed to Git. Only curated
candidate summaries should become durable research notes.

## Daily Report Integration

`new-daily-report.ps1` reads:

- `records/inbox/gmail/YYYY-MM-DD.jsonl`
- `records/inbox/chatgpt/YYYY-MM-DD.jsonl`

and adds:

- `#メールタスク`
- `#研究アイデア候補`
- counts in the daily Discord digest

The Discord digest contains counts only; detailed mail and ChatGPT snippets stay
in Obsidian/local Markdown.




