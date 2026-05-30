# Literature Notes

This file is the controlled bibliography workspace for the APS/G2-ZOO project.
It is not only a reading list. Each entry should record what theorem, example,
or definition can be imported into the project, and which repository note would
change if the source is verified.

## Entry Standard

Use the following shape for each source:

```md
### Author/Title

- Location:
- Bibliographic status:
- Topic:
- Exact result needed:
- Repository use:
- Verification state:
- Open extraction tasks:
```

The `Exact result needed` line is mandatory. A source is not useful merely
because it is thematically close; it must support a specific definition,
theorem, counterexample, or citation gap.

## Source Classes

### APS and Abstract Incompleteness

These sources support the basic APS axiom package, abstract G2/FG2 principles,
and comparisons with derivability conditions.

Needed results:

$$
\mathrm{G2}(S):
\quad
\boxtimes T\le\bot\Rightarrow T\le\bot,
$$

and:

$$
\mathrm{FG2}(S):
\quad
\boxtimes\boxtimes T\le\boxtimes T.
$$

Extraction target: identify which assumptions are syntactic, which are
order-theoretic, and which are proof-theoretic.

### Provability Logic and Derivability Conditions

These sources support the interpretation of $\Box$ and the treatment of weak
provability predicates. They should be used to calibrate A1-A4, especially the
introspection-like condition:

$$
\boxtimes x\le\Box\boxtimes x.
$$

Extraction target: separate Hilbert-Bernays-Lob style conditions from
Rosser/Feferman/Shavrukov-style weakened predicates.

### Categorical Diagonalization

These sources support the fixed-point engine behind syntactic diagonalization.
They must distinguish:

$$
\Delta_X:X\to X\times X
$$

from quotation and self-substitution:

$$
\varphi\mapsto
\varphi(\ulcorner\mathrm{diag}(\varphi)\urcorner).
$$

Extraction target: a precise Lawvere/Smullyan theorem statement usable in
`smullyan-lawvere-categorical-diagonalization.md`.

### Domain Theory and Completion

These sources support MacNeille completion, Scott topology, compact reflection,
and fixed-point theorems for monotone or antitone operators.

Extraction target: conditions under which a semantic completion fixed point
reflects to a syntactic or compact fixed point.

### Residuated and Substructural Algebra

These sources support resource-sensitive APS, residuals, contraction/weakening
analysis, and finite algebraic expansions.

Extraction target: identify which residuated laws are needed for the current
finite APS witnesses and which structural rules they validate or refute.

## Current Entries

### Beklemishev-Shamkanov Abstract G2 Material

- Location: https://drive.google.com/file/d/1Pkj6ZxECucSputAXulzhpYWuXxNnEf_J
- Bibliographic status: Drive item found as
  `beklemishev_shamkanov_abstract_g2_beamer.pdf`; exact paper/proceedings
  citation still needs verification.
- Topic: abstract G2, contraction-free arithmetic/logics, BS16 background.
- Exact result needed: theorem-level assumptions under which abstract
  formalized G2 follows in a nonclassical or contraction-free setting.
- Repository use: verify the assumptions behind
  `bs16-fiber-residuated-aps.md`,
  `formalized-g2-implicational-aps.md`, and the residuated APS reconstruction.
- Verification state: partial. The existence and rough topic of the Drive file
  are recorded, but theorem numbers and hypotheses have not been extracted.
- Open extraction tasks:
  - identify the exact statement corresponding to BS16 in repository notes;
  - record whether contraction, weakening, necessitation, and Löb-like rules
    are assumed;
  - decide whether the result is about G2, FG2, local-FG2, or a stronger
    formalized reflection principle.

## Citation Gaps

The following repository claims should not be treated as publication-ready until
their literature anchors are filled.

| Claim family | Needed source | Current note |
|---|---|---|
| APS axiom stability under completion | canonical extension or MacNeille reference | `g2-aps-zoo-classification.md` |
| Lawvere theorem variant for syntax | categorical fixed-point theorem with quotation/substitution discussion | `smullyan-lawvere-categorical-diagonalization.md` |
| Weak provability predicates as weak APS | arithmetic reference for Feferman/Shavrukov/Rosser behavior | `provability-predicate-weak-aps.md` |
| Residuated formalized G2 | substructural arithmetic or residuated logic source | `bs16-fiber-residuated-aps.md` |
| Domain-theoretic fixed-point reflection | algebraic dcpo/compact reflection theorem | `predicate-topology-fixed-points.md` |

## Reading Workflow

1. Fetch or open the source from Drive.
2. Extract theorem statements with hypotheses exactly.
3. Add a short proof-use paragraph: which line in the APS argument the source
   supports.
4. Update the target research note with a citation-ready statement.
5. If the extraction changes an autonomous research result, publish the updated
   Markdown summary as PDF under `artifacts/pdf/`.
