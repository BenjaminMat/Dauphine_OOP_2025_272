"""
Exercise 1: Market Capitalization Filter

Given a dictionary of companies and their market capitalizations in billions, use a list comprehension to produce a list
of companies with a market capitalization of more than $500 billion.

Syntax:     [expression for item in iterable if condition] for creating a list which contains expression as value
            {expression which generate a dict for item in iterable if condition} for creating a dict

            An iterable in Python is any object you can loop over because it can produce an iterator.
            More formally:
            It implements __iter__() that returns an iterator, or
            It implements the old sequence protocol: __len__ and __getitem__(index) starting at 0.
            Common iterables: lists, tuples, dicts (iterate over keys), sets, strings, files, ranges,
            many library objects.

Example :
    prices = [100.5, 102.3, 98.7, 105.6]
    log_returns = [math.log(prices[i] / prices[i - 1]) for i in range(1, len(prices))]

    ==> here log return will return the result of math.log(prices[i] / prices[i - 1]).
    During the run time the expression will be executed 3 time (prices has 4 element) with i taking the following value
    1, 2, 3 and 4 (int btw 1 and 4 (len(prices)).
    This implementation is similar to the following one :
    for i in range(1, len(prices)):
        log_return = math.log(prices[i] / prices[i - 1])
        log_returns_with_for_loop.append(log_return)
"""

market_caps = {
    'Apple': 2200,
    'Microsoft': 1980,
    'Google': 1450,
    'Amazon': 1675,
    'Tesla': 650,
    'Zoom': 120
}

# Expected Output: ['Apple', 'Microsoft', 'Google', 'Amazon', 'Tesla']
filtered_list = []
for k, v in market_caps.items():
    if v > 500:
        filtered_list.append(k)
# [expression for item in iterable if condition]
filtered_list = [k for k, v in market_caps.items() if v > 500]
print(f"Expected Output: ['Apple', 'Microsoft', 'Google', 'Amazon', 'Tesla'] - output {filtered_list}")

"""
Exercise 2: Normalizing Data

Given a list of numbers, normalize them so they range between 0 and 1. 
To normalize a value, you'd use the formula (value - min_value) / (max_value - min_value)

"""
data = [50, 100, 150, 200, 250]
#[expression for item in iterable if condition] for creating a list
# Step 1: Find min and max values of the list
# Step 2: Normalize the numbers
normalized_value = [(v - max(data))/(max(data) - min(data)) for v in data]
print(f"Expected Output: [0, 0.25, 0.5, 0.75, 1] - Output {normalized_value}")
# Expected Output: [0, 0.25, 0.5, 0.75, 1]

"""
Exercise 3: Stock Price Adjustments
Given a list of stock prices and a separate list of dividend payouts, adjust the stock prices for dividends.

Hint: use zip() in the list comprehension
The zip() function is a built-in function in Python that is used to combine multiple iterables (like lists or tuples) 
element-wise. When you zip two or more iterables, it returns an iterator of tuples, where the i-th tuple contains 
the i-th element from each of the argument sequences.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped)) #output => [(1, 'a'), (2, 'b'), (3, 'c')]

In list comprehension the synthax to manipulate tuple is the following: 
[ *operation to perform* for value1, value2 in zip(list1, list2)]

example: [str(value1) + value2 for value1, value2 in zip(list1, list2)] ==> ['1a', '2b', '3c']
"""
#[expression for item in iterable if condition] for creating a list
prices = [100, 101, 102, 103, 104]
dividends = [0, 0.5, 0, 0, 1]

# expected Output: [100, 100.5, 102, 103, 103]
output_zip_example = [price - dividend for price, dividend in zip(prices, dividends)]
print(f"Expected Output: [100, 100.5, 102, 103, 103] - Output {output_zip_example}")











