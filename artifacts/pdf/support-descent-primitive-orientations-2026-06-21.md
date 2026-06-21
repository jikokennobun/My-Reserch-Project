# Support Descent for All-Prime Primitive Orientations

Autonomous discussion Pass 105 isolates the support-descent statement for the
all-prime primitive-orientation package.

For finite support $S$, the primitive orientations are
$$
\mathcal O_S=
\{c=(c_p)_{p\in S}\in\mathbb Z^S:
\sum_{p\in S}c_p=0,\ \gcd(c_p)=1\}.
$$
If $S\subseteq T$, the canonical orientation map is zero-extension
$$
e_{S,T}:\mathcal O_S\to\mathcal O_T.
$$
It preserves zero-sum, primitivity, and the antipode, and it composes
strictly along support chains.

The boundary support map has the opposite variance:
$$
T_T\to T_S.
$$
There is no total restriction map on primitive orientations
$\mathcal O_T\to\mathcal O_S$.  Deleting coordinates can destroy zero-sum:
$$
(1,1,-2)\in\mathcal O_{\{2,3,5\}}
$$
restricts to $(1,1)$ on $\{2,3\}$, whose sum is $2$.

Therefore the all-prime primitive-orientation object is a filtered colimit by
zero-padding.  It may be represented as primitive finitely supported
zero-sum integer functionals on the set of all primes, modulo padded zero
coordinates.

The antipode quotient gives primitive lines $[c]=\{c,-c\}$, but the sign
must still be retained as the $B\mathbb Z/2$ local system on the
boundary/Yoneda line from Pass 104.  The correct categorical package is
therefore a span-stack or Grothendieck presentation combining:

- zero-extension on orientation torsors;
- support projection on boundary groups;
- the $B\mathbb Z/2$ boundary-line local system.

It is not a plain sheaf of primitive orientations on finite supports with
restriction maps, and it does not create a degree-$0$ Weyl/Fourier morphism
$\epsilon\to\mathbb Q$.

The checker
`artifacts/reports/pass105-support-descent-primitive-orientations-check.json`
verifies zero-extension preservation and functoriality, explicit restriction
failure, colimit padding equivalence, nonexistence of support-symmetric
primitive orientations, and the span-stack verdict.

The next task is to compute the obstruction to stackifying primitive
orientations over finite supports when restriction maps are demanded, then
state the universal property of the span-stack/left-Kan colimit package.
