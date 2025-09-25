"""
Table of contents :
        ## Polymorphism in OOP
        ## Abstract class
        ## Protocol class
        ## Error handling
"""
from datetime import datetime

from scipy.stats import norm
import math

"""
## 1.10 - Polymorphism

    ** Definition/Concept **    
        Polymorphism is one of the four fundamental principles of Object-Oriented Programming (OOP). 
        Polymorphism is the ability of an object to take on many forms, and it allows the programmer 
        to treat derived class members just like their parent class's members. This increases code reusability and 
        improves the efficiency of the code.

    ** Why to use it** 
        Polymorphism brings two major benefits:
        1. __Flexibility__: It allows developers to use the same function/entity name to mean different things in 
                            different contexts, making the code more flexible and easy-to-understand.
        2. __Reusability__: Polymorphism encourages reusability by accommodating different types and classes in the
                            same entity, or function. This reduces unnecessary code and makes it more efficient.

    In the context of programming, polymorphism allows us to use a single interface with different underlying forms. 
    This means that functions or classes can be used with many types of objects, and behave differently based on 
    the object's type.

    ** When to use it **
        Polymorphism is useful when you have a list (or other collections) of objects that could be instances of 
        several different classes related through inheritance and you want to operate on them in the same way. 

"""
from abc import ABC, abstractmethod


class Asset(ABC):
    @abstractmethod
    def price(self):
        return NotImplemented


class Equity(Asset):
    def __init__(self, spot_price):
        self.spot_price = spot_price

    def price(self):
        return self.spot_price


class Option(Asset):
    def __init__(self, spot, strike, risk_free, time_to_maturity, volatility):
        self.spot: float = spot
        self.strike: float = strike
        self.risk_free: float = risk_free
        self.ttm: float = time_to_maturity
        self.vol: float = volatility

    def compute_d1(self):
        d1 = (math.log(self.spot / self.strike) + (self.risk_free + 0.5 * self.vol ** 2) * self.ttm) / \
             (self.vol * math.sqrt(self.ttm))
        return d1

    def compute_d2(self):
        d2 = self.compute_d1() - self.vol * math.sqrt(self.ttm)
        return d2

    def price(self):
        raise NotImplemented


class Call(Option):
    def __init__(self, spot, strike, risk_free, time_to_maturity, volatility):
        super().__init__(spot, strike, risk_free, time_to_maturity, volatility)

    def price(self):
        n_d1 = norm.cdf(self.compute_d1())
        n_d2 = norm.cdf(self.compute_d2())
        return self.spot * n_d1 - self.strike * math.exp(-self.risk_free * self.ttm) * n_d2


class Put(Option):
    def __init__(self, spot, strike, risk_free, time_to_maturity, volatility):
        super().__init__(spot, strike, risk_free, time_to_maturity, volatility)

    def price(self):
        n_minus_d1 = norm.cdf(-self.compute_d1())
        n_minus_d2 = norm.cdf(-self.compute_d2())
        return self.strike * math.exp(-self.risk_free * self.ttm) * n_minus_d2 - self.spot * n_minus_d1


# Instantiate different assets
stock = Equity(spot_price=100)
call = Call(spot=100, strike=90, volatility=0.2, time_to_maturity=1, risk_free=0.05)
put = Put(spot=100, strike=90, volatility=0.2, time_to_maturity=1, risk_free=0.05)


def print_asset_price(asset: Asset):
    print(f"The price of the {asset.__class__.__name__} is: {asset.price():.2f}")


# Use the same function to print prices of different asset types
print_asset_price(stock)  # Output: The price of the Equity is: 100.00
print_asset_price(call)  # Output: The price of the Call is: 16.70
print_asset_price(put)  # Output: The price of the Put is: 2.31

"""
Types of Polymorphism:
         Overriding - Runtime Polymorphism (Dynamic):
            Achieved through method overriding
            Resolved at runtime

        Overloading - Compile-time Polymorphism (Static):
            Achieved through method overloading
            Resolved at compile time

Method Overriding - Native in Python
    Method overriding is a fundamental aspect of runtime polymorphism. It occurs when a derived class (child class) 
    has a method with the same name and signature as a method in its base class (parent class).

    Key Points about Method Overriding:
        Same Name and Signature: The overriding method must have the same name and parameter list as the method in 
        the parent class.

    Runtime Decision: The method to be invoked is determined at runtime based on the object’s type.

    Extends or Modifies Behavior: Overriding allows a child class to provide a specific implementation of a method 
    that is already defined in its parent class.

    Polymorphic Behavior: It’s a key mechanism for achieving polymorphic behavior in OOP.
"""

"""    
Method Overloading - Not native in Python
    Method overloading is a fundamental aspect of compile-time polymorphism (static polymorphism). 
        In java or C++, it occurs when a class contains multiple methods with the same name but different parameter lists 
        (different types, number of parameters, or both).

    Key Points about Method Overloading:
        Same Name, Different Signatures: The overloaded methods must share the same name but have different parameter 
        lists. This difference can be in the number of parameters, the types of parameters, or both.

    Compile-time Decision: The method to be invoked is determined at compile time based on the method signature 
    that matches the arguments provided during the method call.

    Enhances Flexibility: Overloading allows a class to perform similar or related operations with different inputs, 
    providing multiple ways to use the same method name. This enhances code readability and usability.

    Not Polymorphic at Runtime: Unlike method overriding, method overloading does not exhibit polymorphic behavior at
    runtime. All decisions are made during compilation, and no dynamic method dispatch occurs.
"""

from multipledispatch import dispatch


class CalculatorDispatchExample:
    @dispatch(int, int)
    def add(self, a, b):
        return a + b

    @dispatch(float, float)
    def add(self, a, b):
        return a + b

    @dispatch(int, int, int)
    def add(self, a, b, c):
        return a + b + c


calc = CalculatorDispatchExample()
print(f"Sum of integers: {calc.add(5, 10)}")  # Output: 15
print(f"Sum of integers: {calc.add(5, 10, 15)}")  # Output: 30

"""    
Method Overloading - Alternative to dispatch package
    In Python, if we do not want to use the dispatch package we need to use different strategies to handle different 
    types of inputs:
        - Different Function Names, 
        - Single Function with Type Checking
"""


class CalculatorPythonNative:
    def add(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return self._add_int(a, b)
        if isinstance(a, float) and isinstance(b, float):
            return self._add_double(a, b)
        else:
            raise TypeError("Unsupported type for add method")

    def _add_int(self, a: int, b: int) -> int:
        return a + b

    def _add_double(self, a: float, b: float) -> float:
        return a + b


# Usage
calc = CalculatorPythonNative()
print(calc.add(5, 10))  # Output: 15
print(calc.add(5.0, 10.0))  # Output: 30

"""
Dynamic input handling : 
    In order to add flexibility to a code, we sometime wants to create generic methods than can handle a wide range of
    arguments. In this case, we use *args and kwargs as inputs in our methods signatures. 
    It allows us to accept a variable number of positional (*args) and keyword (**kwargs) arguments without predefining 
    them all.
    The advantage is that it easily pass through any extra arguments to another function (great for decorators, 
    adapters, subclass overrides) and you can extend a function later without breaking older call sites, 
    new parameters can be caught by **kwargs.
    When we use this type of functionalities, the handling of the input are defined in the implementation of the class

    *args is a tuple of the extra positional arguments.
    **kwargs is a dict mapping str keys to the extra keyword-argument values.

    Best practices
        Don’t overuse
        Prefer explicit parameters when the function has a stable, known interface—they’re self-documenting and type-check 
        better.

        Validate & document
        If you accept **kwargs, document supported keys and validate them (e.g., raise error on unknowns).

        Type hints help
        Use Typing : *args: int or **kwargs: str to aid developers when applicable.

        Combine with explicit params
        Put required/commonly used params explicitly, then *args/**kwargs for extras:
            def plot(data, *args, color="black", **kwargs):
                ...

        Use for pass-through
        Great when your function largely forwards to another function and you don’t want to mirror its entire signature.
"""


class CalculatorWithDynamicHandling:
    def add(self, *args):
        if all([isinstance(arg, int) for arg in args]):
            return sum(args)
        if all([isinstance(arg, float) for arg in args]):
            return math.fsum(args)
        else:
            raise TypeError


calc = CalculatorWithDynamicHandling()
print(f"int sum : {calc.add(1, 2, 3)}")
print(f"float sum : {calc.add(2.0, 3.0, 4.5, 99999999999.3456789)}")


# calc.add(1, 5.5)


# A more concrete example of method overloading and dynamic input
class FinancialAssetUtil:
    def calculate_return(*args, method='simple'):
        """
        Calculates financial returns based on the inputs provided.

        Parameters:
        - If two numerical arguments are provided:
          - Calculates simple or logarithmic return between two values.
          - Use method='simple' (default) for simple return.
          - Use method='log' for logarithmic return.
        - If a list of prices is provided:
          - Calculates returns between consecutive prices.
          - Use method='simple' or method='log' to specify the return type.
        """
        if len(args) == 2 and all(isinstance(arg, (int, float)) for arg in args):
            initial_value, final_value = args
            if method == 'simple':
                # Simple Return
                return (final_value - initial_value) / initial_value
            elif method == 'log':
                # Logarithmic Return
                return math.log(final_value / initial_value)
            else:
                raise ValueError("Invalid method. Use 'simple' or 'log'.")
        elif len(args) == 1 and isinstance(args[0], list):
            prices = args[0]
            if len(prices) < 2:
                raise ValueError("Price list must contain at least two prices.")
            returns = []
            for i in range(1, len(prices)):
                initial_value = prices[i - 1]
                final_value = prices[i]
                if method == 'simple':
                    ret = (final_value - initial_value) / initial_value
                elif method == 'log':
                    ret = math.log(final_value / initial_value)
                else:
                    raise ValueError("Invalid method. Use 'simple' or 'log'.")
                returns.append(ret)
            return returns
        else:
            raise ValueError("Invalid arguments provided.")


# Examples of usage:
# 1. Simple return between two values
initial_price = 100
final_price = 110
simple_return = FinancialAssetUtil.calculate_return(initial_price, final_price)
print(f"Simple Return: {simple_return:.2%}")  # Output: Simple Return: 10.00%

# 2. Logarithmic return between two values
log_return = FinancialAssetUtil.calculate_return(initial_price, final_price, method='log')
print(f"Logarithmic Return: {log_return:.4f}")  # Output: Logarithmic Return: 0.0953

# 3. Returns from a list of prices (simple returns)
price_series = [100, 105, 103, 108]
returns_simple = FinancialAssetUtil.calculate_return(price_series)
print(f"Simple Returns: {[f'{r:.2%}' for r in returns_simple]}")
# Output: Simple Returns: ['5.00%', '-1.90%', '4.85%']

# 4. Returns from a list of prices (logarithmic returns)
returns_log = FinancialAssetUtil.calculate_return(price_series, method='log')
print(f"Logarithmic Returns: {[f'{r:.4f}' for r in returns_log]}")
# Output: Logarithmic Returns: ['0.0488', '-0.0191', '0.0474']


"""
## Abstraction in Python

    ** Definition/Concept** 
        Abstraction in OOP is the process of hiding the underlying details and displaying only the functionalities. 
        It helps to reduce the complexity by separating the behavior from the implementation. 
        In Python, one way to perform abstraction is through using Abstract Base Classes (ABCs). 
        An Abstract Base Class is a class serving as a blueprint for other classes. 
        It allows you to define methods that must be created within any child classes built from the ABC. 
        Therefore, it provides a certain level of design structure, enforcing that certain methods exist within any 
        child classes.

    ** Why to use it** 
        Abstraction allows us to define a clear and consistent interface of an object in our code. 
        By leveraging the ABC package, we can ensure that all classes that derive from our abstract base class will 
        adhere to the same interface. This helps to improve the maintainability and readability of our code, as we can 
        code using the abstract base class knowing that certain methods will always be present in any subclasses.

        Moreover, code abstraction can allow better system design and efficient, scalable code. More subsequent 
        operations and functionalities can be added and integrated with minimal disruption to the original code 
        structure. 

    ** When to use it  ** 
        ABCs should be employed when we have a core set of methods that we expect to be present in every subclass, 
        but we do not want to provide a default implementation for those methods. 
        This is particularly relevant when we have a number of related classes with common functionalities 
        which need not be repeated in each individual class. 

    ** How to implement an abstract class**
        You will find below a basic implementation of an abstract method. The AbstractClassExample is an abstract 
        class as it implements/ inherit the ABC class.
        When the @abstractmethod is defined prior a function, this makes this function mandatory for every subclass 
        implementing the abstract class. When @abstractmethod is not defined prior a function, its implementation 
        become non-mandatory. It considers as best practice to only implement mandatory method in an abstract class. 
"""

from abc import ABC, abstractmethod


class AbstractClassExample(ABC):
    @abstractmethod
    def mandatory_method(self):
        pass

    def not_mandatory_method(self):
        pass


class Subclass(AbstractClassExample):
    def mandatory_method(self):
        print("The subclass is implementing the mandatory method")

    def another_method(self):
        print("The subclass is implementing another method")


class AnotherSubclass(AbstractClassExample):
    def another_method(self):
        print("The subclass isn't implementing the mandatory method")


x = Subclass()
x.mandatory_method()
# y = AnotherSubclass() # TypeErrorWill: Can't instantiate abstract class AnotherSubclass
# z = AbstractClassExample() # TypeError: Can't instantiate abstract class


"""
# Protocol in Python

    **Protocols**, introduced in Python 3.8, provide a way to define structural subtyping (often called “duck typing”).
     They allow you to define interfaces in a more flexible and Pythonic way compared to abstract base classes.

    ## Key Concepts
        - **Structural Subtyping**: An object is considered a subtype if it has the required methods and attributes, regardless of inheritance.
        - **No Runtime Enforcement**: Protocols are primarily used for static type checking and don’t enforce method implementation at runtime.
        - **Flexibility**: Classes don’t need to explicitly inherit from a Protocol to be considered compatible.

    To use Protocols, you need to import them from the `typing` module:

"""

from typing import Protocol


class Tradable(Protocol):
    symbol: str

    def current_price(self) -> float:
        ...


"""
`Tradable` is a protocol that specifies any object with a `symbol` attribute of type `str` and a `current_price` 
method that returns a `float`.
Now, consider a class `Stock` that doesn't inherit from `Tradable` but matches its structure.
We can write a function that accepts any object conforming to the `Tradable` protocol.
"""


class Ticker:
    def __init__(self, symbol: str):
        self.current_symbol = symbol
        self.old_symbol = []


class Stock:
    def __init__(self, symbol: str, price_per_share: float):
        self.symbol = symbol
        self.price_per_share = price_per_share

    def current_price(self) -> float:
        return self.price_per_share


def display_instrument_price(instrument: Tradable):
    print(f"The current price of {instrument.symbol} is ${instrument.current_price():.2f}")


ticker = Ticker("AAPL")
stock = Stock("AAPL", 150.0)
display_instrument_price(stock)  # Output: The current price of AAPL is $150.00

"""
Even though `Stock` doesn't inherit from `Tradable`, it is accepted by the `display_instrument_price` function
because it has the required `symbol` attribute and `current_price` method.
"""


# Another Example
class Pricable(Protocol):
    def price(self) -> float:
        ...


class StockPricable:
    def __init__(self, symbol: str, price_per_share: float):
        self.symbol = symbol
        self.price_per_share = price_per_share

    def price(self) -> float:
        return self.price_per_share


class CallPricable:
    def __init__(self, spot, strike, risk_free, time_to_maturity, volatility):
        self.spot: float = spot
        self.strike: float = strike
        self.risk_free: float = risk_free
        self.ttm: float = time_to_maturity
        self.vol: float = volatility

    def compute_d1(self):
        d1 = (math.log(self.spot / self.strike) + (self.risk_free + 0.5 * self.vol ** 2) * self.ttm) / \
             (self.vol * math.sqrt(self.ttm))
        return d1

    def compute_d2(self):
        d2 = self.compute_d1() - self.vol * math.sqrt(self.ttm)
        return d2

    def price(self) -> float:
        n_d1 = norm.cdf(self.compute_d1())
        n_d2 = norm.cdf(self.compute_d2())
        return self.spot * n_d1 - self.strike * math.exp(-self.risk_free * self.ttm) * n_d2


def calculate_asset_list_value(assets: list[Pricable]) -> float:
    total = 0.0
    for asset in assets:
        total += asset.price()
    return total


stock = StockPricable("AAPL", 150.0)
option = CallPricable(spot=100, strike=90, volatility=0.2, time_to_maturity=1, risk_free=0.05)

asset_list = [stock, option]

total_value = calculate_asset_list_value(asset_list)
print(f"Total Portfolio Value: ${total_value:.2f}")

"""
## Python Exception Handling

    Exception Handling in Python: try, except, finally
     ** In-Depth Definition/Concept**
        In Python, as with any programming language, errors are bound to happen in code.
        These could be syntax errors made by programmers, or exceptions that arise during execution.
        Exception handling is an essential aspect of programming that determines how a program reacts to unexpected 
        errors during its execution process. Python provides built-In exceptions that can handle various types of 
        errors ranging from dividing a number by zero, to calling a non-existent method.

    To handle exceptions, Python uses three keywords: try, except, and finally.
        - The `try` block lets you test a block of code for errors.
        - The `except` block lets you handle the error.
        - The `finally` block allows you to execute code, regardless of the result of the try and except blocks.

    ** Why use it **
        Exception handling is a key aspect of coding in any language including Python.
        It's essential for creating robust and fault-tolerant software applications. It offers a way to anticipate 
        problems, and provides a method of handling errors gracefully without causing crashes.

    ** When to use it  **
        Exception handling should be used whenever there's a chance that an error could occur during the execution of 
        your code.This can be when you're interacting with files, making network requests, working with collections,
        or undertaking many other common tasks.
"""


def divide(a, b):
    division = None
    try:
        division = a / b
    except ZeroDivisionError:
        print("You tried to divide by zero.")
    finally:
        return division


result = divide(10.5, 2.0)
print(result)
result1 = divide(10.5, 0.0)

"""
## Custom Exception
    ** Definition/Concept** 
        Python by default provides several built-in exceptions such as `ValueError`, `TypeError`, `IndexError` etc.
        However, there might be cases where we would want to purposefully raise an exception. This is where custom 
        exceptions come into play. A custom exception class can be created by inheriting from the base class 
        `Exception`, or any other built-in exception class.

    ** Why to use Custom Exceptions** 
        - **Understandability**: By creating our own exceptions, we give clear names to them which can easily be 
                                understood by someone else reading the code. Instead of using common built-in exceptions 
                                everywhere, having a specific exception type give more human-readable and self-explained 
                                exceptions. 
        - **Control flow**: Custom exception allows us to control the flow of our program explicitly. 
                            We can choose when and where to raise these exceptions.
        - **Modularity**: A single custom exception class can be used across multiple modules in an application.

    ** When to use Custom Exceptions  ** 
        Custom exceptions are especially helpful when we want to handle certain situations differently based on the type 
        of error in our code. For every unique situation, we can create a new exception class and then catch it in our 
        code. When we are building a large Python application, it's a good practice to define our own exception class.

The primary goal is often just to provide a unique type that can be caught and handled separately from other types of 
exceptions. When creating a custom exception class, it's not always necessary to add additional methods or attributes 
to the class. If no extra functionality is needed, and the sole purpose is to provide a distinct exception type, 
then the body of the class can be left empty.
"""

"""
Example: Exception when particular behavior happened during execution, application to Updating quote for the
FinancialAsset object
"""


class NegativePriceException(Exception):
    def __init__(self, *args):
        self._args = args

    def __str__(self):
        return f"Negative Price Exception for {self._args}"


class Quote:
    def __init__(self, date: datetime, price: float):
        self.date = date
        self.price = price

    def __repr__(self):
        return f"Quote(date={self.date!r}, price={self.price!r})"


class FinancialAsset:
    def __init__(self, ticker, quote, currency):
        self.ticker: str = ticker
        self.last_quote: Quote = quote
        self.currency: str = currency
        self.history: [Quote] = []

    def update_last_quote(self, new_quote: Quote):
        try:
            self.__check_quote_for_asset(new_quote)
            self.history.append(self.last_quote)
            self.last_quote = new_quote
        except NegativePriceException as price_exception:
            print(str(price_exception))
            print("Quote has not been updated")
            # raise
        finally:
            pass

    def __check_quote_for_asset(self, new_quote: Quote):
        if new_quote.price < 0:
            raise NegativePriceException(new_quote)


last_date, last_close = datetime.now(), 175.0
equity_last_quote = Quote(last_date, last_close)
equity = FinancialAsset('AAPL', equity_last_quote, 'USD')

last_date2, last_close2 = datetime.now(), -200
equity_last_quote2 = Quote(last_date2, last_close2)
equity.update_last_quote(equity_last_quote2)

# TODO: Create a custom exception after the PriorDateForUpdatingQuoteException that raised an error when the date
# of a quote used to update last quote for asset is before the current stored quote. Then modify the update last quote
# to store the quote in the quote history without updating the last quote attribute

