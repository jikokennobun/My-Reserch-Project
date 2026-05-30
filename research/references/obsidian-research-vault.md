# Obsidian Research Vault

Vault path:

`$HOME\Documents\Mr.Jikokennobun`

This is an Obsidian-style vault that includes both research notes and personal notes. Codex should only index the research-related roots listed below.

## Included Roots

- `Research`
- `Research-memo`
- `References`
- `Logic & Logic`
- `Proof_memo`
- `Tex`
- `研究紹介`

## Excluded by Policy

- Daily logs
- Personal life notes
- Mental/health notes
- Financial/life-planning notes
- Images and assets
- Non-research creative notes

`Logic & Logic` is included because it contains research notes, but the indexing script excludes obviously personal or creative titles such as `自己省察`, `妄想`, `Song`, and `書きたい本`.

## Generated Indexes

- [../notes/obsidian-research-index.md](../notes/obsidian-research-index.md)
- [obsidian-research-index.csv](obsidian-research-index.csv)

## Update Command

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\index-obsidian-research.ps1
```
