# Definitions

This file normalizes recurring definitions for the APS/G2-ZOO project.

## Abstract Provability Structure

An abstract provability structure is treated as preorder-like data

\[
S=(L_S,\le_S,\Box,\boxtimes,T,\bot).
\]

The intended readings are:

\[
T\le_S x
\quad\text{means}\quad
x\text{ is provable},
\]

\[
x\le_S\bot
\quad\text{means}\quad
x\text{ is refutable}.
\]

The symbols \(T\) and \(\bot\) are distinguished APS constants; a preAPS need
not make them greatest or least elements unless this is stated separately.

**Bottom discipline** is the additional order principle:

\[
\forall x\in L_S,\quad \bot\le_S x.
\]

Read proof-theoretically, this is an ex-falso or absurdity-weakening principle:
from the contradiction/refutation constant one may weaken to any element. In the
four-element model `M4-G2FG2FP`, all instances of bottom discipline already hold
except \(\bot\le c\), so the residuated order repair is exactly the missing
bottom-discipline instance for the \(c\)-branch.

## G2

\[
\mathrm{G2}(S):
\quad
\boxtimes T\le_S\bot
\Rightarrow
T\le_S\bot.
\]

Read: if the consistency-like assertion is refutable, then the system is already inconsistent.

## FG2

\[
\mathrm{FG2}(S):
\quad
\boxtimes\boxtimes T\le_S\boxtimes T.
\]

Read: a formalized second incompleteness principle internal to the APS order.

For \(k\ge 1\), define:

\[
\mathrm{nFG2}(k):
\quad
\boxtimes^{k+1}T\le_S\boxtimes^kT.
\]

Thus FG2 is \(\mathrm{nFG2}(1)\). The \(T\)-orbit of \(\boxtimes\) is:

\[
T,\boxtimes T,\boxtimes^2T,\ldots
\]

All-level nFG2 means \(\mathrm{nFG2}(k)\) holds for every \(k\ge 1\). In finite
preAPS models this is equivalent to eventual stabilization of the tail orbit at
a syntactic \(\boxtimes\)-fixed point.

The **first-true nFG2 depth** of a model is the least \(d\ge 1\) such that
\(\mathrm{nFG2}(d)\) holds, if such a \(d\) exists. The family \(D_N\) in
`notes/g2-fg2-hierarchy.md` has first-true depth \(N+1\).

If \(S\) is non-collapsed, i.e. \(T\not\le_S\bot\), then G2 holds iff
\(\boxtimes T\not\le_S\bot\). Thus G2 in non-collapsed finite preAPS models is
always vacuous in the material-implication sense.

## Fixed Point Principles

Jeroslow/refutability fixed point:

\[
\exists p\,(p=_S\boxtimes p).
\]

Godel/negated provability fixed point:

\[
\exists p\,(p=_S\neg\Box p).
\]

These must be kept distinct unless \(\boxtimes\) is explicitly defined from \(\neg\Box\).

## Completion Vocabulary

For a preorder \(L\) and \(X\subseteq L\), write:

\[
X^u=\{a\in L:\forall x\in X,\ x\le a\},
\qquad
X^l=\{a\in L:\forall x\in X,\ a\le x\}.
\]

A MacNeille-closed lower cut is a set \(C\subseteq L\) such that:

\[
C=(C^u)^l.
\]

The MacNeille completion \(\widehat L\) is the ordered collection of these
closed lower cuts, with the principal embedding:

\[
i(a)=(\{a\}^u)^l.
\]

A completion-generated fixed point for \(\boxtimes\) is an element
\(q\in\widehat L\) satisfying:

\[
q=\widehat{\boxtimes}q.
\]

A syntactic fixed point is a formula-level or APS-level element \(p\in L\)
satisfying:

\[
p=\boxtimes p.
\]

A completion fixed point is reflected when \(q=i(p)\) for such a \(p\), or when
a stated definable/compact rounding lemma recovers such a \(p\) from \(q\).

For antitone \(\boxtimes\), the extension should be treated as a monotone map
into the order dual before any comparison back with \(\widehat L\).

The **correct lower extension** of an antitone \(\boxtimes:L\to L\) to
MacNeille cuts is the map \(\widehat{\boxtimes}:\widehat L\to(\widehat L)^{op}\)
defined by:

\[
\widehat{\boxtimes}(C) = \bigl((\boxtimes[C])^{l_L}\bigr)^{u_L},
\]

i.e., the \(L^{op}\)-MacNeille closure of the pointwise image \(\boxtimes[C]\).
This satisfies the extension condition
\(\widehat{\boxtimes}(i(a))=i_{L^{op}}(\boxtimes a)\) for all \(a\in L\).

**Warning**: computing \(((\boxtimes[C])^{u_L})^{l_L}\) instead (the
\(L\)-MacNeille closure) is the wrong polarity. It agrees with the correct
formula on lattice models (where every cut is principal) but diverges on
non-lattice models, producing spurious completion fixed points.

A completion fixed point \(q\) is **reflected** iff \(q=i(p)\) for some
syntactic fixed point \(p\in L\) (i.e., \(\boxtimes p = p\)).

A completion fixed point is **principal-unreflected** iff \(q=i(a)\) for some
\(a\in L\) but \(\boxtimes a \neq a\). Principal-unreflected fixed points can
appear even in lattice models (as in `three-chain-antitone` where \(q=i(t)\)
with \(\boxtimes t = b\neq t\)).

## Residuated APS

A residuated APS adds a resource composition and residuals:

\[
(L,\le,\otimes,\mathbf 1,\backslash,/,\Box,\boxtimes,T,\bot).
\]

The residuation law is:

\[
a\otimes b\le c
\iff
b\le a\backslash c
\iff
a\le c/b.
\]

For finite structural-rule checks in the G2-ZOO notes, use:
\[
E:\ a\otimes b=b\otimes a,
\qquad
C:\ a\otimes a\le a,
\]
and the strong weakening form
\[
W:\ a\le b\Rightarrow a\otimes c\le b.
\]
The reflexive instance of \(W\), \(a\otimes c\le a\), is recorded separately in
machine reports as `discarding_reflexive_W`.

For the bottom-disciplined \(B_N\) family, the
**truncated-exponent \(U\)-absorbing tensor** is the commutative tensor with
unit \(T\), zero \(b\), \(U\) absorbing over nonzero non-unit factors, and
exponents

\[
e(s)=e(a_{N+1})=1,\qquad e(a_i)=i+1\quad(1\le i\le N).
\]

For \(x,y\in\{s,a_1,\ldots,a_{N+1}\}\),

\[
x\otimes y=
\begin{cases}
a_{e(x)+e(y)-1} & e(x)+e(y)\le N+1,\\
U & e(x)+e(y)>N+1.
\end{cases}
\]

The case \(e(x)+e(y)=1\) never occurs for two non-unit factors, so the
ambiguous exponent-1 pair \(s,a_{N+1}\) only matters in residuals, where
\(a_{N+1}\) is the maximum element with exponent 1 because \(s\le a_{N+1}\).

For \(N\ge 3\), the **front-shifted non-\(U\)-absorbing tensor** on \(B_N\) is
the commutative tensor with unit \(T\), zero \(b\), front set
\(F=\{a_1,a_2\}\), and tail
\[
R_N=\{s,a_{N+1},a_3,\ldots,a_N\}.
\]
The front elements are orthogonal idempotents:
\[
a_1^2=a_1,\qquad a_2^2=a_2,\qquad a_1a_2=b.
\]
For \(p\in F\) and \(r\in R_N\cup\{U\}\), set
\[
p\otimes r=p,\qquad U\otimes p=p.
\]
On the tail, put
\[
\tau(s)=\tau(a_{N+1})=1,\qquad \tau(a_i)=i-1\quad(3\le i\le N),
\]
let \(\rho(1)=a_{N+1}\) and \(\rho(q)=a_{q+1}\) for \(2\le q\le N-1\), and set
\[
r\otimes r'=
\begin{cases}
\rho(\tau(r)+\tau(r')) & \tau(r)+\tau(r')\le N-1,\\
U & \tau(r)+\tau(r')>N-1.
\end{cases}
\]
Finally \(U\otimes r=U\) for \(r\in R_N\) and \(U^2=U\). This template is not
\(U\)-absorbing because \(U\otimes a_1=a_1\) and \(U\otimes a_2=a_2\).

Its residuals are symmetric, so it is enough to give \(m\backslash c\). Write
\(p^\perp\) for the other front element, i.e. \(a_1^\perp=a_2\) and
\(a_2^\perp=a_1\). Then:
\[
b\backslash c=U,\qquad T\backslash c=c,
\]
\[
p\backslash c=
\begin{cases}
U & c\in\{p,U\},\\
p^\perp & \text{otherwise}
\end{cases}
\quad(p\in F),
\]
and
\[
U\backslash c=
\begin{cases}
U & c=U,\\
c & c\in F,\\
b & \text{otherwise.}
\end{cases}
\]
For \(r\in R_N\):
\[
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
\]
Commutativity gives the same right residuals.

The same tensor has a useful **front ideal-extension presentation**. Let
\[
I=\{b,a_1,a_2\}.
\]
Then \(I\) is a downward closed two-sided tensor ideal:
\[
x\le y\in I\Rightarrow x\in I,\qquad I\otimes L\subseteq I.
\]
Inside \(I\), the nonzero front elements form an orthogonal idempotent
zero-band:
\[
a_1^2=a_1,\qquad a_2^2=a_2,\qquad a_1a_2=b.
\]
Multiplication by any element outside the other front atom projects back to the
chosen front atom:
\[
a_i\otimes x=a_i
\quad(x\notin\{b,a_{3-i}\}).
\]
The Rees quotient collapsing \(I\) to its zero \(b\) is the shifted tail monoid
on representatives
\[
\{b,T,U,s,a_{N+1},a_3,\ldots,a_N\}.
\]
Thus the construction is best viewed as an ideal extension of the shifted
truncated tail by a two-atom contractive front ideal, not as a direct product.
This explains the structural-rule profile: contraction holds locally in \(I\),
while the quotient tail retains the noncontractive resource-sensitive behavior.
The finite checker
`scripts/check-front-shifted-extension-presentation.py` verifies this
presentation on the saved depth-3, depth-4, and depth-5 instances.

More generally, the **orthogonal front-width schema** replaces the front by
\[
F_k=\{a_1,\ldots,a_k\}
\]
with pairwise zero product and idempotent diagonal, then shifts the tail to
\[
\{s,a_{N+1},a_{k+1},\ldots,a_N\}.
\]
The finite report `outputs/front-ideal-size-bound-check.json` checks this
schema at depths 3, 4, and 5. Front widths \(k=0,1,2\) are fully residuated in
those checks, while \(k\ge3\) fails immediately by non-principal residual
fibers: for \(p\in F_k\), the fiber of \(p\backslash b\) contains
\(\{b\}\cup(F_k\setminus\{p\})\), which has multiple incomparable maximal
front atoms when \(k\ge3\). Thus the two-atom front is maximal in the present
same-order orthogonal-front schema, though a one-atom non-\(U\)-absorbing
variant remains available and should get its own closed residual table.

For \(k\in\{0,1,2\}\), write
\[
\tau_k(s)=\tau_k(a_{N+1})=1,\qquad
\tau_k(a_i)=i-k+1\quad(k+1\le i\le N),
\]
with \(\rho_k(1)=a_{N+1}\) and
\(\rho_k(d)=a_{k+d-1}\) for \(2\le d\le N-k+1\). The closed residual table is
the following uniform one. As usual,
\[
b\backslash c=U,\qquad T\backslash c=c.
\]
For \(p\in F_k\),
\[
p\backslash c=
\begin{cases}
U & c\in\{p,U\},\\
b & k=1,\ c\notin\{p,U\},\\
p^\perp & k=2,\ c\notin\{p,U\},
\end{cases}
\]
where \(p^\perp\) denotes the unique other front atom. For \(U\),
\[
U\backslash c=
\begin{cases}
U & c=U,\\
c & c\in F_k,\\
b & \text{otherwise.}
\end{cases}
\]
For \(r\) in the shifted tail,
\[
r\backslash c=
\begin{cases}
U & c=U,\\
c & c\in F_k,\\
T & c=s,\ r=s,\\
T & c=a_{N+1},\ r\in\{s,a_{N+1}\},\\
T & c=r\in\{a_{k+1},\ldots,a_N\},\\
\rho_k(\tau_k(c)-\tau_k(r)) &
  c\in\{a_{k+1},\ldots,a_N\},
  \tau_k(c)-\tau_k(r)\ge1,\\
b & \text{otherwise.}
\end{cases}
\]
Commutativity gives the right residuals. The checker
`scripts/check-front-width-residual-formula.py` verifies this formula with zero
mismatches for \(k=0,1,2\) at depths 3, 4, and 5.

## Open Definition Tasks

- Define ACR precisely.
- Normalize A1-A4 and variants.
- Define primitive versus definitional \(\boxtimes\).
- Define indexed/fibered APS.
- Define completion-generated fixed points versus syntactic fixed points.
