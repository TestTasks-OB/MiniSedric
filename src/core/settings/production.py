import logging

from pydantic import Field
from src.core.settings.app import AppSettings
from src.core.settings.env import ENV_PATH, ENR_FILE
import os
from loguru import logger



 
class ProdAppSettings(AppSettings):
    debug: bool = True

    title: str = "Prod MiniSedric API"

    logging_level: int = logging.DEBUG  
    class Config(AppSettings.Config):
        env_file = ENR_FILE
