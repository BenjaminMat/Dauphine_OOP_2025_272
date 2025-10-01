"""
Table of contents :
    ## Utility classes
    ## Static Methods
    ## Data class
    ## Decorators
    ## Built-in Decorator
    ## Class-based Decorator



"""
from datetime import datetime
from theory.s3 import FinancialAsset

"""
## Utility classes
    ** Definition/Concept**
        
    ** Why to use Utility it**
        
    ** When to use Utility Classes **
        
"""

import math
import statistics
import numpy as np

class FinancialAssetUtil:
    @staticmethod
    def calculate_one_period_return(initial_value: float, final_value: float, method= "simple"):
        """
        Calculates financial returns based on the one initial price and one final price.
        Parameters:
        - If two numerical arguments are provided:
        - Calculates simple or logarithmic return between two values.
        - Use method='simple' (default) for simple return.
        - Use method='log' for logarithmic return.
        Returns:
        - One return, type float.
        """
        if method == 'simple':
            return FinancialAssetUtil.calculate_simple_return(initial_value, final_value)
        elif method == 'log':
            return FinancialAssetUtil.calculate_log_return(initial_value, final_value)
        else:
            raise ValueError("Invalid method. Use 'simple' or 'log'.")

    @staticmethod
    def calculate_simple_return(initial_value, final_value):
        return (final_value - initial_value) / initial_value

    @staticmethod
    def calculate_log_return(initial_value, final_value):
        return math.log(final_value / initial_value)

    @staticmethod
    def calculate_volatility(returns):
        """
        Calculates the volatility (standard deviation) of a series of returns.

        Parameters:
        - returns: List or array of returns.

        Returns:
        - Volatility (standard deviation) of the returns.
        """
        if not isinstance(returns, (list, tuple)):
            raise ValueError("Returns must be a list or tuple.")
        if len(returns) < 2:
            raise ValueError("Returns list must contain at least two returns.")
        return statistics.stdev(returns)

    @staticmethod
    def calculate_drawdown(prices):
        """
        Calculates the drawdowns for a series of prices.

        Parameters:
        - prices: List of prices.

        Returns:
        - List of drawdown values.
        """
        if not isinstance(prices, list):
            raise ValueError("Prices must be a list.")
        peak = prices[0]
        drawdowns = []
        for price in prices:
            if price > peak:
                peak = price
            drawdown = (peak - price) / peak
            drawdowns.append(drawdown)
        return drawdowns

    @staticmethod
    def calculate_max_drawdown( prices):
        """
        Calculates the max drawdowns for a series of prices.

        Parameters:
        - prices: List of prices.

        Returns:
        - max drawdown value.
        """
        return np.max(FinancialAssetUtil.calculate_drawdown(prices))

    @staticmethod
    def calculate_cumulative_return(returns):
        """
        Calculates the cumulative return from a series of returns.

        Parameters:
        - returns: List of returns.

        Returns:
        - Cumulative return value.
        """
        cumulative = 1.0
        for r in returns:
            cumulative *= (1 + r)
        return cumulative - 1



"""
## Static Methods: @staticmethod
    ** Definition/Concept** 

    ** Why to use it** 
       
    ** When to use it   ** 
"""

#TODO: modify the FinancialAssetUtil with static method


"""
## Decorators
    ** Definition/Concept
       
    ### Why
        
    ### When to use it
       
"""

"""
Example: how to implement and use a decorator
to implement a function based operator, you need to create a function which take a function as input and implement a
wrapper function in it. 
"""

def simple_decorator(func):  # here we defined a decorator
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")

    return wrapper


@simple_decorator  # here we applied the decorator to the function say_hello()
def say_hello():
    print("Hello, OOP course")

say_hello()

"""
** Decorators
Python provides several built-in decorators and others in its standard library. 
The most common are @staticmethod, @dataclass, @property, @classmethod
We already saw the first two one. Let's take a look at the other ones.

    @staticmethod
    The @staticmethod decorator is used for methods that don’t need access to the class or instance.
    
    @dataclass
    The @dataclass decorator, introduced in Python 3.7, automatically generates special methods like init(), repr(), 
    and eq() for a class

    @property
    The @property decorator is used to define methods in a class that act like attributes.
    
    @classmethod
    The @classmethod decorator is used to define methods that operate on the class rather than instances.
"""

""" 
## Data class

    **Definition/Concept:**

    **Why to use it:**

    **When to use it:**

"""

"""
Example of a dataclass: Quote
To define a dataclass we use the decorator @dataclass. By doing so we no longer need to implement the init method or
other dunder method that are frequently implemented. Moreover if we perform an equality test for a dataclass, it will
check if all the attribute are the same and not if the instance of the two object are the same. 
"""

from dataclasses import dataclass


@dataclass()
class Quote:
    date: datetime
    price: float


equity_last_quote = Quote(datetime(2023, 9, 29), 150)
print("str representation of dataclass")
print(str(equity_last_quote))
print("repr representation of dataclass")
print(repr(equity_last_quote))

equity_last_quote1 = Quote(datetime(2023, 9, 29), 150)
print("equal condition of dataclass")
print(equity_last_quote == equity_last_quote1)

"""
** @property Decorator

    ### Definition/Concept
       
    ### Why to use it
        
    ### When to use it
        

"""

class Position:
    def __init__(self, asset: FinancialAsset, initial_investment: float, current_value: float):
        self.asset = asset
        self.average_entry_price = initial_investment
        self.market_value = current_value

    @property
    def pnl(self):
        return self.market_value - self.average_entry_price


last_date, last_close = datetime.now(), 175.0
equity_last_quote = Quote(last_date, last_close)
equity = FinancialAsset('AAPL', equity_last_quote, 'USD')

position = Position(equity, 1000, 1250)
print(position.pnl)

#TODO: implement a new property which compute the total return of the position


"""
** @classmethod decorator
    ** Definition/Concept
       
    ** Why to use it
        
    ** When to use it
        
"""

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)

date = Date.from_string("2024-07-29")
print(date.year)  # Output: 2024


"""
## Class-based Decorator
    ** Definition/Concept** 
    
    ** Why to use it** 
    
    ** When to use it  ** 

"""


class TradeLogger:
    def __init__(self, log_file='trade_log.txt'):
        self.log_file = log_file

    def __call__(self, execute_trade_func):
        def wrapper(*args, **kwargs):
            trade_result = execute_trade_func(*args, **kwargs)
            with open(self.log_file, 'a') as file:
                date = datetime.now()
                file.write(f"{date} - Trade Executed - Details: {trade_result}\n")
            return trade_result

        return wrapper


class Order:
    def __init__(self, ticker, quantity, order_type, order_status="CREATED", price_limit=None):
        self.ticker = ticker,
        self.qty = quantity,
        self.order_status = order_status,
        self.order_type = order_type
        self.price_limit = price_limit


class TradeExecutionService:
    @staticmethod
    @TradeLogger(log_file='../my_trades.txt')
    def execute_trade(order: Order):
        # For simplicity, we'll just return a dict of trade details.
        # In reality, the function might communicate with a brokerage API, handle order placement, etc.
        trade_details = {
            'ticker': order.ticker,
            'price': 100,
            'qty': order.qty,
            'order_type': order.order_type,
            'trade_status': "DONE"
        }
        return trade_details


# Executing a trade
order_0 = Order('FP FP Equity', -1000, "limit", price_limit=99.95)
trade_details = TradeExecutionService.execute_trade(order_0)



