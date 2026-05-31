# PDF Outputs

This directory stores exported discussion notes, papers, handouts, and other
research PDFs.

## Current Files

- `discussion-summary-2026-05-30.pdf`: discussion summary covering the Markdown
  math-display cleanup and the APS/G2-ZOO research state through 2026-05-30.
- `discussion-summary-2026-05-30.md`: source Markdown for the PDF above.
- `project-note-depth-policy-2026-05-30.pdf`: policy note explaining why
  Project-derived Markdown imports must be expanded into detailed mathematical
  notes rather than kept as short summaries.
- `residuated_APS_principles.pdf`: externally supplied PDF on residuated APS
  principles, added from the local Downloads folder on 2026-05-31.

## Workflow

Every autonomous research result should have both:

- a source Markdown file in this directory;
- a generated PDF in this directory.

Publish a Markdown summary with:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\publish-research-output.ps1 -MarkdownPath .\artifacts\pdf\<summary-name>.md
```

The script also updates `manifest.csv` and mirrors the PDF to the local Google
Drive backup folder when available. Git PDFs should remain in Git even after the
Drive backup succeeds.

## Quality Gate

A PDF summary should point to the durable Markdown or TeX source that contains
the mathematical details. For research notes, use
`../../docs/research-note-quality-standard.md` as the minimum checklist:
definitions, named claims, proof sketches, examples or checker tasks, and open
problems.
