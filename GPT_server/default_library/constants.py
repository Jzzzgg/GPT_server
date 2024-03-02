"""
ConstantsS
"""
from pathlib import Path

# file location
RESOURCE = "resource"
APP_CONFIG = "app.cfg"
WORK_SPACE = Path(__file__).parent.parent
CONFIG_PATH = WORK_SPACE.joinpath(RESOURCE, APP_CONFIG)

# environment
ALL_ENV = ["LOCAL", "PROD"]



if __name__ == "__main__":
    pass