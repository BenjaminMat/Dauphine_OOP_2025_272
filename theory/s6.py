"""
    # Imports
    # Package management
"""
"""
IDE are great tools for Debugging, Code navigation, refactors and test run. 
However, if your code is deployed in a server or will run with cron, the behavior will be closer to the one you can 
mimic through shell. 
When you run your script in a production set up, it is important to understand imports and package management in order
to verify that your code could run outside your predetermine set up from your IDE. 

few useful commands line : 
                cd	                        Change Directory	
                cd /path/to/dir	            Go to specific folder	
                ls	                        List files/folders	ls	Shows what’s in the current directory
                pwd	                        Print Working Directory	pwd	Shows where you are
                mkdir	                    Make Directory	mkdir new_folder	Creates a new folder
                rmdir	                    Remove Directory	rmdir old_folder	Only works if folder is empty
                rm	                        Remove file. ex: rm file.txt	==> Deletes a file
                touch                       Creates an empty file or updates timestamps
                clear	                    Clear screen	clear	Clears the console window
"""


"""
## Understanding Python Imports and Project Structure

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

logger = logging.getLogger(__name__)   # use a stable, package-wide name
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
Python Package Management and Virtual Environments
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
