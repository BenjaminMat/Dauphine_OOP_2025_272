"""
    ## Unit test
    ## Design Pattern

"""


"""
## unit test
     ** Definition/Concept** 
        Unit testing is a software development practice where individual components or functions of a program are 
        tested in isolation.
        A unit test typically follows this pattern: 
            1. Set up the test conditions. 
            2. Call the function or method being tested. 
            3. Assert that the output or behavior matches the expected result.
        
        Python offers several frameworks to help write and run unit tests efficiently. While the built-in unittest 
        module is available, pytest in another option which is efficient.

     ** Why to use it** 
        To verify that each part of the program works correctly on its own.
        To catch and fix bugs early in the development process.
        To facilitate refactoring and maintenance of code.
        To serve as documentation for how components should behave.

    **  When to use it ** 
        Use `unittest` whenever you write new code and want to verify its behavior or when you refactor or modify 
        the existing code to ensure its behavior hasn't changed unexpectedly.
        
        When you launch a unit test, a test session will start. For each unit test the result will be 'Passed' 
        if the unit test has the expected behavior. If not the result will be 'Failed'.
        
        Typically, we try to regroup all the unit test in one directory or one script. If you are implementing a 
        complex or large project you might want to use several script to do you unit test, each script checking one
        part of your project. If you want to run all the unit test of your script you can use the following code : 
        'unittest.main()'. If you plan to doing so, your script should implement the 'if __name__ == "__main__":'
        logic. Unit test should always be implemented in a separate script
        
    *** How to built it **
    
    One way to build you unit test is by creating a class starting with Test and inheriting from unittest.Testcase
    if you need to initialize variable for your test or have common variable to multiple test you can create a setUp(self)
    method and store those variable as attribute. You can then access the attribute in all your test.
    Good practise impose to implement one test for each behavior you want to test / control in you project. 
    WARNING : all test method should start with a Test in their name. This is important to control the behavior of 
    the test execution when you try to run all the test in one script.
    
    If you want to run all the unit test in a script you can use the following : 
        unittest.main(...)
    This is the entry point that runs your tests when a test file is executed directly.
    It discovers tests in the current module (classes deriving from unittest.TestCase, methods starting with test), 
    runs them, and reports results.
    Argument of the unitest.main : 
        - argv : unittest.main normally parses command-line args from sys.argv (like -k, -v, etc.). In notebooks or 
        embedded environments, sys.argv may contain unrelated flags that confuse unittest.
        - verbosity : Controls the amount of output:
                - 0 = quiet (dots or minimal),
                - 1 = default,
                - 2 = verbose (shows each test name and status). With 2, you get a readable list of test methods as they run.
        - exit: By default, unittest.main() calls sys.exit(...) with the test result code when it’s done. In some 
        environments, that would terminate the kernel. exit=False prevents the sys.exit, keeping the session alive.
    
    ==> a robust default settings for the function is : unittest.main(argv=[''], verbosity=2, exit=False)
"""


def square(n):
    return n ** 2


import unittest


class TestSquareFunction(unittest.TestCase):
    def setUp(self):
        pass

    def test_positive_number(self):
        self.assertEqual(square(2), 4)

    def test_zero(self):
        self.assertNotEqual(square(0), 1)


""" *** Output of unit test in the Python Console **
============================= test session starts ==============================
collecting ... collected 2 items

all_classes_extended_version.py::TestSquareFunction::test_positive_number 
all_classes_extended_version.py::TestSquareFunction::test_zero 

============================== 2 passed in 1.15s ===============================

Process finished with exit code 0
PASSED [ 50%]PASSED    [100%]
"""


"""
Example of Unit test usage
Class: TestSquareFunction
    Purpose: To containerize tests for the square function.
    Inheritance: Inherits from unittest.TestCase, allowing it to use testing methods and assertions provided by the 
    framework.

    Method: test_positive_number(self)
        Purpose: To test if the square function returns the correct output for a positive number.
        Test Assertion: self.assertEqual(square(2), 4): Asserts that square(2) should return 4.
    Method: test_zero(self)
        Purpose: To test if the square function returns the correct output for an input of zero.
        Test Assertion: self.assertEqual(square(0), 0): Asserts that square(0) should return 0.

4. Run the Tests
You can either launch the test by clicking to the play/run button next to the class or use unittest.main()
Note: Running this as-is in a regular Python script might raise an error because unittest.main() takes command 
line arguments. If you're running this in a script, you might want to use if __name__ == "__main__": 
before `unittest.main
"""




"""
## Design Pattern
"""

"""
**Descriptor
    Descriptors are especially useful when you want to add validation, logging, or specific behavior during 
    attribute access or modification, which is what we're doing in this example with volatility.
    
    Definition / Concept
        - A descriptor is an object that defines one or more of: __get__, __set__, __delete__.
        
        - When placed as a class attribute, it intercepts attribute access on instances:
            __get__(self, obj, objtype)   -> reading  obj.attr
            __set__(self, obj, value)     -> writing  obj.attr = value
            __delete__(self, obj)         -> deleting del obj.attr
            ==> When these methods are present, Python’s attribute access (obj.attr) is redirected through the 
            descriptor methods instead of the default __dict__ lookup. That’s how descriptors control what happens 
            when you get or set a value.
        
        - __set_name__(self, owner, name) (optional) runs at class creation to tell the
          descriptor its attribute name. owner in __set_name__(self, owner, name) is the class that owns the descriptor
          i.e., the class where the descriptor appears as a class attribute. It’s passed so the descriptor can set 
          itself up with awareness of which class it belongs to.
          name is the name of the attribute on which we want to apply the descriptor

    Why to use it
        - Reusable validation & coercion across many classes/fields
        - Computed/managed attributes that are used like simple fields.
        - Lazy loading & caching; easy invalidation on set/delete.
        - Cross-cutting concerns (logging, access control, metrics).

    When to use it
        Use a descriptor when:
        - The same attribute behavior is needed in multiple places.
        - Behavior must be centralized and hard to bypass (data descriptors beat instance dict).
        - You want attribute syntax, not method calls, but with custom logic.

    Prefer simpler tools when:
    - One-off attribute logic → use @property (with setter/deleter).
    - Schema-heavy models → dataclasses.

Quick checklist to implement descriptor:
- Place the descriptor on the class, not the instance.
- Implement __set_name__ to avoid manually passing the field name.
- Store the underlying value on the instance (e.g., "_<name>").
- Keep descriptors small and focused—readability first.
"""


class NonNegativeFloat:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.storage_name = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.storage_name)

    def __set__(self, obj, value):
        try:
            v = float(value)
        except (TypeError, ValueError):
            raise TypeError(f"{self.public_name} must be a number") from None

        if v < 0.0:
            raise ValueError(f"{self.public_name} must be ≥ 0")
        setattr(obj, self.storage_name, v)



class FinancialAsset:
    price = NonNegativeFloat()
    div_rate = NonNegativeFloat()

    def __init__(self, ticker: str, price: float, div_rate: float = 0.):
        self.ticker = ticker
        self.price = price
        self.div_rate = div_rate

    def __repr__(self):
        return f"{self.__class__.__name__}(ticker={self.ticker!r}, price={self.price!r})"


# Usage
asset = FinancialAsset("AAPL", 250)
print(asset.price)
asset.price=255.
# asset.price = -300  # Raises ValueError

""" another example: The LazyProperty
The idea behind lazy loading is that the value for the attribute is only computed when it's accessed for the first time,
 rather than when the object is initialized.
"""


class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        value = self.function(obj)
        setattr(obj, self.name, value)
        return value


class DataProcessor:
    def __init__(self, filename):
        self.filename = filename

    @LazyProperty
    def data(self):
        print("Loading data...")
        with open(self.filename, 'r') as f:
            return f.read()


processor = DataProcessor(
    '/Users/benjaminmat/Desktop/Dauphine_OOP_2025_272/theory/additional_ressources/dunder_method_list.txt')
# Data is not loaded yet
print(processor.data)  # Prints "Loading data..." and then the content
print(processor.data)  # Prints the content without "Loading data..."

"""
Let’s break down how this works step by step:
When @LazyProperty is applied to the data method in DataProcessor:
    An instance of LazyProperty is created, with the data method as its function attribute.
    This LazyProperty instance replaces the data method in the class dictionary.

When we create a DataProcessor instance:
    No data is loaded yet. The filename is stored, but data is not accessed.

The first time processor.data is accessed:
    In Python, attributes (including properties) can be accessed without parentheses if they are not methods 
    (i.e., they don't require arguments). In this example, data is a property. If a method does not have arguments
    it's a property. 
    Python sees that data is a descriptor (it has a __get__ method) and calls LazyProperty.__get__(processor, DataProcessor).
    Inside __get__:
        It checks if obj (processor) is None. It’s not, so it continues.
        It calls self.function(obj), which is equivalent to calling the original data method.
        This prints “Loading data…” and reads the file.
        The result is stored back into the processor instance using setattr(obj, self.name, value).
        The value is returned.

The second time processor.data is accessed:
    Python first looks for an instance attribute named data.
    It finds one (because we set it in step 3d), so it returns that value directly.
    The LazyProperty.__get__ method is not called this time.

The key point is that after the first access, the LazyProperty descriptor is effectively replaced by the computed value.
This is why the “Loading data…” message only appears once.
"""

"""
## Creational Design Patterns in Python
Creational design patterns provide various object creation mechanisms, which increase flexibility and reuse of existing
code.

## 4.8 - singleton
    ** Definition/Concept** 
        The Singleton pattern is a design pattern that restricts a class to instantiate multiple objects. 
        It's a way to ensure a class has only one, unique instance, and to provide a global point of access to it.

    ** Why to use it** 
        Singleton pattern is employed when we need to control object creation, ensuring that there's only one object 
        of its kind throughout the application, for example, a single database connection shared by multiple objects as 
        opening a database connection is a costly process.

    ** When to use it ** 
        Utilize the Singleton pattern when a particular class in your program should be available to all clients and 
        shared among all, like a single configuration object.

In Python, we can create Singleton using the `__new__` method.
"""


class SingletonExample:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def another_method(self):
        pass


a = SingletonExample()
b = SingletonExample()
print(a is b)

"""
You can also dissociate the implementation of the singleton logic from the implementation of the class by 
creating a decorator
"""


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class DatabaseConnection:
    def __init__(self):
        # Initialize the database connection
        pass


# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)

"""
## 4.5 - factory

    ## Definition/Concept
        Factory Pattern in Object-Oriented Programming (OOP) refers to a creational design pattern that provides an 
        interface for creating objects. Instead of calling a class constructor directly to create an object, a factory 
        method is used to create the object. This method is typically defined in an interface, which is implemented 
        by concrete classes.

    ### 2. Why to use it
        Here are some reasons to use the Factory Pattern:
        - **Decoupling**: The Factory Pattern promotes the decoupling of the code that uses objects from the code that 
                        creates them, which can simplify code changes and maintenance.
        - **Handling Complexity**: When object creation is complex or involves multiple steps, constructors might 
                        become overly complex. A factory can encapsulate this complexity and provide a simple API to 
                        the client.
        - **Code Reusability**: Factories can be reused across the application, which often leads to less code 
                        duplication.

    ### 3. When to use it
    The Factory Pattern is particularly beneficial in the following scenarios:

    - **Dynamic Implementation**: When the exact type of the object to be created needs to be determined at runtime 
                                based on some conditions, a factory can decide which subclass to instantiate.

    - **Complex Object Creation**: When the object creation process is complex and involves multiple steps,     
                                   it's logical to encapsulate this complexity in a factory rather than complicating the 
                                   client code with it.

    - **Family of Related Objects**: If you have a family of related objects that you need to instantiate, 
                                     it might be useful to use a factory to manage these creations, especially if they 
                                     have similar instantiation logic or configurations.

    - **Enhanced Control Over Object Creation**: If you need more control over object creation, for example implementing 
                                                 a singleton pattern, object pooling, or caching, a factory can provide 
                                                 this centralized control.

==> Use Factory when you're unsure about the exact types and dependencies of the objects your code should work with, 
    or when you want to delegate the responsibility of deciding which class to instantiate.
"""

""" 
Example
The Stock class requires a ticker symbol and price. It has a method get_market_value that returns a string indicating 
its market value per share.
The Bond class needs an issuer and face value. It has a method get_face_value that returns a string indicating its 
face value.
The FinancialInstrumentFactory class creates either a Stock or a Bond instance depending on the instrument_type 
parameter. The **kwargs argument allows us to pass the keyword arguments needed to instantiate the desired 
financial instrument.

This pattern enables you to manage the creation of various financial instrument objects systematically, even when the 
precise types of financial instruments are not known until runtime. The factory method can be extended to handle 
additional financial instrument types as needed, enhancing modularity and scalability in the software design.
"""


class FinancialInstrumentFactory:
    @staticmethod
    def create_financial_instrument(instrument_type, **kwargs):
        if instrument_type.lower() == "stock":
            return StockFactoryExample(**kwargs)
        elif instrument_type.lower() == "bond":
            return BondFactoryExample(**kwargs)
        else:
            raise ValueError("Invalid financial instrument type")


class StockFactoryExample:
    def __init__(self, ticker, price):
        self.ticker = ticker
        self.price = price

    def get_market_value(self):
        return f"The market value of {self.ticker} is ${self.price} per share."


class BondFactoryExample:
    def __init__(self, issuer, face_value):
        self.issuer = issuer
        self.face_value = face_value

    def get_face_value(self):
        return f"The face value of bond issued by {self.issuer} is ${self.face_value}."


# Create a Stock
stock = FinancialInstrumentFactory.create_financial_instrument("stock", ticker="AAPL", price=150)
print(stock.get_market_value())  # Output: The market value of AAPL is $150 per share.

# Create a Bond
bond = FinancialInstrumentFactory.create_financial_instrument("bond", issuer="US Government", face_value=1000)
print(bond.get_face_value())  # Output: The face value of bond issued by US Government is $1000.
