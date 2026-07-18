---
type: research-cycle
id: CYCLE-20260718-091020
status: complete
goal: RSYS-001
created: 2026-07-18T09:10:20+09:00
updated: 2026-07-18
---

# RAMS様相原理の関係を整理する

## 範囲

- 対象: K、4、T、D、M、C、Löb、sLöb、FLöb、CP、整合性、固定点、選言性、構造原理。
- 今回しないこと: 完全な分類、全APS条件の有限モデル列挙、未定義記号の推測。
- 終了条件: 定義表、確実な含意、反例候補、二名査読、反芻、次の問題を残す。

## アイデア案

### Ideator A: 多軸の関係地図

原理を「modal operator」「residuated基礎」「構造規則」「固定点・整合性」の四軸に分ける。同じ名前でも基礎の違いで意味が変わるため、無条件の一枚図は作らない。

### Ideator B: 第二不完全性の中心線

最初は `縮約 → 固定点 → Löb → Con` の中心線に絞り、選言性やLinは分離例を作る補助軸として扱う。研究目的に近い部分から証明を固める。

### 相互批判と統合

Aだけでは表が大きくなりすぎる。BだけではK・M・Cの基礎関係を見落とす。そこで「全体の型表」と「Löb・SC中心線」の二層にした。

## 定式化

問題カード [PROB-20260718-RAMS-MAP](../../../research/problems/PROB-20260718-rams-principle-map.md) を作成した。単位元 `e` と上端 `⊤` を分け、integralityを必要な箇所だけに付けた。未確定の `P` と `E` は保留した。

## 理論地図

- 証明: `M+C⇒K`、`CP⇒4`、`CP⇒normality`、`T+CP⇒□=id`。
- integralで証明: `sLöb⇒Löb`。
- 追加仮定つき: integral基礎で `D_derived+normality⇒Con_L_sem⇒Con_EG_elem`。
- 崩壊: `T+Löb`、および通常の条件下の `normality+D+Löb`。
- 中心予想: K、4、normality、integrality、CtrBoxの下で `Löb⇔FLöb⇔SC_elem`。

## Solver attempts

### Solver A: 手計算

residuationによる `M+C⇒K` と、`SC_elem⇒¬□FP_elem` の特殊化を確認した。セミナーノートの同値証明では `□p≤□p⊗□p` が使われることを確認した。

### Solver B: 有限鎖全列挙

2～4元のGödel鎖とŁukasiewicz鎖、全574個の単項写像を検査した。単純な非含意の反例候補と、複数仮定つき中心予想への小モデル支持を得た。結果は [JSON report](../../../artifacts/reports/rams-principle-chain-census.json) にある。

## Skeptic report

[skeptic.md](skeptic.md) を参照。有限鎖、integral、derived diamondへの偏りを常に区別する。

## 判断

| 判断 | 理由 | 根拠 | 留保 |
| --- | --- | --- | --- |
| 最初に定義の型を固定する | 原理名だけでは層が混ざる | `Con_EG`、Ros、E | ユーザー定義待ち |
| CtrとCtrBoxを分ける | セミナーの証明がbox像上の向きを使用 | SC⇒Löb等の式変形 | 全域CtrならCtrBoxを含意 |
| finite censusを反例探索に限定する | 有限鎖で一般定理は証明できない | 574写像の列挙 | APS条件は未実装 |

## 査読への対応

- integralityを欠いたFLöb⇒Löbを訂正し、Mを不要とした。
- Ctr/CtrBox、SC_elem/SC_def、primitive/derived Dを分離した。
- censusへ定義、明示的なサイズ、Python版、スクリプトhash、実行コマンドを追加した。
- 中心四方向の計算を作業ノートへ展開し、Con_L/Con_L_semを分離した。
- 次の実験を非鎖Heyting代数と仮定除去テストに限定した。

## 査読

- [主査](review-primary.md)
- [副査](review-secondary.md)

## 統合

主査の初回major-revisionと副査のmajor-revisionを反映した。主査は最終 `accept`、副査は再査読 `accept`。中心四方向は証明計算を本文へ追加し、finite censusは要素意味論の反例探索に限定した。

## 反芻

[reflection.md](reflection.md)

## 次の一手

APSの `☒` を含む有限モデル検査を追加する前に、`P`、`E`、`Con_EG` の定義を確定する。
