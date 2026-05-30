---
title: "Project由来ノートの詳細化方針"
date: "2026-05-30"
lang: ja-JP
mainfont: "Yu Mincho"
sansfont: "Yu Gothic"
monofont: "Consolas"
geometry: margin=24mm
fontsize: 11pt
---

# 背景

これまでのChatGPT Project由来ノートは、まず内容を失わないための
索引・要約として作成されることが多かった。そのため、初回取り込み時には
研究ノートとしては簡略すぎるものがあった。

今後は、共有リンクやDrive経由で読めるProject内容について、できる限り
省略せず、数学的に再利用できる形でMarkdown化する。

# 新しい基準

Project由来ノートには、可能な限り次を含める。

1. source URL / file path / import date / access status
2. 議論が答えていた問い
3. 定義と記法
4. 命題・補題・定理スキーマ・予想
5. 証明または証明スケッチ
6. 例・反例・有限モデル検査課題
7. 既存ノートとの関係
8. 未解決問題と次の作業
9. 読めなかったファイルや `sandbox:/mnt/data/...` 参照の扱い

# 今回増補したノート

- `research/notes/formalized-g2-implicational-aps.md`
- `research/notes/provability-predicate-weak-aps.md`
- `research/notes/self-elimination-logic.md`
- `research/notes/sequential-pair-theory-indexed-aps.md`

いずれも、短い要約から、定義・基本補題・証明スケッチ・有限モデル検査方針を
含む研究ノートへ増補した。

# 自動化側の変更

`docs/codex-research-automation.md` と
`docs/codex-autonomous-discussion-prompt.md` に、Project由来ノートを
詳細な数学ノートとして保存する基準を追加した。

また、実行中の `Research Project Relay Sync` automation と
`Codex Research Discussion Loop` automation にも同じ基準を反映した。

# 注意

Project内の未共有チャットや `sandbox:/mnt/data/...` の一時ファイルは、
このrepoから直接は読めない。PDFやTeXなどの実ファイルを取り込む場合は、
Google Drive artifact inbox に保存してから
`code/scripts/sync-chatgpt-project-artifacts.ps1` で同期する。
