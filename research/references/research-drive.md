# Google Drive Research Folder

Research folder:

https://drive.google.com/drive/folders/1gL0PZ7jfej58l3MUDV-fdiLrF_PsIuDC?usp=sharing

This folder is for research outputs, slides, drafts, and AI-generated materials. It is distinct from the broader reference literature folder in [drive.md](drive.md).

## Top-Level Structure

- Claude: https://drive.google.com/drive/folders/1izaXlfFOgOKPThQdTIcPzkeEt1lQNUEe
- Gemini: https://drive.google.com/drive/folders/1boq_8q2sAiQ-PDvN1Mxa2QyZPYj1C58W
- Paper: https://drive.google.com/drive/folders/1YmDsKbuokr_5GNIEUr1gv6nDQvdJFoVN
- Others: https://drive.google.com/drive/folders/1lnsIXF6KxEFyLhxpV3ECLGXSyJFj-gp9
- Slide: https://drive.google.com/drive/folders/1yFvEYhhoN3-9EsKwV8b1cu1roxt_Se9c
- ロジックセミナー: https://drive.google.com/drive/folders/1Usavglr4EcdukaGY3ZLU_e-CKQ_gcsdK
- 学振: https://drive.google.com/drive/folders/17O_NNebJx3SrIh5xvoxrkgTH5QnlpOGQ
- 鹿島研究室_セミナー: https://drive.google.com/drive/folders/1VXbvQwD4FBc-Wj0CIWqtvPX9b-O4nFKt

## Paper Folder Snapshot

- Monograph
- algebraic_reverse_math_g2_aps.pdf
- aps_g2_zoo_research_notes_lualatex_thesis_expanded.pdf
- aps_g2_zoo_research_notes_lualatex_proof_complete.pdf
- aps_dissertation_lualatex.pdf
- aps_g2_zoo_research_notes_lualatex.pdf

### Monograph (current)

- aps_g2_zoo_monograph_lualatex.pdf
- APS_G2_Algebraic_Reverse_Mathematics_Monograph.pdf
- aps_monograph.pdf
- aps_monograph_xelatex.pdf

## Slide Folder Snapshot

- beklemishev_shamkanov_abstract_g2_beamer.pdf
- pakhomov_visser_self_comprehension_beamer.pdf
- aps_g2_algebraic_reverse_math_v5.pdf
- aps_g2_algebraic_reverse_math_v4.pdf
- aps_g2_algebraic_reverse_math_v3.pdf
- aps_g2_algebraic_reverse_math_v2.pdf
- aps_g2_algebraic_reverse_math.pdf
- 01.pdf
- wakate.pdf

## AI Output Folders

Gemini includes:

- 不完全性現象の代数的逆数学_総合モノグラフ_コピー.pdf
- thesis_コピー.pdf
- Incompleteness_Reverse_Mathematics_Grand_Monograph_v3_コピー.pdf
- Incompleteness_Phenomena_Grand_Monograph_コピー.pdf
- Incompleteness_Algebraic_Reverse_Mathematics_Thesis_コピー.pdf
- Mathematical_Logic_Document_コピー.pdf
- aps_report_コピー.pdf

Claude includes:

- files:
  - APS_dissertation.pdf
  - APS_dissertation.tex
  - references.bib

## Usage

- Use this folder as the source of generated drafts, slides, and research outputs.
- Use [drive.md](drive.md) as the source of external reference literature.
- When importing ideas from a PDF or slide deck, create a note under `research/notes/` and link back to the Drive file here.
- When creating a new local PDF from this repository, write its Markdown source
  under `artifacts/pdf/` and run
  `code/scripts/publish-research-output.ps1`. This keeps the PDF under
  `artifacts/pdf/` and mirrors it to the local Google Drive backup folder when
  available.
- When exporting PDF slides or slide decks from ChatGPT Project, place them in
  `C:\Users\20010215fjii\マイドライブ\ChatGPT Project Inbox\My-Reserch-Project`
  and run `code/scripts/sync-chatgpt-project-artifacts.ps1` to import them into
  the repository.

## Local Drive Backup

- 2026-05-30: Backed up GitHub PDF artifacts to the local Google Drive sync
  folder `C:\Users\20010215fjii\マイドライブ\GitHub PDF Backup\My-Reserch-Project\artifacts\pdf`.
  Current file: `discussion-summary-2026-05-30.pdf`
  (`sha256 73d73bc4ad501b08f9e68b30f8a8a429a55b122b3364cb32d2b0d054f787694a`).
- 2026-05-30: Added `code/scripts/publish-research-output.ps1` as the standard
  Markdown-to-PDF publication step for autonomous research outputs.
- 2026-05-30: Google Drive connector search did not list
  `discussion-summary-2026-05-30.pdf` immediately after the local sync copy, so
  the verified local Drive folder hash is the current backup proof until Drive
  indexing catches up.
- 2026-05-30: Added a ChatGPT Project artifact inbox workflow for importing
  generated PDF slides and slide decks from local Google Drive sync into
  `artifacts/slides/chatgpt-project/` and `artifacts/pdf/`.
