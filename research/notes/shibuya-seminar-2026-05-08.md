# Shibuya Seminar 2 — 2026-05-08

Imported from Cowork session: 2026-05-30.

Individual seminar talk; notes transcribed from handwritten/oral record.

---

## Definition: Abstract Provability Structure (APS)

An **abstract consequential relation** (ACR) is a sextuple

$$
S = (L_S,\;\le_S,\;\Box,\;\boxtimes,\;T,\;\bot)
$$

where $(L_S,\le_S,T,\bot)$ is a bounded partial order (greatest element $T$,
least element $\bot$) and $\Box,\boxtimes:L_S\to L_S$ are unary operators
satisfying the following four axioms.

| Label | Statement | Reading |
|-------|-----------|---------|
| **A1** | $x\le y\Rightarrow\Box x\le\Box y\;$ and $\;\boxtimes y\le\boxtimes x$ | $\Box$ monotone, $\boxtimes$ antitone |
| **A2** | $T\le\boxtimes\bot$ | $\bot$ is refutable |
| **A3** | $x\le\Box y,\;x\le\boxtimes y\;\Rightarrow\;x\le\boxtimes T$ | provable + refutable $\Rightarrow$ refutability of $T$ |
| **A4** | $\boxtimes x\le\Box\boxtimes x$ | refutability is provably refutable |

A4' (appearing later): $\Box x\le\Box\Box x$ — the modal axiom 4 / D3 condition.
A4 and A4' are **independent** (see Case 4 below).

**Examples.** K4 (and all normal modal logics extending it), K4-algebras,
the modal Lindenbaum algebra of $(PA, \mathrm{StdProv})$, Magari algebras,
K4-Locales, some continuous domains of information (CDoI).

**Remark.** APS is K4 stripped of Boolean connectives and their associated
propositional principles; the underlying order replaces the truth-value algebra.

---

## Main Theorem (Beklemishev–Shamkanov 2016)

**Theorem.** Let $S$ be an APS with a $\boxtimes$-fixed point: $\exists p,\;p=_s\boxtimes p$. Then:

1. **G2** (non-formalized second incompleteness theorem):
$$\boxtimes T\le\bot\;\Rightarrow\; T\le\bot.$$

2. **FG2** (formalized second incompleteness theorem):
$$\boxtimes\boxtimes T\le\boxtimes T.$$

**Proof of G2.**
Let $p=\boxtimes p$. Assume $\boxtimes T\le\bot$.
By A2, $T\le\boxtimes\bot\le\boxtimes p=p$.
By A1 (antitonicity), $\boxtimes p\le\boxtimes T$.
So $T\le p=\boxtimes p\le\boxtimes T\le\bot$. $\square$

**Proof of FG2.**
$p=\boxtimes p\le\Box\boxtimes p=\Box p$ (by A4).
So $p\le\Box p$ and $p\le\boxtimes p$; by A3, $p\le\boxtimes T$.
Then $\boxtimes\boxtimes T\le\boxtimes p=p\le\boxtimes T$. $\square$

---

## Reverse Mathematics: 3-point linear order $L=\{\bot,a,T\}$, $\bot<a<T$

The goal is to separate the hypotheses of the Beklemishev–Shamkanov theorem.

### Case 1. G2 $\not\Rightarrow$ FG2 (under A1–A4)

$$\boxtimes T=a,\quad\boxtimes a=T,\quad\boxtimes\bot=T.$$

- G2: $\boxtimes T=a\not\le\bot$ (antecedent false), so G2 holds vacuously.
- FG2: $\boxtimes^2 T=\boxtimes a=T\not\le a=\boxtimes T$. **FG2 fails.**
- Remark: separating FG2 $\Rightarrow$ G2 on $L_{\mathrm{Id}}$ (identity order) seems impossible. Whether FG2 $\Rightarrow$ G2 holds syntactically is **open**.

### Case 2. G2 $\not\Rightarrow$ $\exists\boxtimes$-fixed point (under A1–A4)

Same map as Case 1. The range of $\boxtimes$ is $\{a,T\}$; neither is a fixed point.

### Case 3. $\exists\boxtimes$-fixed point $\not\Rightarrow$ FG2 (under A1, A2, A4)

$$\boxtimes T=\bot,\quad\boxtimes a=a,\quad\boxtimes\bot=T.$$

- Fixed point: $a=\boxtimes a$.
- A3 fails: $a\le\Box a$ and $a\le\boxtimes a=a$, but $a\not\le\boxtimes T=\bot$. $\square$

### Case 4. A4 $\not\Leftarrow$ A4' (under A1–A3 + $\exists\boxtimes$-fixed point)

Four-element model. Set $\Box\equiv\bot$ (the constant $\bot$ map).

$$\boxtimes T=\bot,\quad\boxtimes a=a,\quad\boxtimes\bot=T.$$

- A4' ($\Box x\le\Box\Box x$): $\bot\le\bot$. ✓
- A4 ($\boxtimes x\le\Box\boxtimes x$): $\boxtimes a=a\le\Box a=\bot$. ✗

**Algebraic interpretation.** $\Box$ and $\boxtimes$ are genuinely asymmetric.
The asymmetry — specifically $\Box T\ne\boxtimes\bot$ — is the structural source
of G2-type phenomena; it creates a "friction" between provability and refutability
that contraction erases.

### Case 5. $\exists$SC $\not\Rightarrow$ Löb (implication-extended APS)

Work on $[0,1]$ with Łukasiewicz implication $x\to y=\min\{1,1-x+y\}$,
$\Box=\mathrm{Id}$, and the CDoI refutability

$$\boxtimes(x)=\begin{cases}1-x & x\le 0.5\\ 0.5 & x>0.5.\end{cases}$$

- **$\exists$SC** (Santa Claus sentences exist): The equation $\varphi=\Box\varphi\to\Psi$
  reduces to $\varphi=\varphi\to\Psi$. With Łukasiewicz implication, the map
  $f_\Psi(x)=x\to\Psi$ is continuous on $[0,1]$. The intermediate value theorem
  gives a fixed point $\varphi$ with $f_\Psi(\varphi)=\varphi$, so $\exists$SC holds.
  (With Gödel implication $f_a$ is discontinuous, IVT inapplicable directly.)
- **Löb** ($\Box\varphi\le\varphi\Rightarrow T\le\varphi$): $\Box=\mathrm{Id}$
  makes the premise $\varphi\le\varphi$ always true, so Löb would demand
  $T\le\varphi$ for all $\varphi$ — which is false for $\varphi<1$. **Löb fails.**

Conclusion: on this model, $\exists$SC holds but Löb fails.

---

## Open Problem (session)

> **Is there an APS model where Löb holds but G2 fails?**

Vacuous-G2 models (where $\boxtimes T\not\le\bot$) are easy: take $\Box=\mathrm{Id}$
and $\boxtimes T=a$ for some $a>\bot$. Whether Löb forces G2 in the non-vacuous
sense — i.e., whether Löb + $\boxtimes T\le\bot\Rightarrow T\le\bot$ is a
theorem of pure APS — is **open**.

Candidate strategy: search for an implication-extended APS on $[0,1]$ where Löb
holds (e.g., via a contracting $\Box$ with fixed points only at $T$) but
$\boxtimes T$ is not forced to $\bot$ by G2.

---

*Reference: L. Beklemishev and D. Shamkanov, Some abstract forms of Gödel's
second incompleteness theorem, LMCS 12(2), 2016.*
