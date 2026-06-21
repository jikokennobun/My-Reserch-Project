# Discord Inbox

Raw Discord captures should be stored here as `YYYY-MM-DD.jsonl`.

Each JSONL line should use this shape:

```json
{
  "timestamp": "2026-06-15T21:30:00+09:00",
  "channel": "research-inbox",
  "author": "display-name",
  "message_id": "discord-message-id",
  "content": "message text",
  "attachments": []
}
```

Inbound capture should stay raw. Codex can classify messages into todos,
research ideas, daily-report material, and follow-up questions during a later
triage pass.

If exported messages have empty `content`, check that the bot has access to the
channel, can read message history, and is allowed to receive message content in
the Discord developer settings for the bot.
