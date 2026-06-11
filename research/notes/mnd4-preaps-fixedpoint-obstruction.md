# MND4-preAPS and Fixed Point Obstruction

## Source and Provenance

- Primary shared-link source: https://chatgpt.com/share/6a0fbc5a-a86c-8322-8ce7-1888af5f455e
- Imported from shared-link watchlist: 2026-05-22
- Shared-link access status on 2026-06-11: inaccessible from this environment; `records/logs/chatgpt-share-state.csv` records `error` with remote connection failure.
- Drive supplements used for mathematical reconstruction on 2026-06-11:
  - [Double APS と MND4-preAPS における固定点・崩壊・定義可能性](https://drive.google.com/file/d/1AwBiM1z2A7fOL4RSe3izVG6w7P64Pc84/view?usp=drivesdk)
  - [Relative MND4-APS](https://drive.google.com/file/d/1dCRpoENyBwlS8Xzqc6YYI935nXgSyScM/view?usp=drivesdk)
- The discussion below separates direct extraction from these Drive PDFs from reconstruction of how they refine the original shared-link topic.

## Abstract

The core issue is to distinguish two fixed-point mechanisms that look similar in a thin summary but behave very differently in algebraic semantics for incompleteness:

$$
p =_S \boxtimes p
\quad\text{versus}\quad
p =_S \neg \Box p.
$$

Primitive refutability fixed points of the first kind can live in nontrivial
MND4-style pre-APS models. By contrast, once refutability is identified with
classical negated provability and enough explosion/contraction structure is
available, a Godel-style fixed point forces collapse:

$$
\text{Classical MND4-preAPS} + \exists p\,(p =_S \neg \Box p)
\Longrightarrow
T \le \bot.
$$

The new Drive material sharpens this in two directions. First, it gives explicit
finite and infinite countermodels showing that primitive $\boxtimes$-fixed
points do not trivialize MND4-preAPS. Second, it proposes a relative/two-level
semantics in which the MND4 rules act only on a safe fragment $D$, while the
fixed point lives in an ambient structure $S \setminus i[D]$. The real
obstruction is therefore not mere existence of fixed points, but leakage of
self-reference into the fragment on which the MND4 rules are allowed to act.

## Background and Notation

We keep the repository-wide APS notation

$$
S=(L,\le,\Box,\boxtimes,T,\bot).
$$

Here:

- $T \le x$ means "$x$ is provable".
- $x \le \bot$ means "$x$ is refutable".
- $\Box x$ is provability.
- $\boxtimes x$ is refutability, either primitive or defined from $\Box$ and
  negation.

The main ambiguity is whether $\boxtimes$ is:

1. a primitive operation, as in Beklemishev-Shamkanov style abstract G2; or
2. shorthand for $\Box \neg x$ or, equivalently in classical notation,
   refutability via $\neg \Box x$.

The Drive supplements use "MND4-preAPS" for a weaker structure than a full APS.
Following that convention, I will write $\Box$ for provability and reserve
$\boxtimes$ for abstract refutability.

## Definitions

### MND4-preAPS

An MND4-preAPS is a structure

$$
S=(L,\le,\Box,\boxtimes,T,\bot)
$$

with preorder $\le$ and the following conditions:

$$
\text{M}: x \le y \Rightarrow \Box x \le \Box y,
$$

$$
\text{N}: T \le x \Rightarrow T \le \Box x,
$$

$$
\text{D}: \Box x \perp \boxtimes x,
$$

$$
4: \Box x \le \Box\Box x.
$$

The key point is that this is not yet the same as a full APS. In particular,
the APS axiom

$$
\text{A4}: \boxtimes x \le \Box \boxtimes x
$$

is not the same as the modal 4-condition above. This distinction matters in the
fixed-point arguments.

### Classical MND4-preAPS

The collapse theorem uses a stronger package with a classical involutive
negation $\neg$ satisfying

$$
x \le y \Rightarrow \neg y \le \neg x,
\qquad
\neg\neg x =_S x,
\qquad
\neg \bot =_S T,
$$

and interprets refutability through provability of negation. At the level of
informal reading, the fixed point becomes

$$
p =_S \neg \Box p.
$$

The Drive reconstruction also isolates a relative explosion law:

$$
z \le y,\quad z \le \neg y
\Longrightarrow
z \le \bot.
$$

This is the ingredient that converts simultaneous proof/refutation information
into outright inconsistency.

### Relative MND4-APS

The second Drive PDF proposes a two-level structure

$$
R=(D,S,\le_D,\le_S,T_D,\bot_D,T_S,\bot_S,\Box_D,\boxtimes_D,\Box_S,\boxtimes_S,i),
$$

where:

- $D$ is a safe fragment;
- $S$ is an ambient universe allowing self-reference;
- $i:D \to S$ is an order-preserving embedding preserving at least $T$, $\bot$,
  and $\Box$;
- the MND4 rules are required only on $D$;
- external fixed points are allowed in $S \setminus i[D]$.

The no-leak condition is:

$$
\operatorname{Diag}_{\boxtimes}(S)\cap i[D]=\varnothing,
$$

where $\operatorname{Diag}_{\boxtimes}(S)=\{p\in S : p =_S \boxtimes p\}$, or
in the Godel-style version the analogous $\neg\Box$-fixed-point set.

This formulation is the cleanest mathematical expression of the thesis:

$$
\text{MND4 rules act only on the safe fragment, fixed points live outside it.}
$$

## Main Claims

### Proposition 1. Primitive refutability fixed points do not force collapse.

The strongest correction to the earlier thin note is that

$$
\exists p\,(p =_S \boxtimes p)
$$

is not by itself destructive. The Drive reconstruction gives explicit small
models where a primitive refutability fixed point exists while the structure is
nontrivial. So the naive implication

$$
MND4\text{-preAPS} + \exists p\,(p=\boxtimes p)
\Rightarrow
T\le\bot
$$

is false.

### Theorem 2. Classical Godel fixed points collapse Classical MND4-preAPS.

Under the classical package, if

$$
\exists p\,(p =_S \neg\Box p),
$$

then

$$
T \le \bot.
$$

#### Proof sketch

The idea is standard but the Drive text makes the dependency structure clear.

1. Assume $p =_S \neg\Box p$.
2. Use the M/N/D/4 package together with the involutive classical reading of
   refutability to derive both provability-side and refutability-side
   information about $p$.
3. Apply the relative explosion principle to these two pieces of information.
4. Conclude $T \le \bot$.

The moral is that the collapse is not caused by "having a fixed point" in the
abstract, but by allowing the MND4 rules to apply to a Godel sentence inside a
classical environment where proof and refutation can be fused.

### Proposition 3. The obstruction is a definability/no-leak obstruction.

If a fixed point $p$ is definable inside the safe fragment, then the rules of
that fragment apply to $p$, and the collapse mechanism restarts. Therefore in a
nontrivial Double/Relative APS the fixed point must satisfy

$$
p \in S \setminus \operatorname{Def}(D).
$$

Equivalently: the semantic space supporting self-reference must be larger than
the syntactic or theorem-safe core.

## Examples and Counterexamples

### Example 1. Three-valued Lukasiewicz witness

The Drive supplement identifies the three-valued Lukasiewicz chain

$$
0 < \tfrac12 < 1
$$

with $\Box=\mathrm{id}$ as the cleanest small residuated witness for a
Godel-style fixed point outside the definable classical core. The midpoint

$$
\tfrac12 = \neg \Box \tfrac12
$$

acts as a fixed point, while $\{0,1\}$ can remain the definable/classical
fragment. This is exactly the kind of two-level separation the earlier thin
summary only gestured at.

### Example 2. Central-antichain pathology

For any set $I$, let

$$
M_I=\{0,1\}\cup\{m_i : i\in I\},
$$

ordered by

$$
0 < m_i < 1
$$

with distinct $m_i$ incomparable, involution $\neg m_i = m_i$, and
$\Box=\mathrm{id}$. Then every $m_i$ satisfies

$$
m_i = \neg \Box m_i.
$$

So one gets arbitrarily many fixed points, but relative explosion fails exactly
at the middle points. This shows that fixed-point cardinality is not the right
invariant by itself; the key issue is which additional classical/explosive laws
hold.

### Example 3. Relative safe-fragment toy model

The relative MND4 note builds small two-level toy models where:

- $D$ is a tiny safe algebra closed under the operations relevant to MND4;
- $S$ contains an extra element $p$ with $p=\boxtimes p$;
- $p \notin i[D]$.

Such models witness that "external self-reference" is algebraically coherent
provided the rules cannot leak from $D$ onto $p$.

### Counterexample schema

The Drive texts also list sharp failure modes:

- if $N$ fails, fixed points can appear too easily;
- if $D$ fails, proof/refutation orthogonality is too weak;
- if modal $4$ fails, finite Boolean countermodels reappear;
- if relative explosion fails, nonclassical fixed-point carriers survive.

So the collapse theorem is structurally exact: it uses a full package, not just
one modal axiom.

## Relation to Existing Notes

- [`research/notes/bs16-fiber-residuated-aps.md`](bs16-fiber-residuated-aps.md):
  this note clarifies why the Beklemishev-Shamkanov abstract G2 theorem should
  be compared with primitive $\boxtimes$-fixed points, not immediately with
  classical Godel sentences.
- [`research/notes/g2-fg2-hierarchy.md`](g2-fg2-hierarchy.md):
  the thin fixed-point discussion there is refined by the present distinction
  between primitive fixed points, classical $\neg\Box$-fixed points, and
  fragment-relative fixed points.
- [`research/notes/formalized-g2-implicational-aps.md`](formalized-g2-implicational-aps.md):
  the current note suggests a further split between what is formalizable inside
  a safe implicational fragment and what must remain external.
- [`research/notes/provability-predicate-weak-aps.md`](provability-predicate-weak-aps.md):
  the "no leak" principle is a semantic counterpart of weakening the
  derivability interface rather than the fixed-point principle itself.

## Finite-Model and Verification Tasks

1. Build a finite explicit relative MND4-APS in `code/models/` whose safe
   fragment $D$ satisfies the MND4 package while the ambient carrier contains a
   primitive fixed point outside $D$.
2. Search for the minimal residuated example where the definable fragment is
   classical but the ambient carrier contains a non-definable
   $\neg\Box$-fixed-point analogue without collapse.
3. Formalize the no-leak condition as an invariant check:

   $$
   \operatorname{Diag}_{\boxtimes}(S)\cap i[D]=\varnothing.
   $$

4. Compare the safe-fragment condition with existing G2/FG2 witnesses in
   `code/models/examples/`: which witnesses already admit a two-level
   interpretation?

## Open Problems

1. Find an arithmetically natural safe class $D$ of sentences such that

   $$
   MND4 \subseteq PL_D(\operatorname{Pr})
   $$

   while diagonal fixed points still exist in the ambient universe.
2. Determine whether the no-leak condition is best formulated as a definability
   prohibition, a fiber condition, or a reflective-subcategory condition in a
   categorical semantics.
3. Classify which closure notions on $D$ are safe: closure under provability,
   term operations, parameters, Scott closure, or computable generation may
   behave very differently.
4. Relate the relative-fragment formulation to the repository's broader A3/A4
   and cut-stability program: is "safe fragment versus ambient self-reference"
   another instance of the same saturation-versus-closure tension?
