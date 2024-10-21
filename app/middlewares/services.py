"""Module with service middleware."""

from typing import Any, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message

from app.core import settings
from app.core.db import get_db
from app.core.redis import redis
from app.core.repository import RedisRepository
from app.repositories.remote import RemoteRepository
from app.repositories.subscription import SubscriptionRepository
from app.repositories.user import UserRepository
from app.services.schedule import ScheduleService
from app.services.subscription import SubscriptionService
from app.services.user import UserService


class ServicesMiddleware(BaseMiddleware):
    """Middleware for working with services."""

    def __init__(self):
        """Initialize middleware for working with services."""
        self.session = get_db()
        self.services = {
            'schedule_service': ScheduleService(
                RemoteRepository(settings.API_URL), RedisRepository(redis)
            ),
            'subscription_service': SubscriptionService(
                SubscriptionRepository(self.session)
            ),
            'user_service': UserService(UserRepository(self.session)),
        }

    async def __call__(
        self, handler: Callable, event: Message, data: Dict[str, Any], **kwargs
    ):
        """
        Get services to routers for working with its.

        :param handler: Aiogram message handler.
        :param event: Aiogram event.
        :param data: Telegram and other data.
        :param kwargs: Other parameters.
        :return: None
        """
        data = {**data, **self.services}
        return await handler(event, data)
