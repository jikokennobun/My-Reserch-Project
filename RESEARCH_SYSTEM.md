# 半自動研究システム

普段は [CURRENT.md](CURRENT.md) だけを開けばよい。

## 使い方

1. `CURRENT.md` で現在のGoal・問題・ノートを確認する。
2. Codexに「`CURRENT.md` から研究を続けて」と伝える。
3. 結論は研究ノート、未解決事項はproblem card、判断理由はcycleへ残す。
4. 成果は主査・副査の二名査読と反芻を通してから採用する。

状態確認と検査だけは次のコマンドで行う。

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\research.ps1 status
powershell -ExecutionPolicy Bypass -File .\code\scripts\research.ps1 validate
```

## 保存先

| 内容 | 場所 |
| --- | --- |
| 現在の作業 | `CURRENT.md` |
| Goal | `research/goals/` |
| アイデア | `research/ideas/` |
| 定式化した問題 | `research/problems/` |
| 研究ノート | `research/notes/` |
| 文献と原文リンク | `research/literature/` |
| 議論・査読・反芻 | `records/research-cycles/` |
| 論文・スライド・PDF | `artifacts/` |
| 自動処理 | `code/` |

Git/GitHubをテキストと履歴の正本、Obsidianを閲覧・手編集の場所、Google Driveを原資料と大容量成果物の保管場所にする。Drive資料は複製せず、安定したIDとURLを文献カードに記録する。

## 運用原則

- 一度に活動中のGoalは一件だけにする。
- エージェントの役割は必要な場面だけ使い、会話を増やすこと自体を目的にしない。
- 定義、証明済み、計算実験、予想を分ける。
- 論文は章ごとの雛形から育てる。一回で全体を書かない。
- 文体とスライドは簡素にする。[執筆規約](docs/writing-style.md)に従う。
- 研究成果には「なぜ調べたか」と「次に何が変わるか」を添える。
- システム変更は意図、効果の測り方、戻し方を記録する。

詳細は [設計・運用資料](docs/research-system-v2.md) と [機械可読設定](config/research-system.json) に残す。
