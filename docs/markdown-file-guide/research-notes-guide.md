# Research Notes Guide

作成日: 2026-05-31

この資料は `research/` 配下の Markdown、とくに `research/notes/` の研究ノートを
テーマ別に読むための解説です。APS/G2-ZOO の研究線は広がっているので、
「定義」「有限モデル」「算術」「圏論」「位相/完備化」「証明構造」に分けて
読むと見通しがよくなります。

## 最初に読むべき中核

### [research/definitions.md](../../research/definitions.md)

APS/G2-ZOO 全体の語彙集です。特に次の基本記法を固定しています。

$$
S=(L,\le,\Box,\boxtimes,T,\bot),
$$

$$
\mathrm{G2}(S):
\quad
\boxtimes T\le\bot\Rightarrow T\le\bot,
$$

$$
\mathrm{FG2}(S):
\quad
\boxtimes\boxtimes T\le\boxtimes T.
$$

研究ノートで記法が分からなくなったら、まずここに戻ります。

### [research/open_problems.md](../../research/open_problems.md)

現在の課題表です。単なるToDoではなく、有限モデル探索、固定点反映、
residuated expansion、算術的G2変種、domain/topology方向の問題を
研究プログラムとして並べています。

### [research/notes/g2-fg2-hierarchy.md](../../research/notes/g2-fg2-hierarchy.md)

有限モデル側の主戦場です。G2, FG2, nFG2, fixed point の分離証人を
多数記録しています。ZOO の「何が独立か」を知りたいならこのノートが中心です。

### [research/notes/g2-aps-zoo-classification.md](../../research/notes/g2-aps-zoo-classification.md)

ZOO の分類軸を与えます。logic axis, algebra axis, proof-theory axis を
分けているので、新しいモデルや原理をどこに入れるか判断できます。

## 算術・導出可能性・G2変種

### [research/notes/g2-zoo-arithmetic.md](../../research/notes/g2-zoo-arithmetic.md)

Jeroslow, Kurahashi, Hilbert-Bernays など、算術的な第二不完全性定理の
変種を比較します。APS の抽象原理がどの算術的現象を忘れているかを
確認するための橋です。

### [research/notes/derivability-conditions.md](../../research/notes/derivability-conditions.md)

導出可能性条件を整理します。provability predicate がどの条件を満たすと
APS の A1--A4 に近づくか、弱い provability predicate がどこで外れるかを
見るための基礎資料です。

### [research/notes/provability-predicate-weak-aps.md](../../research/notes/provability-predicate-weak-aps.md)

Feferman/Shavrukov/Rosser 的な弱い provability predicate を weak APS として
扱います。標準APSに入らない述語を「失敗例」として捨てず、どの公理が
どの程度壊れるかを測るノートです。

### [research/notes/aps-arithmetic-realization-kernel.md](../../research/notes/aps-arithmetic-realization-kernel.md)

算術から APS への realization map と kernel の問題です。抽象APSの
区別が算術では同一視されるのか、逆に算術的差異がAPSで潰れるのかを
調べます。

### [research/notes/consistency-notions-hierarchy.md](../../research/notes/consistency-notions-hierarchy.md)

Con, SCon, WSCon などの無矛盾性概念を階層化します。算術側の
consistency notion を ZOO の抽象原理へ写すときの参照先です。

## Residuated APS と部分構造論理

### [research/notes/bs16-fiber-residuated-aps.md](../../research/notes/bs16-fiber-residuated-aps.md)

BS16 カット除去・contraction-free arithmetic を fibered residuated APS として
読む中心ノートです。A3 を hidden contraction として見るなど、
substructural な理解の核になっています。

### [research/notes/residuated-algebra-domain-completion.md](../../research/notes/residuated-algebra-domain-completion.md)

residuated algebra, domain theory, completion を広く接続します。
finite ZOO model を代数的に増強する方向、MacNeille completion と
residuation を同時に考える方向で使います。

### [research/notes/residuated-fixedpoint-existence.md](../../research/notes/residuated-fixedpoint-existence.md)

residuated algebra 内で固定点存在をどう得るかの短いノートです。
より大きい completion/domain ノートへの入口として読むと便利です。

### [research/notes/formalized-g2-implicational-aps.md](../../research/notes/formalized-g2-implicational-aps.md)

implication-like structure を持つ APS で、G2 と FG2 の間に local-FG2 や
formalized G2 を置くノートです。local-FG2 pullback ノートと強く接続します。

## 固定点・完備化・位相

### [research/notes/completion-and-fixed-points.md](../../research/notes/completion-and-fixed-points.md)

MacNeille completion と固定点反映の基礎ノートです。completion-generated
fixed point が syntactic fixed point に戻るかどうかが主題です。

### [research/notes/predicate-topology-fixed-points.md](../../research/notes/predicate-topology-fixed-points.md)

predicate space, topology, domain-theoretic fixed point のノートです。
Scott continuity や dcpo 的見方をAPSに導入する入口です。

### [research/notes/g2-zoo-topological-taming.md](../../research/notes/g2-zoo-topological-taming.md)

G2-ZOO の有限モデル的な混沌を topology/domain 条件で tame する構想です。
discrete topology は無力、Alexandrov topology は monotonicity を回収、
Scott/domain structure は固定点定理へつながる、という階層を整理しています。

### [research/notes/aps-cardinal-invariants-fixed-points.md](../../research/notes/aps-cardinal-invariants-fixed-points.md)

固定点の個数やスペクトルを不変量として見る方向です。まだ補強余地が
ありますが、self/mutual reference hierarchy と自然につながります。

## 対角化・自己言及・相互言及

### [research/notes/self-existence-sentences.md](../../research/notes/self-existence-sentences.md)

自己存在文の作り方を扱います。自己言及がAPSの固定点にどう対応するかの
初期ノートです。

### [research/notes/self-elimination-logic.md](../../research/notes/self-elimination-logic.md)

自己消去的な論理を、静的崩壊と動的意味論に分けて読むノートです。
self-reference が消える/維持される条件を調べるときに使います。

### [research/notes/self-mutual-reference-hierarchy.md](../../research/notes/self-mutual-reference-hierarchy.md)

自己言及を単一固定点だけでなく、2-cycle, finite network, graph-shaped
reference として一般化します。$\boxtimes^2$ の固定点と mutual reference の
対応が重要です。

### [research/notes/smullyan-lawvere-categorical-diagonalization.md](../../research/notes/smullyan-lawvere-categorical-diagonalization.md)

Lawvere の固定点定理と Smullyan/Godel 的対角化を整理します。重要なのは、
単なる diagonal map では不十分で、quotation と substitution が必要だという点です。

## Indexed/Fibred/Categorical APS

### [research/notes/indexed-aps-fibred-algebra.md](../../research/notes/indexed-aps-fibred-algebra.md)

indexed preorder:

$$
F:C^{op}\to\mathbf{Preord}
$$

を使って、context/fibre つき APS を定義します。substitution や
hyperdoctrine 的読みを入れたいときの基礎です。

### [research/notes/sequential-pair-theory-indexed-aps.md](../../research/notes/sequential-pair-theory-indexed-aps.md)

G2 を meta-level, syntax-level, APS-level に分解します。pair theory や
sequential theory を indexed APS として扱う方向です。

### [research/notes/local-fg2-pullback-aps-zoo.md](../../research/notes/local-fg2-pullback-aps-zoo.md)

local-FG2 profile と APS pullback のノートです。複数モデルを共通 reduct の
上で比較し、Godel-style/Jeroslow-style 原理を分離する構想を扱います。

### [research/notes/generalized-proof-structures.md](../../research/notes/generalized-proof-structures.md)

APS の order を proof object の存在として decategorify するノートです。
proof-relevant G2/FG2、2-cell、cut elimination、categorical AAL との接続を扱います。

## セミナー・インポート・外部索引

### [research/notes/shibuya-seminar-2026-05-08.md](../../research/notes/shibuya-seminar-2026-05-08.md)

渋谷セミナー2の整理です。APS 定義、Beklemishev-Shamkanov 主定理、
reverse mathematics 的な分離ケースを含みます。

### [research/notes/chatgpt-imports-2026-05-22.md](../../research/notes/chatgpt-imports-2026-05-22.md)

2026-05-22時点の ChatGPT 共有リンクのインポート索引です。初期ノート群の
由来を確認するための小さな目次です。

### [research/notes/research-project-chat-links-handoff.md](../../research/notes/research-project-chat-links-handoff.md)

Research Project から渡された共有リンク群の対応表です。どの link が
どの note へ変換されたかを追跡できます。

### [research/notes/obsidian-research-index.md](../../research/notes/obsidian-research-index.md)

Obsidian vault の研究ノートを索引化した結果です。ローカル vault と repo の
接続点です。

### [research/notes/literature.md](../../research/notes/literature.md)

文献読解の作業台です。citation gap を明確化し、どの文献がどの theorem/claim を
支えるかを記録します。

## 推奨読書順

有限モデル中心:

1. [definitions.md](../../research/definitions.md)
2. [g2-fg2-hierarchy.md](../../research/notes/g2-fg2-hierarchy.md)
3. [g2-aps-zoo-classification.md](../../research/notes/g2-aps-zoo-classification.md)
4. [formalized-g2-implicational-aps.md](../../research/notes/formalized-g2-implicational-aps.md)

算術・provability 中心:

1. [derivability-conditions.md](../../research/notes/derivability-conditions.md)
2. [g2-zoo-arithmetic.md](../../research/notes/g2-zoo-arithmetic.md)
3. [provability-predicate-weak-aps.md](../../research/notes/provability-predicate-weak-aps.md)
4. [aps-arithmetic-realization-kernel.md](../../research/notes/aps-arithmetic-realization-kernel.md)

圏論・対角化中心:

1. [indexed-aps-fibred-algebra.md](../../research/notes/indexed-aps-fibred-algebra.md)
2. [smullyan-lawvere-categorical-diagonalization.md](../../research/notes/smullyan-lawvere-categorical-diagonalization.md)
3. [self-mutual-reference-hierarchy.md](../../research/notes/self-mutual-reference-hierarchy.md)
4. [generalized-proof-structures.md](../../research/notes/generalized-proof-structures.md)

完備化・位相中心:

1. [completion-and-fixed-points.md](../../research/notes/completion-and-fixed-points.md)
2. [predicate-topology-fixed-points.md](../../research/notes/predicate-topology-fixed-points.md)
3. [g2-zoo-topological-taming.md](../../research/notes/g2-zoo-topological-taming.md)
4. [residuated-algebra-domain-completion.md](../../research/notes/residuated-algebra-domain-completion.md)
