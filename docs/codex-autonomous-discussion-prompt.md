# Codex Autonomous Discussion Prompt

Use this as the recurring automation prompt.

Run the next autonomous research discussion pass for this repository.

Read:

- `docs/codex-research-automation.md`
- `records/discussions/autonomous-discussion.md`
- `research/ideas/research-questions.md`
- `research/open_problems.md`
- `research/definitions.md`
- the most relevant topic notes under `research/notes/`

Then perform one compact multi-role discussion using these roles:

- Proposer
- Skeptic
- Formalist
- Archivist

Append the result to `records/discussions/autonomous-discussion.md` using the established
format. Update `research/ideas/research-questions.md`, `research/open_problems.md`, or topic notes
only when there is a concrete new question, conjecture, definition, or proof
task. Add a short dated entry to `records/logs/research-log.md`.

Create a concise Markdown publication summary for the pass under
`artifacts/pdf/`, then publish it as PDF with:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\publish-research-output.ps1 -MarkdownPath .\artifacts\pdf\<summary-name>.md
```

The PDF must remain in `artifacts/pdf/`. When the local Google Drive sync
folder is available, the script also backs it up to
`C:\Users\20010215fjii\マイドライブ\GitHub PDF Backup\My-Reserch-Project\artifacts\pdf`.
Do not delete Git-tracked PDFs after the Drive backup.

Commit the changed research files and push the current branch to GitHub. Keep
the commit message short and specific.

Do not fabricate Project content, paper details, or citation claims. If the
next step depends on inaccessible ChatGPT Project material or a missing source,
record that as a bridge/source gap and propose the smallest useful workaround.
