from enum import Enum
from pydantic import Field
from pydantic_settings import BaseSettings 
from src.core.settings.env import  ENV_PATH, ENR_FILE
import os


class AppEnvTypes(Enum):
    prod: str = "prod"
    dev: str = "dev"
    test: str = "test"

class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = Field(default_factory=lambda: AppEnvTypes[os.environ.get('ENV', 'prod')])
    secret_key: str = Field(default_factory=lambda: os.environ['SECRET_KEY'])  
    env: str = Field(default_factory=lambda: os.environ['ENV'])  
    AWS_ACCESS_KEY_ID: str = Field(default_factory=lambda: os.environ['AWS_ACCESS_KEY_ID']) 
    AWS_SECRET_ACCESS_KEY: str = Field(default_factory=lambda: os.environ['AWS_SECRET_ACCESS_KEY']) 
    AWS_DEFAULT_REGION: str = Field(default_factory=lambda: os.environ['AWS_DEFAULT_REGION']) 

    class Config:
        env_file = ENV_PATH
        