# Markdown File Guide

作成日: 2026-05-31

このフォルダは、repository 内のすべての Markdown ファイルを読むための
解説資料です。単なるファイル一覧ではなく、「何のためのファイルか」
「いつ読むべきか」「どの研究線と関係するか」が分かるように整理しています。

## 収録資料

- [all-md-files.md](all-md-files.md): 全 Markdown ファイルの索引。各ファイルの役割と読む場面を一行ずつ整理。
- [research-notes-guide.md](research-notes-guide.md): `research/` 配下、とくに `research/notes/` の研究ノートをテーマ別に解説。
- [operations-and-artifacts-guide.md](operations-and-artifacts-guide.md): `docs/`, `records/`, `artifacts/`, `code/`, root 直下の Markdown を解説。

## 読み方

最初に全体像を掴むなら:

1. root の [README.md](../../README.md)
2. root の [index.md](../../index.md)
3. このフォルダの [all-md-files.md](all-md-files.md)

研究内容を追うなら:

1. [research/definitions.md](../../research/definitions.md)
2. [research/open_problems.md](../../research/open_problems.md)
3. [research-notes-guide.md](research-notes-guide.md)

運用や自動化を追うなら:

1. [docs/workflow.md](../workflow.md)
2. [docs/codex-research-automation.md](../codex-research-automation.md)
3. [operations-and-artifacts-guide.md](operations-and-artifacts-guide.md)

## 更新方針

新しい Markdown ファイルを追加したら、少なくとも
[all-md-files.md](all-md-files.md) に追記してください。研究ノートなら
[research-notes-guide.md](research-notes-guide.md)、運用・成果物・ログなら
[operations-and-artifacts-guide.md](operations-and-artifacts-guide.md) も更新します。

この資料自体も Markdown ファイルなので、索引では `docs/markdown-file-guide/`
配下として扱います。
