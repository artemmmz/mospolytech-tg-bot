from abc import ABC

from app.utils.models import User
from app.utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository, ABC):
    model = User
