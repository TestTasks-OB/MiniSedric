import logging

from pydantic import Field
from src.core.settings.app import AppSettings
from src.core.settings.env import ENV_PATH, ENR_FILE
import os
from loguru import logger


 
class DevAppSettings(AppSettings):
    debug: bool = True

    title: str = "Dev MiniSedric API"

    logging_level: int = logging.DEBUG
     
    class Config(AppSettings.Config):
        env_file = ENV_PATH
