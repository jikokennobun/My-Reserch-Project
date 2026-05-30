---
title: "議論メモ: Markdown数式表示とAPS/G2-ZOO進捗"
date: "2026-05-30"
lang: ja-JP
mainfont: "Yu Mincho"
sansfont: "Yu Gothic"
monofont: "Consolas"
geometry: margin=24mm
fontsize: 11pt
---

# 目的

このメモは、2026-05-30時点の作業議論をPDFとして保管するための要約である。
今回の直接の問題は、Markdown上の数式が表示環境によって読みにくくなっていたことだった。
対策として、リポジトリ内のMarkdown数式区切りを、GitHub・Obsidian系で扱いやすい
`$...$` と `$$...$$` に正規化した。

# Markdown数式表示の修正

従来のノートでは、インライン数式に `\(...\)`、別行数式に `\[...\]` が多く使われていた。
これはLaTeXとしては自然だが、Markdownビューアによってはそのまま文字列として出る。
今回、コードブロックとインラインコードを避けて、次の形式へ変換した。

$$
\mathrm{nFG2}(k):\quad \boxtimes^{k+1}T\le\boxtimes^kT.
$$

あわせて、Markdown表の中で列区切りと衝突しやすい `$|L|$` などは
$\lvert L\rvert$ の形へ直した。
再実行用のスクリプトは `scripts/normalize-markdown-math.ps1` に置いた。

# 議論の要点

## 1. Completion-reflection square

議論の出発点は、APS/preAPS $L$ から補完 $\widehat L$ への埋め込み
$i:L\to\widehat L$ を取り、補完側で得られる固定点
$q=\widehat{\boxtimes}q$ が本当に構文側の固定点
$p=\boxtimes p$ を反映しているのか、という問題だった。

重要な区別は次の三つである。

- reflected: $q=i(p)$ かつ $p=\boxtimes p$。
- principal-unreflected: $q=i(a)$ だが $\boxtimes a\ne a$。
- nonprincipal-without-syntactic: 補完側に固定点があるが、構文側に対応する固定点がない。

この区別によって、「補完で固定点がある」という主張と、「APS言語内で固定点がある」
という主張を混同しないための基準が得られた。

## 2. MacNeille補完と反変性

MacNeille補完では、反単調な $\boxtimes$ をそのまま単調写像のように拡張すると
極性を誤る。そこで、$\boxtimes:L\to L$ をいったん $L\to L^{op}$ の単調写像として扱い、
$L^{op}$ 側の閉包で拡張する方針を採った。

この修正により、`three-chain-antitone` は principal-unreflected、
`three-element-nolattice-nosynt` は nonprincipal-without-syntactic と分類された。

## 3. G2/FG2/n-FG2の有限モデル

G2とFG2の独立性は3要素モデルで確認された。
代表例は、FG2を満たすがG2を満たさない `M-010` と、
G2を満たすがFG2を満たさない `M-100` である。

n-FG2階層については、

$$
\mathrm{nFG2}(k)\quad\Longleftrightarrow\quad
\boxtimes^{k+1}T\le\boxtimes^kT
$$

という軌道条件で整理された。さらに、任意の有限深さで「初めて真になる」
$D_N$ / $B_N$ 型のモデル族が導入され、有限モデル探索の対象が明確になった。

## 4. Bottom disciplineとresiduation

底元規律 $\forall x(\bot\le x)$ を入れると、既存の分離例の一部は壊れる。
一方で、$B_N$ family は底元 $b$ と上界 $U$ を分けることで、
G2、FG2、FP-synt、n-FG2の挙動を保ちながら底元規律を満たすように設計された。

その後、$B_N$ に対して複数の同一順序上のfull-residuated tensorが構成された。
最初は $U$-absorbing なテンソル、次に truncated-exponent テンソル、
さらに $U$-absorptionを避ける front-shifted 型へ進んだ。

## 5. Front idealと群的escape

front-shifted構成では、前方部分 $F=\{a_1,a_2\}$ がテンソルイデアルとして働き、
tail側の切り詰め加法モノイドと分離される。
直交front幅については、$k=0,1,2$ ではresiduationが成立し、
$k\ge3$ では $p\backslash b$ のfiberがprincipalでなくなる障害が現れる。

最新の議論では、この障害を直交積ではなく群積で回避するルートが検討された。
$F_3$ に巡回群 $\mathbb Z/3\mathbb Z$ の積を入れると、
front間の積が底元 $b$ に落ちず、$p\backslash b=b$ がprincipalになる。
次の課題は、Klein four-group や $\mathbb Z/4\mathbb Z$ など、
$\lvert G\rvert\ge4$ のfront群が同じ方針で成立するかを判定することである。

# 次の作業

1. $\lvert G\rvert\ge4$ のfront群候補を、同一順序・full residuation・反単調性の条件で検査する。
2. MacNeille補完固定点がprincipalまたはreflectedになるためのAPS公理条件を整理する。
3. Markdown数式の新規追加時は、原則として `$...$` と `$$...$$` を使う。

# 保管場所

このPDFと元Markdownは `outputs/pdf/` に置く。
生成物の一覧から辿れるように、`outputs/pdf/README.md` と `outputs/README.md` にも記録する。
