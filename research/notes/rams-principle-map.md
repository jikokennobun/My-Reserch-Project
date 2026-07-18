---
type: research-note
status: working
created: 2026-07-18
updated: 2026-07-18
problem: PROB-20260718-RAMS-MAP
---

# RAMS様相原理の関係図

## 目的

狙いは原理の一覧を作ることではない。どの構造仮定が、どの不完全性・整合性・固定点現象を生むかを切り分けることである。これは、算術的符号化より代数的構造から第二不完全性現象を理解したいという現在の関心に合う。

## 記法と型

基礎を有界可換単位的residuated orderとする。積は `⊗`、単位元は `e` である。`e=⊤` はintegralityとして別に仮定する。`¬x=x→⊥`、`◇x=¬□¬x` とする。

| 原理 | 代数的な形 | 型 |
| --- | --- | --- |
| M | `x≤y` なら `□x≤□y` | 規則 |
| normality | `□⊤=⊤` | 方程式 |
| K | `□(x→y)≤(□x→□y)` | 不等式 |
| 4 | `□x≤□□x` | 不等式 |
| T | `□x≤x` | 不等式 |
| CP | `x≤□x` | 不等式 |
| C | `□x⊗□y≤□(x⊗y)` | 不等式 |
| D_derived | `□x≤¬□¬x` | 不等式 |
| Löb | `□x≤x` なら `⊤≤x` | 準方程式 |
| sLöb | `(□x→x)≤x` | 不等式 |
| FLöb | `□(□x→x)≤□x` | 不等式 |
| Ctr | `x≤x⊗x` | 全要素上の構造原理 |
| CtrBox | `□x≤□x⊗□x` | box像上の縮約 |
| 選言性 | `□(x∨y)=□x∨□y` | 方程式 |
| SC_elem | `∀x∃p[p=(□p→x)]` | 代数要素の固定点存在 |
| `¬□`FP_elem | `∃p[p=¬□p]` | 代数要素の固定点存在 |

`SC_elem` は代数の全要素を量化する。式として一様に固定点を作れるという構文的な `SC_def` とは別であり、有限モデル実験は前者しか検査しない。`Con_EG_elem` と `¬□FP_elem` も同様である。

`E` は、`□` が商代数上の関数ならextensionalityとして自動的である。構文上の規則として置く場合だけ独立の検討対象になる。`P(¬□⊥)` は定義を確認するまで保留する。

## 証明できる基本含意

以下では必要な仮定を省略しない。

1. `M + C ⇒ K`。
   `(x→y)⊗x≤y` にMを使い、Cを介して `□(x→y)⊗□x≤□y` を得る。residuationでKになる。
2. `CP ⇒ 4`。CPに `□x` を代入する。
3. 上端を持つ場合、`CP ⇒ normality`。`⊤≤□⊤≤⊤` である。
4. `M + T ⇒ □□x≤□x`。さらに4があれば `□` は冪等になる。
5. `T + CP ⇒ □=id`。
6. integralな基礎では `sLöb ⇒ Löb`。`□x≤x` なら `⊤≤□x→x≤x` である。
7. integralな基礎では `normality + FLöb ⇒ Löb`。Mは不要である。integralityを外すと非integralな3要素鎖に反例がある。
8. derived diamondを用い、通常の有界integral基礎では `D_derived + normality ⇒ Con_L_sem`。
9. `Con_L_sem ⇒ Con_EG_elem`。証人を `⊥` とする。
10. integralかつMの下では `Con_L_sem⇒Ros`。`φ≤⊥` にMを使う。逆の `Ros⇒Con_L_sem` は `φ=⊥` の代入で得る。
11. `SC_elem⇒¬□FP_elem`。SCを `x=⊥` に特殊化する。

## 崩壊する組合せ

- `T + Löb` は全要素を `⊤` にする。Tにより常に `□x≤x` なので、Löbが常に発火する。
- `normality + D + Löb` も、上の仮定の下では崩壊する。Dが `Con_L` を与え、Löbを `x=⊥` に使える。
- `T + CP` はmodal operatorを恒等写像にする。この上でLöbを加えると再び崩壊する。

これらは「強いほどよい」のではなく、第二不完全性型の現象には非反射性が必要であることを示す。

## 整合性原理

| 名称 | 読み | 現時点の関係 |
| --- | --- | --- |
| `Con_L` | 対象言語の式 `¬□⊥` が妥当 | integralで `Con_L_sem` と対応 |
| `Con_L_sem` | 代数的不等式 `□⊥≤⊥` | Mの下でRos規則と対応 |
| `Con_EG_elem` | `∃x[□x≤⊥]` | `Con_L_sem` より弱い。代数要素の存在 |
| `Con_S=D_derived` | `□x→◇x` | normality等の下で `Con_L_sem` を含意 |

primitiveな `☒` を使うD、すなわち `□x⊗☒x≤⊥` と、derived diamondによるDは同一視しない。

`Con_L` の妥当性は `¬□⊥=⊤` と書ける。integralなresiduated基礎では、これはcensusが検査する `Con_L_sem: □⊥≤⊥` と同値である。非integralな基礎ではこの対応を自動的に使わない。

## Löb・FLöb・SC

`[[渋谷セミナー3]]` の中心予想は、normal、integral、commutativeなRAMSにK、4、`CtrBox`を加えたときの

`Löb ⇔ FLöb ⇔ ∀∃SC`

である。ここでSCはまず `SC_elem` と読む。必要仮定は次のように分解できる。

- `FLöb⇒Löb`: integrality + normality。
- `FLöb⇒SC_elem`: integrality + M。
- `SC_elem⇒Löb`: integrality + normality + K + 4 + CtrBox。
- `Löb⇒FLöb`: K + 4 + CtrBox。

normality、integrality、KがあればMは導けるため、共通仮定の下では三者が結ばれる見込みである。証明は `□p≤□p⊗□p` の向きを使う。`□p⊗□p≤□p` はintegralityから出る弱化側であり、別の原理である。

### 四方向の計算

`FLöb⇒Löb`。`□x≤x` とする。integralityより `□x→x=⊤` である。normalityとFLöbから

`⊤=□⊤=□(□x→x)≤□x≤x`

を得る。

`FLöb⇒SC_elem`。任意の `x` に対し `p=□x→x` と置く。integralityより `x≤p` なので、Mから `□x≤□p`。従って `□p→x≤p` である。一方、FLöbから `□p≤□x` なので、`p⊗□p≤p⊗□x≤x`。よって `p≤□p→x` でもあり、`p=□p→x` を得る。

`SC_elem⇒Löb`。`□x≤x` とし、SC_elemにより `p=□p→x` を取る。K、4、CtrBoxから

`□p≤□p⊗□p≤□p⊗□□p≤□x≤x`

を得る。integralityより `p=⊤`。normalityから `□p=⊤` なので `⊤≤x` となる。

`Löb⇒FLöb`。`q=□x→x`、`a=□q→□x` と置く。Kを `a` と `q` に使い、4とCtrBoxを挟むと

`□a⊗□q≤□a⊗□q⊗□q≤□a⊗□□q⊗□q≤□□x⊗□q≤□x`

となる。従って `□a≤a`。Löbより `⊤≤a`、residuationより `□q≤□x`。これはFLöbである。

## 選言性、排中律、Lin

- Mだけで `□x∨□y≤□(x∨y)` が出る。選言性で新しく要求しているのは逆向きである。
- 排中律とnormalityと選言性から `□x∨□¬x=⊤` が出る。これはmodalな決定性であり、Dとは別である。
- Linを `((x→y)∨(y→x))=⊤` と読む場合、有限鎖では自動的だが、一般RAMSでは選言性やDを直ちに与えない。
- 直観主義的原理は一括りにせず、Heyting基礎、prelinearity、排中律、二重否定除去を別軸にする。

## 有限モデル実験の位置づけ

有限Gödel鎖とŁukasiewicz鎖上の全単項写像 `□` を列挙する。これは非含意の反例候補を探すための実験であり、一般定理の証明ではない。実行コードは `code/scripts/check-rams-principles.py`、結果は `artifacts/reports/rams-principle-chain-census.json` に置く。

2～4元鎖の全574写像を調べた。次の非含意には反例候補が得られた。

| 非含意 | 最小の候補 |
| --- | --- |
| `K ⇏ M` | 2元Gödel鎖、`□=[1,0]` |
| `K ⇏ C` | 4元Łukasiewicz鎖、`□=[0,2,0,0]` |
| `Con_EG_elem ⇏ Con_L_sem` | 2元Gödel鎖、`□=[1,0]` |
| `Löb ⇏ FLöb`、仮定なし | 3元Łukasiewicz鎖、`□=[1,2,0]` |
| `¬□FP_elem ⇏ SC_elem` | 3元Gödel鎖、`□=[1,0,2]` |

一方、`M+C⇒K`、`normality+D_derived⇒Con_L_sem`、`normality+FLöb⇒Löb`、`M+FLöb⇒SC_elem` は全列挙で反例がなかった。列挙対象はすべてintegralである。K、4、normality、M、CtrBoxを加えたLöb・FLöb・SC_elem間の検査も未反証だった。ただし、これらの写像がprimitiveな `☒` を含むAPS条件を満たすかは未検査である。

## 次の証明課題

1. Löb・FLöb・SC_elemの四方向から仮定を一つずつ除き、最小仮定を確認する。
2. 有限鎖で得た最小反例をRAMSおよびAPS条件まで含めて確認する。
3. `¬□FP_elem` とSC_elemの関係を、`x=⊥` の特殊化だけでなく逆向きも調べる。
4. Con系を対象言語の式とメタレベルの存在に分離する。

## 参考文献

- Beklemishev and Shamkanov, *Some abstract versions of Gödel's second incompleteness theorem based on non-classical logics*, [arXiv:1602.05728](https://arxiv.org/abs/1602.05728). [確認記録](../literature/beklemishev-shamkanov-2016-abstract-g2.md)
