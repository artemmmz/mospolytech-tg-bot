"""Module with repository for managing users."""

from abc import ABC

from app.core.repository import SQLAlchemyRepository
from app.utils.models import User


class UserRepository(SQLAlchemyRepository, ABC):
    """
    Repository for managing users.

    Attributes:
        model: SQLAlchemy model
    """

    model = User
