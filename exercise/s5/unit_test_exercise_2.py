"""
EXERCISE 2 — Returns & Annualized Volatility

Goal:
Implement the function and then write the unit test TestLogReturn

TestLogReturn
    - test a valid case (for example : prices = np.array([100.0, 110.0, 121.0])
    - test a nan case (for example : prices = np.array([100.0, 110.0, 121.0])
    - test a negative case (for example : prices = np.array([100.0, 110.0, 121.0])

    You can check the output for each case by running the script after the implementation of the function
"""
import unittest

import numpy as np
from appscript.defaultterminology import elements


def log_returns(prices:[]):
    """
    TODO:
    - Validate there are a minimum of 2 items and each items in the list are numbers.
    - If any entry is <= 0 (and not NaN), raise ValueError.
    - Create an output array of length len(prices)-1 filled with NaN.
    - Compute log(prices[i+1]/prices[i]) only where both prices are not NaN.
    - Return the new list
    """
    raise NotImplementedError



if __name__ == "__main__":
    # QUICK CHECKS (not a substitute for unit tests)
    prices = np.array([100.0, 110.0, 121.0])
    prices_nan = np.array([100.0, np.nan, 105.0])
    prices_neg = np.array([100.0, -5.0, 105.0])

    try:
        r = log_returns(prices)
        print("log_returns([100,110,121]) ->", r)

        r_nan = log_returns(prices_nan)
        print("log_returns([100,nan,105]) ->", r_nan)

        r_neg = log_returns(prices_neg)
        print("log_returns([100,nan,105]) ->", r_neg)
    except NotImplementedError:
        print("Implement log_returns first.")