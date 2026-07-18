# 半自動研究システム v2 — Architecture and Operations

## 1. 設計原則

このシステムは研究を全自動化しない。自動化するのは収集、索引、差分検出、雛形生成、機械検査、定期的な再提示である。研究上の主張、採否、優先順位、公開は、人間が確認可能な記録を経て決める。

中心単位は「会話」ではなく研究オブジェクトである。各オブジェクトはID、状態、出典、親Goal、根拠、反対証拠、次の判定可能な行動を持つ。

## 2. 研究オブジェクト

| Object | ID例 | 状態遷移 | 完了条件 |
| --- | --- | --- | --- |
| Goal | `GOAL-20260718-01` | proposed → active → blocked/completed/abandoned | 終了条件を満たし査読済み |
| Literature | DOI/arXiv/OpenAlex/Drive ID | candidate → triaged → reading → cited/rejected | 本文へのアクセスと採否理由あり |
| Idea | `IDEA-20260718-01` | inbox → discussed → formulated/rejected/parked | problem cardへ移すか理由付き終了 |
| Problem | `PROB-20260718-01` | draft → formulated → active → partial/resolved/refuted | 仮定・問い・成功/反例条件が明確 |
| Claim | `CLM-...` | conjecture → tested → reviewed → accepted/refuted | 証明または反例と独立査読 |
| Research cycle | `CYCLE-...` | scoped → exploring → reviewing → integrated | 二名査読、反芻、正本更新 |
| Chapter | `CH-...` | skeleton → claim-map → draft → reviewed → revised | 根拠リンクと未解決マーカーを確認 |
| Improvement | `IMP-...` | proposed → tested → accepted/rejected | 意図・変更・観測結果・戻し方あり |

## 3. 一周の状態機械

```mermaid
flowchart LR
    A["Goalを固定"] --> B["資料・Obsidian・過去議論を収集"]
    B --> C["Ideator A/Bが独立提案"]
    C --> D["Formulatorが問題化"]
    D --> E["Theory Maker / Solverが攻撃"]
    E --> F["Skepticが反証・逸脱検査"]
    F --> G["主査・副査が独立査読"]
    G -->|要修正| D
    G -->|採択| H["Writerが章単位で統合"]
    G -->|棄却・保留| I["理由付きで保存"]
    H --> J["研究反芻"]
    I --> J
    J --> K["システム自己改善記録"]
    K --> L["正本更新・次Goal"]
```

### 必須停止条件

- 引用元へ到達できないのに、その内容を事実として使おうとしている。
- 定義が役割間で一致していない。
- 主張と計算機実験の射程を混同している。
- Skepticの重大異論が未解決なのに「成果」として公開しようとしている。
- 主査と副査が同じ推論文を共有して独立性を失っている。
- Goalの範囲を越えた方向転換を、理由なしで行おうとしている。

## 4. 情報収集

### 自動入口

- arXiv API: 論文、プレプリント、サーベイ候補。
- OpenAlex: 横断検索、講義ノート・レビュー・関連研究候補。
- Google Drive: 既存参考資料の `fileId`、URL、更新日時、所在。
- Obsidian: 許可された研究フォルダの索引と変更差分。
- GitHub: コード、Issue/PR、実験結果、履歴、定期実行。

自動収集物はすべて `candidate` であり、内容を読まずに引用してはならない。重複判定は DOI、arXiv ID、OpenAlex ID、Drive fileId の順で行う。PDFの保存はライセンスとアクセス権を確認し、Gitへ大容量原本を重複保存しない。

### 収集結果の優先度

候補は次の観点で人またはArchivistが評価する。

1. Active Goalとの直接関係。
2. 現在の定義・未解決問題に与える差分。
3. サーベイ・講義資料としての地図作成能力。
4. 原文アクセス可能性。
5. 反証、既知結果、重複研究を示す可能性。

## 5. 連携境界

### Obsidian

Obsidianは表示・検索・手書き編集の面であり、Git管理Markdownと研究用Vault索引をつなぐ。個人・健康・生活メモは既存の除外規則を維持する。エージェントが人物像の根拠に利用できるのは、明示的に許可された研究領域だけである。

### GitHub

GitHubは来歴と再現可能性の正本である。自動収集は `.github/workflows/research-intake.yml` で実行できる。自動コミットは候補書誌に限定し、数学的主張・査読判断・公開成果は自動承認しない。

### Google Drive

Driveは参考資料原本と大容量成果物の資料庫である。Driveの安定した fileId は名前変更後も参照キーとして使う。ローカル文献カードには `drive_file_id`、`url`、`access_checked_at` を記録する。検索は対象フォルダを狭め、更新差分には `modifiedTime` を使う。

## 6. 査読

主査は正しさ、仮定、証明の穴、再現性を担当する。副査は新規性、位置づけ、説明可能性、別解・反例方向を担当する。両者は同じ結論へ収束する義務を持たない。

判定は `accept / minor-revision / major-revision / reject / hold`。Leaderは異論を削除せず、採否理由と未解決異論を統合記録へ残す。計算機検証は「有限範囲で反例なし」等の正確な射程で表現する。

## 7. 論文・スライド

一回で論文全体を書かない。章ごとに次の版を作る。

1. skeleton: 目的、読者、節見出し、依存する主張。
2. claim-map: 各段落が支える主張と根拠リンク。
3. draft: 本文。未確認箇所は `TODO[claim]` 等で明示。
4. reviewed: 主査・副査コメントを章単位で受ける。
5. revised: 対応表を残して改稿。

`.tex` を成果物の正本、`.pdf` を配布版とする場合でも、対応するGoal、problem、claim、reviewへのリンクを近接するREADMEまたはfront matterへ置く。

## 8. 反芻と自己改善

研究反芻とシステム改善は分ける。

- 研究反芻: なぜこの方向を選んだか、何を見落としたか、結果がGoalや動機をどう変えたか。
- システム改善: どの仕組みが欠陥だったか、変更の意図、観測指標、結果、戻し方。

日次は候補整理、周回終了時は成果反芻、週次はGoal・人物像・逸脱検査、月次は構造と自動化の監査を行う。人物像は断定ではなく、根拠・日付・確信度・反証可能性を持つ更新可能な仮説として保存する。

## 9. 導入順序

1. `validate` と `status` を毎回の開始点にする。
2. 一週間、`RSYS-001` で一件の問題を実際に周回させる。
3. 自動収集候補のノイズ率と見逃しを記録し、検索語を調整する。
4. 二名査読の差分が有用かを反芻する。
5. その後にのみ、通知、Drive差分同期、LLMの定期実行を増やす。

