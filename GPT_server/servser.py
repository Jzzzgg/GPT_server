"""
Create ChatGPT serverr
"""
import sys

# Custom libraries
from default_library.utils import (validate_args)
from default_library.configuration import DataConfiguration

def main() -> int:
    """
    Run main function
    """
    args = sys.argv
    validate_args(args=args)
    environment = args[1].upper()
    DataConfiguration(environment=environment)
    return 0
# End mian method


if __name__ == "__main__":
    result_code = main()
    SystemExit(result_code)