# Derivability Conditions

Source: Obsidian vault `抽象的証明可能構造.md`, Cowork session 2026-05-30.

$Pr_T(x)$ は $T$ の証明可能性述語, $\square\varphi := Pr_T(\ulcorner\varphi\urcorner)$, $\diamond\varphi := \neg\square\neg\varphi$.

---

## 条件一覧

| 略称 | 定式 | 別名 |
|------|------|------|
| $D1^U$ | $\varphi(x)$ ならば $Pr_T(\ulcorner\varphi(x)\urcorner)$ | Uniform necessitation |
| $D2^U$ | $Pr_T(\ulcorner\varphi(x)\to\Psi(x)\urcorner) \to (Pr_T(\ulcorner\varphi(x)\urcorner) \to Pr_T(\ulcorner\Psi(x)\urcorner))$ | Uniform D2 |
| $D2^G$ | $\forall x,y\; (Pr_T(x\to y) \to (Pr_T(x) \to Pr_T(y)))$ | Global D2 |
| $\Delta_0 C^U$ | $\varphi(x) \to Pr_T(\ulcorner\varphi(x)\urcorner)$, $\varphi(x) \in \Delta_0$ | $\Delta_0$-completeness |
| $\Sigma_1 C^U$ | $\varphi(x) \to Pr_T(\ulcorner\varphi(x)\urcorner)$, $\varphi(x) \in \Sigma_1$ | $\Sigma_1$-completeness |
| $\Sigma_n C^U$ | $\varphi(x) \to Pr_T(\ulcorner\varphi(x)\urcorner)$, $\varphi(x) \in \Sigma_n$ | $\Sigma_n$-completeness |
| $M$ | $\varphi(x) \to \Psi(x)$ ならば $Pr_T(\ulcorner\varphi(x)\urcorner) \to Pr_T(\ulcorner\Psi(x)\urcorner)$ | Monotonicity (local) |
| $M^U$ | $\forall x\; (\varphi(x) \to \Psi(x))$ ならば $\forall x\; (Pr_T(\ulcorner\varphi(x)\urcorner) \to Pr_T(\ulcorner\Psi(x)\urcorner))$ | Uniform monotonicity |
| $CB$ | $Pr_T(\ulcorner\forall x\varphi(x)\urcorner) \to \forall x\; Pr_T(\ulcorner\varphi(x)\urcorner)$ | Collection for Box |
| $CB_\exists$ | $\exists x\; Pr_T(\ulcorner\varphi(x)\urcorner) \to Pr_T(\ulcorner\exists x\varphi(x)\urcorner)$ | — |
| $PC^G$ | $\forall x\; (Pr_\emptyset(x) \to Pr_T(x))$ | PC global |
| $REF^G$ | $\forall x\; (Pr_T(x) \to \mathrm{Tr}(x))$ | Reflection |
| $E$ | $\varphi \Leftrightarrow \Psi$ ならば $\square\varphi \Leftrightarrow \square\Psi$ | Extensionality |
| $E^U$ | $\varphi(x) \Leftrightarrow \Psi(x)$ ならば $\square\varphi(x) \Leftrightarrow \square\Psi(x)$ | Uniform E |
| $C$ | $\square(\varphi \to \Psi) \to (\square\varphi \to \square\Psi)$ | K-axiom |
| $wM$ | $Pr_T(\varphi) \land Pr_T(\varphi \to \Psi)$ ならば $Pr_T(\Psi)$ | Weak monotonicity |
| $TM$ | $\varphi \to (\Psi \to \gamma)$ ならば $\square\varphi \to (\square\Psi \to \square\gamma)$ | Transfer monotonicity |
| $TM'$ | $\varphi \to (\Psi \to \gamma)$ ならば $\varphi \to (\square\Psi \to \square\gamma)$ | — |
| $TM_n$ | $\varphi_1 \to (\varphi_2 \to \cdots (\varphi_{n-1} \to \varphi_n)\cdots)$ ならば $\square\varphi_1 \to (\square\varphi_2 \to \cdots (\square\varphi_{n-1} \to \square\varphi_n))$ | — |
| $\mathrm{Ros}$ | $\neg\varphi$ ならば $\neg\square\varphi$ | Rosser rule |
| $\mathrm{Ros}^U$ | $\forall x\; \neg\varphi(x)$ ならば $\forall x\; \neg\square\varphi(x)$ | Uniform Rosser |
| $\mathrm{L\ddot{o}b}^U$ | $\forall x\; (\square\varphi(x) \to \varphi(x))$ ならば $\forall x\; \varphi(x)$ | Uniform Löb |
| $D3$ | $\square\varphi \to \square\square\varphi$ | Introspection (modal 4) |

---

## 重要な関係

### $D2 \Leftrightarrow M + C$

**$\Rightarrow$:**
- $D2 \Rightarrow M$: 容易．
- $D2 \Rightarrow C$: $\varphi \land (\varphi \to \Psi) \to \Psi$ より $\square((\varphi\to\Psi)\land\varphi) \to \square\Psi$. また $\square((\varphi\to\Psi)\land\varphi) \to (\square(\varphi\to\Psi)\land\square\varphi)$ より $\square(\varphi\to\Psi) \to (\square\varphi \to \square\Psi)$.

**$\Leftarrow$:**
- $(\varphi\to\Psi)\land\varphi \to \Psi$ より $\square((\varphi\to\Psi)\land\varphi) \to \square\Psi$.
- $\square((\varphi\to\Psi)\land\varphi) \to (\square(\varphi\to\Psi) \land \square\varphi)$ なので仮定を弱めて $\square(\varphi\to\Psi) \to (\square\varphi \to \square\Psi)$.

### $TM \Rightarrow K$ (on $N$)

$(p\to q)\to(p\to q)$ より $\square(p\to q) \to (\square p \to \square q)$. つまり $TM \Rightarrow C \Rightarrow K$.

### $M$ と $TM$ の非同値性 (on $MN$)

$MN$ 上で $RM$ と $TM$ は同値でない:  
$(TM)+D3+\neg\square\bot$ から $T \vdash \pi$ を導ける（$\pi$: Gödel 文）. よって $(RM)+D3+\neg\square\bot$ から $T \vdash \pi$ が言え，D3 と単調性を満たす Rosser 証明可能性述語の存在に矛盾する．

**Open:** $M^U \Rightarrow T \nvdash Con_T^L$?（$M^U$ は $TM$ を導くか？）

### Hierarchy

$$
\text{Global} \Rightarrow \text{Uniform} \Rightarrow \text{Local}
$$

---

## 証明可能性述語の自己言及特性

$$
Pr_T(x) \Leftrightarrow Pr_T(Pr_T(x)) \quad (\text{自己言及特性})
$$

---

## 備考

- $REF^G$: $T$ 上では（基本的に）成立しない. $CT_0(T)$ などの上で考える必要がある.
- $D2 \Leftrightarrow M + C$ はモーダル代数的には $K4$-代数の基本恒等式に対応する.
- $TM_n$ と $D2$ の同値性は未解決（**Open: $TM_n \Leftrightarrow D2$?**）.
- **Q.** $(\square\varphi_1 \land \cdots \land \square\varphi_n) \to \square(\varphi_1 \land \cdots \land \varphi_n)$ と $TM_n$ の関係を調べよ.
- **Q.** $wM$ と $D3$ のもとで $T \nvdash Con_T^S$ に弱められるか？

---

## References

- Beklemishev–Shamkanov (2016), LMCS 12(2).
- Kurahashi (2021).
- Jeroslow (1973).
- Hilbert–Bernays (1939).
- Buchholz (1993).
