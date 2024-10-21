from abc import ABC

from app.utils.models import Subscription
from app.utils.repository import SQLAlchemyRepository


class SubscriptionRepository(SQLAlchemyRepository, ABC):
    model = Subscription
