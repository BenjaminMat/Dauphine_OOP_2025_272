"""
TP: Monte Carlo Option Pricing with Decorators
In this practical exercise, we’ll create a Monte Carlo simulator for option pricing and use decorators to inject
different payoff functions into the simulator. This approach will allow us to easily create and price various types
of options using the same underlying simulation framework.

Scenario: Flexible Option Pricing System
We want to build a system that can price different types of options using Monte Carlo simulation. The system should be
flexible enough to handle various payoff structures without modifying the core simulation logic.

First, let’s implement our base MonteCarloSimulator class:
"""

import numpy as np


class MonteCarloSimulator:
    def __init__(self, S0, r, sigma, T):
        self.S0 = S0  # Initial stock price
        self.r = r  # Risk-free rate
        self.sigma = sigma  # Volatility
        self.T = T  # Time to maturity

    def simulate_paths(self, num_simulations, num_steps):
        dt = self.T / num_steps
        paths = np.zeros((num_simulations, num_steps + 1))
        paths[:, 0] = self.S0

        for i in range(1, num_steps + 1):
            z = np.random.standard_normal(num_simulations)
            paths[:, i] = paths[:, i - 1] * np.exp((self.r - 0.5 * self.sigma ** 2) * dt +
                                                   self.sigma * np.sqrt(dt) * z)
        return paths

    def price_option(self, num_simulations, num_steps):
        paths = self.simulate_paths(num_simulations, num_steps)
        payoffs = self.payoff(paths[:, -1])
        option_price = np.exp(-self.r * self.T) * np.mean(payoffs)
        return option_price

    def payoff(self, price):
        raise NotImplementedError("Subclasses must implement payoff method")


"""
TO DO: Implement the Decorator
Now, implement a decorator called option_pricer. This decorator should:
    Take a payoff function as input
    Create a new class OptionPricer that inherits from MonteCarloSimulator
    Inject the input function as the payoff method of the new class
    Return a func which return the new class
"""

"""
Once you’ve implemented the decorator, you should be able to use it like this:
"""

@option_pricer
def european_call_payoff(current_spot_price, strike=100):
    return np.maximum(current_spot_price - strike, 0)

@option_pricer
def european_put_payoff(current_spot_price, strike=100):
    return np.maximum(strike - current_spot_price, 0)

# Usage
if __name__ == "__main__":
    call_pricer = european_call_payoff(strike=100)(S0=100, r=0.05, sigma=0.2, T=1)
    call_price = call_pricer.price_option(num_simulations=100000, num_steps=252)
    print(f"European Call Option Price: {call_price:.4f}")

    put_pricer = european_put_payoff(strike=100)(S0=100, r=0.05, sigma=0.2, T=1)
    put_price = put_pricer.price_option(num_simulations=100000, num_steps=252)
    print(f"European Put Option Price: {put_price:.4f}")

