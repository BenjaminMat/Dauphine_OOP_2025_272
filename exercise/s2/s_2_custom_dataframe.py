"""
Instructions
Your task is to create a class DataFrameSimple that simulates the basic functionalities of a dataframe.
Follow these steps to complete the task:

Step 1: Implement the DataFrameSimple Class
    Implement the DataFrameSimple class with the following methods:
        __init__(self, data):
            Constructor that accepts a dictionary of data.
            Convert the data into a NumPy array for internal storage.
            Store the column names as a list.

        mean(self, column_name):
            Calculates the mean (average) of the specified column.
            Use NumPy's np.mean() for the calculation.

        sum(self, column_name):
            Calculates the sum of the specified column.
            Use NumPy's np.sum() for the calculation.

    min(self, column_name):
        Finds the minimum value of the specified column.
        Use NumPy's np.min() for the calculation.

    max(self, column_name):
        Finds the maximum value of the specified column.
        Use NumPy's np.max() for the calculation.

    select_column(self, column_name):
        Returns the values of the specified column as a NumPy array.

Step 2: Define Class Attributes
    Ensure your class has the following attributes:
        data: A NumPy array that contains the data.
        columns: A list of column names.

Step 3: Use NumPy for Calculations
        Make sure to use NumPy functions for statistical calculations:
        np.mean() for mean.
        np.sum() for sum.
        np.min() for minimum.
        np.max() for maximum.

Tips
Start by implementing the constructor (__init__()).
Utilize NumPy's functions for all statistical calculations.
Remember to import NumPy at the beginning of your dataframe_simple.py file.

Numpy Array example :

arr1 = np.array([1, 2, 3, 4, 5])
print("1D array:", arr1) ==> Output : 1D array: [1 2 3 4 5]

arr2 = np.array([[1, 2, 3], [4, 5, 6]]) # Create a 2D NumPy array (matrix)
print("2D array:\n", arr2)
==> output :
2D array:
 [[1 2 3]
  [4 5 6]]

# Access elements
print("Element at row 1, column 2:", arr2[0, 1]) ==> output : Element at row 1, column 2: 2

Final Check
Verify that your DataFrameSimple class handles various scenarios correctly and passes all unit tests.

"""

import unittest
import numpy as np


class DataFrameSimple:
    # TODO
    pass


class TestDataFrameSimple(unittest.TestCase):

    def setUp(self):
        self.data_dict = {
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50],
            'C': [100, 200, 300, 400, 500]
        }
        self.df = DataFrameSimple(self.data_dict)

    def test_create(self):
        self.assertIsInstance(self.df, DataFrameSimple)
        self.assertEqual(list(self.df.columns), ['A', 'B', 'C'])

    def test_mean(self):
        self.assertEqual(self.df.mean('A'), 3)
        self.assertEqual(self.df.mean('B'), 30)

    def test_sum(self):
        self.assertEqual(self.df.sum('A'), 15)
        self.assertEqual(self.df.sum('B'), 150)

    def test_min(self):
        self.assertEqual(self.df.min('A'), 1)
        self.assertEqual(self.df.min('B'), 10)

    def test_max(self):
        self.assertEqual(self.df.max('A'), 5)
        self.assertEqual(self.df.max('B'), 50)

    def test_select_column(self):
        np.testing.assert_array_equal(self.df.select_column('A'), np.array([1, 2, 3, 4, 5]))

def run_tests():
    unittest.main(argv=[''], verbosity=2, exit=False)

if __name__ == '__main__':
    run_tests()
