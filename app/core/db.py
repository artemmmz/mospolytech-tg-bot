""" Module for database initialization """

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core import settings

engine = create_async_engine(
    url=settings.POSTGRES_URL,
    future=True,
    echo=True,
    execution_options={'isolation_level': 'AUTOCOMMIT'},
)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


def get_db() -> AsyncSession:
    """
    Function for getting database session
    :return: AsyncSession
    """
    return async_session()
