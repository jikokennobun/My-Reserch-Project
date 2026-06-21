# Research Workflow

## Recommended Roles

- ChatGPT Project: broad discussion, brainstorming, and long conversational exploration.
- Codex: repository work, file organization, literature indexing, scripts, TeX/PDF generation, and Git-tracked research artifacts.
- Google Drive: reference PDFs and generated final PDFs.
- Obsidian: daily reading/writing interface over Markdown files.
- VSCode: precise editing, TeX, Git, and code work.

## ChatGPT Project Access

Codex cannot directly open a private ChatGPT Project as a folder. Use one of these bridges:

1. Paste important ChatGPT Project outputs into `research/ideas/inbox.md`.
2. Share a ChatGPT conversation link and ask Codex to extract or summarize it.
3. Export/copy project notes into Markdown files in this repository.
4. Use Google Drive Docs as an intermediate shared notebook when the content should be accessible from both ChatGPT-style work and Codex.

## Codex-Centered Research Loop

1. Put raw ideas into `research/ideas/inbox.md`.
2. Ask Codex to sort them into claims, definitions, examples, proof attempts, and references.
3. Ask Codex to search/list the Drive reference folder for relevant materials.
4. Store literature notes in `research/notes/literature.md` or topic-specific files under `research/notes/`.
5. Summarize each finished research result as Markdown under `artifacts/pdf/`.
6. Publish that Markdown to PDF and mirror the PDF to the Drive backup folder.
7. Commit meaningful milestones with Git.

## Autonomous Discussion Loop

Use [codex-research-automation.md](codex-research-automation.md) for the
repository-first automation design. The recurring prompt lives at
[codex-autonomous-discussion-prompt.md](codex-autonomous-discussion-prompt.md),
and the running state/log lives at
[../records/discussions/autonomous-discussion.md](../records/discussions/autonomous-discussion.md).

The intended division is:

- ChatGPT Project: human-facing research conversation and long exploratory context.
- Repository files: stable source of truth for Codex automation.
- Codex automation: scheduled multi-role discussion, synthesis, and GitHub push.

## Claude Code Review Bridge

Use [claude-code-research-bridge.md](claude-code-research-bridge.md) when you
want Claude Code to act as an independent reviewer for the Codex research loop.
Generate a focused handoff packet with:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\new-claude-code-handoff.ps1 -Focus "Review the next MacNeille finite-model search step."
```

The stable Claude Code prompt is
[claude-code-autonomous-review-prompt.md](claude-code-autonomous-review-prompt.md).
Claude Code should append results to
[../records/discussions/claude-code-review.md](../records/discussions/claude-code-review.md), while Codex
continues to integrate accepted items into the main notes, scripts, and Git
history.

## Project-to-Codex Sync

Use [../research/references/drive-relay.md](../research/references/drive-relay.md) as the operating rule.

- ChatGPT Project remains the exploration space.
- Google Drive holds durable drafts, slides, PDFs, and long-form relay notes.
- `research/references/chatgpt-share-watchlist.csv` holds stable shared links.
- Codex periodically checks changed sources and updates local Markdown notes.

For ordinary ChatGPT shared links, continuing a Project conversation may not update the shared snapshot automatically. Update the share or add a new link when a conversation has new material that Codex should ingest.

For PDF slides or exported slide decks created in ChatGPT Project, place the
file in this local Google Drive sync folder:

```text
C:\Users\20010215fjii\マイドライブ\ChatGPT Project Inbox\My-Reserch-Project
```

Then run:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\sync-chatgpt-project-artifacts.ps1
```

The script imports supported artifacts into
`artifacts/slides/chatgpt-project/`, collects PDFs into `artifacts/pdf/`, and
writes `artifacts/reports/chatgpt-project-artifact-sync.csv`.

## Obsidian-to-Codex Index

The Obsidian vault at `C:\Users\20010215fjii\Documents\Mr.Jikokennobun` contains both research and personal notes. Codex should only index the research roots recorded in [../research/references/obsidian-research-vault.md](../research/references/obsidian-research-vault.md).

Refresh the research-only index with:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\index-obsidian-research.ps1
```

## Discord Bridge

Use [discord-obsidian-codex-bridge.md](discord-obsidian-codex-bridge.md) when
you want Discord to act as the quick-capture and notification surface for daily
reports, todo grooming, and research synthesis. Start with an outbound webhook
digest, then add inbound bot commands only after the repository file contracts
are stable.

Use [daily-activity-automation.md](daily-activity-automation.md) for the current
daily activity sources, Discord bot setup, YouTube capture, and full daily run
command.

## PDF Collection

For a new autonomous-research result, create the Markdown summary first, then run:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\publish-research-output.ps1 -MarkdownPath .\artifacts\pdf\<summary-name>.md
```

The generated PDF is stored in `artifacts/pdf/`, recorded in
`artifacts/pdf/manifest.csv`, and mirrored to the local Google Drive sync folder
when available.

For older or externally generated PDFs, run this from the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\collect-pdfs.ps1
```

The script copies PDFs found under the project into `artifacts/pdf/`, writes
`artifacts/pdf/manifest.csv`, and mirrors the centralized PDF folder to Drive
when the sync folder is available.
