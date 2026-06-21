# Codex Thread Recovery Handoff

Date: 2026-06-21 JST

This note is the recovery point after the long Codex thread for Discord,
Obsidian, and daily-report automation became hard to access from the UI.
Use this file as the first context note when continuing the work in a new
thread.

## Current Repository

- Repository: `C:\Users\20010215fjii\Documents\GitHub\My-Reserch-Project`
- Branch: `main`
- Remote status at start of recovery: `main...origin/main`
- Latest observed commit: `118094f`
- Obsidian vault: `C:\Users\20010215fjii\Documents\Mr.Jikokennobun`

The repository is the source of truth for automation scripts, source packets,
daily reports, research triage, and health reports. Obsidian is the human
writing surface, and Discord is the capture/notification surface.

## Core Automation Files

- `code/scripts/run-daily-research-report.ps1`
  - Main daily wrapper.
  - Loads user environment variables, repairs local state, runs preflight,
    collects inputs, generates reports, writes run ledger, and runs postflight.
- `code/scripts/new-daily-report.ps1`
  - Builds `records/daily/YYYY-MM-DD.md` from daily packets and structured
    inboxes.
  - Can sync to Obsidian with `-SyncObsidian`.
  - Can post a digest with `-PostDiscordDigest`.
- `code/scripts/process-discord-codex-commands.ps1`
  - Processes Discord command/natural-language posts into todos, watch logs,
    mood logs, research ideas, and related local records.
- `code/scripts/collect-discord-math-musings.ps1`
  - Scans readable Discord activity for self-authored research/math musings.
- `code/scripts/watch-discord-message-events.ps1`
  - Discord Gateway listener for live message events.
- `code/scripts/invoke-discord-ai-chat-pending.ps1`
  - Processes pending self-manzokubun messages.
  - In `QueueOnly` mode, it marks messages as queued and does not call OpenAI.
- `code/scripts/collect-weather-activity.ps1`
  - Writes `records/inbox/weather/YYYY-MM-DD.json` from Open-Meteo.
- `code/scripts/test-automation-health.ps1`
  - Writes redacted health reports under `records/health/`.

## Reference Docs

- `docs/discord-obsidian-codex-bridge.md`
- `docs/daily-activity-automation.md`
- `docs/gmail-chatgpt-pro-obsidian-bridge.md`
- `docs/codex-research-automation.md`
- `records/tasks/todo.md`

## Recovery Health Check

Run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\test-automation-health.ps1 -Date 2026-06-21 -WriteReport
```

Observed recovery result after cleanup:

```text
Automation health (2026-06-21): WARN (OK=42 WARN=2 FAIL=0)
```

Remaining warnings:

- `X_BEARER_TOKEN` is missing. This is optional; Twitter/X import can remain
  manual or disabled.
- `pending self-manzokubun replies`: 2 messages are queued/not replied. This is
  expected in `QueueOnly` mode unless a human/Codex responder posts replies.

Resolved during recovery:

- Weather JSON for 2026-06-21 was generated.
- `records/daily/2026-06-21.md` was regenerated locally so the weather
  transition section is present.
- `invoke-discord-ai-chat-pending.ps1` was fixed to append rows using the
  existing `discord-ai-chat-state.csv` schema.
- This handoff note was added. Commit these recovery changes before relying on
  `origin/main` as the latest recovery state.

## Safe Continuation Commands

Health only:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\test-automation-health.ps1 -Date YYYY-MM-DD -WriteReport
```

Generate or refresh today's local daily report without posting to Discord:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\new-daily-report.ps1 -Date YYYY-MM-DD
```

Generate weather input:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\collect-weather-activity.ps1 -Date YYYY-MM-DD
```

Queue pending self-manzokubun messages without API billing:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\invoke-discord-ai-chat-pending.ps1 -Date YYYY-MM-DD -Mode QueueOnly -MaxMessages 10
```

Full daily wrapper:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\run-daily-research-report.ps1 -Date YYYY-MM-DD
```

The full wrapper may sync Obsidian and post configured Discord digests, so use
the local-only commands above when checking or repairing state without
notifications.

## Next Useful Work

- Decide whether pending self-manzokubun queue items should be answered by
  Codex/manual replies or left queued.
- Decide whether Twitter/X should remain manual or receive `X_BEARER_TOKEN`.
- Consider unpausing or replacing the `self-manzokubun-discord-responder`
  automation if live replies are desired.
- Keep this handoff note updated whenever the daily-report automation contract
  changes.
