# Gmail Inbox

Ignored JSONL captures derived from Gmail messages labelled `Codex/大学タスク`.

Expected flow:

1. Google Apps Script exports `university-mail-tasks-YYYY-MM-DD.json` to Drive.
2. `code/scripts/import-gmail-task-export.ps1` converts it into
   `records/inbox/gmail/YYYY-MM-DD.jsonl`.
3. The same script writes an Obsidian task note under `Tasks/大学メール/`.

Do not commit raw mail captures.

