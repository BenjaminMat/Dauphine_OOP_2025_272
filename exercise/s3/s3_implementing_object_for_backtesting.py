"""
TP Instructions: Implementing a Strategy and a Portfolio for a backtesting task

Objective:
You need to implement methods and functionalities for a Portfolio class. The class should handle the operations
of initializing the portfolio with financial instrument, rebalancing its positions based on a given strategy,
and providing a summary of the portfolio positions.

Tips:
    - Use the methods and attributes of other provided classes like Instrument, Quote, and Position in the resource
    folder.
    - Before starting the exercise be sure to fully understand how the object provided for it worked.
    - Remember to handle cases where certain attributes might be None or missing.
    - If you finish the exercise early, you can implement method to populate the attribute of the Portfolio class
    that are not handle yet.
"""

import pandas as pd
from datetime import datetime
import math

from exercise.s3.resource.instrument import Instrument
from exercise.s3.resource.quote import Quote
from exercise.s3.resource.position import Position


"""
PART I: Creating the meta class strategy and one specific strategy:
Create an abstract class Strategy that will serve as the base for all strategies. 

This class should:
    Include an abstract method generate_signals that will generate trading signals based on input data.
    Document the method generate_signals with a docstring explaining the parameters and return value (see below):
        Parameters for the class : A dictionary with tickers as keys and positions as values. The dict should be named 
                                   data_for_signal_generation
        Return: A dictionary with tickers as keys and signals as values.

Create a derived class EqualWeightStrategy from Strategy:
    This class should inherit from Strategy and implement the generate_signals method.
    It should calculate and return a dictionary with equal-weight signals for each ticker.

To Implement the generate_signals method:
    The method should calculate equal-weight signals for each ticker by dividing 1 by the total number of tickers.
    The input of the method could be either a list or a dict of ticker. 
    It should return a dictionary where each ticker has an equal weight as its signal.
"""

# TODO: Implement here the Part I


"""
Part II : Creating the Portfolio class:

Class Attributes: Based on the provided code framework, create a Portfolio class which should have the following attributes:
                name: Name of the portfolio.
                currency: The currency in which the portfolio is denominated.
                aum: Assets Under Management.
                nav : The last net asset value computed for the portfolio
                historical_nav: A list that keeps track of the historical Net Asset Values.
                positions: A list of Position objects representing the portfolio’s assets.
                historical_positions : A dict date as key and and dict of positions for this date. 
                strategy: A strategy object, an instance of a class derived from the Strategy class.
                
                Initialization: Implement the __init__ method to initialize the portfolio attributes.

Initialize Portfolio Positions: 
Implement a initialize_position_from_instrument_list method to initialize the portfolio’s positions with a given 
list of Instrument objects. Each Instrument should be wrapped in a Position object.

Positions to Dictionary: 
Implement the _positions_to_dict method which returns a dictionary of positions with 
ticker symbols as keys and Position objects as values. This will help in rebalancing operations.

Rebalancing: Implement the rebalance_portfolio method which performs the following tasks:
    Convert the positions list into a dictionary.
    Generate trading signals using the provided strategy.
    Update the weight and quantity of each position in the portfolio based on the generated signals.
    Input : rebalancing_date.

Portfolio Summary: Implement the portfolio_position_summary method. This method should return a dataframe 
    summarizing the portfolio’s current positions, including the ticker symbols, weights, quantities, 
    and last close for the assets
"""

# TODO: Implement here the Part II



import unittest

class TestPortfolio(unittest.TestCase):
    def setUp(self):
        # Set up the instruments and quotes
        self.last_date_asset_1 = datetime(2025, 8, 29)
        self.last_close_asset_1 = 230.02
        self.equity_last_quote_asset_1 = Quote(self.last_date_asset_1, self.last_close_asset_1)
        self.equity_1 = Instrument('AAPL', 'NASDAQ', self.equity_last_quote_asset_1, 'USD')

        self.last_date_asset_2 = datetime(2025, 8, 29)
        self.last_close_asset_2 = 414.75
        self.equity_last_quote_asset_2 = Quote(self.last_date_asset_2, self.last_close_asset_2)
        self.equity_2 = Instrument('MSFT', 'NASDAQ', self.equity_last_quote_asset_2, 'USD')

        self.last_date_asset_3 = datetime(2025, 8, 29)
        self.last_close_asset_3 = 414.75
        self.equity_last_quote_asset_3 = Quote(self.last_date_asset_3, self.last_close_asset_3)
        self.equity_3 = Instrument('NVDA', 'NASDAQ', self.equity_last_quote_asset_2, 'USD')

        self.last_date_asset_4 = datetime(2025, 8, 29)
        self.last_close_asset_4 = 414.75
        self.equity_last_quote_asset_4 = Quote(self.last_date_asset_4, self.last_close_asset_4)
        self.equity_4 = Instrument('GOOGLE', 'NASDAQ', self.equity_last_quote_asset_2, 'USD')

        # Update prices
        self.last_date_asset_1 = datetime(2025, 8, 30)
        self.last_close_asset_1 = 229.0
        self.equity_1.update_price(Quote(self.last_date_asset_1, self.last_close_asset_1))

        self.last_date_asset_2 = datetime(2025, 8, 30)
        self.last_close_asset_2 = 417.14
        self.equity_2.update_price(Quote(self.last_date_asset_2, self.last_close_asset_2))

        self.last_date_asset_3 = datetime(2025, 8, 30)
        self.last_close_asset_3 = 417.14
        self.equity_3.update_price(Quote(self.last_date_asset_3, self.last_close_asset_3))

        self.last_date_asset_4 = datetime(2025, 8, 30)
        self.last_close_asset_4 = 417.14
        self.equity_4.update_price(Quote(self.last_date_asset_4, self.last_close_asset_4))

        # Set up the portfolio strategy and portfolio
        self.pft_strategy = EqualWeightStrategy()
        self.portfolio = Portfolio("Tech Portfolio", "USD", 1000000, 10000, self.pft_strategy)
        self.portfolio.initialize_position_from_instrument_list([self.equity_1, self.equity_2, self.equity_3,
                                                                 self.equity_4])

    def test_initial_portfolio_summary(self):
        # Test the initial summary of the portfolio
        summary = self.portfolio.portfolio_position_summary()
        expected_data = {
            "Ticker": ['AAPL', 'MSFT', 'NVDA', 'GOOGLE'],
            "Weight": [0., 0., 0., 0.],
            "Quantity": [0., 0., 0., 0.],
            "Last close": [229.0, 417.14, 417.14, 417.14]
        }

        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(summary, expected_df)

    def test_rebalance_portfolio(self):
        # Rebalance the portfolio and check the summary
        self.portfolio.rebalance_portfolio()
        summary = self.portfolio.portfolio_position_summary()

        # Calculate expected values
        total_aum = self.portfolio.aum
        expected_weight = 0.25
        expected_quantity_1 = math.floor((total_aum * expected_weight) / self.equity_1.last_quote.price)
        expected_quantity_2 = math.floor((total_aum * expected_weight) / self.equity_2.last_quote.price)
        expected_quantity_3 = math.floor((total_aum * expected_weight) / self.equity_3.last_quote.price)
        expected_quantity_4 = math.floor((total_aum * expected_weight) / self.equity_4.last_quote.price)

        expected_data = {
            "Ticker": ['AAPL', 'MSFT', 'NVDA', 'GOOGLE'],
            "Weight": [expected_weight, expected_weight, expected_weight, expected_weight],
            "Quantity": [expected_quantity_1, expected_quantity_2, expected_quantity_3, expected_quantity_4],
            "Last close": [229.0, 417.14, 417.14, 417.14]
        }
        expected_df = pd.DataFrame(expected_data)

        pd.testing.assert_frame_equal(summary, expected_df)

def run_tests():
    unittest.main(argv=[''], verbosity=2, exit=False)

if __name__ == '__main__':
    run_tests()
