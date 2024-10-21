from typing import AnyStr, Dict, Any

from app.repositories.remote import IRemoteRepository

BASE_URL = ''

class ScheduleService:
    def __init__(self, repository: IRemoteRepository):
        self.repository = repository

    async def get_schedule(self, group: AnyStr) -> Dict[AnyStr, Any]:
        return await self.repository.get(
            method='group', parameters={'group': group, 'session': 0}
        )
