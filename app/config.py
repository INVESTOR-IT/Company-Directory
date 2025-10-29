from pydantic_settings import BaseSettings, SettingsConfigDict
from loguru import logger

import sys


class Settings(BaseSettings):
    URL_DATABASE: str

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


settings = Settings()

logger.remove()
logger.add(sys.stderr, level='INFO')
