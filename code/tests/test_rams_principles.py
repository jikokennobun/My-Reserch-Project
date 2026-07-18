import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "code" / "scripts" / "check-rams-principles.py"
SPEC = importlib.util.spec_from_file_location("check_rams_principles", PATH)
checker = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(checker)


class RamsPrincipleTests(unittest.TestCase):
    def test_identity_on_three_element_godel_chain(self):
        truth = checker.evaluate((0, 1, 2), "godel")
        self.assertTrue(truth["normality"])
        self.assertTrue(truth["M"])
        self.assertTrue(truth["T"])
        self.assertTrue(truth["CP"])
        self.assertFalse(truth["Lob"])

    def test_cp_implies_four_in_small_census(self):
        report = checker.census(3)
        self.assertTrue(report["implications"]["CP=>4"]["holds_in_census"])

    def test_con_l_sem_implies_con_eg_elem_in_small_census(self):
        report = checker.census(3)
        self.assertTrue(report["implications"]["Con_L_sem=>Con_EG_elem"]["holds_in_census"])

    def test_m_and_c_imply_k(self):
        for family in ("godel", "lukasiewicz"):
            for box in __import__("itertools").product(range(3), repeat=3):
                truth = checker.evaluate(box, family)
                self.assertFalse(truth["M"] and truth["C"] and not truth["K"])

    def test_conditional_claims_have_supporting_models(self):
        report = checker.census(3)
        for claim in report["conditional_claims"].values():
            self.assertTrue(claim["holds_in_census"])
            self.assertGreater(claim["supporting_models"], 0)

    def test_report_records_unambiguous_scope_and_definitions(self):
        report = checker.census(3)
        self.assertEqual(report["scope"]["sizes"], [2, 3])
        self.assertIn("SC_elem", report["definitions"])
        self.assertIn("script_sha256", report["reproducibility"])


if __name__ == "__main__":
    unittest.main()
