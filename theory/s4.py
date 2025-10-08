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

from exercise.s3.corrected_version.cutom_error_corrected import NegativePriceException
from theory.s3 import FinancialAsset

"""
## Utility classes
    ** Definition/Concept**
        A utility class is a design pattern in Object-Oriented Programming (OOP) where the class groups together a set 
        of methods that perform common, often standalone, functions without maintaining state. These classes are 
        typically static in nature and are not instantiated. Instead, they serve as a collection of methods that can be
         called without creating an object of the class.

    ** Why to use Utility it**
        -Organization and Cohesion: By grouping related methods together, you make the codebase cleaner and more 
        intuitive. Related functionalities are located together, so developers know where to look.

        -Code Reusability: Once a method is defined in a utility class, it can be used anywhere in the application 
        without instantiation, reducing redundancy.

        - Statelessness: Utility classes typically don't maintain state, reducing the potential for bugs related to 
        mutable shared state.

    ** When to use Utility Classes **
        - Common Calculations: As with the example above, if there are calculations that are used frequently in 
        different parts of the application, they can be grouped in a utility class.
        - Data Validations: Validating data formats, ensuring data adheres to certain standards, or checking 
        constraints.

        -Conversions: Any kind of conversion, be it currency, data format, units, etc., can be incorporated within a 
        utility class for easy access and clarity.

        -Constants: If there are constants specific to your project that need to be used across different parts of 
         an application, they can be housed in a utility class.

    However, one should be cautious not to overuse utility classes. If you find that a utility class is growing too 
    large or incorporating too many unrelated methods, it might be a sign that the responsibilities should be refactored
    or divided among more specialized classes. Utility classes should remain cohesive, with each method serving a related 
    utility function.
"""

import math
import statistics
import numpy as np


class FinancialAssetUtil:
    def calculate_one_period_return(self, initial_value: float, final_value: float, method="simple"):
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
            return self.__calculate_simple_return(initial_value, final_value)
        elif method == 'log':
            return self.__calculate_log_return(initial_value, final_value)
        else:
            raise ValueError("Invalid method. Use 'simple' or 'log'.")

    @staticmethod
    def __calculate_simple_return(initial_value, final_value):
        return (final_value - initial_value) / initial_value

    @staticmethod
    def __calculate_log_return(initial_value, final_value):
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

    def calculate_max_drawdown(self, prices):
        """
        Calculates the max drawdowns for a series of prices.

        Parameters:
        - prices: List of prices.

        Returns:
        - max drawdown value.
        """
        return np.max(self.calculate_drawdown(prices))

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
## Static Methods : @staticmethod
    ** Definition/Concept** 
        Static methods in python are a special kind of method which are created within a class for helping 
        purposes. They don't know anything about class state. They are used to perform utility tasks, and they can't 
        modify class or instance state.

    ** Why to use it** 
        Static methods are a way of putting methods in a class (to keep all the related functions together),  without 
        needing the class or instance around.

    **   When to use it   ** 
        Use a static method when you don't require access to an instance or any of its attributes or when you're 
        not going to modify the class or instance state. 
"""

# TODO: modify the FinancialAssetUtil with static method


"""
## Decorators
    ** Definition/Concept
        In Python, a decorator is a tagged that we put where a method is implemented that allows us to modify the 
        behavior of a function or class method without permanently modifying it. Decorators wrap a function, 
        augmenting or changing its behavior.
        In a nutshell, a decorator allow us to perform operation before or after the execution of a function.
        To applied a decorator to a function you will need to put an @ with the name of the decorator before the 
        implementation of the desired function (see example below)

    ### Why
        Decorators provide a way to extend a function's behavior without changing its source code. 
        This means you can reuse the same function in different contexts with different behaviors.

    ### When to use it
        Decorators are used when you want to wrap a function with additional functionality. 
        For example, you can use decorators to track execution time or check if a user is logged in before running 
        the function.
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
    print("Hello")


say_hello()

"""
Decorators can also work with functions that accept arguments:
"""


def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@log_function_call
def add(a, b):
    return a + b


result = add(3, 5)
print(result)
# Output:
# Calling function: add
# 8

"""
Decorators can also be applied to classes. Here’s a simple example:
"""


def add_description(cls):
    def description(self):
        return f"User first name is {self.first_name} and User last name is {self.last_name}"

    cls.description = description
    return cls


def test():
    pass


@add_description
class User:
    def __init__(self, first_name, last_name):
        self.first_name: str = first_name
        self.last_name: str = last_name


person = User("Bob", "Dupont")
print(person.description())

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
        `dataclass` is a decorator, introduced in Python 3.7 as part of the `dataclasses` module. 
        It provides a way to automatically generate special methods for classes, such as `__init__()`, `__repr__()`, 
        and `__eq__()`, based on the class's annotated fields. The primary aim is to reduce the boilerplate code 
        required for creating classes, especially ones that are primarily used to carry data.

    **Why to use it:**
    1. **Reduce Boilerplate**: Writing classes that primarily store data often requires repetitive code for basic 
                               operations (e.g., initializing, representation, comparison). `dataclass` reduces the 
                                need for such boilerplate.

    2. **Improve Readability**: By using `dataclass`, the intent of the class becomes clearer. It indicates that the 
                                class is primarily used for data storage.

    3. **Flexibility**: While the automatic generation of methods is its key feature, `dataclass` also offers a range 
                        of parameters, such as `order` (for ordering operations like less than or greater than), 
                        `frozen` (to make the instance immutable), and `default` (to set default values).

    4. **Type Annotations**: It encourages the use of type annotations, making code more self-documenting and 
                             potentially catching type-related errors earlier.

    **When to use it:**
    1. **Data Holders**: When you're defining classes that primarily act as data containers or simple data structures. 

    2. **Avoid Repetition**: If you find yourself repeatedly writing the same methods (`__init__`, `__repr__`, etc.) 
                            for different classes.

    3. **Immutable Data Structures**: By setting the `frozen` parameter to `True`, you can easily create immutable 
                                      data structures.

    5. **Caution**: Avoid using `dataclass` for classes with complex logic, behavior, or those that don't fit 
                    the "data container" mold. In such cases, it's better to manually implement required methods to 
                    ensure control over the class's behavior.
"""

"""
Example of a dataclass: Quote
To define a dataclass we use the decorator @dataclass. By doing so we no longer need to implement the init method or
other dunder method that are frequently implemented. Moreover if we perform an equality test for a dataclass, it will
check if all the attribute are the same and not if the instance of the two object are the same. 
"""

from dataclasses import dataclass


@dataclass
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
The dataclass decorator also takes arguments which can modify its behavior : 
    init: bool / Default: True => Generate __init__ methods automatically. Set False if you want to write your own.

    repr: bool / Default: True => Generate __repr__ showing field values. Set False if you want to write your own.

    eq: bool / Default: True => TrueGenerate __eq__ (and __ne__ by fallback). Set False if you want to write your own.

    frozen: bool / Default: False
        Make instances “read-only” after __init__ (assignments raise FrozenInstanceError).
        Warning: If you run a __post_init__() method with a Frozen = true, the object is already immutable. If you want 
        to set argument you will need to use object.__setattr__

    kw_only: bool / Default: False => Make generated __init__ parameters keyword-only by default.

    slots: bool / Default: False => Add __slots__ for the fields (saves memory, forbids new attributes).
        By default, in a python class, each instance has a dictionary that maps attribute names to values (__dict__)
        This is flexible (you can add new attributes at runtime), but it uses more memory and is slower to access.

        If you define __slots__, Python doesn’t create a __dict__. Instead, it pre-allocates fixed storage for the 
        given names, saving memory and making attribute access faster. But you cannot add arbitrary new attributes 
        unless you explicitly include "__dict__" in the slots.

        Dataclass auto-implement slots if you set the argument to true. It automatically generates __slots__  behind 
        the scenes for every attribute defined in the Dataclass. 
        Warning: if you decide to do so, you can't add new attribute after __init__
"""

from dataclasses import dataclass, field


# init (turn off auto __init__)
@dataclass(init=False)
class DataStructureNoInit:
    attribute_1: int
    attribute_2: int

    def __init__(self, attribute_1: int):  # custom initializer
        self.attribute_1 = attribute_1
        self.attribute_2 = 0


p = DataStructureNoInit(3)
print(p)

# frozen (immutable after construction)
from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    first_name: str
    last_name: str
    position: str = field(default_factory=str)
    id: str = field(init=False)

    def __post_init__(self):
        # Use object.__setattr__ if you must compute fields
        object.__setattr__(self, "id", self.first_name.lower() + self.last_name.upper())


usr = User("Léa", "Martin", "Quant analyst")
usr_1 = User("Martin", "Dupont")
# usr_1.name = "Bob"        # FrozenInstanceError
print(f"id:{usr.id}")
print(usr_1)

"""
__post_init__ is a special hook in Python’s dataclasses that runs right after the generated __init__ finishes. 
It’s perfect for validation, derived fields, type coercion, or tweaking values that depend on multiple fields.

field(default_factory=T) tells a dataclass to call a zero-argument callable T() to produce the field’s default each 
time a new instance is created. It also make the attribute optional in the init method
"""

from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class DataStructureSlotsKwOnly:
    attribute_1: int
    attribute_2: int


# d = DataStructureSlotsKwOnly(1, attribute_2=2) #Error
d = DataStructureSlotsKwOnly(attribute_1=1, attribute_2=2)
print(f"d = {d}")
# d.attribute_3 = 3              # AttributeError (slots)
d.attribute_1 = 9
print(f"d = {d}")

"""
** @property Decorator

    ### Definition/Concept
        @property is a built-in Python decorator that allows you to define a method in a class that can be accessed 
        like an attribute. It is often used to control access to private attributes or to add computed properties. 
        This means you can retrieve the result of a method by accessing it like a simple attribute, rather than calling 
        it with parentheses.

    ### Why to use it
        Using @property allows you to create methods that can be accessed like attributes, which makes code cleaner and 
        more intuitive for users of the class. It provides a way to encapsulate and protect data, and to define computed
         attributes without changing the interface of your class.

    ### When to use it
        You should use @property when you want to expose a method as a readable attribute while still maintaining the 
        flexibility to change its underlying logic or behavior later without breaking existing code. It is useful when 
        you need to perform computations or transformations on an attribute before returning it, but don't want the user
         to be aware of the logic involved.

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

# TODO: implement a new property which compute the quantity of the position based on the last price and the market value

"""
* Advanced use of property decorator
    @attributeName.setter is the decorator that defines the setter for a @property.
    It lets you run custom code (validation, normalization, side-effects) whenever someone assigns to that attribute.

    @cached_property is a decorator that computes a property once on first access, stores the result on the instance, 
    and returns the cached value on subsequent lookups until you explicitly invalidate it. 
"""

from functools import cached_property


class Position:
    def __init__(self, asset, initial_investment, current_value):
        self.asset = asset
        self._avg = initial_investment
        self._mv = current_value

    @property
    def average_entry_price(self):
        return self._avg

    @average_entry_price.setter
    def average_entry_price(self, v):
        if v < 0:
            raise NegativePriceException
        self._avg = v
        self.__dict__.pop("pnl", None)  # invalidate cache

    @property
    def market_value(self):
        return self._mv

    @market_value.setter
    def market_value(self, v):
        if v < 0:
            raise NegativePriceException
        self._mv = v
        self.__dict__.pop("pnl", None)  # invalidate cache

    @cached_property
    def pnl(self):
        return self.market_value - self.average_entry_price


"""
** @classmethod decorator
    ** Definition/Concept
        @classmethod is a decorator used to define a method that belongs to the class itself, not to an instance of 
        the class. The first argument to a class method is cls, which refers to the class (not an instance). 
        This allows class methods to modify the class state, create new instances, or access class-level attributes.

    ** Why to use it
        Class methods allow you to work with class-level data and behaviors. They are useful when you want a method 
        that logically operates on the class itself, rather than on instances of the class. You can use them to modify 
        class-level state or to provide factory methods that create instances in a certain way.

    ** When to use it
        Use a class method when:
            You need to work with class-level attributes or behaviors.
            You need to create factory methods that return instances of the class, but you want the method to remain 
            flexible and applicable to subclasses.
            You want to provide alternative constructors or handle logic related to the entire class rather than 
            individual instances.
"""


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return f"Date(year={self.year}, month={self.month}, day={self.day})"

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)


date = Date.from_string("2024-07-29")
print(date.year)  # Output: 2024

"""
## Class-based Decorator
    ** Definition/Concept** 
    Class-based decorators use the functionality of objects to hold state or utilize inheritance for related decorator 
    logic. Essentially, a class-based decorator is a class that implements the __call__ method and the wrapper function. 
    When the instance of the class is called, the __call__ method is executed. The instance of the class is called
    before the method or function annotated by the decorator. 

    ** Why to use it** 
     - State Management: One of the biggest advantages of class-based decorators over function-based ones is the ability
                        to retain state. Since classes can have instance variables, it's easy to store and manage state
                        between calls.

    - Reusability and Composition: Class-based decorators can utilize inheritance to create a family of related 
                                   decorators, or even compose multiple decorators together.

    - Enhanced Control: By defining other methods apart from __call__, you can provide more controlled or varied 
                        behavior, enhancing flexibility.

    ** When to use it  ** 
    - Stateful Decorations: When the decorator needs to remember something between calls, such as counting the number of 
                            times a function has been called or caching its results.

    - Configurable Decorations: If you need to pass arguments to your decorator to configure its behavior. 
                                Though function-based decorators can also achieve this, class-based decorators can 
                                sometimes make this more intuitive, especially when there are many parameters or complex 
                                configurations.

    - Multiple Related Decorators: If you are designing a suite of related decorators, it might be beneficial to 
                                encapsulate their shared logic within a base class and derive from it.
"""


class TradeLogger:
    def __init__(self, log_file='trade_log.txt'):
        self.log_file = log_file

    def __call__(self, execute_trade_func):
        def wrapper(*args, **kwargs):
            trade_result = execute_trade_func(*args, **kwargs)
            with open(self.log_file, 'a') as file:
                _date = datetime.now()
                file.write(f"{_date} - Trade Executed - Details: {trade_result}\n")
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
trade_details_ex = TradeExecutionService.execute_trade(order_0)

