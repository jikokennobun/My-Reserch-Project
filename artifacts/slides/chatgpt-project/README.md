# ChatGPT Project Slide Imports

PDF slides and exported slide decks copied from the local Google Drive inbox are
stored here.

## Purpose

This folder is the repository-side landing zone for slide artifacts created in
ChatGPT Project. It is not the only archive: imported PDFs are also copied into
the central `../../pdf/` collection so they are easy to back up and review.

Each substantial slide artifact should be connected to a Markdown research note
or publication summary. If the deck contains mathematical content that is not
written elsewhere, promote that content into `../../../research/notes/` before
using the deck as evidence.

## Import Path

Default inbox:

```text
C:\Users\20010215fjii\マイドライブ\ChatGPT Project Inbox\My-Reserch-Project
```

Sync command:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\sync-chatgpt-project-artifacts.ps1
```

## Traceability Checklist

After importing, record:

1. source file name;
2. import date;
3. corresponding Markdown note or PDF summary;
4. whether the PDF was also collected in `../../pdf/`.
