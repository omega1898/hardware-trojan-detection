import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from trojan_detect.compare import diff_netlists, is_suspicious

BASELINE = {"gates": {"g1": "AND", "g2": "OR"}, "wires": [("g1", "g2")]}
TROJANED = {
    "gates": {"g1": "AND", "g2": "OR", "t1": "XOR"},
    "wires": [("g1", "t1"), ("t1", "g2")],
}


class DiffNetlistsTest(unittest.TestCase):
    def test_inserted_gate_is_flagged(self):
        difference = diff_netlists(BASELINE, TROJANED)
        self.assertEqual(difference["extra_gates"], [("t1", "XOR")])
        self.assertIn(("g1", "g2"), difference["missing_wires"])
        self.assertTrue(is_suspicious(difference))

    def test_identical_netlists_are_clean(self):
        self.assertFalse(is_suspicious(diff_netlists(BASELINE, BASELINE)))


if __name__ == "__main__":
    unittest.main()
