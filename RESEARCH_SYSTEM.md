# 半自動研究システム v2 — Command Center

このファイルが、渋谷伊織とエージェント群の共通の窓口です。

## 今ここから始める

1. [active goal](research/goals/active.md) で「今回どこまで進めれば終了か」を確認する。
2. [idea inbox](research/ideas/inbox.md) または [literature inbox](research/literature/inbox/README.md) から一件を選ぶ。
3. 問題として扱える段階なら [problem card](research/templates/problem.md) に定式化する。
4. 研究周回を開始する。

```powershell
python .\code\scripts\research_system.py status
python .\code\scripts\research_system.py init-cycle --goal RSYS-001 --focus "今回の焦点"
```

5. 周回の成果は二名の独立査読を通し、採択・要修正・棄却・保留のいずれかを明示する。
6. 採択された内容だけを論文・スライド・恒久ノートへ昇格する。
7. 周回終了時に、研究内容の反芻とシステム改善記録を別々に残す。

## 正本と役割

| 対象 | 正本 | 役割 |
| --- | --- | --- |
| 研究の意味・動機・方向 | `research/meta/` | なぜこの研究をするか |
| Goal | `research/goals/` | 有限の終了条件を持つ作業単位 |
| 生の着想 | `research/ideas/` | まだ主張しない探索材料 |
| 定式化済み問題 | `research/problems/` と `research/open_problems.md` | 仮定、問い、判定基準、反例条件 |
| 文献メタデータ・読書状態 | `research/literature/` | DOI/arXiv/Drive IDを含む文献台帳 |
| 数学的研究ノート | `research/notes/` | 定義、主張、証明、反例、計算 |
| 周回・議論・査読・反芻 | `records/` | 判断過程と異論を含む追跡記録 |
| 実行可能な検証 | `code/` | チェッカー、探索、再現手順 |
| 論文、スライド、PDF | `artifacts/` | 人に渡す成果物 |

Git/GitHub がテキスト・コード・来歴の正本、Obsidian が日常の閲覧編集面、Google Drive が参考資料原本と大容量成果物の資料庫です。Driveの資料は複製せず、安定した `fileId` とURLを文献カードへ記録します。

## よく使うコマンド

```powershell
# 構造と必須ファイルの検査
python .\code\scripts\research_system.py validate

# 文献候補を自動収集（arXiv、OpenAlex）
python .\code\scripts\research_system.py collect

# APIを呼ばず収集設定だけ確認
python .\code\scripts\research_system.py collect --dry-run

# Obsidian研究領域の索引更新
powershell -ExecutionPolicy Bypass -File .\code\scripts\index-obsidian-research.ps1
```

OpenAlexを継続利用する場合は `.env` または実行環境へ `OPENALEX_API_KEY` を設定します。自動収集はPDFを無断転載せず、まずアクセス可能な書誌情報と原文リンクだけを候補箱へ入れます。

## エージェント構成

役割契約は [.agents/](.agents/) にあります。標準周回は次の順です。

1. Leader/Conductor が Goal、範囲、終了条件、採用基準を固定。
2. Ideator A/B が独立案を出し、相互批判後に統合案を作る。
3. Formulator が定義・仮定・主張・反例条件へ変換。
4. Theory Maker と Problem Solver A/B が証明路線と検証路線を分担。
5. Skeptic が全段階を横断して疑義と停止条件を記録。
6. Primary/Secondary Reviewer が独立査読。
7. Writer が章単位で雛形→主張地図→草稿→査読→改稿を反復。
8. Archivist がリンク、状態、判断理由、次の一手を正本へ反映。

## Goal運用

- 長い作業では Codex の `\goal` と `research/goals/active.md` を同じ目的に揃える。
- 一度にアクティブな研究Goalは一件。脇道は idea/problem card に退避する。
- Goalには成果物ではなく、検証可能な終了条件を書く。
- 「難しい」だけでは blocked にしない。必要な入力・権限・外部変化を特定する。
- 完了前に二名査読、再現性、反芻、判断記録を確認する。

## 詳細設計

- [Architecture and operations](docs/research-system-v2.md)
- [Machine-readable configuration](config/research-system.json)
- [Research-cycle prompt](docs/prompts/research-cycle.md)
- [Templates](research/templates/README.md)

