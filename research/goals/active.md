---
type: research-goal
id: RSYS-001
status: active
created: 2026-07-18
updated: 2026-07-18
owner: 渋谷伊織
---

# 半自動研究システム v2 を一週間試運転する

## Objective

一件の実在する未解決問題を、情報収集から二名査読・章雛形・反芻まで一周させ、システムの有用性と欠陥を観測する。

## Why now

構造だけを増やしても研究は進まないため、最小の実運用から改善根拠を得る。

## In scope

- `research/open_problems.md` から一件を選ぶ。
- Ideator A/B、Formulator、Solver A/B、Skeptic、主査、副査を一周させる。
- 研究反芻とシステム改善記録を一件ずつ残す。

## Out of scope

- 既存研究ノート全件の移行。
- Drive内の全PDFの再分類。
- 論文全体の一括執筆。

## Done criteria

- [ ] 一件のcycle directoryが完了状態になる。
- [ ] 主査と副査の独立査読がある。
- [ ] 一章のskeletonとclaim-mapがある。
- [ ] 研究反芻がある。
- [ ] 少なくとも一件の改善提案が意図・指標・rollback付きで記録される。

## Evidence required

- problem card、cycle、review二件、reflection、improvement、chapterへのリンク。

## Constraints and budget

- Time: 一週間の試運転。
- Compute: 既存環境と小規模検証を優先。
- External access: 原文へ到達できない文献は未確認扱い。

## Risks and blockers

- 役割を増やしすぎて研究時間を奪うこと。
- 同じモデルによる査読の独立性を過大評価すること。

## Linked objects

- Problems: 未選択
- Cycles: [CYCLE-20260718-091020](../../records/research-cycles/2026-07-18-091020-rsys-001/cycle.md)
- Artifacts: 未作成

## Decision log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-07-18 | 一週間の試運転を最初のGoalとする | 全件移行より運用上の欠陥を早く発見できる | `RESEARCH_SYSTEM.md` |
