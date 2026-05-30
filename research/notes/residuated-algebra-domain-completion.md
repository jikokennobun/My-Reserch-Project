# Residuated Algebra, Domain Theory, and Completion

Source: https://chatgpt.com/share/6a0cbab3-b174-83ab-8a89-db8a746eacda

Imported: 2026-05-22

Rechecked from user-supplied shared-link batch: 2026-05-30

The refreshed share also links this axis to algebraic proof theory and
Abstract Geometry of Interaction: residuated algebra gives the order-theoretic
semantics of assumptions and implication; completions such as MacNeille,
ideal, canonical, or quantale completions extend that semantics to infinitary
or relational settings; cut elimination is then read as a conservativity or
stability property of the completion; Abstract GoI reads cut elimination as a
dynamic feedback computation over the completed algebra.

The share reports generated files named `residuated_completion_goi_notes.pdf`
and `residuated_completion_goi_notes.tex`. They appear as
`sandbox:/mnt/data/...` links from the ChatGPT session and are not directly
readable from this local repository environment. If exported to the Google
Drive artifact inbox, they can be imported into `artifacts/` by
`code/scripts/sync-chatgpt-project-artifacts.ps1`.

## Core Idea

$$
\text{residuated algebra}
=
\text{ordered algebra of implication, resource consumption, and weakest preconditions}.
$$

$$
\text{domain theory}
=
\text{order/topology of approximation, limits, and recursive fixed points}.
$$

Their meeting point is:

$$
\text{residuated dcpo / quantale / Scott-continuous residuated structure}.
$$

This is a natural setting for APS because it combines:

- implication and resource sensitivity,
- completion and limits,
- fixed point semantics,
- cut-elimination/completion stability questions.

## Residuated Side

Start with an ordered monoid:

$$
(A,\le,\otimes,e).
$$

Residuals exist when:

$$
a\otimes b\le c
\iff
b\le a\backslash c
\iff
a\le c/b.
$$

For fixed $a$, the map

$$
L_a(b)=a\otimes b
$$

has right adjoint:

$$
a\backslash -.
$$

This makes implication a weakest-precondition operation.

## Domain-Theoretic Side

In a dcpo or continuous domain, recursive definitions are interpreted by least fixed points of Scott-continuous maps:

$$
\mu F = \bigvee_{n<\omega}F^n(\bot).
$$

The compatibility problem is:

Do $\otimes,\backslash,/$, $\Box$, and $\boxtimes$ preserve directed joins or admit Scott-continuous extensions?

## Candidate Structures

- residuated dcpo
- quantale
- continuous quantale
- domain-enriched residuated lattice
- canonical extension of residuated lattices
- MacNeille completion with residuals

## APS Application

This note supports the broader program:

$$
\text{APS/G2 phenomena}
\quad\text{via}\quad
\text{residuated completions and domain-theoretic fixed points}.
$$

It connects directly to:

- BS16 cut elimination as completion stability.
- Analytic APS as topological/domain-theoretic APS.
- Completion-generated fixed points versus syntactic fixed points.

## Finite Search Result: M4 Obstruction

The non-degenerate finite G2+FG2+FP witness `M4-G2FG2FP` cannot be expanded to a
full residuated ordered monoid on its existing carrier and order. The exhaustive
search report
[../../artifacts/reports/residuated-search-M4-G2FG2FP.json](../../artifacts/reports/residuated-search-M4-G2FG2FP.json)
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
$\bot\le c$ to `M4-G2FG2FP` makes the order into the diamond
$\bot<p<T$, $\bot<c<T$, $p\parallel c$. The resulting model
`M4-G2FG2FP-order-plus-bot-c-residuated` has a full residuated monoid expansion
with unit $p$, while preserving the G2+FG2+FP-reachable behavior. The tensor
has $p$ as unit, $\bot$ as zero, $T\otimes T=T$, $T\otimes c=c$, and
$c\otimes c=\bot$.

The conceptual reading is now sharper. In `M4-G2FG2FP`, the constant named
$\bot$ is not initially a least element: $\bot\le p$ and $\bot\le T$, but
$\bot\not\le c$. The repair $\bot\le c$ is therefore exactly the missing
instance of **bottom discipline**
$$
\forall x,\quad \bot\le x.
$$
Proof-theoretically, this is an ex-falso or absurdity-weakening principle for
the $c$-branch. Algebraically, it turns the order into the four-element
Boolean lattice with atoms $p$ and $c$, so residual fibers that previously
had no principal maximum can become principal. The repair is therefore not a
random order edge; it is the minimal bounded-order/lattice completion of the M4
witness. The remaining question is whether bottom discipline is intended in the
APS package under study, especially in the BS16 contraction-free setting.

Pass 14 tested bottom discipline as a finite-model filter. The report
`../../artifacts/reports/bottom-discipline-filter-g2-zoo.json` shows that only `M-000`,
`M-010`, `M-111`, `M4-G2FG2FP`, and the already repaired M4 model remain
antitone after pure bottom-order enforcement. Full recorded behavior is stable
only for `M-111` and the M4 pair. The arbitrary-depth `nfg2-depth-3` witness
does not survive this enforcement: making its bottom element $s$ below
$T,a_1,a_2,a_3$ would require antitone image relations
$a_1,a_2,a_3,a_4\le s$, which are absent. Thus bottom discipline is a real
structural filter, not just a notational cleanup.

Pass 15 supplies a bottom-disciplined replacement for the $D_N$ idea by
separating the bottom constant $b$ from the eventual fixed point $s$ and
adding a helper upper bound $U=\boxtimes b$. The checked depth-3 instance
`bottom-nfg2-depth-3` has G2 true, FG2 false, FP-synt at $s$, and nFG2 pattern
`FFFTTTTT` while satisfying $b\le x$ for every element.

Pass 18 shows that the checked depth-3 $B_N$ instance also admits a
same-order full-residuated expansion. The template uses $T$ as unit, $b$ as
zero, and $U$ as a top absorber:
$$
b\otimes x=b,\qquad T\otimes x=x,\qquad x\otimes y=U
$$
for all remaining nonzero, non-unit cases. The report
`../../artifacts/reports/residuated-top-absorbing-report-bottom-nfg2-depth-3.json` verifies
associativity, monotonicity, principal left/right residuals, and the full
residuation law. The expansion
`bottom-nfg2-depth-3-residuated` preserves G2 true, FG2 false, FP-synt at $s$,
bottom discipline, and nFG2 pattern `FFFTTTTT`.

Pass 19 promotes this from a checked instance to a uniform finite lemma. For
every $B_N$, put $M_N=B_N\setminus\{b,T\}$ and use the same tensor:
$b$ is zero, $T$ is unit, and every product inside $M_N$ is $U$.
Associativity follows because $U\in M_N$ is absorbing after the first
non-unit/nonzero product. Monotonicity follows from the order generators
$b\le x$, $x\le U$, and $s\le a_{N+1}$. The residual fibers are principal:
$$
b\backslash c=U,\quad T\backslash c=c,\quad
m\backslash c=
\begin{cases}
U & c=U,\\
T & m\le c\ne U,\\
b & \text{otherwise}
\end{cases}
$$
for $m\in M_N$, with right residuals identical by commutativity. Therefore
the bottom-disciplined arbitrary-depth $B_N$ separations all survive full
residuation on their original carrier/order. What remains mathematically
interesting is whether a less explosive tensor can do the same job.

Pass 20 answers this positively for the checked $B_3$ instance under a
conservative $U$-absorbing search class. Keep $T$ as unit, $b$ as zero,
commutativity, and $U\otimes x=U$ for every nonzero $x\ne T$, but search
the remaining 15 products among $a_1,a_2,a_3,a_4,s$. The complete constrained
search finds a full-residuated tensor with only 7 $U$-valued products, rather
than 15. The non-$U$ products form the pattern
$$
a_1^2=a_3,\quad a_1a_4=a_1s=a_2,\quad
a_2a_4=a_2s=a_3,\quad a_4^2=a_4s=s^2=a_1.
$$
The resulting model `bottom-nfg2-depth-3-u-absorbing-minU` has the same
G2 true, FG2 false, FP-synt at $s$, and nFG2 pattern `FFFTTTTT`. This
separates two questions: top-absorbing residuation is not minimal for $B_3$,
but it remains open whether the 7-$U$ pattern generalizes to $B_N$, and
whether $U$-absorption itself is forced.

Pass 21 tests the same idea at depth 4. The direct branch-and-bound
$U$-absorbing search did not finish within the local 120-second pass budget,
but the pass 20 table has a truncated-exponent reading. Give $a_{N+1}$ and
$s$ exponent 1, give $a_i$ exponent $i+1$ for $1\le i\le N$, and send
nonzero non-unit products to the element whose exponent is the sum when that
sum is at most $N+1$, otherwise to $U$. The builder
`../../code/scripts/build-truncated-u-absorbing-residuated.py` verifies this template
for `bottom-nfg2-depth-4`: it is associative, monotone, and fully residuated on
the same carrier/order, with only 10 $U$-valued searched products out of 21
instead of the 21 forced by the top-absorbing tensor. The checker confirms that
the expanded model still has G2 true, FG2 false, FP-synt at $s$, and nFG2
pattern `FFFFTTTT`.

Pass 22 closes the uniform existence question for this finer template. For
$A_N=\{s,a_1,\ldots,a_{N+1}\}$, set $e(s)=e(a_{N+1})=1$ and
$e(a_i)=i+1$. Products in $A_N$ add exponents until the sum would exceed
$N+1$, at which point they become $U$; $T$ is still unit, $b$ is zero,
and $U$ is absorbing over nonzero non-units. Associativity is truncated
addition with overflow, and monotonicity follows from $b\le x$, $x\le U$,
and $e(s)=e(a_{N+1})$ for the only nontrivial interior order
$s\le a_{N+1}$. Residuals are principal: $b\backslash c=U$,
$T\backslash c=c$, $U\backslash U=U$, $U\backslash c=b$ for $c\ne U$,
and for $m\in A_N$, $q=e(m)$,
$$
m\backslash c=
\begin{cases}
U & c=U,\\
T & m\le c,\\
\pi(t(c)-q) & c=a_i,\ 1\le i\le N,\ q<t(c),\\
b & \text{otherwise,}
\end{cases}
$$
where $t(a_i)=i+1$, $\pi(1)=a_{N+1}$, and
$\pi(r)=a_{r-1}$ for $r\ge2$. Right residuals are the same by
commutativity. Thus every $B_N$ has this less top-collapsing full-residuated
same-order expansion; the remaining algebraic question is whether the
$U$-absorbing constraint itself is necessary.

Pass 23 separates two meanings of "weakening $U$-absorption." If the
truncated-exponent product table on $A_N$ is held fixed, $U$-absorption is
forced before residuals enter. The reports
`../../artifacts/reports/truncated-u-forcing-bottom-nfg2-depth-3.json` and
`../../artifacts/reports/truncated-u-forcing-bottom-nfg2-depth-4.json` show that for every
$y\in A_N$, some $x\in A_N$ satisfies $x\le U$ and $x\otimes y=U$.
Monotonicity therefore yields $U\le U\otimes y$, and topness of $U$ gives
$U\otimes y=U$. A second monotonicity step then gives $U\otimes U=U$.
Thus a genuinely non-$U$-absorbing tensor must also modify the orbit product
table, not merely the action of $U$ on the already fixed truncated template.

Pass 24 implements the first broader search for such a tensor on the checked
B3 instance. The search fixes only commutativity, unit $T$, and zero $b$;
it allows both $U$-products and the orbit product table to vary, subject to
same-order monotonicity, associativity, and principal residual fibers. The
bounded report
`../../artifacts/reports/residuated-non-u-absorbing-search-bottom-nfg2-depth-3.json` checks
382 complete assignments inside 1000 search nodes and finds no candidate, but
the search is incomplete. The failure mode is useful: without residual-fiber
pruning the unrestricted orbit-table search is too slow to complete in the
local pass budget.

Pass 25 adds partial residual-fiber pruning and completes the B3 search. The
result is positive: `bottom-nfg2-depth-3-non-u-absorbing` is a same-order
full-residuated expansion with $T$ as unit and $b$ as zero, but without
$U$-absorption. Specifically $U\otimes a_4=a_4$ and $U\otimes s=s$. The
price is that the orbit table changes from truncated addition to a mixed
group/idempotent/zero pattern: $a_1,a_2,a_3$ form a Klein-four subgroup over
$T$, $a_4$ is fixed by multiplication with those three elements, and
$a_4s=s^2=b$. The checker report
`../../artifacts/reports/g2-zoo-bottom-nfg2-depth-3-non-u-absorbing.json` confirms that the
G2/FG2/FP/nFG2 profile is unchanged. Therefore $U$-absorption is not forced
by same-order full residuation on $B_3$; it is only forced if the truncated
orbit table is held fixed.

Pass 26 shows that non-$U$-absorption is not confined to checked depth 3. A
bounded run of the same search on `bottom-nfg2-depth-4` finds
`bottom-nfg2-depth-4-non-u-absorbing`, a full-residuated same-order expansion
whose residuals are principal and whose G2-ZOO profile remains `FFFFTTTT`. The
search report is positive but incomplete for optimization: it stops at 1000
nodes, after 48 $U$-action patterns and 147 complete assignments. The found
tensor differs from the B3 pattern. Here $U$ fixes $a_1$ and $a_2$, while
$U\otimes a_3=U\otimes a_4=U\otimes a_5=U\otimes s=U$. Thus the current
evidence says that same-order full residuation permits non-$U$-absorbing
repairs at both checked depths, but the uniform algebraic explanation remains
open.

Pass 27 gives the first uniform explanation candidate. The
front-shifted template keeps $T$ as unit and $b$ as zero, makes
$a_1,a_2$ orthogonal idempotents, lets $U$ fix exactly those two front
elements, and puts a shifted truncated-exponent product on
$\{s,a_{N+1},a_3,\ldots,a_N\}$. The builder
`../../code/scripts/build-front-shifted-non-u-absorbing-residuated.py` verifies full
residuation for `bottom-nfg2-depth-3`, `bottom-nfg2-depth-4`, and the newly
generated `bottom-nfg2-depth-5`. The depth-4 template is exactly the pass 26
bounded-search witness; the depth-3 template is a different valid
non-$U$-absorbing repair than the earlier max-non-$U$ search witness. The
uniform theorem is now reduced to a symbolic residual-table proof for this
front/tail decomposition.

Pass 28 records the residual table and verifies it against the checked models.
For front elements $p$, $p\backslash c$ is either $U$ when $c$ is
$p$ or $U$, or the opposite front element otherwise. For $U$, the
residual is $U$ at target $U$, the front target itself at front targets,
and $b$ otherwise. For tail elements $r$, front targets again return that
front element; tail targets are controlled by shifted exponent subtraction,
with the duplicate exponent-1 case generating the principal downset
$\downarrow a_{N+1}$. The formula is now implemented in
`../../code/scripts/check-front-shifted-residual-formula.py`, and the reports
`../../artifacts/reports/front-shifted-residual-table-check-bottom-nfg2-depth-{3,4,5}.json`
show zero mismatches against both left and right residuals. This turns the
front-shifted construction from a checked schema into a uniform full-residuated
$B_N$ template, modulo ordinary presentation polishing.

Pass 29 compares structural rules across the current residuated examples. The
report `../../artifacts/reports/structural-rules-front-shifted-comparison.json` shows a
consistent resource-sensitive pattern. Exchange holds for every checked
tensor. Strong weakening $a\le b\Rightarrow a\otimes c\le b$ fails for every
checked tensor, as does its reflexive discarding instance $a\otimes c\le a$;
the unit $T$ already forces this when $c\not\le T$. Global contraction
$a\otimes a\le a$ holds only for `bottom-G2FG2-noFP-residuated`. The
front-shifted $B_N$ tensor is therefore best read as a local contraction
construction: the front idempotents $a_1,a_2$ are contractive, while the
shifted tail carries the noncontractive behavior required by the nFG2-depth
separation.

Pass 30 makes that reading precise as an ideal extension. Let
$$
I=\{b,a_1,a_2\}.
$$
In the front-shifted template, $I$ is downward closed and satisfies
$I\otimes L\subseteq I$, so it is a two-sided tensor ideal. Its nonzero part
is a two-atom orthogonal idempotent zero-band. The quotient that collapses
$I$ to $b$ has representatives
$$
\{b,T,U,s,a_{N+1},a_3,\ldots,a_N\}
$$
and carries exactly the shifted truncated tail tensor. The finite report
`../../artifacts/reports/front-shifted-extension-presentation-check.json` verifies the
order-ideal condition, tensor-ideal condition, front zero-band, front action,
tail quotient product, and tail quotient order shape for depths 3, 4, and 5.
Thus the construction is an ideal extension of a resource-sensitive tail by a
contractive front ideal, not a product decomposition.

Pass 31 checks the size bound for this kind of front ideal. The generalized
schema uses an orthogonal idempotent front
$$
F_k=\{a_1,\ldots,a_k\}
$$
and shifts the tail to $\{s,a_{N+1},a_{k+1},\ldots,a_N\}$. The report
`../../artifacts/reports/front-ideal-size-bound-check.json` checks depths 3, 4, and 5. The
positive cases are $k=0,1,2$; the first failure is always $k=3$, and the
witness is a non-principal residual fiber. For $p\in F_k$, the set of
right-multipliers sending $p$ below $b$ contains
$\{b\}\cup(F_k\setminus\{p\})$, which has no single maximum when
$\lvert F_k\setminus\{p\}\rvert\ge2$. This gives a concrete same-order obstruction to
front ideals of width at least three in the orthogonal-front schema.

Pass 32 adds the closed residual formula for the positive widths. For
$k=0,1,2$, the tail residuals are shifted exponent subtraction with
$\rho_k(1)=a_{N+1}$ and $\rho_k(d)=a_{k+d-1}$. The front clause says:
for $p\in F_k$, $p\backslash c=U$ at $c=p,U$; otherwise it is $b$ when
$k=1$, and the other front atom when $k=2$. Together with
$b\backslash c=U$, $T\backslash c=c$, and the usual $U$-row, this gives
a uniform residual table for widths $0,1,2$. The report
`../../artifacts/reports/front-width-residual-formula-check.json` verifies zero mismatches
against generated residuals for the checked depths 3, 4, and 5.

Pass 16 adds `bottom-G2FG2-noFP`, a 5-element bottom-disciplined witness for
G2+FG2 without FP-synt. It again uses a true bottom $b$ and helper upper bound
$U$, but the $T$-orbit is $T\to a\to d\to a\to\cdots$ with $d\le a$.
This makes FG2 true while keeping $a,d$ as a strict two-cycle, so no syntactic
$\boxtimes$-fixed point appears.

Pass 17 shows that this witness is not merely pre-residuated. The broad
unrestricted tensor search is too large on five elements
($5^{16}=152587890625$ candidates per unit), so the report
`../../artifacts/reports/residuated-search-bottom-G2FG2-noFP.json` now correctly records the
unrestricted search as not run. A targeted commutative search with unit $T$
and zero $b$ reduces the space to $5^6=15625$ candidates and finds 8 full
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
- Search whether the $D_N$ nFG2-depth family admits analogous finite
  residuated repairs.
- Test non-orthogonal front ideals or mild front-order refinements as possible
  ways around the $k\ge3$ non-principal residual-fiber obstruction.

## Related References and Drive Files

- Galatos, Jipsen, Kowalski, Ono, *Residuated Lattices: An Algebraic Glimpse at Substructural Logics*.
- [algebraic_reverse_math_g2_aps.pdf](https://drive.google.com/file/d/1JoGMqK-9uQqC2Qp3490G2ZJvMj9N5DTe)
- [Incompleteness_Algebraic_Reverse_Mathematics_Thesis_コピー.pdf](https://drive.google.com/file/d/1p1r0-FLjAF9x9d_OvXm1HqgC1xF_NYk_)
- [APS_dissertation.pdf](https://drive.google.com/file/d/1VtS6tSvhUcoIG01fWprIrxGKZ3vZPjxc)
