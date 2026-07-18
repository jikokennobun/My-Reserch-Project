---
type: research-review
reviewer_role: primary
reviewed_object: CYCLE-20260718-091020
independent: true
verdict: major-revision
created: 2026-07-18
---

# Review

## Scope reviewed

指定された作業ノート、問題票、列挙コード、census JSONのみを独立に査読した。重点は含意の必要仮定、Löb/FLöb/SC、縮約の向き、有限反例の解釈である。

## Strongest contribution

中心予想は、`CtrBox: □u≤□u⊗□u` の向きを使えば整合的である。より正確には次の分解ができる。

- `FLöb⇒Löb`: integral + normality。
- `FLöb⇒SC`: integral + M。中心仮定では normality + K から M が従う。
- `SC⇒Löb`: integral + normality + K + 4 + CtrBox。
- `Löb⇒FLöb`: K + 4 + CtrBox。

したがって、ノート75--79行の normal・integral・K・4・縮約の下での三者同値は、縮約を少なくとも `CtrBox` の向きで読む限り正しい見込みが強い。逆向き `□u⊗□u≤□u` はintegralityによる弱化であり、これと取り違えていない点も正しい。

## Blocking issues

なし。

## Major issues

1. ノート50行の `M + normality + FLöb ⇒ Löb` には **integrality が必要**である。「必要な仮定を省略しない」という41行の宣言に反する。反例は非integralな3要素鎖 `0<e<⊤`。`0` を零元、`e` を単位元、`⊤⊗⊤=⊤` とし、`□0=e, □e=e, □⊤=⊤` と置く。この写像は M・normality・FLöb を満たすが、`□e=e≤e` なのに `⊤≤e` でないため Löb を満たさない。修正形は `integral + normality + FLöb ⇒ Löb` であり、Mは不要である。census はintegral鎖だけなので、この欠落を検出できない。

## Minor issues

1. ノート53行のRos規則との対応は証明方向の説明が逆である。`Con_L⇒Ros` で `φ≤⊥` にMを使い、`Ros⇒Con_L` は `φ=⊥` の代入で得る。
2. `Con_L` と `Con_EG` は要素名ではなく妥当性／メタ主張として型を固定すべきである。コード70--71行はそれぞれ `¬□⊥=⊤`、`∃x(¬□x=⊤)` を `□0=0`、`∃x(□x=0)` として実装している。この読みは列挙範囲では正しいが、ノートの記法だけでは式と原理が混在する。
3. ノート32行の `Ctr` は全要素上の構造縮約だが、コード68行と条件付き主張はその弱い像制限版 `CtrBox` だけを検査する。中心証明には `CtrBox` で足りるが、JSONの利用時に「全域縮約を検査した」と読めないよう明記が必要である。特に3値以上のŁukasiewicz鎖は全域Ctrを満たさない。

## Counterexample / alternative interpretation

上記3要素反例により、integralを明記しない一般RAMS上では FLöb からLöbへ進めない。理由は `□x≤x` から `□x→x=⊤` を得る段階がintegralityに依存するためである。

中心同値の `Löb⇒FLöb` では、`q=□x→x`, `a=□q→□x` と置く。K・4・CtrBoxから `□a⊗□q≤□x`、従って `□a≤a`。Löbより `a=⊤`、ゆえに `□q≤□x`、すなわちFLöbとなる。この計算は縮約の必要方向を直接確認している。

## Source and reproducibility check

コードのGödel/Łukasiewicz積・含意、M/K/4/T/CP/C/D、Löb/FLöb/SCの実装は記載定義と一致する。全574モデルについて独立再計算し、JSONの272単純含意と6条件付き主張の反例・supporting_modelsに不一致はなかった。最後の二つの中心条件付き主張の支持モデルは各11個に限られるため、JSON自身の警告どおり一般証明の代用にはならない。

## Required changes

- [ ] ノート50行と対応する主張にintegralを追加し、Mが不要であることを整理する。
- [ ] Ros規則の二方向の証明説明を訂正する。
- [ ] `Con_L`/`Con_EG` の妥当性・量化レベルと、`Ctr`/`CtrBox` の差を明記する。
- [ ] Löb/FLöb/SCの四つの方向を上記の最小仮定ごとに本文へ展開する。

## Verdict rationale

中心予想、縮約方向、有限列挙は有望かつ内部整合的である。しかし「仮定を省略しない」ことが課題の核心である以上、明示反例のあるintegrality欠落は主要修正事項である。判定は `major-revision`。

## 再査読

修正版の作業ノート、問題票、列挙script・JSON、cycle、chapterを再確認した。

初回必須変更のうち、(1) `normality+FLöb⇒Löb` へのintegrality追加とMの除去、(2) Ros規則の証明方向の訂正、(3) Ctr/CtrBox、SC_elem/SC_def、primitive/derived Dの区別は解消した。scriptの実SHA-256はJSON記録値と一致し、2～4元の全574写像について独立再計算した272単純含意・6条件付き主張にも不一致はない。

数学的には四方向も再確認できた。`FLöb⇒Löb` はintegrality+normality、`FLöb⇒SC_elem` はintegrality+Mで成立する。`SC_elem⇒Löb` は、`p=□p→x`、K、4、CtrBoxから `□p≤□x≤x` を得て、integralityとnormalityで `p=⊤`、`⊤=□p≤x` とする。`Löb⇒FLöb` は `q=□x→x`, `a=□q→□x` と置き、K、4、CtrBoxから `□a≤a` を得る計算で成立する。したがって記載された最小仮定と縮約方向に新たな反例・誤りはない。

ただし初回必須変更 (4) は部分対応に留まる。ノート85--88行は仮定一覧だけで証明計算を本文に展開しておらず、117行でもなお「次の証明課題」とされ、chapter 24--25行も二方向を `conditional` としている。誤った定理化ではなく保守的な留保なので主要問題ではないが、中心結果を `proved` に上げる前に上記計算を本文へ記す必要がある。またノートの `Con_L` とscript/JSONの `Con_L_sem` は意味上対応するものの名称が未統一であり、`Con_L := (¬□⊥=⊤)` と妥当性を明記すると型の曖昧さが完全に消える。

主要な数学的誤りは解消した。残件は証明記載と名称統一であるため、再査読判定は `minor-revision` とする。

verdict_after_revision: minor-revision

final_verdict: accept

