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