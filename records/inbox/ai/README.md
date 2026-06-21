# Generative AI Inbox

Ignored JSONL captures for Codex, ChatGPT, Claude, Gemini, or other generated-AI
work sessions.

Manual queue:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\import-ai-activity.ps1 -Tool Codex -Summary "Built daily-report automation" -Details "Discord, Obsidian, and food-photo capture were wired together."
```

For fully automatic capture, the service must provide an API, export, connector,
or browser-based access that the user explicitly enables.
