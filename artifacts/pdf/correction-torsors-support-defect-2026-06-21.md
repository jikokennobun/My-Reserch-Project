# Correction Torsors for Support-Defect Repairs

Autonomous discussion Pass 107 models support-defect repairs as torsors and
separates ordinary choice data from Rosser/cosheaf phantom data.

For finite support $S$, define
$$
K_S=\ker\Sigma_S
=\{a\in\mathbb Z^S:\sum_{p\in S}a_p=0\}.
$$
If coordinate deletion gives $u=d|_S$ with additive defect
$\Delta=\Sigma_S(u)$, an additive repair is
$$
r=u-a,\qquad \Sigma_S(a)=\Delta.
$$
Any two additive repairs differ by an element of $K_S$, and adding an element
of $K_S$ to one repair gives another.  Thus additive repairs form a free
transitive $K_S$ torsor.

Primitive repairs are a refinement, not the whole torsor.  On support
$\{2,3\}$, the vector $(1,-1)$ is primitive, but adding the kernel element
$(1,-1)$ gives $(2,-2)$, which is zero-sum but nonprimitive.  Hence the
primitive repair locus is not stable under the full $K_S$ action.

A basepoint $b\in S$ gives a splitting
$$
s_b(n)=n e_b.
$$
Transitions between basepoints are
$$
\tau_{a,b}=s_b(1)-s_a(1)\in K_S,
$$
and satisfy the cocycle identity
$$
\tau_{a,b}+\tau_{b,c}=\tau_{a,c}.
$$
These transitions are coboundaries of chosen splittings.  Along support
inclusions, basepointed splittings are natural exactly when the basepoint is
preserved.

Therefore the support-defect repair data is ordinary finite-level choice
data, not a Rosser/cosheaf phantom.  The finite exact sequence
$$
0\to K_S\to\mathbb Z^S\xrightarrow{\Sigma_S}\mathbb Z\to0
$$
splits after choosing a basepoint, and no non-Mittag-Leffler inverse tower is
present.  Linear repairs commute with the antipode, so the $B\mathbb Z/2$
boundary-line local system is unaffected.

The checker
`artifacts/reports/pass107-correction-torsors-support-defect-check.json`
verifies the additive torsor property, primitive-locus non-stability,
basepoint transition coboundaries, inclusion naturality under preserved
basepoints, antipode compatibility, and the ordinary-choice-not-phantom
verdict.

The next task is to classify the integral equivariant obstruction: rational
support-symmetric sections of $\Sigma_S$ exist by barycenters, but integral
support-symmetric sections do not.
