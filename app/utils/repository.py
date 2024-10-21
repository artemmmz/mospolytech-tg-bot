from abc import ABC, abstractmethod
from typing import TypeVar, Type, List

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.utils.models import BaseModel


class AbstractRepository(ABC):
    @abstractmethod
    async def find_all(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def add_one(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, **kwargs):
        raise NotImplementedError


_T = TypeVar('_T', BaseModel, Type[BaseModel])


class SQLAlchemyRepository(AbstractRepository, ABC):
    model: _T = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, **data) -> _T:
        instance: _T = self.model(**data)
        self.session.add(instance)
        await self.session.commit()
        return instance

    async def get_all(self) -> List[_T]:
        statement = select(self.model)
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def get_one(self, **data) -> _T:
        statement = select(self.model).where(**data)
        result = await self.session.execute(statement)
        return result.scalars().one()
