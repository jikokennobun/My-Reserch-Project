---
type: manuscript-chapter
id: CH-01
status: skeleton
parent_goal: RSYS-001
paper: RAMS様相原理の関係
created: 2026-07-18
updated: 2026-07-18
---

# RAMS上のLöb原理と固定点

## 目的

Löb、FLöb、SCの関係と、そのために必要な構造仮定を明らかにする。

## Claims

| Claim | Status | Evidence or proof | Dependency |
| --- | --- | --- | --- |
| `sLöb⇒Löb` | proved | residuation | integrality |
| `normality+FLöb⇒Löb` | proved | 一行証明、主査確認 | integrality |
| `M+FLöb⇒SC_elem` | proved | 固定点の直接構成 | integrality |
| `SC_elem⇒Löb` | proved | 作業ノートの四方向計算、主査確認 | K、4、normality、integrality、CtrBox |
| `Löb⇒FLöb` | proved | 作業ノートの四方向計算、主査確認 | K、4、CtrBox |

## Draft

1. 基礎代数と原理の型を定義する。
2. 縮約 `x≤x⊗x` とintegrality由来の `x⊗x≤x` を分ける。
3. 三方向の証明を、使用仮定を各行に付けて示す。
4. 仮定を除いた有限反例を示す。

## Review and next revision

- 指摘: integrality欠落、Ctr/CtrBox混同、存在の型の混同。
- 修正: 主張表と機械実験の名称を分離し、四方向の計算を本文へ追加した。
- 残る問題: APSのprimitive `☒` 条件と構文的 `SC_def` への接続。
