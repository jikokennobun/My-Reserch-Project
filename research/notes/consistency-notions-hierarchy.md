# Consistency Notions Hierarchy

Source: Obsidian vault `抽象的証明可能構造.md`, Cowork session 2026-05-30.

## 1. 無矛盾性の算術化いろいろ

以下では $T$ は PA の r.e. 拡大, $Pr_T(x)$ は標準 $\Sigma_1$-証明可能性述語とする．

| No. | 定式 | 略称 |
|-----|------|------|
| 1 | $\neg Pr_T(\ulcorner\bot\urcorner)$ | $Con_T^L$ (Löb-style) |
| 2 | $\exists x \in \mathrm{Fml}\; \neg Pr_T(x)$ | $Con_T^G$ (Gödel-style) |
| 2.2 | $\exists \varphi\; \neg Pr_T(\varphi)$ | — |
| 3.1 | $\forall \varphi\; (Pr_T(\varphi) \to \neg Pr_T(\neg\varphi))$ | $Con_T^S$ (Strong/Hilbert) |
| 3.2 | $\exists \varphi\; (Pr_T(\varphi) \to \neg Pr_T(\neg\varphi))$ | — |
| 3.3 | $Pr_T(\bot) \to \neg Pr_T(\neg\bot)$ | — |
| 4 | $\forall x \in \mathrm{Fml}\; \neg(Pr_T(x) \land Pr_T(\neg x))$ | $Con_T^H$ (Hilbert-Bernays) |
| 5.1 | $\varphi \Leftrightarrow \neg Pr_T(\neg\varphi)$ ならば $\neg\varphi$ の否定 | — |
| 5.2 | $\varphi \to \neg Pr_T(\neg\varphi)$ ならば $\neg\varphi$ の否定 | — |
| 5.3 | $\exists\varphi\; (Con_T(\varphi) \land \varphi)$, where $Con_T(\varphi) \Leftrightarrow \neg Pr_T(\neg\varphi)$ | — |
| 6 | $\exists\varphi\; \neg Pr_T(Con_T(\varphi))$ | — |
| 6.2 | $\exists\varphi\; \neg Pr_T(Pr_T(\varphi))$ | — |
| 6.3 | $\neg Pr_T(\neg Pr_T(\bot))$ | — |
| 7 | Rosser consistency | Ros |

### 導出関係

$$
7 \to 1 \to 5.3 \to 2.2 \to 2
$$
$$
5.3 \to 5.2, \quad 5.1 \Leftrightarrow 5.2
$$
$$
5.3 \to 1 \quad (\text{規則 E を仮定}), \quad 1 \to 7 \quad (\text{規則 M を仮定})
$$

**標準的順序:**
$$
Con_T^G < Con_T^L < \mathrm{Ros} < Con_T^S < Con_T^H
$$

**Open:**
- $5.2 \Rightarrow 5.3$?
- $5.2 \Rightarrow 2.2$?
- $2.2 \Rightarrow 5.2$?
- **Q.** $5.3$ と $1$ を分離する導出可能性条件（あるいは証明可能性述語）を構成せよ．
- **Q.** $1$ と $7$（あるいは $1$ と $2$）の間を埋め尽くすような原理の単調可算列を構成せよ．

---

## 2. 自己無矛盾性条件 SCon / WSCon / WSCon2

$M$ をある形式的体系, $Pr = \square$, $\diamond \varphi \Leftrightarrow \neg\square\neg\varphi$ とする．

### SCon (Strong Self-Consistency)

$$
M \vdash \varphi \Leftrightarrow \diamond\varphi \;\Big|\; M \vdash \neg\varphi
$$

等価的に: $M \vdash \varphi \Leftrightarrow \square\varphi \;\Big|\; M \vdash \varphi$．

### WSCon (Weak Self-Consistency)

$$
M \vdash \varphi \to \diamond\varphi \;\Big|\; M \vdash \neg\varphi
$$

等価的に: $M \vdash \square\varphi \to \varphi \;\Big|\; M \vdash \varphi$．

### WSCon2

$$
M \vdash \varphi \to \diamond\varphi \;\Big|\; M \nvdash \varphi
$$

**関係:**
- $\mathrm{WSCon} \to \mathrm{WSCon2}$
- WSCon2 の否定 $\Leftrightarrow \exists\varphi\;((\varphi \to \diamond\varphi) \land \varphi)$ (真な自己無矛盾文が存在) $\Leftrightarrow$ (無矛盾性の下で) $\exists\varphi(\varphi \land \diamond\varphi)$

**事実:** $NP + \varphi \to \diamond\varphi \;\Big|\; \neg\varphi$ は矛盾体系 $\bot$ に一致する（$NP$ は WSCon を満たさない）．

**Prf.** $NP \vdash T \to \diamond T$ より $NP \vdash \neg T$. $\square$

**事実:** $NP \vdash \exists\varphi((\varphi \to \diamond\varphi) \land \varphi)$（$\varphi \Leftrightarrow T$ とすれば良い）．

### Rosser fails

$\mathrm{Ros\;fails} := \neg\varphi \;\Big|\; \neg\square\varphi$ が成立しない．

$$
\exists\varphi(\neg\varphi \land \square\varphi) \Rightarrow \mathrm{Ros\;fails}
$$

---

## 3. D と P の間の階層

$$
D: \square\varphi \to \neg\square\neg\varphi \quad (\square\varphi \to \diamond\varphi)
$$
$$
P: \neg\square\bot \quad ((\square T) \to \diamond T)
$$

**D $\Rightarrow$ P の証明:** $\square\varphi \to \neg\square\neg\varphi$ より特に $\square\bot \to \neg\square T$. $\square T$ だから（その対偶により）$\neg\square\bot$. $\square$

**P $\Rightarrow$ D の証明 (K のもとで):** $\varphi \land \neg\varphi \to \bot$ より $\square\varphi \land \square\neg\varphi \to \square\bot$. $\square\bot \to \bot$ だから $\square\varphi \land \square\neg\varphi \to \bot$. $\square$

### D の変種

| 番号 | 原理 |
|------|------|
| $D_1$ | $\square T \to \neg\square\bot$ |
| $D_2$ | $\square\square T \to \neg\square\neg\square T$ |
| $D_3$ | $\square\square T \to \neg\square\square\bot$ |
| $D_4$ | $\square\square\varphi \to \neg\square\square\neg\varphi$ |
| $D_5$ | $\square\diamond T \to \diamond\diamond T$ |
| $D_6$ | $\square\diamond\bot \to \diamond\diamond\bot$ |
| $D_n$ | $\square\varphi \to \diamond\varphi$, $\varphi \in n\text{-BOX}$ |

ここで $\varphi \in n\text{-BOX}$ とは $\varphi$ の命題変数 $p$ が $n$ 個以上の $\square$ に束縛されていること．

### P の変種

| 番号 | 原理 |
|------|------|
| $P_\varphi$ | $\neg\square\varphi$ |
| $P_1$ | $\exists\varphi\; \neg\square\varphi$ |
| $P_2$ | $\forall\varphi\; \neg\square\varphi$ |
| $P_3$ | $\neg\square\exists\varphi\; \varphi$ |
| $P_4$ | $\neg\square\forall\varphi\; \varphi$ |
| $P_n$ | $\exists\varphi\; \neg\square\varphi$, $\varphi \in n\text{-BOX}$ |

**Open:**
- **Q.** D と各 $D_n$ を分離する述語モデルを構成せよ．
- **Q.** P と各 $P_n$ を分離する述語モデルを構成せよ．
- **Q.** 任意の $\Psi$ について, $P_\Psi$ と D は同値か？

---

## 4. ConLat_T

$$
\mathrm{ConLat}_T := \{\varphi \mid N \models \varphi \Leftrightarrow \neg\square\bot\}
$$

- **Q.** $\mathrm{ConLat}_T$ 上の導出関係を調べよ．
- **Q.** $Con_T^G$ に収束する無限降下列は $\mathrm{ConLat}_T$ 上に存在するか？（$T$ が $\Sigma_1$-sound の場合）
  - Ref: [Gödel's Consistency に収束する Consistency Sequence]
- $\{\exists_n \varphi\; \neg\square\varphi\}_{n \in \omega}$ は $Con_T^G$ と $Con_T^L$ の間の無限降下列をなす（はず）．

---

## References

- Beklemishev–Shamkanov (2016), LMCS 12(2).
- Kurahashi (2021): G2 under conditions M and D3.
- Jeroslow (1973): G2 under $\Sigma_1C$.
- Hilbert–Bernays (1939): G2 under M, CB, $\Delta_0 C^U$.
