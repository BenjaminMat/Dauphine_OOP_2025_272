"""
Exercise: Performance Measurement and Memoization with Decorators

Part 1: Create a decorator named @timing_decorator that measures the execution time of a function and prints the elapsed
time when the function completes.

Steps:
Define a decorator timing_decorator that:
    Accepts a function as input.
    Uses time from the time module to measure the execution time.
    Prints out the function’s name and how long it took to execute.
    Apply this decorator to a function that calculates the Black-Scholes option price for European options.

Hint:
For timing the execution of your code use the time package. To start and end the timer you can use the
following line :
start_time = time.time()
end_time = time.time()
The execution time is the difference between the two.
"""
import io
import math
import time
import unittest
from contextlib import redirect_stdout


from scipy.stats import norm

#TODO: implement the decorator here:


"""
Part 2: Creating the validate_inputs Decorator

Define a decorator validate_inputs that:
    Checks if the inputs to a function are valid.
    For any invalid input, raises a ValueError.
    The decorator should specifically check for the following conditions:
        Prices must be positive.
        Time to maturity (T) must be greater than 0.
        Volatility must be a positive.
        Apply this decorator to relevant method to ensure inputs are valid before the calculation proceeds.
"""


"""
Create a decorator named @MemoizationDecorator to cache the results of functions for given inputs to avoid redundant 
calculations.

Steps:
Define a decorator memoization_decorator that:
    Caches the function’s results using a dictionary where the name of the function arguments are the keys
    If the function has already been called with a particular set of arguments, the decorator should return 
    the cached result instead of recalculating it.
    Apply this decorator to the option classes when you think it make sense to do it.

Create test cases where the function is called multiple times with the same and different arguments. 
Observe the time taken with and without memoization using your timing_decorator from Part 1.
"""

#TODO: implement the decorator here:


class Option:
    def __init__(self, s: float, k: float, r: float, t: float, vol: float):
        self.spot = s
        self.strike = k
        self.r = r
        self.ttm = t
        self.vol = vol

    @MemoizationDecorator()
    def d1(self):
        return (math.log(self.spot / self.strike) + (self.r + 0.5 * self.vol**2) * self.ttm) / self.vol * math.sqrt(self.ttm)

    @MemoizationDecorator()
    def d2(self):
        return self.d1() - self.vol * math.sqrt(self.ttm)

    def vega(self):
        return self.spot * norm.pdf(self.d1()) * math.sqrt(self.ttm)


class Call(Option):
    @timing_decorator
    def price(self):
        d1, d2 = self.d1(), self.d2()
        return self.spot * norm.cdf(d1) - self.strike * math.exp(-self.r * self.ttm) * norm.cdf(d2)

    def delta(self):
        return norm.cdf(self.d1())

    def rho(self):
        return self.ttm * self.strike* math.exp(-self.r * self.ttm) * norm.cdf(self.d2())

    def theta(self):
        d1, d2 = self.d1(), self.d2()
        return (-(self.spot * norm.pdf(d1) * self.vol) / (2 * math.sqrt(self.ttm))
                -self.r * self.strike * math.exp(-self.r * self.ttm) * norm.cdf(d2))

    def theta_per_day(self):
        return self.theta() / 365.0


class Put(Option):
    @timing_decorator
    def price(self):
        d1, d2 = self.d1(), self.d2()
        return self.strike * math.exp(-self.r * self.ttm) * norm.cdf(-d2) - self.spot * norm.cdf(-d1)

    def delta(self):
        return norm.cdf(self.d1()) - 1.0

    def rho(self):
        return -self.ttm * self.strike * math.exp(-self.r * self.ttm) * norm.cdf(-self.d2())

    def rho_per_1pct(self):
        return 0.01 * self.rho()

    def theta(self):
        d1, d2 = self.d1(), self.d2()
        return (-(self.spot * norm.pdf(d1) * self.vol) / (2 * math.sqrt(self.ttm)) + self.r * self.strike *
                math.exp(-self.r * self.ttm) * norm.cdf(-d2))

    def theta_per_day(self):
        return self.theta() / 365.0


class TestOptionPricing(unittest.TestCase):
    def setUp(self):
        self.spot = 200.0
        self.strike = 250.0
        self.r = 0.05
        self.ttm = 1.0
        self.vol = 0.15
        self.call = Call(self.spot, self.strike, self.r, self.ttm, self.vol)
        self.call_wrong_input = Call(-self.spot, self.strike, self.r, self.ttm, self.vol)
        self.put = Put(self.spot, self.strike, self.r, self.ttm, self.vol)

    def test_timing_decorator_prints_and_returns_price(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            price = self.call.price()
        msg = buf.getvalue()
        self.assertIsInstance(price, float)
        self.assertIn("execution time for", msg)

    def test_memoization_caches_compute_d1(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            _ = self.call.d1()  # store
            _ = self.call.d1()  # cache hit
        out = buf.getvalue()
        self.assertIn("result stored for key:", out)
        self.assertIn("getting result stored in cache for key:", out)

    def test_memoization_caches_compute_d2(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            _ = self.call.d2()  # store
            _ = self.call.d2()  # cache hit
        out = buf.getvalue()
        self.assertIn("getting result stored in cache for key:", out)


    def test_put_call_parity_holds_approximately(self):
        """
        C - P ≈ S - K*e^{-rT}. We allow a small tolerance because of floating and cdf/pdf evaluations.
        """
        with redirect_stdout(io.StringIO()):
            c = self.call.price()
            p = self.put.price()
        lhs = c - p
        rhs = self.spot - self.strike * math.exp(-self.r * self.ttm)
        self.assertAlmostEqual(lhs, rhs, places=6)

    def test_validate_inputs_allows_good_values(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            price = self.call.price()

        msg = buf.getvalue()
        self.assertIsInstance(price, float)
        self.assertIn("validating inputs", msg)

    def test_validate_inputs_raises_for_negative_values(self):
        self.assertRaises(ValueError, self.call_wrong_input.price)


if __name__ == "__main__":
    unittest.main(verbosity=2)