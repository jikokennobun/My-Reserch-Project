# Local-FG2 Pullback and APS Zoo

Source: https://chatgpt.com/share/6a0b9917-ef00-83a7-a14d-57f0788adab2

Imported from Research Project handoff: 2026-05-22

Access note: the share is recorded in the local watchlist as
`Consistency zoo and APS`. It has previously appeared as both reachable and
temporarily inaccessible in relay logs. The notation $M_G$ and $M_{GJ}$ is kept
as working notation until the source transcript is re-exported.

## Abstract

This note develops a local and relative version of FG2 suitable for comparing
different APS models. Ordinary FG2 is the single inequality:

$$
\boxtimes\boxtimes T\le\boxtimes T.
$$

Local-FG2 replaces this global assertion by a family of tests indexed by a
target $a\in L$ or by a morphism into a comparison model. Pullbacks then become
a way to combine, separate, or align Godel-style and Jeroslow-style consistency
principles inside one APS-ZOO framework.

The guiding question is:

$$
\text{Can G2-independent principles be compared by pulling APS models back
along a common reduct?}
$$

## Background

Write:

$$
S=(L,\le,\Box,\boxtimes,T,\bot).
$$

Let:

$$
d_S:=\boxtimes T.
$$

The ordinary principles are:

$$
\mathrm{G2}(S):
\quad
d_S\le\bot\Rightarrow T\le\bot,
$$

and:

$$
\mathrm{FG2}(S):
\quad
\boxtimes d_S\le d_S.
$$

The Project discussion motivates treating these not as isolated truth values
but as points in a comparison geometry. The two model names should be read as:

- $M_G$: a Godel-style or global consistency model;
- $M_{GJ}$: a mixed Godel-Jeroslow or refutability-based comparison model.

Those readings must be verified against a fresh source export. The formal
construction below does not depend on the names.

## Local FG2

Define the local formalized G2/FG2 condition at $a\in L$ by:

$$
\mathrm{LG2}_S(a):
\quad
d_S\le a\Rightarrow \boxtimes a\le d_S.
$$

This is the local condition already isolated in
`formalized-g2-implicational-aps.md`. It says that whenever $a$ is above the
consistency-like object $d_S$, the refutability of $a$ is absorbed by $d_S$.

Special cases:

$$
\mathrm{LG2}_S(\bot):
\quad
d_S\le\bot\Rightarrow \boxtimes\bot\le d_S,
$$

and:

$$
\forall a\in L\ \mathrm{LG2}_S(a).
$$

Under A2, $\mathrm{LG2}_S(\bot)$ implies ordinary G2:

$$
T\le\boxtimes\bot\le d_S\le\bot.
$$

Under antitonicity, global FG2 implies every local instance. Indeed, if
$d_S\le a$, then:

$$
\boxtimes a\le \boxtimes d_S\le d_S.
$$

Thus the hierarchy is:

$$
\mathrm{FG2}
\Longrightarrow
\forall a\,\mathrm{LG2}(a)
\Longrightarrow
\mathrm{LG2}(\bot)
\Longrightarrow
\mathrm{G2}
$$

provided the displayed uses of A1 and A2 are available.

## APS Morphisms

For pullbacks, use structure-preserving maps. A strict APS morphism

$$
f:S\to R
$$

from $S=(L_S,\le_S,\Box_S,\boxtimes_S,T_S,\bot_S)$ to
$R=(L_R,\le_R,\Box_R,\boxtimes_R,T_R,\bot_R)$ is a monotone map
$f:L_S\to L_R$ satisfying:

$$
f(T_S)=T_R,
\qquad
f(\bot_S)=\bot_R,
$$

$$
f(\Box_Sx)=\Box_Rf(x),
\qquad
f(\boxtimes_Sx)=\boxtimes_Rf(x).
$$

One can weaken strictness to inequalities when needed, but strict morphisms are
the clean setting for first pullback experiments.

## Pullback Construction

Given strict morphisms:

$$
S\xrightarrow{f}R\xleftarrow{g}S',
$$

define the pullback carrier:

$$
P=S\times_R S'
:=
\{(x,y)\in L_S\times L_{S'}:f(x)=g(y)\}.
$$

Order it componentwise:

$$
(x,y)\le_P(x',y')
\quad\Longleftrightarrow\quad
x\le_Sx'\ \text{and}\ y\le_{S'}y'.
$$

Define:

$$
T_P=(T_S,T_{S'}),
\qquad
\bot_P=(\bot_S,\bot_{S'}),
$$

and, when the operations preserve the equalizer condition:

$$
\Box_P(x,y)=(\Box_Sx,\Box_{S'}y),
$$

$$
\boxtimes_P(x,y)=(\boxtimes_Sx,\boxtimes_{S'}y).
$$

The compatibility condition is automatic for strict morphisms:

$$
f(\boxtimes_Sx)=\boxtimes_Rf(x)
=\boxtimes_Rg(y)=g(\boxtimes_{S'}y).
$$

### Lemma 1: Pullbacks Preserve the PreAPS Operations

If $f$ and $g$ are strict APS morphisms, then $P=S\times_R S'$ carries a
componentwise preAPS structure. If $\Box$ is monotone and $\boxtimes$ is
antitone in both $S$ and $S'$, then the same monotonicity/antitonicity holds in
$P$.

Proof. Closure of $P$ under $\Box$ and $\boxtimes$ follows from strictness.
Componentwise order gives the monotonicity statements immediately.

### Lemma 2: FG2 Is Componentwise in Products

For the direct product $S\times S'$,

$$
\mathrm{FG2}(S\times S')
$$

holds iff both $\mathrm{FG2}(S)$ and $\mathrm{FG2}(S')$ hold.

Proof. In the product:

$$
\boxtimes_{S\times S'}T_{S\times S'}
=
(\boxtimes_ST_S,\boxtimes_{S'}T_{S'}),
$$

and:

$$
\boxtimes^2_{S\times S'}T_{S\times S'}
=
(\boxtimes_S^2T_S,\boxtimes_{S'}^2T_{S'}).
$$

The product inequality is exactly the pair of component inequalities.

### Warning: G2 Is Not Purely Componentwise

In the product, the antecedent of G2 is:

$$
(\boxtimes_ST_S,\boxtimes_{S'}T_{S'})
\le
(\bot_S,\bot_{S'}).
$$

This is the conjunction of the two component antecedents. Therefore one
component can mask a G2 failure in the other component by making its antecedent
false. Pullbacks can therefore hide, reveal, or localize G2 failures depending
on the comparison map.

This is one reason local FG2 is useful: it records where the implication is
being tested, not only whether the global material implication happens to hold.

## Local Profiles

Define the local-FG2 profile of $S$:

$$
\mathrm{LG2Prof}(S)
:=
\{a\in L_S:\mathrm{LG2}_S(a)\}.
$$

For a morphism $f:S\to R$, define the relative profile over $r\in R$:

$$
\mathrm{LG2Prof}_f(r)
:=
\{a\in L_S:f(a)=r\ \text{and}\ \mathrm{LG2}_S(a)\}.
$$

For a pullback $P=S\times_R S'$, a local point is a compatible pair
$(a,a')$. The condition is:

$$
d_P\le(a,a')
\Rightarrow
\boxtimes_P(a,a')\le d_P,
$$

equivalently:

$$
d_S\le a,\ d_{S'}\le a'
\Rightarrow
\boxtimes_Sa\le d_S,\ \boxtimes_{S'}a'\le d_{S'}.
$$

Thus, in strict componentwise pullbacks, local profiles intersect along the
base. This gives a computable classification target.

## Model-Building Use

The G2-ZOO already includes models with the following profiles:

- FG2 without G2;
- G2 without FG2;
- G2 plus syntactic fixed point without FG2;
- G2 plus FG2 without syntactic fixed point;
- arbitrary first-true nFG2 depth.

Pullbacks should be used to test whether these profiles remain independent
after adding comparison structure. A typical experiment is:

1. choose two finite witnesses $S$ and $S'$;
2. define a common reduct $R$ that records only the consistency object, only
   the $\boxtimes$-orbit of $T$, or only the bottom-disciplined quotient;
3. compute $P=S\times_R S'$;
4. run the G2-ZOO checker on $P$;
5. compare local profiles before and after pullback.

## Candidate Interpretation of $M_G$ and $M_{GJ}$

Until the source is re-exported, use the following neutral placeholders.

### $M_G$

$M_G$ should denote a comparison model in which consistency is represented by a
Godel-style object, usually tied to a negated provability expression:

$$
g\approx \neg\Box T.
$$

If $\neg$ is unavailable in bare APS, $M_G$ should be treated as a reduct that
remembers the Godel-style fixed-point or consistency profile without forcing
$\boxtimes=\neg\Box$.

### $M_{GJ}$

$M_{GJ}$ should denote a model where Godel-style and Jeroslow/refutability-style
objects are compared. The relevant distinction is:

$$
p=\neg\Box p
$$

versus:

$$
p=\boxtimes p.
$$

The APS program must not identify these unless $\boxtimes$ is explicitly
defined as $\neg\Box$.

## Conjectures

### Conjecture 1: Pullback Separates Godel and Jeroslow Fixed Points

There are strict finite comparison diagrams

$$
M_G\to R\leftarrow M_{GJ}
$$

whose pullback has a Jeroslow/refutability fixed point but no Godel-style fixed
point, or conversely.

The purpose is to make precise the slogan:

$$
\text{primitive }\boxtimes\text{-fixed points are not the same as }
\neg\Box\text{-fixed points.}
$$

### Conjecture 2: Local FG2 Is Pullback-Stable Under Strict Morphisms

If $S$ and $S'$ satisfy local FG2 at all points over a base element $r\in R$,
then their pullback satisfies local FG2 at all compatible points over $r$.

This follows for strict componentwise pullbacks, but the real question is how
far it survives for lax morphisms or quotient-like comparison maps.

### Conjecture 3: G2-Independence Requires Local Profiles

The global truth value of G2 is too coarse to classify pullbacks. Two models
can have the same global G2 status but different $\mathrm{LG2Prof}$ sets, and
those differences should affect pullback behavior.

## Relation to Existing Notes

- `formalized-g2-implicational-aps.md` supplies the local-FG2 definition and
  the implication chain from FG2 to G2.
- `g2-aps-zoo-classification.md` gives the finite profiles that pullbacks
  should combine or separate.
- `indexed-aps-fibred-algebra.md` provides the categorical background: a
  pullback of APS models is a finite shadow of fibred/indexed semantics.
- `self-mutual-reference-hierarchy.md` is relevant when pullbacks create
  paired or networked fixed points rather than a single fixed point.

## Verification Tasks

1. Re-export the source share and replace the provisional readings of $M_G$
   and $M_{GJ}$ with exact definitions.
2. Add a strict APS morphism checker to `code/models/`.
3. Add product and pullback constructors for finite preAPS models.
4. Compute $\mathrm{LG2Prof}(S)$ for all current finite ZOO witnesses.
5. Search for a pullback witness separating:
   - Godel fixed point from Jeroslow fixed point;
   - global G2 from $\mathrm{LG2}(\bot)$;
   - FG2 from full local-FG2 profile.
6. Record whether bottom discipline is preserved by each pullback.
