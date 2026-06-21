# Twitter/X Inbox

Ignored JSONL captures for Twitter/X activity from `@jikokennobun`.

Manual queue:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\import-twitter-activity.ps1 -Text "posted about ..." -Url "https://x.com/jikokennobun/status/..."
```

API queue, if an X API bearer token is available:

```powershell
[Environment]::SetEnvironmentVariable("X_BEARER_TOKEN", "<token>", "User")
powershell -ExecutionPolicy Bypass -File .\code\scripts\import-twitter-activity.ps1 -FetchApi -Date YYYY-MM-DD
```

Do not commit API tokens or raw exports.
