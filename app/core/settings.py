from enum import Enum

from pydantic import computed_field
from pydantic_settings import BaseSettings

from urllib import parse


class Mode(str, Enum):
    development = 'development'
    testing = 'testing'
    production = 'production'


class Settings(BaseSettings):
    MODE: Mode = Mode.development

    BOT_TOKEN: str

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
        return parse.urlencode(self.POSTGRES_ARGUMENTS)

    @computed_field
    @property
    def POSTGRES_URL(self) -> str:
        return (
            f'{self.POSTGRES_PROTOCOL}://'
            f'{self.POSTGRES_USER}:'
            f'{self.POSTGRES_PASSWORD}@'
            f'{self.POSTGRES_HOST}:'
            f'{self.POSTGRES_PORT}/'
            f'{self.POSTGRES_DATABASE}?'
            f'{self.POSTGRES_ARGUMENTS_STR}'
        )


settings = Settings()
