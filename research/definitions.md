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
