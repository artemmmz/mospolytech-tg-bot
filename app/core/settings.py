""" Settings module with main configuration """

from enum import Enum
from pathlib import Path
from urllib import parse

from pydantic import computed_field
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Mode(str, Enum):
    """
    Enumeration for the application's operational modes.

    Attributes:
        development (str): The development mode for debug.
        testing (str): The testing mode.
        production (str): The production mode.
    """

    development = 'development'
    testing = 'testing'
    production = 'production'


class Settings(BaseSettings):
    """
    Configuration settings for the application.

    This class contains various configuration parameters that can be adjusted
    to tailor the application's behavior.

    Attributes:
        MODE (Mode): The current application mode.
        BOT_TOKEN (str): Application bot token from telegram bot `Bot father`.
        API_URL (str): MosPolytech schedule base api url
        POSTGRES_PROTOCOL (str): PostgreSQL protocol
        POSTGRES_HOST (str): PostgreSQL host
        POSTGRES_PORT (str): PostgreSQL port
        POSTGRES_USER (str): PostgreSQL user
        POSTGRES_PASSWORD (str): PostgreSQL password
        REDIS_PROTOCOL (str): Redis protocol
        REDIS_HOST (str): Redis host
        REDIS_PORT (str): Redis port
        REDIS_USER (str): Redis user
        REDIS_PASSWORD (str): Redis password
        REDIS_DATABASE (str): Redis database
        SCHEDULE_EXPIRE_SECS (str): Time in seconds to expire schedule in Redis database
    """

    MODE: Mode = Mode.development

    BOT_TOKEN: str

    API_URL: str = 'https://rasp.dmami.ru/site'

    POSTGRES_PROTOCOL: str = 'postgresql+asyncpg'
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DATABASE: str
    POSTGRES_ARGUMENTS: dict[str, str] = {}

    @computed_field
    @property
    def POSTGRES_ARGUMENTS_STR(self) -> str:
        """
        Dynamic variable for getting PostgreSQL arguments.
        :return: str
        """
        return parse.urlencode(self.POSTGRES_ARGUMENTS)

    @computed_field
    @property
    def POSTGRES_URL(self) -> str:
        """
        Dynamic variable for getting PostgreSQL url.
        :return: str
        """
        return (
            f'{self.POSTGRES_PROTOCOL}://'
            f'{self.POSTGRES_USER}:'
            f'{self.POSTGRES_PASSWORD}@'
            f'{self.POSTGRES_HOST}:'
            f'{self.POSTGRES_PORT}/'
            f'{self.POSTGRES_DATABASE}?'
            f'{self.POSTGRES_ARGUMENTS_STR}'
        )

    REDIS_PROTOCOL: str = 'redis://'
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_USER: str
    REDIS_PASSWORD: str
    REDIS_DATABASE: int

    @computed_field
    @property
    def REDIS_URL(self) -> str:
        """
        Dynamic variable for getting Redis url.
        :return: str
        """
        return (
            f'{self.REDIS_PROTOCOL}://'
            f'{self.REDIS_USER}:'
            f'{self.REDIS_PASSWORD}@'
            f'{self.REDIS_HOST}:'
            f'{self.REDIS_PORT}/'
            f'{self.REDIS_DATABASE}'
        )

    SCHEDULE_EXPIRE_SECS: int = 6 * 60 * 60  # 6 hours


settings = Settings(_env_file=BASE_DIR / '.env')
