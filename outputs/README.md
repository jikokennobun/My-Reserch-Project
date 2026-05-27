# Outputs

Generated artifacts go here.

- `pdf/`: compiled papers, handouts, notes, and exported PDFs
- `claude-code/`: generated one-off handoff packets for Claude Code review
  passes.
- `macneille-reflection-three-chain-antitone.json`: first checker report for
  the 3-element MacNeille reflection smoke-test model under legacy v0.
- `macneille-reflection-three-chain-antitone-v1.json`: corrected v1 report for
  the chain smoke-test model, classified as `principal-unreflected`.
- `macneille-reflection-three-element-nolattice-nosynt-v1.json`: corrected v1
  report for the size-3 non-lattice separation model, classified as
  `nonprincipal-without-syntactic`.
- `g2-zoo-M4-G2FG2FP.json`: checker report for the 4-element non-degenerate
  G2+FG2+FP-synt witness with fixed point at the interior element `p`.
- `g2-zoo-nfg2-depth-3.json`: checker report for the arbitrary-depth nFG2
  witness example with pattern `FFFTTTTT`.
- `residuated-search-M4-G2FG2FP.json`: exhaustive negative search report showing
  that `M4-G2FG2FP` has no full residuated monoid expansion on its existing
  carrier/order.
- `residuated-order-search-M4-G2FG2FP.json`: same-carrier order-repair search
  report showing that adding `bot <= c` yields a full-residuated expansion.
- `g2-zoo-M4-G2FG2FP-order-plus-bot-c-residuated.json`: G2-ZOO checker report
  for the full-residuated order repair.
- `bottom-discipline-filter-g2-zoo.json`: finite report showing which G2-ZOO
  witnesses and the checked `nfg2-depth-3` example survive pure enforcement of
  `bottom <= x` for every carrier element; updated to include
  `bottom-nfg2-depth-3`, `bottom-nfg2-depth-4`, and the full-residuated
  bottom-disciplined expansions.
- `g2-zoo-bottom-nfg2-depth-3.json`: checker report for the
  bottom-disciplined arbitrary-depth nFG2 witness example with pattern
  `FFFTTTTT`.
- `residuated-top-absorbing-report-bottom-nfg2-depth-3.json`: constructive
  report verifying a top-absorbing full-residuated expansion of
  `bottom-nfg2-depth-3`.
- `g2-zoo-bottom-nfg2-depth-3-residuated.json`: checker report for the
  full-residuated same-order expansion of `bottom-nfg2-depth-3`.
- `residuated-u-absorbing-search-bottom-nfg2-depth-3.json`: complete
  constrained search report finding a less top-collapsing \(U\)-absorbing
  full-residuated expansion of `bottom-nfg2-depth-3`.
- `g2-zoo-bottom-nfg2-depth-3-u-absorbing-minU.json`: checker report for that
  less top-collapsing expansion.
- `g2-zoo-bottom-nfg2-depth-4.json`: checker report for the next checked
  bottom-disciplined arbitrary-depth nFG2 witness, with pattern `FFFFTTTT`.
- `residuated-truncated-u-absorbing-bottom-nfg2-depth-4.json`: constructive
  report verifying the truncated-exponent \(U\)-absorbing full-residuated
  expansion of `bottom-nfg2-depth-4`.
- `g2-zoo-bottom-nfg2-depth-4-truncated-u-absorbing.json`: checker report for
  that truncated-exponent same-order expansion.
- `truncated-u-forcing-bottom-nfg2-depth-3.json`: analyzer report showing that,
  once the truncated-exponent orbit table is fixed on `bottom-nfg2-depth-3`,
  monotonicity forces every \(U\)-product.
- `truncated-u-forcing-bottom-nfg2-depth-4.json`: the same forcing check for
  `bottom-nfg2-depth-4`.
- `residuated-non-u-absorbing-search-bottom-nfg2-depth-3.json`: first bounded
  search report for a same-order full-residuated `bottom-nfg2-depth-3` tensor
  that does not assume \(U\)-absorption and allows the orbit product table to
  vary; incomplete, no candidate found within 1000 nodes.
- `g2-zoo-bottom-G2FG2-noFP.json`: checker report for the bottom-disciplined
  G2+FG2 without FP-synt witness.
- `residuated-search-bottom-G2FG2-noFP.json`: unrestricted tensor search report
  recording that the five-element operation space is too large for the current
  exhaustive bound.
- `residuated-commutative-zero-search-bottom-G2FG2-noFP.json`: targeted
  commutative fixed-unit/fixed-zero search report finding full residuated
  tensors for `bottom-G2FG2-noFP`.
- `g2-zoo-bottom-G2FG2-noFP-residuated.json`: checker report for the
  full-residuated same-order expansion of `bottom-G2FG2-noFP`.
