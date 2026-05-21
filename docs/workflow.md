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

## PDF Collection

Run this from the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\collect-pdfs.ps1
```

The script copies PDFs found under the project into `outputs/pdf/` and writes `outputs/pdf/manifest.csv`.
