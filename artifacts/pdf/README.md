# PDF Outputs

This directory stores exported discussion notes, papers, handouts, and other
research PDFs.

## Current Files

- `discussion-summary-2026-05-30.pdf`: discussion summary covering the Markdown
  math-display cleanup and the APS/G2-ZOO research state through 2026-05-30.
- `discussion-summary-2026-05-30.md`: source Markdown for the PDF above.

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
