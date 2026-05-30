---
title: "ChatGPT共有リンク取り込みメモ"
date: "2026-05-30"
lang: ja-JP
mainfont: "Yu Mincho"
sansfont: "Yu Gothic"
monofont: "Consolas"
geometry: margin=24mm
fontsize: 11pt
---

# 概要

2026-05-30に、ユーザー提供のChatGPT共有リンク7件を確認した。
うち5件は新規リンクとして `research/references/chatgpt-share-watchlist.csv`
に追加し、各内容を研究ノートへ要約した。2件は既存登録済みだったため、
既存ノートを再確認・補強した。

# 新規追加リンク

| Title | Local note |
| --- | --- |
| Formalized G2 in Implicational APS | `research/notes/formalized-g2-implicational-aps.md` |
| Provability Predicate in Weak APS | `research/notes/provability-predicate-weak-aps.md` |
| Self-Elimination Logic | `research/notes/self-elimination-logic.md` |
| Sequential Pair Theory and Indexed APS | `research/notes/sequential-pair-theory-indexed-aps.md` |
| Research Project Share Links Batch | `research/notes/research-project-chat-links-handoff.md` |

# 要約

## Formalized G2 in Implicational APS

G2を外部的含意

$$
\boxtimes T\le \bot \Longrightarrow T\le \bot
$$

としてだけでなく、局所化された形式化原理として扱う方向を整理した。
とくに $d=\boxtimes T$ として、

$$
\mathrm{LG2}(a):\quad d\le a\Longrightarrow \boxtimes a\le d
$$

を導入し、G2とFG2の間に $\mathrm{FG2}[q]$ や $\mathrm{LG2}(a)$ の
階層を置く研究課題を追加した。

## Provability Predicate in Weak APS

Feferman型、Shavrukov型、Rosser型、KD型の証明可能性述語を、
通常APSの例ではなく、A4または反証可能性内省が制御された形で失敗する
weak APS の標準標本として読む方針を追加した。

## Self-Elimination Logic

公理性そのものを対象化し、

$$
E\leftrightarrow\text{``}E\text{ is not an axiom / is deleted''}
$$

のような自己消滅的構造を扱う前論理を整理した。静的古典論理では自明化するため、
削除作用素や安定拡張をもつ動的・非単調意味論として扱う必要がある。

## Sequential Pair Theory and Indexed APS

Visser型のSequential Theory / Pair TheoryをAPSへ直接二項演算として足すのではなく、
コード層と命題順序層を分けた indexed preorder / fibration として扱う方針を追加した。
G2は、sequentialityが固定点を供給し、APSがその固定点からG2/FG2を抽出する、
という三層構造で整理した。

## Existing Links Rechecked

次の2件はすでにwatchlistに登録済みだった。

- `https://chatgpt.com/share/6a0b7536-836c-83ab-ae90-5eb16748d05e`
- `https://chatgpt.com/share/6a0cbab3-b174-83ab-8a89-db8a746eacda`

前者はG2-ZOOの基数不変量化、Tukey還元、関係系としてのG2原理へ展開されていた。
後者は剰余付き代数、完備化、カット除去、Abstract GoIの接続が追加的に読めた。

# ファイル可読性

共有ページ内にはPDF/TeX生成物への `sandbox:/mnt/data/...` リンクが含まれていた。
これらは元のChatGPTセッション内部のファイル参照であり、このローカルrepoからは
直接読めない。ファイルそのものを取り込みたい場合は、ChatGPT ProjectからGoogle Driveの
artifact inboxへ保存し、`code/scripts/sync-chatgpt-project-artifacts.ps1` で同期する。

# 同期結果

`code/scripts/check-chatgpt-shares.ps1` による確認結果:

- total: 23 links
- new: 5
- changed: 2
- unchanged: 16

状態は `records/logs/chatgpt-share-state.csv` と
`records/logs/chatgpt-share-sync.md` に記録した。
