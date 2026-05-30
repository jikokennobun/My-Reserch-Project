# G2 Zoo — Arithmetic Variants

Source: Obsidian vault `抽象的証明可能構造.md`, Cowork session 2026-05-30.

G2 の証明のポイント: Gödel 文の証明可能性を導くには，どのような導出可能性条件と Consistency Statement が必要か？

$\pi$: Gödel 文 ($T \vdash \pi \Leftrightarrow \neg\square\pi$).  
$\square = Pr_T$, $\diamond\varphi = \neg\square\neg\varphi$.

---

## G2 variants 比較表

| # | 結論 | 前提条件 | 作者・年 |
|---|------|----------|---------|
| 1 | $T \nvdash \neg\square\bot$ | $\Sigma_1$-predicates + D2 + D3 | standard HBL |
| 1.2 | $T \nvdash \neg\square\bot$ | $\Sigma_1$-predicates + TM + D3 | — |
| 2 | $\exists\varphi\; T \nvdash (\square\varphi \to \diamond\varphi)$ | $\Sigma_1 C$ | Jeroslow (1973) |
| 3 | $\exists\varphi\; T \nvdash (\square\varphi \to \diamond\varphi)$ | M + D3 | Kurahashi (2021) |
| 3.1 | $T \nvdash Con_T^S$ | E + D3 | Kurahashi (改良版) |
| 4 | $T \nvdash Con_T^H$ | M + CB + $\Delta_0 C^U$ | Hilbert–Bernays (1939) |
| 4.1 | $T \nvdash Con_T^H$ | CB + $\Delta_0 C^U$ (M 不要) | Kurahashi (改良版) |
| 5 | $T \nvdash Con_T^G$ | $D2^G$ + $PC^G$ | Montagna (1979) |
| 6 | $T \nvdash Pr_T(\ulcorner 0=1\urcorner)$ | $D1^U$ + $D2^U$ ($\Rightarrow \Sigma_1 C^U$) | Buchholz (1993) |

---

## 1. 標準 G2 (My_Arrange)

**Th.** $\Sigma_1$-述語 $Pr_T(x)$ が D2 と D3 を満たすなら, $T \nvdash \neg\square\bot$.

**Prf.** $T \vdash \neg\square\bot \to \pi$ を示せばよい.  
$T \vdash (\pi \to \bot) \Leftrightarrow \square\pi$ (Gödel 文の定義).  
D3: $T \vdash \square\square\pi \to (\square\pi \to \square\bot)$.  
D3: $T \vdash \square\pi \to \square\bot$.  
よって $T \vdash \neg\square\bot \to \neg\square\pi \to \pi$. $\square$

### 1.2. 改定版 (TM に弱化)

**Th.** D2 の前提を TM に弱めても成立: $TM + D3 \Rightarrow T \nvdash \neg\square\bot$.

**Prf.** TM の使用箇所: $\square\square\pi \to (\square\pi \to \square\bot)$ は TM から従う (TM によれば $\varphi_1 \to (\varphi_2 \to \gamma)$ ならば $\square\varphi_1 \to (\square\varphi_2 \to \square\gamma)$ であり, $\pi\to\bot\to\pi\to\bot$ を代入). $\square$

---

## 2. Jeroslow (1973)

**Th.** $\Sigma_1$-述語 $Pr_T$ が $\Sigma_1 C$ を満たすなら,  
$\exists\varphi\; T \nvdash (\square\varphi \to \diamond\varphi)$.  
（結論を $\neg\square\bot$ まで強めることは**不可**: $\Sigma_1 C$ を満たす Rosser 述語が存在する）

**Prf.** 背理法: $\forall\varphi\; T \vdash (\square\varphi \to \diamond\varphi)$ とする.  
$T \vdash \pi \Leftrightarrow \neg\square\pi$ (Gödel 文).  
$T \vdash \neg\pi \to \square\neg\pi$ (by $\Sigma_1 C$).  
$T \vdash \square\pi \to \square\neg\pi$ (Gödel 文より).  
$T \vdash \square\pi \to \diamond\neg\pi$ (仮定).  
$T \vdash \square\pi \to \neg\square\pi$.  
$T \vdash \neg\square\pi$, $T \vdash \pi$: 矛盾. $\square$

---

## 3. Kurahashi (2021)

**Th.** $Pr_T$ が M と D3 を満たすなら, $\exists\varphi\; T \nvdash (\square\varphi \to \diamond\varphi)$.  
（結論を $\neg\square\bot$ に強めることは**不可**）

**Prf.** 背理法: $\forall\varphi\; T \vdash (\square\varphi \to \diamond\varphi)$ とする.  
$T \vdash \pi \Leftrightarrow \neg\square\pi$ (Gödel 文).  
$T \vdash \square\pi \to \square\neg\square\pi$ (by M).  
$T \vdash \square\pi \to \diamond\neg\square\pi$ (仮定).  
$T \vdash \square\pi \to \neg\square\square\pi$.  
D3: $T \vdash \square\pi \to \neg\square\pi$.  
$T \vdash \neg\square\pi$, $T \vdash \pi$: 矛盾. $\square$

### 3.1. 改良版 (Kurahashi): E + D3

**Th.** $\{E, D3\} \Rightarrow T \nvdash Con_T^S$.

**Prf.** 同様の背理法: E による等値置換で $\square\pi \Leftrightarrow \square\neg\square\pi$ を導く. $\square$

*注意: この結論は Ros には持ち上げられない（E と D3 を満たす Rosser 述語が存在する）.*

---

## 4. Hilbert–Bernays (1939)

**Th.** $Pr_T(x)$ が M, CB, $\Delta_0 C^U$ を満たすなら,  
$T \nvdash \forall x\; (\mathrm{Fml}(x) \land Pr_T(x) \to \neg Pr_T(\neg x))$.

*前提が非常に弱い繊細な G2. 結論を $Con_T^S$ に強めることはできない.*

### 4.1. 改良版 (Kurahashi)

**Th.** (a) $\{CB\} \Rightarrow T \nvdash RFN_T(\Delta_0)$.  
(b) $\{\Delta_0 C^U\} \Rightarrow T + Con_T^H \vdash RFN_T(\Delta_0)$.

**Prf of (a):** CB: $Pr_T(\ulcorner\forall x\varphi(x)\urcorner) \to \forall x\; Pr_T(\ulcorner\varphi(x)\urcorner)$ かつ $\forall\varphi\in\Delta_0 \forall x\; (Pr_T(\ulcorner\varphi(x)\urcorner) \to \varphi(x))$ を仮定. これより $\forall\Psi\in\Pi_1\; (Pr_T(\ulcorner\Psi\urcorner) \to \Psi)$. Gödel 文 $\pi$ について $Pr_T(\ulcorner\pi\urcorner) \to \pi$: 矛盾. $\square$

**Prf of (b):** $\Delta_0 C^U$ と $Con_T^H$ を仮定. $\varphi\in\Delta_0$, $\forall x\; \varphi(x)$ ならば $Pr_T(\ulcorner\varphi(x)\urcorner)$, $Con_T^H$ より $\neg Pr_T(\ulcorner\neg\varphi(x)\urcorner)$, よって $RFN_T(\Delta_0)$. $\square$

*注意: $\Delta_0 C^U$ は $RFN_T(\Delta_0)$ の逆.*

---

## 5. Montagna (1979)

**Th.** $Pr_T(x)$ が $D2^G$ と $PC^G$ を満たすなら, $T \nvdash \exists x\; (\mathrm{Fml}(x) \land \neg Pr_T(x))$.

*前提が非常に強い.*

---

## 6. Buchholz (1993)

**Th.** $Pr_T(x)$ が $D1^U$ と $D2^U$ を満たすならば, $D1^U + D2^U \Rightarrow \Sigma_1 C^U$.

**Cor (G2):** $D1^U + D2^U \Rightarrow T \nvdash \neg Pr_T(\ulcorner 0=1\urcorner)$.

*この系の結論を $Con_T^G$ に強めることはできない.*

---

## Open Problems (算術的 G2 まわり)

- **Q.** $M^U \Rightarrow T \nvdash Con_T^L$? ($M^U$ は TM を導くか？)
- **Q.** $\{wM, D3\} \Rightarrow T \nvdash Con_T^S$ に弱められるか？
- **Q.** D2 の前提を $wM$ に弱めた形式化された G1 (FedG1) と G2 を分離する述語モデルは存在するか？  
  FedG1: $T \vdash \neg\square\bot \to \neg\square\neg\square\bot$.
- **Q.** Ros fail と Löb fail の関係性を調べよ.
  - Löb $\Rightarrow T \vdash Con_T^L$.
  - Ros: $\varphi \to \bot \;\Big|\; \square\varphi \to \bot$ に対応 ($M + \neg\square\bot$ に対応？).

---

## References

- Jeroslow, R. G. (1973). *Redundancies in the Hilbert-Bernays derivability conditions for Gödel's second incompleteness theorem.* JSL.
- Kurahashi, T. (2021). *Rosser provability and the second incompleteness theorem.* MLQ.
- Hilbert, D. & Bernays, P. (1939). *Grundlagen der Mathematik II.*
- Montagna, F. (1979). On the diagonalizable algebra of Peano arithmetic. *Boll. UMI*.
- Buchholz, W. (1993). A note on the ordinal analysis of IDω. In: *Proof Theory*, Springer.
- Beklemishev–Shamkanov (2016), LMCS 12(2).
