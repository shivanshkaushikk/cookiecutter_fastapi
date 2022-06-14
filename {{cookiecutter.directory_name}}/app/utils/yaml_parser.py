# config_loader.py
import yaml
import os
import re

from dotenv import load_dotenv
from pathlib import Path
import logging
from envyaml import EnvYAML
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class Config:
    """Interact with configuration variables."""

    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

    __configFilePath = (os.path.join(os.getcwd(), 'conf/config.yaml'))
    __configParser = EnvYAML(__configFilePath)

    @classmethod
    def __getenvvar(cls, key):
        value = os.getenv(key)
        if value == '' or value is None:
            # use default value as DEV, in case env is not set
            value = None
        return value

    @classmethod
    def get_config_val(cls, key):
        """Get prod values from config.yaml."""
        config_value = None
        try:
            config_value = cls.__configParser[key]
        except Exception as e:
            logger.error(e)
            logger.error('invalid key structure passed for retrieving value from config.yaml')
            config_value = None

        # logger.info("config value for key {0} : {1}".format(key, config_value))

        return config_value
