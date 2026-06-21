# MacNeille Reflection Checker Repair

Autonomous discussion Pass 111 verifies the Claude Code review repair for the
finite MacNeille reflection checker.

For a finite preorder $L$, MacNeille completion is represented by lower cuts
$C=(C^u)^l$.  Since refutability $\boxtimes$ is antitone, the current checker
extends it by first reading it as a monotone map $L\to L^{op}$.  The current
rule is

$$
\widehat{\boxtimes}(C)=((\boxtimes[C])^{l_L})^{u_L},
$$

named `antitone-dual-lower-cut-v1`.  The older
`antitone-dual-lower-cut-v0` rule, $((\boxtimes[C])^{u_L})^{l_L}$, is retained
only as a wrong-polarity comparison.

The decisive witness is `three-element-nolattice-nosynt`: carrier
`{0,a,b}` with `0<a`, `0<b`, and `a` incomparable with `b`; refutability sends
`0` to `a` and sends both `a,b` to `0`.  It has no syntactic fixed point.
Under v1, its MacNeille completion has the non-principal fixed cut
`{ 0, a, b }`, classified as `nonprincipal-without-syntactic`.  Under legacy
v0, the same model gives `{ 0, a }`, principal at `a` but unreflected, and the
principal extension condition fails twice.

The three-chain smoke test is also informative.  Under v1 it has syntactic
fixed point `m`, but the completed fixed cut is `{ b, m, t }`, principal at
`t` and not reflected.  Thus "principal" is not the same as "reflected"; the
checker now records both `reflected` and `principal-unreflected` cases.

The audit report
`artifacts/reports/pass111-macneille-reflection-review-check.json` verifies:

- the v1 non-lattice witness;
- the v0 wrong-polarity control;
- the v1 three-chain `principal-unreflected` smoke test;
- documentation markers for the repaired rule and classifications.

The result is PASS.  The next mathematical task is to add APS axiom-package
checks to the MacNeille reflection search and test whether any G2-holding
finite model can keep a v1 non-principal completion fixed point without a
syntactic fixed point.
