"""Module with PostgreSQL models."""

from datetime import time

from sqlalchemy import Column, ForeignKey, Integer, String, Time
from sqlalchemy.orm import DeclarativeBase, relationship


class BaseModel(DeclarativeBase):
    """
    Abstract base class with id for all models.

    Attributes:
        id_ (Column): Model id.
    """

    id_ = Column(Integer, name='id', primary_key=True)


class User(BaseModel):
    """
    User model for PostgreSQL database.

    Attributes:
        id_ (Column): Telegram user id.
    """

    __tablename__ = 'users'

    subscriptions = relationship("Subscription", back_populates='user')


class Subscription(BaseModel):
    """
    Subscription model for PostgreSQL database.

    Attributes:
        id_ (Column): Subscription id
        user_id (Column): Telegram user id.
        group (Column): MosPolytech education group.
        time (Column): Time of subscription.
    """

    __tablename__ = 'subscriptions'

    user_id = Column(
        Integer, ForeignKey(User.id_, ondelete='CASCADE'), nullable=False
    )
    group = Column(String, nullable=False)
    time = Column(Time, default=time(hour=19), nullable=False)

    user = relationship(User, back_populates='subscriptions')
