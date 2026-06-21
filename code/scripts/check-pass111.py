#!/usr/bin/env python3
"""Finite verification for Pass 111: MacNeille reflection checker repair.

This checker does not reimplement the MacNeille construction.  It audits the
reports produced by code/scripts/check-macneille-reflection.ps1 after the
Claude Code review repair:

* v1 is the current antitone L -> L^op extension convention.
* v0 is kept only as a wrong-polarity comparison.
* principal completion fixed points are split into reflected and
  principal-unreflected cases.
* the size-3 non-lattice witness has a non-principal completion fixed point
  and no syntactic fixed point under v1.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REPORTS = {
    "non_lattice_v1": Path(
        "artifacts/reports/macneille-reflection-three-element-nolattice-nosynt-v1.json"
    ),
    "non_lattice_v0": Path(
        "artifacts/reports/macneille-reflection-three-element-nolattice-nosynt-v0.json"
    ),
    "chain_v1": Path(
        "artifacts/reports/macneille-reflection-three-chain-antitone-v1.json"
    ),
}

DOC_MARKERS = {
    "code/models/macneille-checker-interface.md": [
        "antitone-dual-lower-cut-v1",
        "principal-unreflected",
        "reflected",
        "dual principal cut",
    ],
    "code/models/macneille-reflection-search.md": [
        "three-element-nolattice-nosynt",
        "nonprincipal-without-syntactic",
        "principal-unreflected",
        "G2-holding",
    ],
    "research/notes/completion-and-fixed-points.md": [
        "antitone-dual-lower-cut-v0",
        "antitone-dual-lower-cut-v1",
        "principal but unreflected",
        "G2-holding variants",
    ],
}


def read_json(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8-sig"))


def fixed_cut(report: dict, display: str) -> dict | None:
    for row in report.get("completedFixedPoints", []):
        if row.get("display") == display:
            return row
    return None


def all_doc_markers_present(root: Path) -> tuple[bool, list[dict]]:
    rows: list[dict] = []
    ok = True
    for relative, markers in DOC_MARKERS.items():
        path = root / relative
        text = path.read_text(encoding="utf-8-sig")
        missing = [marker for marker in markers if marker not in text]
        rows.append(
            {
                "path": relative,
                "requiredMarkers": markers,
                "missingMarkers": missing,
                "ok": not missing,
            }
        )
        ok = ok and not missing
    return ok, rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="artifacts/reports/pass111-macneille-reflection-review-check.json",
    )
    args = parser.parse_args()

    root = Path.cwd()
    reports = {name: read_json(root / path) for name, path in REPORTS.items()}

    non_lattice_v1 = reports["non_lattice_v1"]
    non_lattice_v1_cut = fixed_cut(non_lattice_v1, "{ 0, a, b }")
    v1_checks = {
        "uses_current_dual_rule": non_lattice_v1.get("extensionRule")
        == "antitone-dual-lower-cut-v1",
        "classification_is_nonprincipal_without_syntactic": non_lattice_v1.get(
            "classification"
        )
        == "nonprincipal-without-syntactic",
        "has_no_syntactic_fixed_points": non_lattice_v1.get(
            "syntacticFixedPoints"
        )
        == [],
        "has_expected_nonprincipal_fixed_cut": bool(non_lattice_v1_cut)
        and not non_lattice_v1_cut.get("principal")
        and not non_lattice_v1_cut.get("reflected"),
        "has_no_principal_extension_failures": non_lattice_v1.get(
            "extensionConditionFailures"
        )
        == [],
        "is_not_g2_or_fg2": non_lattice_v1.get("g2") is False
        and non_lattice_v1.get("fg2") is False,
    }

    non_lattice_v0 = reports["non_lattice_v0"]
    non_lattice_v0_cut = fixed_cut(non_lattice_v0, "{ 0, a }")
    v0_warnings = " ".join(non_lattice_v0.get("warnings", []))
    v0_checks = {
        "uses_legacy_wrong_polarity_rule": non_lattice_v0.get("extensionRule")
        == "antitone-dual-lower-cut-v0",
        "classification_records_principal_unreflected": non_lattice_v0.get(
            "classification"
        )
        == "principal-unreflected",
        "principal_cut_is_not_reflected": bool(non_lattice_v0_cut)
        and non_lattice_v0_cut.get("principal")
        and non_lattice_v0_cut.get("principalElement") == "a"
        and not non_lattice_v0_cut.get("reflected"),
        "principal_extension_condition_fails": len(
            non_lattice_v0.get("extensionConditionFailures", [])
        )
        == 2,
        "warning_mentions_wrong_polarity": "wrong polarity" in v0_warnings,
    }

    chain_v1 = reports["chain_v1"]
    chain_v1_cut = fixed_cut(chain_v1, "{ b, m, t }")
    chain_checks = {
        "classification_is_principal_unreflected": chain_v1.get(
            "classification"
        )
        == "principal-unreflected",
        "syntactic_fixed_point_m_remains_visible": chain_v1.get(
            "syntacticFixedPoints"
        )
        == ["m"],
        "completed_fixed_point_is_principal_t_but_not_reflected": bool(
            chain_v1_cut
        )
        and chain_v1_cut.get("principal")
        and chain_v1_cut.get("principalElement") == "t"
        and not chain_v1_cut.get("reflected"),
        "has_no_principal_extension_failures": chain_v1.get(
            "extensionConditionFailures"
        )
        == [],
    }

    doc_ok, doc_rows = all_doc_markers_present(root)

    checks = {
        "v1_non_lattice_current_rule_ok": all(v1_checks.values()),
        "v0_wrong_polarity_comparison_ok": all(v0_checks.values()),
        "chain_v1_principal_unreflected_ok": all(chain_checks.values()),
        "documentation_markers_ok": doc_ok,
    }

    report = {
        "pass": 111,
        "title": "MacNeille reflection checker review repair verification",
        "inputs": {name: str(path) for name, path in REPORTS.items()},
        "A_current_v1_non_lattice_witness": {
            "statement": (
                "Under the v1 antitone L -> L^op extension, the size-3 "
                "non-lattice witness has a non-principal completion fixed "
                "cut and no syntactic fixed point."
            ),
            "checks": v1_checks,
            "classification": non_lattice_v1.get("classification"),
            "completedFixedPoints": non_lattice_v1.get("completedFixedPoints"),
        },
        "B_legacy_v0_polarity_control": {
            "statement": (
                "The legacy v0 rule is retained only as a wrong-polarity "
                "control; on the same witness it returns a principal but "
                "unreflected cut and fails the principal extension condition."
            ),
            "checks": v0_checks,
            "classification": non_lattice_v0.get("classification"),
            "extensionConditionFailures": non_lattice_v0.get(
                "extensionConditionFailures"
            ),
        },
        "C_chain_smoke_test": {
            "statement": (
                "The old three-chain smoke test is no longer labelled merely "
                "principal-only: v1 separates the syntactic fixed point m "
                "from the unreflected principal completion cut at t."
            ),
            "checks": chain_checks,
            "classification": chain_v1.get("classification"),
            "completedFixedPoints": chain_v1.get("completedFixedPoints"),
        },
        "D_documentation_audit": {
            "statement": (
                "Checker interface, search note, and completion note contain "
                "the repaired rule names and classification vocabulary."
            ),
            "rows": doc_rows,
        },
        "E_next_problem": {
            "statement": (
                "The bare non-lattice reflection counterexample is verified, "
                "but it is neither G2 nor FG2; the next search should add APS "
                "axiom-package checks and look for G2-holding variants."
            )
        },
        "checks": checks,
        "overall": "PASS" if all(checks.values()) else "FAIL",
    }

    output_path = root / args.output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"wrote {output_path}")
    print(f"overall {report['overall']}")


if __name__ == "__main__":
    main()
