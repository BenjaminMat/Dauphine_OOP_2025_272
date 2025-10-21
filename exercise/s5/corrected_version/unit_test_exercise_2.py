import unittest
import numpy as np


def log_returns(prices):
    """
        - Validate there are a minimum of 2 items and each items in the list are numbers.
        - If any entry is <= 0 (and not NaN), raise ValueError.
        - Create an output array of length len(prices)-1 filled with NaN.
        - Compute log(prices[i+1]/prices[i]) only where both prices are not NaN.
        - Return the new list
        """
    arr = np.asarray(prices, dtype=float)
    if len(prices) < 2:
        raise ValueError("prices must contain at least two elements")

    if len([price for price in prices if price <= 0. and price is not np.NaN]):
        raise ValueError("All non-NaN prices must be strictly positive")

    out = np.full(arr.size - 1, np.nan, dtype=float)
    for i in range(arr.size - 1):
        if (not np.isnan(arr[i])) and (not np.isnan(arr[i + 1])):
            out[i] = np.log(arr[i + 1] / arr[i])

    return out


class TestLogReturn(unittest.TestCase):
    def test_valid_case(self):
        prices = np.array([100.0, 110.0, 121.0])
        expected = np.array([np.log(110.0/100.0), np.log(121.0/110.0)])
        result = log_returns(prices)
        np.testing.assert_allclose(result, expected, rtol=1e-12, atol=0.0)

    def test_nan_case(self):
        prices = np.array([100.0, np.nan, 105.0])
        result = log_returns(prices)
        # Both positions involve at least one NaN, so both returns are NaN
        self.assertEqual(result.shape, (2,))
        self.assertTrue(np.all(np.isnan(result)))

    def test_negative_case(self):
        prices = np.array([100.0, -5.0, 105.0])
        with self.assertRaises(ValueError):
            _ = log_returns(prices)

    def test_zero_case(self):
        # Optional extra: zero should also raise
        prices = np.array([100.0, 0.0, 105.0])
        with self.assertRaises(ValueError):
            _ = log_returns(prices)

    def test_min_length(self):
        with self.assertRaises(ValueError):
            _ = log_returns([100.0])  # fewer than 2 prices


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False, verbosity=2)
