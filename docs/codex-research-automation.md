# Codex Research Automation

This file defines the repository-side workflow for using Codex as an
autonomous research discussion engine while keeping ChatGPT Projects as the
human-facing research workspace.

## Architecture

- ChatGPT Project is the exploration workspace for long conversational work.
- This repository is the durable research ledger.
- Codex runs scheduled discussion passes against the repository files.
- Claude Code can optionally run independent review passes against the same
  repository state; see [claude-code-research-bridge.md](claude-code-research-bridge.md).
- GitHub is the shared archive for generated notes, logs, and synthesis.

Codex should not assume it can directly read private ChatGPT Project state.
Project material must enter the repository through one of these bridges:

1. Paste important Project output into `ideas/inbox.md`.
2. Add or refresh a `https://chatgpt.com/share/...` link in
   `references/chatgpt-share-watchlist.csv`.
3. Export ChatGPT data and place the relevant JSON/Markdown extract in the
   repository.
4. Put a durable relay note in Google Drive and mirror the summary into this
   repository.

## Discussion Loop

Each automated pass should:

1. Read `logs/autonomous-discussion.md` to find the current state.
2. Review `ideas/research-questions.md`, `open_problems.md`, `definitions.md`,
   and the most relevant topic notes under `notes/`.
3. Run a compact multi-role discussion:
   - Proposer: formulates the strongest next conjecture or construction.
   - Skeptic: searches for hidden assumptions and likely counterexamples.
   - Formalist: asks what definitions, lemmas, and proof obligations are needed.
   - Archivist: converts the discussion into repository-ready notes.
4. Append one dated iteration to `logs/autonomous-discussion.md`.
5. Update `ideas/research-questions.md` or a topic note only when the discussion
   produces a concrete new question, conjecture, definition, or proof task.
6. Add a short entry to `logs/research-log.md`.
7. Commit and push the resulting files so GitHub receives the research trace.

When a Claude Code review exists in `logs/claude-code-review.md`, Codex should
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

## Current Limits

- `https://chatgpt.com/share/...` links have recently failed from this local
  PowerShell environment with a remote-server-unreachable error.
- ChatGPT Project files are not automatically visible to Codex.
- ChatGPT Tasks do not reliably solve this bridge because Project files are not
  available to Tasks in the same way they are available inside Project chats.

The stable path is therefore repository-first: move any Project insight that
matters into Markdown or a watched relay source, then let Codex develop it.
