"""
Create ChatGPT serverr
"""
import sys

# Custom libraries
from default_library.utils import (validate_args)
from default_library.configuration import DataConfiguration
from resource.socket import sr

def main() -> int:
    """
    Run main function
    Args:
        None
    Return:
        Integers
    """
    # args = sys.argv
    args = ["", 'LOCAL']
    validate_args(args=args)
    environment = args[1].upper()
    DataConfiguration(environment=environment)
    sr.start()
    return 0
# End mian method


if __name__ == "__main__":
    result_code = main()
    SystemExit(result_code)