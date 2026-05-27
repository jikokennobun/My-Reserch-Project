# Residuated Algebra, Domain Theory, and Completion

Source: https://chatgpt.com/share/6a0cbab3-b174-83ab-8a89-db8a746eacda

Imported: 2026-05-22

## Core Idea

\[
\text{residuated algebra}
=
\text{ordered algebra of implication, resource consumption, and weakest preconditions}.
\]

\[
\text{domain theory}
=
\text{order/topology of approximation, limits, and recursive fixed points}.
\]

Their meeting point is:

\[
\text{residuated dcpo / quantale / Scott-continuous residuated structure}.
\]

This is a natural setting for APS because it combines:

- implication and resource sensitivity,
- completion and limits,
- fixed point semantics,
- cut-elimination/completion stability questions.

## Residuated Side

Start with an ordered monoid:

\[
(A,\le,\otimes,e).
\]

Residuals exist when:

\[
a\otimes b\le c
\iff
b\le a\backslash c
\iff
a\le c/b.
\]

For fixed \(a\), the map

\[
L_a(b)=a\otimes b
\]

has right adjoint:

\[
a\backslash -.
\]

This makes implication a weakest-precondition operation.

## Domain-Theoretic Side

In a dcpo or continuous domain, recursive definitions are interpreted by least fixed points of Scott-continuous maps:

\[
\mu F = \bigvee_{n<\omega}F^n(\bot).
\]

The compatibility problem is:

Do \(\otimes,\backslash,/\), \(\Box\), and \(\boxtimes\) preserve directed joins or admit Scott-continuous extensions?

## Candidate Structures

- residuated dcpo
- quantale
- continuous quantale
- domain-enriched residuated lattice
- canonical extension of residuated lattices
- MacNeille completion with residuals

## APS Application

This note supports the broader program:

\[
\text{APS/G2 phenomena}
\quad\text{via}\quad
\text{residuated completions and domain-theoretic fixed points}.
\]

It connects directly to:

- BS16 cut elimination as completion stability.
- Analytic APS as topological/domain-theoretic APS.
- Completion-generated fixed points versus syntactic fixed points.

## Finite Search Result: M4 Obstruction

The non-degenerate finite G2+FG2+FP witness `M4-G2FG2FP` cannot be expanded to a
full residuated ordered monoid on its existing carrier and order. The exhaustive
search report
[../outputs/residuated-search-M4-G2FG2FP.json](../outputs/residuated-search-M4-G2FG2FP.json)
checks every binary tensor with each possible unit and finds no operation that
is associative, monotone, and admits both residuals.

This is a useful obstruction rather than a failure of the program. It says that
the current 4-element witness is genuinely a sparse preAPS artifact. A
residuated G2+FG2+FP witness likely requires at least one of:

- adding new order elements so residual downsets become principal;
- changing the underlying order while preserving the G2/FG2/FP behavior;
- weakening to one-sided or partial residuals;
- searching in a different finite family.

Pass 12 found the minimal same-carrier order repair. Adding the single relation
\(\bot\le c\) to `M4-G2FG2FP` makes the order into the diamond
\(\bot<p<T\), \(\bot<c<T\), \(p\parallel c\). The resulting model
`M4-G2FG2FP-order-plus-bot-c-residuated` has a full residuated monoid expansion
with unit \(p\), while preserving the G2+FG2+FP-reachable behavior. The tensor
has \(p\) as unit, \(\bot\) as zero, \(T\otimes T=T\), \(T\otimes c=c\), and
\(c\otimes c=\bot\).

The conceptual reading is now sharper. In `M4-G2FG2FP`, the constant named
\(\bot\) is not initially a least element: \(\bot\le p\) and \(\bot\le T\), but
\(\bot\not\le c\). The repair \(\bot\le c\) is therefore exactly the missing
instance of **bottom discipline**
\[
\forall x,\quad \bot\le x.
\]
Proof-theoretically, this is an ex-falso or absurdity-weakening principle for
the \(c\)-branch. Algebraically, it turns the order into the four-element
Boolean lattice with atoms \(p\) and \(c\), so residual fibers that previously
had no principal maximum can become principal. The repair is therefore not a
random order edge; it is the minimal bounded-order/lattice completion of the M4
witness. The remaining question is whether bottom discipline is intended in the
APS package under study, especially in the BS16 contraction-free setting.

Pass 14 tested bottom discipline as a finite-model filter. The report
`../outputs/bottom-discipline-filter-g2-zoo.json` shows that only `M-000`,
`M-010`, `M-111`, `M4-G2FG2FP`, and the already repaired M4 model remain
antitone after pure bottom-order enforcement. Full recorded behavior is stable
only for `M-111` and the M4 pair. The arbitrary-depth `nfg2-depth-3` witness
does not survive this enforcement: making its bottom element \(s\) below
\(T,a_1,a_2,a_3\) would require antitone image relations
\(a_1,a_2,a_3,a_4\le s\), which are absent. Thus bottom discipline is a real
structural filter, not just a notational cleanup.

Pass 15 supplies a bottom-disciplined replacement for the \(D_N\) idea by
separating the bottom constant \(b\) from the eventual fixed point \(s\) and
adding a helper upper bound \(U=\boxtimes b\). The checked depth-3 instance
`bottom-nfg2-depth-3` has G2 true, FG2 false, FP-synt at \(s\), and nFG2 pattern
`FFFTTTTT` while satisfying \(b\le x\) for every element.

Pass 18 shows that the checked depth-3 \(B_N\) instance also admits a
same-order full-residuated expansion. The template uses \(T\) as unit, \(b\) as
zero, and \(U\) as a top absorber:
\[
b\otimes x=b,\qquad T\otimes x=x,\qquad x\otimes y=U
\]
for all remaining nonzero, non-unit cases. The report
`../outputs/residuated-top-absorbing-report-bottom-nfg2-depth-3.json` verifies
associativity, monotonicity, principal left/right residuals, and the full
residuation law. The expansion
`bottom-nfg2-depth-3-residuated` preserves G2 true, FG2 false, FP-synt at \(s\),
bottom discipline, and nFG2 pattern `FFFTTTTT`.

Pass 19 promotes this from a checked instance to a uniform finite lemma. For
every \(B_N\), put \(M_N=B_N\setminus\{b,T\}\) and use the same tensor:
\(b\) is zero, \(T\) is unit, and every product inside \(M_N\) is \(U\).
Associativity follows because \(U\in M_N\) is absorbing after the first
non-unit/nonzero product. Monotonicity follows from the order generators
\(b\le x\), \(x\le U\), and \(s\le a_{N+1}\). The residual fibers are principal:
\[
b\backslash c=U,\quad T\backslash c=c,\quad
m\backslash c=
\begin{cases}
U & c=U,\\
T & m\le c\ne U,\\
b & \text{otherwise}
\end{cases}
\]
for \(m\in M_N\), with right residuals identical by commutativity. Therefore
the bottom-disciplined arbitrary-depth \(B_N\) separations all survive full
residuation on their original carrier/order. What remains mathematically
interesting is whether a less explosive tensor can do the same job.

Pass 20 answers this positively for the checked \(B_3\) instance under a
conservative \(U\)-absorbing search class. Keep \(T\) as unit, \(b\) as zero,
commutativity, and \(U\otimes x=U\) for every nonzero \(x\ne T\), but search
the remaining 15 products among \(a_1,a_2,a_3,a_4,s\). The complete constrained
search finds a full-residuated tensor with only 7 \(U\)-valued products, rather
than 15. The non-\(U\) products form the pattern
\[
a_1^2=a_3,\quad a_1a_4=a_1s=a_2,\quad
a_2a_4=a_2s=a_3,\quad a_4^2=a_4s=s^2=a_1.
\]
The resulting model `bottom-nfg2-depth-3-u-absorbing-minU` has the same
G2 true, FG2 false, FP-synt at \(s\), and nFG2 pattern `FFFTTTTT`. This
separates two questions: top-absorbing residuation is not minimal for \(B_3\),
but it remains open whether the 7-\(U\) pattern generalizes to \(B_N\), and
whether \(U\)-absorption itself is forced.

Pass 21 tests the same idea at depth 4. The direct branch-and-bound
\(U\)-absorbing search did not finish within the local 120-second pass budget,
but the pass 20 table has a truncated-exponent reading. Give \(a_{N+1}\) and
\(s\) exponent 1, give \(a_i\) exponent \(i+1\) for \(1\le i\le N\), and send
nonzero non-unit products to the element whose exponent is the sum when that
sum is at most \(N+1\), otherwise to \(U\). The builder
`../scripts/build-truncated-u-absorbing-residuated.py` verifies this template
for `bottom-nfg2-depth-4`: it is associative, monotone, and fully residuated on
the same carrier/order, with only 10 \(U\)-valued searched products out of 21
instead of the 21 forced by the top-absorbing tensor. The checker confirms that
the expanded model still has G2 true, FG2 false, FP-synt at \(s\), and nFG2
pattern `FFFFTTTT`.

Pass 22 closes the uniform existence question for this finer template. For
\(A_N=\{s,a_1,\ldots,a_{N+1}\}\), set \(e(s)=e(a_{N+1})=1\) and
\(e(a_i)=i+1\). Products in \(A_N\) add exponents until the sum would exceed
\(N+1\), at which point they become \(U\); \(T\) is still unit, \(b\) is zero,
and \(U\) is absorbing over nonzero non-units. Associativity is truncated
addition with overflow, and monotonicity follows from \(b\le x\), \(x\le U\),
and \(e(s)=e(a_{N+1})\) for the only nontrivial interior order
\(s\le a_{N+1}\). Residuals are principal: \(b\backslash c=U\),
\(T\backslash c=c\), \(U\backslash U=U\), \(U\backslash c=b\) for \(c\ne U\),
and for \(m\in A_N\), \(q=e(m)\),
\[
m\backslash c=
\begin{cases}
U & c=U,\\
T & m\le c,\\
\pi(t(c)-q) & c=a_i,\ 1\le i\le N,\ q<t(c),\\
b & \text{otherwise,}
\end{cases}
\]
where \(t(a_i)=i+1\), \(\pi(1)=a_{N+1}\), and
\(\pi(r)=a_{r-1}\) for \(r\ge2\). Right residuals are the same by
commutativity. Thus every \(B_N\) has this less top-collapsing full-residuated
same-order expansion; the remaining algebraic question is whether the
\(U\)-absorbing constraint itself is necessary.

Pass 23 separates two meanings of "weakening \(U\)-absorption." If the
truncated-exponent product table on \(A_N\) is held fixed, \(U\)-absorption is
forced before residuals enter. The reports
`../outputs/truncated-u-forcing-bottom-nfg2-depth-3.json` and
`../outputs/truncated-u-forcing-bottom-nfg2-depth-4.json` show that for every
\(y\in A_N\), some \(x\in A_N\) satisfies \(x\le U\) and \(x\otimes y=U\).
Monotonicity therefore yields \(U\le U\otimes y\), and topness of \(U\) gives
\(U\otimes y=U\). A second monotonicity step then gives \(U\otimes U=U\).
Thus a genuinely non-\(U\)-absorbing tensor must also modify the orbit product
table, not merely the action of \(U\) on the already fixed truncated template.

Pass 16 adds `bottom-G2FG2-noFP`, a 5-element bottom-disciplined witness for
G2+FG2 without FP-synt. It again uses a true bottom \(b\) and helper upper bound
\(U\), but the \(T\)-orbit is \(T\to a\to d\to a\to\cdots\) with \(d\le a\).
This makes FG2 true while keeping \(a,d\) as a strict two-cycle, so no syntactic
\(\boxtimes\)-fixed point appears.

Pass 17 shows that this witness is not merely pre-residuated. The broad
unrestricted tensor search is too large on five elements
(\(5^{16}=152587890625\) candidates per unit), so the report
`../outputs/residuated-search-bottom-G2FG2-noFP.json` now correctly records the
unrestricted search as not run. A targeted commutative search with unit \(T\)
and zero \(b\) reduces the space to \(5^6=15625\) candidates and finds 8 full
residuated tensors. The persisted model
`bottom-G2FG2-noFP-residuated` keeps the same order, G2/FG2/no-FP behavior, and
bottom discipline while adding full residuals.

## Next Tasks

- Define "residuated dcpo" carefully.
- Check which residuals are Scott-continuous or preserve meets/joins.
- Compare quantale completion with MacNeille completion.
- Find examples where completion creates a fixed point not present syntactically.
- Connect Galatos-Jipsen-Kowalski-Ono style residuated lattices with APS/G2-ZOO.
- Test bottom discipline against the BS16/resource-sensitive reading: decide
  whether ex-falso weakening is acceptable without reintroducing hidden
  contraction.
- Search whether the \(D_N\) nFG2-depth family admits analogous finite
  residuated repairs.
- Test whether the \(U\)-absorbing assumption is forced by same-order full
  residuation or can be weakened further.

## Related References and Drive Files

- Galatos, Jipsen, Kowalski, Ono, *Residuated Lattices: An Algebraic Glimpse at Substructural Logics*.
- [algebraic_reverse_math_g2_aps.pdf](https://drive.google.com/file/d/1JoGMqK-9uQqC2Qp3490G2ZJvMj9N5DTe)
- [Incompleteness_Algebraic_Reverse_Mathematics_Thesis_コピー.pdf](https://drive.google.com/file/d/1p1r0-FLjAF9x9d_OvXm1HqgC1xF_NYk_)
- [APS_dissertation.pdf](https://drive.google.com/file/d/1VtS6tSvhUcoIG01fWprIrxGKZ3vZPjxc)
