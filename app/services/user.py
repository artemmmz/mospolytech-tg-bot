"""Module with service for managing users."""

from app.core.repository import AbstractRepository


class UserService:
    """Service for managing users."""

    def __init__(self, repository: AbstractRepository):
        """
        Initialize a new instance of the User Service.

        :param repository: Repository instance.
        """
        self.repository = repository

    async def create_user(self, user_id: int):
        """
        Create a new user by user_id.

        :param user_id: Telegram user id.
        :return: User instance.
        """
        return await self.repository.add_one(user_id=user_id)

    async def get_user(self, user_id: int):
        """
        Get User instance by user_id.

        :param user_id: Telegram user id.
        :return: User instance.
        """
        return await self.repository.get_one(user_id=user_id)
