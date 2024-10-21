from app.utils.repository import AbstractRepository


class UserService:
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    async def create_user(self, user_id: int):
        return self.repository.add_one(user_id=user_id)

    async def get_user(self, user_id: int):
        return self.repository.get_one(user_id=user_id)
