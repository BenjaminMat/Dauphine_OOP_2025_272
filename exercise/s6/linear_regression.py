"""
In this TP, you’ll create a simple machine learning package focused on linear regression.
You’ll use Poetry for package management, implement basic classes, write tests, set up continuous integration,
manually publish your package, and finally automate the publishing process.

Objectives
    Set up a Python project using Poetry
    Implement a basic linear regression class
    Write unit tests for your implementation
    Use GitHub Actions for continuous integration
    Manually publish your package to PyPI
    Automate the publishing process using GitHub Actions

Prerequisites
    Basic understanding of Python and object-oriented programming
    Familiarity with linear regression concepts
    Git and GitHub account
    Python 3.8 or higher installed

Step 1: Setting Up the Project
    Set up your project using Poetry.
    Install Poetry if you haven’t already.
    Create a new project named finance-ml-your_last_name.
    Edit the pyproject.toml file to add necessary dependencies (numpy for calculations, pytest for testing).
    Install the dependencies using Poetry.

Set up the project structure as described above. Familiarize yourself with the pyproject.toml file and
Poetry commands.
"""

"""
Step 2: Implementing Linear Regression

Create a new file src/finance_ml/linear_models.py 
Implement a LinearRegression class with the following methods:
    __init__(self, use_intercept=True): Initialize the model parameters.
        use_intercept → whether to fit an intercept (bias)
        coef_ → model weights (for each feature)
        intercept_ → bias term
        _fitted → flag to check if model is trained
        
    fit(self, X, y): Fit the model to the training data.
        When you fit data, you must ensure X is a 2D matrix and optionally add a column of ones if you use an intercept.
        Compute parameters using the Normal Equation:
                            tetha = θ = (XᵀX)⁻¹ Xᵀy
        
        the @ operator is used when computing the matrix product between 2d arrays.
        X.T is used to have the transpose matrix
        np.linalg.inv() is used to have the inverse matrix
        alternatively you can use the we can use the Moore–Penrose pseudoinverse matrix to handle collinear feature 
        with np.linalg.pinv(X)
        
    predict(self, X): Make predictions using the trained model.

Your implementation should handle cases with and without an intercept term and use numpy for efficient calculations.
"""

"""
Step 3: Writing Tests

Create a new file tests/test_linear_models.py and write test functions to cover various scenarios and edge cases.
Implement the test functions for your LinearRegression class.


"""

"""
[Optional] Step 4: Setting Up Basic GitHub Actions

Set up a basic GitHub Actions workflow to run your tests automatically.
Create a new file .github/workflows/tests.yml and copy paste the following:
    name: Run Tests

    on: [push, pull_request]

    jobs:
      test:
        runs-on: ubuntu-latest
        steps:
        - uses: actions/checkout@v2
        - name: Set up Python
          uses: actions/setup-python@v2
          with:
            python-version: '3.8'
        - name: Install dependencies
          run: |
            pip install poetry
            poetry install
        - name: Run tests
          run: poetry run pytest

1. Set up a GitHub repository for your project and add the GitHub Actions workflow as shown above.
2. Push your code and verify that the tests run automatically on push and pull requests.
"""

"""
[Optional] Step 5: Manual Package Publishing

Register an account on PyPI (https://pypi.org/)
Build your package using Poetry
Publish your package to PyPI using Poetry

Follow the steps above to manually publish your package to PyPI.
Verify that you can install your package from PyPI using pip.
"""

"""
[Optional] Step 6: Automating Package Publishing
Finally, automate the publishing process using GitHub Actions.

Modify the GitHub Actions workflow you created in Step 4 to include a job for publishing the package to PyPI when
pushing to the main branch.
2. Research how to securely add your PyPI credentials as secrets in GitHub Actions.
3. Update your workflow to use these secrets for authentication when publishing.
4. Test your automated publishing process by pushing a change to the main branch.

Hint: You’ll need to add a new job to your workflow, use conditional execution based on the branch,
and incorporate the PyPI credentials as secrets.
"""