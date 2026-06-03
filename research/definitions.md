# Definitions

This file normalizes recurring definitions for the APS/G2-ZOO project.

## Abstract Provability Structure

An abstract provability structure is treated as preorder-like data

$$
S=(L_S,\le_S,\Box,\boxtimes,T,\bot).
$$

The intended readings are:

$$
T\le_S x
\quad\text{means}\quad
x\text{ is provable},
$$

$$
x\le_S\bot
\quad\text{means}\quad
x\text{ is refutable}.
$$

The symbols $T$ and $\bot$ are distinguished APS constants; a preAPS need
not make them greatest or least elements unless this is stated separately.

**Bottom discipline** is the additional order principle:

$$
\forall x\in L_S,\quad \bot\le_S x.
$$

Read proof-theoretically, this is an ex-falso or absurdity-weakening principle:
from the contradiction/refutation constant one may weaken to any element. In the
four-element model `M4-G2FG2FP`, all instances of bottom discipline already hold
except $\bot\le c$, so the residuated order repair is exactly the missing
bottom-discipline instance for the $c$-branch.

## G2

$$
\mathrm{G2}(S):
\quad
\boxtimes T\le_S\bot
\Rightarrow
T\le_S\bot.
$$

Read: if the consistency-like assertion is refutable, then the system is already inconsistent.

## FG2

$$
\mathrm{FG2}(S):
\quad
\boxtimes\boxtimes T\le_S\boxtimes T.
$$

Read: a formalized second incompleteness principle internal to the APS order.

For $k\ge 1$, define:

$$
\mathrm{nFG2}(k):
\quad
\boxtimes^{k+1}T\le_S\boxtimes^kT.
$$

Thus FG2 is $\mathrm{nFG2}(1)$. The $T$-orbit of $\boxtimes$ is:

$$
T,\boxtimes T,\boxtimes^2T,\ldots
$$

All-level nFG2 means $\mathrm{nFG2}(k)$ holds for every $k\ge 1$. In finite
preAPS models this is equivalent to eventual stabilization of the tail orbit at
a syntactic $\boxtimes$-fixed point.

The **first-true nFG2 depth** of a model is the least $d\ge 1$ such that
$\mathrm{nFG2}(d)$ holds, if such a $d$ exists. The family $D_N$ in
`research/notes/g2-fg2-hierarchy.md` has first-true depth $N+1$.

If $S$ is non-collapsed, i.e. $T\not\le_S\bot$, then G2 holds iff
$\boxtimes T\not\le_S\bot$. Thus G2 in non-collapsed finite preAPS models is
always vacuous in the material-implication sense.

## Fixed Point Principles

Jeroslow/refutability fixed point:

$$
\exists p\,(p=_S\boxtimes p).
$$

Godel/negated provability fixed point:

$$
\exists p\,(p=_S\neg\Box p).
$$

These must be kept distinct unless $\boxtimes$ is explicitly defined from $\neg\Box$.

## Completion Vocabulary

For a preorder $L$ and $X\subseteq L$, write:

$$
X^u=\{a\in L:\forall x\in X,\ x\le a\},
\qquad
X^l=\{a\in L:\forall x\in X,\ a\le x\}.
$$

A MacNeille-closed lower cut is a set $C\subseteq L$ such that:

$$
C=(C^u)^l.
$$

The MacNeille completion $\widehat L$ is the ordered collection of these
closed lower cuts, with the principal embedding:

$$
i(a)=(\{a\}^u)^l.
$$

A completion-generated fixed point for $\boxtimes$ is an element
$q\in\widehat L$ satisfying:

$$
q=\widehat{\boxtimes}q.
$$

A syntactic fixed point is a formula-level or APS-level element $p\in L$
satisfying:

$$
p=\boxtimes p.
$$

A completion fixed point is reflected when $q=i(p)$ for such a $p$, or when
a stated definable/compact rounding lemma recovers such a $p$ from $q$.

For antitone $\boxtimes$, the extension should be treated as a monotone map
into the order dual before any comparison back with $\widehat L$.

The **correct lower extension** of an antitone $\boxtimes:L\to L$ to
MacNeille cuts is the map $\widehat{\boxtimes}:\widehat L\to(\widehat L)^{op}$
defined by:

$$
\widehat{\boxtimes}(C) = \bigl((\boxtimes[C])^{l_L}\bigr)^{u_L},
$$

i.e., the $L^{op}$-MacNeille closure of the pointwise image $\boxtimes[C]$.
This satisfies the extension condition
$\widehat{\boxtimes}(i(a))=i_{L^{op}}(\boxtimes a)$ for all $a\in L$.

**Warning**: computing $((\boxtimes[C])^{u_L})^{l_L}$ instead (the
$L$-MacNeille closure) is the wrong polarity. It agrees with the correct
formula on lattice models (where every cut is principal) but diverges on
non-lattice models, producing spurious completion fixed points.

A completion fixed point $q$ is **reflected** iff $q=i(p)$ for some
syntactic fixed point $p\in L$ (i.e., $\boxtimes p = p$).

A completion fixed point is **principal-unreflected** iff $q=i(a)$ for some
$a\in L$ but $\boxtimes a \neq a$. Principal-unreflected fixed points can
appear even in lattice models (as in `three-chain-antitone` where $q=i(t)$
with $\boxtimes t = b\neq t$).

## Residuated APS

A residuated APS adds a resource composition and residuals:

$$
(L,\le,\otimes,\mathbf 1,\backslash,/,\Box,\boxtimes,T,\bot).
$$

The residuation law is:

$$
a\otimes b\le c
\iff
b\le a\backslash c
\iff
a\le c/b.
$$

For finite structural-rule checks in the G2-ZOO notes, use:
$$
E:\ a\otimes b=b\otimes a,
\qquad
C:\ a\otimes a\le a,
$$
and the strong weakening form
$$
W:\ a\le b\Rightarrow a\otimes c\le b.
$$
The reflexive instance of $W$, $a\otimes c\le a$, is recorded separately in
machine reports as `discarding_reflexive_W`.

For the bottom-disciplined $B_N$ family, the
**truncated-exponent $U$-absorbing tensor** is the commutative tensor with
unit $T$, zero $b$, $U$ absorbing over nonzero non-unit factors, and
exponents

$$
e(s)=e(a_{N+1})=1,\qquad e(a_i)=i+1\quad(1\le i\le N).
$$

For $x,y\in\{s,a_1,\ldots,a_{N+1}\}$,

$$
x\otimes y=
\begin{cases}
a_{e(x)+e(y)-1} & e(x)+e(y)\le N+1,\\
U & e(x)+e(y)>N+1.
\end{cases}
$$

The case $e(x)+e(y)=1$ never occurs for two non-unit factors, so the
ambiguous exponent-1 pair $s,a_{N+1}$ only matters in residuals, where
$a_{N+1}$ is the maximum element with exponent 1 because $s\le a_{N+1}$.

For $N\ge 3$, the **front-shifted non-$U$-absorbing tensor** on $B_N$ is
the commutative tensor with unit $T$, zero $b$, front set
$F=\{a_1,a_2\}$, and tail
$$
R_N=\{s,a_{N+1},a_3,\ldots,a_N\}.
$$
The front elements are orthogonal idempotents:
$$
a_1^2=a_1,\qquad a_2^2=a_2,\qquad a_1a_2=b.
$$
For $p\in F$ and $r\in R_N\cup\{U\}$, set
$$
p\otimes r=p,\qquad U\otimes p=p.
$$
On the tail, put
$$
\tau(s)=\tau(a_{N+1})=1,\qquad \tau(a_i)=i-1\quad(3\le i\le N),
$$
let $\rho(1)=a_{N+1}$ and $\rho(q)=a_{q+1}$ for $2\le q\le N-1$, and set
$$
r\otimes r'=
\begin{cases}
\rho(\tau(r)+\tau(r')) & \tau(r)+\tau(r')\le N-1,\\
U & \tau(r)+\tau(r')>N-1.
\end{cases}
$$
Finally $U\otimes r=U$ for $r\in R_N$ and $U^2=U$. This template is not
$U$-absorbing because $U\otimes a_1=a_1$ and $U\otimes a_2=a_2$.

Its residuals are symmetric, so it is enough to give $m\backslash c$. Write
$p^\perp$ for the other front element, i.e. $a_1^\perp=a_2$ and
$a_2^\perp=a_1$. Then:
$$
b\backslash c=U,\qquad T\backslash c=c,
$$
$$
p\backslash c=
\begin{cases}
U & c\in\{p,U\},\\
p^\perp & \text{otherwise}
\end{cases}
\quad(p\in F),
$$
and
$$
U\backslash c=
\begin{cases}
U & c=U,\\
c & c\in F,\\
b & \text{otherwise.}
\end{cases}
$$
For $r\in R_N$:
$$
r\backslash c=
\begin{cases}
U & c=U,\\
c & c\in F,\\
T & c=s,\ r=s,\\
T & c=a_{N+1},\ r\in\{s,a_{N+1}\},\\
T & c=r\in\{a_3,\ldots,a_N\},\\
a_{N+1} & c=a_j,\ 3\le j\le N,\ j-1-\tau(r)=1,\\
a_{d+1} & c=a_j,\ 3\le j\le N,\ d=j-1-\tau(r),\ 2\le d\le N-1,\\
b & \text{otherwise.}
\end{cases}
$$
Commutativity gives the same right residuals.

The same tensor has a useful **front ideal-extension presentation**. Let
$$
I=\{b,a_1,a_2\}.
$$
Then $I$ is a downward closed two-sided tensor ideal:
$$
x\le y\in I\Rightarrow x\in I,\qquad I\otimes L\subseteq I.
$$
Inside $I$, the nonzero front elements form an orthogonal idempotent
zero-band:
$$
a_1^2=a_1,\qquad a_2^2=a_2,\qquad a_1a_2=b.
$$
Multiplication by any element outside the other front atom projects back to the
chosen front atom:
$$
a_i\otimes x=a_i
\quad(x\notin\{b,a_{3-i}\}).
$$
The Rees quotient collapsing $I$ to its zero $b$ is the shifted tail monoid
on representatives
$$
\{b,T,U,s,a_{N+1},a_3,\ldots,a_N\}.
$$
Thus the construction is best viewed as an ideal extension of the shifted
truncated tail by a two-atom contractive front ideal, not as a direct product.
This explains the structural-rule profile: contraction holds locally in $I$,
while the quotient tail retains the noncontractive resource-sensitive behavior.
The finite checker
`code/scripts/check-front-shifted-extension-presentation.py` verifies this
presentation on the saved depth-3, depth-4, and depth-5 instances.

More generally, the **orthogonal front-width schema** replaces the front by
$$
F_k=\{a_1,\ldots,a_k\}
$$
with pairwise zero product and idempotent diagonal, then shifts the tail to
$$
\{s,a_{N+1},a_{k+1},\ldots,a_N\}.
$$
The finite report `artifacts/reports/front-ideal-size-bound-check.json` checks this
schema at depths 3, 4, and 5. Front widths $k=0,1,2$ are fully residuated in
those checks, while $k\ge3$ fails immediately by non-principal residual
fibers: for $p\in F_k$, the fiber of $p\backslash b$ contains
$\{b\}\cup(F_k\setminus\{p\})$, which has multiple incomparable maximal
front atoms when $k\ge3$. Thus the two-atom front is maximal in the present
same-order orthogonal-front schema, though a one-atom non-$U$-absorbing
variant remains available and should get its own closed residual table.

**Front-rigidity ceiling (Pass 34).** The orthogonal idempotent zero-band is not
just *a* front but the *forced* one. Any commutative, monotone, fully residuated
same-carrier/order tensor on $B_N$ ($N\ge1$) satisfies the *front integrality*
inequality $a_i\otimes a_j\le a_j$ on the incomparable front (monotonicity
against $a_i\le U$ together with principality of the diagonal fiber
$a_j\backslash a_j$ force $U\otimes a_j\le a_j$). With commutativity this yields
$a_i\otimes a_j\le a_i\wedge a_j=b$ for $i\ne j$ and $a_i^2\in\{a_i,b\}$ — i.e.
the orthogonal zero-band. Consequently a finite *group* on the front exists iff
$\lvert G\rvert=1$: the Pass-33 cyclic-group "Route A" is refuted, since a
nontrivial group forces $U$-absorption and breaks the diagonal residual. See
`code/scripts/check-front-group-order-bound.py` and the Front Rigidity section of
`research/notes/g2-fg2-hierarchy.md`.

**Order-theoretic diagnosis (Pass 35).** Front rigidity is *not* an artifact of
commutativity or integrality. Dropping commutativity (admitting two residuals
$\backslash,/$ with independent left/right $U$-actions) does not reopen group
fronts: for a group front $F_k\cong G$ with $k\ge2$ the translations
$L_{a_j},R_{a_j}$ permute $F_k$, so two-sided monotonicity forces
$a_j\otimes U=U\otimes a_j=U$, and both diagonal fibers $a_j\backslash a_j$, $a_j/a_j$ strand the
incomparable pair $\{T,a_{i_0}\}$ (global unit vs. local group identity), whose
sole common upper bound $U$ is excluded by absorption; hence neither fiber is
principal and $\lvert G\rvert=1$ even non-commutatively (incl. $S_3$). See
`code/scripts/check-noncommutative-front-group-bound.py`.

**Selective median $m=T\vee e_G$ (Pass 37).** $B_N^{\mathrm{med}}$ is the
bottom-disciplined $B_N$ augmented by one element $m$ with order
$b,T,e_G\le m\le U$ ($e_G=a_1$ the group identity), $m$ incomparable to every
non-identity front atom and to the tail; the tensor keeps $b$ zero, $T$ unit,
the group product on $F_k$, sets $m\otimes m=m$, $m\otimes g=g\otimes m=g$ for
front $g$, $a_j\otimes m=a_j$, and collapses every remaining nonzero non-unit
product to $U$; $\boxtimes m:=b$ (forced, since $\boxtimes m\le\boxtimes
T\wedge\boxtimes e_G=a_1\wedge a_2=b$).

**Missing-join principle (Pass 37).** A finite group fits the residuated front
of $B_N$ iff the order supplies a common upper bound of the obstructing pair
$\{T,e_G\}$ *strictly below* the absorbing top $U$. The same-carrier rigidity
ceiling $\lvert G\rvert=1$ of Passes 34–36 is therefore exactly the failure
$T\vee e_G=U$; the minimal repair is the single join $m=T\vee e_G$, after which
the diagonal fiber $a_j\backslash a_j=\{b,T,e_G,m\}$ is principal with maximum
$m$ and $\lvert G\rvert$ becomes unbounded (finite abelian, machine-verified
$\mathbb Z/2,\dots,\mathbb Z/5$).

**Single-median uniformity (Pass 38).** Dropping commutativity does *not* demand
extra order data. For the two-residual $B_N^{\mathrm{med}}$ the *same* one-point
median $m=T\vee e_G$ makes *both* diagonal fibers principal,
$a_j\backslash a_j=a_j/a_j=\{b,T,e_G,m\}$, because left/right group translations
are bijections and the only join-deficient pair below $U$ remains $\{T,e_G\}$
regardless of $\lvert G\rvert$ or conjugacy structure. Hence $\#$(medians needed)
$=1$ for every finite front group — it is *not* a new group invariant.
Machine-verified for $S_3$, $D_4$, $Q_8$ (and the abelian control $\mathbb
Z/4$) by `code/scripts/check-noncommutative-selective-median.py`.

**$G^1$-block / collapsing-ideal decomposition (Pass 39).** In
$B_N^{\mathrm{med}}$ the nonzero non-unit multiplicative part splits as
$M^\ast=(F\cup\{m\})\sqcup C$ with $C=\{a_{N+1},s,U\}$. The block
$F\cup\{m\}\cong G^1$ is the group $G$ with a *freshly adjoined* identity $m$:
$m$ is the two-sided block identity ($m\otimes g=g\otimes m=g$, $m^2=m$), while
the group identity $e_G=a_1$ is *not* the block identity ($e_G\otimes m=e_G\ne
m$), so $G$ sits inside as a subsemigroup-not-submonoid. $C$ is a two-sided
tensor ideal on which every product collapses to $U$. Thus $M^\ast$ is the ideal
extension $G^1\hookrightarrow M^\ast\twoheadrightarrow\{U\}$; associativity is
ideal-extension associativity and is independent of the Cayley table of $G$.

**Front-inverting anti-automorphism $\phi$ (Pass 39).** $\phi(a_i)=a_{i^{-1}}$
on the front, $\phi=\mathrm{id}$ off $F$. $\phi$ is an order-automorphism (it
permutes the front antichain, fixes $a_1=e_G$, preserves $a_1\le m$) and a
tensor anti-automorphism, $\phi(x\otimes y)=\phi(y)\otimes\phi(x)$. It carries
left residual fibers to right residual fibers, so for $B_N^{\mathrm{med}}$ "every
left fiber is principal" implies "every right fiber is principal" with no
separate computation — the formal device behind two-sided residuation from a
one-sided check.

**Uniform selective-median theorem (Pass 39).** For *every* finite group $G$,
$B_N^{\mathrm{med}}$ ($N=\lvert G\rvert$) with front $F_k\cong G$ and the single
median $m=T\vee e_G$ is fully two-sided residuated; $\#$(medians needed) $=1$ and
the maximum front-group order is $\infty$, uniformly in $G$. Proof = three
$G$-free lemmas: (1) ideal-extension associativity via the $G^1$-block; (2)
monotonicity using only $a_1\otimes a_j=a_j=m\otimes a_j$ (the identity law);
(3) fiber classification — diagonal fibers always strand exactly $\{T,e_G\}$
(capped by $m$), off-diagonal fibers $\{b,a_{p^{-1}r}\}$ strand no pair.
Empirically reconfirmed for $\mathbb Z/6,(\mathbb Z/2)^3,D_5,A_4,S_4$ (up to
order 24) by `code/scripts/check-uniform-selective-median-theorem.py`.

**Poset $\mathcal M$ of admissible medians (Pass 40).** Fix the
$B_N^{\mathrm{med}}$ order minus its median, $M_0$, with collapsing ideal
$C=\{a_{N+1},s,U\}$ and front $F\cong G$. A *candidate median* is a single fresh
$m'<U$ with the monotone-forced least tensor extension $a\otimes m':=
\bigvee\{a\otimes z:z\le m'\}$; it is *admissible* iff $\otimes$ stays monotone
and every diagonal fiber $a_p\backslash a_p$ is principal. $\mathcal M$ is the
poset of admissible medians under $\downarrow$-inclusion. **Theorem (Pass 40):
$\mathcal M$ is a singleton** $\{T\vee e_G\}$ — the least repair is the *only*
repair, for every finite $G$.

**Backwards-Cap-Ejection uniqueness principle (Pass 40).** The Cap-Ejection
lemma (Pass 36 — a ceiling over the whole front is ejected by monotonicity) run
in reverse pins the median: any element a candidate median dominates *beyond*
the obstructing pair $\{T,e_G\}$ is ejected, because (i) tail/ideal elements $z$
have $a_p\otimes z=U$, forcing $a_p\otimes m'=U\not\le a_p$, and (ii)
non-identity front atoms $a_q$ have $a_p\otimes a_q=a_{pq}\not\le a_p$. Hence
$\downarrow m'\cap M_0=\{b,T,e_G\}$ and $\uparrow m'=\{U\}$ are *forced*. The
median is thus a representable (free) repair: $m=T\vee e_G$ computed in the
largest sub-join-subsemilattice of $\downarrow U$ avoiding $C\cup(F\setminus
\{e_G\})$, both initial and terminal in $\mathcal M$.

**Cardinality-freedom of $B^{\mathrm{med}}$ residuation (Pass 40).** For *any*
group $G$ (finite or infinite) every residual fiber of $R(G)$-with-median is
either $\le4$ elements (diagonal $\{b,T,e_G,m\}$, off-diagonal
$\{b,a_{p^{-1}r}\}$) or the whole carrier (cofinal at $U$); no proper infinite
fiber arises, so full residuation needs no infinitary suprema beyond the
absorbing top. Residuation transfers verbatim to $\mathbb Z,\mathbb Q,S_\infty$.

**Limit fixed point $s_\omega$ (Pass 40).** When the front is infinite and also
carries the $\boxtimes$-orbit, the orbit $T\to a_1\to a_2\to\cdots$ has no
terminal stage; nFG2($k$) is false for all finite $k$ and FP-synt fails unless
one adjoins $s_\omega:=\bigwedge_{n<\omega}\boxtimes^n T$ (the orbit meet) with
$\boxtimes s_\omega=s_\omega$. This is the orbit-side (not front/residual-side)
completion; cf. the on-file infinite-orbit-stabilization problem.
