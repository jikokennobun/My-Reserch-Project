# Slides

Slide decks and exported slide material go here. Slides are presentation
artifacts; the durable mathematical source should still live in
`../pdf/*.md`, `../../research/notes/`, or `../tex/`.

## Role

Use this directory for:

- ChatGPT Project-generated PDF slide exports;
- `.pptx`, `.ppt`, or `.odp` decks;
- rendered presentation PDFs;
- slide handoff material that should be preserved with the repository.

## ChatGPT Project Imports

Put ChatGPT Project-generated PDF slides or exported decks in:

```text
C:\Users\20010215fjii\マイドライブ\ChatGPT Project Inbox\My-Reserch-Project
```

Then run:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\sync-chatgpt-project-artifacts.ps1
```

Imported files are stored in `chatgpt-project/`. PDF imports are also copied to
the central `../pdf/` collection.

## Mathematical Traceability

Each substantial deck should be traceable to a note or summary. If a slide deck
contains a theorem, model, or conjecture not written elsewhere, create or update
a Markdown note before treating the slide as a research source.
