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

## Iterated Consistency Tower

For an AMS/preAPS, define:

$$
C_0:=T,\qquad C_{n+1}:=\boxtimes C_n.
$$

The Pass-69 G2-ZOO layer uses the following APS-level consistency names:

$$
\mathrm{Con}^{\mathrm{orb}}_n(S):\quad C_n\nleq_S\bot,
$$

$$
\mathrm{G2}_n(S):\quad C_n\le_S\bot\Rightarrow T\le_S\bot,
$$

$$
\mathrm{FG2}_n(S):\quad C_{n+1}\le_S C_n.
$$

Thus $\mathrm{FG2}_n$ is exactly $\mathrm{nFG2}(n)$.  The statement
$\mathrm{Flat}_{\le N}$ means that the distinct values occurring in the checked
finite orbit $C_0,\ldots,C_N$ are pairwise incomparable.  Equality is allowed
when a finite cycle returns to an earlier value.  This is a finite shadow of the
infinite star-dynamic consistency tower.

The cut/collision consistency statement is:

$$
\mathrm{CutA3}(S):\quad
x\le_S\Box y\ \wedge\ x\le_S\boxtimes y
\Rightarrow
x\le_S\boxtimes T.
$$

This is APS axiom A3 read as a consistency principle: no proof/refutation
collision survives except below the base consistency element $\boxtimes T$.

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

**Limit fixed point $s_\omega$ (Pass 40, REFUTED Pass 41).** Originally proposed:
when the front is infinite and carries the $\boxtimes$-orbit, adjoin
$s_\omega:=\bigwedge_{n<\omega}\boxtimes^n T$ (the orbit meet) with $\boxtimes
s_\omega=s_\omega$ to recover FP-synt. **Pass 41 refutes this as an order-attached
fixed point (Theorem 41b):** for an antitone $\boxtimes$, no fresh $\sigma$ with
$\boxtimes\sigma=\sigma$ that is below all / above all / sandwiche

**Orbit flatness and $T$-reachability of a cycle (Pass 47).** For an antitone
$\boxtimes$ on a finite poset $L$ and seed $T$, write $o_n=\boxtimes^n T$ and let
$C\subseteq\{o_n\}$ be the *eventual cycle* (the terminal $\boxtimes$-periodic
set of the orbit). The orbit is **flat** if $C$ is an antichain (a singleton
counts). A cycle $K\subseteq L$ is **$T$-reachable** if $K=C$ for the orbit of
$T$ (equivalently $\exists n\, o_n\in K$). The Pass-44 local equivalence
"$T$-orbit descends $\Leftrightarrow$ $T$ reaches an attached fixed point" holds
along $O(T)$ exactly when the orbit is flat (Thm 47b); this gate is *independent*
of bottom discipline ($C_5$ is bottom-disciplined-but-not-flat; the
sub-$\bot$-augmented $R_2$ is flat-but-not-bottom-disciplined), and $B_N$
satisfies it because its front is an antichain with a degenerate sink, not
because $\bot$ is least (Prop 47c). The correct predicate is *reachability*, not
*existence*: a $\{\bot,U\}$ chain-cycle may coexist in a flat $B_N$ yet be
unreachable from $T$.

**Bracketing involution and cube-gap (Pass 48).** For a comparable eventual
$2$-cycle $\{a,b\}$, $a<b$, on a finite poset, the interval $I=[a,b]$ is
$\boxtimes$-invariant, $F:=\mathrm{Fix}(\boxtimes^2)\cap I$ contains $a,b$, and
the **bracketing involution** is $\tau:=\boxtimes|_F$, an order-reversing
involution of $F$ swapping $a\leftrightarrow b$. The cycle **brackets** a fixed
point iff $\tau$ has a fixed point; sufficiently, $|F|$ odd (Thm 48a). On a chain
$F=I$, recovering Thm 47d. A **cube-gap** is a comparable $2$-cycle with
$\mathrm{Fix}(\boxtimes)\cap I=\varnothing$ on a fat interval; the paradigm is the
Boolean cube $2^{[n]}$ under complementation $\boxtimes S=S^c$, with comparable
$2$-cycle $\{\varnothing,[n]\}$, $|I|=2^n$, and no fixed point. The cube shows
that neither $|I|$ nor its parity controls bracketing (the same $2^2$ carries an
order-reversing involution with two fixed points); only the cycle type of $\tau$
does. Cube-gaps are the higher-dimensional analogue of the even-chain Rosser gap
and of the $M_3$ gadget $R_2$.

**Period-$2k$ Rosser gadget $R_{2k}$ (Pass 48).** The family generalizing the
Pass-42 gadget $R_2$: carrier $\{b,o_0,\dots,o_{2k-1},p,U\}$ with $b$ least, $U$
greatest, $\{o_0,\dots,o_{2k-1},p\}$ an antichain, $\boxtimes$ the $2k$-cycle on
the $o_i$ together with $\boxtimes p=p$, $\boxtimes b=U$, $\boxtimes U=b$. Each
$R_{2k}$ is antitone, realizes FP-synt via the *detached* fixed point $p$, and has
a fixed-point-free antichain eventual cycle of even period $2k$ reachable from
$T=o_0$. By Prop 48c (period-$k$ detachment) any $\boxtimes$-fixed point
coexisting with an antichain cycle of period $\ge2$ is necessarily detached, so
$R_{2k}$'s $p$ is forced incomparable to the entire orbit. $R_4$ is the first new
instance; its $\boxtimes^2$ is a free $\mathbb Z/2$ on the front
$(o_0\,o_2)(o_1\,o_3)$.

### Smith bracketing / fixed-vertex criterion (Pass 49)

Given an antitone $\boxtimes$ with a comparable eventual $2$-cycle $\{a,b\}$
($a<b$), invariant interval $I=[a,b]$, fixed-square set
$F=\mathrm{Fix}(\boxtimes^2)\cap I$, and bracketing involution
$\tau=\boxtimes|_F$ (order-reversing, $\tau(a)=b$), let $\Delta(F)$ be the
**order complex** of $F$ (simplices = nonempty chains). $\Delta(F)$ is
$\mathbb F_2$-acyclic (cone with apex $a=\min F$), and $\tau$ acts simplicially.
By Smith theory the fixed subcomplex $|\Delta(F)|^{\tau}$ is nonempty and
$\mathbb F_2$-acyclic with Lefschetz number $L(\tau)=1$. The **Smith bracketing
criterion** is
$$
\boxtimes\text{ brackets in }I\iff |\Delta(F)|^{\tau}\text{ meets the }0\text{-skeleton}
\iff \exists\ \tau\text{-invariant chain of odd cardinality.}
$$
The **cube-gap** is the degenerate witness $F=2^{[n]}$, $\tau=$ complementation,
where $|\Delta(F)|^{\tau}$ is the lone barycenter of the flipped edge
$\{\varnothing,[n]\}$ — nonempty/acyclic but vertex-free, hence no bracket; odd
$|F|$ (Thm 48a) is the special case $F=$ a single odd invariant chain.

### Phantom chain-lattice $P$ (Pass 49)

The complete lattice
$P=\{o_0<o_1<\cdots\}\cup\{a^{*}=\bigvee_n o_n\}\cup\{m\}\cup\{b^{*}\}\cup\{\top\}$
with covers $a^{*}\prec m$, $a^{*}\prec b^{*}$, $m\prec\top$, $b^{*}\prec\top$
(so $a^{*}$ has two covers). An antitone $\boxtimes$ with
$\boxtimes(o_{2n})\uparrow b^{*}$ and $\boxtimes(a^{*})=m<b^{*}$ fails
join-continuity at the **single** cover $a^{*}\prec\{m,b^{*}\}$, producing a
phantom limit $2$-cycle (Construction 49b). Demonstrates: one failed join-cover
suffices to reinstate the Thm-41c phantom; join-continuity (Thm 48b) is not
relaxable to "continuous off a finite set."

### Group-orbit Rosser gadget / non-integral unit (Pass 49)

The relation-free diamond $M_5=\{\bot,o_0,o_1,o_2,o_3,p,\top\}$ with box$=\mathrm{id}$,
refutability the free $\mathbb Z/4$-orbit $(o_0\,o_1\,o_2\,o_3)$, and detached fixed
point $\boxtimes p=p$, equipped with a commutative full-residuated tensor whose
**unit is the non-integral element $p$** (equivalently $o_0$). Census:
$411$ residuated tensors with unit $=p$ (and $411$ with unit $=o_0$, the $S_4$
front-symmetry classes), $0$ integral (unit $=\top$). Integral obstruction = the
$M_n$ ($n\ge3$) phenomenon: $\top\backslash\bot$ has the non-principal fiber
$\{b\}\cup(\text{atoms}\setminus\{a\})$. Establishes (Thm 49d) that front rigidity
forbids group *tensors* on a $B_N$ front but NOT a free group *orbit* carrying a
detached fixed point, the escape REQUIRING a non-integral unit. Witness:
`code/models/examples/R4-residuated.json`.

## Self-dual subposet $F^{\tau}$ and the vertex-counting Euler invariant $e(F^\tau)$ (Pass 50)

For a comparable eventual $2$-cycle with bracketing involution
$\tau=\boxtimes|_F$ on $F=\mathrm{Fix}(\boxtimes^2)\cap I$, the **self-dual
subposet** is $F^{\tau}=\{x\in F:\boxtimes x=x\}$ (the $\boxtimes$-fixed elements
of the interval). Its **vertex-counting Euler invariant** is
$e(F^{\tau})=\chi(\Delta(F^{\tau}))$, the Euler characteristic of its order
complex. By the Hopf-trace split of the simplicial Lefschetz number,
$L(\tau)=e(F^{\tau})+\Phi(\tau)=1$, where $\Phi(\tau)$ is the signed count of
*flipped* $\tau$-invariant chains (Thm 50a). Unlike the topological
$\chi(|\Delta(F)|^{\tau})\equiv1$, $e(F^{\tau})$ sees the $0$-skeleton: $e\ne0$
witnesses the bracket, $e=0$ (with $\Phi=1$) is the cube-gap.

## Phantom Betti number $b_{\mathrm{phantom}}$ (Pass 50)

For an antitone $\boxtimes$ on a complete lattice, $b_{\mathrm{phantom}}$ counts
the independent phantom $2$-cycles created by failures of join-continuity. On the
fan $P_r$ of $r$ order-independent even-orbit arms (Constr 50b),
$b_{\mathrm{phantom}}(P_r)=\#\{\text{failed join-covers}\}=r$; phantoms are
additive in independent discontinuities (one failed cover $=$ one phantom).

## Front-cardinality decoupling: group-orbit vs group-tensor (Pass 50)

A finite group $G$ can enter a preAPS in two disjoint ways. As a **group tensor**
on a $B_N$ front it is killed by front rigidity (Pass 34/35: only the orthogonal
zero-band survives residuation). As a **free group orbit** of refutability on an
antichain front of $M_{|G|+1}$ (with a detached fixed point $p$) it survives, and
the accompanying commutative full-residuated tensor depends ONLY on the front
cardinality $n=|G|$, never on the multiplication of $G$ (Thm 50d). Thus
abelian/non-abelian fronts of equal size are residuation-indistinguishable: the
group law is carried entirely by the $\boxtimes$-orbit, the tensor by $n$. The
escape requires a **non-integral unit** ($p\ne\top$).

## Fixed-point antichain lemma & deflation of $e(F^{\tau})$ (Pass 51)

For any antitone $\boxtimes:L\to L$, $\mathrm{Fix}(\boxtimes)$ is an **antichain**
(Lemma 51a: $p\le q$ both fixed $\Rightarrow q=\boxtimes q\le\boxtimes p=p$).
Consequently the self-dual subposet $F^{\tau}=\mathrm{Fix}(\boxtimes)\cap I$ has a
*discrete* order complex, and the vertex-counting Euler invariant collapses to a
cardinality:
$$ e(F^{\tau})=\chi(\Delta(F^{\tau}))=|F^{\tau}|. $$
Hence $e$ is a **complete** bracket invariant ($e=0\iff F^{\tau}=\varnothing\iff$
no bracket), but tautologically so — "$e=0$ with $F^{\tau}\ne\varnothing$" is
impossible and the order-complex-circle pathology is unrealizable as a fixed-vertex
set (Thm 51a). The genuine homological content is the **flipped invariant**
$\Phi(\tau)=L(\tau)-e(F^{\tau})=1-|F^{\tau}|$ (the cube-gap is $\Phi=1$).

## Phantom as $\varprojlim^1$ / obstruction complex (Pass 51)

The phantom $2$-cycle of an antitone $\boxtimes$ at a failed join-cover is the
nonvanishing of $\varprojlim^1$ of the image tower $(\boxtimes o_n)_n$: the failure
$\boxtimes(\bigvee_n o_n)<\bigwedge_n\boxtimes o_n$ of $\boxtimes$ to commute with a
directed join. The **obstruction complex** is $\mathrm{Ob}^\bullet(P_r)=[\,0\to
C^1\to0\,]$ with $C^1=\mathbb F^{\{\text{failed join-covers}\}}$ and $C^0=0$
(infinitary rigidity), so the **phantom Betti number** is upgraded from a count to
a cohomology dimension, $b_{\mathrm{phantom}}(P_r)=\dim_{\mathbb F}H^1=r$, additive
because $\varprojlim^1$ commutes with finite direct sums (Thm 51b). Field
coefficients make $\varprojlim^1$ of finite-dimensional towers vanish, so the
genuine cohomology is taken over $\mathbb Z$; $C^0=0$ is a property of the
completion, not of finite truncations.

## Integral vs non-integral unit = Löb vs Rosser (Pass 51)

The unit of a full residuated tensor on an APS is **integral** if $1=\top$ and
**non-integral** otherwise. For $\boxtimes=\neg\Box$ with $\boxtimes$-fixed point
$\phi$: an integral unit exists iff $\phi$ is orbit-**attached** ($\phi=\boxtimes
\bot$), which arithmetically is the de Jongh–Sambin Löb-coincidence
$\phi\equiv\mathrm{Con}_T$; the unit is forced non-integral iff $\phi$ is
**detached**, realized only by a Rosser predicate $\Box_R$ keeping
$D1+\Sigma_1$-completeness but evading Löb (Guaspari–Solovay 1979; Kurahashi 2021).
Thus "non-integral unit" is the algebraic shadow of "Rosser predicate evading Löb"
(Thm 51c). Witnesses: attached 3-chain Gödel (integral unit $\top$); detached
$R_2/M_3$ ($0$ integral, non-integral units $\{o_0,o_1,p\}$).

## Flipped invariant $\Phi(\tau)$ and the flipped-chain sign $s(d)$ (Pass 52)

For a finite poset $F$ with minimum and an order-reversing involution
$\tau=\boxtimes|_F$ acting on the $\mathbb F_2$-acyclic order complex $\Delta(F)$,
the **flipped invariant** is $\Phi(\tau):=L(\tau)-e(F^{\tau})=1-|F^{\tau}|$, the
genuine homological residue after the Thm-51a deflation $e(F^{\tau})=|F^{\tau}|$.
Its intrinsic formula (Thm 52a) is $\Phi(\tau)=\sum_{d\ge1}s(d)N_d$, a signed
count of $\tau$-invariant $d$-chains ($N_d$ of them) weighted by the
**flipped-chain sign**
$$ s(d)=(-1)^{d}(-1)^{d(d+1)/2}=+1\ (d\equiv0,1),\ -1\ (d\equiv2,3)\ (\mathrm{mod}\ 4), $$
the period-4 pattern $+\,+\,-\,-$ arising as the simplicial degree sign times the
sign of the vertex-reversal permutation of an invariant chain.

## Fixed-antichain fan $F_m$ (Pass 52)

The poset $F_m=(\hat0<a_1,\dots,a_m<\hat1)$ with $a_1,\dots,a_m$ pairwise
incomparable and the order-reversing involution $\tau$ swapping
$\hat0\leftrightarrow\hat1$ and fixing every $a_i$. It is the pathological
extremal-*negative* companion of the cube: $|F^{\tau}|=m$ and $\Phi(\tau)=1-m$,
so the fan witnesses $\inf\Phi=-\infty$ (Thm 52b) while the cube/$C_4$ witness
$\sup\Phi=+1$. The $m$ flipped triangles $\{\hat0<a_i<\hat1\}$ ($s(2)=-1$) cancel
the $m$ fixed vertices to the single residual flipped edge $\{\hat0,\hat1\}$.

## Geometric vs combinatorial fixed-point Euler characteristic (Pass 52)

$\chi(|\Delta(F)|^{\tau})$ is the **geometric** (topological) fixed-point Euler
characteristic — by Smith theory $=1$ on an $\mathbb F_2$-acyclic complex —
counting barycenters of *all* $\tau$-invariant simplices; $\chi(\Delta(F^{\tau}))=
|F^{\tau}|$ is the **combinatorial** one, counting only fixed *vertices*. Their gap
is exactly $\Phi(\tau)=\chi(|\Delta(F)|^{\tau})-\chi(\Delta(F^{\tau}))$ (Thm 52c);
$\Phi\ne0$ iff the geometric fixed set carries flipped-chain barycenters invisible
to the vertex count.

## Dilation solenoid, integral phantom, and the Rosser-unit no-go (Pass 53–57)

*(Consolidated vocabulary for the Pass 53–57 thread; entries 53–56 are recorded here
compactly to restore the glossary after a mount-lag run skipped their inserts.)*

The **integral phantom** is the derived limit $\varprojlim^1(\mathbb Z,\times m)=
\widehat{\mathbb Z}_m/\mathbb Z$ ($\widehat{\mathbb Z}_m=\prod_{p\mid m}\mathbb Z_p$),
uncountable and divisible, of the dilation coefficient tower (Pass 53/54). It is
**radical-invariant** (depends only on $\mathrm{rad}(m)$) and a *field shadow*: over
any field the tower is Mittag–Leffler and $\varprojlim^1=0$, so the phantom is purely
integral and invisible to every finitely supported probe.

The **dilation solenoid** is the honest carrier: $C_m=\varinjlim(\mathbb Z^-,d_m)=
\mathbb Z[1/m]^-$, the negative cone of the $m$-adic localization (the *inverse* limit
is the one-point lattice), whose MacNeille completion is the classical $m$-adic
solenoid $\mathbb S_m=(\mathbb R\times\widehat{\mathbb Z}_m)/\mathbb Z$. The
**dilation refutability** $\boxtimes_m$ (Constr 55a) is Construction 49b with $m$-adic
rungs $a_n=-1/m^n\uparrow a^\ast$; its join-continuity fails at the single cover
$a^\ast$ with failure module $(\mathbb Z,\times m)$, so the phantom is $\boxtimes_m$'s
own $\varprojlim^1$. **ML $=$ nFG2 dichotomy** (Thm 55c): Mittag–Leffler $\iff$ orbit
stabilizes $\iff$ all-level nFG2 $\iff\varprojlim^1=0$ — all fail for $m\ge2$
($G2\wedge\neg$FG2), all hold at every finite truncation (the phantom is **liman**,
i.e. limit-only). Slogan **finitely Löb, limanly Rosser** (Thm 55d): finite
truncations carry an integral (Löb) unit, the limit a non-integral (Rosser) one.

The **residuation/Rosser dichotomy** (Thm 56a): the completed arena is a frame, so it
residuates under $\otimes=\wedge$ with the integral unit $\top$, but the dilation
monoid $\otimes=+$ (Rosser unit $a^\ast$) has a **non-principal cover fiber**
$c\backslash a^\ast=\{a_n\}$ (non-attained sup) and does not residuate. The
**dilation-cover Čech complex** (Thm 56b) is the two-term $\delta=\mathrm{id}-m\cdot
\mathrm{sh}$ on $\prod_n\mathbb Z$ with $\check H^0=\varprojlim=0$, $\check H^1=
\varprojlim^1=\widehat{\mathbb Z}_m/\mathbb Z$.

The **carrier-free cancellativity no-go** (Lemma 57a / Cor 57a$'$): in any complete
residuated lattice, a unit that is the *non-attained* sup of a strictly ascending
chain admits **no completely join-irreducible cover** above it (else
$c=e\otimes c=\bigvee_n(a_n\otimes c)<c$). Hence the Rosser (sup-of-chain) unit is
not merely tensor-shy but **completion-incompatible**: *Rosser unit $\perp$
join-irreducible cover*. **Phantom $\veebar$ Quantale** (Thm 57c): the ideal/downset
(Day-convolution) completion is a unital residuated quantale carrying an additive
unit, but it de-singularizes the cover (the chain's sup splits off as a principal
point), voiding the no-go's hypothesis and killing the phantom — so a residuated
additive tensor and the phantom are mutually exclusive across completions.

The **absorbing Rosser cap** $W$ (Pass 58, Thm 58a) is the pathological companion of
the no-go: the complete chain $a_0=\bot<a_1<\cdots<e<c<\top$ ($e=\bigvee a_n$
non-attained) with $\otimes$ given by $\bot$ as absorbing zero, $\min$ below the unit
$e$, and $\max$ once a *large* operand $\ge c$ appears. It is a genuine complete
commutative residuated lattice with a completely join-irreducible cover $c\succ e$ and
**cofinal absorption** $a_n\otimes c=c$ ($n\ge1$), so Lemma 57a's contradiction
$\bigvee_n(a_n\otimes c)=c$ is satisfied *trivially* (every summand already $=c$):
**cancellativity/strictness in Lemma 57a is essential, not cosmetic.** A residuated
Rosser unit *can* sit beneath a join-irreducible cover — iff the cover absorbs.

The **cancellative–absorbing dichotomy / Phantom trichotomy** (Thm 58b): for a
non-attained sup-of-chain unit beneath a join-irreducible cover $c$, the chain acts on
$c$ either *cancellatively* ($a_n\otimes c<c$ — the Pass-57 no-go, residual forced
integral/Löb, phantom only in the non-residuated MacNeille arena) or *absorbingly*
($a_n\otimes c=c$ — the cap $W$, residual present, fiber $c\backslash e=\bot$
principal, image tower constant/ML, $\varprojlim^1=0$). With the quantale escape this
makes a **trichotomy** over $\{$residuation, join-irreducible cover, phantom
$\varprojlim^1\}$: MacNeille keeps (cover, phantom), the ideal/quantale keeps
(residual, —) de-singularizing the cover, and $W$ keeps (residual, cover) killing the
phantom — *any two, never all three*. Absorbing $=$ non-free witness-comparison action
$=$ degenerate Rosser torsor; cancellative $=$ free action $=$ nontrivial torsor. The
**radical-graded naturality** (Prop 58c): $\Theta:\mathrm{Ros}_{(-)}\Rightarrow
\varprojlim^1(-)$ is a natural transformation on $\mathbf{Deriv}^{\mathrm{res}}_
{\mathrm{rad}}$, with a dilation-tower morphism $(\mathbb Z,\times m)\to(\mathbb Z,
\times m')$ existing **iff** $\mathrm{rad}(m)\mid\mathrm{rad}(m')$ — radical
divisibility the precise naturality obstruction.

## Integral phantom and the $2$-adic $\varprojlim^1$ (Pass 53)

The **phantom Betti number** $b_{\mathrm{phantom}}(P_r)=r$ (Pass 50/51) is a
*field-coefficient* invariant: over any field the image tower of a finite-
dimensional inverse system is **Mittag-Leffler** (the image filtration
$F_j(A_0)=\mathrm{im}(A_j\to A_0)$ stabilizes), so $\varprojlim^1=0$ and $r$ is
merely the rank of the finitary cochain $C^1=\mathbb F^{\{\text{failed covers}\}}$.

The **integral phantom** is the genuine derived-limit obstruction at $\mathbb Z$
coefficients with a **non-Mittag-Leffler** tower. The canonical witness is the
dyadic tower $(\mathbb Z,\times2):\ \mathbb Z\xleftarrow{\times2}\mathbb Z
\xleftarrow{\times2}\cdots$, with $F_j(\mathbb Z)=2^j\mathbb Z$ (index $2^j\to
\infty$) and, by the SES of towers $0\to(\mathbb Z,\times2)\to(\mathbb Z,
\mathrm{id})\to(\mathbb Z/2^n)\to0$,
$$\varprojlim(\mathbb Z,\times2)=0,\qquad
  \varprojlim{}^1(\mathbb Z,\times2)=\widehat{\mathbb Z}_2/\mathbb Z$$
(uncountable, divisible). It is invisible to every field and to every finitely
supported probe. More generally the **$m$-adic phantom** is
$\varprojlim^1(\mathbb Z,\times m)=\widehat{\mathbb Z}_m/\mathbb Z$ for $m\ge2$.

## The Löb/Rosser functor $L_{(-)}$ and the integral-unit subcategory (Pass 53)

$\mathbf{Deriv}$: category of **derivability packages** $(\Box,\Pi)$, $\Pi\subseteq
\{D1,D2,D3,\Sigma_1\text{-comp.},\text{Rosser witness-comparison}\}$, morphisms
relative-interpretation translations preserving $\vdash$ and $\Pi$.
$\mathbf{resAPS}$: residuated APS with $\boxtimes$- and unit-preserving
homomorphisms; $\mathbf{resAPS}_{\mathrm{int}}\subseteq\mathbf{resAPS}$ the
**integral-unit** subcategory (commutative integral residuated, tensor unit
$e=\top$).

$L_{(-)}:\mathbf{Deriv}\to\mathbf{resAPS}$ sends $(\Box,\Pi)$ to its **Lindenbaum
residuated APS** ($\otimes=\wedge$, $\backslash=\to$, $\boxtimes=\neg\Box$, unit
$e=$ chosen $\boxtimes$-fixed point). On the **Löb subcategory** $\mathbf{GL}$ it is
canonical (de Jongh–Sambin uniqueness) with $e=\top\iff$ Löb and essential image
$\mathbf{resAPS}_{\mathrm{int}}$; **Rosser packages** land in the non-integral
complement as a **unit-torsor** (non-unique Rosser fixed points). Slogan: Löb $=$
fixed-point uniqueness $=$ unit integrality $=$ canonical functoriality.

## $m$-adic dilation solenoid and the radical-invariant phantom (Pass 54)

The **$m$-adic dilation solenoid** is the inverse limit $L_\infty^{(m)}=
\varprojlim_n(\mathbb Z^-,d_m)$ of the negative-cone integral residuated lattice
$\mathbb Z^-=\{0,-1,-2,\dots\}$ ($x\otimes y=x+y$, residual $x\backslash y=\min(0,
y-x)$, unit $e=0=\top$) under the **$m$-fold dilation** $d_m(x)=mx$ — an injective,
non-surjective **residuated-lattice endomorphism** (image $m\mathbb Z^-$,
cover-fiber multiplicity $m$; the residual identity $d_m(x\backslash y)=d_m x
\backslash d_m y$ needs $m>0$ to pull through the meet). It is the honest residuated
realization of Pass 53's abstract coefficient tower: the top-cover coefficient tower
is $(\mathbb Z,\times m)$, supplied by the $\mathbb Z$-grading of $\otimes$ and never
by a poset's $\pm1$ incidence. Its derived limit is the **radical-invariant phantom**
$$ \varprojlim{}^1(\mathbb Z,\times m)=\widehat{\mathbb Z}_m/\mathbb Z,\qquad
\widehat{\mathbb Z}_m=\prod_{p\mid m}\mathbb Z_p, $$
depending on $m$ only through $\mathrm{rad}(m)=\{p:p\mid m\}$ (Thm 54b): the towers
$\times2,\times4,\times8$ are pairwise **non-isomorphic** yet **pro-isomorphic**, so
share the phantom $\widehat{\mathbb Z}_2/\mathbb Z$, while $\times6,\times12$ give
$(\mathbb Z_2\times\mathbb Z_3)/\mathbb Z$; $m=1$ (identity tower, Mittag-Leffler) is
the phantom-free boundary, and over every field the phantom collapses (purely
integral). Cor 54c: the refutability orbit must carry $\widehat{\mathbb Z}_m$ acting
by dilation on the single solenoidal cover fiber. See [[aps-run-sync-hazard]] for the
mount-lag protocol used to verify the Pass-54 edits.

## Dilation-solenoid refutability $\boxtimes_m$; ML $=$ nFG2; liman Rosser unit (Pass 55)

**Carrier correction.** The *inverse* limit $\varprojlim_n(\mathbb Z^-,d_m)$ is the
**trivial one-point lattice** ($x_0=m^nx_n\Rightarrow x_0=0$); the honest non-trivial
object is the directed **colimit** $C_m=\varinjlim(\mathbb Z^-,d_m)=\mathbb Z[1/m]^-$,
the negative cone of the $m$-adic localization (integral residuated lattice, dense
chain), whose MacNeille completion $\overline{C_m}$ is the genuine arena — *literally*
the classical $m$-adic solenoid ($\widehat{C_m}=\mathbb S_m=(\mathbb R\times
\widehat{\mathbb Z}_m)/\mathbb Z$, van Dantzig 1930).

The **dilation-solenoid refutability** $\boxtimes_m$ (Construction 55a) is
Construction 49b lifted onto $\overline{L}^{(m)}=\overline{C_m}$: rungs $a_n=-1/m^n
\uparrow a^\ast=0^-$, doubled cover $a^\ast\prec\{c,b^\ast\}\prec\top$, antitone
$\boxtimes_m\top=a_0$, $\boxtimes_m(a_{2k})\uparrow b^\ast$, $\boxtimes_m(a^\ast)=c$.
The *one* new ingredient vs 49b is **$m$-adic rung dilation** (cover fiber $m$, not
$1$), upgrading 49b's rank-$1$ field-phantom ($\varprojlim^1=0$, a shadow) to the
genuine non-ML $(\mathbb Z,\times m)$ with $\varprojlim^1=\widehat{\mathbb Z}_m/
\mathbb Z$ realized as the derived limit of $\boxtimes_m$ **itself** (Thm 55b: join-
continuity fails at the lone cover $a^\ast$, failure module $(\mathbb Z,\times m)$).

**ML $=$ nFG2 dichotomy (Thm 55c).** For the $\boxtimes_m$-image tower: Mittag–Leffler
$\iff$ orbit stabilizes $\iff$ all-level nFG2 (index-$2$, Thm 41a) $\iff$
$\varprojlim^1=0$. All four FAIL for $m\ge2$ ($\boxtimes_m$ is a perpetual non-
stabilizing orbit, $\neg$FG2) while every finite truncation satisfies all four — the
phantom is strictly **liman** (limit-only). G2 holds **vacuously**
($\boxtimes_m T=a_0\not\le\bot$); the solenoid lives in $G2\wedge\neg$FG2.

**Liman Rosser unit / fusion (Thm 55d).** Finite truncations are integral-unit (Löb-
attached); the fixed-point/unit tower is the same $(\mathbb Z,\times m)$ with
$\varprojlim=0$ (detached limit fixed point $\Rightarrow$ non-integral $\Rightarrow$
Rosser) and $\varprojlim^1=\widehat{\mathbb Z}_m/\mathbb Z$ (the unit is a **torsor**).
A residuated tensor forces a Rosser unit, and Pass-54 obligations (1) [phantom] and
(2) [Rosser torsor $=H^1$] become **one statement**: the join-continuity-failure
module of $\boxtimes_m$ *is* the Löb$\to$Rosser gluing obstruction
$H^1(\text{dilation cover};\mathrm{Aut(unit)})=\varprojlim^1$. *Slogan: finitely Löb,
limanly Rosser — the phantom is the price of gluing consistency across the solenoid.*

## Residuation/Rosser dichotomy; non-principal cover fiber; dilation-cover Čech complex (Pass 56)

**Residuation/Rosser dichotomy (Thm 56a).** The completed arena $\overline{L}^{(m)}$
(chain $C_m=\mathbb Z[1/m]^-$ Dedekind-completed $+$ the doubled cover $a^\ast\prec\{c,
b^\ast\}\prec\top$) is a complete **distributive** lattice and a **frame** (binary meet
distributes over the cover join $a^\ast=\bigvee_n a_n$), hence a complete **Heyting**
algebra: it residuates under $\otimes=\wedge$ but with the **integral** unit $\top$
(Löb). The **dilation monoid** $\otimes=+$ (unit $e=a^\ast$, the non-integral Rosser
unit, $c,b^\ast$ as positive infinitesimals above $0=a^\ast$) does **not** extend to a
residual: $x\mapsto x\otimes c$ fails join-preservation at the lone cover,
$\bigvee_n(a_n\otimes c)=a^\ast<c=a^\ast\otimes c$. So residuation and the Rosser unit
are **mutually exclusive** in the completion — keep $\wedge$ (residuated, integral, Löb)
or keep $+$ (Rosser unit, but only a preAPS). *Slogan: finitely residuated, limanly
preAPS.*

**Non-principal cover fiber.** The minimal failing residual is $c\backslash a^\ast=\{z:
z\otimes c\le a^\ast\}=\{a_n\}_n$, whose supremum $a^\ast$ is **not attained** (the cover
$a^\ast=\bigvee_n a_n$ is a non-attained sup in the completion). This is the
non-principal-fiber obstruction of the Pass-49 $M_n$ ($n\ge3$) escape, now at a
*non-attained* cover; at every finite truncation $a^\ast=a_K$ is the chain maximum, so
$c\backslash a^\ast=a_{K-1}$ is principal and both tensors residuate (finitely-true,
limanly-false). Non-principal $=$ non-attained sup $=$ the Mittag–Leffler failure that
also produces the phantom — one defect, two maps ($\boxtimes_m$ and $\otimes$).

**Dilation-cover Čech complex (Thm 56b).** The even/odd half-telescope cover
$\mathcal U=\{U_0,U_1\}$ of the dilation telescope has *interval* nerve, so its
$\check{\mathrm C}$ech complex on $\underline{\mathbb Z}_{\times m}$ (stalk $\mathbb Z=
\mathrm{Aut(unit)}$, restriction $\times m$) is the **two-term** $0\to\prod_n\mathbb Z
\xrightarrow{\ \delta=\mathrm{id}-m\cdot\mathrm{sh}\ }\prod_n\mathbb Z\to0$,
$\delta((x_n))=(x_n-m\,x_{n+1})$, with $\check H^0=\ker\delta=\varprojlim=0$ (detached
limit fixed point) and $\check H^1=\operatorname{coker}\delta=\varprojlim^1=
\widehat{\mathbb Z}_m/\mathbb Z$. Only $H^0,H^1$ occur, making Thm-55d's
$H^1=\varprojlim^1$ a literal cochain identity; the Rosser unit-torsor class is
$[(1,0,0,\dots)]\in\operatorname{coker}\delta$.

## Absorption depth, idempotence defect, and the no-partial-phantom theorem (Pass 59)

For a complete residuated tensor $\otimes$ with a non-attained sup-of-chain unit
$e=\bigvee_n a_n$ ($a_n\uparrow e$ strictly) and a completely join-irreducible cover
$c\succ e$:

**Absorption depth.** $d(\otimes):=\inf\{n\ge1:a_n\otimes c=c\}\in\{1,2,\dots\}\cup
\{\infty\}$, the first rung at which the cover absorbs the unit-approximants. By
Cor 57a$'$ the residuated regime is exactly $d<\infty$ (cofinal strict $a_n\otimes c<c$,
i.e. $d=\infty$, admits no residuation). The cover-fiber image tower $(a_n\otimes c)_n$
is non-decreasing with sup $e\otimes c=c$ and, for $d<\infty$, **eventually constant**
$=c$.

**Idempotence defect.** $\iota(\otimes):=[\,c\otimes c\ne c\,]\in\{0,1\}$; in the
witness family $W_{d,\delta}$ it equals $\delta$, with $c\otimes c=\top$ when $\delta=1$.
It is independent of $d$ and **$\varprojlim^1$-invisible**: it localizes at the *compact*
cover above $c$, not at the non-compact cover $e\prec c$ where the phantom is pinned.

**No-partial-phantom (Thm 59a / Cor 59b).** Finite absorption depth $\Rightarrow$
Mittag–Leffler $\Rightarrow\varprojlim^1=0$ genuinely — a $\varprojlim^1$ class is a
tail/pro-invariant, so there is no "finitely supported" phantom. By **Gray's dichotomy**
($\varprojlim^1$ of a tower of countable abelian groups is $0$ or of cardinality
$2^{\aleph_0}$; Gray 1966, McGibbon–Steiner 1995) no finite-rank intermediate value is
available to any invariant. Hence the Pass-58 trichotomy is **sharp**: $(d,\iota)$ are
genuine lattice moduli but *phantom-flat coordinates*; the phantom jumps
$0\to2^{\aleph_0}$ only at the non-residuated wall $d=\infty$. **Prop 59c:** absorption
depth $=$ nFG2 stabilization index $=$ Mittag–Leffler $=$ phantom-free (unifying
Thm 41a, 55c, 58b). *Slogan: a phantom is all-or-nothing — there are no partial ghosts.*

## Carrier criterion, rad-grading, phantom sheaf on $\mathrm{Spec}$, and the $\aleph_1$-phantom (Pass 60)

**Carrier criterion (Thm 60a).** A residuated cover-filtration map of dilation-solenoid
arenas $C_m\to C_{m'}$ (where $C_m=\mathbb Z[1/m]^-$, Pass 55) exists $\iff$ the
localization embeds $\mathbb Z[1/m]\subseteq\mathbb Z[1/m']$ $\iff$ $\mathrm{rad}(m)\mid
\mathrm{rad}(m')$ (every prime of $m$ divides $m'$). The grading on
$\mathbf{Deriv}^{\mathrm{res}}_{\mathrm{rad}}$ is thus **forced by the carrier**, not
decreed.

**rad-grading $=$ squarefree divisibility lattice.** Up to the rad-grading,
$\mathbf{Deriv}^{\mathrm{res}}_{\mathrm{rad}}\cong(\mathcal P_{\mathrm{fin}}(\mathbb P),
\subseteq)$, finite prime-sets under inclusion, with meet $=\gcd$ of radicals and join
$=\mathrm{lcm}$. The pinned arrows are the localization inclusions $\iota_{m,m'}$.

**Sole-obstruction naturality (Thm 60b).** $\Theta:\mathrm{Ros}_{(-)}\Rightarrow
\varprojlim^1(-)$ is a natural isomorphism on this lattice: wherever an arrow exists the
Čech-cochain square commutes (snake-lemma naturality of $\delta=\mathrm{id}-m\cdot
\mathrm{sh}$, Prop 58c), and rad-divisibility is the *unique* obstruction — off it the
hom-set is empty (naturality vacuous), never a square that fails. **Phantom presheaf:**
$S\mapsto(\prod_{p\in S}\mathbb Z_p)/\mathbb Z$ on $\mathrm{Spec}$; $\Theta$ identifies it
with the Rosser-torsor presheaf.

**Incomparable pathology (Cor 60c).** $m=6,m'=10$ are rad-incomparable; no arrow either
way, only a common lower bound $C_2$ (the shared $2$-adic ghost $\mathbb Z_2/\mathbb Z$).

**$\aleph_1$-phantom (Thm 60d).** Gray's $0$-or-$2^{\aleph_0}$ dichotomy is strictly an
$\omega$-cofinality phenomenon. An $\omega_1$-cofinal long cover makes the cover-fiber
system pro-isomorphic to the Mardešić–Prasolov strong-homology system, whose
$\varprojlim^1$ is **nonzero under CH** (Mardešić–Prasolov 1988) and **zero under PFA**
(Dow–Simon–Vaughan 1989); hence "a genuinely $\aleph_1$-engendered intermediate phantom
exists" is **independent of ZFC** — a model-dependent ghost, present under CH, exorcised
by $\mathrm{MA}_{\aleph_1}$. *No partial phantom at $\omega$; a whole undecidable phantom
at $\omega_1$.*

## Phantom presheaf, stalkwise sheafification, Rosser $=$ descent obstruction (Pass 61)

**Phantom presheaf $P$ and its resolution.** $P(S)=(\prod_{p\in S}\mathbb Z_p)/\mathbb Z$
on the prime lattice $(\mathcal P_{\mathrm{fin}}(\mathbb P),\subseteq)$ (prime-cover
topology; **restriction $=$ coordinate projection**), resolved by the presheaf SES
$0\to\underline{\mathbb Z}\xrightarrow{\Delta}\mathcal F\xrightarrow{\pi}P\to0$ with
$\mathcal F(S)=\prod_{p\in S}\mathbb Z_p$ a **flasque sheaf** and $\underline{\mathbb Z}$
the constant presheaf.

**Stalkwise sheafification $L$ (Thm 61a).** $P$ **fails descent**: $P(S)\to\prod_pP(\{p\})$
is onto with kernel $\mathbb Z^{|S|-1}\ne0$ (the separation defect $\mathbb Z^{S}/\Delta
\mathbb Z$, $\underline{\mathbb Z}$ being non-separated with sheafification $\mathbb Z^{S}$).
The sheafification is the stalkwise sheaf $P^{\#}=L$, $L(S)=\prod_{p\in S}(\mathbb Z_p/
\mathbb Z)$, stalk $\mathbb Z_p/\mathbb Z$ at $p$; the unit $P\twoheadrightarrow L$ has
kernel $\mathbb Z^{|S|-1}$.

**Rosser $=$ obstruction to descent (Thm 61b, correction of the Pass-60 slogan).** The
Rosser torsor $\widehat{\mathbb Z}_m/\mathbb Z=P(S)$ is **not** the sheafification $L$;
sheafification *discards* it. Dictionary split along $P\twoheadrightarrow L$: **Löb $=$
sheaf** $L$ (stalk-local, "consistency is local at each prime"); **Rosser $=$ failure of
descent** $\ker(P\to L)$, with a horizontal free part $\mathbb Z^{|S|-1}=\check H^1(
\underline{\mathbb Z})$ (prime cover) and a vertical $\varprojlim^1=\widehat{\mathbb Z}_p/
\mathbb Z$ (dilation tower) per stalk. The Pass-60 slogan holds only **dualized**: $P$ is a
flabby **cosheaf**, Löb $=$ sheaf, Rosser $=$ cosheaf.

## Löb–Rosser bicomplex, mixed class $\epsilon_S$, cosheafification collapse (Pass 62)

**The bicomplex (Thm 62a).** The total phantom $P(S)=\widehat{\mathbb Z}_S/\mathbb Z$
($S=\mathrm{rad}(m)$, $s=|S|$) is $H^1$ of the double complex $D^{\bullet,\bullet}$ with
**vertical** differential the per-prime Milnor $\varprojlim$-cochain $[\prod_n\mathbb Z
\xrightarrow{1-p\,\mathrm{sh}}\prod_n\mathbb Z]$ of the dilation tower $(\mathbb Z,\times p)$
($H^0=0$, $H^1=\mathbb Z_p/\mathbb Z$) and **horizontal** differential the augmented reduced
Čech cochain of $\underline{\mathbb Z}$ over the singleton prime cover ($\operatorname{coker}
\Delta=\mathbb Z^{s-1}$). Both spectral sequences degenerate at $E_2$ to the two cells
$E_2^{1,0}=\mathbb Z^{s-1}$ (**Rosser/horizontal**) and $E_2^{0,1}=\prod_{p\in S}(\mathbb Z_p/
\mathbb Z)=L(S)$ (**Löb/vertical**); $E_2^{2,0}=E_2^{0,2}=0$. The Löb/Rosser dictionary **is**
the $E_2$ page.

**Mixed class $\epsilon_S$ (Thm 62b).** With survivors only at the complementary cells $(1,0)$,
$(0,1)$ and zero neighbours, $d_r=0$ for $r\ge2$ ($E_2=E_\infty$); the "mixing" is the
filtration extension
$$0\to\mathbb Z^{s-1}\xrightarrow{\iota}\widehat{\mathbb Z}_S/\mathbb Z\xrightarrow{\rho}
\textstyle\prod_{p\in S}(\mathbb Z_p/\mathbb Z)\to0,$$
**non-split** for $s\ge2$ — a retraction would restrict to $\mathrm{Hom}(\mathbb Z_p,\mathbb Z)
=0$ on each stalk and annihilate the integer points $e_p$ generating $\mathbb Z^S/\Delta\mathbb
Z$. The **mixed Löb–Rosser class** $\epsilon_S\in\mathrm{Ext}^1_{\mathbb Z}(L(S),\mathbb Z^{s-1})
\setminus\{0\}$ is the connecting $\partial$ of the filtration (no pure-horizontal/pure-vertical
representative), **not** a page $d_2$; a genuine $d_2:E_2^{0,1}\to E_2^{2,0}$ appears only after
**unabridging** each $\mathbb Z_p$ into its $\mathbb Z/p^n$-tower. Pathology $S=\{2,3\}$:
$(\mathbb Z_2\times\mathbb Z_3)/\Delta\mathbb Z$, the horizontal generator $[(1,0)]=[(0,-1)]$ has
no direct complement (a purely horizontal relation welded to the local ghosts).

**Cosheafification collapse (Thm 62c, correction of the Pass-61 slogan).** On the singleton
(discrete) prime site the cosheafification is the costalk coproduct $\check P(S)=\bigoplus_{p\in
S}(\mathbb Z_p/\mathbb Z)$, and for finite $S$ the comparison $\bigoplus\to\prod$ is an iso, so
$\check P(S)=\prod_{p\in S}(\mathbb Z_p/\mathbb Z)=L(S)=P^{\#}(S)$: **sheafification $=$
cosheafification $=L$**. The global $\widehat{\mathbb Z}_S/\mathbb Z$ is **neither** — irreducibly
presheaf-level, the descent defect $\mathbb Z^{s-1}$. "Rosser $=$ cosheaf" is **false on the
discrete site** (too disconnected for $\mathbf{Sh}\ne\mathbf{coSh}$); a nonzero $\check H^1$ needs
the coarser **Zariski/cofinite** topology on $\mathrm{Spec}\,\mathbb Z$. Corrected dictionary:
**Löb $=$ common (co)sheafification $L$; Rosser $=$ descent defect $\mathbb Z^{s-1}=\ker(P\to L)$**,
glued to the local ghosts by the non-split seam $\epsilon_S$.

**$\mathfrak b$-wall (Thm 61c).** For the $\omega_1$-cofinal long cover: $\mathfrak b=
\aleph_1\Rightarrow\varprojlim^1\mathbf A_{\omega_1}\ne0$ (weaker than CH);
$\mathrm{MA}_{\aleph_1}\Rightarrow0$ (forces $\mathfrak b=\aleph_2$). Threshold is
**bracketed, not a single named cardinal characteristic**; an $\aleph_2$-cofinal cover
gives a *sequence* of higher-$\varprojlim^s$ ($s\ge2$) independence statements, not a
$0/\aleph_1/2^{\aleph_0}$ trichotomy.

## Zariski $j_!$-cosheaf, unabridged $d_2$, and the $\mathrm{Ext}^1$ ghost line (Pass 63)

**Zariski generic-point site.** The finite connected space $X=\{\eta\}\cup\{(p):p\in S\}$
($S=\mathrm{rad}(m)$, $s=|S|$) with the subspace (particular-point) Zariski topology — opens
$=\varnothing$ and every set containing the generic point $\eta$. The cover $\mathcal U=\{U_p=
\{\eta,(p)\}\}$ has **all** nonempty overlaps $=\{\eta\}$, so its nerve is the **full simplex**
$\Delta^{s-1}$ (contractible) — opposite to the discrete singleton cover ($s$ disjoint vertices).

**Zariski relocation / $j_!$-cosheaf Rosser class (Thm 63a).** On the connected site the constant
sheaf $\underline{\mathbb Z}$ is a genuine sheaf with $\check H^{\ge1}=0$, so the discrete-site
horizontal defect $\mathbb Z^{s-1}=\check H^0_{\mathrm{red}}$ **vanishes** (connectivity kills
constant-coefficient $H^1$). The Rosser relations **relocate up one degree** to the
extension-by-zero from the open generic point $j:\{\eta\}\hookrightarrow X$:
$$H^1(X,\ j_!\underline{\mathbb Z})=\mathbb Z^s/\Delta\mathbb Z=\mathbb Z^{\,s-1}\ne0,$$
via $0\to j_!\mathbb Z\to\mathbb Z_X\to i_*\mathbb Z_Z\to0$ ($i:Z\hookrightarrow X$ the closed
$s$-point complement). Since $j_!$ is the left-adjoint (compact-support/**cosheaf**) extension,
"Rosser $=$ cosheaf" finally holds, in the precise form **Rosser $=H^1$ of $j_!$ supported at the
generic point**; Löb $=$ the stalkwise sheaf $L(S)$. (The naive cover-cosheafification still
returns $L(S)$ — overlaps carry the skyscraper $0$ — so the rescuing functor is specifically
$j_!$, not $\check{(-)}$ over $\mathcal U$.)

**Unabridged $d_2$ (Thm 63b).** Resolving each $\mathbb Z_p=\varprojlim_n\mathbb Z/p^n$ by its
$\mathbb Z/p^n$-tower opens a third bicomplex column $E_2^{2,0}=\operatorname{coker}(\Delta:
\mathbb Z\to\mathbb Z^s)=\mathbb Z^{s-1}$, turning the Pass-62 hidden $E_\infty$ extension into a
genuine page differential $d_2:E_2^{0,1}=L(S)\to E_2^{2,0}=\mathbb Z^{s-1}$, $(x_p)\mapsto
[(x_p-x_{p_0})_{p\ne p_0}]$ — the **common-integer-lift obstruction** (image rank $s-1$). The
class $\epsilon_S=\partial$ and the $d_2$ are *one datum in two resolutions* (a two-column
$E_\infty$ extension becomes a $d_2$ upon manufacturing a third column).

**Ext$^1$ ghost line; arithmetic vs cardinal (Thm 63c).** $\mathrm{Hom}(\mathbb Z_p,\mathbb Z)=0$
makes $\delta:\mathbb Z\hookrightarrow\mathrm{Ext}^1(\mathbb Z_p/\mathbb Z,\mathbb Z)$ injective;
$\delta(1)=\epsilon_p$ is the **ghost class**, of **infinite order** (lacunary witness $u=\sum_k
p^{k!}$), generating a canonical $\mathbb Z$-line inside the uncountable $\mathrm{Ext}^1(\mathbb Z_p/
\mathbb Z,\mathbb Z)$ (an extension of the continuum-dimensional $\mathrm{Ext}^1(\mathbb Z_p,\mathbb
Z)$ by $\mathbb Z$). $\epsilon_S\in\bigoplus_{p\in S}\mathrm{Ext}^1(\mathbb Z_p/\mathbb Z,\mathbb
Z)^{s-1}$ is nonzero of infinite order for $s\ge2$. **Cardinal vs arithmetic:** the *target* rank
$s-1$ depends only on $|S|$ (cardinal), but $\epsilon_S$ lives on the pairwise **non-isomorphic**
ghost groups $\mathbb Z_p/\mathbb Z$ (torsion subgroup $\bigoplus_{q\ne p}\mathbb Z(q^\infty)$,
uniquely *omitting* the $p$-Prüfer), so it is a genuinely **arithmetic** invariant of the prime
set: $\epsilon_{\{2,3\}}\ne\epsilon_{\{2,5\}}$. *Slogan: the phantom remembers which primes, not
just how many.*

## Löb–Rosser recollement, dilation coefficient, $i^*=$ Löb / $j_!=$ Rosser, the prime-spectrum motive (Pass 64)

**The two-stratum space and its six functors.** $X=X_S=\{\eta\}\sqcup Z$, $Z=\{(p):p\in S\}$ the
closed discrete $s$-point stratum, $j:U=\{\eta\}\hookrightarrow X$ the **open** generic point,
$i:Z\hookrightarrow X$ the **closed** complement. On this finite (Alexandrov) space the six
operations exist with $j^*=j^!$ (open immersion) and $i_*=i_!$ (closed immersion), and form a
**recollement** (Thm 64a, BBD §1.4):
$$D(Z)\ \underset{i_*=i_!}{\hookrightarrow}\ D(X)\ \underset{j^*=j^!}{\twoheadrightarrow}\ D(U),\qquad
j_!\dashv j^*\dashv j_*,\quad i^*\dashv i_*\dashv i^!,$$
with $j^*i_*=0$; $i_*,j_!,j_*$ fully faithful; gluing triangles $j_!j^*\to\mathrm{id}\to i_*i^*
\xrightarrow{+1}$ and $i_*i^!\to\mathrm{id}\to Rj_*j^*\xrightarrow{+1}$.

**Dilation coefficient $\mathcal V$.** The pro-sheaf on $X$ with generic value $j^*\mathcal V=
\underline{\mathbb Z}$ and closed costalk at $(p)$ the Milnor pro-system of the dilation tower
$(\mathbb Z,\times p)$: $i^*\mathcal V$ has $R\varprojlim$ with $H^0=\varprojlim=0$ (the **detached**
limit fixed point) and $H^1=\varprojlim^1=\mathbb Z_p/\mathbb Z$. The single‑sheaf truncation gives
only one dilation step; the full $p$-adic ghost is the derived limit, so $\mathcal V$ is honestly a
tower and $H^1(X,j_!\mathcal V)$ is the continuous/derived $H^1$.

**Phantom $=H^1(j_!\mathcal V)$ (Thm 64b).** Because $j^*j_!=\mathrm{id}$ and $i^*j_!=0$, the
open/closed triangle on $j_!\mathcal V$ collapses to the short exact sequence
$$0\to\underbrace{\mathbb Z^{s-1}}_{H^1(j_!\underline{\mathbb Z}),\ \text{Rosser}}\to
\underbrace{H^1(X,j_!\mathcal V)}_{=\ \widehat{\mathbb Z}_S/\mathbb Z}\to
\underbrace{\textstyle\prod_p(\mathbb Z_p/\mathbb Z)}_{i^*\!\text{-stalk }\varprojlim^1,\ \text{Löb}}
\xrightarrow{\partial}0,$$
whose boundary $\partial:(x_p)\mapsto[(x_p-x_{p_0})]$ (image rank $s-1$, kernel the diagonal
$\mathbb Z$) is **identically** the Pass-63 $d_2$ and the Pass-62 $\epsilon_S$. Thus the **total
phantom is a single $j_!$-cohomology**, and the three avatars (filtration $\partial$, page $d_2$,
recollement boundary) are one morphism in three guises.

**The dictionary as six functors.** **Löb $=i^*$** — the closed-stalk sheaf part, the genuine local
ghosts $\mathbb Z_p/\mathbb Z$ that descend; **Rosser $=j_!$** — the generic-point, compact-support
part, the horizontal relations $\mathbb Z^{s-1}$ that survive only with proper support toward
$\eta$; **mixing $=\partial$** — the recollement boundary gluing $j_!j^*$ to $i_*i^*$, the
irreducible obstruction to splitting "pure Löb $\oplus$ pure Rosser."

**Prime-spectrum motive $M$ (Thm 64c).** $S\subseteq S'\Rightarrow X_S$ is **open** in $X_{S'}$
(complement is closed points), giving an open immersion and a restriction on the recollement data;
$M:S\mapsto j_!\mathcal V_S$ is a functor $(\mathcal P_{\mathrm{fin}}(\mathbb P),\subseteq)\to
D^b(\mathbb Z)$, weight-filtered ($W_0=$ Löb stalks, $\mathrm{gr}^W_1=$ Rosser horizontal), with
$\epsilon$ a natural transformation. $M$ is genuinely **arithmetic** (Thm 63c): not a function of
the cardinal $s$. The name "motive" is a deliberate analogy — $M$ is an honest constructible-sheaf
/ $D^b(\mathbb Z)$ gluing datum on the arithmetic base, *not* a Voevodsky motive — marking the
structural niche (functor on a geometric base, graded by the dictionary's two columns).

**Pathologies.** *(i) $s=1$ — pure Löb:* $H^1(j_!\underline{\mathbb Z})=\mathbb Z^0=0$, the
horizontal stratum is empty, the phantom is the bare $\mathbb Z_p/\mathbb Z$; **Rosser relations
need $\ge2$ primes** (they are relational). *(ii) Incomparable strata:* $\{2,3\}$ and $\{2,5\}$
(rad-incomparable, Cor 60c) — neither $X_S$ open in the other, only common open sub-stratum
$X_{\{2\}}$ (shared $2$-adic ghost), $\epsilon_{\{2,3\}}\ne\epsilon_{\{2,5\}}$. *(iii) The adelic
punchline:* $S=\mathbb P$ (all primes) makes $X=\mathrm{Spec}\,\mathbb Z$ and
$$H^1(\mathrm{Spec}\,\mathbb Z,\ j_!\mathcal V)=\widehat{\mathbb Z}/\mathbb Z=\Big(\textstyle\prod_p
\mathbb Z_p\Big)\big/\mathbb Z=\mathbb A_{\mathbb Q,\mathrm{fin}}^{\mathrm{int}}/\mathbb Z,$$
the **integral finite-adele class group**. *Smullyan gloss: the ghost haunting every consistency
statement at once is precisely an adele that is not an integer.*

## Verdier-dual recollement, $i^!$ Rosser lattice, and signed functional equation (Pass 65)

Let $X_S=\{\eta\}\sqcup\{(p):p\in S\}$, with $j:\{\eta\}\hookrightarrow X_S$ open and
$i:Z\hookrightarrow X_S$ closed. The **Verdier-dual recollement presentation** is the second
open/closed gluing triangle
$$i_*i^!F\to F\to Rj_*j^*F\xrightarrow{+1},$$
dual to the Pass-64 triangle $j_!j^*F\to F\to i_*i^*F\xrightarrow{+1}$.

The **$i^!$ Rosser lattice** is the local-support complex
$$\mathbb Z\xrightarrow{\Delta}\mathbb Z^S,\qquad 1\mapsto(1,\ldots,1),$$
with
$$H^0(i^!)=0,\qquad H^1(i^!)=\operatorname{coker}\Delta\cong\mathbb Z^{|S|-1}.$$
It is the closed-support counterpart of the Pass-63 presentation
$H^1(X_S,j_!\underline{\mathbb Z})\cong\mathbb Z^{|S|-1}$.

The **signed functional equation** is the finite-model duality rule for the mixed class
$\epsilon_S$. If
$$d_S:\mathbb Z^S\to\mathbb Z^{|S|-1},\qquad
(x_p)\mapsto(x_p-x_{p_0})_{p\ne p_0}$$
represents the recollement boundary, then Verdier duality sends
$$d_S\longmapsto -d_S^T,$$
so
$$\mathbb D(\epsilon_S)=-\epsilon_S^\vee.$$
Duality squared returns $d_S$. The sign is invisible over $\mathbb F_2$ but remains visible over
$\mathbb Z$ as an orientation datum of the gluing triangle. This statement is presently proved only
for the finite Alexandrov model; the honest $\mathrm{Spec}\,\mathbb Z$ site lift requires a separate
dualizing-normalization proof.

## Character-normalized duality and restricted-product gap (Pass 66)

The **character-normalized dual** of a discrete abelian group $A$ is
$$D_{\mathrm{ch}}(A)=\operatorname{Hom}(A,\mathbb Q/\mathbb Z).$$
For finite cyclic groups it preserves the layer:
$$D_{\mathrm{ch}}(\mathbb Z/n)\cong\mathbb Z/n.$$
This is the finite-level duality compatible with the Pass-65 signed boundary equation
$D_{\mathrm{ch}}(\epsilon_S)=-\epsilon_S^\vee$ for finite prime sets $S$.

The **plain $\mathbb Z$-linear dual shift** is the failure of
$\operatorname{Hom}_{\mathbb Z}(-,\mathbb Z)$ to see finite torsion in degree $0$:
$$\operatorname{Hom}_{\mathbb Z}(\mathbb Z/n,\mathbb Z)=0,\qquad
\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z)\cong\mathbb Z/n.$$
Thus $R\mathrm{Hom}_{\mathbb Z}(-,\mathbb Z)$ sees the dilation layers only after a cohomological
shift; it is not the literal degree-preserving duality of the finite Loeb-Rosser matrix spine.

The **all-prime product/direct-sum gap** is the obstruction to passing from finite $S$ to
$S=\mathbb P$ by bare products. Continuous characters of an infinite product have finite support,
so the dual of $\prod_p A_p$ is naturally $\bigoplus_p D(A_p)$, not another product. Consequently
the full adelic Loeb-Rosser duality must be formulated using restricted products / locally compact
abelian sheaves, where finite adeles carry their own self-duality normalization.

## Tag order, witness-comparison Rosser box, and the $I\Sigma_n$-graded Rosser tower (Pass 137)

**Tag order $\prec_t$.** For an injective map $t\colon\omega\to\omega^{<\omega}$ (a *tag map*),
the **tag order** is $n\prec_t m :\iff t(n)<_{\mathrm{lex}}t(m)$. When $t$ is $\Sigma_1$-definable
with $O(1)$ per-comparison encoding ($m_{\mathrm{enc}}=O(1)$) but non-primitive-recursive, the
relation $\prec_t$ is a $\Sigma_1$, non-p.r. linear order (Prop 136d).

**Witness-comparison Rosser box $\Box_R^{\prec}$.** For a linear order $\prec$ on proof-codes with
a $\prec$-least element, $\Box_R^{\prec}\psi := \exists p\,(\mathrm{Prf}(p,\psi)\wedge(\forall
q\prec p)\,\neg\mathrm{Prf}(q,\neg\psi))$. The order $\prec$ is the Guaspari--Solovay
witness-comparison ordering; the standard Rosser box takes $\prec\;=\;<$ (the p.r. order on codes).

**$I\Sigma_1$-linearity primitivity (Thm 137a) / vacuity (Cor 137b).** A $\Sigma_1$ order whose
linearity (trichotomy $+$ asymmetry) is provable in $I\Sigma_1$ has **primitive-recursive**
comparison (provable trichotomy makes $\neg\varphi$ provably $\Sigma_1$, so $\chi_\varphi$ is
$I\Sigma_1$-provably total recursive $=$ p.r. by Parsons--Mints--Takeuti). Hence **no** $\Sigma_1$
non-p.r. order is $I\Sigma_1$-provably linear; the linearity of $\prec_t$ is a true $\Pi_2$
sentence of $\mathbb N$ that $I\Sigma_1$ cannot prove.

**Order-robust derivability profile (Thm 137c).** For **any** linear $\prec$ with a $\prec$-least
element, $\neg D2\wedge\neg\Box_R^{\prec}\bot$ hold in $\mathbb N$ — the Guaspari--Solovay Rosser
mechanism uses only linearity, a least element, and the Rosser fixed point, **never**
primitive-recursiveness of $\prec$. So the modal profile $D1\wedge\neg D2\wedge\neg\Box_R\bot$ is
*order-robust*; p.r.-ness controls only the arithmetic level that certifies it.

**$I\Sigma_n$-graded Rosser tower (Thm 137d).** If the tag map is provably total exactly in
$I\Sigma_k\setminus I\Sigma_{k-1}$, then $I\Sigma_k\vdash\mathrm{Lin}(\prec_t)\Rightarrow(\neg
D2\wedge\mathrm{Con}_R)$ for $\Box_R^{\prec_t}$ while $I\Sigma_{k-1}$ proves neither — a strictly
increasing certification hierarchy, all levels sharing the same standard-model modal profile.
The **Ackermann-scrambled order** $\prec_A$ ($t(n)=\langle A(n),n\rangle$, $A$ Ackermann) is the
pathological witness: $I\Sigma_2$-provably linear, not $I\Sigma_1$-provably linear, comparison
total-recursive but non-p.r. *Slogan: finitely uncertified, standardly Rosser* — the
ordinal-graded echo of Pass 55's "finitely Löb, limanly Rosser." See
[[aps-run-sync-hazard]]; `code/scripts/check-pass137.py`.

## Finite conductor window, self-annihilating lattice, and CRT collapse (Pass 67)

For a prime $p$ and conductor $k\ge1$, the **finite conductor window** is
$$W_{p,k}=p^{-k}\mathbb Z_p/p^k\mathbb Z_p\cong\mathbb Z/p^{2k}\mathbb Z,$$
equipped with the pairing
$$\langle x,y\rangle=\frac{xy}{p^{2k}}\in\mathbb Q/\mathbb Z.$$
It is the finite quotient that models the local self-duality of the restricted product
$\prod'_p(\mathbb Q_p,\mathbb Z_p)$.

The **self-annihilating integral lattice** inside $W_{p,k}$ is
$$\mathbb Z_p/p^k\mathbb Z_p\cong p^k\mathbb Z/p^{2k}\mathbb Z.$$
Its annihilator under the conductor pairing is itself. Finite products of such windows retain this
self-annihilating lattice property.

The **CRT collapse** is the finite-level fact that for
$N=\prod_{p\mid N}p^{e_p}$, the diagonal map
$$\mathbb Z/N\mathbb Z\to\prod_{p\mid N}\mathbb Z/p^{e_p}\mathbb Z$$
is an isomorphism. Thus the quotient by the diagonal is zero at each fixed finite conductor. The
phantom $\widehat{\mathbb Z}/\mathbb Z$ cannot be recovered from any single finite level; it is a
derived/pro quotient phenomenon of the limiting system.

## Derived pro-cokernel of the diagonal (Pass 68)

Let $N_n=\operatorname{lcm}(1,\ldots,n)$.  The **kernel tower** of the diagonal finite quotient is
$$K_n=N_n\mathbb Z\subset\mathbb Z,$$
with transition $K_{n+1}\hookrightarrow K_n$.  The levelwise exact sequence
$$0\to K_n\to\mathbb Z\to\mathbb Z/N_n\mathbb Z\to0$$
has zero ordinary cokernel at each finite stage, because $\mathbb Z\to\mathbb Z/N_n\mathbb Z$ is
surjective and CRT identifies $\mathbb Z/N_n\mathbb Z$ with its prime-power product.

The **derived pro-cokernel** is the failure of $\varprojlim$ to preserve this levelwise
surjectivity:
$$0\to\mathbb Z\to\widehat{\mathbb Z}\to\varprojlim\nolimits^1 K_n\to0,$$
so
$$\varprojlim\nolimits^1(N_n\mathbb Z)\cong\widehat{\mathbb Z}/\mathbb Z.$$
The kernel tower is non-Mittag-Leffler: after identifying $K_n\cong\mathbb Z$, the transition
indices $N_{n+1}/N_n$ are nontrivial infinitely often and the image indices grow without bound.

The **levelwise-zero / derived-nonzero distinction** is the core all-prime phantom mechanism:
finite CRT quotients see no quotient, but the derived inverse-limit sequence records the nonzero
Loeb-Rosser class.

## Derived pro-cokernel filtration and $\epsilon_S$ (Pass 70)

For a finite prime set $S$, put
$$M_{S,k}:=\prod_{p\in S}p^k.$$
The finite-prime derived pro-cokernel is
$$\varprojlim\nolimits^1(M_{S,k}\mathbb Z)\cong\widehat{\mathbb Z}_S/\mathbb Z,$$
where
$$\widehat{\mathbb Z}_S=\prod_{p\in S}\mathbb Z_p.$$

The comparison to local derived cokernels is the projection
$$\widehat{\mathbb Z}_S/\mathbb Z\longrightarrow
\prod_{p\in S}(\mathbb Z_p/\mathbb Z).$$
Its kernel is
$$\mathbb Z^S/\Delta\mathbb Z\cong\mathbb Z^{|S|-1},$$
where $\Delta(1)=(1,\ldots,1)$.  Thus the recollement class
$$\epsilon_S:\quad
0\to\mathbb Z^S/\Delta\mathbb Z\to
\widehat{\mathbb Z}_S/\mathbb Z\to
\prod_{p\in S}(\mathbb Z_p/\mathbb Z)\to0$$
is the finite-prime filtration of the derived pro-cokernel by local derived
cokernels.

With a chosen base prime $p_0\in S$, the boundary matrix is
$$d_S:\mathbb Z^S\to\mathbb Z^{|S|-1},\qquad
(x_p)\mapsto (x_p-x_{p_0})_{p\ne p_0}.$$
Its kernel is the diagonal $\Delta\mathbb Z$ and it is surjective.  Under the
finite character-normalized duality convention, the dual boundary is represented
by $-d_S^T$, so finite shadows satisfy
$$D_{\mathrm{ch}}(\epsilon_S)=-\epsilon_S^\vee.$$

## Restricted-product epsilon duality package (Pass 71)

A **support-preserving restricted-product duality** for the all-prime
Loeb-Rosser class is a duality formalism which remembers conductor and lattice
data.  Locally it uses self-dual pairs $(A_p,L_p)$, with $L_p$ an integral
lattice, and globally it uses restricted products
$$\prod_p'(A_p,L_p)$$
rather than the bare product $\prod_p A_p$.  This condition is necessary
because ordinary continuous characters of an infinite product have finite
support, so bare product duality collapses the all-prime product information to
a direct-sum shadow.

The **all-prime epsilon object** is the compatible family
$$\epsilon_{\mathbb P}:=\{\epsilon_S\}_{S\subset\mathbb P,\ |S|<\infty}$$
together with the derived pro-cokernel
$$\varprojlim\nolimits^1(N_n\mathbb Z)\cong\widehat{\mathbb Z}/\mathbb Z.$$
Here each finite shadow is the Pass-70 extension
$$0\to\mathbb Z^S/\Delta\mathbb Z\to
\widehat{\mathbb Z}_S/\mathbb Z\to
\prod_{p\in S}(\mathbb Z_p/\mathbb Z)\to0.$$
The topology is not carried by the non-Hausdorff quotient
$\widehat{\mathbb Z}/\mathbb Z$ alone; it is carried by the finite-conductor
restricted-product presentation plus the derived pro-Ab quotient.

The **pro-restricted signed law** is the finite-shadow statement
$$D_{\mathrm{res}}(\epsilon_{\mathbb P})=-\epsilon_{\mathbb P}^{\vee}$$
meaning: for every finite prime set $S$, every finite conductor window, and
every restriction $S\subset S'$, the boundary
$$d_S(x)=(x_p-x_{p_0})_{p\ne p_0}$$
dualizes to $-d_S^T$, duality squared returns $d_S$, and the restriction
squares commute.  This is presently a precise finite-shadow/pro-object
formulation, not yet a full theorem in a chosen LCA-sheaf, condensed, or solid
category.

## Hybrid epsilon exact-category candidate (Pass 72)

The **hybrid epsilon category candidate** $\mathcal H_\epsilon$ is the minimal
bookkeeping category proposed for the all-prime Loeb-Rosser class.  An object
has two synchronized layers:

1. finite restricted-product shadows $(S,k,W_{S,k},L_{S,k},d_S)$, where
   $S$ is a finite prime set, $k\ge1$,
   $$W_{S,k}=\prod_{p\in S}(p^{-k}\mathbb Z_p/p^k\mathbb Z_p),\qquad
   L_{S,k}=\prod_{p\in S}(\mathbb Z_p/p^k\mathbb Z_p),$$
   and $d_S:\mathbb Z^S\to\mathbb Z^{|S|-1}$ is the Loeb-Rosser boundary;
2. a derived pro-Ab diagonal layer given by the lcm kernel tower
   $$K_n=N_n\mathbb Z,\qquad N_n=\operatorname{lcm}(1,\ldots,n).$$

A sequence in $\mathcal H_\epsilon$ is **hybrid-exact** when every finite
restricted-product shadow is exact and the pro layer supplies the derived
diagonal quotient
$$\varprojlim\nolimits^1 K_n\cong\widehat{\mathbb Z}/\mathbb Z.$$
Equivalently, the finite CRT quotient is levelwise zero, while the non-ML
kernel tower records the all-prime phantom.

The candidate duality $\mathbb D_{\mathcal H}$ is the signed finite-shadow
duality
$$d_S\mapsto -d_S^T$$
together with the rule that $\widehat{\mathbb Z}/\mathbb Z$ remains a derived
pro-Ab quotient rather than an ordinary Hausdorff LCA quotient.  Pass 72 checks
finite exactness, restriction functoriality, conductor bookkeeping, and the
non-ML pro witness; the remaining task is to prove a universal property or
embed $\mathcal H_\epsilon$ fully into an established LCA-sheaf,
condensed/solid, or exact pro-category framework.

## Presentation-level universal property of $\mathcal H_\epsilon$ (Pass 73)

A **support-preserving certificate target** for $\epsilon_{\mathbb P}$ is a
category-like target equipped with images of five generator families:

1. finite conductor windows $W_{S,k}$ and lattices $L_{S,k}$;
2. Loeb-Rosser boundaries $d_S$;
3. restriction morphisms for $S\subset S'$;
4. signed duality morphisms $d_S\mapsto -d_S^T$;
5. the derived pro-Ab lcm tower $K_n=N_n\mathbb Z$.

The target is **admissible** when these images satisfy the finite exactness,
restriction, signed-dual, conductor, and non-Mittag-Leffler pro relations
checked in Pass 72.

The **presentation-level universal property** says that
$\mathcal H_\epsilon$ is initial among admissible support-preserving certificate
targets: any admissible target receives a unique generator-preserving functor
from $\mathcal H_\epsilon$.  This is a universal property of the presented
bookkeeping category.  It is not yet a proof that $\mathcal H_\epsilon$ embeds
fully faithfully into LCA sheaves, condensed/solid abelian groups, or a
canonical exact pro-category.

The **minimality obstruction** is that omitting any generator family destroys
one part of $\epsilon_{\mathbb P}$: without conductor windows there is no
support-preserving local duality; without $d_S$ there is no $\epsilon_S$;
without restrictions the finite shadows do not assemble; without signed
duality the functional equation is untyped; without the lcm tower finite CRT
levels remain zero and $\widehat{\mathbb Z}/\mathbb Z$ is lost.

## Tagged restricted pro-Ab realization (Pass 74)

The **tagged restricted pro-Ab realization target**
$$\mathcal R_\epsilon:=\mathbf{Pro}^{\mathrm{rp}}_{\mathrm{tag}}(\mathbf{Ab}_{\mathrm{fin}})
\times\mathbf{Pro}_{\mathrm{tag}}(\mathbf{Ab})$$
is a concrete certificate category for $\mathcal H_\epsilon$.  It realizes the
five generator families as tagged finite/pro abelian data:

1. $(S,k,W_{S,k},L_{S,k})$ is sent to the finite abelian group presentation
   with support tag $S$, conductor tag $k$, elementary divisors
   $(p,2k)_{p\in S}$, and lattice divisors $(p,k)_{p\in S}$;
2. $d_S$ is sent to its integer boundary matrix together with source and
   target support tags;
3. each restriction $S\subseteq S'$ is sent to the corresponding tagged
   coordinate-restriction matrix;
4. signed duality is sent to the tagged matrix $-d_S^T$;
5. $K_n=N_n\mathbb Z$ is sent to the tagged pro-stage $(n,N_n)$.

The realization functor
$$\rho_{\mathrm{tag}}:\mathcal H_\epsilon\to\mathcal R_\epsilon$$
is **generator-faithful** when these tagged signatures distinguish all five
generator families.  Pass 74 verifies this on finite shadows through six primes,
conductors $k\le3$, and lcm stages through $N_{24}$.

The **tag-forgetting obstruction** is that the corresponding plain pro-Ab
target is not faithful on the same samples: source support for restrictions
and repeated lcm stages collide after the tags are forgotten.  Thus Pass 74
gives the first concrete faithful realization test, but the next task is to
justify the tags intrinsically inside an LCA-sheaf, condensed/solid, or
canonical exact pro-category framework.

## Projector-enriched restricted pro-Ab realization (Pass 75)

The **projector-enriched restricted pro-Ab realization** replaces the external
support and stage tags of Pass 74 by internal projectors.  It has:

1. commuting Boolean support idempotents $e_p$ for primes, with
   $$e_S=\prod_{p\in S}e_p,\qquad e_Se_T=e_{S\cap T};$$
2. stage projectors $q_n$ for the lcm tower, with
   $$q_nq_m=q_{\min(n,m)}.$$

The realization
$$\rho_{\mathrm{proj}}:\mathcal H_\epsilon\to\mathcal R_\epsilon^{\mathrm{proj}}$$
sends finite conductor windows, boundaries, restrictions, signed duals, and
lcm stages to the same finite/pro abelian data as $\rho_{\mathrm{tag}}$, but
source support and stage are now recovered from the action of $e_S$ and $q_n$.

Pass 75 verifies generator faithfulness after this replacement on the same
finite/pro window as Pass 74.  The plain target that forgets both projector
actions remains non-faithful, so the projectors are not optional.  The remaining
task is to realize these idempotents as natural support and stage structure in
an established LCA-sheaf, condensed/solid, or exact pro-category setting.

## Finite-prime stratified pro-site model $\mathrm{StratPro}_\epsilon(U,N)$ (Pass 76)

The **finite-prime stratified pro-site model** $\mathrm{StratPro}_\epsilon(U,N)$
is the first natural model for the Pass-75 projectors.  Over a finite prime
universe $U$ carried as a finite discrete (Stone) space, and an lcm truncation
depth $N$, it has:

1. **clopen support projectors**: $e_p$ is multiplication by the characteristic
   function $\mathbf 1_{\{p\}}$ of the clopen stratum $\{p\}\subseteq U$, so
   $e_S=(\cdot)\mathbf 1_S$ and $e_Se_T=e_{S\cap T}$ is pointwise idempotent
   multiplication $\mathbf 1_S\mathbf 1_T=\mathbf 1_{S\cap T}$;
2. **pro-stage truncation projectors**: $q_n$ is the prefix truncation of the
   non-Mittag-Leffler lcm tower $K_m=N_m\mathbb Z$ at stage $n$, with
   $q_nq_m=q_{\min(n,m)}$, cofinal so that $\varprojlim^1 K_m\cong
   \widehat{\mathbb Z}/\mathbb Z$ persists.

The **site realization** $\rho_{\mathrm{site}}:\mathcal H_\epsilon\to
\mathrm{StratPro}_\epsilon(U,N)$ factors the projector realization as
$\rho_{\mathrm{proj}}=(\text{forget site})\circ\rho_{\mathrm{site}}$ and is
**site-faithful** on the five generator families.  Pass 76 verifies this on
$U=\{2,3,5,7,11,13\}$, conductors $k\le3$, and lcm stages through $N_{24}$, with
the Boolean clopen relations and the prefix-truncation chain relations both
holding, while the plain tag-forgetting target stays non-faithful.  The model is
still finite-window and discrete; the remaining task is the all-prime derived
LCA-sheaf/condensed/solid exact upgrade carrying the signed duality law
$D_{\mathrm{res}}(\epsilon_{\mathbb P})=-\epsilon_{\mathbb P}^{\vee}$.

## All-prime derived realization: solid dual, degree-1 shift, LCA barrier (Pass 77)

The **solid dual** of a solid abelian group $A$ is
$$A^{*}:=R\underline{\mathrm{Hom}}_{\mathrm{Solid}}(A,\mathbb Z),$$
the derived internal hom in the category $\mathrm{Solid}_{\mathbb Z}$ of solid
abelian groups (Clausen-Scholze).  For a profinite layer it is **degree-shifted**:
$$R\underline{\mathrm{Hom}}(\mathbb Z_p,\mathbb Z)\cong(\mathbb Q_p/\mathbb Z_p)[-1],
\qquad
\widehat{\mathbb Z}^{\,*}\cong(\mathbb Q/\mathbb Z)[-1],$$
the second by the solid **product-to-sum identity**
$R\underline{\mathrm{Hom}}(\prod_p\mathbb Z_p,\mathbb Z)=\bigoplus_p
R\underline{\mathrm{Hom}}(\mathbb Z_p,\mathbb Z)$.  The first follows from the
levelwise resolution $\mathbb Z\xrightarrow{p^n}\mathbb Z\to\mathbb Z/p^n$, which
gives $\mathrm{Hom}(\mathbb Z/p^n,\mathbb Z)=0$,
$\mathrm{Ext}^1(\mathbb Z/p^n,\mathbb Z)=\mathbb Z/p^n$, and colimit
$\mathbb Q_p/\mathbb Z_p$ in degree $1$.

The **LCA dense-subgroup barrier** is the classical obstruction:
$\mathbb Z$ is dense in $\widehat{\mathbb Z}$, so $Q=\widehat{\mathbb Z}/\mathbb Z$
is non-Hausdorff and not an object of $\mathrm{LCA}$, and its Pontryagin dual
$$Q^{\vee}_{\mathrm{LCA}}=\operatorname{Ann}_{\widehat{\widehat{\mathbb Z}}}
(\mathbb Z)=\ker\big(\mathbb Q/\mathbb Z\hookrightarrow\mathbb T\big)=0$$
vanishes.  Hence the all-prime phantom $\epsilon_{\mathbb P}=
\widehat{\mathbb Z}/\mathbb Z=\varprojlim^1(N_n\mathbb Z)$ admits **no** nonzero
LCA realization, while in $D(\mathrm{Solid})$ it is nonzero and sits in
cohomological degree $1$.  The signed duality law
$D_{\mathrm{res}}(\epsilon_{\mathbb P})=-\epsilon_{\mathbb P}^{\vee}$ is therefore
a **degree-1 derived equation**: the antipode sign $-1$ of the finite shadows
$D(d_S)=-d_S^{T}$ (with $D^2=\mathrm{id}$) is carried to $\varprojlim^1$ through
the odd shift $[-1]$.  The all-prime support idempotents $e_S$, $S\in
\mathcal P(\mathbb P)$, are the clopen idempotents of the Stone space
$\beta\mathbb P$ (Stone dual of $\mathcal P(\mathbb P)$), with $e_Se_T=e_{S\cap T}$
for all subsets, extending the finite-window Boolean algebra of Pass 76.

## Solid biduality of the phantom: reflexivity up to the antipode (Pass 78)

The **solid dualizing functor** is $D(-)=R\underline{\mathrm{Hom}}(-,\mathbb Z)$ on
$D(\mathrm{Solid}_{\mathbb Z})$.  Writing $\epsilon=\epsilon_{\mathbb P}=
\widehat{\mathbb Z}/\mathbb Z=\varprojlim^1(N_n\mathbb Z)$, Pass 78 computes:

1. **Single dual.** $\operatorname{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Z)=0$ and
   $$D\epsilon\cong E[-1]\cong\mathbb Q[-1],$$
   where $E$ is the extension of $\mathbb Q/\mathbb Z$ by $\mathbb Z$ of class the
   **unit** $1\in\widehat{\mathbb Z}^\times=\operatorname{Ext}^1(\mathbb Q/\mathbb Z,
   \mathbb Z)$ (the connecting datum $\delta(1)$ of $0\to\mathbb Z\to\widehat{\mathbb
   Z}\to\epsilon\to0$); concretely $E\cong\mathbb Q$.  The dual of the phantom sits
   in cohomological degree $1$.
2. **Double dual / reflexivity.** Dualizing again, with $\mathbb Q/\mathbb Z=
   \operatorname{colim}_n\mathbb Z/n$ dualized termwise to $D(\mathbb Q/\mathbb Z)=
   \widehat{\mathbb Z}[-1]$, the connecting map is the dense inclusion
   $d:\mathbb Z\hookrightarrow\widehat{\mathbb Z}$ (multiplication by the unit class),
   so $\ker d=0$, $\operatorname{coker}d=\widehat{\mathbb Z}/\mathbb Z=\epsilon$, and
   $$\epsilon^{**}=R\underline{\mathrm{Hom}}(R\underline{\mathrm{Hom}}(\epsilon,
   \mathbb Z),\mathbb Z)\cong\epsilon.$$
   The phantom is **solidly reflexive**, with **no** $\varprojlim^1$-of-$\varprojlim^1$
   secondary phantom: such a term arises iff the connecting class is a non-unit
   (zero-divisor), e.g. the idempotent $e_2\in\widehat{\mathbb Z}$, whose cokernel
   $\widehat{\mathbb Z}/c\widehat{\mathbb Z}$ carries $\prod_{p\mid c}p^\infty$ torsion.
3. **Biduality sign (antipode).** The evaluation $\eta_\epsilon:\epsilon\to
   \epsilon^{**}$ is an isomorphism equal to $-\mathrm{id}_\epsilon$: finite shadows
   give $D^2(d_S)=d_S$ (sign $+1$), and the phantom's single odd shift $[-1]$
   contributes Koszul sign $(-1)^{1}=-1$.  Thus $\epsilon$ is a $[-1]$-shift
   self-dual solid object **up to the antipode** $-1$ (not its negation).
   *(Terminology corrected in Pass 79: item 3 records **reflexivity**
   $\epsilon^{**}\cong\epsilon$, NOT object-level self-duality $\epsilon\cong
   D\epsilon[1]$ -- the latter is false, since $D\epsilon[1]\cong\mathbb Q\not\cong
   \epsilon$.  See below.)*

## The phantom as a dual pair; the adele self-pairing; Darboux no-go (Pass 79)

**Dual pair $(\epsilon,\mathbb Q)$.** In $D(\mathrm{Solid}_{\mathbb Z})$,
$$D\epsilon\cong\mathbb Q[-1],\qquad D\mathbb Q\cong\epsilon[-1],$$
so $\epsilon$ and $\mathbb Q$ are Spanier-Whitehead duals up to the shift $[-1]$.
This is a **dual pair**, not self-duality: as bare abelian groups
$\epsilon\cong\mathbb A_f/\mathbb Q$ (strong approximation $\mathbb A_f=\mathbb Q+
\widehat{\mathbb Z}$, $\mathbb Q\cap\widehat{\mathbb Z}=\mathbb Z$) is a
$\mathbb Q$-vector space of dimension $2^{\aleph_0}$, while $\dim_{\mathbb Q}\mathbb Q=1$;
no shift makes $D\epsilon\cong\epsilon[s]$.  Reflexivity (Pass 78) holds for every
dualizable object and does not imply self-duality.

**Forced self-pairing degree.** For all $m\in\mathbb Z$,
$$\operatorname{Hom}_{D(\mathrm{Solid})}(\epsilon\otimes^{\blacksquare}\epsilon,
\mathbb Z[m])\cong\operatorname{Ext}^{m-1}_{\mathrm{Solid}}(\epsilon,\mathbb Q)
\cong\begin{cases}\mathbb Q,&m=2,\\0,&m\ne2,\end{cases}$$
computed solidly via $R\underline{\mathrm{Hom}}(\widehat{\mathbb Z},\mathbb Q)=
D\widehat{\mathbb Z}\otimes^{\blacksquare}\mathbb Q=(\mathbb Q/\mathbb Z)[-1]\otimes
\mathbb Q=0$.  The target $\mathbb Z[-1]$ admits only the zero pairing; the unique
nonzero self-pairing lives in $\mathbb Z[2]$.

**Adele self-pairing.** The generator of $\operatorname{Ext}^1_{\mathrm{Solid}}
(\epsilon,\mathbb Q)\cong\mathbb Q$ is the **finite-adele class extension**
$$b\ :\quad 0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0,$$
the pushout of $0\to\mathbb Z\to\widehat{\mathbb Z}\to\epsilon\to0$ along
$\mathbb Z\hookrightarrow\mathbb Q$.

**Type: alternating but degenerate.** $b$ is a degree-$1$ Yoneda class, hence
**alternating** ($\sigma^{*}b=-b$, the Pass-78 antipode sign), but **degenerate**:
its adjoint $\hat b:\epsilon\to\mathbb Q[1]$ is not an isomorphism.  The nondegenerate
symplectic object is the **hyperbolic plane** $H=\epsilon\oplus\mathbb Q$ with perfect
cross-pairing $\langle\,,\rangle:\epsilon\otimes^{\blacksquare}\mathbb Q\to\mathbb Z[1]$;
$\epsilon$ and $\mathbb Q$ are its two complementary **Lagrangians**.

**Darboux no-go / prime-indecomposability.** A StratPro support idempotent $e_S$
($S\subseteq\mathbb P$) on $\widehat{\mathbb Z}=\prod_p\mathbb Z_p$ **descends** to
$\mathrm{End}_{\mathrm{Solid}}(\epsilon)$ iff it preserves the diagonal
$\mathbb Z\hookrightarrow\widehat{\mathbb Z}$, iff $e_S(1)=\mathbf 1_S$ is a constant
CRT vector, iff $S\in\{\varnothing,\mathbb P\}$.  Hence $\epsilon$ admits no
$e_S$-induced decomposition: it is **prime-indecomposable**, obstructed by the unit
class $1\in\widehat{\mathbb Z}^{\times}$ (the engine of Pass-78 reflexivity).  The
primes are not Darboux coordinates of $\epsilon$.

## Skew hyperbolic plane, solid Borel $\mathrm{Sp}(H)$, and the no-flip wall (Pass 80)

The **skew hyperbolic phantom plane** is $H=\epsilon\oplus\mathbb Q$ in
$D(\mathrm{Solid}_{\mathbb Z})$, with nondegenerate symplectic form the
antisymmetrised perfect cross-pairing
$\langle\,,\rangle:\epsilon\otimes^{\blacksquare}\mathbb Q\to\mathbb Z[1]$.  It is
*skew* because its two complementary Lagrangians $\epsilon,\mathbb Q$ form a **dual
pair but are not isomorphic** (Pass 79): $\epsilon$ is reflexive
($\epsilon^{**}\cong\epsilon$) yet **not** $\otimes$-dualizable, so its endomorphism
object must be computed directly rather than via $D\epsilon\otimes\epsilon$.

**Endomorphism asymmetry.** $\mathrm{End}_{\mathrm{Solid}}(\mathbb Q)=\mathbb Q$,
$\mathrm{Hom}_{\mathrm{Solid}}(\mathbb Q,\epsilon)=\epsilon\neq0$, but
$$\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)
=H^0\,R\underline{\mathrm{Hom}}(\epsilon,\mathbb Q)=H^0(\mathbb Q[-1])=0,$$
so every solid endomorphism of $H$ is **upper-triangular**.

**Solid Borel symplectic group.** Consequently
$$\mathrm{Sp}(H)=\underline{\mathrm{Aut}}(H,\langle\,,\rangle)=B=T\ltimes U
\cong\mathbb Q^{\times}\ltimes\epsilon,$$
the affine "$ax+b$" group / Siegel-parabolic Schrödinger model fixing the
polarization $\epsilon$: torus $T=\mathbb Q^{\times}$ (rescaling the dual pair,
$\lambda$ on $\mathbb Q$ and $\lambda^{-1}$ on $\epsilon$) and abelian unipotent
radical $U$ of shears by the degenerate self-pairing $b$.  It is solvable — **not**
$\mathrm{SL}_2$ (no Weyl element / opposite unipotent) and **not** a nonabelian
Heisenberg group.

**Metaplectic non-descent wall.** The finite-adele Weil representation of
$\mathrm{SL}_2(\mathbb A_f)$ does **not** descend to a solid action on $\epsilon$:
the cross-polarization Weyl flip $w$ (finite-level Fourier transform $F_N$,
$F_N^4=I$, $|g_N|^2=N$) has no solid limit, because that limit would lie in
$\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0$.  The **precise wall** is this
one-sided vanishing — equivalently $\epsilon$ reflexive-but-not-dualizable — and is
**not** the degeneracy of $b$ (the shear-by-$b$ unipotent survives in $B$; only the
inverse intertwiner $\epsilon\to\mathbb Q$ is absent).  Only $B$, the Schrödinger
model in the fixed polarization $\epsilon$, acts.

## Degenerate principal series and the no-functional-equation wall (Pass 81)

For the solid Borel
$$B=\mathbb Q^{\times}\ltimes\epsilon=\mathrm{Sp}(H),$$
an unramified character is a character
$$\chi_s:B\twoheadrightarrow\mathbb Q^{\times}\xrightarrow{|\cdot|^s}R^{\times}$$
trivial on the unipotent radical $U=\epsilon$.

The associated **maximally degenerate principal series** is
$$I(s)=\mathrm{Ind}_{B}^{\mathrm{Sp}(H)}\chi_s.$$
Since $\mathrm{Sp}(H)=B$, the flag variety $\mathrm{Sp}(H)/B$ is a point and
$$I(s)\cong\chi_s.$$
It has length $1$ and no reducibility points.

The **standard intertwiner**
$$M(w,s):I(s)\to I(-s)$$
would require the opposite unipotent
$$\bar U=\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q).$$
But $\bar U=0$, so there is no nonzero Weyl/Fourier intertwiner and no
$s\mapsto -s$ functional equation.  Equivalently, the
Gindikin-Karpelevich / Harish-Chandra $c$-function is the empty product
$c(s)=1$ with no reflection operator attached to it.

Finite levels still have the usual Fourier reflection: for
$V_N=\mathbb C[\mathbb Z/N]$, dilation $D_t f(x)=f(t^{-1}x)$, and unitary finite
Fourier transform $F_N$,
$$F_ND_tF_N^{-1}=D_{t^{-1}}.$$
Thus the functional equation is **finitely present but limanly absent**.

## Whittaker vanishing and archimedean repair (Pass 82)

For the Pass-81 principal series $I(s)=\chi_s$, the unipotent radical
$U=\epsilon$ acts trivially.  Hence for a character $\psi:U\to R^{\times}$,
$$
\mathrm{Hom}_U(I(s),\psi)\cong
\begin{cases}
R,&\psi=1,\\
0,&\psi\ne1.
\end{cases}
$$
This is the **Whittaker vanishing** statement: nontrivial Whittaker or
generalized-Whittaker functionals do not exist; only the trivial-character
constant term survives.  The Rosser torsor is carried by the shear parameter
$U=\epsilon$, not by a generic Whittaker coefficient.

The finite Fourier shadow is the elementary identity
$$
\sum_{x\in\mathbb Z/N}e^{2\pi ikx/N}
=
\begin{cases}
N,&k=0,\\
0,&k\ne0,
\end{cases}
$$
so nontrivial finite characters also vanish on the constant $U_N$-action.

Adjoining the archimedean place gives the full adelic solenoid
$$
\Sigma=(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z
\cong\mathbb A/\mathbb Q.
$$
Projection to the real circle fits into the compact Hausdorff exact sequence
$$
0\to\widehat{\mathbb Z}
\to\Sigma\to\mathbb R/\mathbb Z\to0.
$$
The earlier Pass-82 shorthand that called $\epsilon$ the finite-prime kernel is
corrected in Pass 83: $\epsilon=\widehat{\mathbb Z}/\mathbb Z$ is the
dense/non-Hausdorff quotient $\Sigma/\mathbb R$, not the closed kernel of
$\Sigma\to\mathbb R/\mathbb Z$.
The real circle makes $\Sigma$ compact Hausdorff and globally self-dual, so it
repairs Fourier duality for the full adelic quotient.  It does **not** repair
the finite-prime Weyl wall: no solid morphism $\epsilon\to\mathbb Q$ is created.

## Global solenoid exact rows and the finite-phantom boundary (Pass 83)

For
$$
\Sigma=(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z,
$$
there are two different rows:
$$
0\to\widehat{\mathbb Z}\to\Sigma\to\mathbb R/\mathbb Z\to0,
$$
and
$$
\mathbb R\to\Sigma\to
\epsilon=\widehat{\mathbb Z}/\mathbb Z\to0.
$$
The first is a compact Hausdorff solenoid extension with closed profinite
kernel.  The second is the dense quotient row: the image of $\mathbb R$ in
$\Sigma$ is dense, and the quotient is the non-Hausdorff / derived-solid
phantom $\epsilon$.

Pontryagin duality sends the compact row to
$$
0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0.
$$
It is nonsplit: any section $\mathbb Q/\mathbb Z\to\mathbb Q$ would send
torsion to torsion, but $\mathbb Q$ is torsion-free.  Equivalently,
$\Sigma\to\mathbb R/\mathbb Z$ has no continuous, condensed degree-$0$, or
Borel-compatible splitting.

The restriction of global characters $\widehat{\Sigma}\cong\mathbb Q$ to the
closed kernel $\widehat{\mathbb Z}$ is the quotient
$$
\mathbb Q\to\mathbb Q/\mathbb Z.
$$
Only the trivial finite character descends further to
$\epsilon=\widehat{\mathbb Z}/\mathbb Z$, because a character of
$\widehat{\mathbb Z}$ descends to the quotient by dense $\mathbb Z$ exactly
when it kills $\mathbb Z$.  Thus the global Fourier transform gives a genuine
finite-character boundary $\mathbb Q/\mathbb Z$, but not a degree-$0$
Whittaker/Fourier character of $\epsilon$.

## Dense phantom quotient and shifted solid boundary (Pass 84)

The quotient topology on
$$
\epsilon=\widehat{\mathbb Z}/\mathbb Z
$$
is **indiscrete**.  Indeed, $\mathbb Z$ is dense in $\widehat{\mathbb Z}$, so
the saturation of any nonempty open set under addition by $\mathbb Z$ is all of
$\widehat{\mathbb Z}$.  Hence the Hausdorff reflection of $\epsilon$ is $0$,
and every continuous homomorphism from $\epsilon$ to a Hausdorff group is zero.
In particular, the Borel unipotent $U=\epsilon$ does **not** act by nontrivial
continuous translations on the compact Hausdorff solenoid $\Sigma$.

The nonzero finite-prime phantom is therefore not a topological degree-$0$
character object.  It is the solid derived boundary
$$
D\epsilon\simeq\mathbb Q[-1],
\qquad
\mathrm{Ext}^1_{\mathrm{Solid}}(\epsilon,\mathbb Q)\simeq\mathbb Q.
$$
The generator is the finite-adele extension
$$
0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0.
$$
Thus the missing finite-prime Weyl flip $\epsilon\to\mathbb Q$ is replaced by a
degree-$1$ boundary/shear class, not by a degree-$0$ morphism.  The object
$\mathbb Q/\mathbb Z$ remains the finite-character boundary of the closed
kernel $\widehat{\mathbb Z}\subset\Sigma$; its solid arithmetic completion is
the shifted boundary $\mathbb Q[-1]$ attached to $\epsilon$.

## Two-term complex models for the phantom boundary (Pass 85)

Use cohomological degrees $0\to1$.  The finite-prime boundary has three useful
two-term models:
$$
C_{\mathbb Z}=[\,\mathbb Z\to\widehat{\mathbb Z}\,],\qquad
C_{\mathbb R}=[\,\mathbb R\to\Sigma\,],\qquad
C_{\mathbb Q}=[\,\mathbb Q\to\mathbb A_f\,].
$$
Each differential is injective and each degree-$1$ quotient is
$$
H^1(C_{\mathbb Z})\cong H^1(C_{\mathbb R})\cong H^1(C_{\mathbb Q})
\cong\epsilon=\widehat{\mathbb Z}/\mathbb Z.
$$
Their ordinary finite/Hausdorff shadows are acyclic: the diagonal image is
surjective at every finite modulus, and the images of $\mathbb R$ in $\Sigma$
and $\mathbb Q$ in $\mathbb A_f$ are dense.

The complexes differ as extension data.  The map
$$
C_{\mathbb Z}\to C_{\mathbb Q}
$$
is the pushout along $\mathbb Z\hookrightarrow\mathbb Q$ and preserves the unit
class, giving the finite-adele shear extension
$$
0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0.
$$
The archimedean complex $C_{\mathbb R}$ has the same quotient $\epsilon$ but
does not preserve this finite-adele kernel/Yoneda class; it is the compact
solenoid repair, not the Borel shear replacement.

## Shear-pushout universal property (Pass 86)

Let $\mathcal P_{\mathbb Q}(\epsilon)$ denote the category of
shear-marked quotient models
$$
0\to D\to E\to\epsilon\to0
$$
equipped with a map from
$C_{\mathbb Z}=[\,\mathbb Z\to\widehat{\mathbb Z}\,]$, where:

1. $D$ is uniquely divisible, equivalently a $\mathbb Q$-vector object;
2. the extension is the pushout of
   $0\to\mathbb Z\to\widehat{\mathbb Z}\to\epsilon\to0$ along the chosen
   $\mathbb Z\to D$;
3. ordinary finite/Hausdorff quotient shadows are acyclic.

Then
$$
C_{\mathbb Q}=[\,\mathbb Q\to\mathbb A_f\,]
$$
is initial in $\mathcal P_{\mathbb Q}(\epsilon)$ under $C_{\mathbb Z}$.  The
reason is the localization property of $\mathbb Q$: a map
$\mathbb Z\to D$ into a uniquely divisible kernel has a unique extension
$\mathbb Q\to D$.  Therefore every shear-preserving pushout model factors
uniquely through $C_{\mathbb Q}$.

This is the categorical replacement for the missing finite-prime Weyl flip:
one localizes the kernel inside the extension category, rather than producing
a degree-$0$ morphism $\epsilon\to\mathbb Q$.

The hypothesis "uniquely divisible" is essential.  If arbitrary divisible
kernels are allowed, $\mathbb Q/\mathbb Z$ gives multiple maps
$$
\mathbb Q\to\mathbb Q/\mathbb Z,\qquad q\mapsto kq\bmod\mathbb Z
$$
that restrict identically on $\mathbb Z$ but differ on fractions.  Thus the
universal property is false for torsion-divisible kernels unless an additional
$\mathbb Q$-linear structure map or shear decoration is specified.

## Derived mapping-space form of shear initiality (Pass 87)

Let
$$
C_{\mathbb Z}=[\,\mathbb Z\to\widehat{\mathbb Z}\,],
\qquad
C_{\mathbb Q}=[\,\mathbb Q\to\mathbb A_f\,].
$$
For a shear-marked target model
$$
M=(0\to D\to E\to\epsilon\to0),
$$
the restriction map
$$
\operatorname{Map}(C_{\mathbb Q},M)\to
\operatorname{Map}(C_{\mathbb Z},M)
$$
has homotopy fiber
$$
\mathbf R\!\operatorname{Map}(\mathbb Q/\mathbb Z,D)
$$
over a fixed shear-marked map.  This follows from the cofiber sequence
$$
\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z
$$
on kernels.

If $D$ is uniquely divisible, then this fiber is contractible:
there is no nonzero homomorphism from the torsion group
$\mathbb Q/\mathbb Z$ to torsion-free $D$, and higher Ext obstructions vanish
because divisible groups are injective.  Thus the Pass-86 initiality of
$C_{\mathbb Q}$ is a derived mapping-space contractibility statement.

If $D$ has a torsion-divisible summand $T$, the extra fiber
$$
\mathbf R\!\operatorname{Map}(\mathbb Q/\mathbb Z,T)
$$
is nontrivial.  Strict initiality is recovered by either imposing $T=0$ or
adding a boundary decoration that fixes the component
$\mathbb Q/\mathbb Z\to T$.

## Stabilizer split for the finite-adele shear extension (Pass 88)

For the final shear extension
$$
0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0
$$
there are three different stabilizer levels.

1. **Strict marked stabilizer.**  As an object under
   $C_{\mathbb Z}=[\mathbb Z\to\widehat{\mathbb Z}]$, the complex
   $C_{\mathbb Q}=[\mathbb Q\to\mathbb A_f]$ has trivial automorphism group:
   the marked image of $1\in\mathbb Z$ forces scalar $1$, and the Pass-87
   mapping fiber $\mathbf R\operatorname{Map}(\mathbb Q/\mathbb Z,\mathbb Q)$
   is contractible.
2. **Extension-line stabilizer.**  Forgetting the integral marking but
   preserving the one-dimensional finite-adele Ext line leaves the Levi
   stabilizer $\mathbb Q^\times$, acting by rational scalar multiplication on
   $\mathbb Q$ and $\mathbb A_f$.
3. **Hyperbolic/Borel stabilizer.**  The full solid Borel
   $$
   \mathbb Q^\times\ltimes\epsilon
   $$
   is recovered only at the hyperbolic-plane level
   $H=\epsilon\oplus\mathbb Q$ with its polarization.  Here
   $\mathbb Q^\times$ is the Levi part and $\epsilon$ is the unipotent shear
   parameter; $\epsilon$ is not an endpoint-fixing automorphism of the bare
   exact row.

Thus the finite-adele row contributes the Borel's Levi extension class, while
the hyperbolic object supplies the unipotent shear action.

## Borel-torsor theorem for the Rosser phantom (Pass 89)

In the APS/Rosser phantom model developed in Passes 53-88, the following data
are four presentations of one torsor/extension class:

1. a Guaspari-Solovay witness-comparison Cech $1$-cocycle;
2. the derived-limit class
   $$\varprojlim\nolimits^1(\mathbb Z,\times m)\cong
   \widehat{\mathbb Z}_m/\mathbb Z,$$
   or, in the all-prime limit, $\epsilon=\widehat{\mathbb Z}/\mathbb Z$;
3. the finite-adele extension line
   $$0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0;$$
4. the hyperbolic Borel shear orbit for
   $$\mathbb Q^\times\ltimes\epsilon$$
   on $H=\epsilon\oplus\mathbb Q$.

The bridge is:
$$
\text{witness Cech cocycle}
\longmapsto
[\text{cocycle}]\in\operatorname{coker}\delta
\cong \varprojlim\nolimits^1
\longmapsto
0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0.
$$
The last arrow is the pushout/localization of
$$
0\to\mathbb Z\to\widehat{\mathbb Z}\to\epsilon\to0
$$
along $\mathbb Z\to\mathbb Q$.  The finite-adele row gives the Levi
extension line.  Passing to the hyperbolic plane restores the full Borel:
$\mathbb Q^\times$ is the Levi stabilizer and $\epsilon$ is the unipotent
shear torsor.

Changing Guaspari-Solovay witness choices is a gauge change.  It may change
the chosen section, finite truncation lift, or integer cocycle
representative, but only by a Cech coboundary.  Therefore the invariant data
are:

- the cohomology/torsor class in $\operatorname{coker}\delta$;
- the finite conductor restrictions and radical support;
- the finite-adele extension line;
- the hyperbolic Borel orbit up to the $\epsilon$ shear action.

Non-invariant data are the concrete representative, the witness enumeration,
and the chosen finite Loeb lift.  Thus the slogan "finitely Loeb, limanly
Rosser" can be sharpened: finite stages split after choosing a lift, while
the inverse limit remembers the unsplittable Borel-torsor class.

## Conductor-functorial Borel torsors (Pass 90)

For a finite prime support $S$, set
$$
P(S)=\left(\prod_{p\in S}\mathbb Z_p\right)/\Delta\mathbb Z.
$$
The canonical functoriality of $P(S)$ is by **restriction**.  If
$S\subseteq T$, coordinate projection induces
$$
\rho_{T,S}:P(T)\to P(S),
$$
because the diagonal copy of $\mathbb Z$ in $\prod_{p\in T}\mathbb Z_p$
projects to the diagonal copy of $\mathbb Z$ in
$\prod_{p\in S}\mathbb Z_p$.

The opposite direction has no canonical map on the quotient.  Zero-insertion
$$
\prod_{p\in S}\mathbb Z_p\to\prod_{p\in T}\mathbb Z_p
$$
does not descend to $P(S)\to P(T)$ when $T\setminus S\ne\varnothing$ and
$S\ne\varnothing$: the diagonal vector $(1,\ldots,1)$ maps to
$(1,\ldots,1,0,\ldots,0)$, which is not diagonal in the target.  Therefore
support enlargement is represented by a span, a pullback/fiber-product
condition, or a chosen finite-conductor section, not by a canonical quotient
homomorphism.

For rad-incomparable supports $S,T$, the canonical comparison is:

- a meet span
  $$P(S)\to P(S\cap T)\leftarrow P(T)$$
  for the shared ghost;
- a join arena $P(S\cup T)$ for gluing, with descent data checked by
  restrictions back to $S$ and $T$.

At finite conductor, the Borel shadows
$$
B_N=(\mathbb Z/N)^\times\ltimes\mathbb Z/N
$$
are functorial by reduction along $N\mid N'$.  The reduction
$B_{N'}\to B_N$ preserves the unit class $1\bmod N$ and the singleton strict
marked stabilizer.  Thus the Pass-89 Borel-torsor theorem is natural as a
restriction/span object over the finite prime-support lattice.

## Borel descent obstruction on the finite prime-cover site (Pass 91)

On the finite singleton-prime cover site, the unipotent phantom presheaf
$$
P(S)=\left(\prod_{p\in S}\mathbb Z_p\right)/\Delta\mathbb Z
$$
is not separated for $|S|\ge2$.  The descent map to singleton stalks has
kernel
$$
K_S=\mathbb Z^S/\Delta\mathbb Z\cong\mathbb Z^{|S|-1}.
$$
This is the horizontal Rosser descent defect.

The global-Levi Borel prestack is
$$
B^{\mathrm{glob}}(S)=\mathbb Q^\times\ltimes P(S).
$$
It is not a sheaf for multi-prime $S$: the unipotent kernel $K_S$ remains, and
the constant global Levi $\mathbb Q^\times$ sheafifies to local Levi data.
The local Borel sheafification/stackification is
$$
B^\#(S)=(\mathbb Q^\times)^S\ltimes
\prod_{p\in S}(\mathbb Z_p/\mathbb Z).
$$
The morphism $B^{\mathrm{glob}}\to B^\#$ forgets the Rosser horizontal kernel
and replaces the global Levi by independent local Levi factors.

The hyperbolic Borel shear action does not remove this defect.  It acts
transitively on the set of global lifts with the same local data, but it does
not choose a canonical zero lift.  Therefore the shear **transports** the
Rosser descent kernel rather than killing it.  On the discrete prime-cover
site, the Borel torsor is consequently a prestack/descent-obstruction object,
not a genuine sheaf; its sheafification is the local Loeb object.

## Zariski/generic Borel ghost line (Pass 92)

For a finite prime support $S$, let
$$
X_S=\{\eta\}\cup\{(p):p\in S\}
$$
with the finite Zariski/generic-point topology, and let
$j:\{\eta\}\hookrightarrow X_S$ be the open generic point.  The minimal-open
cover $U_p=\{\eta,(p)\}$ has full-simplex nerve, so constant coefficients on
$X_S$ have no horizontal $H^1$ defect.

The Zariski relocation of the Borel descent obstruction is the unipotent
$j_!$ cohomology group
$$
H^1(X_S,j_!\underline{\mathbb Z})
\cong \operatorname{coker}(\Delta:\mathbb Z\to\mathbb Z^S)
\cong \mathbb Z^S/\Delta\mathbb Z
\cong \mathbb Z^{|S|-1}.
$$
Thus the Borel analogue of the Pass-63 $j_!\mathbb Z$ ghost line is the
low-degree semidirect coefficient
$$
\mathfrak b_{j!}(S)=\underline{\mathbb Q^\times}\ltimes
j_!\underline{\mathbb Z}.
$$
The constant Levi $\mathbb Q^\times$ remains degree-$0$ global data on the
connected site; the Rosser/Borel obstruction lives in the unipotent radical.

Modulo $N$,
$$
|H^1(X_S,j_!\mathbb Z/N)|=N^{|S|-1},
$$
matching the finite diagonal descent kernel from the discrete prime-cover site.
With the dilation coefficient $\mathcal V$, the horizontal Borel ghost embeds
in the total phantom
$$
H^1(X_S,j_!\mathcal V)\cong\widehat{\mathbb Z}_S/\mathbb Z.
$$
Pushing out the integral row along $\mathbb Z\to\mathbb Q$ gives the
finite-adele extension line, while the hyperbolic Borel
$\mathbb Q^\times\ltimes\epsilon$ reads the same datum as a shear orbit.  The
Levi rescales representatives and the unipotent shear transports them, but no
canonical zero section is selected.

## All-prime continuous Borel $j_!$ coefficient (Pass 93)

On the honest all-prime Zariski site $\mathrm{Spec}\,\mathbb Z$, the singleton
generic point $\{\eta\}$ is **not** open: every nonempty basic open $D(n)$
contains $\eta$ and all but finitely many closed primes.  Therefore the
finite-support notation $j_!$ from $X_S=\{\eta\}\cup S$ cannot be interpreted
all-prime as ordinary extension by zero along an open immersion.

The all-prime Borel coefficient is instead the pro-open / continuous / solid
object
$$
\mathfrak B^{\mathrm{cont}}_{j!}
=\mathbb Q^\times\ltimes
R\!\varprojlim_{S\Subset\mathbb P}j_{S,!}\mathcal V_S,
$$
where $S$ ranges over finite prime supports and $\mathcal V_S$ is the
Pass-64 dilation coefficient.  The transition maps are restriction maps from
larger supports to smaller supports.

The support direction is Mittag-Leffler.  For $S\subseteq T$, the horizontal
integer skeleton has a surjection
$$
\mathbb Z^T/\Delta\mathbb Z\to\mathbb Z^S/\Delta\mathbb Z
$$
whose kernel has rank $|T|-|S|$; modulo $N$ its kernel has size
$N^{|T|-|S|}$.  Thus the support inverse system contributes no additional
$\varprojlim^1$.  The nonzero derived content remains the per-prime dilation
tower already built into $\mathcal V$.

The all-prime identity is therefore a continuous-cohomology statement:
$$
H^1_{\mathrm{cont}}(\mathrm{Spec}\,\mathbb Z,j_!\mathcal V)
:=\varprojlim_{S\Subset\mathbb P}H^1(X_S,j_{S,!}\mathcal V_S)
\cong
\left(\prod_p\mathbb Z_p\right)/\Delta\mathbb Z
=\widehat{\mathbb Z}/\mathbb Z.
$$
The global Levi $\mathbb Q^\times$ is retained.  Replacing it by
$\prod_p\mathbb Q^\times$ would be the local Loeb sheafification, not the
Rosser/Borel torsor.  Pushing out
$0\to\mathbb Z\to\widehat{\mathbb Z}\to\widehat{\mathbb Z}/\mathbb Z\to0$
along $\mathbb Z\to\mathbb Q$ yields the finite-adele row
$$
0\to\mathbb Q\to\mathbb A_f\to\widehat{\mathbb Z}/\mathbb Z\to0,
$$
and the hyperbolic Borel $\mathbb Q^\times\ltimes\epsilon$ acts on the same
continuous shear class.

## All-prime Borel $j_!$ solid-dual boundary (Pass 94)

Let
$$
\epsilon=\widehat{\mathbb Z}/\mathbb Z
$$
be the unipotent all-prime class of the continuous Borel $j_!$ coefficient.
In $D(\mathrm{Solid}_{\mathbb Z})$ its dual is
$$
D\epsilon\simeq\mathbb Q[-1].
$$
Thus the Verdier/solid dual of
$$
\mathfrak B^{\mathrm{cont}}_{j!}
=\mathbb Q^\times\ltimes
R\!\varprojlim_{S\Subset\mathbb P}j_{S,!}\mathcal V_S
$$
is a Levi-marked boundary object whose unipotent part is $\mathbb Q[-1]$
with contragredient $\mathbb Q^\times$ action.  It is not an opposite Borel
in degree $0$.

The finite signed Verdier rule survives:
$$
D(d_S)=-d_S^T,\qquad D^2(d_S)=d_S,
$$
where $d_S:\mathbb Z^S\to\mathbb Z^{|S|-1}$ is the recollement boundary from
the finite $X_S$ model.  The sign is visible over $\mathbb Z$ and invisible
modulo $2$.

All-prime, the same sign is the boundary-level antipode:
$$
\eta_\epsilon=-\mathrm{id}_\epsilon.
$$
It gives a functional-equation shadow only after replacing the missing
Weyl/Fourier operator by the degree-$1$ finite-adele extension
$$
0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0.
$$
No forbidden degree-$0$ flip is created, since
$$
\operatorname{Hom}^0_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0.
$$

## Boundary-only Borel constant-term complex (Pass 95)

The **boundary-only Borel constant-term complex** is
$$
C_B=\mathbb Q^\times\ltimes[\mathbb Q\to\mathbb A_f],
$$
with cohomological degrees $0\to1$.  The differential is the diagonal
inclusion $\mathbb Q\hookrightarrow\mathbb A_f$, and the global Levi
$\mathbb Q^\times$ acts by scalar multiplication on both terms.

Its all-prime solid boundary is
$$
H^0(C_B)=0,\qquad
H^1(C_B)=\mathbb A_f/\mathbb Q
\cong\widehat{\mathbb Z}/\mathbb Z=\epsilon.
$$
Thus $C_B$ packages the Pass-94 boundary functional-equation shadow without
creating an opposite Borel or a degree-$0$ Weyl operator.

At finite conductor $N$, the shadow is
$$
C_{B,N}=(\mathbb Z/N)^\times\ltimes
\left[\mathbb Z/N\to\prod_{p^e\parallel N}\mathbb Z/p^e\right].
$$
The diagonal map is an isomorphism by the Chinese remainder theorem, so every
fixed finite conductor shadow is ordinary-acyclic.  The phantom is therefore
not a fixed-level finite cokernel; it is the all-prime solid/pro boundary.

For $N\mid M$, conductor reduction gives a commuting square of two-term
complexes and preserves the Borel unit class.  For supports $S\subseteq T$,
projection $T\to S$ is canonical.  Support enlargement $S\to T$ is only a
finite-conductor CRT choice/span: exact zero-insertion does not preserve the
diagonal copy of $\mathbb Z$ in the all-prime product.

## Constant-term local Loebification comparison (Pass 96)

For finite prime support $S$, the compact skeleton of the Pass-95
constant-term complex is
$$
C_B^{\mathrm{int}}(S)=\mathbb Q^\times\ltimes
\left[\mathbb Z\to\prod_{p\in S}\mathbb Z_p\right],
$$
with diagonal degree-$0$ map.  The local Loebification target is
$$
C_L(S)=(\mathbb Q^\times)^S\ltimes
\left[\mathbb Z^S\to\prod_{p\in S}\mathbb Z_p\right],
$$
with coordinatewise degree-$0$ map.

The canonical comparison
$$
\alpha_S:C_B^{\mathrm{int}}(S)\to C_L(S)
$$
is diagonal on the Levi and on degree $0$, and identity on
$\prod_{p\in S}\mathbb Z_p$.  On unipotent $H^1$ it gives
$$
0\to\mathbb Z^S/\Delta\mathbb Z\to
(\prod_{p\in S}\mathbb Z_p)/\Delta\mathbb Z\to
\prod_{p\in S}(\mathbb Z_p/\mathbb Z)\to0.
$$
Thus the lost unipotent kernel is
$$
K_S=\mathbb Z^S/\Delta\mathbb Z\cong\mathbb Z^{|S|-1}.
$$
Modulo $N$, this kernel has size $N^{|S|-1}$.

The Levi comparison has a different character:
$$
\mathbb Q^\times\hookrightarrow(\mathbb Q^\times)^S
$$
has trivial kernel.  The local-Levi freedom created by sheafification is the
quotient
$$
\Lambda_S=(\mathbb Q^\times)^S/\Delta\mathbb Q^\times,
$$
not a second kernel.  Therefore the best formulation is a map of two-term
complexes plus stackification/local constant-term projection.  Pure
Hausdorff reflection describes only the unipotent quotient and misses the
Levi decentralization.

## Rationalized finite-adele Loebification comparison (Pass 97)

For finite support $S$, the rationalized version of the Pass-96 comparison is
the map of two-term complexes
$$
[\mathbb Q\to\prod_{p\in S}\mathbb Q_p]\to
[\mathbb Q^S\to\prod_{p\in S}\mathbb Q_p],
$$
diagonal in degree $0$ and identity in degree $1$.

The induced map on rationalized unipotent $H^1$ has exact kernel
$$
K_{\mathbb Q,S}=\mathbb Q^S/\Delta\mathbb Q.
$$
The compact integral kernel from Pass 96,
$$
K_{\mathbb Z,S}=\mathbb Z^S/\Delta\mathbb Z,
$$
injects into $K_{\mathbb Q,S}$.  Hence rationalization does not kill the
horizontal Loeb/Rosser kernel; it turns it into a divisible
$\mathbb Q$-vector boundary of dimension $|S|-1$.

The finite shadows are regraded.  Since $K_{\mathbb Q,S}$ is divisible,
$$
K_{\mathbb Q,S}/N K_{\mathbb Q,S}=0.
$$
But the quotient
$$
K_{\mathbb Q,S}/K_{\mathbb Z,S}
\cong(\mathbb Q/\mathbb Z)^S/\Delta(\mathbb Q/\mathbb Z)
$$
has $N$-torsion of size
$$
N^{|S|-1}.
$$
Thus the old finite shadow of $K_{\mathbb Z,S}$ survives as torsion in the
rational/integral boundary quotient, not as a finite quotient of
$K_{\mathbb Q,S}$ itself.

For $S\subseteq T$, support projection gives a surjection
$$
K_{\mathbb Q,T}\to K_{\mathbb Q,S}
$$
with kernel of $\mathbb Q$-dimension $|T|-|S|$.  Therefore the support
direction remains Mittag-Leffler after rationalization.

## Torsion boundary and solid-dual comparison (Pass 98)

For finite support $S$, define the **torsion boundary**
$$
T_S=(\mathbb Q/\mathbb Z)^S/\Delta(\mathbb Q/\mathbb Z).
$$
Equivalently,
$$
T_S\cong K_{\mathbb Q,S}/K_{\mathbb Z,S}
$$
for
$K_{\mathbb Q,S}=\mathbb Q^S/\Delta\mathbb Q$ and
$K_{\mathbb Z,S}=\mathbb Z^S/\Delta\mathbb Z$.

For every $N\ge2$,
$$
|T_S[N]|=N^{|S|-1}.
$$
This is the compact finite shadow from Pass 96 after rationalization: it is
not a quotient of the divisible vector group $K_{\mathbb Q,S}$, but the
$N$-torsion of the boundary quotient $K_{\mathbb Q,S}/K_{\mathbb Z,S}$.

The comparison with the Pass-94 solid dual
$$
D\epsilon\simeq\mathbb Q[-1],
\qquad
\epsilon=\widehat{\mathbb Z}/\mathbb Z,
$$
is not raw degree-$0$ object equality.  The bridge is the canonical unit
extension
$$
0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0.
$$
Applying the extension/solid-dual passage sends one
$\mathbb Q/\mathbb Z$ boundary coefficient to one shifted
$\mathbb Q[-1]$ constant-term obstruction generator.  Thus
$T_S\cong(\mathbb Q/\mathbb Z)^{|S|-1}$ presents $|S|-1$ finite-support
copies of the generator before passing to the all-prime boundary.

Consequently, the finite-support multiplicity $|S|-1$ is local-support
bookkeeping, but the $\mathbb Q/\mathbb Z$ coefficient is not a separate
artifact: it is the torsion presentation of the same shifted obstruction whose
all-prime solid-dual form is $\mathbb Q[-1]$.  This bridge does not create a
degree-$0$ Weyl/Fourier map $\epsilon\to\mathbb Q$.

## Primitive-collapse bridge to the constant-term complex (Pass 99)

The torsion boundary carries a canonical exact triangle
$$
K_{\mathbb Z,S}\to K_{\mathbb Q,S}\to T_S\to K_{\mathbb Z,S}[1],
$$
where
$$
K_{\mathbb Z,S}=\mathbb Z^S/\Delta\mathbb Z,\qquad
K_{\mathbb Q,S}=\mathbb Q^S/\Delta\mathbb Q,\qquad
T_S=(\mathbb Q/\mathbb Z)^S/\Delta(\mathbb Q/\mathbb Z).
$$

A map from this finite-support triangle to the one-generator unit extension
$$
\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to\mathbb Z[1]
$$
is determined by an integral zero-sum functional
$$
c=(c_p)_{p\in S}\in\mathbb Z^S,\qquad \sum_{p\in S}c_p=0.
$$
The zero-sum condition is exactly the condition that $c$ vanish on the
diagonal and therefore descend from $\mathbb Z^S,\mathbb Q^S,
(\mathbb Q/\mathbb Z)^S$ to the quotients.  The induced collapse
$$
T_S\to\mathbb Q/\mathbb Z
$$
is surjective precisely when $c$ is primitive, i.e.
$$
\gcd_{p\in S}(c_p)=1.
$$

For $r=|S|-1$ and primitive $c$, the map on finite shadows is
$$
T_S[N]\twoheadrightarrow(\mathbb Q/\mathbb Z)[N],
$$
with kernel of size
$$
N^{r-1}=N^{|S|-2}
$$
when $|S|\ge2$.

This collapse is not canonical.  The only support-symmetric integral
functional is constant on $S$, and the zero-sum condition forces it to be
zero.  Hence the passage from $|S|-1$ finite-support boundary coordinates to
one constant-term generator is an **orientation torsor** of primitive
zero-sum functionals, not a plain support limit.

After choosing such a primitive $c$, the triangle maps to the unit extension
and then to the all-prime constant-term row
$$
[\mathbb Q\to\mathbb A_f],
\qquad
H^1=\epsilon=\mathbb A_f/\mathbb Q.
$$
The antipode acts on the chosen functional by $c\mapsto -c$, negating the
boundary class.  This sign is visible over $\mathbb Z$ and invisible mod $2$.
The construction remains shifted through $D\epsilon\simeq\mathbb Q[-1]$ and
does not create a degree-$0$ Weyl/Fourier morphism $\epsilon\to\mathbb Q$.

## Orientation torsor under support change (Pass 100)

For finite support $S$ with $|S|\ge2$, the **primitive orientation torsor** is
$$
\mathcal O_S=
\{c=(c_p)_{p\in S}\in\mathbb Z^S:
\sum_{p\in S}c_p=0,\ \gcd_{p\in S}(c_p)=1\}.
$$
An element $c\in\mathcal O_S$ represents a primitive collapse
$$
T_S=(\mathbb Q/\mathbb Z)^S/\Delta(\mathbb Q/\mathbb Z)
\twoheadrightarrow\mathbb Q/\mathbb Z.
$$
The antipode acts freely by
$$
c\longmapsto -c.
$$

For an inclusion $S\subseteq T$, the canonical operation is pullback along the
boundary projection $T_T\to T_S$.  On orientations it is **zero-extension**
$$
e_{S,T}(c)_p=
\begin{cases}
c_p,&p\in S,\\
0,&p\in T\setminus S.
\end{cases}
$$
This preserves zero-sum, primitivity, and the collapse to
$\mathbb Q/\mathbb Z$.  It is strictly functorial:
$$
e_{T,U}\circ e_{S,T}=e_{S,U}.
$$
It is also antipode-equivariant:
$$
e_{S,T}(-c)=-e_{S,T}(c).
$$

The reverse operation is not canonical.  Restricting
$d\in\mathcal O_T$ to $S$ may fail the zero-sum condition and therefore may
not descend to a collapse on $T_S$.  For example,
$$
(1,1,-2)\in\mathcal O_{\{2,3,5\}}
$$
restricts to $(1,1)$ on $\{2,3\}$, whose sum is $2$.

If $c\in\mathcal O_S$ and $e_{S,T}(c)\in\mathcal O_T$ is its zero-extension,
then the finite-shadow kernel under collapse factors as
$$
N^{|T|-2}=N^{|S|-2}\cdot N^{|T|-|S|}.
$$
The first factor is the old collapse kernel and the second is the new support
kernel of $T_T\to T_S$.

There is no nonzero support-symmetric orientation: a support-symmetric
integral functional is constant, and zero-sum forces it to be zero.  Hence the
all-prime constant-term generator is not selected by a canonical symmetric
orientation.  It is obtained only after choosing an element of the
orientation torsor, quotienting by the antipode, or forgetting the orientation
data.

## Oriented-support action groupoid and antipode quotient (Pass 101)

For finite support $S$ with $|S|\ge2$, keep
$$
\mathcal O_S=
\{c=(c_p)_{p\in S}\in\mathbb Z^S:
\sum_{p\in S}c_p=0,\ \gcd_{p\in S}(c_p)=1\}.
$$
The **signed oriented-support action groupoid** has objects $(S,c)$ with
$c\in\mathcal O_S$.  For $S\subseteq T$, a morphism
$(S,c)\to(T,d)$ is a sign $\sigma\in\{\pm1\}$ such that
$$
d=\sigma e_{S,T}(c),
$$
where $e_{S,T}$ is zero-extension.  Composition multiplies signs:
$$
(\tau,U)\circ(\sigma,T)=(\tau\sigma,U),
$$
and identities have sign $+1$.

The antipode is the sign $-1$ morphism over a fixed support,
$$
(S,c)\longrightarrow(S,-c),
$$
and it squares to the identity.  It is compatible with support change because
$$
e_{S,T}(-c)=-e_{S,T}(c).
$$

The coarse antipode quotient replaces $c$ by the primitive line
$$
[c]=\{c,-c\}.
$$
This quotient presents the single collapse line but forgets the sign of a
transport path.  Therefore the plain quotient is not enough to retain the
Pass-94 functional-equation sign.  The equivalent sign-preserving package is
the coarse quotient together with the residual $\mathbb Z/2$ sign local
system coming from the double cover $(S,c)\to(S,[c])$.

On finite $N$-torsion, the antipode acts by multiplication by $-1$ on
$(\mathbb Q/\mathbb Z)[N]$.  This sign is visible for $N>2$ and collapses for
$N=2$.  Hence the signed action groupoid/local-system package preserves
exactly the earlier finite sign bookkeeping while still allowing the
all-prime constant-term generator to be presented as an antipode quotient.

## Sign local system through the finite-adele boundary (Pass 102)

Let
$$
\beta=[0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0]
$$
denote the one-generator unit extension reached after choosing a primitive
collapse $T_S\to\mathbb Q/\mathbb Z$.  Let
$$
\delta_\epsilon=[0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0],
\qquad
\epsilon=\mathbb A_f/\mathbb Q,
$$
denote the all-prime finite-adele boundary class.

The $\mathbb Z/2$ sign local system from the oriented-support quotient acts
on these boundary/Yoneda classes by multiplication:
$$
\beta\longmapsto\sigma\beta,\qquad
\delta_\epsilon\longmapsto\sigma\delta_\epsilon,
\qquad \sigma\in\{\pm1\}.
$$
Thus the sign is not an additional boundary object.  It is the local-system
coefficient on the one-dimensional line spanned by the extension class.

At finite level $N$, the shadow of $\beta$ is the Bockstein generator
$$
1\in\operatorname{Ext}^1(\mathbb Z/N,\mathbb Z)\cong\mathbb Z/N.
$$
The signed shadow is
$$
\sigma\in\mathbb Z/N.
$$
Consequently the sign is visible exactly for $N>2$ and collapses at $N=2$.

The boundary morphism of the finite-adele row is
$$
\partial_\epsilon:\epsilon\to\mathbb Q[1].
$$
Under the shifted dual identification
$$
D\epsilon\simeq\mathbb Q[-1],
$$
this is the same generator shifted.  A one-sided sign change negates the
class; applying the sign on both source and target multiplies by
$(-1)^2=1$.  Hence the biduality square is compatible with the antipode
involution.

The plain coarse quotient $[c]=\{c,-c\}$ is still insufficient because it
forgets whether the boundary class is $+\delta_\epsilon$ or
$-\delta_\epsilon$.  The $\mathbb Z/2$ local system is sufficient for the
finite sign bookkeeping and does not create any degree-$0$ Weyl/Fourier map
$\epsilon\to\mathbb Q$.

## Signed boundary naturality under conductor reduction (Pass 103)

For a finite conductor $N$, the signed finite Bockstein class is
$$
b_N^\sigma=\sigma\in\mathbb Z/N,\qquad \sigma\in\{\pm1\}.
$$
If $M\mid N$, the conductor-reduction map
$$
\rho_{N,M}:\mathbb Z/N\to\mathbb Z/M
$$
satisfies
$$
\rho_{N,M}(b_N^\sigma)=b_M^\sigma.
$$
Thus the sign local system is natural over finite conductor reductions.  The
only finite conductor reduction that erases the distinction between the two
signs is reduction to modulus $2$.

The signed finite conductor version of the Pass-95 constant-term complex is
$$
C^\sigma_{B,N}=(\mathbb Z/N)^\times\ltimes
\left[\mathbb Z/N
\xrightarrow{d_N^\sigma}
\prod_{p^e\parallel N}\mathbb Z/p^e\right],
$$
where
$$
d_N^\sigma(x)=(\sigma x\bmod p^e)_{p^e\parallel N}.
$$
Since $\sigma=\pm1$ is a unit modulo every $N$, $d_N^\sigma$ is a CRT
isomorphism.  Therefore
$$
H^0(C^\sigma_{B,N})=H^1(C^\sigma_{B,N})=0
$$
for every fixed finite conductor $N$.

For $M\mid N$, the square formed by $d_N^\sigma$, $d_M^\sigma$, and conductor
reduction on source and prime-power target coordinates commutes.  Hence
conductor reduction introduces no sign-twisted finite cohomology class.  The
all-prime boundary $\epsilon$ is still a pro/solid phenomenon, not a fixed
finite CRT cokernel.

This conductor result does not change the support warning from Pass 95:
support projection is canonical, but support enlargement remains only a
finite-conductor CRT choice/span and is not a canonical all-prime
diagonal-preserving morphism.

## Signed pro/solid all-prime boundary object (Pass 104)

The signed finite conductor system
$$
b_N^\sigma=\sigma\bmod N,\qquad \sigma\in\{\pm1\},
$$
is compatible under all conductor reductions.  Therefore it has inverse
limit
$$
\{b_N^\sigma\}_N=\sigma\in\widehat{\mathbb Z}.
$$

Since $\sigma=\pm1$ is a diagonal integer, its image in
$$
\epsilon=\widehat{\mathbb Z}/\mathbb Z
$$
is zero.  Thus the two signs do not define two distinct points of
$\epsilon$, and the orientation double cover does not survive as a
nontrivial point-cover or torsor over the all-prime boundary group itself.

The sign survives instead as the $\mathbb Z/2$ local-system action on the
boundary/Yoneda line.  If
$$
\delta_\epsilon=[0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0],
$$
then
$$
\delta_\epsilon\longmapsto\sigma\delta_\epsilon
$$
is the remaining sign action.  Under
$$
D\epsilon\simeq\mathbb Q[-1],
$$
this is the same action on the shifted boundary generator.

The minimal sign-preserving all-prime package is therefore:

1. the oriented-support action groupoid of pairs $(S,c)$;
2. the finite-conductor pro-system of signed CRT-isomorphism complexes
   $C^\sigma_{B,N}$;
3. a $B\mathbb Z/2$ local system on the boundary/Yoneda line.

This package records support, conductor, and sign, but it does not create a
degree-$0$ Weyl/Fourier morphism:
$$
\operatorname{Hom}^0(\epsilon,\mathbb Q)=0.
$$

## Support descent for all-prime primitive orientations (Pass 105)

For finite support $S$ with $|S|\ge2$, let
$$
\mathcal O_S=
\{c=(c_p)_{p\in S}\in\mathbb Z^S:
\sum_{p\in S}c_p=0,\ \gcd_{p\in S}(c_p)=1\}.
$$
If $S\subseteq T$, the canonical orientation operation is zero-extension:
$$
e_{S,T}:\mathcal O_S\to\mathcal O_T,\qquad
(e_{S,T}c)_p=
\begin{cases}
c_p,&p\in S,\\
0,&p\in T\setminus S.
\end{cases}
$$
It preserves zero-sum, primitivity, and the antipode:
$$
e_{S,T}(-c)=-e_{S,T}(c).
$$
It is also strictly functorial:
$$
e_{T,U}e_{S,T}=e_{S,U}.
$$

The boundary support projection points in the opposite direction:
$$
T_T\to T_S.
$$
Thus support descent is a span-style construction, not a single variance.
There is no total canonical restriction map
$$
\mathcal O_T\to\mathcal O_S.
$$
Deleting coordinates can destroy zero-sum; for instance
$$
(1,1,-2)\in\mathcal O_{\{2,3,5\}}
$$
restricts to $(1,1)$ on $\{2,3\}$, whose sum is $2$.

The all-prime primitive-orientation object is therefore the filtered colimit
of the $\mathcal O_S$ under zero-extension, modulo padded zero coordinates.
Equivalently, it is the set of primitive finitely supported zero-sum integer
functionals on the prime set, with support padding forgotten.  Passing to the
antipode quotient gives primitive lines
$$
[c]=\{c,-c\},
$$
but the sign must still be retained as the $B\mathbb Z/2$ local system on the
boundary/Yoneda line.

The correct categorical package is a span-stack/Grothendieck presentation
over finite supports with:

1. orientation zero-extension $e_{S,T}$;
2. boundary projection $T_T\to T_S$;
3. the $B\mathbb Z/2$ local system on $\delta_\epsilon$.

It is not a plain sheaf of primitive orientations with restriction maps, and
it still does not create a degree-$0$ Weyl/Fourier morphism
$\epsilon\to\mathbb Q$.

## Stackification obstruction for primitive orientations (Pass 106)

For $S\subseteq T$ and $d\in\mathcal O_T$, coordinate deletion to $S$ has
additive defect
$$
\Delta_{T,S}(d)=\sum_{p\in S}d_p.
$$
Because $d$ is zero-sum over $T$,
$$
\Delta_{T,S}(d)=-\sum_{p\in T\setminus S}d_p.
$$
Thus coordinate deletion defines a primitive restriction only on the partial
domain where
$$
\Delta_{T,S}(d)=0
\quad\text{and}\quad
\gcd_{p\in S}(d_p)=1.
$$
The additive and primitivity obstructions are independent.  For example,
$$
(2,-2,1,-1)\in\mathcal O_{\{2,3,5,7\}}
$$
has zero additive defect on $\{2,3\}$ but restricts to $(2,-2)$, which is
not primitive.

Repairing a nonzero defect requires a section of the summation map
$$
\Sigma_S:\mathbb Z^S\to\mathbb Z,\qquad
(a_p)\mapsto\sum_{p\in S}a_p.
$$
If a section were support-symmetric, the image of $1$ would be a constant
vector $(k,\dots,k)$, forcing
$$
|S|k=1,
$$
which has no integer solution for $|S|>1$.  Based or ordered supports can
choose a section, but the basepoint or order is extra structure and is not
natural after forgetting it.

Therefore the correct universal object is not a restriction sheaf.  It is
the zero-extension colimit
$$
\mathcal O_{\mathbb P}^{\mathrm{fin}}
=\operatorname*{colim}_{S\in\mathcal P_{\mathrm{fin}}(\mathbb P)}
\mathcal O_S,
$$
formed under the maps $e_{S,T}$.  A family
$F_S:\mathcal O_S\to X$ factors uniquely through this colimit exactly when
$$
F_T(e_{S,T}c)=F_S(c)
$$
for every $S\subseteq T$.  Concretely,
$\mathcal O_{\mathbb P}^{\mathrm{fin}}$ is primitive finitely supported
zero-sum integer functions on the prime set, modulo deletion of padded zeros.

The antipode quotient
$$
[c]=\{c,-c\}
$$
is the coarse orientation line.  It forgets whether the boundary/Yoneda line
is acted on by $+\delta_\epsilon$ or $-\delta_\epsilon$, so the
$B\mathbb Z/2$ local system remains part of the all-prime package.  This
obstruction analysis still creates no degree-$0$ Weyl/Fourier morphism
$\epsilon\to\mathbb Q$.

## Correction torsors for support-defect repairs (Pass 107)

For finite support $S$, set
$$
K_S=\ker\Sigma_S
=\{a\in\mathbb Z^S:\sum_{p\in S}a_p=0\}.
$$
Given $S\subseteq T$ and $d\in\mathcal O_T$, let $u=d|_S$ be the coordinate
deletion and let
$$
\Delta=\Sigma_S(u).
$$
An additive repair is a vector $r\in\mathbb Z^S$ of the form
$$
r=u-a,\qquad \Sigma_S(a)=\Delta,
$$
so that $\Sigma_S(r)=0$.  If $r$ and $r'$ are additive repairs, then
$$
r'-r\in K_S.
$$
Conversely, $r+k$ is an additive repair for every $k\in K_S$.  Thus additive
repairs form a free transitive $K_S$ torsor.

Primitive repair choices are subtler.  They are the primitive vectors inside
the additive repair torsor, and this primitive locus is not stable under the
full kernel action.  For example, on support $\{2,3\}$,
$$
(1,-1)+(1,-1)=(2,-2),
$$
where both summands lie in $K_S$ and $(1,-1)$ is primitive, but $(2,-2)$ is
not primitive.

A basepoint $b\in S$ gives a section
$$
s_b:\mathbb Z\to\mathbb Z^S,\qquad s_b(n)=n e_b.
$$
Transitions between basepoints are
$$
\tau_{a,b}=s_b(1)-s_a(1)\in K_S,
$$
and they satisfy the cocycle identity
$$
\tau_{a,b}+\tau_{b,c}=\tau_{a,c}.
$$
These transitions are coboundaries of the chosen splittings.  Along an
inclusion $S\subseteq T$, the splittings are natural exactly when the
basepoint is preserved; changing basepoint gives a $K_T$-valued transition.

Therefore the support-defect repair data is ordinary finite-level choice
data, not a Rosser/cosheaf phantom.  The short exact sequence
$$
0\to K_S\to\mathbb Z^S\xrightarrow{\Sigma_S}\mathbb Z\to0
$$
splits after any basepoint choice, and no non-Mittag-Leffler inverse tower is
present.  Linear repair sections are antipode-compatible:
$$
\operatorname{repair}_{s_b}(-d)=-\operatorname{repair}_{s_b}(d),
$$
so the $B\mathbb Z/2$ boundary-line local system is unaffected.

## Integral equivariant repair-section obstruction (Pass 108)

Let $S$ be a finite support with $|S|=n>1$, and let
$G=\operatorname{Sym}(S)$ act on $\mathbb Z^S$ by permuting coordinates.  The
summation map
$$
\Sigma_S:\mathbb Z^S\to\mathbb Z
$$
is $G$-equivariant, where $\mathbb Z$ has the trivial action.

The invariant lattice is
$$
(\mathbb Z^S)^G=\mathbb Z\mathbf 1_S,
\qquad
\mathbf 1_S=(1,\dots,1).
$$
Hence
$$
\Sigma_S(k\mathbf 1_S)=nk,
$$
so the invariant image is $n\mathbb Z$.  A support-symmetric integral
section would require an invariant vector mapping to $1$, which is
impossible for $n>1$.

After tensoring with $\mathbb Q$, the barycentric section
$$
s_{\mathrm{bar}}:\mathbb Q\to\mathbb Q^S,\qquad
s_{\mathrm{bar}}(1)=\frac1n\mathbf 1_S
$$
is $G$-equivariant and satisfies $\Sigma_Ss_{\mathrm{bar}}(1)=1$.  Thus the
obstruction is exactly the denominator $n$.  Equivalently, an equivariant
integral lift of $m\in\mathbb Z$ exists iff
$$
n\mid m.
$$
The finite obstruction group can be recorded as
$$
\mathbb Z/\Sigma_S((\mathbb Z^S)^G)\cong\mathbb Z/n\mathbb Z.
$$

This obstruction is separate from the antipode local system.  The antipode
acts by a scalar sign on the boundary/Yoneda line and commutes with support
permutations.  It sends the rational barycenter to its negative but does not
change the denominator $n$.

Under an inclusion $S\subseteq T$, barycentric sections are not natural:
zero-extending $\frac1{|S|}\mathbf 1_S$ to $T$ differs from
$\frac1{|T|}\mathbf 1_T$ by an element of
$K_T\otimes\mathbb Q$.  The denominators of these rational transition
classes are the next bookkeeping problem.

## Barycentric support-transition denominators (Pass 109)

For finite supports $S\subset T$, set $|S|=n$ and $|T|=m$.  The rational
barycentric transition is
$$
\tau_{S,T}
=e_{S,T}\left(\frac1n\mathbf 1_S\right)-\frac1m\mathbf 1_T
\in\mathbb Q^T.
$$
Its coordinates are
$$
(\tau_{S,T})_p=
\begin{cases}
\frac{m-n}{nm}, & p\in S,\\[2mm]
-\frac1m, & p\in T\setminus S.
\end{cases}
$$
The sum is zero, so
$$
\tau_{S,T}\in K_T\otimes\mathbb Q.
$$

Let $g=\gcd(n,m)$, $n=ga$, and $m=gb$ with $\gcd(a,b)=1$.  The exact
denominator of $\tau_{S,T}$ is
$$
\operatorname{den}(\tau_{S,T})=\operatorname{lcm}(n,m)=\frac{nm}{g}.
$$
Equivalently, a finite conductor $N$ clears $\tau_{S,T}$ iff
$$
\operatorname{lcm}(n,m)\mid N.
$$

The minimal integral clearing is
$$
\eta_{S,T}:=\operatorname{lcm}(n,m)\tau_{S,T}.
$$
It has coordinates
$$
(\eta_{S,T})_p=
\begin{cases}
\frac{m-n}{g}, & p\in S,\\[2mm]
-\frac{n}{g}, & p\in T\setminus S.
\end{cases}
$$
This vector is zero-sum and primitive, because its nonzero coordinate values
are $b-a$ and $-a$, with $\gcd(b-a,a)=1$.

For a chain $S\subset T\subset U$, the rational transitions satisfy
$$
e_{T,U}\tau_{S,T}+\tau_{T,U}=\tau_{S,U}.
$$
After clearing by any common conductor divisible by all three transition
denominators, this identity holds integrally.  The individually primitive
vectors $\eta_{S,T}$, however, carry different normalizing conductors, so
their chain law requires rescaling.

This denominator bookkeeping is distinct from finite CRT cohomology.  At any
finite conductor $N$, the ordinary and signed CRT maps remain bijections; the
denominator only says when the rational support transition has an integral
zero-sum representative.

## Primitive conductor-cleared transition chain law (Pass 110)

For finite supports $S\subset T$, define
$$
L_{S,T}:=\operatorname{lcm}(|S|,|T|)
$$
and
$$
\eta_{S,T}:=L_{S,T}\tau_{S,T}\in K_T.
$$
The vector $\eta_{S,T}$ is the minimally conductor-cleared barycentric
transition.  If $|S|=n$, $|T|=m$, and $g=\gcd(n,m)$, then its entries are
$$
(\eta_{S,T})_p=
\begin{cases}
\frac{m-n}{g}, & p\in S,\\[2mm]
-\frac{n}{g}, & p\in T\setminus S.
\end{cases}
$$
It is zero-sum and primitive.

For a chain $S\subset T\subset U$, set
$$
C=\operatorname{lcm}(L_{S,T},L_{T,U},L_{S,U}).
$$
The rational coboundary identity for the $\tau$'s is equivalent to the
conductor-weighted integral identity
$$
\frac{C}{L_{S,T}}e_{T,U}\eta_{S,T}
+\frac{C}{L_{T,U}}\eta_{T,U}
=
\frac{C}{L_{S,U}}\eta_{S,U}.
$$

Thus the pair $(L_{S,T},\eta_{S,T})$ is functorial edge data, while the
primitive vector or primitive line alone is generally not functorial.  Strict
primitive composition can occur in equal-conductor cases, but in general the
common-conductor identity may produce a nonprimitive multiple of the endpoint
primitive vector.  This is the same arithmetic phenomenon as in primitive
repair loci: additive kernels are closed under the relevant sums, while
primitive representatives are only normalized elements inside those kernels.

## MacNeille reflection checker repair (Pass 111)

For a finite preorder $L$, write
$$
X^u=\{a\in L:\forall x\in X,\ x\le a\},
\qquad
X^l=\{a\in L:\forall x\in X,\ a\le x\}.
$$
The MacNeille completion is represented by lower cuts
$$
C=(C^u)^l,
$$
with principal lower cut
$$
i_L(a)=(\{a\}^u)^l.
$$

For an antitone refutability map
$$
\boxtimes:L\to L,
$$
the current checker convention treats $\boxtimes$ as a monotone map
$L\to L^{op}$ before closing the pointwise image.  The rule is named
`antitone-dual-lower-cut-v1` and is
$$
\widehat{\boxtimes}(C)=\bigl((\boxtimes[C])^{l_L}\bigr)^{u_L}.
$$
The legacy rule `antitone-dual-lower-cut-v0`,
$$
\bigl((\boxtimes[C])^{u_L}\bigr)^{l_L},
$$
has the wrong polarity for antitone $L\to L^{op}$ extensions and is retained
only as a comparison control.

A completed fixed cut $q$ is **principal** if $q=i_L(a)$ for some
$a\in L$.  It is **reflected** if it is principal and the principal element
is a syntactic fixed point:
$$
a=\boxtimes a.
$$
A **principal-unreflected** fixed cut is principal but its principal element
is not a syntactic fixed point.  A **nonprincipal-without-syntactic** fixed
cut is a non-principal completed fixed cut occurring in a model with no
syntactic fixed point.

For v1 the principal-extension condition compares the completed value of
$i_L(a)$ with the dual principal cut at $\boxtimes a$:
$$
\widehat{\boxtimes}(i_L(a))=i_{L^{op}}(\boxtimes a).
$$
Failure of this condition indicates that the selected extension rule is not
preserving principal elements with the intended variance.

The three-element non-lattice witness `three-element-nolattice-nosynt` has
carrier $\{0,a,b\}$ with $0<a$, $0<b$, and $a,b$ incomparable.  Its
refutability sends $0$ to $a$ and sends $a,b$ to $0$.  It has no syntactic
fixed point.  Under v1, the completion has the non-principal fixed cut
`{ 0, a, b }`; under legacy v0, it instead returns the principal but
unreflected cut `{ 0, a }` and fails the principal-extension condition.

## Finite APS table checks for MacNeille reports (Pass 112)

The MacNeille reflection checker now records a finite `apsAxioms` block for
each input table.  These are order/table checks on the finite carrier, not
residuation or completion-stability theorems.

For a finite preorder with distinguished `top` $T$, `bottom` $\bot$,
monotone candidate $\Box$, and antitone candidate $\boxtimes$, the fields mean:

1. **A1BoxMonotone:** $x\le y$ implies $\Box x\le\Box y$.
2. **A1BoxtimesAntitone:** $x\le y$ implies $\boxtimes y\le\boxtimes x$.
3. **A2TopLeBoxtimesBottom:** $T\le \boxtimes\bot$.
4. **A3CollisionCut:** if $x\le\Box y$ and $x\le\boxtimes y$, then
   $x\le\boxtimes T$.
5. **A4BoxtimesLeBoxBoxtimes:** $\boxtimes x\le\Box(\boxtimes x)$.

The checker abbreviates
$$
\mathrm{A124Core}:=\mathrm{A1BoxMonotone}\wedge
\mathrm{A1BoxtimesAntitone}\wedge
\mathrm{A2TopLeBoxtimesBottom}\wedge
\mathrm{A4BoxtimesLeBoxBoxtimes}
$$
and
$$
\mathrm{APS}:=\mathrm{A124Core}\wedge\mathrm{A3CollisionCut}.
$$

The Pass-112 fixed-carrier search also isolates an **A2 gate** on the
three-element V-carrier $\{0,a,b\}$ with $0<a$ and $0<b$: completion
separation plus G2 exists on that carrier only when A2 is not required.  Once
A2 is imposed, no table on that carrier has simultaneously a v1
non-principal completion fixed cut without syntactic fixed point and G2.  This
is a carrier-local search fact, not yet a general reflection theorem.

## Four-element G2+finite-APS MacNeille witness (Pass 113)

The Pass-113 witness is the finite poset
$$
0<a<b,\qquad 0<c,
$$
with no comparison between $c$ and $a,b$ beyond $0<c$.  The distinguished
elements and operations are
$$
T=a,\qquad \bot=0,
$$
$$
\boxtimes(0)=b,\quad \boxtimes(a)=b,\quad
\boxtimes(b)=0,\quad \boxtimes(c)=0,
$$
and
$$
\Box(0)=0,\quad \Box(a)=0,\quad \Box(b)=b,\quad \Box(c)=0.
$$

This table is antitone for $\boxtimes$ and monotone for $\Box$.  It satisfies
finite A1-A4:

- A2 holds because $T=a\le b=\boxtimes\bot$.
- G2 holds in the formal implication sense because
  $\boxtimes T=b\not\le0=\bot$.
- FG2 holds because $\boxtimes^2T=\boxtimes b=0\le b=\boxtimes T$.

There is no syntactic fixed point $x=\boxtimes x$.  Under the v1 MacNeille
extension, the cut
$$
\{0,a,b,c\}
$$
is a fixed cut and is non-principal, since the carrier has no greatest
element.  This witness shows that the Pass-112 A2 gate is specific to the
three-element V-carrier.  It does **not** yet supply residual operations or a
completion-stability theorem.

## Same-carrier residual obstruction for the four-element witness (Pass 114)

For a finite ordered carrier with binary operation $\otimes$, a left residual
for fixed $a,c$ exists in the carrier exactly when the fiber
$$
\{x:a\otimes x\le c\}
$$
is a principal downset.  The right residual is checked dually by requiring
$$
\{x:x\otimes a\le c\}
$$
to be principal for every $a,c$.

Pass 114 applies this principal-downset criterion to every binary operation on
the Pass-113 four-element carrier/order with a two-sided unit.  Among
1,048,576 operations, 624 are associative and 56 are both associative and
monotone, but none has both residuals.  The first residual obstruction is
$$
\{x:0\otimes x\le0\}=\{0,a,b,c\},
$$
which is not principal because the four-element carrier has no greatest
element.  This is a same-carrier and same-order obstruction only; adding a
top or join may change the principal-fiber calculation and must be checked as
a separate order-repair problem.

## $\boxtimes$-antichain 2-cycle plateau and the antitone De Morgan join law (Pass 117)

A **$\boxtimes$-antichain $k$-cycle plateau** is a set of pairwise-incomparable
carrier elements $\{x_0,\dots,x_{k-1}\}$ ($x_i\parallel x_j$ for $i\ne j$)
permuted cyclically by $\boxtimes$: $\boxtimes x_i=x_{i+1\bmod k}$. For $k=2$
this is the detached-Rosser $R_2$ geometry: $x\parallel y$,
$\boxtimes x=y$, $\boxtimes y=x$, so $\boxtimes^2$ fixes both while $\boxtimes$
itself has no fixed point among $\{x,y\}$. A plateau is **join-defected** when
its join $\bigvee_i x_i$ is unattained in the carrier — realized minimally by a
**doubled cover** (two incomparable minimal upper bounds), the one-dimension-up
analogue of the Pass-49 phantom $a^\ast\prec\{m,b^\ast\}$.

The **MacNeille antitone extension** of an antitone $\boxtimes$ to the
completion is $\widehat\boxtimes(C)=(\boxtimes[C])^{\ell}$ (the lower bounds of
the image); it is antitone and agrees with $\boxtimes$ on principal cuts,
$\widehat\boxtimes(\mathrm{down}\,a)=\mathrm{down}(\boxtimes a)$. The
**antitone De Morgan join law** is the identity, for incomparable $x,y$ with
unattained join,
$$
\widehat\boxtimes(x\vee y)=\boxtimes x\wedge\boxtimes y ,
$$
i.e. an antitone map sends a completion join to the meet of the images. It is
the load-bearing fact of Pass 117: the join is a $\widehat\boxtimes$-fixed cut
iff $x\vee y=\boxtimes x\wedge\boxtimes y$, i.e. iff the images lie **above** the
summands — impossible for any orbit (descending chain or swap 2-cycle) that runs
*through* the summands.

An **even-orbit** carrier (all $\boxtimes$-orbits of even combinatorial length,
including collapsing chains that terminate at $\bot$) yields a
$\widehat\boxtimes$ whose antitone-Tarski interval
$[\mathrm{lfp}\,\widehat\boxtimes^2,\mathrm{gfp}\,\widehat\boxtimes^2]$ carries
no interior self-dual cut, hence is **fixed-point-free** (the
$2^n$-complementation phenomenon). An **odd self-dual seed** is a carrier-level
Jeroslow refutability fixed point $p=\boxtimes p$ (FP-synt) or, more generally,
a self-dual cut fixed by $\widehat\boxtimes$; by Thm 117c its presence is
*necessary* for any non-principal $\widehat\boxtimes$-fixed cut on a finite
carrier — completion-generated separation is a conservative shadow of FP-synt.

## Pentagon top-repair $N_5$ and the join-defect load-bearing principle (Pass 115)

The **top-repair** of the Pass-113 four-element witness adjoins the single
missing join $U:=b\vee c$ as a new greatest element, giving the carrier
$\{0,a,b,c,U\}$ with $0<a<b<U$, $0<c<U$.  This order is exactly the **pentagon
$N_5$**, the smallest non-modular (hence non-distributive) lattice
($b\wedge c=0$, $a\wedge c=0$, $a\vee c=b\vee c=U$).  Antitonicity forces
$\boxtimes U=0$; monotonicity leaves $\Box U\in\{b,U\}$.

The **join-defect load-bearing principle** records the outcome (Thm 115a): on
this carrier the Pass-114 residual non-principality and the Pass-113 MacNeille
completion-separation are *one* defect, the absent join $b\vee c$.  Supplying it
(i) preserves A1-A4, G2, FG2 and $\mathrm{Fix}(\boxtimes)=\varnothing$;
(ii) **destroys** the completion-separation, because a finite lattice is its own
MacNeille completion so every cut is principal — the unique completion-fixed cut
$\downarrow U$ is principal and *unreflected* ($\boxtimes U\ne U$); and
(iii) **repairs** residuation but only into the non-integral (Rosser) regime —
$115$ commutative residuated tensors exist, all with unit in $\{a,b,c\}$ and
none with the integral unit $U$, since $N_5$ non-distributive makes the meet
tensor non-residuated.  Consequence (Cor 115b): a **non-principal MacNeille
fixed cut requires a non-lattice carrier**; the separation cannot coexist with a
lattice (finite-complete) top-repair.  See
`research/notes/g2-fg2-hierarchy.md` (Pass 115) and
`code/scripts/check-pass115.py` ->
`artifacts/reports/pass115-top-repair-n5-check.json`.  Compare the residuated
non-integral-unit regime with [[integral-vs-non-integral-unit-loeb-rosser]]
(Pass 51c) and the doubled-cover phantom of Pass 49.

## Doubled-cover top-repair and join-defect conservation (Pass 116)

The **doubled-cover top-repair** of the Pass-113 four-element witness is the
*non-lattice* alternative to the pentagon $N_5$ repair.  Instead of adjoining a
single top $U=b\vee c$, one adjoins a top $U$ above **two incomparable minimal
upper bounds** $m,n$ of $\{b,c\}$: the carrier is $L_1=\{0,a,b,c,m,n,U\}$ with
covers $0\prec a\prec b$, $0\prec c$, $b\prec m$, $b\prec n$, $c\prec m$,
$c\prec n$, $m\prec U$, $n\prec U$ ($m\parallel n$).  $L_1$ is **bounded but not
a lattice**: $b\vee c$ (and $a\vee c$, and $m\wedge n$) are unattained.  It is
the one-dimension-up analogue of the Pass-49 phantom $a^\ast\prec\{m,b^\ast\}$.

**Join-defect conservation** (Thm 116a, Cor 116b) is the principle governing
such repairs: on the collapsing-chain orbit $T=a\mapsto b\mapsto 0$ with
$\boxtimes b=\boxtimes c=0$, the absent join $b\vee c$ is a **conserved charge**
that a bounded repair can *relocate* but not *annihilate*.  A single top ($N_5$)
displaces it into principality (no non-principal cut; residuation repaired at the
Rosser tax); a doubled-cover top ($L_1$) retains the non-principal cut
$\{0,a,b,c\}$ but displaces the defect into (1) $\widehat{\boxtimes}$-unfixedness
of that cut — $\widehat{\boxtimes}(b\vee c)=\boxtimes b\wedge\boxtimes c=\bot<b$ —
and (2) a top-less residual fiber $\{0,a,b,c,m,n\}=L_1\setminus\{U\}$ one level
down.  Hence "principal residual fiber" and "non-principal completion-**fixed**
cut" cannot coexist on any such carrier.  By Rem 116c the obstruction is
orbit-driven, not order-driven: a fixed non-principal cut at $j=x\vee y$ needs
$\boxtimes x\wedge\boxtimes y=j>x,y$, which antitonicity permits only for an
incomparable $\boxtimes$-**plateau** ($2$-cycle $\boxtimes x=y,\boxtimes y=x$),
never for a collapsing chain.  See `research/notes/g2-fg2-hierarchy.md`
(Pass 116), `code/scripts/check-pass116.py` ->
`artifacts/reports/pass116-doubled-cover-coexistence-check.json`.  Compare the
Pass-42 $R_2$ / Pass-48 $R_{2k}$ detached-Rosser $2$-cycle geometry, retargeted
as the Pass-117 plateau-join question.

## MacNeille frontier pair and the frontier-onto criterion (Pass 118)

Let $L$ be a finite bounded poset, $\boxtimes$ antitone, $\widehat L$ its
Dedekind–MacNeille completion, and $\widehat{\boxtimes}(C)=(\boxtimes[C])^{\ell}$
the antitone extension (agreeing with $\boxtimes$ on principal cuts:
$\widehat{\boxtimes}(\mathord\downarrow a)=\mathord\downarrow\boxtimes a$).

The **frontier pair** of a non-principal cut $w\in\widehat L$ is
$(F,G)$ with **lower frontier** $F=\max(w\cap L)$ and **upper frontier**
$G=\min\{a\in L:a\notin w,\ a\ \text{minimal upper bound of}\ w\}$, so that as
elements of $\widehat L$,
$$
w=\bigvee F=\bigwedge G .
$$
(For the minimal example, the hexagon $H=\{0,x,y,m,n,U\}$, the sole non-principal
cut $w=\{0,x,y\}$ has $F=\{x,y\}$, $G=\{m,n\}$.)

A map is **frontier-onto** at $w$ when $\boxtimes[F]=G$: the lower frontier is
sent exactly onto the upper frontier.  A **two-way frontier swap** additionally
has $\boxtimes[G]=F$.

**Frontier De Morgan law** (Lemma 118a): $\widehat{\boxtimes}(w)=\bigwedge_{f\in
F}\boxtimes f$.  **Frontier-onto criterion** (Thm 118b): $w$ is
$\widehat{\boxtimes}$-fixed iff $\boxtimes[F]=G$ — **no carrier fixed point
$p=\boxtimes p$ is required**.

A **completion-generated self-dual seed** (equivalently **phantom fixed cut**) is
a non-principal $\widehat{\boxtimes}$-fixed cut $w$ on a carrier with
$\mathrm{Fix}(\boxtimes)=\varnothing$; by Thm 118b these exist (hexagon,
$\boxtimes 0=U,\boxtimes x=m,\boxtimes y=n,\boxtimes m=y,\boxtimes n=x,\boxtimes
U=0$).  Their existence refutes the strict form of Pass-117 Thm 117c: the
self-dual seed of the antitone Tarski interval can be a MacNeille cut, not a
carrier Jeroslow point.  Orbit **parity is not the operative invariant** (the
realizing orbits are the even $4$-cycle $(x\,m\,y\,n)$ and the even double
$2$-cycle); the operative datum is frontier routing $\boxtimes[F]=F$ (collapse to
$\bot$) versus $\boxtimes[F]=G$ (fixed).  See
`research/notes/g2-fg2-hierarchy.md` (Pass 118), `code/scripts/check-pass118.py`
-> `artifacts/reports/pass118-completion-generated-selfdual-seed-check.json`.

## Meet-generator, $\mu(w)$, and the meet criterion (Pass 119)

Let $w$ be a non-principal cut with frontier pair $(F,G)$ (so
$w=\bigvee F=\bigwedge G$; see the Pass-118 entry above).

A **meet-generator** of $w$ is a subset $G'\subseteq G$ with $\bigwedge G'=w$.
The **minimal meet-generator size** is
$$
\mu(w)=\min\{\lvert G'\rvert:\ G'\subseteq G,\ \textstyle\bigwedge G'=w\}\in\{2,\dots,\lvert G\rvert\}.
$$
$w$ is **meet-irredundant** when $\mu(w)=\lvert G\rvert$ (only $G$ itself
generates the meet) and **meet-redundant** when $\mu(w)<\lvert G\rvert$.  The
hexagon cut $w=\{0,x,y\}$ is meet-irredundant ($\mu=2=\lvert G\rvert$); the
triple-crossing cut $w=\{0,f_1,f_2,f_3\}$ of the complete bipartite carrier
$K_{3,3}^{0,U}$ is meet-redundant ($\mu=2<3=\lvert G\rvert$, since any two of
$g_1,g_2,g_3$ already meet to $w$).

The **meet criterion** (Thm 119b) is the exact, $\lvert F\rvert$-independent form
of the fixed-cut condition: for antitone $\boxtimes$, $w$ is
$\widehat{\boxtimes}$-fixed **iff** $\bigwedge_{f\in F}\boxtimes f=w$ (i.e.
$\bigwedge\boxtimes[F]=w$).  Its sharp reformulation (Thm 119c,
**meet-generation criterion**): $w$ is fixed **iff**
$\lvert\boxtimes[F]\cap G\rvert\ge\mu(w)$.  Hence the Pass-118 **frontier-onto**
condition $\boxtimes[F]=G$ is *sufficient always* but *necessary iff $w$ is
meet-irredundant*: at a meet-redundant triple crossing $\boxtimes$ may fix $w$
while sending some $f_i$ to a non-frontier element (e.g. the top $U$).  The
**meet-generator hypergraph** $H(w)=\{G'\subseteq G:\bigwedge G'=w\}$ is the
antichain-closed family recording all generators; $\mu(w)$ is its minimal
edge size.  See `research/notes/g2-fg2-hierarchy.md` (Pass 119),
`code/scripts/check-pass119.py` ->
`artifacts/reports/pass119-triple-crossing-frontier-meet-criterion-check.json`.
Compare the meet-irredundant/Löb versus meet-redundant/Rosser-economy reading of
[[integral-vs-non-integral-unit-loeb-rosser]].

## Meet-generator hypergraph, $\mu$-spectrum, frontier slack, frontier meet-rigidity (Pass 120)

Retain the frontier pair $(F,G)$ of a non-principal MacNeille cut $w$
($w=\bigvee F=\bigwedge G$).

The **meet-generator hypergraph** is $H(w)=\{G'\subseteq G:\bigwedge G'=w\}$, an
**up-set** in $(2^{G},\subseteq)$ (if $\bigwedge G'=w$ and $G'\subseteq G''$ then
$w\le\bigwedge G''\le\bigwedge G'=w$); its minimal antichain $H_{\min}(w)$ is the
combinatorial hypergraph proper.  The **$\mu$-spectrum** is the multiset
$\{\lvert H'\rvert:H'\in H_{\min}(w)\}$, with $\mu(w)$ its minimum.  The
**frontier slack** of an antitone $\boxtimes$ at $w$ is
$s(w)=\lvert F\rvert-\mu(w)$, the number of $F$-images that may be wasted (sent
to $U$, repeated, or otherwise non-generating) while still fixing $w$.

**Frontier meet-rigidity** (Thm 120a): in ANY MacNeille completion, distinct
upper-frontier elements $g\ne g'$ satisfy $g\wedge g'=w$, and distinct
lower-frontier elements $c\ne c'$ satisfy $c\vee c'=w$.  Consequence (Cor 120b,
**correcting** the Pass-119 range $\mu\in\{2,\dots,\lvert G\rvert\}$): the range
collapses — $H_{\min}(w)=\binom{G}{2}$ is the complete graph and
$$
\mu(w)=2\quad\text{identically, for every non-principal MacNeille cut }(\lvert F\rvert,\lvert G\rvert\ge2).
$$
Meet-irredundant thus means exactly $\lvert G\rvert=2$.  The **realization**
question is therefore rigid-negative (Thm 120d): the only antichain hypergraphs
arising as $H_{\min}(w)$ are the complete graphs $K_n$; the $\mu$-spectrum is the
constant multiset $\{2,\dots,2\}$ and the hypergraph is determined by
$\lvert G\rvert$ alone, not a free invariant.  On the asymmetric carrier
$K_{2,3}^{0,U}$ ($\lvert F\rvert=2$, $\lvert G\rvert=3$) the slack is $s(w)=0$,
forcing every fixing $\boxtimes$ to inject $F$ onto a distinct $g$-pair.  See
`research/notes/g2-fg2-hierarchy.md` (Pass 120), `code/scripts/check-pass120.py`
-> `artifacts/reports/pass120-asymmetric-frontier-meet-rigidity-check.json`.
The Rosser-economy reading (Rem 120f): the minimal witness budget of a
completion-generated Henkin/Rosser cut is always $2$; see
[[integral-vs-non-integral-unit-loeb-rosser]].

## Completion-relative $\mu(w)$, the filter completion, and meet-density vs meet-freedom (Pass 121)

The meet-generator hypergraph $H_{\min}(w)$, the $\mu$-spectrum, and $\mu(w)$
(Pass 120) are **completion-relative** invariants: they depend on the ambient
completion $C\supseteq L$ in which the non-principal element $w$, its frontier
pair $(F,G)$, and the meets $\bigwedge_C G'$ are computed.  Pass 120's frontier
meet-rigidity ($g\wedge g'=w$, $\mu(w)=2$) is a theorem about the **MacNeille**
completion (equivalently, by Thm 121b, the **canonical extension** $L^{\delta}$,
which for a finite poset coincides with MacNeille because every filter/ideal of a
finite poset is principal).

Three completions of a bounded poset $L$ (all embedding $L$ order-faithfully):
- **MacNeille $\overline L$** (Dedekind cuts): the unique completion in which $L$
  is *both* join- and meet-dense; smallest dense completion.
- **Ideal / downset completion $\mathcal D(L)$**: all down-sets of $L$ under
  inclusion; join $=$ union, **meet $=$ intersection**; $L$ is *join-dense* only.
  Free on joins.
- **Filter / upset completion $\mathcal F(L)$** (order-dual of $\mathcal D$): all
  up-sets of $L$ under **reverse inclusion**; $x\mapsto\mathord\uparrow x$;
  **meet $=$ union of up-sets**, join $=$ intersection; $L$ is *meet-dense* only.
  Free on meets.

A frontier is **meet-dense** in $C$ when its meets are inherited from $L$ (no new
intermediate element between $w$ and a coatom fan) and **meet-free** when $C$
adjoins the free meets of the frontier.  **Completion-relativity of frontier
rigidity** (Thm 121a): on $K_{2,3}^{0,U}$, $w$'s upper frontier is meet-dense in
MacNeille and in $\mathcal D(L)$ (so $g_i\wedge g_j=w$, $\mu(w)=2$, $H_{\min}=K_3$
rigid), but meet-**free** in $\mathcal F(L)$, where $g_i\wedge_{\mathcal F}g_j=
\mathord\uparrow g_i\cup\mathord\uparrow g_j=\{g_i,g_j,U\}$ are distinct new
elements strictly above $w$, so the ONLY meet-generator is the full frontier:
$H_{\min}(w)=\{G\}$ is $\lvert G\rvert$-uniform and $\mu(w)=\lvert G\rvert$.

**Frontier unfreezing law** (Thm 121c): for $L=K_{n,m}^{0,U}$ each one-sided
completion unfreezes exactly one frontier of $w$ — the meet-free filter
completion gives $\mu(w)=m$ (upper frontier a free meet-semilattice), the
join-free ideal completion gives dual join-multiplicity $n$ while keeping the
meet frontier rigid ($\mu(w)=2$); only MacNeille/$L^{\delta}$, dense on both
sides, freezes both to $\mu=2$.  Thus Pass 120's realization-negative theorem
("only complete graphs $K_n$") is a MacNeille/canonical statement; over
$\mathcal F(L)$ the $\ge3$-uniform hyperedge is realized.  Arithmetic reading
(Rem 121d): pairwise-join collapse of the consistency-like lower frontier
($f_i\vee f_j=w$, the $\mathrm{Con}^{\mathrm{orb}}$-tower shadow of Pass 69) is a
property of **meet-density** (the Lindenbaum both-dense completion), not of the
bare consistency order.  See `research/notes/g2-fg2-hierarchy.md` (Pass 121),
`code/scripts/check-pass121.py` ->
`artifacts/reports/pass121-completion-relative-frontier-rigidity-check.json`.
Compare [[integral-vs-non-integral-unit-loeb-rosser]] (meet-density $=$ Löb
economy) and the MacNeille-vs-ideal completion dichotomy of Pass 57.

## True frontier vs distinguished family; frontier meet-density; independent Rosser twins (Pass 122)

Pass 122 separates two families that Passes 120-121 silently conflated, and this
distinction is what makes "completion-relativity" (Pass 121) precise.

- **True frontier.** For a non-principal $w$ in a completion $C$, the **true upper
  frontier** is $G_*(w)=\min\bigl((w)^{u_C}\setminus w\bigr)$ — the *genuine minimal
  upper bounds of $w$ inside $C$* — and dually the **true lower frontier**
  $F_*(w)=\max\bigl((w)^{\ell_C}\setminus w\bigr)$.
- **Distinguished family.** A **distinguished coatom family** $G=\{g_1,\dots,g_m\}$
  is any antichain in $L$ carried up into $C$ and *declared* to be the frontier of
  interest.  The **distinguished-family meet-generator hypergraph** is
  $H_{\min}^{G}(w)=\{$minimal $S\subseteq G:\bigwedge_C S=w\}$; the true-frontier one
  is $H_{\min}^{G_*}(w)$.  Pass 120/121 wrote $H_{\min}(w)$ for $H_{\min}^{G}$ with
  $G=$ the carrier coatoms.

**Frontier meet-density (the exact invariant, Thm 122d).** $C$ is **meet-dense at
$w$** (relative to $G$) when no element of $C$ lies strictly between $w$ and any
$g\in G$; equivalently $G=G_*(w)$.  Then $H_{\min}^{G}(w)=H_{\min}^{G_*}(w)$.

**True-frontier rigidity is unconditional (Thm 122a).** For the *true* frontier,
$g\wedge_C g'=w$ ($g\ne g'\in G_*$) and $c\vee_C c'=w$ ($c\ne c'\in F_*$) in
**every** completion — an order-theoretic fact (a strict meet $z=g\wedge g'>w$ would
satisfy $z<g$, contradicting minimality of $g$), needing no density hypothesis.
Hence $H_{\min}^{G_*}(w)=K_{\lvert G_*\rvert}$ and $\mu_*(w)=2$ always.  So Pass 121's
"completion-relativity" is entirely the gap $H_{\min}^{G}\ne H_{\min}^{G_*}$ opened
when a distinguished $g$ is demoted below the true frontier (as in $\mathcal F(L)$,
where $z_{ij}=g_i\wedge g_j$ separates $g_i$ from $w$).

**Distinguished-family realization is universal (Thm 122c).** Every finite antichain
hypergraph $H$ on $[m]$ equals $H_{\min}^{G}(w)$ for a non-principal $w$ in the ideal
completion of an explicit carrier: atoms $=$ core $\{c_1,c_2\}$ plus one fan $x_I$
per maximal $H$-independent $I\subseteq[m]$, $x_I<g_j\iff j\in I$; then
$\bigwedge_{j\in S}g_j=w\iff S\supseteq$ an $H$-edge.  Atom cost
$2+\lvert\mathrm{MaxInd}(H)\rvert$.  Thus $H_{\min}^{G}$ is a *free* invariant while
$H_{\min}^{G_*}$ is rigid.

**Independent Rosser twins / antichain-frontier phantom (Rem 122f).** The
non-principal $w$ whose lower frontier $F_*$ is an antichain $\{c_1,c_2\}$ of
*order-incomparable* Rosser-type consistency sentences (distinct witness-orderings,
neither $T$-provably below the other) with Henkin disjunction $c_1\vee c_2=w$.  It is
the arithmetic carrier of the pairwise-join collapse $f_i\vee f_j=w$ — as opposed to
the $\mathrm{Con}^{\mathrm{orb}}_n$ **chain** tower (Pass 69), which is frontierless
and whose pairwise joins are maxima $<$ limit in every completion, so no completion
condition makes them collapse.  This *refutes* the Rem 121d identification of the
frontier with the consistency tower.  See `research/notes/g2-fg2-hierarchy.md`
(Pass 122), `code/scripts/check-pass122.py` ->
`artifacts/reports/pass122-two-sided-realization-check.json`.

## Rosser bouquet: cross vs swap, seeded vs seedless center, atom cost $\alpha(H)$ (Pass 123–124)

- **Rosser bouquet / antichain-frontier phantom.** A non-principal cut (or carrier
  join) $w$ whose lower frontier is a $\ge2$-antichain $\{c_1,c_2\}$ of
  order-incomparable Rosser-type consistency twins with $c_1\vee c_2=w$ the
  Henkin/Rosser disjunction.
- **Cross map vs front-internal swap (Thm 123a).** On the Pass-117 hexagon the
  MacNeille $\wid

## Rosser box relative to a tag order; $N$-adequacy; weak-consistency; certified-linearity bit (Pass 138)

- **Rosser box relative to a tag order $\Box_R^{\prec}$.** For a $T$-definable strict
  order $\prec$ with a $\prec$-least element,
  $\Box_R^{\prec}x:=\exists p[\mathrm{Prf}(p,x)\wedge\forall q\prec p\,\neg\mathrm{Prf}(q,\dot\neg x)]$.
  Satisfies Rosser-$D1$ and provable Rosser consistency $T\vdash\neg\Box_R^{\prec}\bot$;
  in general fails $D2$ (non-monotone).
- **$N$-adequacy of a provability predicate (Lemma 138b).** A predicate $\Pi$ is
  $N$-adequate for $T$ if $\mathbb N\models\Pi(\ulcorner C\urcorner)\iff T\vdash C$.
  Every Rosser box $\Box_R^{\prec}$ is $N$-adequate for consistent $T$, independently
  of $\prec$; hence any $D2$-failure of $\Box_R^{\prec}$ is invisible in $\mathbb N$
  and lives only in nonstandard models of $T+\neg\mathrm{Con}_T$.
- **Rosser weak-consistency principle $\mathrm{WC}$.** The modal schema
  $\mathrm{WC}(X):=\neg(\Box_R X\wedge\Box_R\neg X)$. Valid in every consistent
  *linear* Rosser frame; refuted by a *partial-order* frame (incomparable minimal
  proofs of $X$ and $\neg X$). By Thm 138c(b), $\mathrm{WC}\in\mathrm{PL}_T(\Box_R^{\prec})
  \iff T\vdash\mathrm{Lin}(\prec)$.
- **Certified-linearity bit.** The single Boolean "$T\vdash\mathrm{Lin}(\prec)$" that
  the provability logic $\mathrm{PL}_T(\Box_R^{\prec})$ detects (via $\mathrm{WC}$).
  The $I\Sigma_n$ tag-growth rank (Thm 137d) affects $\mathrm{PL}$ *only* through this
  bit; above the threshold $\mathrm{PL}$ is the single Guaspari–Solovay Rosser logic
  for every order-type-$\omega$ tag order (Thm 138c(a)).ehat\boxtimes$ obeys the antitone De Morgan law
  $\widehat\boxtimes(c_1\vee c_2)=\boxtimes c_1\wedge\boxtimes c_2$.  The **cross map**
  ($\boxtimes c_1=m,\boxtimes c_2=n$, images strictly ABOVE the summands) FIXES the cut
  ($m\wedge n=w$); the **front-internal swap** ($\boxtimes c_1=c_2,\boxtimes c_2=c_1$)
  collapses it to $\bot$.  Census: $477$ antitone maps, $22$ fix (all seedless), $38$
  collapse.
- **Completion-manufactured (seedless) center.** A $\widehat\boxtimes$-fixed cut $w=w$
  in the completion with NO carrier Jeroslow point $p=\boxtimes p$ ($\mathrm{Fix}_C(
  \boxtimes)=\varnothing$).  All $22$ hexagon fixing maps are seedless (Thm 123a):
  the odd self-dual seed of Thm 117c is a property of the completion, not the carrier.
- **Seeded center / carrier-join criterion (Thm 124a).** When the disjunction
  $c_1\vee c_2=w$ is a GENUINE carrier join (e.g. the six-element lattice
  $L^\ast=\{0<c_1,c_2,p;\ c_1,c_2<w;\ w<U;\ p<U\}$), the center can be a CARRIER fixed
  point $\boxtimes w=w$, optionally alongside a detached seed $p=\boxtimes p$
  ($p\parallel\{c_1,c_2,w\}$) — a **seeded bouquet-with-center**.  The center is
  carrier-seeded **iff** the bouquet disjunction exists in the carrier; since
  $\mathrm{ConLat}_T$ is Boolean, $\rho_1\vee\rho_2$ always exists, so the arithmetic
  bouquet is always seeded.
- **Separated vs fused twins; normal (De-Morgan) $\boxtimes$ (Thm 124b).** Twins are
  **$\boxtimes$-separated** when $\boxtimes c_1\ne\boxtimes c_2$ (independently
  witnessed), **fused** otherwise.  A **normal** $\boxtimes$ is an antitone lattice
  dual-endomorphism ($\boxtimes(a\vee b)=\boxtimes a\wedge\boxtimes b$ and dually) — the
  abstract shadow of $D2$.  On $L^\ast$, normal $+\ \boxtimes w=w\Rightarrow$ FUSED
  twins ($17$ normal maps, $4$ fix $w$, $0$ separated); a separated seeded
  bouquet-with-center exists only in the $\neg D2$ regime.  ($\mathrm{Fix}(\boxtimes)$
  is always an antichain, Lemma 51a.)
- **Atom cost $\alpha(H)$ and the phantom tax (Thm 123d, Cor 124d).**
  $\alpha_{\mathrm{phantom}}(H)=2+\lvert\mathrm{MaxInd}(H)\rvert$ (non-principal,
  genuine bouquet) and $\alpha_{\mathrm{principal}}(H)=1+\lvert\mathrm{MaxInd}(H)\rvert$
  (principal $w$, twins fused).  The **phantom tax** is their difference, $=1$ for EVERY
  $H$: fan atoms shared, only the core differs $1\to2$; connectedness of the
  independence complex changes $\lvert\mathrm{MaxInd}\rvert$ but not the tax.
  See `research/notes/g2-fg2-hierarchy.md` (Pass 123–124),
  `code/scripts/check-pass124.py` ->
  `artifacts/reports/pass124-odd-seed-bouquet-with-center-check.json`.

## Goblot cofinality-rank vs nerve cohomological dimension; $nFG2(n)$ derived-limit avatar (Pass 140)

- **Goblot cofinality-rank of an index poset.** For an inverse system indexed by a
  directed poset $P$ with $\mathrm{cf}(P)=\aleph_r$, Goblot's theorem gives
  $\varprojlim^n=0$ for all $n\ge r+2$; call $r$ the **Goblot cofinality-rank**. For
  the Mardešić–Prasolov index $P=(\omega^\omega,\le^*)$ one has $\mathrm{cf}(P)=
  \mathfrak d\ge\mathfrak b\ge\aleph_1$, so $r\ge1$ and the vanishing threshold is
  $\ge3$ in every model of ZFC.
- **Nerve cohomological dimension $\mathrm{cd}$ vs Goblot rank (Thm 140a).** The
  cohomological dimension $\mathrm{cd}$ of a coherence datum's *nerve* (a Čech/sheaf
  invariant of a simplicial complex; e.g. $\mathrm{cd}(A^{(a),k})=k$ exact, Thm 136a)
  is a **different, decoupled** invariant (Thm 136c) from the Goblot cofinality-rank
  that governs $\varprojlim^*$ of the same tower re-indexed over $\omega^\omega$. A
  graph-nerve $\mathrm{cd}\le1$ therefore does **not** bound the set-theoretic
  $\varprojlim^{\ge2}A$: the only ZFC vanishing is Goblot's, keyed to index
  cofinality, never $\le2$ for an uncountable-cofinality index. (This refutes the
  Thm-139b Horn-I collapse $(\forall n)h_n\Leftrightarrow h_1$.)
- **Derived-limit avatar of $nFG2(n)$.** The higher derived limit $\varprojlim^n A$
  is the set-theoretic avatar of $nFG2(n)$ ($\boxtimes^{n+1}T\le\boxtimes^n T$): its
  *orbit index* is the directed poset $P$, and the Goblot truncation depth
  $\mathrm{cf\text{-}rank}(P)+1$ is the analogue of the finite antitone orbit's
  self-truncation depth (Thm 41a, $=2$ for a well-founded/linear index). For
  $P=(\omega^\omega,\le^*)$ (uncountable, non-well-founded) the truncation depth is
  **unbounded**, so $nFG2(n)$ descends strictly for cofinally many $n$
  ($nFG2(2)\not\Rightarrow nFG2(1)$) — the continuum-indexed antipode of Thm 41a.
  See `research/notes/g2-fg2-hierarchy.md` (Pass 140), `code/scripts/check-pass140.py`
  -> `artifacts/reports/pass140-horn-a-goblot-vs-nerve-cd-check.json`.

## Transfinite diagonal, depth-$\omega$ collapse, and the phantom uncertainty principle (Pass 141)

- **Suspension-telescope diagonal $A^{(a),\omega}_{\mathrm{tel}}$.** The directed
  colimit $\varinjlim_k A^{(a),k}$ of the $\mathrm{cd}$-graded sphere tower along the
  equatorial suspensions $\sigma_k:S^k\hookrightarrow S^{k+1}$ (avatar $S^\infty$).
  Since $\sigma_k$ is $0$ on the top class $\tilde H_k$, the homology tower is
  degreewise eventually-zero, hence Mittag–Leffler, hence $\varprojlim^n_{\mathrm{tel}}
  = 0$ for all $n$ (**depth-$\omega$ collapse**, Thm 141a): the telescoped
  $\boxtimes$-tower self-truncates to the trivial object — the transfinite echo of
  Thm 41a's finite depth-2 collapse. Contrast the **coproduct diagonal**
  $\bigoplus_k A^{(a),k}$, whose $\varprojlim^n$ is the phantom-additive *union* of the
  finite levels (Prop 141b), not a single class.
- **Cofinal ($cd=\omega$) phantom / $nFG2(\omega)$.** An inverse system with a SINGLE
  index for which $\varprojlim^n\ne0$ cofinally in $n$; the derived-limit avatar of a
  $\boxtimes$-consistency tower descending through every finite $\boxtimes^k T$ without
  stabilising. By Goblot (index-intrinsic, Thm 141c) it requires **unbounded**
  cofinality-rank, i.e. index cofinality $\ge\aleph_\omega$, equivalently
  $2^{\aleph_0}\ge\aleph_{\omega+1}$ (BLH ceiling $\varprojlim^n\ne0\Rightarrow
  \mathfrak c\ge\aleph_{n+1}$, plus König). No cofinal phantom exists at bounded index
  cofinality — no coefficient/twist evades Goblot.
- **Phantom uncertainty principle (Cor 141d).** A genuine $nFG2(\omega)$ [home
  $\mathfrak c\ge\aleph_{\omega+1}$] and the sharp level-2 separator $h_1(A)\wedge
  \varprojlim^2 A^{(a),2}\ne0$ [home $\mathfrak c=\aleph_2$] are mutually exclusive in
  any one model: the continuum resolves the phantom sharply at level 2, or follows it
  to $\omega$, never both at one cut.
- **$\mathrm{MA}_{\aleph_1}$ level-1 discharge (Cor 141e).** $\mathrm{MA}_{\aleph_1}$
  ALONE (not PFA) forces $\varprojlim^1 A=0$ at $2^{\aleph_0}=\aleph_2$: the level-1
  trivialising poset is $\sigma$-centered and needs only $\aleph_1$ dense sets; the
  same axiom does not vanish $\varprojlim^2$, so the level-2 separator survives.
  See `research/notes/g2-fg2-hierarchy.md` (Pass 141), `code/scripts/check-pass141.py`
  -> `artifacts/reports/pass141-cd-omega-diagonal-nfg2omega-check.json`.

## $\pi$-classified system, fibre-acyclic projection, bad part $\Lambda_{\mathrm{bad}}$, oriented bad point / Rosser torsor (Pass 145)

- **$\pi$-classified cover-fiber system / fibre-acyclic projection.** For fixed $n\ge 2$
  and the coordinate projection $\pi_\mu:[\mu]^{<\omega}\to[\omega_{n+1}]^{<\omega}$,
  $X\mapsto X\cap\omega_{n+1}$, the CLH system $A_\mu[\mathbb Z]$ is **$\pi$-classified**
  when $A_\mu[\mathbb Z]\cong\pi_\mu^*B[\mathbb Z]$ for a $\mu$-independent base
  $B[\mathbb Z]$; $\pi_\mu$ is **fibre-acyclic** when every fibre $\pi_\mu^{-1}(Y)$ is
  up-directed (closed under finite unions, $(\cdot)\cap\omega_{n+1}$ being a
  $\cup$-homomorphism), forcing $\varprojlim^{\ge 1}$ over each fibre to vanish. Under both,
  the Bousfield–Kan/Roos spectral sequence collapses ($E_2^{p,q\ge 1}=0$) to the edge iso
  $\varprojlim^n_{[\mu]}A_\mu\cong\varprojlim^n_{[\omega_{n+1}]}B$ (Thm 145a): the $n\ge 2$
  window pro-isomorphism is a consequence of FINALITY, not extra structure.
- **Bad part of the pcf spectrum $\Lambda_{\mathrm{bad}}$.** $\Lambda_{\mathrm{bad}}=
  \{\mu\in\Lambda:S_\mu\text{ is not a good scale}\}$, the $\mu$ whose scale $S_\mu$ has a
  stationary set of bad points (no exact upper bound / non-approachable). The level-1
  phantom is nonzero exactly on $\Lambda_{\mathrm{bad}}$ ($\Phi^1_\mu\ne 0\iff\mu\in
  \Lambda_{\mathrm{bad}}$, Thm 145c); $\Lambda_{\mathrm{bad}}=\varnothing$ (AP /
  very-good-scale) and $\Lambda_{\mathrm{bad}}=\Lambda$ ($\neg$AP / tree property) are both
  consistent, so faithfulness of the level-1 stratification is approachability-conditional.
- **Oriented bad point / Rosser torsor.** A bad point $\alpha$ of $S_\mu$ carries the
  $\mathbb Z/2$-torsor $\mathrm{Or}(\alpha)$ of witnessing cofinal sequences mod finite,
  with sign local system $\mathrm{sgn}_\alpha$ of monodromy $\pm 1$: **Rosser-oriented**
  (Möbius, monodromy $-1$, $H^0(\mathrm{sgn})=0$) $\leftrightarrow$ detached Rosser fixed
  point / non-integral unit; **symmetric** (trivial, $H^0=\mathbb Z/2$) $\leftrightarrow$
  Kripke–Feferman unoriented fixed point; good/eub $\leftrightarrow$ Löb orbit-attached
  fixed point / integral unit (Thm 145d, the transfinite lift of the Pass-51/53
  integral-unit dictionary). See `research/notes/g2-fg2-hierarchy.md` (Pass 145),
  `code/scripts/check-pass145.py` ->
  `artifacts/reports/pass145-thm144a-obligation-discharge-check.json`.

## Pointwise vs schematic orientation, schematic $Z/2$ from recursively-inseparable proof orders, reflection phantoms, and $\delta=$ Spanier–Whitehead antipode (Pass 149)

- **Pointwise vs schematic orientation signature (Def 149.0).** For $\boxtimes=\neg\mathrm{Prov}_T$
  and a $\Sigma_1$ (possibly non-$\Delta_0$) proof order, $H^0_{\mathrm{pt}}(\mathrm{sgn})(\rho)$ is
  the reduced sign-cohomology of a single realized fixed point $\rho$'s race
  $\{\rho,\neg\rho\}$; $H^0_{\mathrm{sch}}(\mathrm{sgn})$ is the Čech $H^0$ of the sign local system
  over the DIAGRAM $\mathrm{Real}(\boxtimes)$ of all realizations. A signature is
  **$\Sigma_1$-pointwise** if $H^0_{\mathrm{pt}}$ comes from a $\Sigma_1$ order, and
  **$\Sigma_1$-schematic** if $H^0_{\mathrm{sch}}$ does.

- **Pointwise eliminability of $\Delta_0$-linearity (Thm 149a).** Every realized detached fixed
  point is oriented ($(Z,0)$), because its singleton race involves two standard proof codes $p,q$
  with $p<q$ decidable on that pair; a non-terminating race is a degenerate oriented (empty-section)
  stalk, not a gap. So "$\Delta_0$ linear proof order" is eliminable from Thm 148a at the level of
  points.

- **Schematic $Z/2$ / recursively-inseparable proof order (Thm 149b).** A recursively-inseparable
  c.e. pair $(A,B)$ (e.g. Kleene $\{e:\phi_e(e)=0/1\}$) codes a $\Sigma_1$ proof order that is
  SCHEMATICALLY unorientable (a uniform $\Sigma_1$ selector would separate $A,B$) yet carries a
  genuine $\boxtimes$-fixed sentence. Its $Z/2$ lives in $H^0_{\mathrm{sch}}$, one level above any
  point. Hence $(Z,Z/2)$ is **$\Sigma_1$-schematic but not $\Sigma_1$-pointwise**: Thm 148b
  preserved and sharpened; the pointwise gap forces KF ascent.

- **Reflection phantom / SW antimatter $-\langle n\rangle$ (Thm 149c, Path. 149e).**
  $GLP^+=(\mathbb N,+)$ is the free commutative monoid on $\langle 1\rangle$, has no inverses for
  $n>0$ (Ignatiev well-order), so is NOT a group; $K_0=\mathbb Z$. The Spanier–Whitehead dual
  $S^{-n}\leftrightarrow-\langle n\rangle$ supplies negatives that are **reflection phantoms**: no
  reflection principle has strength "$-n$-consistency" ($\Pi$-conservativity is conservation
  $\langle n\rangle\to 0$, a morphism, not an additive inverse). $GLP$ is chiral.

- **$\delta=$ Spanier–Whitehead antipode (Thm 149d).** The De Morgan orientation flip $\delta$ and
  the SW antipode $D:S^n\mapsto S^{-n}$ are ONE order-2 involution $s:k\mapsto -k$ on $K_0=\mathbb Z$,
  fixed locus $\{0\}=S^0=T$-floor, free off it. The KF gap cocycle $H^0(\mathrm{sgn})=Z/2$ is the
  equivariant class of the free part; orientation is a ground-floor phenomenon because $s$ fixes
  only $\langle 0\rangle$; the only $\delta$-symmetric grade is the floor, which cannot host a
  detached fixed point, forcing the symmetric $(Z,Z/2)$ to be gapped (KF), not oriented (Rosser).
  The phantom POINT upstairs ($\varprojlim^1=\hat{\mathbb Z}_m/\mathbb Z$) and phantom ANTIMATTER
  downstairs ($-\langle n\rangle$) are $s$-conjugate.

## $\Sigma_1$-orientation dichotomy, tie-break, depth-addition monoidal law, and the restriction retraction (Pass 148)

- **Tie-break / orientation of a fixed point.** A **tie-break** $R$ for a detached
  $\boxtimes$-fixed point $\kappa$ is a relation on $\{$proofs of $\kappa\}\times\{$proofs of
  $\neg\kappa\}$ deciding $\Box\kappa$ by witness comparison. The **orientation double cover**
  $\mathrm{Or}(\kappa)$ has monodromy $\mathrm{sgn}(R\text{ vs }\delta R)$; $R$ **orients** $\kappa$
  iff $\delta R\ne R$ (monodromy $-1$, connected cover, $H^0(\mathrm{sgn})=0$).

- **$\Sigma_1$-orientation dichotomy (Thm 148a).** Any $\Sigma_1$ box with a $\Delta_0$ linear
  proof order $\prec$ makes the Rosser tie-break $R_\prec$ total and antisymmetric, so
  $\delta R_\prec=R_{\prec^{op}}\ne R_\prec$: **every** detached $\Sigma_1$ fixed point is oriented
  ($(Z,0)$, Rosser). The symmetric $(Z,Z/2)$ needs a $\delta$-fixed tie-break; the unique such is
  the undirected **truth-gap** valuation, which is not $\Sigma_1$. Slogan: *the orientation is the
  proof-order; the symmetry is the gap.*

- **Arithmetic-restriction retraction $r$ (Thm 148b).** $r:\mathrm{ConLat}_{KF}\to
  \mathrm{ConLat}_{PA}$ sends $[\varphi]$ to the class of its arithmetic consequences. $\kappa\in
  L_{Tr}$ does not literally sit in $\mathrm{ConLat}_{PA}$; $r([\kappa])$ is a still-detached but
  **re-oriented** $(Z,0)$ shadow (the gap collapses under two-valued restriction,
  $H^0(\mathrm{sgn}):\mathbb Z/2\to0$). Hence $(Z,Z/2)$ is intrinsically non-$\Sigma_1$
  (needs KF, ordinal $\varphi_{\varepsilon_0}(0)$).

- **Depth-addition monoidal law (Thm 148c).** On the target $\mathrm{GLP}^+=(\langle n\rangle)$,
  the monoidal law matching the smash $S^n\wedge S^m=S^{n+m}$ is
  $\langle n\rangle*\langle m\rangle:=\langle n+m\rangle$ (Ignatiev normal-form **depth-addition**),
  NOT conjunction. Conjunction is idempotent ($\langle1\rangle\wedge\langle1\rangle=\langle1\rangle$)
  and collapses the frozen strictness $\langle2\rangle\not\sim\langle1\rangle$; it is the wedge/
  additive law on $\vee$, not on $\wedge$. Beklemishev's reduction
  $\langle n+1\rangle\equiv\langle n\rangle^\omega$ is an **internal coherence iso** of the target,
  not part of the monoidal data; the first transfinite coherence stage $S^\omega=\mathrm{holim}_n
  S^n$ maps to the first limit modality $\langle\omega\rangle$ of $\mathrm{GLP}_\Lambda$.

## Kripke–Feferman consistency fixed point, orientation double cover, the `Coh` functor, and Feferman–Spector path-dependence (Pass 147)

- **Kripke–Feferman consistency fixed point `kappa`.** Over c.e. $T\supseteq\mathrm{EA}$ in the
  strong-Kleene KF closure with partial truth predicate $\mathrm{Tr}$, put
  $\Box_{\mathrm{KF}}\varphi=\mathrm{Tr}(\dot{\ulcorner}\mathrm{Prov}_T\varphi\urcorner)$,
  $\boxtimes=\neg\Box_{\mathrm{KF}}$, and diagonalize $\kappa=\boxtimes\kappa$. The
  self-referential "I am not KF-provable."

- **Ungrounded $=$ detached.** A sentence is **grounded** if it enters the extension or
  anti-extension of the minimal Kripke fixed point at some ordinal stage. Groundedness is a
  $\equiv_T$-invariant. The consistency iterates $c_n=\boxtimes^n T$ are grounded (finite stage);
  $\kappa$ is **ungrounded**, hence $\kappa\not\equiv_T c_n$ for all $n$ (**detached**, Pass 42):
  $\varprojlim^1=\widehat{\mathbb Z}_m/\mathbb Z\ne0$, $H^1=\mathbb Z$.

- **Orientation double cover and $H^0(\mathrm{sgn})$.** The orientation $\mathbb Z/2$-torsor
  $\mathrm{Or}(\kappa)$ of "which side of the truth-gap" has a double cover; define
  $H^0(\mathrm{sgn}):=\widetilde H^0(\mathrm{Or};\mathbb Z/2)=(\#\text{components}-1)\cdot\mathbb Z/2$.
  **Symmetric** ($\delta$-invariant, trivial torsor): cover splits, $2$ components,
  $H^0(\mathrm{sgn})=\mathbb Z/2$ (KF, Rosser-invisible). **Oriented** (Möbius, nontrivial torsor):
  cover connected, $1$ component, $H^0(\mathrm{sgn})=0$ (Rosser). Here $\delta$ is the De Morgan
  involution swapping extension/anti-extension; the strong-Kleene jump $\Gamma$ commutes with
  $\delta$, forcing $\kappa$ symmetric.

- **Coherence$\to$GLP functor `Coh` and reduction-as-suspension.**
  $\mathrm{Coh}([S^n])=\langle n\rangle\top$ ($n$-fold uniform reflection),
  $\mathrm{Coh}(\sigma_n)=$ Beklemishev's reduction
  $\langle n+1\rangle\top\equiv_T\langle n\rangle^\omega\top$. A graded monoid map (BK degree
  $\mapsto$ modality depth) faithful on generators on the positive cone; $H^n(S^n)=\mathbb Z$
  $\leftrightarrow$ strictness $\langle n\rangle\not\sim\langle n+1\rangle$. **First limit
  modality** $\langle\omega\rangle$ ($\mathrm{GLP}_\Lambda$): the reduction spends one $\omega$
  per degree bump, so the first limit is the $n{=}1\to2$ passage; $n=1\mapsto\langle1\rangle$
  (finite base), and $\langle\omega\rangle$ is the transfinite-coherence avatar.

- **Feferman–Spector path-dependence.** The $\omega$-th stage $T_\omega$ of a Turing–Feferman
  uniform-reflection progression is notation-path-dependent (Feferman 1962; Feferman–Spector
  1962): a proved recursion-theoretic non-uniqueness, the arithmetic image of a bad point's
  $\mathbb Z/2$-orientation, parallel to (not identified with) the set-theoretic
  non-absoluteness of approachability (Thm 145c). See `research/notes/g2-fg2-hierarchy.md`
  (Pass 147), `code/scripts/check-pass147.py` ->
  `artifacts/reports/pass147-kf-signature-glp-functor-check.json`.

## Phantom spectrum, Steinitz tower, twin-depth honesty, and pure-`Box`-inexpressibility (Pass 129)

- **Steinitz (supernatural) nesting tower and `Supp_infty`.**  The facet-nesting tower of a
  Rosser predicate is `T = (Z <-x m_1- Z <-x m_2- ...)`.  Its **Steinitz number** is
  `N = prod_n m_n = prod_p p^{e_p}` with `e_p in {0,1,...,infty}` the cumulative `p`-adic
  valuation, living in the **Steinitz monoid** `S = prod_p {0,...,infty}`.  The **infinite
  support** is `Supp_infty(N) = {p : e_p = infty}`.

- **Phantom functor `Phi` and the phantom spectrum.**  `Phi(T) = varprojlim^1 T = hatZ_N/Z`
  (Thm 54b: depends only on `N`).  The **phantom spectrum** is the map
  `Predicates -> S`, `Predicate |-> N`; its solenoidal (genuine `prod Z_p`) part is exactly
  `prod_{p in Supp_infty(N)} Z_p`.  Pass-129 Thm 129a: `Phi` is SURJECTIVE onto every
  squarefree radical via the `r`-ary race `r = prod_{p in S} p`; on the **uniform**
  (constant-arity, constant-overhead) subcategory `Phi` factors ABSOLUTELY through the
  squarefree radical lattice `P_fin(Primes)` (`Phi(p^k) = Phi(p)`, no `p`-power weighting),
  and `P_fin(Primes)` is EXACTLY the uniform image; escaping the lattice to a general
  Steinitz number requires a **depth-varying** race/overhead.

- **Purely finitary / adelic-torsion phantom.**  A phantom `Phi(T) != 0` with
  `Supp_infty(N) = emptyset` (no solenoidal `Z_p` component).  Pathology 129a' (P1): the
  **primorial race** `a_k = p_k` (each prime once) is non-ML with all `e_p = 1`, giving
  `Phi = (prod_p Z/p)/Z != 0` — honest at every prime individually, phantom collectively.
  An isolated finite `Z/p^k` summand is a MIRAGE (surjected and killed by the dense diagonal
  `Z`); a `p`-power-weighted phantom appears only as the finite coordinates of an `N` with
  nonempty `Supp_infty`.

- **Mittag-Leffler tail dichotomy.**  `Phi(T) = 0` iff `T` is Mittag-Leffler iff the tail
  multipliers are eventually units (`m_n in {1,-1}` for large `n`).  Pathology 129a' (P2):
  an eventually-IDENTITY race is honest (`Phi = 0`, "eventually-Löb is honest"); an
  eventually-CONSTANT-`2` race keeps `hatZ_2/Z`.  The phantom dies when the NON-UNIT
  multiplications cease, NOT when growth ceases.

- **Twin-depth honesty `h_n` and simultaneous honesty.**  `h_n :=` "`varprojlim^n` of the
  `aleph_1`-cofinal twin facet tower `= 0`" (Thm 128c `= h_1`).  Pass-129 Thm 129b:
  `(forall n) h_n <=>` strong-homology ADDITIVITY for the twin system (Mardešić-Prasolov
  1988); `h_1` does NOT decide `(h_n)_{n>=2}` (`h_1 ^ ¬h_2` consistent via `MA_{aleph_1}`),
  so honesty STRATIFIES by depth; **simultaneous honesty** `(forall n) h_n` — *[Corrected by
  Pass-130 Thm 130d: NOT a large-cardinal statement. The weakly-compact bound (BLH 2021) was
  only a first upper bound; Bergfalk-Hrušák-Lambie-Hanson removed the large cardinal, so
  `(forall n) h_n` is EQUICONSISTENT WITH ZFC, `2^aleph0 >= aleph_2` necessary. Still fails
  under `V=L`, `b=aleph_1`.]*

- **Pure-`Box`-inexpressibility (bisimulation certificate).**  A schema is
  **pure-`Box`-inexpressible** if no pure-`Box` formula defines it over the relevant frame
  class.  Pass-129 Thm 129c certifies this for `WO` (Pass 128) by two certificates:
  (I) two pointed models with IDENTICAL Box-reduct (pure-`Box`-equal at every depth,
  verified on all 206 depth-`<=4` formulas) differing only in `-<`, with `WO` and Löb
  separated; (II) reflexive singleton vs converse-ill-founded chain, fully bisimilar (so
  pure-`Box` cannot measure `R`-depth), both Löb-refuting.  Census: `68/68` serial+transitive
  frames on `3` worlds (`75` over `<= 3`) refute Löb, all reflexive-cyclic.
  See `research/notes/g2-fg2-hierarchy.md` (Pass 129), `code/scripts/check-pass129.py` ->
  `artifacts/reports/pass129-phantom-spectrum-simultaneous-honesty-inexpressibility-check.json`.

## Phantom divisibility, torsion = complement of `Supp_infty`, the semilattice phantom, graded Rosser predicate, and `WO = Loeb_{-<}` (Pass 130)

- **Phantom divisibility.**  `varprojlim^1(Z, x m_n) = hatZ_N/Z` is a **divisible** abelian
  group (Pass-130 Thm 130a): `ell`-divisible for every prime `ell` because
  `hatZ_N/ell.hatZ_N = A_ell/ell.A_ell` and the dense diagonal `Z` surjects onto it.
  **Consequence (Cor 130a.1):** no nonzero finite group is a direct summand — the Pass-129
  "isolated `Z/q^k` is a mirage" IS divisibility, unconditional in `N`.

- **Torsion detects the complement of `Supp_infty`.**  `Tor(hatZ_N/Z) = bigoplus_{q notin
  Supp_infty(N)} Z/q^inf` (rank-one Prüfer per non-solenoidal prime), and
  `(hatZ_N/Z)/Tor = Q^{(2^aleph0)}` (`= 0` iff `Supp(N)` finite).  The `q`-primary part
  vanishes iff `e_q = inf`; a finite prime (`e_q < inf`, INCLUDING `e_q = 0`) contributes one
  Prüfer `Z/q^inf`.  So the ISO-TYPE of the phantom depends only on `Supp_infty(N)` — every
  finite valuation is forgotten (a strengthening of the Pass-129 "no `p`-power weighting":
  even `e_q=0` vs `e_q=5` is invisible).  Finite primes die as SUMMANDS but survive as the
  divisible hull `Z/q^inf`.

- **Semilattice (idempotent) phantom / `Supp_infty` homomorphism.**  `Phi` is NOT a monoid
  hom into `(Ab,x)`; at iso-type it factors through `Supp_infty : (Steinitz, x) ->
  (P(Primes), cup)`, a SURJECTIVE monoid homomorphism onto the idempotent join-semilattice:
  `Supp_infty(N_1 N_2) = Supp_infty(N_1) cup Supp_infty(N_2)`, `Supp_infty(N^2) =
  Supp_infty(N)`.  Hence `Phi(N^2) = Phi(N)` — the phantom is **idempotent**, a semilattice
  not a group (`Box` a projection).  `P_fin(Primes)` = the uniform-race sub-semilattice.

- **Graded Rosser `Sigma_1` predicate.**  `Pr_{R,vec a}(x) := exists d [Proof_T(d,x) ^
  forall d' in B_{lev(d)} (d' Rosser-refutes x in the a_{lev(d)}-ary race => d <_lex d')]`,
  with `(a_k)` a recursive arity schedule and `B_1,B_2,...` disjoint recursive Gödel bands.
  `Sigma_1` with `Sigma_1`-independent layers (band disjointness), so its consistency-layer
  facet tower is exactly `(Z, x a_k)` and `varprojlim^1 = hatZ_{prod a_k}/Z`; the primorial
  schedule `a_k = p_k` realizes the primorial phantom by an ACTUAL predicate (Pass-130
  Constr 130c; obligations o1 [`D1^¬D2` uniform] and o2 [`ConLat`-tower honest] carried).

- **Non-normal neighborhood box (`D1 ^ ¬D2 ^ D3^hom`).**  A neighborhood model `(W, N, -<)`
  with `[Box]A` true at `w` iff `||A|| in N(w)`, where each `N(w)` contains `W` (`D1`) and is
  upward closed (`D3^hom = RM`) but NOT intersection-closed (`¬D2 = ¬K`).  The 3-world witness
  `N(w) = up{W, {0,1}, {0,2}}` has `{0,1} cap {0,2} = {0} notin N(w)`: the Guaspari-Solovay
  non-normality of a Rosser box (`Pr_R` obeys `D1`, `RM`, not `D2`).

- **`WO = Loeb_{-<}`.**  On any finite `-<`-frame the witness-race well-foundedness schema `WO`
  is EXACTLY the Löb schema for the `-<`-modality: `Box_{-<}(Box_{-<}p -> p) -> Box_{-<}p`
  valid iff `-<` transitive and converse-well-founded (no `-<`-cycle) iff `WO`.  So `WO` is not
  pure-`Box` (Pass-129 Thm 129c) but is the `GL`-axiom of the second modality, and the residual
  `PL(Box_R^A) = R+4` completeness lives in the bimodal `(Box, Box_{-<})` language.
  See `research/notes/g2-fg2-hierarchy.md` (Pass 130), `code/scripts/check-pass130.py` ->
  `artifacts/reports/pass130-phantom-divisibility-supp-inf-neighborhood-check.json`.

## Prufer-rank rigidity, strand-inflation, the honesty ceiling, and bimodal fusion (Pass 131)

- **Prufer rank `kappa_q` (rank-one rigidity).**  `kappa_q := dim_{F_q}(hatZ_N/Z)[q]`, the
  multiplicity of the summand `Z/q^inf` in `Tor(hatZ_N/Z)`.  Pass-131 Thm 131a: for a SINGLE
  rank-1 nesting tower `(Z, x m_n)` (what a graded Rosser predicate produces), `kappa_q = 1`
  for EVERY finite valuation `e_q` (INCLUDING `e_q = 0`) and `kappa_q = 0` iff `e_q = inf`,
  via the snake lemma of `0->Z->hatZ_N->G->0` at `x q` (`G` divisible `=> G/qG = 0` truncates
  it; diagonal `d(1)=1`).  So `Tor(hatZ_N/Z) = bigoplus_{q notin Supp_inf} Z/q^inf` is
  rank-one Prufer per non-solenoidal prime; a depth-varying overhead permutes finite
  valuations but cannot inflate `kappa_q` -- the continuum lives only in the torsion-free
  `Q^{(2^aleph0)}`.

- **Strand-inflation / multi-strand facet tower.**  A rank-`d` facet tower `(Z^d, x
  diag(a_1,...,a_d))` = a `d`-strand graded predicate (d INDEPENDENT consistency
  coordinates).  Then `A_q = bigoplus_{i: e_q^{(i)}<inf} Z/q^{e_q^{(i)}}` and `kappa_q =
  #{i : q finite in strand i}` (Pathology 131a'); an `omega`-strand tower realizes `kappa_q =
  aleph_0` (sum) or `2^aleph0` (product completion).  Continuum-rank `q`-primary Prufer
  torsion is the exact algebraic signature of a multi-strand (vs single-strand rank-1)
  predicate.

- **Honesty ceiling `h_n => 2^aleph0 >= aleph_{n+1}`.**  Pass-131 Thm 131c (necessity from
  Bergfalk-Lambie-Hanson): `h_n` (`varprojlim^n = 0`) forces `2^aleph0 >= aleph_{n+1}`, so
  `(forall n)h_n => 2^aleph0 >= aleph_{omega+1}` (Konig `cf > omega`) -- SHARPENING the
  Pass-130 `aleph_2`.  The depth split `h_1 ^ ¬h_2` holds in the ZFC model `MA_{aleph1} +
  2^aleph0 = aleph_2` (`h_1` by Dow-Simon-Vaughan, `¬h_2` forced by the ceiling): a
  large-cardinal-FREE stratification `2^aleph0 = aleph_n => ¬h_n`.  Exact strength = the
  Bannister-Bergfalk-Moore-Todorcevic `n`-dim `Delta`-system principle, NOT a cardinal
  characteristic.

- **Bimodal fusion `[GL]_Box (+) [GL]_{-<}`.**  Pass-131 Thm 131d: with `Box_R A := A -< ¬A`
  and `WO = Loeb_{-<}` (Thm 130e), `PL(Box_R^A)` is the FUSION of two `GL` modalities --
  provability `Box` and the witness-race `Box_{-<}` -- plus the definitional bridge; pure-`Box`
  fragment `= R+4` (Thm 128a), `-<`-fragment `= R` (Guaspari-Solovay/Kurahashi).  Canonical
  model = up-closed `-<`-cone neighborhood box (monotone, non-`K`) fibered over a `GL`
  `-<`-frame.  Thm 131e: full `D3` coexists with `¬D2` (the `GL`-collapse fusing the twins is
  `D2`-only; `4 + ¬K + ¬Box_R bot` satisfiable); arithmetic full-`D3` realizability carried.
  See `research/notes/g2-fg2-hierarchy.md` (Pass 131), `code/scripts/check-pass131.py` ->
  `artifacts/reports/pass131-prufer-rank-honesty-ceiling-bimodel-check.json`.

## Pure-`Box` / `-<`-fragment split of a Rosser provability logic (Pass 128)

- **Pure-`Box` fragment vs `-<`-fragment.**  For a Rosser predicate `Box_R` with
  witness-comparison ordering `-<`, the provability logic `PL(Box_R)` decomposes into its
  **pure-`Box` fragment** (formulas in the propositional-modal language with `Box_R` only)
  and its **witness-comparison `-<`-fragment** (formulas mentioning the Guaspari-Solovay
  ordering).  Pass-128 Thm 128a: for Arai's `Box_R^A` the pure-`Box` fragment equals that
  of `R+4`; the entire gap to a full identity lives in the `-<`-fragment, whose
  completeness is the classical Guaspari-Solovay/Kurahashi program, NOT Arai-specific.

- **Witness-race well-foundedness schema `WO`.**  The schema asserting "every descending
  witness-race terminates" (arithmetically valid: proof codes are naturals).  `WO` is
  **pure-`Box`-inexpressible**: its normal companion lies in `K4D` (transitive+serial), and
  every serial+transitive frame is converse-ILL-founded (seriality forces an infinite
  ascending `R`-chain), so `WO`/Löb is unsatisfiable over `K4D`.  Consequently `WO` cannot
  be a pure-`Box` axiom separating `PL(Box_R^A)` from `R+4`.  Contrast: in `GL` the Löb
  axiom IS the well-foundedness schema, but it is incompatible with Rosser consistency
  `¬Box bot` (Löb at `bot` => inconsistency), so `PL(Box_R^A) \subsetneq R+4+Löb` strictly.

- **Race arity vs coding overhead (`m = m_race * m_enc`).**  The nesting-growth multiplier
  of the least-witness box factors as `m_race * m_enc`, where `m_race = 2` is the
  **race arity** (proof-vs-refutation, numbering-INDEPENDENT) and `m_enc` is the
  **coding overhead** (sequence-encoding cost, numbering-DEPENDENT).  The phantom
  `varprojlim^1(Z,\times m) = hatZ_m/Z` depends only on `rad(m)` (Thm 54b), so `2 \in rad(m)`
  ALWAYS, and `rad(m) = {2}` (canonical phantom `hatZ_2/Z`) iff `m_enc` is a power of `2`
  (dyadic coding); Gödel prime-power coding gives the maximal `hatZ/Z`.  The `r`-**ary
  Rosser race** (proof vs `r-1` competitors) has `m_race = r`, phantom
  `(prod_{p|r} Z_p)/Z`, realizing any squarefree radical.

- **Derived-limit trivialization principle (`omega_1`-honesty).**  The set-theoretic
  principle whose truth is equivalent to `varprojlim^1 = 0` for the `omega_1`-cofinal Arai
  facet tower (= "the canonical `aleph_1`-twin Arai bouquet is honest").  Pass-128 Thm
  128c: it is bracketed strictly between `b = aleph_1` (dishonest) and `MA_{aleph_1}`
  (honest), is NOT equivalent to Suslin-tree existence nor to `add(M) = aleph_1`, and is a
  genuinely non-classical invariant (Bergfalk 2017; Bergfalk-Lambie-Hanson 2021), not a
  single cardinal-characteristic equation.
  See `research/notes/g2-fg2-hierarchy.md` (Pass 128), `code/scripts/check-pass128.py` ->
  `artifacts/reports/pass128-rplus4-pin-phantom-prime-omega1-honesty-check.json`.

- **Arithmetic facet tower (Pass 127).** For a Rosser box $\Box_R$ with antitone
  refutability $\boxtimes_R=\neg\Box_R$ and a bouquet frontier $c$ (independent Rosser
  sentence, $c\leftrightarrow\boxtimes_R c$, $T$-unprovable/-irrefutable,
  $\prec$-incomparable to the consistency tower), the **facet tower** is the descending
  net $F_n=\boxtimes_R^n c$.  It is **seeded-honest** iff Mittag–Leffler
  ($\varprojlim^1 F_n=0$) and **seeded-phantom** iff non-ML
  ($\varprojlim^1 F_n=\widehat{\mathbb Z}_m/\mathbb Z$).  The frontier is NEVER the top:
  at $T$, $\boxtimes_R T$ is the image-minimum, so even a single $\mathrm{nFG2}(1)$
  collapses the $T$-orbit (Rem 127a').
- **Honest/phantom derivability identity (Thm 127a).**
  $\mathrm{D3^{hom}}(\Box_R)\Leftrightarrow\text{all-level }\mathrm{nFG2}(\boxtimes_R)
  \Leftrightarrow F_n\text{ ML}\Leftrightarrow\text{seeded-honest}$.  It is the SCHEMA
  (axiom $4$, substitution-closed = all-level nFG2 via Thm 41a), not a single instance,
  that yields ML.  Arai's (1990) $\Box_R^A$ = honest; least-witness $\Box_R^{lw}$ =
  phantom (Cor 126d, arithmetized).
- **4-schema stabilization is NOT the Löb index (correction, Pass 127).** The Arai
  facet tower stabilizes at the axiom-$4$/**transitivity** index (index $2$, Thm 41a),
  NOT at a "Löb index": Arai's box is Rosser-consistent ($T\vdash\neg\Box_R^A\bot$),
  which contradicts Löb.  The honest cell is $4$-honest, Löb-free.
- **Vertical/horizontal decoupling (Thm 127c).** Adjoining $4$ ($=\mathrm{D3^{hom}}$)
  to the Guaspari–Solovay logic $R$ rigidifies the VERTICAL (nesting) axis (facet tower
  $\to$ ML, phantom killed) but leaves the HORIZONTAL twin multiplicity (number of
  $\prec$-independent Rosser fixed points, Thm 125b) UNCHANGED — that count is governed
  by $\neg K/\neg D2$ (de Jongh–Sambin uniqueness needs $K$, not $4$).  Arithmetic
  shadow of the Pass-62 Löb–Rosser bicomplex (vertical column vs horizontal row).
- **$R+4$ pin (obligation, Prop 127e).** $\mathrm{PL}(\Box_R^A)\supseteq R^-+4+\neg\Box
  \bot$; the exact identification $=R+4$ is OPEN, requiring a Solovay/arithmetic-
  completeness theorem for the Arai predicate (absent from the literature at cutoff).
  See `research/notes/g2-fg2-hierarchy.md` (Pass 127), `code/scripts/check-pass127.py`
  -> `artifacts/reports/pass127-honest-phantom-rosser-bouquet-decoupling-check.json`.
- **$D3^{\mathrm{mix}}$ vs $D3^{\mathrm{hom}}$ (Thm 125a).** For the Rosser box
  $\Box_R\varphi\ (\in\Sigma_1)$, the **heterogeneous/mixed** third derivability
  condition $\Box_R\varphi\to\Box(\Box_R\varphi)$ (outer PLAIN box) is an
  unconditional theorem via $\Sigma_1$-completeness; the **homogeneous**
  $\Box_R\varphi\to\Box_R\Box_R\varphi$ (outer Rosser box) is $R$-independent
  (arithmetization-dependent; Arai 1990).  The Rosser profile is
  $D1\wedge\neg D2\wedge D3^{\mathrm{mix}}$, $D3^{\mathrm{hom}}$ free; adding $D2$
  ($=$ normality) collapses to $GL$ (de Jongh--Sambin uniqueness) and destroys the
  twins.
- **Witness-comparison logic $R$; $\Box_R A:=(A\prec\neg A)$ (Thm 125b).** The
  Guaspari--Solovay (1979) modal logic of witness comparison $\prec,\preceq$ over a
  $GL$-base $\Box$; the Rosser box is DEFINED as $\Box_R A:=(A\prec\neg A)$ ("some
  proof of $A$ precedes every proof of $\neg A$").  Kripke-with-$\prec$ frames: $GL$
  trees (irreflexive, converse-well-founded) with a linear witness-priority on each
  world's successors; the Henkin center is a CUT, never a world.
- **Exhaustive $\alpha$ identity (Thm 125d).** The Thm-123d bound is EXACT:
  $\alpha(H)=2+\lvert\mathrm{MaxInd}(H)\rvert$, by a blocking/set-cover argument on the
  atom/coatom incidence (each proper fan atom's independent label covers $\le1$
  maximal independent set $\Rightarrow\ge\lvert\mathrm{MaxInd}\rvert$ fan atoms; $\mu=2$
  non-principality $\Rightarrow\ge2$ core), exhaustively verified with zero
  realizations below budget.
- **Seeded-honest vs seeded-phantom center; continuity $=$ ML $=$ nFG2 pivot
  (Thm 125c).** For an $\omega$-bouquet with directed join $w=\bigvee_n c_n$: if
  $\boxtimes$ is join-continuous at $w$ ($\Leftrightarrow$ ML $\Leftrightarrow$
  all-level nFG2, Thm 48b/55c) then $\boxtimes w=\bigwedge_n\boxtimes c_n$ is FORCED and
  the center is **seeded-honest** iff the directed meet attains $w$; a join-continuity
  FAILURE gives a free **seeded-phantom** center (Pass-55 solenoid,
  $\varprojlim^1=\widehat{\mathbb Z}_m/\mathbb Z$).  The finite seeded/seedless split
  (Thm 124a) bifurcates into $\{$seeded-honest, seeded-phantom, seedless$\}$.
  See `code/scripts/check-pass125.py` ->
  `artifacts/reports/pass125-rosser-d3-exhaustive-alpha-carrier-join-check.json`.
- **$D3^{\mathrm{hom}}=$ axiom $\mathbf 4$; least-witness refutes it (Thm 126a).** For
  the STANDARD least-witness $\Box_R$, $D3^{\mathrm{hom}}$ ($\Box_R\varphi\to\Box_R
  \Box_R\varphi$) is a genuine FAILURE, not mere silence: $\sigma=\Box_R\varphi\in
  \Sigma_1$ gives only the mixed step, and the homogeneous step's inner Rosser guard is
  broken in $T+\Box_T\bot$ by a **spurious short witness** $s_0\le r$ for $\dot\neg
  \sigma$ (uncertifiable inside $T$ by G2). Arai (1990) reorders witnesses to repair
  $D3^{\mathrm{hom}}$ while still dropping $D2$ (no Rosser predicate has all of
  $D1,D2,D3^{\mathrm{hom}}$, else HBL$=GL$ refutes Rosser consistency). Modally
  $D3^{\mathrm{hom}}=\mathbf 4$, $D2=\mathbf K$.
- **$D3^{\mathrm{hom}}$-compatible Rosser logic.** A provability logic $L$ in the
  Kurahashi (2016) range with $\mathbf 4\in L$, $\neg\Box\bot\in L$, $\mathbf K\notin L$
  -- transitive, Rosser-consistent, and NON-normal. The least-witness box realizes an
  $\mathbf 4$-free point; Arai's an $\mathbf 4$-containing one.
- **Cardinal $\alpha$-identity (Thm 126b).** $\alpha(H)=2+\lvert\mathrm{MaxInd}(H)
  \rvert$ holds VERBATIM in cardinal arithmetic; for infinite $\lvert\mathrm{MaxInd}
  \rvert$ the $+2$ core tax is ABSORBED, $\alpha(H)=\lvert\mathrm{MaxInd}(H)\rvert$.
  $\alpha$ is UNBOUNDED by $\lvert V(H)\rvert$: the countable perfect matching
  $M_\omega$ has $\lvert\mathrm{MaxInd}\rvert=2^{\aleph_0}$ (continuum-atom carrier over
  $\aleph_0$ vertices).
- **Compact independence complex; seeded-honest $=$ facet-tower-ML (Thm 126c).** A
  bouquet is **seeded-honest** ($\bigwedge_n\boxtimes c_n=w$ attained) $\iff$ the
  descending facet tower $(\boxtimes c_n)_n$ is **Mittag--Leffler** ($=$ nFG2 at the
  frontier), NOT $\iff$ $\lvert\mathrm{MaxInd}(H)\rvert<\aleph_0$. A **compact**
  independence complex (finitely many facets) is SUFFICIENT but not necessary: an
  $\omega$-fan with eventually-constant images is honest; the strictly seeded-phantom
  cell is a non-ML dilation tower ($\varprojlim^1=\widehat{\mathbb Z}_m/\mathbb Z$).
  Cor 126d: the honest/phantom cell is fixed by the SAME $\mathbf 4$-vs-$\neg\mathbf 4$
  freedom as $D3^{\mathrm{hom}}$ (Arai $=$ honest, least-witness $=$ phantom). See
  `code/scripts/check-pass126.py` ->
  `artifacts/reports/pass126-d3hom-frontier-infinite-alpha-check.json`.
- **Multi-strand facet tower / $\kappa_q=d$ (Thm 132a).** The $d$-strand graded Rosser
  predicate $\mathrm{Pr}_{R,\vec a}^{(d)}$ ($d$ recursive Godel color-families, each with
  independent per-band $a_k$-ary Guaspari--Solovay races) has $\mathrm{ConLat}$-image
  $(\mathbb Z^d,\times\mathrm{diag}(a_k))$, phantom $\bigoplus_{i<d}\widehat{\mathbb Z}_N/
  \mathbb Z$, and $q$-Prufer rank $\kappa_q=\#\{\text{strands finite at }q\}=d$. Discharges
  Pathology 131a' as a construction; o1'/o2' (cross-layer GS independence) discharged by a
  uniform recursion-theorem fixed point with parameter $(i,k)$.
- **Arithmetic torsion-rank ceiling (Thm 132a).** Every $\Sigma_1$ Rosser-graded predicate
  carries a RECURSIVE band family, hence $\le\aleph_0$ strands, hence $\kappa_q\le\aleph_0$;
  the arithmetically natural derived limit is the direct SUM (each proof code lies in one
  band, finite support). No $\Sigma_1$ predicate reaches continuum torsion.
- **$\bigoplus\to\prod$ socle jump / Erdos--Kaplansky (Cor 132a').** Continuum torsion
  $\kappa_q=2^{\aleph_0}$ is realized ONLY by the direct PRODUCT completion
  $\prod_{i<\omega}(\mathbb Z,\times a)$, whose $q$-socle $\prod_i\mathbb F_q=\mathbb F_q^{\,
  \omega}$ has dimension $|\mathbb F_q|^{\aleph_0}=2^{\aleph_0}$ (Erdos--Kaplansky). The jump
  $\aleph_0=\dim(\bigoplus\mathbb F_q)\to 2^{\aleph_0}=\dim(\prod\mathbb F_q)$ is the
  finitely-supported$\to$unrestricted (arithmetic$\to$analytic) boundary; continuum-rank
  Prufer torsion has NO arithmetic-hierarchy representative and first appears there, its
  nonvanishing Suslin-sensitive (Pass 60d/61c). The $\prod$-object $=$ the $\aleph_1$-cofinal
  twin tower of Thm 131c.
- **Honesty ceiling, positive half (Thm 132b).** For every $n$ there is a
  large-cardinal-free ZFC model with $2^{\aleph_0}=\aleph_n$ and $h_1\wedge\cdots\wedge
  h_{n-1}\wedge\neg h_n$ (force BHLH $A_{n-1}$ by a length-$\aleph_n$ Hechler iteration;
  $\neg h_n$ from the Thm-131c ceiling). Strict strength chain $A_\kappa\Rightarrow(\forall
  n)h_n\Rightarrow 2^{\aleph_0}\ge\aleph_{\omega+1}$; $A_\kappa$ at neither endpoint,
  equivalence $A_\kappa\Leftrightarrow(\forall n)h_n$ OPEN.
- **Full $D3$ forces $\neg D2$ (Thm 132c).** Over consistent $T$: $D1\wedge D2\wedge(\text{full
  }D3)\wedge(T\vdash\neg\Box_R\bot)$ is inconsistent (five-line Lob collapse at $\bot$), so
  $D1\wedge(\text{full }D3)\wedge(T\vdash\neg\Box_R\bot)\Rightarrow\neg D2$. Rosser-consistency
  $+$ full $D3$ REQUIRE non-normality; the collapse consumes $D2$ (Lob axiom $=_K D2+D3$).
- **$m_{\mathrm{enc}}$ obstruction / $PL\neq$ realizability (Conj 132d).** Uniform full $D3$
  is conjecturally arithmetically incompatible with a $\Sigma_1$ Rosser box: the nesting
  overhead $m_{\mathrm{enc}}$ (Pass 128b) inflates the inner witness code cofinally, so only
  the $O(1)$-nesting fragment $D3^{\mathrm{hom}}$ (Arai) survives. Hence $PL(\Box_R^A)=R+4$ is
  arithmetically INCOMPLETE for Rosser boxes at full $D3$ -- the modal $4\wedge\neg K\wedge
  \neg\Box\bot$ is consistent (monotone neighborhood $N(w)=\mathrm{up}\{W,\{0,1\},\{0,2\}\}$)
  yet unrealized. See `code/scripts/check-pass132.py` ->
  `artifacts/reports/pass132-multistrand-phantom-honesty-ceiling-fulld3-check.json`.

## Continuum-phantom absoluteness, `A_kappa` placement, and witness-bounded full `D3` (Pass 133)

- **`varprojlim^1` commutes with products of a tower (Thm 133a).** For an $\omega$-indexed
  inverse system, $\varprojlim$ and $\varprojlim^1$ are the kernel and cokernel of the exact
  two-term complex $\prod_n A_n\to\prod_n A_n$; since the product functor is EXACT on
  $\mathbf{Ab}$, both commute with arbitrary products $\prod_i$. Hence
  $\varprojlim^1(\prod_{i<\omega}(\mathbb Z,\times a))=(\widehat{\mathbb Z}_a/\mathbb Z)^\omega$
  is **ZFC-absolute** and nonzero. Contrast: $\varprojlim^1$ does NOT commute with uncountable
  direct SUMS -- that failure is the Mardesic--Prasolov non-additivity.
- **Continuum phantom is cardinality, not cofinality (Cor of Thm 133a).** The product-tower
  torsion rank $\kappa_q=2^{\aleph_0}$ (socle $F_q^{\,\omega}$, Erdos--Kaplansky) is a
  **cardinality** fact of the $\bigoplus\to\prod$ socle jump, carrying NO forcing-axiom
  sensitivity. This CORRECTS the Pass-132 Next-step conflation of the continuum phantom with
  the Suslin-sensitive strong-homology / $A_{\aleph_1}$ derived limit.
- **Intermediate a-primary coherent object (Thm 133b).** The genuine CH-realized /
  $\mathrm{MA}_{\aleph_1}$-killed object with $\kappa_q=\aleph_1$ is the $a$-primary
  Mardesic--Prasolov coherent system $A^{(a)}$ ($\mathbb Z/a^n$-coefficients on
  $[\omega_1]^{<\omega}$ / $\omega^\omega$), a **second-order-over-$\omega_1$** limit --
  neither a $\Sigma_1$ graded Rosser predicate nor a discrete-strand sum. Suslin-sensitivity
  lives in the $\omega_1$-COFINALITY of the index, not in the number of strands.
- **`A_kappa` vs `(forall n)h_n`: single-system-vs-all-systems (Thm 133c).** $A_\kappa$
  (the BBMT / BHLH $n$-dimensional $\Delta$-system principle) trivializes $\lim^n$ for ALL
  coherent systems on $[\kappa]^{<\omega}$; $(\forall n)h_n$ trivializes only the distinguished
  twin tower $A$. So $A_\kappa\Rightarrow(\forall n)h_n$; the converse
  $\Leftrightarrow\mathrm{Con}((\forall n)h_n(A)\wedge(\exists\text{ coherent }B)\varprojlim^1B\ne0)$
  (the open BBMT additivity question). At $n=1$ triviality transfers ($A$ is a retract of the
  universal $1$-skeleton); at $n\ge2$ non-retractable systems block it, so $A_\kappa$ is a
  priori strictly stronger.
- **Witness-bounded full `D3` vs schema-`4` (disambiguation, Pass 133).** The modal SCHEMA-`4`
  reading of "full $D3$" ($\Box_R A\to\Box_R\Box_R A$, substitution-closed) is ALREADY Arai's
  (Pass 127a, $=$ all-level nFG2), so Conj 132d is non-vacuous only under the **witness-bounded**
  reading: a primitive-recursive uniform bound $B$ certifying the nested Rosser-witness of
  $\Box_R\sigma$ below $B(|p|)$.
- **`m_enc`-gap inflation family (Constr 133e, Thm 133f).** By the parametrized diagonal lemma,
  primitive-recursive $(\varphi_k)$ with $T\vdash\varphi_k$, least proof length $p_k$, planting
  a spurious $\mathrm{Prf}$-code of $\dot\neg\Box_R\varphi_k$ in the coding-overhead gap
  $(p_k,m_{\mathrm{enc}}(p_k)]$. For the least-witness box the outer guard is preempted on the
  whole gap (width $\to\infty$), so **witness-bounded full $D3$ FAILS cofinally**; the $O(1)$
  Arai reorder repairs it. Conj 132d thereby REDUCES to the carried obligation "every $\Sigma_1$
  witness-comparison Rosser box has $m_{\mathrm{enc}}$ unbounded". See
  `research/notes/g2-fg2-hierarchy.md` (Pass 133), `code/scripts/check-pass133.py` ->
  `artifacts/reports/pass133-continuum-phantom-absoluteness-akappa-menc-check.json`.

## Ordering-internalization, the a-primary intermediate MP phantom, and the 2-coherent separator (Pass 134)

- **Ordering-internalization diagonal (Thm 134a).** The diagonal that beats a candidate
  nested-witness bound $B$ for a Rosser box with witness ordering $\prec$: build $\varphi^*_k$
  (parametrized recursion theorem) planting a $\mathrm{Prf}$-code of $\dot\neg\Box_R\varphi^*_k$
  at $\prec$-rank in the gap $(k,B(k)]$ *defined from the Gödel numbers of both $\prec$ (=$e$) and
  $B$ (=$b$)*. Because the plant references $(e,b)$, a primitive-recursive re-ordering $\pi$ only
  relabels a gap of the same asymptotic width -- the box "cannot outrun its own Gödel number".
  Yields: every **p.r.-ordered** $\Sigma_1$ Rosser box with $\neg D2\wedge\neg\Box_R\bot$ has
  UNBOUNDED $m_{\mathrm{enc}}$ (no p.r. uniform witness-bounded full $D3$), closing Conj 132d for
  the standard class (Cor 134b: $\mathrm{PL}(\Box_R^A)=R+4$ arithmetically incomplete at full
  $D3$). *Scope correction:* the honest universal is "every p.r.-ordered $\Sigma_1$ box", not
  "every $\Sigma_1$ box"; the exotic non-p.r. ordering is carried (needs $\Sigma_1$-induction).
- **a-primary intermediate MP phantom $A^{(a)}$ (Thm 134c).** The $a$-primary reduction of the
  strong-homology coherent system on $(^{\omega}\omega,\le^*)$; $\varprojlim^1 A^{(a)}\ne 0$
  under $\mathfrak b=\aleph_1$ (Mardešić--Prasolov), $=0$ under $\mathrm{MA}_{\aleph_1}$
  (Dow--Simon--Vaughan), with $a$-primary rank $=$ least non-trivializable coherent family
  ($=\aleph_1$ at $\mathfrak b=\aleph_1$). Its rank tracks the COFINALITY of the coherent index,
  not the strand count (contrast Thm 132a's strand-inflation).
- **Strictly-intermediate = Cohen, not CH (Thm 134c(iii)).** Under CH the "intermediate" object
  is not strict ($\aleph_1=2^{\aleph_0}$); the genuine strictly-intermediate witness
  ($\aleph_0<\mathrm{rank}<2^{\aleph_0}$) is the Cohen model $\mathfrak b=\aleph_1<c=\aleph_2$.
- **$\aleph_1$-first `cf`-indexed rank spectrum (Thm 134d).** $\aleph_1$ is the FIRST (minimal),
  NOT the unique, non-arithmetic torsion layer: $\omega_n$-cofinal coherent systems realize a
  strictly increasing spectrum $\aleph_0<\aleph_1<\aleph_2<\cdots<2^{\aleph_0}$ of forcing-
  sensitive $\varprojlim^s$-ranks, the Pass-55 single-prime solenoid $\mathbb Z_p/\mathbb Z$
  being the arithmetic $n=0$ ($\aleph_0$) floor.
- **Level-1 non-separation / 2-coherent separator $A^{(a),2}$ (Thm 134e).** In the Thm-133c
  reduction, $A^{(a)}$ at level 1 does NOT separate (1-dimensional $\Rightarrow$ retract of the
  universal 1-skeleton $\Rightarrow h_1(A)$ kills $\varprojlim^1 A^{(a)}$). The honest separator
  is the 2-coherent $A^{(a),2}$ (two 2-simplices sharing a vertex, non-retractable from a
  1-simplex), reducing $A_\kappa\Leftarrow(\forall n)h_n$ to
  $\mathrm{Con}((\forall n)h_n(A)\wedge\varprojlim^2 A^{(a),2}\ne 0)$ -- an explicit instance of
  the still-open BBMT additivity question. See `research/notes/g2-fg2-hierarchy.md` (Pass 134),
  `code/scripts/check-pass134.py` ->
  `artifacts/reports/pass134-menc-unbounded-a-primary-intermediate-two-system-check.json`.

## Effective sign sheaf, $\omega$-absolute chirality, and interpretability antimatter (Pass 150)

- **Realization diagram $\mathrm{Real}(\boxtimes)$.** The small diagram whose objects are the
  realized detached races $R_e=\{\rho_e,\neg\rho_e\}$ (indexed by $e$ in the domain of a coded
  proof order) and whose morphisms are $\prec$-monotone race refinements. It is the site on which
  the orientation data of $\mathrm{Fix}(\boxtimes)$ is organized.
- **Sign sheaf $\mathrm{sgn}$ and effective sign sheaf $\mathrm{sgn}^{\Sigma_1}$ (Def 150.0).**
  $\mathrm{sgn}$ assigns to each race $R_e$ its orientation $\mathbb Z/2$-torsor $\mathrm{Or}(R_e)=S^0$
  (the two sides). $\mathrm{sgn}^{\Sigma_1}$ is the subsheaf of $\Sigma_1$/c.e.-graph sections, taken
  in the effective (Ershov / realizability) Grothendieck topology whose covers are c.e. families.
- **De-localized $(Z,Z/2)$ (Thm 150a).** The symmetric signature's second coordinate is, honestly,
  the class $[\mathrm{sgn}^{\Sigma_1}]=1\in\check H^1_{\mathrm{eff}}(\mathrm{Real};\mathbb Z/2)=\mathbb Z/2$:
  classically the schematic $\mathbb Z/2$ vanishes ($H^0(\mathrm{sgn})\ne0$ by $AC$, Čech
  $H^1(\mathrm{sgn})=0$ on the discrete singleton-race cover); effectively $H^0(\mathrm{sgn}^{\Sigma_1})=0$
  (no recursive separator of the inseparable Kleene pair) and $H^1_{\mathrm{eff}}=\mathbb Z/2$.
  Nonvanishing is $\mathrm{I}\Sigma_1$-provable (recursion-theorem diagonal); *concentrating* the
  class onto one stalk ($H^0(\mathrm{sgn})(\kappa)=\mathbb Z/2$) costs the KF ordinal
  $\varphi_{\varepsilon_0}(0)$. "$\Sigma_1$-schematic not $\Sigma_1$-pointwise" $=$ globally cheap
  $H^1_{\mathrm{eff}}$, locally expensive $H^0$.
- **$\omega$-absolute chirality (Prop 150b.1).** In every $\Sigma_1$-sound extension of $EA$ every
  realized $\mathrm{GLP}$-modality has grade $\ge0$; $\mathrm{GLP}^+=(\mathbb N,+)$ is well-founded
  with least $\langle0\rangle=T$, so no negative grade is realized over $\omega$-models.
- **Interpretability antimatter $-\langle n\rangle$ / phantom witness (Thm 150c, Pathology 150d).**
  $A_{-1}:=PA+\neg\mathrm{Con}(PA)$ is consistent (Gödel II), $\Pi_1$-sound, and interpretable in
  $PA$ (Feferman 1960); it carries a NONSTANDARD proof of $\bot$ --- the $-\langle1\rangle$ avatar,
  $\equiv_T$-invisible over $\mathbb N$, $\Pi_1$-conservative and interpretability-below $PA$ but not
  $\Sigma_1$-conservative. The phantom fiber over $-\langle1\rangle$ has size $2^{\aleph_0}$
  (Lindström density of the interpretability degrees below $PA$). "Perfect antimatter": a theory that
  proves its own inconsistency yet never proves a false $\Pi_1$ fact.
- **Spanier--Whitehead duality functor $D$ (Thm 150c).** $D:\mathrm{Real}(\boxtimes)^{\mathrm{op}}\to
  \mathrm{SW}^{\mathrm{ph}}$, on grades the antipode $s:k\mapsto-k$ on $K_0=\mathbb Z$
  ($D^2=\mathrm{id}$, fixed locus $\{0\}=S^0=T$-floor, free off it), sends the Pass-53 phantom POINT
  $\varprojlim^1=\widehat{\mathbb Z}_m/\mathbb Z$ to the antimatter CLASS $-\langle n\rangle$; it lands
  only in the phantom-completed $\mathrm{SW}^{\mathrm{ph}}$, never in the chiral cone of
  $\omega$-realized principles. Chirality: absolute over $\omega$, phantom-broken over
  interpretability. See `research/notes/g2-fg2-hierarchy.md` (Pass 150),
  `code/scripts/check-pass150.py` ->
  `artifacts/reports/pass150-effective-derived-z2-phantom-witness-sw-duality-check.json`.
