# Slides

Slide decks and exported slide material go here.

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
