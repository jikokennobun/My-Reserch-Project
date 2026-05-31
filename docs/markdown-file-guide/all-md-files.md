# All Markdown Files

作成日: 2026-05-31

この索引は、現時点の Markdown ファイルをディレクトリ別に説明するものです。
研究本文、運用資料、ログ、PDFソース、モデル解説が混在しても迷わないように、
各ファイルの役割と読む場面を短く記しています。

## Root

| File | 役割 | 読む場面 |
| --- | --- | --- |
| [README.md](../../README.md) | repository 全体の入口。ディレクトリの役割と主要コマンドを示す。 | 最初に全体構造を確認するとき。 |
| [index.md](../../index.md) | 研究索引。主要研究ノート、参照、ログへのリンクを集約。 | APS/G2-ZOO 研究の入口を探すとき。 |

## Docs

| File | 役割 | 読む場面 |
| --- | --- | --- |
| [docs/workflow.md](../workflow.md) | ChatGPT Project, Codex, Claude Code, Drive, Obsidian の研究フロー。 | 研究運用の手順を確認するとき。 |
| [docs/research-note-quality-standard.md](../research-note-quality-standard.md) | 研究ノートの最低品質基準。 | Project由来ノートや自動研究ノートを作る前。 |
| [docs/codex-research-automation.md](../codex-research-automation.md) | Codex 自動研究・PDF化・Driveバックアップの運用設計。 | 自動化の挙動を調整するとき。 |
| [docs/codex-autonomous-discussion-prompt.md](../codex-autonomous-discussion-prompt.md) | 自律議論ループ用プロンプト。 | Codex の議論パスを実行・修正するとき。 |
| [docs/claude-code-research-bridge.md](../claude-code-research-bridge.md) | Claude Code と Codex の分担・連携ルール。 | 外部レビューや別エージェント連携を行うとき。 |
| [docs/claude-code-autonomous-review-prompt.md](../claude-code-autonomous-review-prompt.md) | Claude Code レビュー用プロンプト。 | Claude Code に研究レビューを依頼するとき。 |
| [docs/markdown-file-guide/README.md](README.md) | この解説資料フォルダの入口。 | Markdown 解説資料を読むとき。 |
| [docs/markdown-file-guide/all-md-files.md](all-md-files.md) | 全 Markdown ファイルの一覧解説。 | ファイルの意味を一括で確認するとき。 |
| [docs/markdown-file-guide/research-notes-guide.md](research-notes-guide.md) | 研究ノート群のテーマ別詳解。 | 研究内容の関係を追うとき。 |
| [docs/markdown-file-guide/operations-and-artifacts-guide.md](operations-and-artifacts-guide.md) | 運用・ログ・成果物・コード系 Markdown の詳解。 | 研究以外の管理ファイルを理解するとき。 |

## Research Core

| File | 役割 | 読む場面 |
| --- | --- | --- |
| [research/README.md](../../research/README.md) | `research/` 配下の構成と研究ノート基準。 | 研究資料の置き場所を確認するとき。 |
| [research/definitions.md](../../research/definitions.md) | APS/G2-ZOO の共通定義集。 | 記法や基本概念を確認するとき。 |
| [research/open_problems.md](../../research/open_problems.md) | 未解決問題・部分解決・次の検査課題。 | 次に何を証明/探索するか決めるとき。 |
| [research/bibliography.md](../../research/bibliography.md) | 文献カテゴリと参照アンカー。 | 研究ノートに文献根拠を足すとき。 |
| [research/ideas/inbox.md](../../research/ideas/inbox.md) | 未整理アイデアの受け皿。 | まだノート化していない着想を確認するとき。 |
| [research/ideas/research-questions.md](../../research/ideas/research-questions.md) | 研究質問の短期・後回し・解決済みリスト。 | 自動議論や検査の題材を選ぶとき。 |

## Research Notes

| File | 役割 | 読む場面 |
| --- | --- | --- |
| [analytic-aps.md](../../research/notes/analytic-aps.md) | APS を解析的・位相的に読む初期構想。 | 解析/トポロジー方向の入口として。 |
| [aps-arithmetic-realization-kernel.md](../../research/notes/aps-arithmetic-realization-kernel.md) | 算術から APS への実現写像と kernel/faithfulness の問題。 | APS と算術的完全性を比較するとき。 |
| [aps-cardinal-invariants-fixed-points.md](../../research/notes/aps-cardinal-invariants-fixed-points.md) | 固定点スペクトルや基数的不変量のメモ。 | 固定点の個数・型で分類したいとき。 |
| [aps-monad-computational-effects.md](../../research/notes/aps-monad-computational-effects.md) | APS の provability/refutability を monad/effect として読むノート。 | Curry-Howard-Moggi 的解釈を考えるとき。 |
| [bs16-fiber-residuated-aps.md](../../research/notes/bs16-fiber-residuated-aps.md) | BS16 カット除去を fibered residuated APS として再構成。 | Res-APS と G2 の中心線を読むとき。 |
| [chatgpt-imports-2026-05-22.md](../../research/notes/chatgpt-imports-2026-05-22.md) | 2026-05-22 の ChatGPT共有リンク取り込み索引。 | 初期インポートの由来を追うとき。 |
| [completion-and-fixed-points.md](../../research/notes/completion-and-fixed-points.md) | MacNeille 完備化と固定点反映問題。 | completion fixed point と syntax fixed point の差を見るとき。 |
| [consistency-notions-hierarchy.md](../../research/notes/consistency-notions-hierarchy.md) | 算術的無矛盾性概念の階層。 | Con, SCon, WSCon などを整理するとき。 |
| [derivability-conditions.md](../../research/notes/derivability-conditions.md) | 導出可能性条件の整理。 | provability predicate の条件を確認するとき。 |
| [formalized-g2-implicational-aps.md](../../research/notes/formalized-g2-implicational-aps.md) | implicational APS 内の formalized/local G2。 | G2 と FG2 の中間原理を扱うとき。 |
| [g2-aps-zoo-classification.md](../../research/notes/g2-aps-zoo-classification.md) | G2-ZOO/APS-ZOO の分類軸。 | 有限モデルの分類表を作るとき。 |
| [g2-fg2-hierarchy.md](../../research/notes/g2-fg2-hierarchy.md) | G2/FG2/nFG2 階層と有限モデル証人。 | この研究の有限モデル中核を読むとき。 |
| [g2-zoo-arithmetic.md](../../research/notes/g2-zoo-arithmetic.md) | 算術版 G2 変種の比較。 | Jeroslow/Kurahashi/Hilbert-Bernays 系を比べるとき。 |
| [g2-zoo-topological-taming.md](../../research/notes/g2-zoo-topological-taming.md) | G2-ZOO を topology/domain 条件で tame する構想。 | ZOO の混沌を位相条件で制限したいとき。 |
| [generalized-proof-structures.md](../../research/notes/generalized-proof-structures.md) | proof-relevant APS と generalized proof category。 | proof object まで持つ APS を考えるとき。 |
| [indexed-aps-fibred-algebra.md](../../research/notes/indexed-aps-fibred-algebra.md) | indexed preorder/fibred algebra と APS。 | context/fibre つき APS を定義するとき。 |
| [literature.md](../../research/notes/literature.md) | 文献読解ノートの運用基準と citation gaps。 | どの文献で何を埋めるか確認するとき。 |
| [local-fg2-pullback-aps-zoo.md](../../research/notes/local-fg2-pullback-aps-zoo.md) | local-FG2 と APS pullback による比較構成。 | G2/FG2 を局所化・相対化するとき。 |
| [mnd4-preaps-fixedpoint-obstruction.md](../../research/notes/mnd4-preaps-fixedpoint-obstruction.md) | MND4-preAPS と fixed point obstruction。 | MND4 条件で固定点が崩れる理由を見るとき。 |
| [obsidian-research-index.md](../../research/notes/obsidian-research-index.md) | Obsidian vault 由来の研究索引。 | Obsidian 側の研究メモを参照するとき。 |
| [predicate-topology-fixed-points.md](../../research/notes/predicate-topology-fixed-points.md) | predicate topology と domain-theoretic fixed points。 | Scott/domain 固定点と APS をつなぐとき。 |
| [provability-predicate-weak-aps.md](../../research/notes/provability-predicate-weak-aps.md) | 弱い provability predicate を weak APS として扱う。 | A4 などの失敗を制御して G2 を見るとき。 |
| [research-project-chat-links-handoff.md](../../research/notes/research-project-chat-links-handoff.md) | Research Project 共有リンク群の handoff。 | Project チャット由来ノートの出所を追うとき。 |
| [residuated-algebra-domain-completion.md](../../research/notes/residuated-algebra-domain-completion.md) | residuated algebra, domain theory, completion の大きな接続。 | algebraic/domain completion 方向を読むとき。 |
| [residuated-fixedpoint-existence.md](../../research/notes/residuated-fixedpoint-existence.md) | residuated algebra における固定点存在条件。 | Res-APS の固定点定理を探すとき。 |
| [self-elimination-logic.md](../../research/notes/self-elimination-logic.md) | 自己消去論理の静的/動的解釈。 | self-reference の崩壊や動的意味論を見るとき。 |
| [self-existence-sentences.md](../../research/notes/self-existence-sentences.md) | 自己存在文の構成。 | diagonal/self-existence の基本型を見るとき。 |
| [self-mutual-reference-hierarchy.md](../../research/notes/self-mutual-reference-hierarchy.md) | 自己言及・相互言及・network reference の階層。 | fixed point をグラフ的に一般化するとき。 |
| [sequential-pair-theory-indexed-aps.md](../../research/notes/sequential-pair-theory-indexed-aps.md) | sequential/pair theory と indexed APS。 | G2 の meta/syntax/APS 層を分けるとき。 |
| [shibuya-seminar-2026-05-08.md](../../research/notes/shibuya-seminar-2026-05-08.md) | 渋谷セミナー2の APS/G2 まとめ。 | BS16 主定理や reverse mathematics cases を読むとき。 |
| [smullyan-lawvere-categorical-diagonalization.md](../../research/notes/smullyan-lawvere-categorical-diagonalization.md) | Smullyan/Lawvere 対角化と quotation/substitution。 | APS 固定点の構成原理を確認するとき。 |

## Research References

| File | 役割 | 読む場面 |
| --- | --- | --- |
| [research/references/drive.md](../../research/references/drive.md) | Google Drive reference folder のトップレベル索引。 | Drive 内の文献を探すとき。 |
| [research/references/drive-relay.md](../../research/references/drive-relay.md) | Drive を Project/Codex 間 relay として使う手順。 | PDF/slide/relay file を移すとき。 |
| [research/references/obsidian-research-vault.md](../../research/references/obsidian-research-vault.md) | Obsidian vault の対象範囲と除外ポリシー。 | Obsidian 側を同期/索引化するとき。 |
| [research/references/research-drive.md](../../research/references/research-drive.md) | Google Drive research folder の snapshot。 | Paper/Slide/Gemini/Claude 出力を確認するとき。 |

## Records

| File | 役割 | 読む場面 |
| --- | --- | --- |
| [records/README.md](../../records/README.md) | `records/` の役割、promotion rule、log policy。 | ログと研究ノートの区別を確認するとき。 |
| [records/logs/research-log.md](../../records/logs/research-log.md) | 日付順の作業ログ。 | 何がいつ変わったか確認するとき。 |
| [records/logs/chatgpt-share-sync.md](../../records/logs/chatgpt-share-sync.md) | ChatGPT share watchlist の同期履歴。 | 共有リンクが読めた/読めない履歴を見るとき。 |
| [records/discussions/autonomous-discussion.md](../../records/discussions/autonomous-discussion.md) | Codex 自律議論ログ。 | 研究アイデアの生成過程を追うとき。 |
| [records/discussions/claude-code-review.md](../../records/discussions/claude-code-review.md) | Claude Code レビュー記録。 | 外部レビューの指摘を読むとき。 |

## Artifacts

| File | 役割 | 読む場面 |
| --- | --- | --- |
| [artifacts/README.md](../../artifacts/README.md) | `artifacts/` 全体の説明。 | PDF/reports/slides/tex の置き場所を確認するとき。 |
| [artifacts/pdf/README.md](../../artifacts/pdf/README.md) | PDF 出力棚の説明。 | 生成/追加済み PDF を確認するとき。 |
| [artifacts/pdf/discussion-summary-2026-05-30.md](../../artifacts/pdf/discussion-summary-2026-05-30.md) | 議論要約PDFの Markdown ソース。 | 2026-05-30時点の研究状態を読むとき。 |
| [artifacts/pdf/chatgpt-share-import-2026-05-30.md](../../artifacts/pdf/chatgpt-share-import-2026-05-30.md) | ChatGPT share import のPDF用ソース。 | 共有リンク追加時の要約を確認するとき。 |
| [artifacts/pdf/project-note-depth-policy-2026-05-30.md](../../artifacts/pdf/project-note-depth-policy-2026-05-30.md) | Project由来ノート詳細化方針のPDF用ソース。 | なぜ詳細化が必要か説明するとき。 |
| [artifacts/reports/README.md](../../artifacts/reports/README.md) | machine report の contract。 | JSON/CSV レポートの意味を確認するとき。 |
| [artifacts/slides/README.md](../../artifacts/slides/README.md) | slide artifacts の説明。 | slide/PDF deck の置き場所を確認するとき。 |
| [artifacts/slides/chatgpt-project/README.md](../../artifacts/slides/chatgpt-project/README.md) | ChatGPT Project slide import folder の説明。 | Project生成slideをrepoへ移すとき。 |
| [artifacts/tex/README.md](../../artifacts/tex/README.md) | TeX source folder の説明。 | Markdownからpreprint TeXへ進めるとき。 |
| [artifacts/handoffs/claude-code/handoff-20260525-223647.md](../../artifacts/handoffs/claude-code/handoff-20260525-223647.md) | Claude Code への handoff packet。 | 外部レビューに渡した文脈を確認するとき。 |

## Code

| File | 役割 | 読む場面 |
| --- | --- | --- |
| [code/README.md](../../code/README.md) | `code/` の検証レイヤーとしての役割。 | scripts/models の使い分けを確認するとき。 |
| [code/models/README.md](../../code/models/README.md) | finite APS/preAPS model の schema 概要。 | モデルJSONや検査対象を作るとき。 |
| [code/models/macneille-checker-interface.md](../../code/models/macneille-checker-interface.md) | MacNeille reflection checker の interface 設計。 | checker の入出力仕様を見るとき。 |
| [code/models/macneille-reflection-search.md](../../code/models/macneille-reflection-search.md) | MacNeille reflection search の設計ノート。 | completion/reflection 探索の方針を見るとき。 |
