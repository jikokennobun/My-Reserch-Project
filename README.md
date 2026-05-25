# My-Reserch-Project

Codex, VSCode, Obsidian, ChatGPT, and Google Driveをつなぐための研究ワークスペースです。

## Entry Points

- [index.md](index.md): 研究全体の入口
- [ideas/inbox.md](ideas/inbox.md): 思いつき・会話ログ・断片の投入口
- [definitions.md](definitions.md): APS/G2-ZOOの基本定義
- [open_problems.md](open_problems.md): 未解決問題リスト
- [bibliography.md](bibliography.md): 文献リスト
- [notes/literature.md](notes/literature.md): 文献メモ
- [references/drive.md](references/drive.md): Google Drive参考文献フォルダ
- [references/research-drive.md](references/research-drive.md): Google Drive研究成果フォルダ
- [references/drive-relay.md](references/drive-relay.md): ChatGPT Project/Drive/Codex同期ルール
- [references/chatgpt-share-watchlist.csv](references/chatgpt-share-watchlist.csv): ChatGPT共有リンク監視リスト
- [references/obsidian-research-vault.md](references/obsidian-research-vault.md): Obsidian研究Vault連携ルール
- [docs/claude-code-research-bridge.md](docs/claude-code-research-bridge.md): Claude Code連携ルール
- [logs/claude-code-review.md](logs/claude-code-review.md): Claude Codeレビュー記録
- [notes/obsidian-research-index.md](notes/obsidian-research-index.md): Obsidian研究ノート索引
- [outputs/pdf/](outputs/pdf/): 生成・集約したPDF
- [logs/research-log.md](logs/research-log.md): 作業ログ
- [models/](models/): 有限APS/preAPSモデル
- [scripts/collect-pdfs.ps1](scripts/collect-pdfs.ps1): ローカルPDF集約スクリプト
- [scripts/check-chatgpt-shares.ps1](scripts/check-chatgpt-shares.ps1): ChatGPT共有リンク変更検出スクリプト
- [scripts/index-obsidian-research.ps1](scripts/index-obsidian-research.ps1): Obsidian研究ノート索引生成スクリプト
- [scripts/new-claude-code-handoff.ps1](scripts/new-claude-code-handoff.ps1): Claude Codeハンドオフ生成スクリプト

## Workflow

1. ChatGPT/Gemini/Claude/Codexで出たアイデアは、まず `ideas/inbox.md` に入れる。
2. Codexで整理するときに、`ideas/` から `notes/` や `drafts/` へ移す。
3. 文献参照はGoogle Driveの参考文献フォルダを主ソースにする。
4. 生成したPDFは `outputs/pdf/` に集約する。
5. 重要な作業は `logs/research-log.md` に日付つきで残す。

## Commands

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\collect-pdfs.ps1
```

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check-chatgpt-shares.ps1
```

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\index-obsidian-research.ps1
```

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\new-claude-code-handoff.ps1 -Focus "Review the next MacNeille finite-model search step."
```
