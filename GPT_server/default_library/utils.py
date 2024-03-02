"""
Utilities module for general shared code functions
"""

# Custom libraries
from default_library.exception import CustomEvironmentExcption
from default_library.constants import (ALL_ENV)

def validate_args(args: list) -> None:
    """
    Validate arguments
    Args:
        args: list
            [0]: file name: String
            [1]: environment: String
    Return:
        None
    """
    if len(args) < 2:
        raise CustomEvironmentExcption("Incorrect argument length")
    environment = args[1].upper()
    if environment not in ALL_ENV:
        raise CustomEvironmentExcption("Wrong environment")
# End validate_args function
    

if __name__ == "__main__":
    pass