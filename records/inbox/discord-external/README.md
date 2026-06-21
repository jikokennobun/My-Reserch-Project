# External Discord Inbox

Ignored JSONL captures for Discord servers other than the primary daily-report
server.

Run:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\export-discord-external-activity.ps1 -Date YYYY-MM-DD
```

By default the script excludes `DISCORD_GUILD_ID`, so it is suitable for
recording activity outside the primary server. The bot can only read guilds and
channels where it has been invited and granted `View Channel` plus
`Read Message History`.
