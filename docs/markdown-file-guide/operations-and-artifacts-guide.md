# Operations and Artifacts Guide

作成日: 2026-05-31

この資料は、研究ノート以外の Markdown を解説します。対象は root,
`docs/`, `records/`, `artifacts/`, `code/` 配下です。研究本文を支える
運用・ログ・成果物・検証仕様の位置づけをまとめます。

## Root Entry Points

### [README.md](../../README.md)

repository 全体の玄関です。`research/`, `records/`, `artifacts/`, `code/`,
`docs/` の役割と、よく使う PowerShell コマンドが並んでいます。

追加・整理作業を始める前に読むと、どこへファイルを置くべきかが分かります。

### [index.md](../../index.md)

研究全体の索引です。主要ノート、Drive参照、Claude Code bridge、
PDF outputs、research log などへ飛べます。研究の入口は README より
こちらの方が細かいです。

## Workflow and Automation Docs

### [docs/workflow.md](../workflow.md)

ChatGPT Project, Codex, Claude Code, Google Drive, Obsidian をどう使い分けるかを
定義する文書です。手作業・自動化・レビューの流れがここに集約されています。

### [docs/research-note-quality-standard.md](../research-note-quality-standard.md)

研究ノートの品質基準です。Project由来の薄い要約を防ぐため、source,
abstract, definitions, propositions, proof sketches, examples, open problems を
最低要件として定めています。

### [docs/codex-research-automation.md](../codex-research-automation.md)

Codex による自動研究運用の設計書です。自律議論、PDF化、Driveバックアップ、
Project artifact import、Markdownノート基準がまとめられています。

### [docs/codex-autonomous-discussion-prompt.md](../codex-autonomous-discussion-prompt.md)

自律議論ループに渡す実行プロンプトです。Proposer, Skeptic, Formalist,
Archivist の役割分担と、出力先・PDF化ルールが記録されています。

### [docs/claude-code-research-bridge.md](../claude-code-research-bridge.md)

Claude Code にどの作業を任せ、Codex とどう衝突を避けるかを定めます。
レビューや外部検査を入れるときの交通整理文書です。

### [docs/claude-code-autonomous-review-prompt.md](../claude-code-autonomous-review-prompt.md)

Claude Code 用のレビュー依頼プロンプトです。研究内容をコードレビュー風に
検査してもらうためのテンプレートです。

## Markdown File Guide Folder

### [docs/markdown-file-guide/README.md](README.md)

この解説資料フォルダの入口です。全MD索引、研究ノート詳解、
運用/成果物詳解への導線を持ちます。

### [docs/markdown-file-guide/all-md-files.md](all-md-files.md)

全 Markdown ファイルの一行解説です。ファイルの役割を素早く知るための
地図として使います。

### [docs/markdown-file-guide/research-notes-guide.md](research-notes-guide.md)

`research/` 配下のノートをテーマ別に説明します。APS/G2-ZOO の研究内容を
読むための道案内です。

### [docs/markdown-file-guide/operations-and-artifacts-guide.md](operations-and-artifacts-guide.md)

このファイルです。運用資料、ログ、成果物、検証仕様など、研究本文以外の
Markdownを説明します。

## Records

### [records/README.md](../../records/README.md)

`records/` は過程を保存する場所であり、研究結果そのものは `research/notes/`
へ promote する、という方針を示します。

### [records/logs/research-log.md](../../records/logs/research-log.md)

作業履歴です。何を追加したか、どのPDFをバックアップしたか、どの同期が失敗したかを
日付順に追えます。研究の provenance を確認するために重要です。

### [records/logs/chatgpt-share-sync.md](../../records/logs/chatgpt-share-sync.md)

ChatGPT share watchlist の同期結果です。リンクが `new`, `changed`,
`unchanged`, `error` のどれだったかを保存します。

### [records/discussions/autonomous-discussion.md](../../records/discussions/autonomous-discussion.md)

Codex 自律議論の大きなログです。研究アイデアがどう生成され、どの問題へ
展開されたかを追跡できます。

### [records/discussions/claude-code-review.md](../../records/discussions/claude-code-review.md)

Claude Code のレビュー記録です。外部的な懐疑・検査・改善提案の履歴です。

## Artifacts

### [artifacts/README.md](../../artifacts/README.md)

PDF, reports, handoffs, slides, TeX の置き場所を説明します。成果物管理の
入口です。

### [artifacts/pdf/README.md](../../artifacts/pdf/README.md)

PDF 棚の説明です。議論要約PDF、Project import summary、外部PDFなどの
役割が書かれています。PDF を追加したらここも更新します。

### [artifacts/pdf/discussion-summary-2026-05-30.md](../../artifacts/pdf/discussion-summary-2026-05-30.md)

議論要約PDFの Markdown ソースです。Markdown数式整理、APS/G2-ZOO の状態、
Driveバックアップ運用などをまとめています。

### [artifacts/pdf/chatgpt-share-import-2026-05-30.md](../../artifacts/pdf/chatgpt-share-import-2026-05-30.md)

2026-05-30 の ChatGPT share import 結果をPDF化するためのソースです。
新規追加リンクと既存リンクの扱いを記録しています。

### [artifacts/pdf/project-note-depth-policy-2026-05-30.md](../../artifacts/pdf/project-note-depth-policy-2026-05-30.md)

Project由来ノートを短い要約で止めず、preprint seed レベルまで増やす方針を
PDF化するためのソースです。

### [artifacts/reports/README.md](../../artifacts/reports/README.md)

machine-generated report の読み方です。JSON/CSVレポートがどの数学的主張を
支えるのかを明示する contract を持ちます。

### [artifacts/slides/README.md](../../artifacts/slides/README.md)

slide deck や PDF slide の置き場所を説明します。ChatGPT Project-generated
slides の import 手順もここから辿れます。

### [artifacts/slides/chatgpt-project/README.md](../../artifacts/slides/chatgpt-project/README.md)

Google Drive inbox から取り込んだ ChatGPT Project slide artifacts の
着地点を説明します。

### [artifacts/tex/README.md](../../artifacts/tex/README.md)

TeX 化した preprint/source material の置き場です。Markdown研究ノートが成熟して
TeX論文化するときに使います。

### [artifacts/handoffs/claude-code/handoff-20260525-223647.md](../../artifacts/handoffs/claude-code/handoff-20260525-223647.md)

Claude Code へ渡すための handoff packet です。git status, active research
questions, open problems, review tasks を含む一回限りの引き継ぎ資料です。

## Code and Model Documentation

### [code/README.md](../../code/README.md)

`code/` は研究ノートの検証レイヤーである、という方針を説明します。
scripts, models, reports の関係を読む入口です。

### [code/models/README.md](../../code/models/README.md)

finite APS/preAPS model の予定フィールドや model schema の概要です。
モデルJSONを作るときに参照します。

### [code/models/macneille-checker-interface.md](../../code/models/macneille-checker-interface.md)

MacNeille reflection checker の command, input, validation, output classification
を定義する interface note です。

### [code/models/macneille-reflection-search.md](../../code/models/macneille-reflection-search.md)

MacNeille reflection search の設計ノートです。completion fixed point の分類、
extension discipline、search space を整理しています。

## Maintenance Notes

Markdown ファイルを追加したら、このフォルダの資料も更新します。特に次の3点を
守ると迷子になりにくいです。

1. 研究本文なら `research/notes/` へ置き、`research-notes-guide.md` に追加する。
2. PDFソースや成果物説明なら `artifacts/` へ置き、`operations-and-artifacts-guide.md` に追加する。
3. 運用手順なら `docs/` へ置き、`all-md-files.md` に必ず追加する。
