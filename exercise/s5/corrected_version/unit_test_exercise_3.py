"""
EXERCISE 3 — Validate a Monte Carlo pricer against Black–Scholes

Task:

2) Write tests that:
   - For (S=100,K=100,r=0.05,σ=0.15,T=1year / 252 days) ≈ 8.59 for call and 3.71 for put
   - Check MC estimate is close to values above (0.1 error margin)
   - Check MC estimate vs Black-Scholes is roughly equals (0.1 error margin)

use the class previously implemented for BS and MC option pricing

"""
import unittest

from exercise.s1.s_1_bs_option import Call, Put
from exercise.s4.corrected_version.s_4_monte_carlo_option_pricing_with_decorators_corrected import european_put_payoff, european_call_payoff

class TestOptionPricing(unittest.TestCase):
    def setUp(self):
        self.call_pricer_mc = european_call_payoff(strike=100)(S0=100, r=0.05, sigma=0.15, T=1)
        self.put_pricer_mc = european_put_payoff(strike=100)(S0=100, r=0.05, sigma=0.15, T=1)

        self.call_bs = Call(s=100, k=100, r=0.05, ttm=1.0, sigma=0.15)
        self.put_bs = Put(s=100, k=100, r=0.05, ttm=1.0, sigma=0.15)

    def test_call_pricing(self):
        self.assertTrue(abs(self.call_pricer_mc.price_option(num_simulations=250000, num_steps=252) - 8.59) < 0.1)

    def test_put_pricing(self):
        self.assertTrue(abs(self.put_pricer_mc.price_option(num_simulations=250000, num_steps=252) - 3.72) < 0.1)

    def test_bs_mc_equality_put(self):
        self.assertAlmostEqual(self.put_pricer_mc.price_option(num_simulations=250000, num_steps=252),
                               self.put_bs.price(), places=1)

    def test_bs_mc_equality_call(self):
        self.assertAlmostEqual(self.call_pricer_mc.price_option(num_simulations=250000, num_steps=252),
                               self.call_bs.price(), places=1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
