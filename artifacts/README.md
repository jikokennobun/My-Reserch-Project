# Artifacts

Generated and exported research artifacts live here.

## Layout

- [pdf/](pdf/): compiled papers, handouts, discussion summaries, and collected PDFs.
- [reports/](reports/): machine-generated JSON/CSV checker reports.
- [handoffs/](handoffs/): generated one-off handoff packets for external review.
- [slides/](slides/): slide decks and exported slide material.
- [tex/](tex/): TeX sources and compiled paper drafts.

## Publication Rule

Autonomous research results should be written first as Markdown under
`pdf/`, then published with:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\publish-research-output.ps1 -MarkdownPath .\artifacts\pdf\<summary-name>.md
```

This creates the PDF in `pdf/`, updates `pdf/manifest.csv`, and mirrors the PDF
to the local Google Drive backup folder when available.

## Current Highlights

- [pdf/discussion-summary-2026-05-30.pdf](pdf/discussion-summary-2026-05-30.pdf):
  discussion summary covering the Markdown math-display cleanup and APS/G2-ZOO
  research state through 2026-05-30.
- [reports/g2-zoo-M4-G2FG2FP.json](reports/g2-zoo-M4-G2FG2FP.json):
  checker report for the 4-element non-degenerate G2+FG2+FP-synt witness.
- [reports/front-width-residual-formula-check.json](reports/front-width-residual-formula-check.json):
  checker report for the orthogonal front-width residual formula.
