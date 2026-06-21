# Discord Data Package Inbox

Ignored JSONL created from the official Discord data package.

This route is useful when a bot cannot be invited to a server. It records only
messages included in the user's own Discord data export.

Example:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\import-discord-data-package.ps1 -SourcePath "C:\path\to\discord-package.zip" -GuildId 1498117779575013547 -StartDate 2026-06-01 -EndDate 2026-06-30
```

The target server in the current workflow:

```text
下剋上院進: 1498117779575013547
```
