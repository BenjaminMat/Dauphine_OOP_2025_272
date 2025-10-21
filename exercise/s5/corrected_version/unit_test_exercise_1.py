"""
EXERCISE 1 — From print-checks to unit tests

Task:
1) Run this script once as-is and look at the printed output.
2) Create a test class `TestCompoundInterest` that converts the ad-hoc print
   checks into proper unit tests using Python's `unittest`.
3) Add a couple of case tests (zero periods, zero rate, negative period). make negative periods raise ValueError
    and test for it.
    What to verify:
    - Nominal case 1000 @ 5% for 2 periods -> 1102.5
    - Zero periods returns the principal
    - Zero rate leaves amount unchanged
    - Input validation raises ValueError for negative principal/periods and non-integer periods

4) Add the possibility to run all test in the class when running the script.
    To do so create a function run_tests() and call it under the __name__ == "__main__"
"""
import unittest

def compound_amount(principal, rate, periods):
    """
    Discrete compounding.
    principal: float >= 0
    rate: per-period rate as decimal (e.g., 0.05 for 5%)
    periods: non-negative integer
    """
    if principal < 0:
        raise ValueError("principal must be >= 0")
    if periods < 0 or int(periods) != periods:
        raise ValueError("periods must be a non-negative integer")
    return principal * (1 + rate) ** periods


class TestCompoundInterest(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(compound_amount(1000, 0.05, 2), 1102.5)

    def test_zero_period(self):
        self.assertEqual(compound_amount(1000, 0.05, 0), 1000)

    def test_zero_rate(self):
        self.assertEqual(compound_amount(1000, 0.0, 2), 1000)

    def test_negative_period(self):
        self.assertRaises(ValueError, compound_amount, 1000, 0, -2)

    def test_negative_principal(self):
        self.assertRaises(ValueError, compound_amount, -1000, 0, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
