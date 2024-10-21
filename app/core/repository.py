from abc import ABC, abstractmethod
from typing import Any, Dict, List, Set, Type, TypeVar

from redis.asyncio import Redis
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.utils.models import BaseModel


class AbstractRepository(ABC):
    @abstractmethod
    async def get_all(self, **kwargs):
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

    async def get_all(self, **data) -> List[_T]:
        statement = select(self.model).where(**data)
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def get_one(self, **data) -> _T:
        statement = select(self.model).where(**data)
        result = await self.session.execute(statement)
        return result.scalars().one()


_RTypes = TypeVar('_RTypes', int, float, str, Dict, Set, List)


class RedisRepository(AbstractRepository, ABC):
    def __init__(self, redis: Redis):
        self.redis = redis

    async def add_one(
        self, key: str, value: _RTypes, expire_secs: int = None, **kwargs
    ) -> int | str | Any:
        if isinstance(value, list):
            result = await self.redis.rpush(key, *value)
        elif isinstance(value, set):
            result = await self.redis.sadd(key, *value)
        elif isinstance(value, dict):
            result = await self.redis.hset(key, mapping=value)
        else:
            return await self.redis.set(key, value, expire_secs, **kwargs)
        await self.redis.expire(key, expire_secs)
        return result

    async def get_one(self, key: str) -> _RTypes:
        return await self.redis.get(key)

    async def get_all(self, **kwargs) -> Dict[str, _RTypes]:
        return await self.redis.scan(**kwargs)
