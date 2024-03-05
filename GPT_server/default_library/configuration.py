"""
Base configuration object
"""
# import librariesS
from json import loads
from typing import Tuple

# Custom modulesS
from default_library.constants import (CONFIG_PATH, WORK_SPACE)
from default_library.exception import (CustomEvironmentExcption)

class ConfigKeys(object):
    """
    Config keywords
    """
    open_ai_secret_key = "open_ai_secret_key"
    host_address = "host_address"
    port_number = "port_number"
# End ConfigKeys class
    

class BaseConfiguration(object):
    """
    Base Configuration object
    """
    def __init__(self, environment: str) -> None:
        """
        Init the config class
        Args:
            environment: String
        Return:
            None
        """
        super(BaseConfiguration, self).__init__()
        self.environment = environment
        self.work_space = WORK_SPACE
        self.config_path = CONFIG_PATH
        self.common_data, self.env_data = self.read_config()
    # End init built-in 
    
    
    def read_config(self) -> Tuple:
        """
        Read the congfiguration file
        """
        with open(self.config_path, encoding="utf-8-sig") as input_file:
            full_data = loads(input_file.read())

        env_data = full_data.get(self.environment, None)
        common_data = full_data.get("common", None)
        if env_data is None or common_data is None:
            raise CustomEvironmentExcption("Incorrect config data.")
        return (common_data, env_data)
    # End read_config method
# End BaseConfiguration class
        

class DataConfiguration(BaseConfiguration):
    """
    DataConfiguration 
    Confif class of working project
    """
    @property
    def open_ai_secret_key(self) -> str:
        """
        Get open ai secret key
        Return:
            String
        """
        return self.common_data.get(ConfigKeys.open_ai_secret_key)
    # End open_ai_secret_key function

    @property
    def host_address(self) -> str:
        """
        Get host address
        Return:
            String
        """
        return self.common_data.get(ConfigKeys.host_address)
    # End host_address function

    @property
    def port_number(self) -> str:
        """
        Get port number
        Return:
            String
        """
        return int(self.common_data.get(ConfigKeys.port_number))
    # End port_number function



if __name__ == "__main__":
    pass