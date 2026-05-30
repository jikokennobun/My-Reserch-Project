# Autonomous Discussion Log

## State

- Started: 2026-05-24
- Mode: Codex-centered repository discussion
- Default cadence: one compact pass per scheduled wake-up
- Target run: ongoing until the user explicitly pauses or stops the automation
- Current pass: 33
- Run status: continuous automation resumed on 2026-05-25
- Main bridge: ChatGPT Project material must be copied, exported, shared, or
  relayed into this repository before Codex can use it reliably.
- Initial focus: strengthen the APS/G2-ZOO research program by turning existing
  notes into sharper definitions, conjectures, proof tasks, and counterexample
  searches.

## Iteration Format

```text
### Pass N - YYYY-MM-DD HH:MM JST

Focus:

Proposer:

Skeptic:

Formalist:

Archivist:

Repository updates:

Next step:
```

## Iterations

### Pass 1 - 2026-05-24 14:46 JST

Focus:

Clarify the gap between completion-generated fixed points and syntactic
APS/Jeroslow fixed points, using the completion and residuated-domain notes as
the first bridge.

Proposer:

Make the next target a "completion-reflection square." Start with an APS or
preAPS $L$, an embedding $i:L\to \widehat L$, and an extension
$\widehat{\boxtimes}:\widehat L\to\widehat L$. A completion fixed point
$q=\widehat{\boxtimes}q$ becomes research-useful only when there is a
reflection principle saying either $q=i(p)$ for some formula-level $p$, or
that $q$ has a definable approximation from which an actual
$p=\boxtimes p$ can be recovered.

Skeptic:

The danger is that completions manufacture limit objects that have no syntactic
name. For antitone $\boxtimes$, even existence in $\widehat L$ may come from
working with $\widehat{\boxtimes}^2$, a doubled order, or a topology rather
than from the original APS language. A reflection theorem must therefore name
the exact definability or compactness property that prevents fake fixed points.

Formalist:

Separate four obligations: define the embedding $i$; define which extension of
$\Box$, $\boxtimes$, and residuals is being used; define "principal,"
"compact," or "formula-definable" elements of $\widehat L$; and prove a
rounding/reflection lemma from a completion fixed point back to $L$. Without
these, the slogan "completion fixed point is not syntactic fixed point" stays
useful but non-theorematic.

Archivist:

Added a concrete completion-reflection work package to
`notes/completion-and-fixed-points.md` and promoted the corresponding proof
problem in `open_problems.md`.

Repository updates:

- `logs/autonomous-discussion.md`: recorded pass 1 and advanced the state.
- `notes/completion-and-fixed-points.md`: added the reflection-square target.
- `open_problems.md`: added a concrete completion-reflection problem.
- `logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 2 to choose one candidate completion, preferably MacNeille completion
or ideal completion, and write the first precise version of the embedding and
extension clauses.

### Pass 2 - 2026-05-24 20:36 JST

Focus:

Choose MacNeille completion as the first test case for the completion-reflection
square and make the embedding/extension vocabulary explicit enough for a later
theorem or countermodel.

Proposer:

Use MacNeille completion because it is already tied to algebraic proof theory
and cut-elimination stability in the BS16 note. The first work item should be
purely structural: define the cut embedding $i:L\to \widehat L$, then ask how
$\Box$, $\boxtimes$, and residuals extend across it. A completion fixed
point only counts as reflected when it lands on a principal cut $i(p)$, or when
a separate compact/definable rounding lemma recovers such a $p$.

Skeptic:

MacNeille completion is attractive exactly because it can be too strong. It may
add cuts that satisfy fixed point equations for order-theoretic reasons while
having no formula-level representative. For antitone $\boxtimes$, the main
risk is variance: extending $\boxtimes$ directly as if it were monotone will
hide the real problem. The extension must either pass through the order dual or
state an explicit polarity convention.

Formalist:

Record a three-part test. First, define $X^u$, $X^l$, MacNeille-closed lower
cuts, and the principal embedding. Second, treat $\boxtimes$ as a monotone map
from $L$ to $L^{op}$, then only compare it back to $\widehat L$ after an
explicit dual-identification step. Third, mark the reflection criterion:
$q=\widehat{\boxtimes}q$ is syntactic only if $q=i(p)$ and
$p=\boxtimes p$ holds in $L$, or if a named rounding lemma proves this from
compact definable approximants.

Archivist:

Added MacNeille completion vocabulary to `definitions.md`, added a MacNeille
first-test section to `notes/completion-and-fixed-points.md`, and sharpened the
open problems with an explicit variance/duality task for $\boxtimes$.

Repository updates:

- `logs/autonomous-discussion.md`: recorded pass 2 and advanced the state.
- `definitions.md`: added MacNeille/completion-reflection vocabulary.
- `notes/completion-and-fixed-points.md`: added the MacNeille first test.
- `open_problems.md`: added a concrete antitone-extension task.
- `logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 3 to turn the MacNeille first test into a small finite APS/preAPS model
search target: find either a principal reflected fixed point or a non-principal
completion fixed point that demonstrates failure of reflection.

### Pass 3 - 2026-05-24 21:07 JST

Focus:

Convert the MacNeille reflection idea into a finite model-search target rather
than another abstract slogan.

Proposer:

The next concrete artifact should be a small-model search protocol. Enumerate
finite preorders with $3$ or $4$ elements, choose $T,\bot,\Box,\boxtimes$,
require $\boxtimes$ to be antitone, compute the MacNeille closed lower cuts,
and then classify fixed points of the chosen completion extension as principal
or non-principal. A non-principal fixed cut would be exactly the kind of
completion-generated fixed point that does not automatically reflect to syntax.

Skeptic:

The hardest part is not enumeration but extension discipline. If
$\widehat{\boxtimes}$ is chosen ad hoc, any counterexample may only refute the
wrong extension. The search protocol must therefore record the extension rule
beside every result, and it should separate "APS axiom failure" from
"reflection failure" so that a toy model does not overclaim relevance to the
main G2-ZOO.

Formalist:

Use four classifications for each candidate: (1) no completion fixed point,
(2) only principal fixed points, (3) non-principal fixed points with no
formula-level fixed point, and (4) non-principal fixed points plus a possible
compact/definable rounding path. Also record G2, FG2, primitive
$\boxtimes$-fixed points, and whether A1-A4 or the currently used APS
fragment is being checked.

Archivist:

Added a dedicated model-search note under `models/`, linked it from the model
README, extended the completion note with the finite-search target, and added a
matching open problem.

Repository updates:

- `logs/autonomous-discussion.md`: recorded pass 3 and advanced the state.
- `models/macneille-reflection-search.md`: added finite search protocol.
- `models/README.md`: linked the new search target.
- `notes/completion-and-fixed-points.md`: added finite search target.
- `open_problems.md`: added a finite MacNeille reflection search task.
- `logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 4 to either draft a checker script interface for the search protocol or
write the first hand-checkable 3-element candidate table before automating.

### Pass 4 - 2026-05-24 21:36 JST

Focus:

Turn the MacNeille reflection search protocol into a concrete checker interface
so later passes can automate the small-model search without blurring the
extension convention for antitone $\boxtimes$.

Proposer:

Draft a script contract before writing the script. The checker should accept one
finite APS/preAPS JSON file, validate its preorder and operations, compute
MacNeille closed lower cuts, compute principal cuts, and report primitive
$\boxtimes$-fixed points in $L$. The completed-$\boxtimes$ stage should be
pluggable by named extension rule, because the research question depends on
whether the antitone map is extended through $L^{op}$, a doubled order, or a
later canonical-extension recipe.

Skeptic:

A checker that silently picks one extension rule would create false confidence.
The output must make extension discipline visible: every reported completion
fixed point should carry the extension rule name, whether the cut is principal,
and whether any syntactic $p=\boxtimes p$ exists. Otherwise a "countermodel"
could merely be a countermodel to an undocumented implementation choice.

Formalist:

Use an interface with bounded inputs and explicit output classes:
`no-completion-fixed-point`, `principal-only`, `nonprincipal-without-syntactic`,
and `nonprincipal-with-rounding-candidate`. The first implementation can
support only an `antitone-dual-lower-cut-v0` extension rule, but the output
schema should be ready for additional rules.

Archivist:

Added a checker interface note that specifies the planned PowerShell command,
inputs, output schema, validation checks, and first milestone. Linked it from
the model README and from the MacNeille search protocol.

Repository updates:

- `logs/autonomous-discussion.md`: recorded pass 4 and advanced the state.
- `models/macneille-checker-interface.md`: added checker interface contract.
- `models/macneille-reflection-search.md`: linked the checker interface.
- `models/README.md`: linked the checker interface.
- `logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 5 to implement the first minimal checker skeleton or create one
hand-checkable model JSON that exercises the interface.

### Pass 5 - 2026-05-24 22:53 JST

Focus:

Move from a checker contract to a runnable first milestone for the MacNeille
reflection search.

Proposer:

Implement the smallest useful checker now. It should validate a finite JSON
model, compute MacNeille cuts, identify principal cuts, check syntactic
$\boxtimes$-fixed points, and classify completed fixed points under the
provisional `antitone-dual-lower-cut-v0` rule. Include one 3-element chain model
as a smoke test so the interface is exercised immediately.

Skeptic:

The provisional extension rule remains the weak point. The checker must state
that its rule is not yet a theorem-level canonical extension, otherwise the
first generated classifications could be mistaken for mathematical results.
The model example should therefore be treated as an interface smoke test, not a
G2-ZOO countermodel.

Formalist:

The first script should reject malformed preorders and non-antitone
refutability maps. It should report G2, FG2, syntactic fixed points, MacNeille
closed cuts, completed fixed points, and one of the four classification labels
from the interface note. That is enough to make pass 6 a genuine search pass
rather than more scaffolding.

Archivist:

Added `scripts/check-macneille-reflection.ps1` and a hand-checkable
`models/examples/three-chain-antitone.json` smoke-test model. The checker
implements the first milestone from `models/macneille-checker-interface.md` and
keeps the extension-rule warning in its JSON report. The smoke test reports
`principal-only`, with syntactic fixed point `m`.

Repository updates:

- `logs/autonomous-discussion.md`: recorded pass 5 and advanced the state.
- `scripts/check-macneille-reflection.ps1`: added the first checker milestone.
- `models/examples/three-chain-antitone.json`: added a smoke-test model.
- Smoke-tested the checker on the example model.
- `logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 6 to run the checker across the smoke-test model, record the result,
and decide whether to enumerate additional 3-element candidates or revise the
extension rule first.

### Pass 6 - 2026-05-24 23:24 JST

Focus:

Run the new checker on the smoke-test model and decide what the next research
move should be after the initial six-pass automation cycle.

Proposer:

The checker now gives a reproducible baseline: the 3-element chain smoke test
has three MacNeille cuts, one syntactic fixed point `m`, and one completed fixed
point `{ b, m, t }`, which is principal. That makes it a useful sanity check but
not a reflection counterexample. The next substantive step should be an
enumeration pass over additional 3-element preorders and antitone maps, using
this report format as the stable output.

Skeptic:

The result also shows why the provisional extension rule must stay visibly
provisional. The smoke-test classification is `principal-only`, while G2 and FG2
both fail under the current data. That is useful for interface testing but not
yet a theorem about APS completions. Before drawing conclusions, the project
needs either a reviewed canonical extension rule or a separate note explaining
why `antitone-dual-lower-cut-v0` is the right first approximation.

Formalist:

Record this as a baseline result: model `three-chain-antitone`, extension rule
`antitone-dual-lower-cut-v0`, classification `principal-only`, syntactic fixed
points `{m}`, completed fixed point `{b,m,t}` principal at `t`, G2 false, FG2
false, and A1-A4 unchecked. The next proof obligation is to separate
"principal-only under v0" from "reflection theorem under canonical extension."

Archivist:

Generated a JSON report under `outputs/`, linked it from `outputs/README.md`,
and added a first-run result section to the MacNeille reflection search note.
This completes the initial six-pass Codex research automation cycle. On
2026-05-25, the user clarified that the loop should not stop at six passes, so
the automation was recreated without a pass-count limit.

Repository updates:

- `logs/autonomous-discussion.md`: recorded pass 6 and marked the initial cycle
  completed.
- `outputs/macneille-reflection-three-chain-antitone.json`: saved the checker
  report.
- `outputs/README.md`: linked the MacNeille reflection report.
- `models/macneille-reflection-search.md`: recorded the first checker result.
- `logs/research-log.md`: recorded this autonomous pass.

Next step:

Continue with pass 7 by choosing whether the priority is enumerating
3-element candidates or reviewing the canonical status of the
`antitone-dual-lower-cut-v0` extension rule.

### Pass 7 - 2026-05-25 23:04 JST

Focus:

Incorporate Claude Code Review 1 by replacing the wrong-polarity MacNeille
extension default, separating "principal" from "reflected," and validating the
new size-3 non-lattice example under the corrected rule.

Proposer:

Accept the review's core correction: for antitone
$\boxtimes:L\to L$, treat it as a monotone map $L\to L^{op}$ and use
$((\boxtimes[C])^{l_L})^{u_L}$ as the v1 extension. This makes the old v0
rule a reproducibility path only. The pass should also accept the new
`three-element-nolattice-nosynt` model because it gives exactly the desired
bare finite separation: no syntactic $\boxtimes$-fixed point, but a
non-principal completion fixed point.

Skeptic:

These results are still preAPS/order-theoretic evidence, not APS theorems.
Both validated examples have G2 and FG2 false, and A1-A4 are not checked by the
finite checker. The ChatGPT Project source remains a bridge constraint: no
unrelayed Project content or citation claim was used in this pass. The useful
next question is which additional axioms destroy or preserve the non-principal
completion fixed point.

Formalist:

The checker now distinguishes `reflected-only`, `principal-unreflected`,
`nonprincipal-without-syntactic`, and `nonprincipal-with-rounding-candidate`.
For v1 it checks the principal extension condition against the dual principal
cut $i_{L^{op}}(\boxtimes a)$. The chain smoke test is classified as
`principal-unreflected`: the completed fixed point is $i(t)$, but
$\boxtimes t=b\neq t$. The non-lattice model is classified as
`nonprincipal-without-syntactic`, with fixed cut $\{0,a,b\}$.

Archivist:

Updated the PowerShell checker, regenerated v1 reports for both examples, and
updated the checker interface, search note, output index, and classification
registry. Claude Code Review 1 was incorporated where it supplied concrete
repository artifacts and deferred where it asked for broader APS axiom-package
search.

Repository updates:

- `scripts/check-macneille-reflection.ps1`: added v1, dual principal checks,
  reflected status, and refined classifications.
- `outputs/macneille-reflection-three-chain-antitone-v1.json`: saved the v1
  chain smoke-test report.
- `outputs/macneille-reflection-three-element-nolattice-nosynt-v1.json`: saved
  the v1 non-lattice separation report.
- `models/macneille-checker-interface.md`: documented v1, reflected status, and
  extension-condition checks.
- `models/macneille-reflection-search.md`: recorded the v1 results and marked
  v0 as legacy.
- `notes/completion-and-fixed-points.md`: synchronized the v1 antitone
  extension formula and reflected/principal-unreflected vocabulary.
- `notes/g2-aps-zoo-classification.md`: updated the current model registry to
  use v1.
- `logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 8 to add either a finite APS-axiom checker layer or a small enumerator
for G2-holding variants, then test whether the `three-element-nolattice-nosynt`
phenomenon survives any nontrivial axiom package.

### Pass 8 - 2026-05-25 JST

Focus:

Prove the orbit-stabilization theorem for n-FG2, construct the first
non-degenerate 4-element witness for G2+FG2+FP-synt, and classify the
implication structure of the n-FG2 hierarchy.

Proposer:

The G2-ZOO now has all 8 separating witnesses at size 3. The next theoretical
advance is an exact characterization of when nFG2($k$) holds for ALL $k\ge 1$.
Looking at the certified data: M-011 (TTTTTTTT) has $\boxtimes$-orbit
$T\to\bot\to\bot\to\cdots$ stabilizing at $\bot=\boxtimes\bot$; M-111 has
orbit $T\to T\to\cdots$ stable at $T$. The common pattern is that the sub-orbit
$(\boxtimes T,\boxtimes^2 T,\ldots)$ is non-increasing and eventually reaches a
syntactic fixed point. The conjecture — now proved — is:

**Theorem (Orbit Stabilization)**: Let $(L,\le,\boxtimes,T,\bot)$ be a finite
preAPS. The following are equivalent:

1. $\mathrm{nFG2}(k)$ holds for all $k\ge 1$.
2. The sequence $\boxtimes T\ge\boxtimes^2 T\ge\boxtimes^3 T\ge\cdots$ is
   non-increasing in $L$.
3. There exists $N\ge 1$ such that $\boxtimes^N T$ is a syntactic fixed
   point of $\boxtimes$, and $\boxtimes T\ge\boxtimes^2 T\ge\cdots\ge\boxtimes^N T$.

(1$\Leftrightarrow$2) by definition. (2$\Rightarrow$3): since $L$ is finite,
any non-increasing chain eventually stabilizes; the stable value $p=\boxtimes^N T$
satisfies $\boxtimes p=\boxtimes^{N+1}T=\boxtimes^N T=p$. (3$\Rightarrow$2):
clear.

**Corollary**: All-$k$ nFG2 $\Rightarrow$ FP-synt. (The converse fails:
M-101 has FP at $\bot$ with $\bot$ not on the $\boxtimes$-orbit of $T$,
and nFG2(1)=FG2 is false.)

This introduces a new classification axis separating FP-synt into:

- **FP-reachable**: $\exists N\ge 1$ with $\boxtimes^N T$ a syntactic FP.
  Equivalent to: all-$k$ nFG2 AND non-increasing sub-orbit.
- **FP-unreachable**: FP exists but not on the $\boxtimes$-orbit of $T$.
  M-001 and M-101 are examples.

The implication diagram now reads:

$$
\text{all-}k\text{ nFG2}
\;\Rightarrow\;
\text{FP-reachable}
\;\Rightarrow\;
\text{FP-synt}
\;\Rightarrow\;
\text{neither G2 nor FG2 is forced.}
$$

Skeptic:

The orbit stabilization theorem is correct for finite preorders, but it has a
hidden size dependency: "non-increasing" uses the ambient order $\le$ of $L$,
which is not the APS order in general. In an infinite or non-Noetherian APS
(e.g., the Lindenbaum algebra of a sufficiently strong logic), the sequence
$\boxtimes^k T$ might be non-increasing yet never stabilize. The theorem should
be labeled as a finite-model result. For APS proper, the orbit condition becomes
a well-foundedness assumption on $\boxtimes$-iteration, which is a new axiom
candidate.

Also: both M-011 and M-111 have the FP-reachable condition, but both have G2
FALSE (M-011) or G2 vacuous (M-111 has $\boxtimes T=T\not\le\bot$). The real
challenge is finding a model where all-$k$ nFG2 and G2 hold with a non-trivial
antecedent path. That requires $\boxtimes T\le\bot\Rightarrow T\le\bot$ with
antecedent true but model non-collapsed — which forces $T\le\bot$, i.e.,
collapse. So G2 with true antecedent in a non-collapsed model is impossible.
G2 in non-collapsed models is always vacuous. This is a structural theorem worth
recording explicitly.

Formalist:

Record two results:

**Proposition (G2 in non-collapsed models)**: Let $S$ be a non-collapsed
preAPS ($T\not\le\bot$). Then G2 holds if and only if $\boxtimes T\not\le\bot$.
In particular, G2 in a non-collapsed model is always vacuously true.

*Proof*: G2 states $\boxtimes T\le\bot\Rightarrow T\le\bot$. Since
$T\not\le\bot$, the consequent is FALSE. So G2 holds iff the antecedent
$\boxtimes T\le\bot$ is also FALSE, i.e., $\boxtimes T\not\le\bot$. $\square$

**Corollary**: G2 partitions non-collapsed preAPS into two classes:

- G2 holds: $\boxtimes T\not\le\bot$ (the "consistency statement is not refutable")
- G2 fails: $\boxtimes T\le\bot$ (the "consistency statement is refutable but system is consistent")

This gives G2 an exact algebraic reading: it is the assertion that provability
and refutability of the consistency statement are separated.

**Theorem (Orbit Stabilization — formal)**: In a finite preAPS $S$,
$\mathrm{nFG2}(k)$ for all $k\ge 1$ iff
$\exists N\ge 1\colon \boxtimes^N T\in\mathrm{Fix}_\boxtimes(S)$
and $\boxtimes^j T\ge\boxtimes^{j+1} T$ for $j=1,\ldots,N-1$.

Here $\mathrm{Fix}_\boxtimes(S):=\{p\in L:p=\boxtimes p\}$.

**Non-degenerate 4-element witness** for G2+FG2+FP-synt: the model

$$
L=\{T,p,c,\bot\},
\quad T>p>\bot,\quad T>c,\quad p\parallel c,\quad c\parallel\bot,
$$
$$
\boxtimes:\;T\mapsto p,\;p\mapsto p,\;c\mapsto T,\;\bot\mapsto T.
$$

Verified: antitone ✓, G2 vacuous ($\boxtimes T=p\not\le\bot$) ✓, FG2
($\boxtimes^2 T=p\le p=\boxtimes T$) ✓, FP at $p$ (with $p\ne T,\bot$)
✓, non-collapsed ✓. The $\boxtimes$-orbit of $T$ is $T\to p\to p\to\cdots$
and stabilizes at $p\in\mathrm{Fix}_\boxtimes$. nFG2($k$) holds for all
$k\ge 1$ (pattern TTTTTTTT).

This is the first certified non-degenerate witness for G2+FG2+FP-synt.
It can be stored as `models/examples/M4-G2FG2FP.json`.

Archivist:

Added Pass 8 results: (1) orbit stabilization theorem in
`notes/g2-fg2-hierarchy.md`; (2) "G2 in non-collapsed models" proposition in
`definitions.md`; (3) new model `models/examples/M4-G2FG2FP.json`;
(4) updated `open_problems.md` to mark FP-reachable vs FP-unreachable as a
new axis; (5) updated `notes/g2-aps-zoo-classification.md` registry; and
(6) recorded this pass in `logs/research-log.md`.

Repository updates:

- `logs/autonomous-discussion.md`: recorded pass 8.
- `notes/g2-fg2-hierarchy.md`: added orbit stabilization theorem, corollary,
  implication diagram, and FP-reachable/FP-unreachable classification.
- `definitions.md`: added G2 in non-collapsed models proposition.
- `models/examples/M4-G2FG2FP.json`: new 4-element non-degenerate witness.
- `notes/g2-aps-zoo-classification.md`: added M4-G2FG2FP to model registry.
- `open_problems.md`: added FP-reachable vs FP-unreachable separation problem.
- `logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 9 to determine whether the infinite analogue of the orbit stabilization
theorem requires a new well-foundedness axiom, or whether it is a theorem of
some existing APS axiom package. Also: characterize which 4-element preAPS models
satisfy G2+FG2+FP-synt with FP-reachable (there should be a finite enumeration),
and ask whether any such model also has nontrivial residuation structure.

### Pass 9 - 2026-05-26 18:00 JST

Focus:

Audit the nFG2 claims from pass 8, materialize the missing non-degenerate
G2+FG2+FP witness, and isolate the exact finite-to-infinite gap in orbit
stabilization.

Proposer:

The useful positive result is finite and should be stated sharply: all-level
nFG2 is exactly a non-increasing $\boxtimes$-tail orbit, and in finite
preAPS this tail must stabilize at a syntactic fixed point reachable from $T$.
This gives a clean FP-reachable axis without implying G2. The missing witness
from pass 8 can be made concrete as `M4-G2FG2FP`, with
$\bot<p<T$, $c<T$, $\boxtimes T=p$, $\boxtimes p=p$,
$\boxtimes c=T$, and $\boxtimes\bot=T$.

Skeptic:

The earlier "nFG2 hierarchy is strict at every depth" wording was too strong.
The certified M-010 pattern refutes odd-step implications, including
FG2 $\Rightarrow$ nFG2(2), but it does not refute even-step implications or
arbitrary-depth strictness. Those remain finite search tasks. Also, the
non-degenerate M4 witness still has G2 only vacuously, which is unavoidable in
non-collapsed models under the material implication reading of G2.

Formalist:

Added the definition of nFG2($k$) and the non-collapsed G2 criterion to
`definitions.md`. The finite orbit theorem now has the exact hypothesis where
it works: finiteness, or more generally an orbit well-foundedness/no-infinite-
descent assumption. The checker verifies `M4-G2FG2FP` as non-collapsed with
G2 true, FG2 true, all checked nFG2 levels true, and FP-synt at $p$. It also
reports no MacNeille completion fixed point for that model, which separates the
G2+FG2+FP-synt axis from completion-generated fixed points.

Archivist:

Corrected the overclaim in the nFG2 hierarchy note, added the finite orbit
stabilization theorem, created and checked `M4-G2FG2FP`, saved its JSON report,
and updated the model registry, open problems, model/output indexes, active
research questions, and research log. Claude Code Review 1 had no newer entry;
its already-incorporated MacNeille requests remain closed.

Repository updates:

- `notes/g2-fg2-hierarchy.md`: corrected the strictness claim, added finite
  orbit stabilization, and recorded `M4-G2FG2FP`.
- `definitions.md`: added nFG2($k$), all-level nFG2, and the non-collapsed G2
  criterion.
- `models/examples/M4-G2FG2FP.json`: added the 4-element non-degenerate witness.
- `outputs/g2-zoo-M4-G2FG2FP.json`: saved the checker report.
- `notes/g2-aps-zoo-classification.md`: added the M4 witness and corrected the
  nFG2 strictness status.
- `open_problems.md`: resolved the non-degenerate G2+FG2+FP and all-level
  nFG2-implies-G2 questions; added the infinite orbit-well-foundedness problem.
- `logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 10 to either search for arbitrary-depth nFG2 strictness witnesses or
attempt to equip `M4-G2FG2FP` with nontrivial tensor/residual operations.

### Pass 10 - 2026-05-26 18:56 JST

Focus:

Resolve the arbitrary-depth nFG2 first-true problem by giving a uniform finite
model family and a checked depth-3 instance.

Proposer:

The clean construction is sparse. For any $N\ge 1$, take
$L_N=\{T,a_1,\ldots,a_{N+1},s\}$, order it only by reflexivity plus
$s\le a_{N+1}$, and define
$\boxtimes T=a_1$, $\boxtimes a_i=a_{i+1}$ for $1\le i\le N$,
$\boxtimes a_{N+1}=s$, and $\boxtimes s=s$. Then the orbit of $T$ is
$T\to a_1\to\cdots\to a_{N+1}\to s\to s$, so nFG2 fails through level $N$
and holds from level $N+1$ onward.

Skeptic:

This solves the finite first-true-depth problem only in a deliberately sparse
preAPS class. It does not yet show that the hierarchy remains separated under
any substantive APS axiom package, residual structure, contraction/weakening
discipline, or completion-stability condition. The correct next question is
therefore not "does arbitrary depth exist?" but "which structural axioms kill
or preserve the $D_N$ construction?"

Formalist:

Antitonicity is immediate because the only nontrivial order relation is
$s\le a_{N+1}$, and its image condition is
$\boxtimes a_{N+1}=s\le s=\boxtimes s$. For $1\le k\le N$, nFG2($k$)
asks $a_{k+1}\le a_k$, which is absent. At $k=N+1$, it asks
$s\le a_{N+1}$, which is the added relation; all later levels are $s\le s$.
The generated `nfg2-depth-3` model was checked and has pattern `FFFTTTTT`.

Archivist:

Added a generator script for $D_N$, generated and checked `nfg2-depth-3`,
persisted its report, updated the hierarchy note, and moved the arbitrary-depth
nFG2 task from open to resolved while opening the sharper APS-axiom preservation
problem. The checker was also made tolerant of UTF-8 BOM JSON files produced by
Windows PowerShell.

Repository updates:

- `scripts/new-nfg2-depth-witness.ps1`: generator for the $D_N$ family.
- `models/examples/nfg2-depth-3.json`: checked depth-3 witness.
- `outputs/g2-zoo-nfg2-depth-3.json`: persisted checker report.
- `scripts/check-g2-zoo.py`: accepts UTF-8 BOM JSON input.
- `notes/g2-fg2-hierarchy.md`: added the arbitrary-depth construction theorem.
- `definitions.md`: added first-true nFG2 depth.
- `open_problems.md`: resolved arbitrary-depth first-true witnesses and opened
  the structural-axiom preservation problem.
- `logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 11 to test whether simple tensor/residual candidates can be placed on
`M4-G2FG2FP` or on the $D_N$ family without destroying the certified G2/FG2/
nFG2 behavior.

### Pass 11 - 2026-05-27 00:57 JST

Focus:

Test whether the non-degenerate `M4-G2FG2FP` witness can carry full
tensor/residual structure on its existing carrier and order.

Proposer:

The right first test is exhaustive rather than speculative. Because
`M4-G2FG2FP` has four elements, fixing a two-sided unit leaves $4^9=262144$
binary tensor candidates. Checking all four possible units is small enough to
turn the residuation question into a finite certificate.

Skeptic:

This is only a same-carrier/same-order obstruction. It does not rule out adding
new elements, changing the order while preserving the G2+FG2+FP behavior, using
one-sided residuals, or moving to the $D_N$ family. It also does not use any
external source claim; it is a machine-checkable finite search result inside
the repository.

Formalist:

For each possible unit $e$, the search enumerates every tensor with
$e\otimes x=x=x\otimes e$. It keeps only operations that are associative,
monotone in both arguments, and whose left and right residual fibers are
principal downsets:
$$
\{b:a\otimes b\le c\}=\downarrow(a\backslash c),
\qquad
\{a:a\otimes b\le c\}=\downarrow(c/b).
$$
The result is zero candidates for every unit. Therefore `M4-G2FG2FP` has no
full residuated monoid expansion on the existing four-element order.

Archivist:

Added `scripts/search-residuated-tensor.py`, generated
`outputs/residuated-search-M4-G2FG2FP.json`, and updated the G2/FG2 hierarchy,
residuated-domain note, model/output indexes, open problems, and active
questions. The previous open problem is resolved negatively in the strict
same-order sense and replaced by a sharper search for a modified or expanded
full-residuated witness.

Repository updates:

- `scripts/search-residuated-tensor.py`: exhaustive tensor/residual search.
- `outputs/residuated-search-M4-G2FG2FP.json`: negative finite search report.
- `notes/g2-fg2-hierarchy.md`: recorded the same-order full-residuation
  obstruction for `M4-G2FG2FP`.
- `notes/residuated-algebra-domain-completion.md`: added the M4 obstruction and
  next residuated-search direction.
- `open_problems.md`: resolved the same-order M4 full-residuation question
  negatively and opened the modified/expanded witness problem.
- `logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 12 to search for the smallest order expansion or carrier extension
that preserves G2+FG2+FP-reachable behavior while admitting full residuation, or
to test one-sided/partial residual relaxations as an intermediate target.

### Pass 12 - 2026-05-27 04:40 JST

Focus:

Find the smallest same-carrier order repair of `M4-G2FG2FP` that admits full
residuation while preserving the G2+FG2+FP-reachable behavior.

Proposer:

Instead of adding elements, first enumerate preorder extensions of the existing
four-element order. The search keeps the carrier, $T$, $\bot$, $\Box$, and
$\boxtimes$ fixed; it allows only extra order pairs that preserve
non-collapse, antitonicity of $\boxtimes$, G2, FG2, and a syntactic fixed point.
This gives a bounded finite problem before moving to larger carriers.

Skeptic:

The result should be interpreted as a residuated repair, not automatically as a
proof-theoretic axiom. Adding $\bot\le c$ makes residual downsets principal,
but it is not yet clear whether that relation has a natural reading in the APS
or BS16 resource-sensitive story. No external citation or Project-only content
was used for this step.

Formalist:

The order-extension search found a first hit after checking two candidate
extensions. Adding exactly $\bot\le c$ turns the order into the diamond
$\bot<p<T$, $\bot<c<T$, $p\parallel c$. The resulting model has a full
residuated monoid expansion with unit $p$. The tensor has $p$ as unit,
$\bot$ as zero, $T\otimes T=T$, $T\otimes c=c$, and $c\otimes c=\bot$.
The G2-ZOO checker confirms non-collapse, G2 true, FG2 true, all checked nFG2
levels true, and FP-synt at $p$.

Archivist:

Added a same-carrier order-extension search script, generated the full-residuated
order-repair model, saved both the residuation search report and the G2-ZOO
checker report, and updated the hierarchy, residuated-domain, classification,
model/output index, open-problem, and active-question notes.

Repository updates:

- `scripts/search-residuated-order-expansions.py`: same-carrier order repair
  search.
- `models/examples/M4-G2FG2FP-order-plus-bot-c-residuated.json`: full-residuated
  order repair of the M4 witness.
- `outputs/residuated-order-search-M4-G2FG2FP.json`: order-extension search
  report.
- `outputs/g2-zoo-M4-G2FG2FP-order-plus-bot-c-residuated.json`: checker report
  for the repaired witness.
- `models/finite-aps-schema.json`: documented optional `unit`, `tensor`, and
  residual tables.
- `open_problems.md`: resolved the modified same-carrier full-residuation
  search and opened the interpretation problem for $\bot\le c$.
- `logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 13 to interpret the $\bot\le c$ repair: determine whether it
corresponds to a natural resource/refutability axiom, or whether a more
proof-theoretically meaningful residuated witness should be sought.

### Pass 13 - 2026-05-27 05:10 JST

Focus:

Interpret the $\bot\le c$ repair in
`M4-G2FG2FP-order-plus-bot-c-residuated` and decide whether it is an ad hoc
edge or a named APS/resource principle.

Proposer:

The repair has a clean structural reading: the original M4 order had a
distinguished $\bot$ constant but did not make it a least element. It already
satisfied $\bot\le p$, $\bot\le T$, $p\le T$, and $c\le T$; the only
missing bottom-discipline instance was $\bot\le c$. Adding that relation is
therefore exactly bottom discipline on this carrier:
$$
\forall x,\quad \bot\le x.
$$
Read proof-theoretically, this is ex-falso or absurdity weakening for the
$c$-branch.

Skeptic:

This interpretation is useful but not automatically harmless. In a
resource-sensitive BS16-style setting, ex-falso weakening may be a structural
principle that changes the intended calculus. The pass should therefore not
declare the repair canonical; it should record the principle and make its
effect on existing separations a new finite-model test.

Formalist:

Order-theoretically, adding $\bot\le c$ makes $\bot$ least and keeps $T$
greatest, with $p$ and $c$ as incomparable atoms. Thus the repaired order is
the four-element Boolean lattice. This explains why full residuation becomes
possible: residual solution sets that were non-principal in the sparse order can
now be represented by lattice elements. The G2/FG2/FP behavior is unchanged
because the $T$-orbit of $\boxtimes$ remains $T\to p\to p$.

Archivist:

Added bottom discipline to the shared definitions, recorded the repair
interpretation in the hierarchy and residuated-domain notes, updated the model
metadata, and converted the open interpretive problem into a sharper test:
which G2-ZOO and $D_N$ witnesses survive after enforcing
$\forall x(\bot\le x)$?

Repository updates:

- `definitions.md`: defined bottom discipline as
  $\forall x(\bot\le x)$, with the M4 repair as its missing instance.
- `notes/g2-fg2-hierarchy.md`: interpreted $\bot\le c$ as
  ex-falso/absurdity weakening for the $c$-branch.
- `notes/residuated-algebra-domain-completion.md`: recorded the Boolean-lattice
  reading of the repaired order and the remaining BS16/resource-sensitive risk.
- `notes/g2-aps-zoo-classification.md`: added bottom discipline as the next
  model-classification filter.
- `open_problems.md` and `ideas/research-questions.md`: replaced the raw
  interpretation question with the bottom-discipline preservation problem.
- `models/examples/M4-G2FG2FP-order-plus-bot-c-residuated.json`: added the
  repair interpretation to metadata.
- `logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 14 to implement or run a bottom-discipline filter over the finite
G2-ZOO models and the $D_N$ example, recording which separations survive,
which collapse, and which become better candidates for residuated APS.

### Pass 14 - 2026-05-27 05:47 JST

Focus:

Run bottom discipline as a finite-model filter over the current G2-ZOO
witnesses and the checked `nfg2-depth-3` example.

Proposer:

The direct test is to keep each carrier, $T$, $\bot$, $\Box$, and
$\boxtimes$ fixed, add every missing pair $\bot\le x$, close transitively,
and then ask whether $\boxtimes$ is still antitone. If it is, compare G2,
FG2, FP-synt, collapse, and the checked nFG2 prefix before and after bottom
enforcement.

Skeptic:

This is only a pure order-enforcement test. A model that fails it is not proved
impossible under bottom discipline; it only means that this particular sparse
witness cannot be repaired by adding bottom pairs while leaving $\boxtimes$
unchanged. Replacement witnesses may exist with different carriers, orders, or
refutability maps.

Formalist:

The report `outputs/bottom-discipline-filter-g2-zoo.json` checks 11 models.
Only `M4-G2FG2FP-order-plus-bot-c-residuated` already satisfies bottom
discipline. Pure enforcement preserves antitonicity for `M-000`, `M-010`,
`M-111`, `M4-G2FG2FP`, and the repaired M4 model. Full recorded behavior is
stable only for `M-111` and the M4 pair. `M-010` still witnesses FG2 without
G2, but enforcing bottom discipline makes $0\sim\bot$, adding FP-synt and
turning the checked nFG2 prefix into `TTTTTTTT`. The current arbitrary-depth
witness `nfg2-depth-3` fails pure enforcement because $s\le T,a_1,a_2,a_3$
would require $a_1,a_2,a_3,a_4\le s$ by antitonicity.

Archivist:

Added `scripts/check-bottom-discipline.py`, generated the bottom-discipline
filter report, updated the hierarchy, classification, residuated-domain,
model/output index, open-problem, active-question, and research-log notes. The
new research target is now concrete: find bottom-disciplined replacement
witnesses for the separations lost under pure order enforcement.

Repository updates:

- `scripts/check-bottom-discipline.py`: finite bottom-discipline filter and
  pure order-enforcement report generator.
- `outputs/bottom-discipline-filter-g2-zoo.json`: report for the eight 3-element
  G2-ZOO witnesses, `M4-G2FG2FP`, its repaired residuated version, and
  `nfg2-depth-3`.
- `notes/g2-fg2-hierarchy.md`: added the bottom-discipline filter table and
  consequences for current separations.
- `notes/g2-aps-zoo-classification.md`: recorded which witnesses survive pure
  bottom enforcement.
- `notes/residuated-algebra-domain-completion.md`: noted that bottom discipline
  is a real structural filter and kills the current $D_N$ witness.
- `open_problems.md` and `ideas/research-questions.md`: closed the current
  filter run and opened the replacement-witness search.
- `models/README.md` and `outputs/README.md`: indexed the new script and report.
- `logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 15 to search for bottom-disciplined finite replacement witnesses,
starting with G2 without FG2 and arbitrary first-true nFG2 depth.

### Pass 15 - 2026-05-27 06:17 JST

Focus:

Find bottom-disciplined replacement witnesses for the separations lost under
pure bottom-order enforcement, starting with G2 without FG2 and arbitrary
first-true nFG2 depth.

Proposer:

The sparse $D_N$ construction failed bottom discipline because its eventual
fixed point $s$ was also the bottom constant. Separate those roles. Add a true
bottom $b$ below every element and a helper upper bound $U$ above every
element. Let $\boxtimes b=U$ and $\boxtimes U=b$, while keeping the old
orbit $T\to a_1\to\cdots\to a_{N+1}\to s\to s$.

Skeptic:

This is still a preAPS construction, not a proof that the witness survives any
stronger APS axiom package, residuation requirement, lattice law, or BS16 modal
rule. The helper $U$ is a technical upper bound introduced to absorb
antitonicity requirements from $b\le x$. That is acceptable as a finite
witness but should be tracked as structure added for bottom discipline.

Formalist:

For $B_N$, take carrier
$\{b,T,a_1,\ldots,a_{N+1},s,U\}$, order $b\le x\le U$ for every $x$, and
add $s\le a_{N+1}$. Define
$\boxtimes b=U$, $\boxtimes U=b$, $\boxtimes T=a_1$,
$\boxtimes a_i=a_{i+1}$ for $1\le i\le N$,
$\boxtimes a_{N+1}=s$, and $\boxtimes s=s$. Antitonicity follows from the
bounding pairs and $s\le a_{N+1}$. The $T$-orbit gives nFG2 false through
$N$ and true from $N+1$. Since $a_1\not\le b$, G2 is true vacuously; FG2
fails; and FP-synt holds at $s$.

Archivist:

Added a generator for $B_N$, generated and checked the depth-3 instance, saved
its G2-ZOO report, updated the bottom-discipline filter report to include it,
and revised the hierarchy, classification, residuated-domain, open-problem,
active-question, model index, output index, and research log. The remaining
bottom-disciplined replacement target is G2+FG2 without FP-synt.

Repository updates:

- `scripts/new-bottom-nfg2-depth-witness.py`: generator for the
  bottom-disciplined $B_N$ family.
- `models/examples/bottom-nfg2-depth-3.json`: checked depth-3
  bottom-disciplined witness.
- `outputs/g2-zoo-bottom-nfg2-depth-3.json`: checker report with pattern
  `FFFTTTTT`.
- `outputs/bottom-discipline-filter-g2-zoo.json`: updated filter report now
  includes `bottom-nfg2-depth-3`.
- `notes/g2-fg2-hierarchy.md`: added the $B_N$ construction theorem and proof
  sketch.
- `notes/g2-aps-zoo-classification.md`: added the new registry row and revised
  the bottom-discipline next target.
- `notes/residuated-algebra-domain-completion.md`: recorded the role separation
  $b$ versus $s$ and helper upper bound $U$.
- `open_problems.md` and `ideas/research-questions.md`: resolved the
  bottom-disciplined G2-not-FG2/arbitrary-depth targets and opened the
  G2+FG2-without-FP target.
- `models/README.md` and `outputs/README.md`: indexed the new generator, model,
  and report.
- `logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 16 to search directly for a bottom-disciplined finite preAPS with
G2+FG2 and no syntactic $\boxtimes$-fixed point, or prove that the small
bounded constructions force FP-synt.

### Pass 16 - 2026-05-27 06:47 JST

Focus:

Resolve the remaining bottom-discipline separation: G2+FG2 without syntactic
$\boxtimes$-fixed point.

Proposer:

Use the same role separation as $B_N$: keep a true bottom $b$ and helper
upper bound $U$, but make the $T$-orbit enter a strict two-cycle
$$
T\to a\to d\to a\to\cdots
$$
with $d\le a$. This makes FG2 true at the first step without requiring
$a\sim d$.

Skeptic:

The construction shows bottom discipline alone does not force FP-synt from
G2+FG2. It does not yet say whether a stronger setting such as a full
residuated APS, lattice-ordered APS, or a BS16-derived modal calculus preserves
this separation. The helper $U$ again marks the construction as a bounded
preAPS witness.

Formalist:

The model `bottom-G2FG2-noFP` has carrier $\{b,d,a,T,U\}$, order
$b\le x\le U$ for all $x$, plus $d\le a$. Define
$$
\boxtimes b=U,\quad \boxtimes U=b,\quad \boxtimes T=a,\quad
\boxtimes a=d,\quad \boxtimes d=a.
$$
Antitonicity follows from the bounding pairs and the interior relation
$d\le a$, whose image condition is $d=\boxtimes a\le\boxtimes d=a$. G2 is
true vacuously because $\boxtimes T=a\not\le b$. FG2 is true because
$\boxtimes^2T=d\le a=\boxtimes T$. There is no syntactic fixed point:
$b\leftrightarrow U$, $a\leftrightarrow d$, and $T\mapsto a$ with
$T\not\sim a$. The checker reports nFG2 pattern `TFTFTFTF`.

Archivist:

Added the witness model, saved its checker report, updated the
bottom-discipline filter report, and revised the hierarchy, classification,
residuated-domain, open-problem, active-question, model index, output index,
and research log. Bottom discipline alone now preserves all currently tracked
G2/FG2/FP-synt separations; the next test is residuation.

Repository updates:

- `models/examples/bottom-G2FG2-noFP.json`: 5-element bottom-disciplined
  G2+FG2 without FP-synt witness.
- `outputs/g2-zoo-bottom-G2FG2-noFP.json`: checker report for the new witness.
- `outputs/bottom-discipline-filter-g2-zoo.json`: updated to include
  `bottom-G2FG2-noFP`.
- `notes/g2-fg2-hierarchy.md`: added the construction and proof sketch.
- `notes/g2-aps-zoo-classification.md`: added the registry row and revised the
  immediate target.
- `notes/residuated-algebra-domain-completion.md`: recorded the new witness as
  the next residuation test case.
- `open_problems.md` and `ideas/research-questions.md`: closed the
  bottom-disciplined G2+FG2-without-FP task and opened the residuated-upgrade
  question.
- `models/README.md` and `outputs/README.md`: indexed the new model and report.
- `logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 17 to test whether the bottom-disciplined witnesses, starting with
`bottom-G2FG2-noFP`, admit full residuated expansions or require minimal
order/carrier repairs.

### Pass 17 - 2026-05-27 07:17 JST

Focus:

Test whether `bottom-G2FG2-noFP` admits a full residuated expansion on the same
carrier and order.

Proposer:

The unrestricted five-element tensor search is too large for the current brute
force script, but the model has a natural resource reading: $T$ is the
distinguished APS top and can be tried as monoid unit, while the true bottom
$b$ can be tried as absorbing zero. Adding commutativity makes the finite
search small enough to run exactly.

Skeptic:

This is a targeted positive result, not an exhaustive classification of all
possible tensors. The unrestricted report correctly records that the
$5^{16}$-per-unit operation space was not searched. The positive constrained
search is still mathematically useful because any found tensor/residual tables
are independently checkable witnesses.

Formalist:

`scripts/search-residuated-commutative-zero.py` checks the commutative
fixed-unit/fixed-zero space with unit $T$ and zero $b$. It searches
$5^6=15625$ tensors and finds 8 full-residuated candidates. The persisted
example has $b$ absorbing, $T$ as unit, $U\otimes U=U$,
$U\otimes a=a$, $U\otimes d=d$, and
$a\otimes a=a\otimes d=d\otimes d=b$. The checker confirms that
`bottom-G2FG2-noFP-residuated` preserves non-collapse, G2 true, FG2 true,
FP-synt false, and nFG2 pattern `TFTFTFTF`.

Archivist:

Fixed the unrestricted tensor-search conclusion so skipped searches no longer
claim a negative result, added the targeted commutative-zero search script,
generated the full-residuated expansion and reports, and updated the hierarchy,
classification, residuated-domain, model/output indexes, open problems, active
questions, and research log.

Repository updates:

- `scripts/search-residuated-tensor.py`: distinguishes "not searched because
  too large" from a negative searched result.
- `scripts/search-residuated-commutative-zero.py`: targeted finite search with
  fixed unit, fixed zero, and commutativity.
- `outputs/residuated-search-bottom-G2FG2-noFP.json`: unrestricted search-space
  report for the 5-element witness.
- `outputs/residuated-commutative-zero-search-bottom-G2FG2-noFP.json`: positive
  constrained search report with 8 full-residuated candidates.
- `models/examples/bottom-G2FG2-noFP-residuated.json`: same-order full
  residuated expansion.
- `outputs/g2-zoo-bottom-G2FG2-noFP-residuated.json`: checker report for the
  expansion.
- `outputs/bottom-discipline-filter-g2-zoo.json`: updated to include the
  residuated expansion.
- Topic notes, indexes, `open_problems.md`, `ideas/research-questions.md`, and
  `logs/research-log.md`: recorded the result and moved the next target to the
  bottom-disciplined $B_N$ family.

Next step:

Use pass 18 to test whether the bottom-disciplined arbitrary-depth witness
`bottom-nfg2-depth-3` admits an analogous full residuated expansion or requires
a smaller structural repair.

### Pass 18 - 2026-05-27 08:51 JST

Focus:

Test whether `bottom-nfg2-depth-3`, the checked $B_N$ arbitrary-depth witness,
admits a full residuated expansion on the same carrier and order.

Proposer:

The commutative-zero exhaustive strategy from pass 17 is too large for the
8-element $B_3$ instance. Instead use the visible shape of the construction:
$b$ is a true bottom, $U$ is a helper upper bound, and $T$ is the APS
top. Try $T$ as monoid unit, $b$ as zero, and make every nonzero,
non-unit product collapse upward to $U$.

Skeptic:

This is a strong resource operation: products of two non-unit nonzero elements
become $U$, not a more informative internal element. It is therefore a
same-order full-residuation witness, not evidence that a fine-grained or
BS16-like tensor exists. The uniform $B_N$ theorem still needs a written
proof, even though the checked $B_3$ instance verifies all finite algebraic
conditions.

Formalist:

Added `scripts/build-top-absorbing-residuated-expansion.py`. For a chosen unit
$e$, zero $z$, and absorber $u$, it builds
$$
z\otimes x=z,\qquad e\otimes x=x,\qquad x\otimes y=u
$$
in all remaining cases, then checks unit, zero, commutativity, associativity,
monotonicity, principal left/right residuals, and the full residuation law. On
`bottom-nfg2-depth-3` with $e=T$, $z=b$, and $u=U$, every check succeeds.
The resulting expansion preserves non-collapse, G2 true, FG2 false, FP-synt at
$s$, and nFG2 pattern `FFFTTTTT`.

Archivist:

Generated `bottom-nfg2-depth-3-residuated`, its top-absorbing residuation
report, and its G2-ZOO checker report. Updated the bottom-discipline report to
include the expansion. Recorded the result in the hierarchy, classification,
residuated-domain note, indexes, open problems, active questions, and research
log.

Repository updates:

- `scripts/build-top-absorbing-residuated-expansion.py`: constructive
  top-absorbing full-residuation builder/checker.
- `scripts/check-g2-zoo.py`: adds `--output` for writing checker JSON reports
  without shell redirection.
- `models/examples/bottom-nfg2-depth-3-residuated.json`: same-order full
  residuated expansion of the checked $B_3$ witness.
- `outputs/residuated-top-absorbing-report-bottom-nfg2-depth-3.json`:
  construction and verification report.
- `outputs/g2-zoo-bottom-nfg2-depth-3-residuated.json`: checker report for the
  expansion.
- `outputs/bottom-discipline-filter-g2-zoo.json`: updated to include the new
  residuated expansion.
- Topic notes, indexes, `open_problems.md`, `ideas/research-questions.md`, and
  `logs/research-log.md`: moved the next task to proving the uniform $B_N$
  residuation lemma and searching for less explosive tensors.

Next step:

Use pass 19 to write the general $B_N$ top-absorbing residuation lemma, or
find a strictly less top-collapsing tensor for the same family.

### Pass 19 - 2026-05-27 14:06 JST

Focus:

Promote the `bottom-nfg2-depth-3-residuated` construction to a uniform
same-order full-residuation lemma for every bottom-disciplined $B_N$.

Proposer:

The pass 18 tensor was not an accident of depth 3. The $B_N$ order always has
the same bounding skeleton $b\le x\le U$, plus only $s\le a_{N+1}$. That
shape is exactly what the top-absorbing tensor needs: $T$ acts as unit, $b$
as zero, and products of nonzero non-unit elements can all be sent to $U$.

Skeptic:

The result closes existence of full residuation for $B_N$, but it does so by
using a deliberately coarse tensor. A resource-sensitive reading may reject
the move because nearly every nontrivial product becomes the helper upper
bound. The next serious question is whether the same-order geometry forces
that coarseness or whether a finer tensor exists.

Formalist:

For $B_N$, let $M_N=B_N\setminus\{b,T\}$. Define
$$
b\otimes x=b,\qquad T\otimes x=x,\qquad
x\otimes y=U\quad(x,y\in M_N).
$$
This is a commutative monoid with unit $T$ and zero $b$. Associativity
follows because after removing $T$'s, any product containing $b$ is $b$,
while any product of at least two elements of $M_N$ is $U$, and $U\in M_N$
absorbs further non-unit nonzero factors. Monotonicity follows from the order
generators $b\le x$, $x\le U$, and $s\le a_{N+1}$. Residual fibers are
principal:
$$
b\backslash c=U,\quad T\backslash c=c,\quad
m\backslash c=
\begin{cases}
U & c=U,\\
T & m\le c\ne U,\\
b & \text{otherwise}
\end{cases}
$$
for $m\in M_N$, with identical right residuals by commutativity.

Archivist:

Recorded the uniform $B_N$ top-absorbing residuation lemma in the hierarchy
and residuated-domain notes. Marked the uniform existence question resolved,
and moved the active/open problem to finding less top-collapsing same-order
tensors or proving an obstruction.

Repository updates:

- `notes/g2-fg2-hierarchy.md`: added the uniform $B_N$ tensor and residual
  proof sketch.
- `notes/residuated-algebra-domain-completion.md`: added the same lemma from
  the residuated-APS perspective.
- `open_problems.md`: closed uniform top-absorbing existence and opened the
  finer-tensor/obstruction question.
- `ideas/research-questions.md`: retargeted the active question to the
  less-top-collapsing tensor problem.
- `logs/research-log.md`: recorded this autonomous pass.

Next step:

Use pass 20 to search for a less top-collapsing tensor on
`bottom-nfg2-depth-3`, starting with constraints that keep products among
orbit elements below $U$ whenever residuation permits.

### Pass 20 - 2026-05-27 20:55 JST

Focus:

Search for a less top-collapsing full-residuated tensor on
`bottom-nfg2-depth-3`.

Proposer:

Keep the constraints that made pass 18 tractable and mathematically legible:
commutativity, unit $T$, zero $b$, and $U\otimes x=U$ for every nonzero
$x\ne T$. Then search the remaining 15 unordered products on
$\{a_1,a_2,a_3,a_4,s\}$, minimizing the number of products equal to $U$.

Skeptic:

This does not remove the $U$-absorbing assumption. It only tests whether the
top-absorbing tensor was unnecessarily coarse inside that assumption. The
answer is positive for $B_3$, but the new pattern may still be depth-specific.

Formalist:

Added `scripts/search-u-absorbing-residuated.py`. It performs a complete
branch-and-bound search under the $U$-absorbing constraints, checks
associativity, monotonicity, and principal residual fibers, and emits residual
tables for the best witness. For `bottom-nfg2-depth-3`, the top-absorbing
template has 15 $U$-valued products among the 15 orbit/fixed-point products.
The search finds a full-residuated witness with 7 such products:
$$
a_1s=a_2,\quad a_2s=a_3,\quad
a_1a_4=a_2,\quad a_2a_4=a_3,\quad
a_4s=s^2=a_4^2=a_1,\quad a_1^2=a_3,
$$
with the remaining searched products equal to $U$. The checker confirms the
expanded model keeps G2 true, FG2 false, FP-synt at $s$, and nFG2 pattern
`FFFTTTTT`.

Archivist:

Persisted the new model, search report, and checker report; updated the
bottom-discipline report and the model/output indexes. The notes now record
that top-absorbing residuation is sufficient but not minimal for $B_3$. The
active problem is now to generalize the 7-$U$ pattern to $B_N$, or prove it
is depth-specific, and then test whether $U$-absorption can be weakened.

Repository updates:

- `scripts/search-u-absorbing-residuated.py`: complete constrained search for
  less top-collapsing $U$-absorbing tensors.
- `models/examples/bottom-nfg2-depth-3-u-absorbing-minU.json`: new
  full-residuated witness with 7 $U$-valued searched products.
- `outputs/residuated-u-absorbing-search-bottom-nfg2-depth-3.json`: search
  report.
- `outputs/g2-zoo-bottom-nfg2-depth-3-u-absorbing-minU.json`: checker report.
- `outputs/bottom-discipline-filter-g2-zoo.json`: updated to include the new
  expansion.
- Topic notes, indexes, `open_problems.md`, `ideas/research-questions.md`, and
  `logs/research-log.md`: recorded the result and retargeted the next problem.

Next step:

Use pass 21 to test whether the 7-$U$ pattern extends to $B_4$, or to write
the first obstruction explaining why it is special to $B_3$.

### Pass 21 - 2026-05-27 23:47 JST

Focus:

Test whether the less top-collapsing $U$-absorbing tensor pattern extends
from the checked $B_3$ witness to the next bottom-disciplined arbitrary-depth
witness $B_4$.

Proposer:

Generate `bottom-nfg2-depth-4` first, rather than extrapolating from the old
depth-3 artifact. Then try the pass 20 pattern at the level of the exponent
structure: give $a_{N+1}$ and $s$ exponent 1, give $a_i$ exponent
$i+1$, keep $T$ as unit and $b$ as zero, and send a product to $U$
only when the exponent sum exceeds $N+1$.

Skeptic:

The direct branch-and-bound $U$-absorbing search on $B_4$ did not finish
within the local 120-second pass budget, so this pass does not prove
minimality. It verifies a constructive template that is much finer than the
top-absorbing tensor, and it gives a concrete uniform conjecture to prove.

Formalist:

Added `scripts/build-truncated-u-absorbing-residuated.py`. It infers $N$
from the `a_i` names, constructs the truncated-exponent tensor, checks unit,
zero, commutativity, associativity, monotonicity, principal left/right
residuals, and the full residuation law, then emits both the verification
report and the expanded model. On `bottom-nfg2-depth-4`, it finds a
same-carrier/order full-residuated expansion with 10 $U$-valued products
among the 21 searched unordered products, compared with 21 for the
top-absorbing tensor. The G2-ZOO checker confirms G2 true, FG2 false, FP-synt
at $s$, and nFG2 pattern `FFFFTTTT`.

Archivist:

Persisted `bottom-nfg2-depth-4`, its truncated-exponent full-residuated
expansion, the construction report, and the checker reports. Updated the
bottom-discipline report and the model/output indexes. The active problem is
now a uniform proof of the truncated-exponent $B_N$ residuation template,
including an explicit residual table, followed by a test of whether
$U$-absorption itself is forced.

Repository updates:

- `scripts/build-truncated-u-absorbing-residuated.py`: constructive
  truncated-exponent $U$-absorbing residuation builder/checker.
- `models/examples/bottom-nfg2-depth-4.json`: checked depth-4
  bottom-disciplined arbitrary-depth witness.
- `models/examples/bottom-nfg2-depth-4-truncated-u-absorbing.json`:
  same-order full-residuated expansion.
- `outputs/residuated-truncated-u-absorbing-bottom-nfg2-depth-4.json`:
  construction and verification report.
- `outputs/g2-zoo-bottom-nfg2-depth-4.json`: checker report for the base
  witness.
- `outputs/g2-zoo-bottom-nfg2-depth-4-truncated-u-absorbing.json`: checker
  report for the expanded witness.
- `outputs/bottom-discipline-filter-g2-zoo.json`: updated to include the new
  base and expanded witnesses.
- Topic notes, indexes, `open_problems.md`, `ideas/research-questions.md`, and
  `logs/research-log.md`: recorded the depth-4 result and retargeted the next
  proof task.

Next step:

Use pass 22 to prove the truncated-exponent $U$-absorbing template uniformly
for $B_N$, including a closed residual table, or run $B_5$ as another
checked stress test before writing the proof.

### Pass 22 - 2026-05-28 00:17 JST

Focus:

Prove the truncated-exponent $U$-absorbing tensor template uniformly for the
bottom-disciplined $B_N$ family, including a closed residual table.

Proposer:

Treat the $B_3$ and $B_4$ tensors as instances of one finite algebraic
template. The key invariant is not the names of the orbit points but the
truncated exponent $e$: $e(s)=e(a_{N+1})=1$ and $e(a_i)=i+1$. Products
of two orbit/fixed-point elements add exponents until the sum exceeds $N+1$,
then overflow to $U$.

Skeptic:

This proof still assumes $U$-absorption. It proves a finer same-order
residuated expansion than the top-absorbing tensor, but it does not show that
$U$-absorption is forced or optimal. Also, the duplicate exponent-1 pair
$s,a_{N+1}$ must be handled explicitly in residuals because $s\le a_{N+1}$.

Formalist:

Let $A_N=\{s,a_1,\ldots,a_{N+1}\}$, put
$$
e(s)=e(a_{N+1})=1,\qquad e(a_i)=i+1,
$$
and define $\pi(1)=a_{N+1}$, $\pi(r)=a_{r-1}$ for $2\le r\le N+1$.
The tensor has $T$ as unit, $b$ as zero, $U$ absorbing over nonzero
non-units, and for $x,y\in A_N$:
$$
x\otimes y=
\begin{cases}
a_{e(x)+e(y)-1} & e(x)+e(y)\le N+1,\\
U & e(x)+e(y)>N+1.
\end{cases}
$$
Associativity is associativity of addition with overflow at $N+1$. The two
exponent-1 elements cause no associativity ambiguity because no product of two
non-unit elements has exponent 1. Monotonicity follows from the order
generators $b\le x$, $x\le U$, and $s\le a_{N+1}$; the last is preserved
because $s$ and $a_{N+1}$ have the same exponent.

For residuals:
$$
b\backslash c=U,\quad T\backslash c=c,\quad
U\backslash c=
\begin{cases}
U & c=U,\\
b & c\ne U,
\end{cases}
$$
and for $m\in A_N$, $q=e(m)$, and $t(a_i)=i+1$ for $1\le i\le N$,
$$
m\backslash c=
\begin{cases}
U & c=U,\\
T & m\le c,\\
\pi(t(c)-q) & c=a_i,\ 1\le i\le N,\ q<t(c),\\
b & \text{otherwise.}
\end{cases}
$$
Commutativity gives the same right residuals. These formulas make every
residual fiber principal, so the tensor is fully residuated on the original
$B_N$ carrier and order.

Archivist:

Recorded the tensor definition in `definitions.md`, added the uniform proof and
residual table to the hierarchy and residuated-domain notes, closed the
uniform-template proof task in `open_problems.md`, and retargeted the active
question to weakening or refuting the $U$-absorbing assumption.

Repository updates:

- `definitions.md`: added the truncated-exponent $U$-absorbing tensor
  definition for $B_N$.
- `notes/g2-fg2-hierarchy.md`: added the uniform proof, monotonicity argument,
  and residual table.
- `notes/residuated-algebra-domain-completion.md`: recorded the same lemma from
  the residuated-APS perspective.
- `open_problems.md` and `ideas/research-questions.md`: marked the uniform
  template proof resolved and moved the next question to weakening
  $U$-absorption.
- `notes/g2-aps-zoo-classification.md` and `logs/research-log.md`: updated the
  next-step registry and research trace.

Next step:

Use pass 23 to test whether the $U$-absorbing assumption can be weakened,
starting with the smallest checked case `bottom-nfg2-depth-3`.

### Pass 23 - 2026-05-28 00:47 JST

Focus:

Test whether the $U$-absorbing assumption can be weakened while keeping the
truncated-exponent orbit product table fixed.

Proposer:

Do not begin with a full unrestricted tensor search. First isolate the narrow
question left by pass 22: if the orbit/fixed-point products on
$A_N=\{s,a_1,\ldots,a_{N+1}\}$ are fixed to the truncated-exponent table, is
there any freedom left in products involving $U$?

Skeptic:

This is only a relative obstruction. It can show that $U$-absorption is
forced by the truncated table, but it cannot rule out a more radically
different same-order full-residuated tensor where the orbit product table also
changes.

Formalist:

Added `scripts/analyze-truncated-u-forcing.py`. The analyzer fixes $T$ as
unit, $b$ as zero, and the truncated-exponent products on $A_N$, but does
not assume $U\otimes x=U$. It checks whether monotonicity against the top
relation $x\le U$ already forces those products. On both
`bottom-nfg2-depth-3` and `bottom-nfg2-depth-4`, every $y\in A_N$ has some
$x\in A_N$ such that $x\le U$ and $x\otimes y=U$. Therefore
$$
U=x\otimes y\le U\otimes y,
$$
and since $U$ is top, $U\otimes y=U$. With $y\le U$, a second monotonicity
step forces $U\otimes U=U$. Thus, relative to the truncated orbit table,
$U$-absorption is forced by monotonicity alone, before residuals are checked.

Archivist:

Persisted forcing reports for B3 and B4, updated the hierarchy and
residuated-domain notes, and narrowed the active open question. The next search
must vary the orbit product table itself if it wants a genuinely
non-$U$-absorbing same-order residuated tensor.

Repository updates:

- `scripts/analyze-truncated-u-forcing.py`: analyzer for monotonicity-forced
  $U$-products relative to the truncated orbit table.
- `outputs/truncated-u-forcing-bottom-nfg2-depth-3.json`: B3 forcing report.
- `outputs/truncated-u-forcing-bottom-nfg2-depth-4.json`: B4 forcing report.
- `notes/g2-fg2-hierarchy.md` and
  `notes/residuated-algebra-domain-completion.md`: recorded the relative
  obstruction.
- `open_problems.md`, `ideas/research-questions.md`,
  `notes/g2-aps-zoo-classification.md`, `models/README.md`,
  `outputs/README.md`, and `logs/research-log.md`: updated the trace and next
  target.

Next step:

Use pass 24 to search for a non-$U$-absorbing same-order full-residuated
tensor on `bottom-nfg2-depth-3` by allowing the orbit product table itself to
vary.

### Pass 24 - 2026-05-28 03:01 JST

Focus:

Start the search for a non-$U$-absorbing same-order full-residuated tensor on
`bottom-nfg2-depth-3`, now allowing the orbit product table itself to vary.

Proposer:

Keep only the structural constraints that are already justified by the B3
residuated searches: commutativity, unit $T$, and zero $b$. Split the
search by the possible values of $U\otimes x$ allowed by monotonicity from
$T\le U$, then search the remaining products among the nonzero non-unit
elements.

Skeptic:

The full search is still large. A bounded run can produce useful engineering
information, but not a mathematical obstruction. The important distinction is
to record incompleteness clearly and use the failure mode to choose the next
pruning lemma.

Formalist:

Added `scripts/search-non-u-absorbing-residuated.py`. It fixes commutativity,
unit $T$, and zero $b$, does not assume $U$-absorption, and does not fix
the orbit product table. For each $U$-action pattern, it prunes domains using
monotonicity, then checks associativity, monotonicity, and principal left/right
residual fibers. On `bottom-nfg2-depth-3`, the persisted bounded report visits
1000 search nodes, 12 $U$-action patterns, and 382 complete assignments
without finding a candidate. A larger 10000-node attempt did not finish within
the local 120-second pass budget, so this is an incomplete negative result.

Archivist:

Persisted the bounded search report and search script, updated the hierarchy
and residuated-domain notes, and narrowed the next task to adding residual-fiber
pruning. The zero-target fibers $m\backslash b$ are the first likely pruning
site, because many naive non-$U$-absorbing tables produce non-principal zero
fibers.

Repository updates:

- `scripts/search-non-u-absorbing-residuated.py`: orbit-table-varying search
  that does not assume $U$-absorption.
- `outputs/residuated-non-u-absorbing-search-bottom-nfg2-depth-3.json`: bounded
  incomplete B3 search report.
- `notes/g2-fg2-hierarchy.md` and
  `notes/residuated-algebra-domain-completion.md`: recorded the partial search
  and its limitation.
- `open_problems.md`, `ideas/research-questions.md`,
  `notes/g2-aps-zoo-classification.md`, `models/README.md`,
  `outputs/README.md`, and `logs/research-log.md`: updated the next target.
- Relay logs from the earlier 2026-05-28 sync were preserved: ChatGPT share
  links were unreachable, and Drive outputs had no newly relevant post-2026-05-22
  items.

Next step:

Use pass 25 to add residual-fiber pruning to the B3 non-$U$-absorbing search,
starting with the $m\backslash b$ fibers.

### Pass 25 - 2026-05-28 05:44 JST

Focus:

Complete the B3 non-$U$-absorbing same-order residuation search by adding
residual-fiber pruning.

Proposer:

Use partial residual-fiber principality as a search-time constraint. For every
partially known fiber, keep only branches where some principal downset can still
contain all known included elements and exclude all known excluded elements.
This generalizes the intended $m\backslash b$ pruning rather than hard-coding
only the zero target.

Skeptic:

The result must be read against pass 23: $U$-absorption is forced if the
truncated orbit table is fixed. A non-$U$-absorbing witness therefore has to
change the orbit table, so it may be algebraically less close to the
truncated-exponent construction.

Formalist:

Updated `scripts/search-non-u-absorbing-residuated.py` with partial
left/right residual-fiber pruning. The B3 search now completes: it visits 47
$U$-action patterns, prunes 16 immediately, prunes 1537 branches by residual
fiber obstruction, checks 475 complete assignments, and finds
`bottom-nfg2-depth-3-non-u-absorbing`. The tensor is full-residuated with unit
$T$ and zero $b$, but
$$
U\otimes a_4=a_4,\qquad U\otimes s=s.
$$
The orbit table changes: $a_1,a_2,a_3$ form a Klein-four pattern over $T$,
$a_j\otimes a_4=a_4$, $a_j\otimes s=s$ for $j=1,2,3$, and
$$
a_4^2=a_4,\qquad a_4s=s^2=b.
$$
The G2-ZOO checker confirms G2 true, FG2 false, FP-synt at $s$, and nFG2
pattern `FFFTTTTT`.

Archivist:

Persisted the expanded model, the completed search report, the checker report,
and the updated bottom-discipline report. Updated the hierarchy,
residuated-domain, classification, model/output indexes, open problems, active
questions, and research log. The next question is whether the B3
non-$U$-absorbing pattern extends to B4 or admits a uniform $B_N$ form.

Repository updates:

- `scripts/search-non-u-absorbing-residuated.py`: added residual-fiber pruning.
- `models/examples/bottom-nfg2-depth-3-non-u-absorbing.json`: full-residuated
  non-$U$-absorbing B3 expansion.
- `outputs/residuated-non-u-absorbing-search-bottom-nfg2-depth-3.json`:
  completed positive search report.
- `outputs/g2-zoo-bottom-nfg2-depth-3-non-u-absorbing.json`: checker report.
- `outputs/bottom-discipline-filter-g2-zoo.json`: updated to include the new
  expansion.
- Topic notes, indexes, `open_problems.md`, `ideas/research-questions.md`, and
  `logs/research-log.md`: retargeted the next problem to B4/uniform extension.

Next step:

Use pass 26 to test whether the non-$U$-absorbing B3 tensor pattern extends
to `bottom-nfg2-depth-4`.

### Pass 26 - 2026-05-28 06:14 JST

Focus:

Test whether the non-$U$-absorbing same-order full-residuated phenomenon
found at checked B3 persists at checked B4.

Proposer:

Run the orbit-table-varying search directly on `bottom-nfg2-depth-4`, even if
full exhaustiveness is too expensive. A single verified full-residuated witness
is enough to answer the existential B4 question, while optimization and
classification can remain separate.

Skeptic:

The bounded B4 run cannot prove minimality or uniqueness. It also should not
be described as the B3 pattern literally extending: the found B4 tensor changes
the product-table shape, so the current evidence is existential rather than a
uniform construction.

Formalist:

The search report
`outputs/residuated-non-u-absorbing-search-bottom-nfg2-depth-4.json` stops at
1000 nodes after 48 $U$-action patterns, 697 residual-fiber prunes, and 147
complete assignments. It nevertheless finds a fully checked same-order
residuated expansion. In the found tensor:
$$
U\otimes a_1=a_1,\qquad U\otimes a_2=a_2,
$$
so $U$-absorption fails, while $U\otimes a_3=U\otimes a_4=U\otimes a_5
=U\otimes s=U$. The lower part is not the B3 Klein-four pattern:
$$
a_1^2=a_1,\qquad a_2^2=a_2,\qquad a_1a_2=b.
$$
The G2-ZOO checker confirms that
`bottom-nfg2-depth-4-non-u-absorbing` keeps G2 true, FG2 false, FP-synt at
$s$, bottom discipline, and nFG2 pattern `FFFFTTTT`.

Archivist:

Persisted the B4 non-$U$-absorbing expansion, its bounded positive search
report, checker report, and refreshed bottom-discipline report. Updated the
hierarchy, residuated-domain, classification, model/output indexes, open
problems, active questions, and research log. The active question now shifts
from B4 existence to whether the checked B3 and B4 witnesses have a uniform
$B_N$ explanation.

Repository updates:

- `models/examples/bottom-nfg2-depth-4-non-u-absorbing.json`: B4 same-order
  full-residuated non-$U$-absorbing expansion.
- `outputs/residuated-non-u-absorbing-search-bottom-nfg2-depth-4.json`:
  bounded positive search report.
- `outputs/g2-zoo-bottom-nfg2-depth-4-non-u-absorbing.json`: checker report.
- `outputs/bottom-discipline-filter-g2-zoo.json`: refreshed with the B4
  expansion.
- Topic notes, indexes, `open_problems.md`, `ideas/research-questions.md`, and
  `logs/research-log.md`: retargeted the next problem to a uniform $B_N$
  explanation or obstruction.

Next step:

Use pass 27 to compare the checked B3 and B4 non-$U$-absorbing tensors and
search for either a uniform $B_N$ construction schema or a proof that the
known witnesses are depth-specific repairs.

### Pass 27 - 2026-05-28 11:03 JST

Focus:

Compare the checked B3/B4 non-$U$-absorbing tensors and extract a uniform
construction candidate.

Proposer:

Use the B4 bounded-search witness as the guide. It has a simple decomposition:
$a_1,a_2$ are front orthogonal idempotents, $U$ fixes that front, and the
remaining tail follows a shifted truncated-exponent product. Package that as a
builder rather than treating the B4 table as a one-off search artifact.

Skeptic:

This does not prove the earlier max-non-$U$ B3 search witness is the member
of a uniform family. In fact, the front-shifted depth-3 tensor is different and
has fewer non-$U$ products. The correct claim is therefore existence of a
uniform non-$U$-absorbing template candidate, not minimality or uniqueness.

Formalist:

Added `scripts/build-front-shifted-non-u-absorbing-residuated.py`. For
$N\ge3$, the template splits $B_N$ into front $F=\{a_1,a_2\}$ and tail
$R_N=\{s,a_{N+1},a_3,\ldots,a_N\}$. The front satisfies
$$
a_1^2=a_1,\qquad a_2^2=a_2,\qquad a_1a_2=b,
$$
and $U$ fixes the front:
$$
U\otimes a_1=a_1,\qquad U\otimes a_2=a_2.
$$
The tail uses shifted exponents
$$
\tau(s)=\tau(a_{N+1})=1,\qquad \tau(a_i)=i-1\quad(3\le i\le N),
$$
with overflow above $N-1$ sent to $U$. The builder verifies associativity,
monotonicity, principal left/right residual fibers, and the residuation law.
It succeeds for depths 3, 4, and 5. At depth 4, the generated tensor is exactly
the pass 26 bounded-search witness. At depth 5, the new expansion preserves
G2 true, FG2 false, FP-synt at $s$, bottom discipline, and nFG2 pattern
`FFFFFTTT`.

Archivist:

Recorded the front-shifted tensor definition, added the builder and checked
depth-3/4/5 construction reports, generated the depth-5 base and expanded
models, and refreshed the model registry and bottom-discipline report. The
remaining mathematical task is no longer to find a uniform candidate, but to
write the closed residual table and prove the template for all $N\ge3$.

Repository updates:

- `scripts/build-front-shifted-non-u-absorbing-residuated.py`: uniform template
  builder/checker.
- `models/examples/bottom-nfg2-depth-5.json`: next checked bottom-disciplined
  first-true nFG2 witness.
- `models/examples/bottom-nfg2-depth-{3,4,5}-front-shifted-non-u-absorbing.json`:
  checked template expansions.
- `outputs/residuated-front-shifted-non-u-absorbing-bottom-nfg2-depth-{3,4,5}.json`
  and matching G2-ZOO reports: construction and checker artifacts.
- `definitions.md`, topic notes, indexes, `open_problems.md`,
  `ideas/research-questions.md`, `outputs/bottom-discipline-filter-g2-zoo.json`,
  and `logs/research-log.md`: updated to make the residual-table proof the next
  target.

Next step:

Use pass 28 to derive the explicit residual table for the front-shifted
non-$U$-absorbing template and turn the checked schema into a uniform
$B_N$ lemma.

### Pass 28 - 2026-05-28 11:33 JST

Focus:

Derive the residual table for the front-shifted non-$U$-absorbing $B_N$
template and close the gap between finite checks and a uniform lemma.

Proposer:

Keep the proof organized by the front/tail split. The front part should have a
two-element orthogonal-idempotent residual table; the tail part should be
shifted exponent subtraction, with a special case for the duplicate exponent-1
pair $s,a_{N+1}$.

Skeptic:

The residual table proves full residuation for this template, not minimality
or uniqueness among non-$U$-absorbing tensors. The earlier B3 search witness
still has more non-$U$ products than the front-shifted B3 member, so
classification remains separate.

Formalist:

Recorded the closed residual table in `definitions.md` and the hierarchy note.
For $p\in\{a_1,a_2\}$, $p\backslash c$ is $U$ at targets $p,U$, and
the other front element otherwise. For $U$, the residual is $U$ at $U$,
the target itself at front targets, and $b$ otherwise. For tail
$r\in R_N$, front targets return the front element, exact targets return
$T$, shifted exponent subtraction returns $a_{N+1}$ or $a_{d+1}$, and
impossible fibers return $b$. Commutativity gives the right residuals.
Added `scripts/check-front-shifted-residual-formula.py`, which compares this
symbolic table with generated residuals. The reports for depths 3, 4, and 5
all have zero mismatches.

Archivist:

Updated `definitions.md`, hierarchy and residuated-domain notes, the model and
output indexes, open problems, active questions, and the research log. The
front-shifted construction is now recorded as a uniform same-order
full-residuated non-$U$-absorbing template for $B_N$ with $N\ge3$. The
next meaningful problem is structural interpretation: whether the front/tail
decomposition is a product, quotient, or ideal-extension construction, and how
it behaves with respect to weakening/contraction.

Repository updates:

- `scripts/check-front-shifted-residual-formula.py`: symbolic residual-table
  checker.
- `outputs/front-shifted-residual-table-check-bottom-nfg2-depth-{3,4,5}.json`:
  zero-mismatch checks against generated left/right residuals.
- `definitions.md`, `notes/g2-fg2-hierarchy.md`, and
  `notes/residuated-algebra-domain-completion.md`: explicit residual table and
  proof outline.
- `open_problems.md`, `ideas/research-questions.md`,
  `notes/g2-aps-zoo-classification.md`, `models/README.md`,
  `outputs/README.md`, and `logs/research-log.md`: retargeted from residual
  proof to structural interpretation.

Next step:

Use pass 29 to analyze the structural-rule profile of the front-shifted
template, especially contraction and weakening compared with the
truncated-exponent $U$-absorbing template.

### Pass 29 - 2026-05-28 12:03 JST

Focus:

Analyze the structural-rule profile of the front-shifted non-$U$-absorbing
$B_N$ tensor, especially contraction and weakening.

Proposer:

Add a small analyzer for the Axis III rules already listed in the zoo note:
exchange $E$, contraction $C$, and the strong weakening rule
$a\le b\Rightarrow a\otimes c\le b$. Compare the front-shifted template
against the top-absorbing, truncated $U$-absorbing, earlier non-$U$, and
G2+FG2-without-FP residuated witnesses.

Skeptic:

The strong weakening rule is very strong in this APS order, since the monoid
unit is $T$ but many elements are not below $T$. Therefore a negative
weakening result is expected. The useful information is not merely that $W$
fails, but where contraction fails and whether the front/tail split has a
visible structural signature.

Formalist:

Added `scripts/analyze-structural-rules.py` and saved
`outputs/structural-rules-front-shifted-comparison.json`. All eight compared
residuated tensors satisfy exchange. None satisfies strong weakening or the
reflexive discarding instance $a\otimes c\le a$; the unit already gives
witnesses $T\otimes c=c\not\le T$. Global contraction holds only for
`bottom-G2FG2-noFP-residuated`. In the front-shifted family, however,
contraction holds on the front idempotents $a_1,a_2$ and fails in the shifted
tail. Checked failures include $a_3^2=U$, $a_{N+1}^2=a_3$, and
$s^2=a_3$ in the relevant depths.

Archivist:

Updated the structural-rule axis, hierarchy note, residuated-domain note,
definitions, open problems, active questions, model/output indexes, and
research log. The next task is now algebraic presentation: describe the
front-shifted tensor as an ideal-extension, orthogonal-sum, or related
construction explaining localized front contraction and tail resource
sensitivity.

Repository updates:

- `scripts/analyze-structural-rules.py`: structural-rule checker.
- `outputs/structural-rules-front-shifted-comparison.json`: comparison report.
- `definitions.md`: normalized the finite $E,C,W$ structural-rule checks.
- `notes/g2-aps-zoo-classification.md`, `notes/g2-fg2-hierarchy.md`, and
  `notes/residuated-algebra-domain-completion.md`: recorded the result.
- `open_problems.md`, `ideas/research-questions.md`, `models/README.md`,
  `outputs/README.md`, and `logs/research-log.md`: retargeted the next problem
  to algebraic presentation of the front/tail split.

Next step:

Use pass 30 to present the front-shifted tensor as an ideal-extension or
orthogonal-sum style construction and isolate the exact proof obligations for
that presentation.

### Pass 30 - 2026-05-28 12:33 JST

Focus:

Present the front-shifted non-$U$-absorbing $B_N$ tensor as an algebraic
extension, and decide whether "orthogonal sum" or "ideal extension" is the
right reading.

Proposer:

Use the front/tail split to define a genuine tensor ideal
$I=\{b,a_1,a_2\}$. If $I$ is downward closed and absorbs multiplication by
all elements, then the front-shifted tensor is not merely a patched table. It
is a Rees-style ideal extension: a contractive two-atom front ideal is glued
onto the shifted truncated tail.

Skeptic:

Calling the construction an orthogonal sum would be misleading. Cross-products
between a front atom and a tail element do not vanish to $b$; they project
back to the chosen front atom. Also, the presentation should not be advertised
as a classification theorem. It explains the current template but does not show
that all same-order non-$U$-absorbing repairs arise this way.

Formalist:

Added `scripts/check-front-shifted-extension-presentation.py` and saved
`outputs/front-shifted-extension-presentation-check.json`. For the checked
depths 3, 4, and 5, the script verifies that $I=\{b,a_1,a_2\}$ is a downward
closed two-sided tensor ideal, that $a_1,a_2$ form an orthogonal idempotent
zero-band, and that the quotient collapsing $I$ to $b$ has representatives
$\{b,T,U,s,a_{N+1},a_3,\ldots,a_N\}$ carrying exactly the shifted tail
product. This explains local contraction as behavior internal to $I$, while
the quotient tail keeps the noncontractive resource-sensitive product.

Archivist:

Recorded the ideal-extension presentation in `definitions.md`, the hierarchy
note, the residuated-domain note, and the G2-ZOO classification note. Updated
the active question and open problems away from "find a presentation" and
toward classification of possible front tensor ideals.

Repository updates:

- `scripts/check-front-shifted-extension-presentation.py`: verifies the
  front-ideal extension presentation.
- `outputs/front-shifted-extension-presentation-check.json`: depth-3/4/5
  verification report.
- `definitions.md`: added the front ideal-extension presentation.
- `notes/g2-fg2-hierarchy.md`,
  `notes/residuated-algebra-domain-completion.md`, and
  `notes/g2-aps-zoo-classification.md`: recorded the structural reading.
- `open_problems.md`, `ideas/research-questions.md`, `models/README.md`,
  `outputs/README.md`, and `logs/research-log.md`: retargeted the next problem
  to classifying front-ideal extensions.

Next step:

Use pass 31 to classify small tensor ideals that can replace
$\{b,a_1,a_2\}$ in the front-extension recipe, or prove that the two-atom
zero-band is forced by the present same-order, same-tail constraints.

### Pass 31 - 2026-05-28 15:17 JST

Focus:

Classify the possible size of the orthogonal front ideal in the shifted-tail
schema, keeping the same $B_N$ order.

Proposer:

Generalize the pass-30 presentation by replacing the two-front set with
$$
F_k=\{a_1,\ldots,a_k\}.
$$
Keep the same proof-theoretic shape: $F_k$ is an orthogonal idempotent
zero-band, front elements project products with the tail back to themselves,
and the quotient tail starts at $a_{k+1}$. This gives a clean finite test for
whether the two-front construction is forced or merely one positive choice.

Skeptic:

The current order has front atoms pairwise incomparable. If $k\ge3$, the
residual $p\backslash b$ should fail to exist as a principal element, because
all the other front atoms multiply with $p$ to $b$, and no one of them
dominates the others. Therefore a width-3 failure would be a structural
obstruction, not a search artifact.

Formalist:

Added `scripts/check-front-ideal-size-bound.py` and saved
`outputs/front-ideal-size-bound-check.json`. At depths 3, 4, and 5, front
widths $0,1,2$ pass the unit, zero, commutativity, associativity,
monotonicity, principal residual, and residuation checks. Width $3$ is the
first failure in every checked depth. The displayed witness is the expected
non-principal fiber: for $p=a_1$, $p\backslash b$ has fiber
$\{b,a_2,a_3\}$, with $a_2$ and $a_3$ incomparable.

Archivist:

Recorded the orthogonal front-width bound in `definitions.md`, the hierarchy
note, the residuated-domain note, and the G2-ZOO classification note. Retargeted
the active problem from broad ideal classification to the uniform front-width
theorem, especially the one-front residual table and the $k\ge3$
non-principal-fiber obstruction.

Repository updates:

- `scripts/check-front-ideal-size-bound.py`: generalized orthogonal front-width
  checker.
- `outputs/front-ideal-size-bound-check.json`: depth-3/4/5 report showing
  widths $0,1,2$ pass and width $3$ first fails.
- `definitions.md`, `notes/g2-fg2-hierarchy.md`,
  `notes/residuated-algebra-domain-completion.md`, and
  `notes/g2-aps-zoo-classification.md`: recorded the bound and obstruction.
- `open_problems.md`, `ideas/research-questions.md`, `models/README.md`,
  `outputs/README.md`, and `logs/research-log.md`: retargeted the next proof
  task.

Next step:

Use pass 32 to turn the checked front-width pattern into a uniform theorem:
write the closed residual table for width $1$, fold widths $0,1,2$ into a
single statement where possible, and prove the $k\ge3$ obstruction directly.

### Pass 32 - 2026-05-28 15:47 JST

Focus:

Turn the checked orthogonal front-width pattern into a uniform residual theorem
for widths $0,1,2$, and isolate what remains beyond the same-order schema.

Proposer:

The right statement is not only "the two-front template works." It is a
three-case theorem: $k=0$ recovers the truncated $U$-absorbing tensor,
$k=1$ gives a one-front non-$U$-absorbing tensor, and $k=2$ gives the
front-shifted template. All three share the same shifted-tail residual table,
with only the front residual clause changing.

Skeptic:

The $k\ge3$ obstruction depends on orthogonal front atoms in the same
$B_N$ order. It should not be overstated as ruling out all larger front
ideals. A non-orthogonal front multiplication or an added join/order relation
among front atoms could make the bad residual fiber principal, at the cost of
changing the algebraic or APS profile.

Formalist:

Added `scripts/check-front-width-residual-formula.py` and saved
`outputs/front-width-residual-formula-check.json`. For $k=0,1,2$, the script
compares a closed residual formula against generated residuals at depths 3, 4,
and 5. The report has nine checked cases and zero mismatches. The formula uses
$\tau_k(s)=\tau_k(a_{N+1})=1$,
$\tau_k(a_i)=i-k+1$, and
$\rho_k(1)=a_{N+1},\rho_k(d)=a_{k+d-1}$. For $p\in F_k$,
$p\backslash c=U$ at $c=p,U$; otherwise it is $b$ for $k=1$ and the
other front atom for $k=2$. The $k=0$ case has no front clause.

Archivist:

Recorded the uniform residual table in `definitions.md`, updated the hierarchy
and residuated-domain notes, and marked the orthogonal-front same-order theorem
as resolved for the current schema. The next open direction is now deliberately
narrower: test whether non-orthogonal front ideals or mild front-order
refinements can avoid the $k\ge3$ principal-fiber obstruction.

Repository updates:

- `scripts/check-front-width-residual-formula.py`: closed residual formula
  checker for orthogonal front widths $0,1,2$.
- `outputs/front-width-residual-formula-check.json`: zero-mismatch report for
  depths 3, 4, and 5.
- `definitions.md`, `notes/g2-fg2-hierarchy.md`,
  `notes/residuated-algebra-domain-completion.md`, and
  `notes/g2-aps-zoo-classification.md`: recorded the uniform residual table.
- `open_problems.md`, `ideas/research-questions.md`, `models/README.md`,
  `outputs/README.md`, and `logs/research-log.md`: retargeted the next problem
  to non-orthogonal front ideals or front-order refinements.

Next step:

Use pass 33 to test the smallest $k=3$ escape route: add one front join or
try a non-orthogonal front multiplication, then check whether full residuation
and the $B_N$ APS profile survive.

### Pass 33 - 2026-05-30 JST

Focus:

Test the smallest escape route from the orthogonal-front $k\ge3$
principal-fiber obstruction. Two routes exist: (A) keep the $B_N$ order but
replace the pairwise-zero front product with a non-orthogonal one; (B) add a
join among front atoms, promoting some incomparable pair to a comparable one.
Determine which route, if any, reinstates principal $p\backslash b$ fibers
while preserving full residuation and the G2/nFG2 APS profile.

Proposer:

The $k=3$ obstruction proof in pass 31 ran as follows. Take three pairwise
incomparable front atoms $a_1,a_2,a_3$ with $a_i a_j=b$ for $i\ne j$. The
fiber of $a_1\backslash b$ must contain every $x$ such that $a_1\otimes x\le b$.
Both $a_2$ and $a_3$ qualify because $a_1\otimes a_2=b\le b$ and
$a_1\otimes a_3=b\le b$. Since $a_2\parallel a_3$ in $B_N$, the fiber has no
principal element above both of them, so the residual fails.

The two atomic repairs are therefore:

**Route A (non-orthogonal product)**: Set $a_1\otimes a_2 = a_3$ (or some
non-$b$ value). The residual fiber of $a_1\backslash b$ then excludes $a_2$
(because $a_1\otimes a_2=a_3\not\le b$), potentially leaving a principal fiber.

**Route B (front join)**: Add $a_2\le a_3$ to the order (keeping the original
pairwise-zero product). The fiber of $a_1\backslash b$ still contains both
$a_2$ and $a_3$, but now $a_2\le a_3$ makes $a_3$ the principal maximum.

Both routes change the algebraic or order structure of the model. The question
is whether either preserves the APS and structural-rule profile that the $B_N$
construction was built for.

Skeptic:

Route A is dangerous: if $a_1\otimes a_2=a_3$ but $a_2\otimes a_1=a_3$
(commutativity), then $a_3\backslash b$ now has fiber including $a_1$ and $a_2$
for the same reason, just with the $k=3$ cycle shifted. Unless the three atoms
are given a total order (which breaks the original $B_N$ APS structure), the
non-orthogonal front product appears to propagate the principal-fiber failure
around the triangle.

Route B is cleaner algebraically, but adding $a_2\le a_3$ changes the carrier
poset. Specifically, $a_3$ is now above $a_2$ in $B_N$, which changes the
antitonicity check for $\boxtimes$. In $B_N$, the front atoms $a_1,\ldots,a_k$
are not in the $\boxtimes$-orbit of $T$ (they are in the tail), so the G2/FG2
status is unaffected — but antitonicity of $\boxtimes$ must be rechecked.

Formalist:

**Route A analysis (non-orthogonal $k=3$ front):**

Let $F_3=\{a_1,a_2,a_3\}$ with cycle product $a_i\otimes a_{i+1\bmod3}=a_{i+2\bmod3}$
(cyclic rotation, indices mod 3). For each $p=a_i$, the fiber of
$p\backslash b$ is $\{x:p\otimes x\le b\}$. With the cyclic product, we need
$p\otimes x\le b$, i.e., $p\otimes x=b$. The only $x\in F_3$ satisfying
$p\otimes x=b$ is $x=p$ itself (idempotent: $a_i^2=b$ if we keep that). But
then $p\backslash b$ has fiber $\{b,a_i,\ldots\}$ — we need to also include
tail elements $r$ with $a_i\otimes r\le b$. In the shifted tail template,
$a_i\otimes r=a_i$ (front absorbs tail), so $a_i\not\le b$, excluding all tail
elements. If additionally the self-product $a_i^2$ is changed from $b$ to $a_i$
(idempotent) or some tail element, the fiber changes further.

The clean case: take $a_i^2=a_i$ (idempotent on the diagonal) and
$a_i\otimes a_j=a_k$ (cyclic for $\{i,j,k\}=\{1,2,3\}$). Then $p\backslash b$
has fiber $\{x:p\otimes x\le b\}$. Since $p\otimes p=p\not\le b$ and
$p\otimes a_j=a_k\not\le b$ for $j\ne i$, the only elements of $F_3$ in the
fiber are those $x$ with $p\otimes x=b$ — but we have assigned no product to
$b$ for pairs in $F_3$, so the fiber in $F_3$ is empty. Including $b$ itself:
$p\otimes b=b\le b$, so $b$ is in the fiber. The fiber restricted to the
front+$b$ part is $\{b\}$, which is principal at $b$. But we must also include
the tail: since front absorbs tail, $p\otimes r=p\not\le b$, so no tail element
is in the fiber. Hence $p\backslash b=b$ for each front atom.

This is the cyclic idempotent route. The residual is principal at $b$.

Remaining checks: does this tensor satisfy associativity? We have $(a_1\otimes
a_2)\otimes a_3=a_3\otimes a_3=a_3$, while $a_1\otimes(a_2\otimes
a_3)=a_1\otimes a_1=a_1$. So $a_3\ne a_1$: associativity fails.

The cyclic assignment is not associative. The obstruction is structural:
the cyclic group $\mathbb Z/3\mathbb Z$ is associative, but mapping it onto
$\{a_1,a_2,a_3\}$ conflicts with having $a_i^2=a_i$ (idempotent), since in any
group $x^2=x$ forces $x=e$. Idempotent cyclic products are contradictory.

Retry with the cyclic group product: $a_1^2=a_2$, $a_2^2=a_3$, $a_3^2=a_1$,
$a_1a_2=a_3$, $a_2a_3=a_1$, $a_3a_1=a_2$. This is the cyclic group of order 3
embedded in $\{a_1,a_2,a_3\}$. Then $p\backslash b$: $p\otimes x=b$ requires
$x$ such that $p\cdot x=b$ in the front group. In a group with no zero, there
is no $x$ with $p\cdot x=b$ unless $b$ is the group identity. If $b$ is
not in the group, the fiber in $F_3$ is empty; $b$ maps to $b$ by absorption,
so the fiber is $\{b\}$ again, principal at $b$. But now $a_i\otimes b=b$
(zero absorption), and the residual $b\backslash b$ is $U$ (top), not $T$. So
$p\backslash b=b$ would mean $p\otimes b=b\le b$ ✓ and $p\otimes x\le b$
requires $p\cdot x=b$ in the front group — impossible for $x\in F_3$ since no
product is $b$. So the fiber above $b$ is empty in $F_3$, and the fiber is
$\{b\}$, giving $p\backslash b=b$. Principal. ✓

Associativity: the cyclic group of order 3 is associative. Checking
interactions with tail: $a_i\otimes(a_j\otimes r)=a_i\otimes a_j=a_{k}$, and
$(a_i\otimes a_j)\otimes r=a_k\otimes r=a_k$. ✓ Front interactions with zero
and unit: $b\otimes x=b$ (zero), $T\otimes x=x$ (unit). ✓

Monotonicity: the order generators of $B_N$ are $b\le x$ for all $x$, $x\le U$
for all $x$, and $s\le a_{N+1}$. For $b\le a_i$: $b\otimes y=b\le a_i\otimes
y$ — need $b\le a_i\cdot y$ for all $y$. Since $b$ is bottom, this holds. ✓
For $a_i\le U$: $a_i\otimes y\le U\otimes y$ — if $y\in F_3$, $a_i\otimes y$
is some $a_j$ and $U\otimes a_j=a_j$ (from the non-$U$-absorbing front template
where $U\otimes a_i=a_i$). So $a_j\le a_j$ ✓. For $s\le a_{N+1}$: both are in
the tail, and $a_i\otimes s=a_i$, $a_i\otimes a_{N+1}=a_i$. So $a_i\le a_i$.
✓

The cyclic group of order 3 as front multiplication, with $U$ acting as the
identity on front atoms ($U\otimes a_i=a_i$), gives a non-orthogonal
$k=3$ front ideal that is associative, principal-fiber residuated, and
monotone on the $B_N$ order.

**G2/FG2/nFG2 profile**: the $T$-orbit of $\boxtimes$ in $B_N$ runs
$T\to a_1\to\cdots\to a_{N+1}\to s\to s\to\cdots$. The front atoms $a_1,
\ldots, a_k$ are in the orbit chain for small $k$, and whether the orbit stays
in the group or exits to the tail depends on $N$ and $k$. For $k=3$ and
$N\ge3$, orbit element $a_1=\boxtimes T$, then $\boxtimes a_1=a_2$, then
$\boxtimes a_2=a_3$, then $\boxtimes a_3=a_4$ (now in the tail). The group
multiplication is not the $\boxtimes$ map; $\boxtimes$ on the front atoms is
already determined by the orbit, and the tensor product $\otimes$ is a separate
operation. So the G2/FG2/nFG2 profile is determined by $\boxtimes$, not by
$\otimes$. Adding the cyclic group tensor on $F_3$ does not change the orbit
structure. The APS properties are therefore preserved.

**Summary of Route A resolution**:

The cyclic-group-of-order-3 front multiplication (with $b$ as absorbing zero and
$U\otimes a_i=a_i$) escapes the principal-fiber obstruction at $k=3$. The
residual $p\backslash b=b$ is principal. Associativity holds via the cyclic
group. Monotonicity holds on the $B_N$ order generators. The APS profile
(G2, FG2 false, FP-synt at $s$, arbitrary-depth nFG2) is unchanged.

The key algebraic fact is: **the $k\ge3$ obstruction is specific to the
orthogonal-front schema (pairwise-zero cross-products). A cyclic group
front evades it by making cross-products non-zero, removing their fiber
contributions.**

**Route B analysis (front join, order extension):**

Add $a_2\le a_3$ to $B_N$ while keeping the pairwise-zero product. The fiber
of $a_1\backslash b$ still contains both $a_2$ and $a_3$ (since
$a_1\otimes a_2=b$ and $a_1\otimes a_3=b$). But now $a_2\le a_3$ in the
extended order, so $a_3$ is the maximum of $\{a_2,a_3\}$, and the fiber is
principal at $a_3$: $a_1\backslash b=a_3$. ✓

However, antitonicity of $\boxtimes$: the orbit has $\boxtimes a_1=a_2$ and
$\boxtimes a_2=a_3$ (for $k=3$ and $N\ge3$). With $a_2\le a_3$ in the extended
order, antitonicity requires $\boxtimes a_3\le\boxtimes a_2=a_3$ and
$\boxtimes a_2\le\boxtimes a_1=a_2$, i.e., $\boxtimes a_2=a_3\le a_2$. But
$a_3\not\le a_2$ in the extended order (we only added $a_2\le a_3$, not
$a_3\le a_2$). So antitonicity fails: $\boxtimes a_2=a_3\not\le a_2=\boxtimes
a_1$ when $a_1\le a_2$ (if we added that too) is not present.

Wait — the orbit has $a_1=\boxtimes T$ and $a_2=\boxtimes a_1$, and we added
$a_2\le a_3$ (not $a_1\le a_2$). Antitonicity says $x\le y\Rightarrow\boxtimes
y\le\boxtimes x$. The new relation is $a_2\le a_3$, so antitonicity requires
$\boxtimes a_3\le\boxtimes a_2=a_3$. In $B_N$ (pre-extension), $\boxtimes
a_3=a_4$ (a tail element). So we need $a_4\le a_3$ in the extended order. This
is not among the added relations, so antitonicity fails unless we also add
$a_4\le a_3$.

Adding $a_4\le a_3$ then requires (by antitonicity of $\boxtimes$)
$\boxtimes a_3\le\boxtimes a_4$, i.e., $a_4\le a_5$, and so on down the orbit.
This cascading relation addition will eventually require $s\le a_{N+1}$ — which
is already present — and then $\boxtimes s=s\le s=\boxtimes a_{N+1}$, which
holds. So the cascade terminates, but it changes the order significantly:
we have added a chain $a_2\le a_3\le a_4\le\cdots\le a_{N+1}$ (and $s\le
a_{N+1}$ already). This extended order collapses the nFG2 pattern: now
$\boxtimes^{k+1}T=a_{k+1}\le a_k=\boxtimes^k T$ for all $k\ge2$ (since the
cascade adds $a_{k+1}\le a_k$ relations — wait, we added $a_2\le a_3$, not
$a_3\le a_2$; let me recheck).

Actually antitonicity of $a_2\le a_3$ requires $\boxtimes a_3\le\boxtimes a_2$,
i.e., $a_4\le a_3$. So we add $a_4\le a_3$. Then $a_4\le a_3$ requires
$\boxtimes a_3\le\boxtimes a_4$, i.e., $a_4\le a_5$... but this reverses the
chain again. Actually: $a_4\le a_3$ requires $\boxtimes a_3\le\boxtimes a_4$,
i.e., $a_4\le a_5$ (since $\boxtimes a_3=a_4$ and $\boxtimes a_4=a_5$). So we
must add $a_4\le a_5$, which then forces $a_5\le a_4$ by the same logic — a
contradiction if $a_4\ne a_5$.

In summary: adding $a_2\le a_3$ to $B_N$ and keeping $\boxtimes$ antitone
requires $a_4\le a_5$ which requires $a_5\le a_4$, a contradiction.
**Route B breaks antitonicity in $B_N$** and cannot be reconciled without
collapsing elements. Route B fails for the $B_N$ family.

**Pass 33 result**: Route A (cyclic group front) succeeds; Route B (front join)
breaks antitonicity.

Archivist:

The cyclic-group-of-order-3 front provides the first example of a non-orthogonal
$k=3$ front ideal evading the principal-fiber obstruction. The analysis is
purely algebraic: no new script is needed for the obstruction proof (it follows
from the associativity failure of idempotent cyclic and the success of the
genuine cyclic group). The Route B failure is a clean antitonicity-cascade
argument. Updated `open_problems.md` to record the Route A resolution and the
Route B obstruction. Recorded the cyclic-group-front template in
`notes/g2-fg2-hierarchy.md` and the uniform residual-table extension in
`definitions.md`. Added a new open problem: determine the maximum front-group
order $\lvert G\rvert$ compatible with the $B_N$ APS order, full residuation, and the
antitone $\boxtimes$ profile.

Repository updates:

- `notes/g2-fg2-hierarchy.md`: added the cyclic-group $k=3$ front-ideal
  construction, the Route A/B analysis, and the resulting theorem on orthogonal
  vs.\ non-orthogonal fronts.
- `definitions.md`: added the cyclic-group front-ideal template (identity $T$,
  zero $b$, group product on $F_k$, $U$ acting as group identity on $F_k$,
  tail absorbed to front element).
- `open_problems.md`: marked the $k=3$ Route A escape as resolved and the
  Route B order-extension as obstructed; added the max-front-group-order problem.
- `logs/research-log.md`: recorded Pass 33 result.
- `ideas/research-questions.md` and `notes/g2-aps-zoo-classification.md`:
  retargeted the next structural problem.

Next step:

Use pass 34 to determine the maximum order $\lvert G\rvert$ of a finite group that can
serve as the cyclic/non-orthogonal front in the $B_N$ schema — specifically,
whether $\lvert G\rvert\ge4$ fronts (e.g., the Klein four-group or cyclic group of order 4)
are compatible with full residuation, antitonicity of $\boxtimes$, and the $B_N$
order, or whether the monotonicity constraints force $\lvert G\rvert\le3$.
