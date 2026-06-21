#!/usr/bin/env python3
"""Finite checks for Pass 110: conductor-cleared primitive transitions.

Pass 109 showed that the rational barycentric support transition tau_{S,T}
has exact denominator L_{S,T}=lcm(|S|, |T|).  The minimally cleared vector

    eta_{S,T} = L_{S,T} tau_{S,T}

is primitive and zero-sum.  This checker verifies the chain law for these
primitive clearings: on S subset T subset U, primitive labels do not usually
compose strictly.  They compose after rescaling by a common conductor C:

    (C/L_ST) eta_ST + (C/L_TU) eta_TU = (C/L_SU) eta_SU.

Thus the useful oriented-support edge datum is the pair (L_ST, eta_ST), or
equivalently the rational transition tau_ST, not the primitive line alone.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from math import gcd, lcm
from pathlib import Path


EDGES = [(2, 3), (2, 4), (3, 5), (4, 6), (5, 8), (6, 10), (8, 12)]
CHAINS = [(2, 3, 5), (2, 3, 6), (2, 4, 8), (3, 6, 10), (4, 6, 9), (4, 6, 12), (5, 8, 10)]


@dataclass
class EdgeRow:
    source_size: int
    target_size: int
    edge_conductor: int
    gcd_size: int
    eta_vector: tuple[int, ...]
    eta_sum: int
    eta_zero_sum: bool
    eta_gcd: int
    eta_primitive: bool
    support_values: tuple[int, int]


@dataclass
class ChainRow:
    source_size: int
    middle_size: int
    target_size: int
    conductor_source_middle: int
    conductor_middle_target: int
    conductor_source_target: int
    common_conductor: int
    coefficient_source_middle: int
    coefficient_middle_target: int
    coefficient_source_target: int
    rescaled_identity_ok: bool
    strict_primitive_identity_ok: bool
    strict_identity_expected: bool
    strict_identity_classification_ok: bool
    endpoint_multiplier: int
    common_cleared_endpoint_primitive: bool
    primitive_line_alone_sufficient: bool


@dataclass
class RepairComparisonRow:
    chain: tuple[int, int, int]
    additive_kernel_closed_after_rescaling: bool
    primitive_locus_closed_under_rescaled_sum: bool
    relation_to_repair_torsor: str


@dataclass
class VerdictRow:
    edge_datum: str
    chain_law: str
    primitive_warning: str
    claude_review_status: str
    next_task: str


def integer_gcd(values: tuple[int, ...]) -> int:
    current = 0
    for value in values:
        current = gcd(current, abs(value))
    return current


def eta(n: int, m: int) -> tuple[int, ...]:
    g = gcd(n, m)
    on_source = (m - n) // g
    off_source = -n // g
    return tuple(on_source for _ in range(n)) + tuple(
        off_source for _ in range(m - n)
    )


def extend(values: tuple[int, ...], length: int) -> tuple[int, ...]:
    return values + tuple(0 for _ in range(length - len(values)))


def add_scaled(
    left: tuple[int, ...],
    left_scale: int,
    right: tuple[int, ...],
    right_scale: int,
) -> tuple[int, ...]:
    return tuple(
        left_scale * a + right_scale * b
        for a, b in zip(left, right, strict=True)
    )


def edge_rows() -> list[EdgeRow]:
    rows: list[EdgeRow] = []
    for n, m in EDGES:
        g = gcd(n, m)
        vector = eta(n, m)
        rows.append(
            EdgeRow(
                source_size=n,
                target_size=m,
                edge_conductor=lcm(n, m),
                gcd_size=g,
                eta_vector=vector,
                eta_sum=sum(vector),
                eta_zero_sum=sum(vector) == 0,
                eta_gcd=integer_gcd(vector),
                eta_primitive=integer_gcd(vector) == 1,
                support_values=((m - n) // g, -n // g),
            )
        )
    return rows


def chain_rows() -> list[ChainRow]:
    rows: list[ChainRow] = []
    for n, mid, m in CHAINS:
        l_nm = lcm(n, mid)
        l_mid_m = lcm(mid, m)
        l_n_m = lcm(n, m)
        common = lcm(l_nm, l_mid_m, l_n_m)
        c_nm = common // l_nm
        c_mid_m = common // l_mid_m
        c_n_m = common // l_n_m

        eta_nm = extend(eta(n, mid), m)
        eta_mid_m = eta(mid, m)
        eta_n_m = eta(n, m)
        left_rescaled = add_scaled(eta_nm, c_nm, eta_mid_m, c_mid_m)
        right_rescaled = tuple(c_n_m * x for x in eta_n_m)
        left_strict = add_scaled(eta_nm, 1, eta_mid_m, 1)
        strict_ok = left_strict == eta_n_m
        strict_expected = l_nm == l_mid_m == l_n_m

        rows.append(
            ChainRow(
                source_size=n,
                middle_size=mid,
                target_size=m,
                conductor_source_middle=l_nm,
                conductor_middle_target=l_mid_m,
                conductor_source_target=l_n_m,
                common_conductor=common,
                coefficient_source_middle=c_nm,
                coefficient_middle_target=c_mid_m,
                coefficient_source_target=c_n_m,
                rescaled_identity_ok=left_rescaled == right_rescaled,
                strict_primitive_identity_ok=strict_ok,
                strict_identity_expected=strict_expected,
                strict_identity_classification_ok=strict_ok == strict_expected,
                endpoint_multiplier=c_n_m,
                common_cleared_endpoint_primitive=integer_gcd(right_rescaled) == 1,
                primitive_line_alone_sufficient=(
                    strict_ok and c_nm == c_mid_m == c_n_m == 1
                ),
            )
        )
    return rows


def repair_comparison_rows() -> list[RepairComparisonRow]:
    rows: list[RepairComparisonRow] = []
    for row in chain_rows():
        rows.append(
            RepairComparisonRow(
                chain=(row.source_size, row.middle_size, row.target_size),
                additive_kernel_closed_after_rescaling=row.rescaled_identity_ok,
                primitive_locus_closed_under_rescaled_sum=(
                    row.rescaled_identity_ok
                    and row.common_cleared_endpoint_primitive
                ),
                relation_to_repair_torsor=(
                    "The rescaled sum lies in the additive kernel K_U, but it "
                    "is primitive only when the endpoint coefficient is one; "
                    "this matches the Pass-107 warning that primitive repair "
                    "loci are arithmetic refinements of additive torsors."
                ),
            )
        )
    return rows


def verdict_row() -> VerdictRow:
    return VerdictRow(
        edge_datum=(
            "A primitive support edge should be recorded as (L_ST, eta_ST), "
            "or equivalently as tau_ST=eta_ST/L_ST."
        ),
        chain_law=(
            "For S<T<U, a common conductor C gives "
            "(C/L_ST)eta_ST + (C/L_TU)eta_TU = (C/L_SU)eta_SU."
        ),
        primitive_warning=(
            "The primitive vector or primitive line alone is not generally "
            "functorial; common-conductor sums may be nonprimitive multiples "
            "of the endpoint edge."
        ),
        claude_review_status=(
            "The MacNeille reflection review remains valid and should be "
            "incorporated next; it was not mixed into this support-chain pass."
        ),
        next_task=(
            "Incorporate the Claude Code MacNeille reflection checker review: "
            "add the non-lattice witness, fix the dual closure rule, and "
            "record reflected/principal-unreflected classifications."
        ),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="artifacts/reports/pass110-primitive-transition-chain-law-check.json",
    )
    args = parser.parse_args()

    edges = edge_rows()
    chains = chain_rows()
    repair_comparisons = repair_comparison_rows()
    verdict = verdict_row()

    checks = {
        "edge_primitivity_ok": all(
            row.eta_zero_sum and row.eta_primitive and row.eta_gcd == 1
            for row in edges
        ),
        "rescaled_chain_law_ok": all(row.rescaled_identity_ok for row in chains),
        "strict_identity_classification_ok": all(
            row.strict_identity_classification_ok for row in chains
        ),
        "primitive_line_not_sufficient_in_general_ok": any(
            not row.primitive_line_alone_sufficient for row in chains
        )
        and any(row.primitive_line_alone_sufficient for row in chains),
        "repair_torsor_comparison_ok": all(
            row.additive_kernel_closed_after_rescaling
            for row in repair_comparisons
        )
        and any(
            not row.primitive_locus_closed_under_rescaled_sum
            for row in repair_comparisons
        ),
    }

    report = {
        "pass": 110,
        "title": "Primitive conductor-cleared transition vectors along support chains",
        "A_edge_vectors": {
            "statement": (
                "The minimally conductor-cleared transition eta_ST is always "
                "a primitive integral zero-sum vector."
            ),
            "rows": [asdict(row) for row in edges],
        },
        "B_chain_law": {
            "statement": (
                "Primitive edge labels compose after rescaling by a common "
                "conductor; strict primitive composition occurs exactly when "
                "all three edge conductors agree."
            ),
            "rows": [asdict(row) for row in chains],
        },
        "C_repair_torsor_comparison": {
            "statement": (
                "The rescaled law stays in the additive kernel, while "
                "primitivity can be lost by endpoint multiplication."
            ),
            "rows": [asdict(row) for row in repair_comparisons],
        },
        "D_verdict": {
            "statement": (
                "The support-chain datum is weighted oriented edge data, not "
                "a strict primitive-line cocycle."
            ),
            "row": asdict(verdict),
        },
        "checks": checks,
        "overall": "PASS" if all(checks.values()) else "FAIL",
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"wrote {output_path}")
    print(f"overall {report['overall']}")


if __name__ == "__main__":
    main()
