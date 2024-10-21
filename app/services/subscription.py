from typing import AnyStr, List

from app.utils.models import Subscription
from app.utils.repository import AbstractRepository


class SubscriptionService:
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    async def add(self, user_id: int, group: AnyStr) -> int:
        return await self.repository.add_one(user_id=user_id, group=group)

    async def get_all(self, group: AnyStr) -> List[Subscription]:
        return await self.repository.find_all(group=group)
