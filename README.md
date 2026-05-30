# My-Reserch-Project

Codex, VSCode, Obsidian, ChatGPT, and Google Driveをつなぐための研究ワークスペースです。

## Directory Map

| Directory | Role |
| --- | --- |
| [research/](research/) | 研究本文、定義、未解決問題、文献、アイデア、参照情報 |
| [records/](records/) | 作業ログ、同期ログ、自律議論、Claude Codeレビュー |
| [artifacts/](artifacts/) | PDF、JSONレポート、ハンドオフ、今後のslides/tex成果物 |
| [code/](code/) | 検証スクリプト、生成スクリプト、機械可読モデル |
| [docs/](docs/) | 運用手順、Codex/Claude連携プロンプト |

## Main Entry Points

- [index.md](index.md): 研究全体の入口
- [research/definitions.md](research/definitions.md): APS/G2-ZOOの基本定義
- [research/open_problems.md](research/open_problems.md): 未解決問題リスト
- [research/notes/](research/notes/): 研究ノート
- [records/discussions/autonomous-discussion.md](records/discussions/autonomous-discussion.md): 自律議論ログ
- [records/logs/research-log.md](records/logs/research-log.md): 作業ログ
- [artifacts/pdf/discussion-summary-2026-05-30.pdf](artifacts/pdf/discussion-summary-2026-05-30.pdf): 最新の議論要約PDF
- [code/models/README.md](code/models/README.md): 有限APS/preAPSモデル

## Storage Rules

1. 研究本文と整理済みノートは `research/` に置く。
2. 作業ログ、同期ログ、議論履歴は `records/` に置く。
3. PDF、TeX、スライド、JSONレポートなどの成果物は `artifacts/` に置く。
4. スクリプトや検証モデルなど、実行・検証に使うものは `code/` に置く。
5. 運用手順やエージェント向けプロンプトは `docs/` に置く。

## Common Commands

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\publish-research-output.ps1 -MarkdownPath .\artifacts\pdf\<summary-name>.md
```

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\normalize-markdown-math.ps1
```

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\collect-pdfs.ps1
```

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\check-chatgpt-shares.ps1
```

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\index-obsidian-research.ps1
```
