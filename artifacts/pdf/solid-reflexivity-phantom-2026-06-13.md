# Solid Reflexivity Of The Phantom

Date: 2026-06-13

## Summary

Pass 78 tests whether the all-prime phantom
$$
\epsilon=\widehat{\mathbb Z}/\mathbb Z
$$
is reflexive in the derived/solid target. The answer is positive, but the
reflexivity carries an antipode sign coming from the single odd shift of the
phantom.

## Main Claims

- **Single dual.** The dual of $\epsilon$ is represented by a degree-one
  extension object; finite shadows give
  $\mathrm{Hom}(\mathbb Z/N,\mathbb Z)=0$ and
  $\mathrm{Ext}^1(\mathbb Z/N,\mathbb Z)\cong\mathbb Z/N$.
- **Double dual.** The unit class $c=1$ gives an isomorphism at every checked
  finite stage, so $D^2(\epsilon)=\epsilon$. A pathological idempotent class
  creates a secondary phantom, showing that the unit-class hypothesis is doing
  real work.
- **Antipode sign.** The shadow has $D^2=+\mathrm{id}$, while the degree-one
  phantom shift contributes the Koszul sign $-1$.

## Machine Verification

`code/scripts/check-pass78.py` produced
`artifacts/reports/pass78-solid-reflexivity-phantom-check.json` with overall
PASS. It verifies the degree-one dual, double-dual recovery through the unit
class, the secondary-phantom control example, and the sign calculation.

## Next Use

Pass 78 supplies the distinction used later: $\epsilon$ is reflexive, but this
does not imply tensor dualizability or the existence of a Fourier/Weyl flip.
