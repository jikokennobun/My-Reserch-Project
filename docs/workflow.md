# Research Workflow

## Recommended Roles

- ChatGPT Project: broad discussion, brainstorming, and long conversational exploration.
- Codex: repository work, file organization, literature indexing, scripts, TeX/PDF generation, and Git-tracked research artifacts.
- Google Drive: reference PDFs and generated final PDFs.
- Obsidian: daily reading/writing interface over Markdown files.
- VSCode: precise editing, TeX, Git, and code work.

## ChatGPT Project Access

Codex cannot directly open a private ChatGPT Project as a folder. Use one of these bridges:

1. Paste important ChatGPT Project outputs into `ideas/inbox.md`.
2. Share a ChatGPT conversation link and ask Codex to extract or summarize it.
3. Export/copy project notes into Markdown files in this repository.
4. Use Google Drive Docs as an intermediate shared notebook when the content should be accessible from both ChatGPT-style work and Codex.

## Codex-Centered Research Loop

1. Put raw ideas into `ideas/inbox.md`.
2. Ask Codex to sort them into claims, definitions, examples, proof attempts, and references.
3. Ask Codex to search/list the Drive reference folder for relevant materials.
4. Store literature notes in `notes/literature.md` or topic-specific files under `notes/`.
5. Compile or export results into `outputs/pdf/`.
6. Commit meaningful milestones with Git.

## Autonomous Discussion Loop

Use [codex-research-automation.md](codex-research-automation.md) for the
repository-first automation design. The recurring prompt lives at
[codex-autonomous-discussion-prompt.md](codex-autonomous-discussion-prompt.md),
and the running state/log lives at
[../logs/autonomous-discussion.md](../logs/autonomous-discussion.md).

The intended division is:

- ChatGPT Project: human-facing research conversation and long exploratory context.
- Repository files: stable source of truth for Codex automation.
- Codex automation: scheduled multi-role discussion, synthesis, and GitHub push.

## Project-to-Codex Sync

Use [../references/drive-relay.md](../references/drive-relay.md) as the operating rule.

- ChatGPT Project remains the exploration space.
- Google Drive holds durable drafts, slides, PDFs, and long-form relay notes.
- `references/chatgpt-share-watchlist.csv` holds stable shared links.
- Codex periodically checks changed sources and updates local Markdown notes.

For ordinary ChatGPT shared links, continuing a Project conversation may not update the shared snapshot automatically. Update the share or add a new link when a conversation has new material that Codex should ingest.

## Obsidian-to-Codex Index

The Obsidian vault at `C:\Users\20010215fjii\Documents\Mr.Jikokennobun` contains both research and personal notes. Codex should only index the research roots recorded in [../references/obsidian-research-vault.md](../references/obsidian-research-vault.md).

Refresh the research-only index with:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\index-obsidian-research.ps1
```

## PDF Collection

Run this from the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\collect-pdfs.ps1
```

The script copies PDFs found under the project into `outputs/pdf/` and writes `outputs/pdf/manifest.csv`.
