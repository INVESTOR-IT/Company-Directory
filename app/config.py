from pydantic_settings import BaseSettings, SettingsConfigDict
from loguru import logger

import sys


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    URL_DATABASE: str

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


settings = Settings()

logger.remove()
logger.add(sys.stderr, level='INFO')
