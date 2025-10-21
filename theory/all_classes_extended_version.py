"""
Table of contents :
    Part 1 : Introduction and Core concepts
        ## 1.1 - What is Object-oriented programming
        ## 1.2 - Fundamental Concepts in OOP
        ## 1.3 - Benefits of OOP
        ## 1.4 - Classes and Objects in Python
        ## 1.5 - Attributes and Methods in Python
        ## 1.6 - The self Parameter
        ## 1.7 - The `__init__` Method
        ## 1.8 - Encapsulation in Python
        ## 1.9 - Inheritance in Python
        ## 1.10 - Polymorphism in Python
        ## 1.11 - Abstraction in Python

    Part 2 : Non OOP concepts to have in mind when you write code or build a project
        ## 2.1 - PEP 8
        ## 2.2 - Error Handling
        ## 2.3 - if __name__ == "__main__":
        ## 2.4 - List comprehension

    Part 3 : Dunder methods
        ## 3.1 - Overall definition
        ## 3.2 - Use built-in functions for classes by implementing dunder methods
        ## 3.3 - Operator overloading
        ## 3.4 - Custom properties and behavior definition

    Part 4 : Additional OOP Concepts
        ## 4.1 - Decorators
        ## 4.2 - static method
        ## 4.3 - class method
        ## 4.4 - dataclass
        ## 4.5 - utility class
        ## 4.6 - Factory
        ## 4.7 - custom exception
        ## 4.8 Descriptors
        ## 4.9 - singleton
        ## 4.10 - unit test

    Part 5: Understanding import and project management
         ## 5.1 Imports
         ## 5.2 Package management

"""


"""
If you want to run or debug one of the example below, copy paste it in the main.py script. 
"""


"""
                            Part 1 : Introduction and Core concepts
"""



"""
## 1.1 - What is Object-oriented programming

    ### Definition/Concept:
        Object-oriented programming (OOP) is a design paradigm where the data structures are defined as objects that
        can possess their behavior (methods) and attributes.

    ### Why do we use OOP:
        Code structured according to OOP principles is easier to manage, test, and debug, given its organized and
        modular nature.
        OOP also allows us to encapsulate (i.e., 'hide') internal state and behavior of objects, exposing only what's
        required. This provides a clean and controllable interface with the object's data and functions.

    ### When to use OOP:
        OOP is excellent for situations where you need to create multiple instances that share common behavior but
        have unique states. It also allows programmers to build complex framework while maintaining readability and
        scalability. OOP also allows multiple developers to work easily at the same time in a common project.


## 1.2 - Fundamental Concepts in OOP

    The backbone of OOP includes these four fundamental concepts:
    1. **Encapsulation:** Encapsulation is all about safe data storage. It binds together code (methods) and the data
                          it manipulates (attributes), keeping both safe from outside interferences and misuse.

    2. **Inheritance:** Inheritance allows classes to inherit commonly used state and behavior from other classes,
                        reducing repetitive code.

    3. **Polymorphism:** Polymorphism allows us to redefine methods for derived classes, which enables us to perform
                         a single action in different ways.

    4. **Abstraction:** Abstraction allows us to hide complex details and display only the essentials,
                        providing a simpler user interface.


## 1.3 - Benefits of OOP

    **Modularity for easier troubleshooting: When an issue pops up, you can typically spot it in the
                                             code block or 'object' in question. For example, in a complex
                                             trading algorithm, if a calculation error appears, you can likely
                                             isolate the problem to a specific stock object - which greatly
                                             simplifies the debugging process.

    **Reuse of code through inheritance:Inheritance allows classes to inherit characteristics from existing
                                        classes. Consequently, it helps in reducing code redundancy,
                                        particularly when creating intricate financial models with common
                                        components.

    **Flexibility through polymorphism: This is extremely useful when implementing complex systems that
                                        require a single interface to control different inputs.

    Through these advantages, the principles of OOP allow us to model and solve complex problems more robustly, 
    efficiently, and intuitively.
"""


"""
## 1.4 - Classes and Objects in Python
    **Definition/Concept:** 
        In object-oriented programming (OOP), a class is a blueprint or template that defines the variables and 
        the methods (functions) common to all objects of a certain kind. An object is a specimen of a class.
    
    **Why:** 
        Using classes, we encapsulate data and the methods that operate on them so they are easy to reuse and maintain.
        Objects provide a simple way to access this data and methods provided by classes.
    
    **When to use it:** 
        Classes and objects are used when we need to group relevant data and methods into a single place.


## 1.5 - Attributes and Methods in Python
    **Definition/Concept:** 
        An attribute is a characteristic of an object. These are essentially variables that are bound to the 
        instances of the class. Methods, on the other hand, define the behaviors of these objects. These are 
        like functions defined within a class.

    **Why:** 
        Attributes and methods encapsulate the state and logic of the entities modelled into a cohesive unit.

    **When to use it:** 
        Attributes are used when we need information about the object that must endure for as long as the object exists.
         Methods are used when behavior or action needs to be defined for an object. 
         

## Summary / Key take-away ##   
    A Class in Python is the blueprint from which individual objects are created. It is a user-defined prototype that 
    consists of attributes and methods that act on those attributes. Attributes are the characteristics of the class, 
    while methods define the behaviors of the class.              
"""

"""
EXAMPLE : First example of a class in Python
"""


class FinancialAsset:
    def __init__(self, ticker):
        self.ticker = ticker

    def display_ticker(self):
        print(f'Ticker Symbol: {self.ticker}')


apple_equity = FinancialAsset('AAPL')
print(apple_equity.ticker) #'AAPL'
apple_equity.display_ticker()  # Ticker Symbol: AAPL

""" 
## 1.6 - The self Parameter

    **Definition/Concept:** 
        `self` is a parameter in the instance method and is a reference to the instance of the class. 
    
    **Why:** 
        The `self` represents the instance of the class and by using the `self` keyword we can access the attributes 
        and methods associated with the instance.
    
    **When to use it:** 
        `self` is also used as a parameter in instance methods notably in object initializers which are 
        established by the `__init__` method.


## 1.7 - The `__init__` Method

    **Definition/Concept**: 
        The `__init__` method is one of Python's special methods used for initializing the attributes of a class.
    
    **Why**: 
        The `__init__` method when declared in a class, is automatically invoked when the object of the class is 
        instantiated.
    
    **When to use it:** 
        `__init__` is handy when we need to initialize our object's attributes when the object is being created.


In the above example, we see that `self` is used as the first parameter of the `__init__` method as well as 
being used to define the `display_ticker()` method.
"""

"""
## 1.8 - Encapsulation in Python

    Encapsulation is one of the fundamental principles of object-oriented programming. It involves bundling data
    (attributes) and the methods that manipulate them into a single unit (the class) and controlling access to this
    data from outside the class.

    **Definition/Concept: Public and Private attributes in Python:**
        Unlike languages like Java or C++, Python does not have a strict mechanism to define attributes or methods
        as "private" or "public." Instead, Python follows a naming convention to indicate the developer's intention
        regarding the usage of attributes and methods.

        *Public Attributes and Methods:**
          Named normally, without an underscore.
          Example: `self.attribute`, `def method(self):`
          These are considered part of the class's public interface.

        *"Private" Attributes and Methods (by convention):**
          Prefixed with a single underscore `_`.
          Example: `self._attribute`, `def _method(self):`
          This indicates that these elements are intended for internal use and should not be accessed directly from
          outside the class. This convention is based on trust; technically, these elements remain accessible.

        *Name Mangling for Attributes and Methods:**
          Prefixed with a double underscore `__` (without an underscore at the end).
          Example: `self.__attribute`, `def __method(self):`
          Python applies "name mangling", i.e. it automatically changes of the attribute / method to include the class
          name making access from outside more difficult but not impossible.

    **Why:**
        Encapsulation helps in controlling access to data, providing flexibility to modify the internal implementation
        without affecting the code that uses the class, preventing accidental modifications to internal data, and
        improving code clarity by distinguishing between the public interface and implementation details.

    **When to use it:**
        Use encapsulation when you want to protect the internal state of an object and ensure that only the intended
        methods or functions can modify it.
        Use public methods (getters/setters) to control access to internal data if needed.
        Follow naming conventions (`_attribute` for internal use, `__attribute` for name mangling) to clearly indicate
        the intended use of attributes and methods.

    **Important Points to Remember:**
        Encapsulation in Python is based on conventions rather than strict restrictions.
        Attributes and methods prefixed with a single underscore `_` are considered internal to the class.
        The double underscore `__` triggers name mangling, making external access more difficult but not impossible.
        Encapsulation is a matter of design and programming discipline in Python.
"""


class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner  # Public
        self._balance = initial_balance  # "Private" by convention
        self.__transaction_history = []  # "Private" with name mangling

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__add_transaction(f"Deposit of {amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.__add_transaction(f"Withdrawal of {amount}")
            return True
        return False

    def get_balance(self):
        return self._balance

    def __add_transaction(self, transaction):
        self.__transaction_history.append(transaction)


# Usage
account = BankAccount("Someone", 1000)
print(account.owner)  # Access to a public attribute
account.deposit(500)
# The following lines are possible but not recommended:
print(account._balance)  # Access to a "private" attribute by convention
print(account.get_balance())  # Using a public method to access the balance

# print(account.__transaction_history)  # This will raise an AttributeError
print(account._BankAccount__transaction_history)  # Access to the attribute with name mangling



"""
## 1.9 - Inheritance in Python

    ** Definition/Concept ** 
        Inheritance is a pillar of Object-Oriented Programming (OOP). It allows a class to inherit features 
        (methods and properties) from another class. The class being inherited from is known as the parent class, 
        superclass or base class, and the class that inherits is known as the child class, subclass or derived class.

    ** Why and When to Use Inheritance **
        Inheritance is primarily used to enhance code reusability. Instead of writing repetitive code, common 
        features can be defined in a base class, and other classes can inherit these features. Inheritance should
        be used when there's a clear hierarchical relationship among classes. 
         
    ** Additional Properties **
        An additional feature of inheritance is that a subclass could be considered as the parent class in the code.
        When checking for the type of a subclass, the subclass will return true when we test the following equality:
        isinstance(bond, FinancialAsset) with bond an instance of the Bond class. However, a parent class could not
        be considered as a subclass. This principle is the class hierarchy principle

        
"""

"""
EXAMPLE : In finance, we deal with different types of financial instruments such as bonds and stocks. 
          Each of these instruments can be modeled as a class, inheriting from a base class `FinancialAsset`.

'Bond` and `Stock` classes inherit from the `FinancialAsset` class and add additional attributes specific to each 
instrument. They also contain respective financial computation methods.
"""


# Base Class
class FinancialAsset:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price


# Derived Class
class Bond(FinancialAsset):
    def __init__(self, symbol, price, face_value, maturity_date):
        super().__init__(symbol, price)
        self.face_value = face_value
        self.maturity_date = maturity_date

    def calculate_ytm(self):
        pass  # Implement YTM calculation logic here


# Derived Class
class Stock(FinancialAsset):
    def __init__(self, symbol, price, dividend_yield):
        super().__init__(symbol, price)
        self.dividend_yield = dividend_yield

    def calculate_pe_ratio(self):
        pass  # Implement Dividend Discount Model here


asset = FinancialAsset("USD", "1.0")  # create financial asset object
bond = Bond('T 5 15/09/2045', 100, 100000000, '2023-10-12')  # create bond object
print(f' is bond instance of Bond : {isinstance(bond, Bond)}')  # True
print(f' is bond instance of FinancialAsset : {isinstance(bond, FinancialAsset)}')  # True
print(f' is asset instance of Bond : {isinstance(asset, Bond)}')  # False



"""
## Multiple Inheritance in Python

    **Definition/Concept:**
        Python supports multiple inheritance, which means that a class can inherit from multiple parent classes.
        This allows a derived class to combine functionalities from several base classes.

    ** Syntax of Multiple Inheritance:**
        Python uses a straightforward syntax to define multiple inheritance by listing all parent classes
        in the parentheses after the class name.
"""


class BaseClass1:
    def method(self):
        print("Method in BaseClass1")


class BaseClass2:
    def method(self):
        print("Method in BaseClass2")


class DerivedClass(BaseClass1, BaseClass2):
    def method(self):
        print("Method in DerivedClass")
        BaseClass1.method(self)  # Direct call to A's method
        BaseClass2.method(self)  # Direct call to B's method


derived_class = DerivedClass()
derived_class.method()
# Outputs:
# Method in DerivedClass
# Method in BaseClass1
# Method in BaseClass2

"""
    **Practical Benefits of Multiple Inheritance:**
        Combining Functionality:
            Multiple inheritance allows a class to combine functionalities from different classes into one.
        Code Reuse from Multiple Sources:
            Useful when a class needs to inherit behaviors from several unrelated classes.
        Implementing Complex Designs:
            Enables creating more flexible and adaptable class structures.
"""


class BaseClass1Modified:
    def method_from_base_class_1_modified(self):
        print("Method from BaseClass1Modified")


class BaseClass2Modified:
    def method_from_base_class_2_modified(self):
        print("Method from BaseClass2Modified")


class DerivedClassModified(BaseClass1Modified, BaseClass2Modified):
    pass

derived_class_2 = DerivedClassModified()
derived_class_2.method_from_base_class_1_modified()
derived_class_2.method_from_base_class_2_modified()

"""
    **Method Resolution Order (MRO) in Detail**
        The Method Resolution Order (MRO) is crucial for understanding how Python handles inheritance, especially 
        multiple inheritance.

        The MRO defines the order in which Python searches for methods and attributes in a class hierarchy.

        This is particularly important in multiple inheritance scenarios where multiple parent classes may define 
        the same method.

        Python uses the C3 Linearization Algorithm to determine the MRO. This algorithm ensures that:
            - Subclasses appear before their parent classes.
            - The order of parent classes declared is preserved.
            - The MRO is monotonic (a class always appears before its parents).

        Understanding the MRO is crucial to:
            - Avoid name conflicts in multiple inheritance.
            - Understand the order in which methods are executed.
            - Design coherent and predictable class hierarchies.
"""

# Visualizing MRO:
# You can visualize the MRO of a class using the mro() method or the __mro__ attribute:
print(DerivedClass.mro())  # Displays the MRO for class DerivedClass

# output : [<class '__main__.DerivedClass'>, <class '__main__.BaseClass1'>, <class '__main__.BaseClass2'>, <class 'object'>]

# Detailed Example of Method Resolution: Example to illustrate how the MRO works:


class A:
    def method(self):
        print("Method in A")


class B(A):
    def method(self):
        print("Method in B")


class C(A):
    def method(self):
        print("Method in C")


class D(B, C):
    pass


d = D()
d.method()  # Outputs: Method in B

"""
# 4. Using super()

# Definition/Concept:
# The super() function is a powerful tool in Python for managing inheritance elegantly and flexibly.

# 4.1 Definition and Utility:

# Purpose of super():
# super() allows calling methods from the parent class in a derived class. It is particularly useful for:
# - Extending the behavior of a parent method without completely rewriting it.
# - Ensuring proper management of multiple inheritance.
"""


class Parent:
    def method(self):
        print("Method in Parent")


class Child(Parent):
    def method(self):
        super().method()  # Calls the method from the parent class
        print("Method in Child")


child = Child()
child.method()


# Outputs:
# Method in Parent
# Method in Child


# In the case of multiple inheritance, super() follows the order defined by the MRO:
class A:
    def method(self):
        print("Method in A")


class B(A):
    def method(self):
        print("Method in B")
        super().method()


class C(A):
    def method(self):
        print("Method in C")
        super().method()


class D(B, C):
    def method(self):
        print("Method in D")
        super().method()


d = D()
d.method()


# Outputs:
# Method in D
# Method in B
# Method in C
# Method in A

# Managing Parent Method Calls in Multiple Inheritance
# Direct Call to a Parent Class Method:  In some cases, you might want to call a specific parent class method directly
# rather than following the MRO:
class A:
    def method(self):
        print("Method in A")


class B:
    def method(self):
        print("Method in B")


class C(A, B):
    def method(self):
        print("Method in C")
        A.method(self)  # Direct call to A's method
        B.method(self)  # Direct call to B's method


c = C()
c.method()
# Outputs:
# Method in C
# Method in A
# Method in B

"""
## 1.10 - Polymorphism

    ** Definition/Concept **    
        Polymorphism is one of the four fundamental principles of Object-Oriented Programming (OOP). 
        In the context of programming, polymorphism allows us to use a single interface with different underlying forms. 
        This means that functions or classes can be used with many types of objects, and behave differently based on 
        the object's type.
        In simpler terms, polymorphism is the ability of an object to take on many forms, and it allows the programmer 
        to treat derived class members just like their parent class's members. This increases code reusability and 
        improves the efficiency of the code.

    ** Why to use it** 
        Polymorphism brings two major benefits:
        1. __Flexibility__: It allows developers to use the same function/entity name to mean different things in 
                            different contexts, making the code more flexible and easy-to-understand.
        2. __Reusability__: Polymorphism encourages reusability by accommodating different types and classes in the
                            same entity, or function. This reduces unnecessary code and makes it more efficient.

    ** When to use it **
        Polymorphism is useful when you have a list (or other collections) of objects that could be instances of 
        several different classes related through inheritance and you want to operate on them in the same way. 
        It's heavily used in "abstract factory" design patterns and it stands as a pillar in larger software 
        modularization.

"""

"""
EXAMPLE of polymorphism: 
Here, we have a `FinancialInstrument` class with a `get_description` method. We create child classes `CreditBond` and 
`Equity` each implementing the `get_description` method in different ways. Our main system only needs to call 
the `get_description` of a FinancialInstrument object and to get the detailed description at the subclass level
(i.e Equity and Bond class level)
"""


class FinancialInstrument:
    def __init__(self, symbol, price, currency):
        self.ticker = symbol
        self.price = price
        self.currency = currency

    def get_description(self):
        pass


class CreditBond(FinancialInstrument):
    def __init__(self, symbol, price, currency, face_value, maturity_date):
        super().__init__(symbol, price, currency)
        self.face_value = face_value
        self.maturity_date = maturity_date

    def calculate_ytm(self):
        pass  # Implement YTM calculation logic here

    def get_description(self):
        print(f'The ticker for this bond is {self.ticker} and its price is {round(self.price, 2)}. '
              f'The maturity date is {self.maturity_date}.The face value is paid {self.face_value}')


class Equity(FinancialInstrument):
    def __init__(self, symbol, price, currency, dividend_yield):
        super().__init__(symbol, price, currency)
        self.dividend_yield = dividend_yield

    def calculate_pe_ratio(self):
        pass  # Implement Dividend Discount Model here

    def get_description(self):
        print(f'The ticker for this equity is {self.ticker} and its price is {round(self.price, 2)}. '
              f'Dividend yield is {self.dividend_yield}')

from typing import List

instruments : List[FinancialInstrument] = [
        CreditBond(symbol='US10Y', price=95.5, currency='USD', face_value=100, maturity_date='2031-12-31'),
        Equity(symbol='AAPL', price=150.75, currency='USD', dividend_yield=0.0065),
        CreditBond(symbol='GB5Y', price=97.2, currency='GBP', face_value=100, maturity_date='2026-06-30'),
        Equity(symbol='GOOGL', price=2750.0, currency='USD', dividend_yield=0.0)
    ]

for instrument in instruments:
    instrument.get_description()


"""
Types of Polymorphism:
         Runtime Polymorphism (Dynamic):
            Achieved through method overriding
            Resolved at runtime

        Compile-time Polymorphism (Static):
            Achieved through method overloading
            Resolved at compile time

Method Overriding
    Method overriding is a fundamental aspect of runtime polymorphism. It occurs when a derived class (child class) 
    has a method with the same name and signature as a method in its base class (parent class).

    Key Points about Method Overriding:
        Same Name and Signature: The overriding method must have the same name and parameter list as the method in 
        the parent class.

    Runtime Decision: The method to be invoked is determined at runtime based on the object’s type.

    Extends or Modifies Behavior: Overriding allows a child class to provide a specific implementation of a method 
    that is already defined in its parent class.

    Polymorphic Behavior: It’s a key mechanism for achieving polymorphic behavior in OOP.

Method Overloading
    Method overloading is a fundamental aspect of compile-time polymorphism (static polymorphism). 
        It occurs when a class contains multiple methods with the same name but different parameter lists 
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


class Calculator:
    def add(self, *args):
        if len(args) == 2:
            # Adds two numbers
            return args[0] + args[1]
        elif len(args) == 3:
            # Adds three numbers
            return args[0] + args[1] + args[2]
        else:
            raise ValueError("Invalid number of arguments")


# Usage
calc = Calculator()
print(calc.add(5, 10))  # Output: 15
print(calc.add(5, 10, 15))  # Output: 30


# A more concrete example of method overloading
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
## 1.11 - Abstraction in Python

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
        By leveraging the ABCs, we can ensure that all classes that derive from our abstract base class will adhere to 
        the same interface. This helps to improve the maintainability and readability of our code, as we can code 
        using the abstract base class knowing that certain methods will always be present in any subclasses.
        
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


class AnotherSubclass(AbstractClassExample):

    def mandatory_method(self):
        print("The subclass is implementing the mandatory method")


x = AnotherSubclass()
x.mandatory_method()

"""
Example : Implementation of a Strategy abstract class
"""

from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def generate_signals(self, data_for_signal_generation: dict):
        """
        Generate trading signals based on a series of prices.

        Parameters:
        - price_series: A dictionary with dates as keys and object containing the data needed as values.

        Returns:
        - A dictionary with dates as keys and signals as values.
        """
        pass


class MeanReversionStrategy(Strategy):

    def __init__(self, mean_reversion_window):
        self.mean_reversion_window = mean_reversion_window

    def generate_signals(self, price_series_for_mean_reverion_strategy):
        dates = list(price_series_for_mean_reverion_strategy.keys())
        signals = {}

        for i in range(self.mean_reversion_window, len(dates)):
            current_date = dates[i]
            past_t_prices = self._get_past_t_prices(price_series_for_mean_reverion_strategy, dates, i)
            mean_price = sum(past_t_prices) / self.mean_reversion_window

            signals[current_date] = self._determine_signal(price_series_for_mean_reverion_strategy[current_date],
                                                           mean_price)
        return signals

    def _get_past_t_prices(self, price_series, dates, idx):
        """Retrieve the past t prices for a given index."""
        past_t_prices = []
        for j in range(idx - self.mean_reversion_window, idx):
            past_t_prices.append(price_series[dates[j]])
        return past_t_prices

    def _determine_signal(self, current_price, mean_price):
        """Determine the trading signal based on the current price and mean price."""
        if current_price < mean_price:
            return 1  # Buy
        elif current_price > mean_price:
            return -1  # Sell
        return 0  # Hold


strategy = MeanReversionStrategy(mean_reversion_window=3)
price_data = {
    "2023-09-10": 100,
    "2023-09-11": 101,
    "2023-09-12": 99,
    "2023-09-13": 98,
    "2023-09-14": 102
}
signal_series = strategy.generate_signals(price_data)
print(signal_series)


"""
# Protocol in Python

    **Protocols**, introduced in Python 3.8, provide a way to define structural subtyping (often called “duck typing”).
     They allow you to define interfaces in a more flexible and Pythonic way compared to abstract base classes as
     you get ride of the principle of hierarchy.

    ## Key Concepts
        - **Structural Subtyping**: An object is considered a subtype if it has the required methods and attributes, 
                                    regardless of inheritance.
        - **No Runtime Enforcement**: Protocols are primarily used for static type checking and don’t enforce method 
                                      implementation at runtime.
        - **Flexibility**: Classes don’t need to explicitly inherit from a Protocol to be considered compatible.

    To use Protocols, you need to import them from the `typing` module:
"""

from typing import Protocol, List

class Tradable(Protocol):
    symbol: str

    def current_price(self) -> float:
        ...

"""
`Tradable` is a protocol that specifies any object with a `symbol` attribute of type `str` and a `current_price` 
method that returns a `float`.
The ... is the ellipsis literal in Python. It serves as a placeholder indicating that the method current_price is 
intentionally left without an implementation. This is commonly used in abstract base classes, interfaces, or protocols 
to define methods that subclasses or implementing classes must override.
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

def display_instrument_price(instrument: Tradable): # the function only accepts input variable that match the Tradable "type"
    print(f"The current price of {instrument.symbol} is ${instrument.current_price():.2f}")

ticker = Ticker("AAPL")
stock = Stock("AAPL", 150.0)
display_instrument_price(stock)  # Output: The current price of AAPL is $150.00

"""
Even though `Stock` doesn't inherit from `Tradable`, it is accepted by the `display_instrument_price` function 
because it has the required `symbol` attribute and `current_price` method.
"""

#Another Example
class Pricable(Protocol):
    def price(self) -> float:
        ...

class StockPricable:
    def __init__(self, symbol: str, price_per_share: float):
        self.symbol = symbol
        self.price_per_share = price_per_share

    def price(self) -> float:
        return self.price_per_share

from scipy.stats import norm

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

    def price(self):
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
print(f"Total Portfolio Value: ${total_value:.2f}") # Total Portfolio Value: $166.70


"""
                Part 2 : Non OOP concepts to have in mind when you write code or build a project
"""

"""
## 2.1 - PEP 8 : coding convention for Python code

Why do we used a coding convention ?
    - A consistent coding style is important for collaborative projects. When multiple developers work on the same
    codebase, varying styles can lead to confusion and decrease code maintainability. PEP 8 provides a foundation
    upon which developers can write code that is easily comprehensible by others.

Imports :
    - Always put imports at the top of the file.
    - Import standard libraries first, followed by third-party libraries, and then your own modules.
    - Standard libraries are the libraries that are included with Python, meaning when you install Python,
    these libraries are installed too. Example : math, datetime, json, ...
    - Third-party libraries are developed by individual developers or teams that are not affiliated with the
     official Python development team. Example: pandas, numpy, seaborn, sckit-learn, yfinance, ....
    - Tips : You can separate Built-in and third party libraries from your own module by a blank line

Naming convention:
    - Variables and function names should be lowercase, with words separated by underscores to improve
    readability. This style is known as "snake_case".
    - Constants are usually defined on a module/ class level and written in all capital letters with underscores
    separating words.
    - Class names should normally use the CapWords (also known as CamelCase) convention. Every word is capitalized
    and there are no underscores between words.
    - Like function names, method names and instance variables should be lowercase, with words separated by
    underscores to improve readability.

    Additional guidelines:
    - When naming variables, give them descriptive names so that individuals who didn't write the script can
    intuitively understand what the variable represents.
    - Try to avoid using names of built-in types or functions, such as str, list, or input.
    - In Python and in the context of PEP 8, a private variable in a class is typically indicated by a single
    leading underscore (example: "_variable"). This is more a convention than a strict rule.

Comments:
    - In-line comments (text after hash symbol #) should be separated by two space from the code
    - It is considered as best practise to put docstrings in your class, method and function.

Additional guidelines not in PEP 8:
    - Try to type your input variables and return variable in function and method as much as possible

You will find below a PEP 8 compliant code
"""

import pandas as pd  # Importing third-party libraries at the top

from exercise.s3.ressource.quote import Quote


class FinancialAssetPepCompliant:
    """
    docstring: A class to representing a financial asset for portfolio construction.

    Attributes
    ----------
    ticker : str
        The symbol representing the financial asset in the market.
    last_quote : Quote
        The most recent quote data for the asset.
    currency : str
        The currency in which the asset is quoted.
    history : list[Quote]
        Historical quotes of the asset.

    Methods
    -------
    update_price(new_quote: Quote):
        Updates the last quote and appends the previous last quote to history.
    populate_quote_history_from_df(df_data: pd.DataFrame):
        Populates the quote history from a DataFrame containing date and price data.
    quotes_to_dataframe() -> pd.DataFrame:
        Converts and returns the quotes history as a DataFrame.
    """

    def __init__(self, ticker, quote, currency):
        """
        Initializes the FinancialAsset instance with a ticker, quote, and currency.

        Parameters
        ----------
        ticker : str
            The symbol representing the asset in the market.
        quote : Quote
            The most recent quote data for the asset.
        currency : str
            The currency in which the asset is quoted.
        """
        self.ticker = ticker
        self.last_quote = quote
        self.currency = currency
        self.history = []

    def __str__(self):
        """
        Prints a description of the asset, including its ticker and last quote for end user.
        """
        print(f'The ticker for this asset is {self.ticker} '
              f'and its price is {self.last_quote.price} {self.currency}')

    def update_price(self, new_quote):
        """
        Updates the last quote and appends the previous last quote to history.

        Parameters
        ----------
        new_quote : Quote
            The new quote to update.
        """
        self.history.append(self.last_quote)
        self.last_quote = new_quote

    def populate_quote_history_from_df(self, df_data):
        """
        Populates the quote history from a DataFrame containing date and price data.

        Parameters
        ----------
        df_data : pd.DataFrame
            DataFrame containing historical date and price data.
        """
        dates = df_data.index.to_pydatetime().tolist()
        prices = df_data['Close'].tolist()
        self.history = [Quote(date, price) for date, price in zip(dates, prices)]

    def quotes_to_dataframe(self) -> pd.DataFrame:
        """
        Converts and returns the quotes history as a DataFrame.

        Returns
        -------
        pd.DataFrame
            DataFrame with Date as index and Price as column.
        """
        data = {
            "Date": [quote.date for quote in self.history],
            "Price": [quote.price for quote in self.history]
        }
        df = pd.DataFrame(data)
        df.set_index('Date', inplace=True)
        return df



"""
 ## 2.2 - Error Handling
 
**Python Exception Handling**

Exception Handling in Python: try, except, finally

 ** In-Depth Definition/Concept**
In Python, as with any programming language, errors are bound to happen in code.
These could be syntax errors made by programmers, or exceptions that arise during execution.
Exception handling is an essential aspect of programming that determines how a program reacts to unexpected errors
during its execution process. Python provides built-In exceptions that can handle various types of errors ranging from
dividing a number by zero, to calling a non-existent method.

To handle exceptions, Python uses three keywords: try, except, and finally.

- The `try` block lets you test a block of code for errors.
- The `except` block lets you handle the error.
- The `finally` block allows you to execute code, regardless of the result of the try and except blocks.

 ** Why use it **
Exception handling is a key aspect of coding in any language including Python.
It's essential for creating robust and fault-tolerant software applications. It offers a way to anticipate problems,
and provides a method of handling errors gracefully without causing crashes.

** When to use it  **
Exception handling should be used whenever there's a chance that an error could occur during the execution of your code.
This can be when you're interacting with files, making network requests, working with collections,
or undertaking many other common tasks.
"""


class ArithmeticClassUtil:

    @staticmethod
    def divide(a, b):
        try:
            division = a / b
        except ZeroDivisionError:
            print("You tried to divide by zero.")
            division = None
        finally:
            return division

    @staticmethod
    def divide_with_multiple_error_handling(a, b):
        try:
            division = a / b
        except ZeroDivisionError:
            print("You tried to divide by zero.")
            division = None
        except TypeError:
            if isinstance(a, str):
                a = float(a)
            if isinstance(b, str):
                b = float(b)

            if isinstance(a, float) and isinstance(b, float):
                division = a / b
            else:
                print("You tried to divide by a non number argument")
                division = None
        finally:
            return division


result = ArithmeticClassUtil.divide(10.5, 2.0)
print(result)
result1 = ArithmeticClassUtil.divide(10.5, 0.0)
print(result1)
# result2 = ArithmeticClassUtil.divide(10.5, "5.0") # this will generate an Error
result3 = ArithmeticClassUtil.divide_with_multiple_error_handling(10.5, "5.0")
print(result3)


"""
## 2.3 - if __name__ == "__main__":
    ### Definition/Concept
        In Python, the special built-in variable `__name__` is used to determine if a Python file is being run 
        as the main program or if it is being used as a module in another program. When a Python script is executed,
         `__name__` is set to `"__main__"` if the script is being run as the main program. If the file is being imported 
         as a module into another script, `__name__` is set to the name of the script/module.

    ### Why to Use It
        1. **Code Organization**: It helps in organizing code in a way that it can be both usable as a module and 
        can be run as a standalone script.

        2. **Avoiding Code Execution During Import**: Code under the `__name__ == "__main__"` block won't run when 
        the script is imported as a module, which is useful for preventing code execution when the functions or 
        variables from a script are required elsewhere.

        3. **Testing**: It provides a consistent location to put test code, allowing the file to act as its own 
        test suite.

    ### When to Use It
        1. **Creating Reusable Modules**: If you’re creating a Python script that you want to be usable as a 
        standalone program as well as a module which can be imported and used in other scripts.
        
        2. **Testing Code**: If you want to include test functions in your script that test its internal functionality,
         you might want to run these only when you run the script directly, not when it's imported.
        
        3. **Script Execution Control**: To have control over script execution, i.e., if you want some part of your 
        script to run only when it’s being used as the main program and not during import.

example:

``` ***code in comment to not block the overall script***
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
```
If you run this script directly, it will print "Hello, World!". If you import this script as a module in another 
script, it won’t print anything but the `greet` function will be available for use.
"""

"""
## 2.4 - List comprehension

**Definition/Concept**
    List comprehension is a concise way to create lists in Python. It consists of an expression followed by a `for`
    loop inside square brackets `[]` or '{}. This allows you to generate a new list / dict by applying an expression to 
    each item in an existing list (or other iterable).

    Syntax:     [expression for item in iterable if condition] for creating a list
                {expression which generate a dict for item in iterable if condition} for creating a dict

**Why to use it**
1. **Conciseness:** List comprehensions can make your code more compact and easier to read by reducing the number
                    of lines of code.
2. **Readability:** When used appropriately, list comprehensions can make your intention clear, emphasizing the
                    transformation or filtering of data.
3. **Performance:** In some cases, using list comprehension can be faster than equivalent loops due to internal
                    optimizations in Python.

**When to use it**
1. **Simple Transformations:** When you want to apply a simple transformation to each element in a sequence.
                                For instance, squaring each number in a list or converting each string in a list to
                                uppercase.
2. **Filtering:** When you want to select only certain items from an iterable based on some condition.
                  For example, getting only the even numbers from a list.
3. **Flattening:** When dealing with lists of lists or nested iterables and you want to flatten them.
                    For example, flattening a 2D matrix into a 1D list.

4. **Avoid Overcomplication:** While list comprehensions are powerful, they shouldn't be overused.
                                If the logic becomes too complex, it might be clearer to use traditional loops instead
                                to maintain readability.

It's essential to strike a balance. If a list comprehension becomes hard to read or understand, it might be better
to revert to a more traditional for-loop structure.
"""

"""
Example : simple transformation using list comprehension
"""

import math
from datetime import datetime, timedelta

prices = [100.5, 102.3, 98.7, 105.6]

log_returns_with_for_loop = []
for i in range(1, len(prices)):
    log_return = math.log(prices[i] / prices[i - 1])
    log_returns_with_for_loop.append(log_return)

log_returns = [math.log(prices[i] / prices[i - 1]) for i in range(1, len(prices))]

print('same output for log_returns: ' + str(log_returns == log_returns_with_for_loop))

"""
Example : filtering  using list comprehension
"""
daily_returns = {datetime.today() - timedelta(days=5): 0.02,
                 datetime.today() - timedelta(days=4): -0.01,
                 datetime.today() - timedelta(days=3): 0.03,
                 datetime.today() - timedelta(days=2): -0.015,
                 datetime.today() - timedelta(days=1): 0.04}

profitable_days_with_for_loop = []
non_profitable_days_with_for_loop = []
for k, v in daily_returns.items():
    if v > 0:
        profitable_days_with_for_loop.append((k, v))
    elif v < 0:
        non_profitable_days_with_for_loop.append((k, v))

profitable_days = [(k, v) for k, v in daily_returns.items() if v > 0]  # filtering example
non_profitable_days = [(k, v) for k, v in daily_returns.items() if v < 0]  # filtering example

print('same output for profitable_days: ' + str(profitable_days == profitable_days_with_for_loop))
print('same output for non_profitable_days: ' + str(non_profitable_days == non_profitable_days_with_for_loop))

"""
Example : flattening using list comprehension
"""

list_of_list = [
    [1, 0.5, 0.3],
    [0.5, 1, 0.4],
    [0.3, 0.4, 1]
]

flat_list_with_for_loop = []
for sublist in list_of_list:
    for item in sublist:
        flat_list_with_for_loop.append(item)

flat_list = [item for sublist in list_of_list for item in sublist]

print('same output for flat_list: ' + str(flat_list == flat_list_with_for_loop))

"""
                                    Part 3 : Dunder methods
"""

"""
## 3.1 - Overall definition
    **Definition/Concept**
        "Dunder" is short for "Double underscore" (__). Dunder methods are a set of predefined methods you can use to 
        enrich your classes in Python. You've already seen these special methods in previous chapters with the
        `__init__` method

    **Why**
        Dunder methods allow you to emulate the behavior of built-in types. For instance, to get the length of a 
        string you can call `len('string')`. But an empty class definition doesn't support this behavior out of the box.

   **When to use it**
        Use dunder methods when you want to define operator behavior on your custom classes or want to mimic built-in 
        Python behavior.

You can find a list of dunder methods in the additional resources directory 
"""


"""
## 3.2 - Use built-in functions for classes by implementing dunder methods

    **Definition/Concept**
        The dunder method for specifying the behavior of built-in Python functions like `len` or `str` involves 
        implementing specific, predefined methods within your class using double underscores (__). 
        Such methods include `__len__`, `__str__`, and others, which Python calls when built-in functions of the same 
        name are used on instances of your class. 

    **Why**
        Implementing these dunder methods enables your custom objects to behave similarly to built-in Python objects, 
        thereby making your classes more intuitive and easy to use for other developers. This can also help your 
        objects to adhere to established Python conventions and idioms. For instance, if you define a `__len__` method,
         developers will know they can use the `len()` function on instances of your class.

    **When to use it**
        Utilize dunder methods when:
        - You want your custom objects to have idiomatic behavior similar to built-in Python types (e.g., allowing the
         use of functions like `len()` and `str()` on your objects).
        - You are creating a class where the logical implementation of such methods makes sense. For example, if your 
        class represents a collection of objects, implementing `__len__` would be intuitive.
        - You want to create objects that can be used interchangeably with built-in types or that can take advantage 
        of Python's rich set of built-in functions.

    **How to implement it**
        - Define methods in your class with names matching the dunder methods, ensuring they accept the correct 
        parameters and return values that adhere to Python’s data model.
        - By defining these methods, you allow instances of your class to be used with `len(instance)` and `
        str(instance)`, providing behavior similar to built-in Python objects.
        - Always refer to the Python data model documentation to understand the expected behavior and return values 
        of these methods to ensure compatibility and idiomatic usage.

By adhering to this approach, you ensure that your custom classes are not only user-friendly but also adhere to the 
principles and conventions that Python developers expect.
"""

"""
Example of dunder method : __len__
    __len__(self) determines the “length” of your object, which allows you to use the len(obj) syntax.
    If we do not implement the dunder method, len(instrument_list) will return the following : Error: object of 
    type 'InstrumentList' has no len()
"""


class InstrumentList:
    def __init__(self, list_of_instrument):
        self.instruments: [FinancialAsset] = list_of_instrument

    def __len__(self):
        return len(self.instruments)


asset1 = FinancialAsset('AAPL', 178)  # create a Financial Asset object
asset2 = FinancialAsset('MSFT', 330)  # create a Financial Asset object
instrument_list = InstrumentList([asset1, asset2])
print(len(instrument_list))  # return 2


"""
## 3.2.1 -The __str__() method
    **Definition/Concept**:
        The `__str__()` method in Python is another "dunder" method associated with a class. It is meant to return a 
        string representation of an object which is intended to be informative and easily readable for end-users.

    **Why**:
        - To offer a "user-friendly" string representation of an object that can be used in various contexts like
         printing the object.
        - It is beneficial when you want a simple description of the object rather than an exhaustive or technical one, 
          as given by `__repr__()`.
        - The primary goal of the `__str__()` method is readability over unambiguity. 

    **When to use it**:
        - When you want to provide an intuitive and user-friendly string representation of an object for display 
        purposes, especially in user-facing applications.
        - When you are implementing print statements or logs where the technical details of an object 
        are not necessary.
        - When you call the built-in `str()` function on an object or use format string methods, the `__str__()` 
        method gets invoked. So, it's helpful to define it when you anticipate such use-cases for your custom objects.
"""


class FinancialAssetWithStrDunder:
    def __init__(self, ticker, price, currency):
        self.ticker: str = ticker
        self.price: float = price
        self.currency: str = currency

    def __str__(self):
        return f'The ticker for this asset is {self.ticker} and its price is {self.price} {self.currency}'


asset_str_dunder_example = FinancialAssetWithStrDunder('AAPL', 178, 'USD')
print(str(asset_str_dunder_example))


"""
## 3.2.2 - The __repr__() Method
    **Definition/Concept**:
        The `__repr__()` method in Python is a dunder method associated with a class.  
        It should return a string that looks like a valid Python expression and could be used to recreate an object with 
        the same properties.  Ideally, using `eval(repr(obj))` should produce an object equivalent to `obj`.
        
    **Why**:
        - To provide an "official" string representation of an object that is useful for debugging and development. 
        - The output of `__repr__()` is intended to be unambiguous and helps developers understand the properties of 
        the object.
        - While both `__str__()` and `__repr__()` methods in a class provide string representations, the former is for 
        end-users and should be readable, while the latter is primarily for developers and debugging.
        
    **When to use it**:
        - When you want to provide a detailed and unambiguous string representation of an object for debugging and
         logging.
        - When you want to ensure that there's a clear way to recreate the object from its string representation.
        
    Benefits of __repr__() when implementing complex Python framework:
        Traceability: In complex financial simulations or optimizations, you might be dealing with hundreds of 
                    instrument objects. If something goes wrong, having a clear __repr__() output can help you trace 
                    back to the exact instrument causing the issue.
    
        Reproducibility: Sometimes you may need to send the state of your system (the exact instruments and their 
                    properties) to someone else for verification, testing, or audit purposes. With a clear __repr__() 
                    method, you can recreate the exact state of objects with ease.
    
        Logging: When logging system activities, having a clear representation of the objects being processed can be 
                useful for future reference or debugging.
"""


class FinancialAssetWithDunderRepr:
    def __init__(self, ticker, price, currency):
        self.ticker: str = ticker
        self.price: float = price
        self.currency: str = currency

    def __str__(self):
        return f'The ticker for this asset is {self.ticker} and its price is {self.price} {self.currency}'

    def __repr__(self):
        return f"FinancialAssetWithDunderRepr(ticker='{self.ticker}', price={str(self.price)}, currency='{self.currency}')"


asset_str_dunder_example = FinancialAssetWithDunderRepr('AAPL', 178, 'USD')
print(repr(asset_str_dunder_example))

assetExampleEval = eval(repr(asset_str_dunder_example))
# eval() convert an "official" string representation of an object to the object. Here we create a new object.
print(str(asset_str_dunder_example))  # This new object is an instance of FinancialAssetWithDunderRepr


"""
## 3.3 - Operator overloading
    
    Built-in operator does not work on custom classes. For example, if we try to use "+" or any other operator such as
    "-", "*", "/", ">", ... this will raise a TypeError as the behavior for these operators are not implemented for the
    object. If we want to use built-in operator for custom objects we need to use dunder methods.
    The only exception is the "=" operator. If we don't implement the dunder method to specify the behavior of the
    equal operator for custom objects, python will check for object identity (i.e., both objects are the
    same instance). Thus even though each attributes of 2 objects are equal the "=" will return false
    
    Implementing dunder methods referring to built-in operator is called operator overloading. 
    **Definition/Concept**: 
        It is the ability of one operation, such as addition or multiplication, to behave in one way or more 
        according to the data or objects being operated upon.
    
    **Why**: 
        Operator overloading is used to make programming more intuitive and the code more user friendly,
        behaving like they would with built-in types.
    
    **_When to use `Operator Overloading`_**: 
        Operator overloading is used when you want to specify more than one meaning to an operator or apply specific 
        operation
        
    You will find below example of operator overloading. 
"""

"""
Example of operator overloading for "+" and "-" operator
Here the operator overloading is realized by implementing the following method : __add__ and __sub__

When we try to add up an object to a BankAccount type object with the "+" operator the __add__ method is called. 
The method checks if the object we try to add up to the first element of the addition is a BankAccount instance. If it's
the case it modify the current balance of the first element and return the updated amount. If it's not the case, 
it will not perform any operation. 

When implementing dunder method for operator overloading, we can specify multiply behavior which will depend on the 
type of the object. If we look at the __sub__ method, the object we try to subtract the first element with could be a 
BankAccount instance or a FinancialInstrument with the same currency than the bank account. If it's the case it modify 
the current balance of the first element and return the updated amount. If it's not the case, it will not perform any 
operation. 
"""


class BankAccount:
    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency

    def __add__(self, other):
        if isinstance(other, BankAccount) and other.currency == self.currency:
            self.balance = self.balance + other.balance
            return self.balance

        if isinstance(other, FinancialInstrument) and other.currency == self.currency:
            self.balance = self.balance + other.price
            return self.balance

    def __sub__(self, other):
        if isinstance(other, BankAccount) and other.currency == self.currency:
            self.balance = self.balance - other.balance
            return self.balance

        if isinstance(other, FinancialInstrument) and other.ticker == self.currency:
            self.balance = self.balance - other.price
            return self.balance


acc1 = BankAccount('Account 1', 1200, 'USD')
acc2 = BankAccount('Account 2', 800, 'USD')

print(acc1 + acc2)  # 2000
print(acc1 - acc2)  # 400

asset = FinancialInstrument('USD', 300, 'USD')
print(acc1 + asset)  # 1500

"""
Example of the dunder method __eq__()
"""

class FinancialAssetWithNoDunderEq:
    def __init__(self, ticker):
        self.ticker: str = ticker


print('test equality for object with no __eq__() implementation')
asset = FinancialAssetWithNoDunderEq('AAPL')
asset1 = FinancialAssetWithNoDunderEq('AAPL')
print(f'is object with same attributes equal : {asset == asset1}') #false


class FinancialAssetWithDunderEq:
    def __init__(self, ticker):
        self.ticker: str = ticker

    def __eq__(self, other):
        # First, ensure that the other object is an instance of the same class
        if isinstance(other, FinancialAssetWithDunderEq):
            return self.ticker == other.ticker
        return False  # Return False for types that are not of the same class


asset_eq_dunder_example = FinancialAssetWithDunderEq('AAPL')
asset_eq_dunder_example1 = FinancialAssetWithDunderEq('AAPL')
asset_eq_dunder_example2 = FinancialAssetWithDunderEq('MSFT')
print('__eq__() example')
print(f'asset_eq_dunder_example = FinancialAssetWithDunderEq("AAPL") //'
      f' asset_eq_dunder_example1 = FinancialAssetWithDunderEq("AAPL") //'
      f' asset_eq_dunder_example2 = FinancialAssetWithDunderEq("MSFT")')
print(' ')
print(f'asset_eq_dunder_example == "AAPL": {asset_eq_dunder_example == "AAPL"}')  # False
print(f'asset_eq_dunder_example == asset_eq_dunder_example1: {asset_eq_dunder_example == asset_eq_dunder_example1}')  # true
print(f'asset_eq_dunder_example == asset_eq_dunder_example2 : {asset_eq_dunder_example == asset_eq_dunder_example2}')  # false


"""
## 3.4 - Custom properties and behavior definition

Another type of dunder methods allow us to modify the behavior of object when we interact with them. We could divide
this type of dunder method into 4 sub categories:
    Object Life Cycle:
        - `__new__(cls, *args, **kwargs)`: 
           - Called to create a new instance of the class.
        - `__del__(self)`: 
           - Called when the object is about to be destroyed.
           
    Descriptors (manage object attributes through their definition in classes):
        - `__get__(self, instance, owner)`: 
           - Called to get the attribute of the owner class.
        - `__set__(self, instance, value)`: 
           - Called to set the attribute of the instance.
        - `__delete__(self, instance)`: 
           - Called to delete an attribute.
           
    Attribute Access:
        - `__getattr__(self, name)`: 
           - Called when an attribute lookup is not found in the object.
        - `__getattribute__(self, name)`: 
           - Called unconditionally to retrieve an attribute.
        - `__setattr__(self, name, value)`: 
           - Called when trying to assign a value to an instance attribute.
        - `__delattr__(self, name)`: 
           - Called when an attribute is deleted.

    Item Access and Assignment (for collections, e.g., lists, dictionaries):
        - `__getitem__(self, key)`: 
           - Called to retrieve the value associated with the provided key.
        - `__setitem__(self, key, value)`: 
           - Called to set the value for the provided key.
        - `__delitem__(self, key)`: 
           - Called to delete the value associated with the provided key.

Usage Contexts:
    - **Object Life Cycle Methods**: Enable control during object instantiation and destruction.
    - **Attribute Access Methods**: Allow defining behaviors for attribute access, setting, and deletion.
    - **Item Access Methods**: Provide a way to customize how items in a collection are accessed, set, and deleted.
    - **Descriptor Methods**: Enable creating objects that can manage the attributes of other objects.

Use Cases:
    - **Enhance Usability and Readability**: Provide a Pythonic interface to your classes (e.g., enabling iteration, 
    context management).
    - **Resource Management**: E.g., using `__del__` to release resources or `__setattr__` to update related object 
    states.
    - **Custom Containers**: Utilize `__getitem__` and related methods to create custom collection classes.
    - **Data Wrangling and Validation**: Using `__set__` or `__setattr__` to enforce types or constraints on attribute 
    values.
"""



"""
                                Part 4 : Additional OOP Concepts
"""


"""
## 4.1 - Decorators
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

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)

date = Date.from_string("2024-07-29")
print(date.year)  # Output: 2024


"""
## Class-based Decorator
    ** **Definition/Concept** 
    Class-based decorators leverage the power of objects to hold state or utilize inheritance for related decorator 
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

"""
Example: Class based decorator applied to trade logging execution
An `Order` object is instantiated with details about a trade and stored in the `order` variable.
Then TradeExecutionService.execute_trade(order)` is called:
    1. Internally, `TradeLogger` is called first (due to the decorator). It wraps the original `execute_trade` 
    function with additional functionality (logging).
    2. The wrapped function executes the original `execute_trade` function, retrieves the trade details, logs them, 
    and then returns the trade details.

In-depth code explanation for `TradeLogger`
    - `__init__(self, log_file='trade_log.txt')`:
        - Initializes the logger with a file path (`log_file`), where trade execution details will be logged.
        - `log_file` defaults to 'trade_log.txt' if no argument is provided.
    
    - `__call__(self, execute_trade_func)`:
        - Allows the class instance to be called as a function.
        - Accepts `execute_trade_func` which should be a function executing a trade.
        - Returns a `wrapper` function that enhances `execute_trade_func` with logging functionality.
    
    - `wrapper` Function (Nested inside `__call__`):
        - Takes any positional (`*args`) and keyword (`**kwargs`) arguments.
        - Executes the trade function `execute_trade_func` and stores the result in `trade_result`.
        - Logs the trade details to a file (specified by `self.log_file`):
            - Appends the date, a descriptive message, and `trade_result` to the log file.
        - Returns `trade_result`.

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
order = Order('FP FP Equity', -1000, "limit", price_limit=99.95)
trade_details = TradeExecutionService.execute_trade(order)


"""
## 4.2 - static method

     ** Definition/Concept** 
        Static methods in python are a special kind of method which are created within a class for helping 
        purposes.They don't know anything about class state. They are used to perform utility tasks, and they can't 
        modify class or instance state.

    ** Why to use it** 
        Static methods are a way of putting methods in a class (to keep all the related functions together),  without 
        needing the class or instance around.

    **   When to use it   ** 
        Use a static method when you don't require access to an instance or any of its attributes or when you're 
        not going to modify the class or instance state.
"""

"""
Example : We can take the MeanReversionStrategy previously implemented and modify it to make the relevant method
static.
If we look at this example one method could be switch to static: _determine_signal. When we want to make a function
static, we first need to put the decorator 'staticmethod' above it and delete the 'self' input argument. As a static 
method does not modify the state of an object, the self argument is useless. Using static method is not mandatory in 
python but this is considered as a best practice. 
"""


class MeanReversionStrategyWithStaticMethod(Strategy):

    def __init__(self, mean_reversion_window):
        self.mean_reversion_window = mean_reversion_window

    def generate_signals(self, price_series):
        """ generate signals for the mean reversion strategy"""
        dates = list(price_series.keys())
        signals = {}

        for i in range(self.mean_reversion_window, len(dates)):
            current_date = dates[i]
            past_t_prices = self._get_past_t_prices(price_series, dates, i)
            mean_price = sum(past_t_prices) / self.mean_reversion_window

            signals[current_date] = self._determine_signal(price_series[current_date], mean_price)

        return signals

    def _get_past_t_prices(self, price_series, dates, idx):
        """Retrieve the past t prices for a given index."""
        past_t_prices = []
        for j in range(idx - self.mean_reversion_window, idx):
            past_t_prices.append(price_series[dates[j]])
        return past_t_prices

    @staticmethod
    def _determine_signal(current_price, mean_price):
        """Determine the trading signal based on the current price and mean price."""
        if current_price < mean_price:
            return 1  # Buy
        elif current_price > mean_price:
            return -1  # Sell
        return 0  # Hold


"""
## 4.3 - class method

    ** Definition/Concept** 
        Class methods in python are methods that are bound to the class and not the instance of the object. 
        These types of methods can't modify the instance state. They are marked by the decorator `@classmethod`.

    ** Why to use it** 
        Class methods handle tasks that can be carried out only by the class, not by any specific instance. 

    **   When to use it  ** 
        class methods are used to create functions that are aware of and can modify class-level details, 
        regardless of a specific instance of the class.

"""

"""
Example of a class method usage
"""


class BankAccountWithInterestRate:
    interest_rate = 0.02  # Example: 2% annual interest

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    @classmethod
    def get_interest_rate(cls):
        return cls.interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate


account = BankAccountWithInterestRate(1000)  # Create an account with an initial balance of 1000
account2 = BankAccountWithInterestRate(5000)  # Create an account with an initial balance of 5000

# Use class method to get the interest rate
print(f"Current interest rate: {BankAccountWithInterestRate.get_interest_rate() * 100}%")

# This operation could also be requested at instance level
print(f"Current interest rate: {account.get_interest_rate() * 100}%")

# Use class method to set the interest rate
BankAccountWithInterestRate.set_interest_rate(0.03)  # Update the interest rate to 3%
print(f"New interest rate: {BankAccountWithInterestRate.get_interest_rate() * 100}%")

# When we modify the interest rate, the modification is applied to all instance
print(f"New interest rate for account: {account.get_interest_rate() * 100}%")
print(f"New interest rate for account2: {account.get_interest_rate() * 100}%")

# Add interest to the account balance
account.add_interest()
print(f"New balance after interest: ${account.balance:.2f}")


"""
## 4.4 - dataclass
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
### 4.5 - utility class

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


class PerformanceAnalysisUtils:

    @staticmethod
    def compute_returns(prices_df: pd.DataFrame, column_name: str) -> pd.Series:
        """
        Computes the returns from prices.

        :param prices_df: Dataframe containing prices
        :param column_name: Name of the column containing prices
        :return: A Series containing returns
        """
        return prices_df[column_name].pct_change().dropna()

    @staticmethod
    def compute_sharpe_ratio(prices_df: pd.DataFrame, risk_free_rate: float, column_name: str) -> float:
        """
        Computes the Sharpe Ratio for a given set of prices and risk-free rate.

        :param prices_df: Dataframe containing prices
        :param risk_free_rate: Annual risk-free rate as a decimal (e.g., 0.03 for 3%)
        :param column_name: Name of the column containing prices
        :return: Sharpe Ratio
        """
        # Calculate daily returns
        returns = PerformanceAnalysisUtils.compute_returns(prices_df, column_name)

        # Convert annual risk-free rate to daily rate assuming 252 trading days
        daily_rf = (1 + risk_free_rate) ** (1 / 252) - 1

        # Calculate Sharpe Ratio
        excess_return = returns - daily_rf
        sharpe_ratio = excess_return.mean() / returns.std()

        return sharpe_ratio * math.sqrt(252)


data = {'price': [100, 97, 95, 99.97, 100.5]}
df = pd.DataFrame(data)
risk_free_rate = 0.03
sharpe_ratio = PerformanceAnalysisUtils.compute_sharpe_ratio(df, risk_free_rate, 'price')
print(f'sharpe ratio: {sharpe_ratio}')


"""
## 4.6 - Factory

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
            return StockCreatedThroughFactoryExample(**kwargs)
        elif instrument_type.lower() == "bond":
            return BondCreatedThroughFactoryExample(**kwargs)
        else:
            raise ValueError("Invalid financial instrument type")


class StockCreatedThroughFactoryExample:
    def __init__(self, ticker, price):
        self.ticker = ticker
        self.price = price

    def get_market_value(self):
        return f"The market value of {self.ticker} is ${self.price} per share."


class BondCreatedThroughFactoryExample:
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


"""
## 4.7 - custom exception
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
    of error in our code. For every unique situation, we can create a new exception class and then catch it in our code. 
    When we are building a large Python application, it's a good practice to define our own exception class.

The primary goal is often just to provide a unique type that can be caught and handled separately from other types of 
exceptions. When creating a custom exception class, it's not always necessary to add additional methods or attributes 
to the class. If no extra functionality is needed, and the sole purpose is to provide a distinct exception type, 
then the body of the class can be left empty.
"""

"""
Example: create Exception when particular behavior happened during execution, application to Updating quote for the
FinancialAsset object
"""


class NegativePriceException(Exception):
    """ Raised when the price of a financial asset is negative """
    pass


class QuoteCustomExceptionExample:
    def __init__(self, date: datetime, price: float):
        self.date = date
        self.price = price

    def __repr__(self):
        return f"Quote(date={self.date!r}, price={self.price!r})"


class FinancialAssetCustomExceptionExample:
    def __init__(self, ticker, quote, currency):
        self.ticker: str = ticker
        self.last_quote: Quote = quote
        self.currency: str = currency
        self.history: [Quote] = []

    def update_last_quote(self, new_quote: QuoteCustomExceptionExample):
        try:
            DataQualityUtils.check_quote_for_asset(self, new_quote)
            self.history.append(self.last_quote)
            self.last_quote = new_quote
        except NegativePriceException as price_exception:
            print(str(price_exception))
            print("Quote has not been updated")


class DataQualityUtils:
    @staticmethod
    def check_quote_for_asset(asset: FinancialAssetCustomExceptionExample, new_quote: QuoteCustomExceptionExample):
        if new_quote.price < 0:
            raise NegativePriceException(f"quote: {repr(new_quote)} for updating asset {asset.ticker} is negative.")


last_date, last_close = datetime.today(), -175.0
equity_last_quote1 = QuoteCustomExceptionExample(last_date, last_close)
equity = FinancialAssetCustomExceptionExample('AAPL', equity_last_quote, 'USD')
equity.update_last_quote(equity_last_quote1)


"""
## 4.7 Descriptors : Descriptors provide a way to customize attribute access in Python classes. 
    A descriptor is a special type of object in Python that customizes the behavior of attribute access (getting, 
    setting, and deleting). To implement a descriptor, you define a class that implements any of these methods:

        __get__(self, obj, objtype): Called when you retrieve the attribute (i.e., when you access instrument.volatility).

        __set__(self, obj, value): Called when you assign a value to the attribute (i.e., financialasset.price = value).

        __delete__(self, obj): (optional) Called when you delete the attribute.
        Descriptors are especially useful when you want to add validation, logging, or specific behavior during 
        attribute access or modification, which is what we're doing in this example with volatility.

"""


class PriceDescriptor:
    def __init__(self, name):
        self.name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if value < 0:
            raise ValueError("Price below zero should not be possible")
        setattr(obj, self.name, value)


class FinancialAsset:
    price = PriceDescriptor("price")

    def __init__(self, ticker: str, price: float):
        self.ticker = ticker
        self.price = price


# Usage
asset = FinancialAsset("AAPL", 250)
print(asset.price)
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
    '/Users/benjaminmat/Desktop/oop_272_dauphine_2024/theory/additional_resources/Built-in error in python.txt')
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


a = SingletonExample()
b = SingletonExample()

print(a == b)  # Output: True



"""
## 4.10 - unit test
     ** Definition/Concept** 
        Unit testing is a method of software testing that checks whether individual components of the source code work
         as expected. In Python, `unittest` is a built-in module for testing units of code.
        
     ** Why to use it** 
        The `unittest` module provides a rich set of tools for constructing and running tests, helping you ensure your 
        code behaves as expected, which is crucial for building reliable applications.
        
    **  When to use it ** 
        Use `unittest` whenever you write new code and want to verify its behavior or when you refactor or modify 
        the existing code to ensure its behavior hasn't changed unexpectedly.
        When you launch a unit test, a test session will start. For each unit test the result will be 'Passed' 
        if the unit test has the expected behavior. If not the result will be 'Failed'. 
        Typically, we try to regroup all the unit test in one directory or one script. If you are implementing a 
        complex or large project you might want to use several script to do you unit test, each script checking one
        part of your project. If you want to run all the unit test of your script you can use the following code : 
        'unittest.main()'. If you plan to doing so, your script should implement the 'if __name__ == "__main__":'
        logic. Unit test should always be implemented in a seperate script
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

def square(n):
    return n**2


import unittest


class TestSquareFunction(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(square(2), 4)

    def test_zero(self):
        self.assertEqual(square(0), 0)


""" *** Output of unit test in the Pyhton Console **
============================= test session starts ==============================
collecting ... collected 2 items

all_classes_extended_version.py::TestSquareFunction::test_positive_number 
all_classes_extended_version.py::TestSquareFunction::test_zero 

============================== 2 passed in 1.15s ===============================

Process finished with exit code 0
PASSED [ 50%]PASSED    [100%]
"""



"""
## 5.1 Understanding Python Imports and Project Structure

The Python Import System
Python’s import system is fundamental to how we organize and use code across multiple files and directories.
Understanding it is crucial for structuring projects effectively.

When Python executes a file, it builds sys.path (the module search path).
When you use an import statement, Python searches for the module in several locations:
    The directory containing the script
    PYTHONPATH (if set)
    Standard library directories
    Site-packages directory (for installed third-party packages)

Understanding PATH and PYTHONPATH
    PATH:   An environment variable that tells the operating system where to look for executables. 
            It’s not directly related to Python imports but is important for running Python from the command line.

    PYTHONPATH: An environment variable that you can set to add additional directories where Python will look for 
                modules and packages.


Importing from the Current Directory 
    To import modules from the current directory, you have several options: 
        Run Python from the directory containing your modules:
            if the current directory is your python project you can run it directly with this command line: 
                python my_script.py
                ==> The script’s directory is added to sys.path, so import my_module works

        Add the current directory to PYTHONPATH :
            # macOS/Linux
            export PYTHONPATH="$PWD${PYTHONPATH:+:$PYTHONPATH}"

            # PowerShell (Windows)
            $env:PYTHONPATH = (Get-Location).Path + [IO.Path]::PathSeparator + $env:PYTHONPATH

            ==> running this command line will add the directory in the python path
            ==> Environment variable entries will be added to sys.path for every Python run.
            Pros:   Works no matter where you run Python from; easy for quick experiments.
            Cons:   Global and brittle. It can mask import errors, cause conflicts between projects, and behave 
                    differently on coworkers’ machines/CI.
            ==> if you want to clear your PYTHONPATH you can use the following command : unset PYTHONPATH
            ==> if you want to see your import path you can use the following command : python -c "import sys, pprint; pprint.pp(sys.path)"
            ==> if you have a script inside a directory in a python path you can run it from everywhere using : python -m script_name


        Modify sys.path in your script:
            import sys
            import os
            sys.path.append(os.path.dirname(os.path.realpath(__file__)))

            ==> running this command line will also add the directory in the python path
            ==> these command line are insert in python script. 
            ==> It dynamically inserts the script’s directory into the import path at runtime, allowing python to 
            look in specific directory.
"""

"""
Importing Modules vs Specific Items
    When importing in Python, it’s important to understand the difference between importing entire modules and 
    importing specific items from modules. This distinction affects not only how you use the imported elements but 
    also how Python executes the import process.

    Importing a module:
        import mymodule
        mymodule.my_function()

    Importing specific items:
        from mymodule import my_function
        my_function()

    Key points to understand:
        Module Execution: When you import a module (either the entire module or specific items), Python first executes 
        the entire module from top to bottom. This happens regardless of whether you’re importing the whole module or 
        just specific functions or classes.

    Namespace Differences:
        When importing the entire module, you need to use the module name as a prefix to access its contents 
        (e.g., mymodule.my_function()).
        When importing specific items, they are brought directly into the current namespace, allowing you to use 
        them without the module prefix (e.g., my_function()).

    Import Process:
        For import mymodule:
            Python executes all code in mymodule.
            It creates a namespace for mymodule in the current scope.
            You access items through this namespace (e.g., mymodule.my_function()).

        For from mymodule import my_function:
            Python executes all code in mymodule.
            It locates my_function within mymodule.
            It creates a reference to my_function in the current namespace.

    Performance and Memory:
        Importing specific items doesn’t save on initial execution time or memory, as the entire module is still executed.
        However, it can make your code slightly faster when accessing the imported items, as there’s no need to go 
        through the module namespace.

    Potential Pitfalls:
        Importing specific items can lead to naming conflicts if you import items with the same name from different 
        modules.
        It can also make it less clear where a function or class is coming from when reading the code.

    Relative imports use dots to refer to the current and parent packages:
            from . import sibling_module => look in the current package for the import
            from .. import parent_package_module => look in the parent package for the import

    Generally, absolute imports are preferred for clarity and to avoid confusion
"""

"""
Viewing the Module Search Path
    You can view the current module search path in python using:
        import sys
        print(sys.path)
"""

"""
Best Practices for Directory Layout

    A well-organized project structure enhances readability and maintainability. Here’s a common layout:

            my_project/
            │
            ├── my_package/
            │   ├── __init__.py
            │   ├── module1.py
            │   └── module2.py
            │
            ├── tests/
            │   ├── test_module1.py
            │   └── test_module2.py
            │
            ├── docs/
            │   └── index.md
            │
            ├── pyproject.toml
            └── README.md

Note: Some projects use a src/ directory (e.g., src/my_package/) to separate package code. 
While this can be beneficial for larger projects or when building distributions, it’s not mandatory and can add 
complexity for smaller projects.

            my_project/
            │
            ├── src/
            │   └── my_package/
            │       ├── __init__.py
            │       ├── module1.py
            │       └── module2.py
            │
            ├── tests/
            │   ├── test_module1.py
            │   └── test_module2.py
            │
            ├── docs/
            │   └── index.md
            │
            ├── pyproject.toml
            └── README.md


Key Idea : Separating Source Code, Tests, and Documentation
    Source Code (my_package/): Contains the actual package code
    Tests (tests/): Keeps tests separate from source code
    Documentation (docs/): Separates documentation from code
    Project Files: pyproject.toml for project configuration
    README.md for project overview


"""

"""
example to run through shell

# Create project directory
mkdir my_project
cd my_project

# Create package directory
mkdir my_package
touch my_package/__init__.py
touch my_package/module1.py

# Create tests directory
mkdir tests
touch tests/test_module1.py

# Create docs directory
mkdir docs
touch docs/index.md

# Create project files
touch pyproject.toml README.md

"""

"""
The Role of __init__.py
    The __init__.py file marks a directory as a Python package. It can be empty or contain initialization code. 
    When you import a package, the __init__.py file is executed.

    __init__.py Example: Simplifying imports for package users:
    # mypackage/__init__.py
    from .database import Database
    from .models import User, Product
    from .utils import format_currency

    __all__ = ['Database', 'User', 'Product', 'format_currency']

    This allows users to do:
    from mypackage import Database, User, Product

    Instead of:
    from mypackage.database import Database
    from mypackage.models import User, Product

Initializing package-level resources example:
"""

import logging
import os
from pathlib import Path
from logging.handlers import RotatingFileHandler

DEFAULT_LOG_FILE = os.getenv("MY_PACKAGE_LOG_FILE", str(Path.cwd() / "my_package_log.txt"))

logger = logging.getLogger(__name__)  # use a stable, package-wide name
logger.setLevel(logging.INFO)

_formatter = logging.Formatter(
    "%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(message)s"
)


def _add_file_handler(log_file: str):
    """Attach a rotating file handler if not already present for this file."""
    abs_target = os.path.abspath(log_file)
    for h in logger.handlers:
        if isinstance(h, RotatingFileHandler) and getattr(h, "baseFilename", "") == abs_target:
            return  # already attached for this file

    Path(abs_target).parent.mkdir(parents=True, exist_ok=True)
    fh = RotatingFileHandler(abs_target, maxBytes=1_000_000, backupCount=5, encoding="utf-8")
    fh.setFormatter(_formatter)
    logger.addHandler(fh)


def _add_console_handler():
    """Attach one console handler (optional; nice during dev)."""
    if not any(isinstance(h, logging.StreamHandler) and not isinstance(h, RotatingFileHandler)
               for h in logger.handlers):
        ch = logging.StreamHandler()
        ch.setFormatter(_formatter)
        logger.addHandler(ch)


# Initialize package-wide configurations
CONFIG = {
    "PACKAGE_VERSION": "v1",
}


def initialize(log_file: str = DEFAULT_LOG_FILE, console: bool = True):
    """
    Initialize logging to a rotating .txt file (and optionally console).
    You can override the file path here or via the MY_PACKAGE_LOG_FILE env var.
    """
    _add_file_handler(log_file)
    if console:
        _add_console_handler()
    logger.info(f"Initializing my_package {__name__}")
    # Perform any startup tasks here


# Call initialize on import if you want immediate file logging:
initialize()

"""
logging is a Python’s built-in, flexible system for writing messages about what your code is doing for debugging and 
production monitoring, without using print() everywhere.

| Term          | Meaning                                                  | Example                                               |
| ------------- | -------------------------------------------------------- | ----------------------------------------------------- |
| **Logger**    | Entry point where your code writes log messages.         | `logging.getLogger(__name__)`                         |
| **Level**     | Severity of a message; controls what gets recorded.      | `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`       |
| **Handler**   | Decides *where* logs go.                                 | Console, file, syslog, HTTP, etc.                     |
| **Formatter** | Decides *how* logs look.                                 | `"%(asctime)s %(name)s [%(levelname)s]: %(message)s"` |


Version information and metadata:
    # mypackage/__init__.py

    __version__ = "1.0.0"
    __author__ = "Your Name"
    __license__ = "Dauphine"

    # You can even load version from a separate file
    from .version import __version__
    The file should be named __version__.py
"""

"""
Import Order and Behavior
    Python first looks for built-in modules.
    If not found, it searches in the directories listed in sys.path.
    For a package, Python executes the __init__.py file.
    For a module, Python executes the entire file.

    Importing Modules vs Specific Items
        Importing a module:
            import mymodule
            mymodule.my_function()

    Importing specific items:
        from mymodule import my_function
        my_function()

    Importing the entire module executes it but requires using the module name as a prefix. 
    Importing specific items brings them directly into the current namespace.

"""

""" 
Avoiding Circular Imports
    Circular imports occur when two modules import each other, directly or indirectly. 
    Here’s a realistic example and how to resolve it:

    Project structure:

    myproject/
    ├── __init__.py
    ├── models.py
    ├── services.py
    └── utils.py

    # models.py
    class User:
        def __init__(self, username):
            self.username = username

        def get_data(self):
            return DataService.fetch_user_data(self.username)

    # services.py
        from .utils import format_data

        class DataService:
            @staticmethod
            def fetch_user_data(username):
                # Simulate fetching data
                data = {username: "some data"}
                return format_data(data)

            @staticmethod
            def create_user(username):
                return User(username)

    # utils.py
        def format_data(data):
            return str(data).upper()

    This creates a circular import between models.py and services.py. 

    When you do:
        import models

    Python does three things:
        Checks if "models" is already in sys.modules.
        If not, creates an empty module object (sys.modules['models'] = <module 'models'>).
        Executes the code in models.py top to bottom, filling in that empty module with functions, classes, etc.

    If that module imports another one at the top level, Python repeats this process recursively.

    In our case we have this dependency graph:
        models.py ──imports──▶ services.py
        services.py ──imports──▶ models.py

    When Python tries to import models:
        models starts executing.
        It reaches from .services import DataService.
        Python sees services isn’t loaded yet → creates an empty module for it and starts executing services.py.
        But inside services.py, it sees from .models import User → tries to import models again.
        This time, models is in sys.modules, but it’s only partially initialized (Python hasn’t finished executing it yet).
        So when services.py tries to use User, that class doesn’t exist yet → (AttributeError: module 'models' has no attribute 'User').

    That’s the circular import problem: both modules depend on each other while they’re still being executed.





    Resolve it using __init__.py:
    # __init__.py

        # First, import modules that don't have dependencies
        from . import utils

        # Then import modules with dependencies, but don't use them yet
        from . import models
        from . import services

        # both modules are loaded and present in sys.modules, so their class definitions exist.

        # Now set up the references
        models.DataService = services.DataService
        services.User = models.User

        # Optionally, clean up the namespace
        del models, services

        # Expose what you want at the package level
        from .models import User
        from .services import DataService
        from .utils import format_data

        __all__ = ['User', 'DataService', 'format_data']

    # delete circular imports on models and services

    Now, users can simply do:
        from myproject import User, DataService

        user = User("alice")
        data = user.get_data()
        new_user = DataService.create_user("bob")


    This approach:  1. Breaks the circular dependency by importing modules in a specific order. 
                    2. Sets up the necessary references after all modules are loaded. 
                    3. Provides a clean, easy-to-use interface for the package users.
"""

"""
## 5.2 Python Package Management and Virtual Environments
    When developing Python projects, managing dependencies and isolating environments are crucial. 
    There are several tools available for these tasks 
        Package Management Tools:
            pip: The standard package installer for Python.
            Poetry: A modern dependency management and packaging tool.
            Conda: A package, dependency, and environment management system (popular in data science).

        Virtual Environment Tools:
            venv: Built-in Python module for creating virtual environments.
            pyenv: Allows you to easily switch between multiple versions of Python.
            virtualenv: A tool to create isolated Python environments (precursor to venv).

    Let’s focus on pip, venv, and an introduction to Poetry.

    Using pip and venv
    Create a virtual environment (in bash):
        python -m venv myenv

    Activate the environment:
        Windows: myenv\Scripts\activate
        macOS/Linux: source myenv/bin/activate

    ==> source myenv/bin/activate (or myenv\Scripts\activate on Windows) only activates that virtual environment 
    in the current shell session (and its child processes). It doesn’t affect “all projects” or other terminals.
    ==> if you want to "close" the venv in your shell do : deactivate

    Install packages:
        pip install package_name

    Create a requirements.txt file
        A requirements.txt file lists all the Python packages (and their versions) that your project depends on.
        It lets you:
            Recreate the same environment later (or on another machine).
            Share dependencies with teammates or on servers.
            Make deployment and servers builds consistent.

            Example requirements.txt:
                Flask==3.0.3
                requests==2.32.3
                pandas==2.2.2

        When your virtual environment already has everything installed, run:
            pip freeze > requirements.txt
            ==> pip freeze lists all installed packages in the current environment (and exact versions).
            ==> The > operator redirects that output into a file named requirements.txt

    On another computer (or after recreating a clean virtual environment):
        pip install -r requirements.txt
        ==> The -r flag means “install all packages listed in this requirements file.”
        ==> pip installs the same versions listed, guaranteeing reproducibility.


    list of pip command line that you can run in your terminal : 
    | Command                         | Meaning                                   |
    | ------------------------------- | ----------------------------------------- |
    | `pip install package`           | Download + install that package from PyPI |
    | `pip install -U package`        | Upgrade to the latest version             |
    | `pip uninstall package`         | Remove it                                 |
    | `pip show package`              | See details (location, version)           |
    | `pip list`                      | Show everything installed                 |
    | `pip freeze > requirements.txt` | Save installed packages to a file         |
"""

"""
Introduction to Poetry
    Poetry is a more modern tool that combines dependency management, package building, and publishing.

    Install Poetry:
        pip install poetry

    Create a new project or initialize an existing one:
        poetry new myproject #Creates a fresh project skeleton for you.
        # or
        poetry init # Initializes Poetry in an existing folder (or a blank one you prepared),
                    # building a pyproject.toml.

    Add dependencies:
        poetry add package_name

        ==> Declare a new dependency and install it right away.
        What happens:
            Updates pyproject.toml with the package and version constraint.
            Resolves versions and updates poetry.lock.
            Installs into Poetry’s virtualenv.
            Use when you want to add something to your project

    Install dependencies:
        poetry install

        ==> Install everything listed in poetry.lock (or resolve from pyproject.toml if no lock yet).
        A poetry.lock file is Poetry’s lockfile. It records the exact versions (and hashes) of all packages that 
        were resolved for your project—including transitive dependencies—so installs are reproducible across machines.

        What happens:
            If poetry.lock exists → installs exact locked versions (reproducible).
            If no lock → resolves deps, creates poetry.lock, then installs.
            Use when: you (or teammate) want to recreate the environment for this project.
            Common flags:
            poetry install --no-root          # don’t install the project itself as a package
            poetry install --only main        # only main deps (skip dev)
            poetry install --with dev         # include dev deps
            poetry install --sync             # remove anything not in the lock

    The pyproject.toml File
    Poetry uses pyproject.toml for project configuration. Here’s a simple example:
        [tool.poetry]
        name = "myproject"
        version = "0.1.0"
        description = "A sample Python project"
        authors = ["Your Name <you@example.com>"]

        [tool.poetry.dependencies]
        python = "^3.9"
        requests = "^2.26.0"

        [tool.poetry.dev-dependencies]
        pytest = "^6.2.5"

    This file defines your project’s metadata and dependencies.

    Building and Publishing
        Building a package means creating a distribution that can be installed by pip. 
        Publishing means uploading this distribution to a package index like PyPI.

    Build your package:
        poetry build
        This creates distribution files in the dist/ directory.

    Publish to PyPI:
        poetry publish
        This uploads your built package to PyPI, making it available for others to install.

    Poetry simplifies these processes, handling the complexities of building and publishing for you.
"""
"""
Integrating unitest / pytest with Poetry

Add pytest to your project’s dev-dependencies:
    poetry add --dev pytest

Update your pyproject.toml:
    [tool.poetry.dev-dependencies]
    pytest = "^7.4.0"

    [tool.pytest.ini_options]
    testpaths = ["tests"]

This configuration tells pytest to look for tests in the tests directory.

Organize your project structure:

    myproject/
    ├── src/
    │   └── mypackage/
    │       └── example.py
    ├── tests/
    │   └── test_example.py
    └── pyproject.toml

Write your tests in the tests directory.
Example of test using pytest: 
#test_example.py
    def test_addition():
    assert 1 + 1 == 2

    def test_string():
    assert "hello".upper() == "HELLO"

Run tests using Poetry:
    poetry run pytest

Advanced pytest Configuration
You can add more options to your pyproject.toml:
    [tool.pytest.ini_options]
    testpaths = ["tests"]
    addopts = "-v --cov=src"

    This configuration: - Runs tests verbosely (-v) - Includes coverage reporting (--cov=src)

Running Tests with Poetry
To make running tests easier, you can add a script to your pyproject.toml:
    [tool.poetry.scripts]
    test = "pytest" 


Now you can run tests with:    
    poetry run test
"""







