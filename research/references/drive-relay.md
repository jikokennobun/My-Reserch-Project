# Drive Relay

This file defines the stable relay between ChatGPT Project discussions, Google Drive, and this Codex workspace.

## Relay Principle

Use ChatGPT Project for exploratory conversation. Move important outputs into a stable source that Codex can read:

- Google Drive research folder: [research-drive.md](research-drive.md)
- Google Drive reference folder: [drive.md](drive.md)
- ChatGPT shared links: [chatgpt-share-watchlist.csv](chatgpt-share-watchlist.csv)

Codex should treat the local repository as the durable research record.

## Recommended Flow

1. Discuss freely in ChatGPT Project.
2. When a conversation becomes research-relevant, create or update a shared link.
3. Add the shared link to `research/references/chatgpt-share-watchlist.csv`.
4. If the output is a draft, slide, PDF, or long note, put it in the Google Drive research folder.
5. Codex checks the watchlist and Drive folders, then updates local notes under `research/notes/`.

## Important Limitation

For ordinary ChatGPT shared links, the link is usually a snapshot of the conversation at share time. If the Project conversation continues, Codex may not see new messages unless the shared link is updated or a new shared link is added. Enterprise/Edu shared links may behave differently.

## Codex Sync Targets

- Watch changed shared links and update their corresponding `NoteFile`.
- Watch the research Drive folder for new outputs under `Paper`, `Slide`, `Gemini`, and `Claude`.
- Summarize meaningful updates in [../../records/logs/research-log.md](../../records/logs/research-log.md).
- Add raw ideas to [../ideas/inbox.md](../ideas/inbox.md) when they do not yet have a home.
