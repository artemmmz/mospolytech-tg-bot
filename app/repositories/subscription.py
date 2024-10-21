"""Module with subscription repository."""

from abc import ABC

from app.core.repository import SQLAlchemyRepository
from app.utils.models import Subscription


class SubscriptionRepository(SQLAlchemyRepository, ABC):
    """
    Repository for managing subscriptions.

    Attributes:
        model: SQLAlchemy model
    """

    model = Subscription
