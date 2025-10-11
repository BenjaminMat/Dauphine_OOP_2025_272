"""
Build a tiny FinancialAsset model using descriptors:

1) Data descriptor: UpperTicker
   - Coerces to uppercase string and validates letters only (A-Z, 1–10 chars)
   - Used for: ticker

&) Non-data descriptor: DailyReturn
   - Read-only computed attribute: (price / prev_close) - 1
   - Only __get__ (no __set__/__delete__)

Key ideas:
- Descriptors must live on the *class* to intercept attribute access.
- Data descriptor (with __set__) wins over instance dict.
- Non-data descriptor (only __get__) is great for computed attributes.

Fill every TODO below.

Additional information :
Python `re` (regular expressions) package
    - Use `re` for pattern matching and text processing.
    - Common funcs: compile, match, fullmatch, search, findall, finditer, sub, split
    - re.compile(pattern) builds a reusable regex object.
    - regex.match(s) tries to match the pattern at the BEGINNING of s.
    - for "^[A-Z]{1,10}$ pattern, the match function will match if the string is in upper case

    code snippet to understand how it works :
    pat = re.compile(r"^[A-Z]{1,10}$")

    tests = [
        "AAPL",      # OK (4 uppercase letters)
        "GOOG",      # OK
        "X",         # OK (length 1)
        "ABCDEFGHIJ",# OK (length 10)
        "ABCDEFGHIJK",# NO (length 11)
        "Aapl",      # NO (lowercase present)
        "MSFT!",     # NO (non-letter '!')
        "MS FT",     # NO (space)
        "",          # NO (needs at least 1)
    ]

    for s in tests:
        m = pat.match(s)
        print(f"{s!r:12} ->", bool(m))
"""
import re

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



class UpperTicker:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.storage_name = "_" + name
        self._re = re.compile(r"^[A-Z]{1,10}$")

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        # TODO: return the stored ticker
        raise NotImplementedError

    def __set__(self, obj, value):
        # TODO: coerce to str, uppercase it
        # TODO: validate with regex self._re; if invalid, raise ValueError("Ticker must be 1-10 uppercase letters")
        # TODO: store the value on the instance under self.storage_name
        raise NotImplementedError

    def __delete__(self, obj):
        raise AttributeError(f"Cannot delete {self.public_name}")


class DailyReturn:
    """
    Read-only computed attribute:
        return = (price / prev_close) - 1
    If prev_close is 0, raise ZeroDivisionError.
    """
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        # TODO: fetch price and prev_close from obj (they trigger descriptor reads)
        # TODO: compute and return (price / prev_close) - 1
        # TODO: if prev_close == 0, raise ZeroDivisionError("prev_close is zero")
        raise NotImplementedError


class FinancialAsset:
    ticker = UpperTicker()
    price = NonNegativeFloat()
    prev_close = NonNegativeFloat()
    daily_return = DailyReturn()  # read-only computed attribute

    def __init__(self, ticker: str, price: float, prev_close: float):
        # These lines will invoke descriptor __set__ and validate inputs
        self.ticker = ticker
        self.price = price
        self.prev_close = prev_close


if __name__ == "__main__":
    # Expected: ticker coerced to uppercase, numbers validated as non-negative
    asset = FinancialAsset("aapl", 150.0, 148.0)
    print("Ticker:", asset.ticker)             # "AAPL"
    print("Price:", asset.price)               # 150.0
    print("Prev close:", asset.prev_close)     # 148.0
    print("Daily return:", asset.daily_return) # ~0.0135

    # Uncomment to test validations:
    # asset.price = -1                                  # ValueError
    # asset.prev_close = "abc"                          # TypeError
    # asset.ticker = "msft!"                            # ValueError
    # asset.prev_close = 0                              # ZeroDivisionError on asset.daily_return
    # print("Daily return:", asset.daily_return)        # ZeroDivisionError on asset.daily_return
    # you can also create a unit test for that

