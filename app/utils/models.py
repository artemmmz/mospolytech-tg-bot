from datetime import datetime, time

from sqlalchemy import Column, Integer, String, ForeignKey, Time
from sqlalchemy.orm import DeclarativeBase, relationship


class BaseModel(DeclarativeBase):
    id_ = Column(Integer, name='id', primary_key=True)


class User(BaseModel):
    __tablename__ = 'users'

    subscriptions = relationship("Subscription", back_populates='user')


class Subscription(BaseModel):
    __tablename__ = 'subscriptions'

    user_id = Column(
        Integer,
        ForeignKey(User.id_, ondelete='DELETE'),
        nullable=False
    )
    group = Column(String, nullable=False)
    time = Column(Time, default=time(hour=19), nullable=False)

    user = relationship(User, back_populates='subscriptions')
