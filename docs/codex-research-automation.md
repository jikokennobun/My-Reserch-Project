# Codex Research Automation

This file defines the repository-side workflow for using Codex as an
autonomous research discussion engine while keeping ChatGPT Projects as the
human-facing research workspace.

## Architecture

- ChatGPT Project is the exploration workspace for long conversational work.
- This repository is the durable research ledger.
- Codex runs scheduled discussion passes against the repository files.
- Every autonomous research result is summarized in Markdown and published as a
  PDF artifact.
- Claude Code can optionally run independent review passes against the same
  repository state; see [claude-code-research-bridge.md](claude-code-research-bridge.md).
- GitHub is the shared archive for generated notes, logs, synthesis, and PDF
  artifacts; Google Drive is the backup mirror for final PDFs.

Codex should not assume it can directly read private ChatGPT Project state.
Project material must enter the repository through one of these bridges:

1. Paste important Project output into `research/ideas/inbox.md`.
2. Add or refresh a `https://chatgpt.com/share/...` link in
   `research/references/chatgpt-share-watchlist.csv`.
3. Export ChatGPT data and place the relevant JSON/Markdown extract in the
   repository.
4. Put a durable relay note in Google Drive and mirror the summary into this
   repository.
5. Put ChatGPT Project-generated PDFs or slide decks in the local Google Drive
   artifact inbox, then import them with
   `code/scripts/sync-chatgpt-project-artifacts.ps1`.

## Discussion Loop

Each automated pass should:

1. Read `records/discussions/autonomous-discussion.md` to find the current state.
2. Review `research/ideas/research-questions.md`, `research/open_problems.md`, `research/definitions.md`,
   and the most relevant topic notes under `research/notes/`.
3. Run a compact multi-role discussion:
   - Proposer: formulates the strongest next conjecture or construction.
   - Skeptic: searches for hidden assumptions and likely counterexamples.
   - Formalist: asks what definitions, lemmas, and proof obligations are needed.
   - Archivist: converts the discussion into repository-ready notes.
4. Append one dated iteration to `records/discussions/autonomous-discussion.md`.
5. Update `research/ideas/research-questions.md` or a topic note only when the discussion
   produces a concrete new question, conjecture, definition, or proof task.
6. Add a short entry to `records/logs/research-log.md`.
7. Write a concise Markdown publication summary under `artifacts/pdf/`.
8. Run `code/scripts/publish-research-output.ps1` for that Markdown file so the
   result is always converted to PDF and collected under `artifacts/pdf/`.
9. Commit and push the resulting files so GitHub receives the research trace.

When a Claude Code review exists in `records/discussions/claude-code-review.md`, Codex should
read the newest review before choosing the next pass focus, then explicitly
either incorporate, defer, or reject its suggested repository updates.

## Output Standard

Each iteration should be concise but useful. Prefer this shape:

- Focus: the question or note being advanced.
- Proposer: the best positive move.
- Skeptic: the most important objection.
- Formalist: definitions or lemmas needed.
- Archivist: concrete repository updates.
- Next step: one action for the next pass.

The loop should avoid inventing bibliographic facts. When it needs external
sources, it should record the source gap and create a follow-up task instead of
guessing.

## Publication Rule

Research output is not complete until it has both a Markdown source and a PDF:

1. Write the source Markdown in `artifacts/pdf/`.
2. Run:

   ```powershell
   powershell -ExecutionPolicy Bypass -File .\code\scripts\publish-research-output.ps1 -MarkdownPath .\artifacts\pdf\<summary-name>.md
   ```

3. Confirm that the generated PDF and `manifest.csv` are in `artifacts/pdf/`.
4. If Google Drive for Desktop is available, confirm that the PDF was mirrored
   to `C:\Users\20010215fjii\マイドライブ\GitHub PDF Backup\My-Reserch-Project\artifacts\pdf`.
5. Keep the Git copy and the Drive backup; Drive is an additional backup, not a
   replacement for Git.

For older or externally generated PDFs, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\collect-pdfs.ps1
```

This keeps all repository-visible PDFs gathered under `artifacts/pdf/` and
mirrors that folder to Drive when the sync folder is available.

## ChatGPT Project Artifact Import

ChatGPT Project-generated PDF slides and exported decks should be placed in:

```text
C:\Users\20010215fjii\マイドライブ\ChatGPT Project Inbox\My-Reserch-Project
```

Then run:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\sync-chatgpt-project-artifacts.ps1
```

The script imports `.pdf`, `.ppt`, `.pptx`, and `.odp` files into
`artifacts/slides/chatgpt-project/`. PDF files are also collected into
`artifacts/pdf/` so the repository keeps one central PDF shelf.

## Current Limits

- `https://chatgpt.com/share/...` links have recently failed from this local
  PowerShell environment with a remote-server-unreachable error.
- ChatGPT Project files are not automatically visible to Codex.
- ChatGPT Tasks do not reliably solve this bridge because Project files are not
  available to Tasks in the same way they are available inside Project chats.

The stable path is therefore repository-first: move any Project insight that
matters into Markdown or a watched relay source, then let Codex develop it.
