"""Module with service for subscription conversation."""

from typing import AnyStr, List

from app.core.repository import AbstractRepository
from app.utils.models import Subscription


class SubscriptionService:
    """Service for managing subscriptions."""

    def __init__(self, repository: AbstractRepository):
        """
        Initialize service for subscription conversation.

        :param repository: Repository for subscription conversation.
        """
        self.repository = repository

    async def add(self, user_id: int, group: AnyStr) -> int:
        """
        Add subscription to database.

        :param user_id: Telegram user id.
        :param group: MosPolytech educational group.
        :return: Subscription id.
        """
        return await self.repository.add_one(user_id=user_id, group=group)

    async def get_all_by_group(self, group: AnyStr) -> List[Subscription]:
        """
        Get all subscriptions by one group from database.

        :param group: MosPolytech educational group.
        :return: List of subscriptions.
        """
        return await self.repository.get_all(group=group)

    async def get_all_by_user_id(self, user_id: int):
        """
        Get all subscriptions by one user from database.

        :param user_id: Telegram user id.
        :return: List of subscriptions.
        """
        return await self.repository.get_all(user_id=user_id)

    async def get_all(self):
        """
        Get all subscriptions.

        :return: List of subscriptions.
        """
        return await self.repository.get_all()
