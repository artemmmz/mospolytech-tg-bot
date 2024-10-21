"""Module with service for managing schedules."""

import json
from typing import Any, AnyStr, Dict

from app.core import settings
from app.core.repository import AbstractRepository
from app.core.schedule import Schedule
from app.exceptions.schedule import ScheduleError
from app.repositories.remote import IRemoteRepository

BASE_URL = ''


class ScheduleService:
    """Service for managing schedules."""

    def __init__(
        self,
        remote_repository: IRemoteRepository,
        local_repository: AbstractRepository,
        key_label: str = 'app:schedule',
    ):
        """
        Initialize service.

        :param remote_repository: Repository for remote data.
        :param local_repository: Repository for cached data.
        :param key_label: label for identification cached data.
        """
        self.label = key_label
        self.remote_repository = remote_repository
        self.local_repository = local_repository

    async def __get_remote_schedule(self, group: AnyStr) -> Dict[AnyStr, Any]:
        """
        Get schedule from remote repository.

        :param group: Educational group
        :return: Remote response.
        """
        remote_result: Dict = await self.remote_repository.get(
            method='group', parameters={'group': group, 'session': 0}
        )
        return remote_result

    async def __get_local_schedule(
        self, group: AnyStr
    ) -> Dict[AnyStr, Any] | None:
        """
        Get schedule from local repository.

        :param group: Educational group.
        :return: Local data.
        """
        local_result = await self.local_repository.get_one(
            key=f'{self.label}:{group}'
        )
        if local_result is not None:
            return json.loads(local_result)

    async def get_schedule(self, group: AnyStr) -> Schedule:
        """
        Get schedule from local (if exists) or remote repository.

        :param group: Educational group.
        :return: Schedule.
        """
        local_result = await self.__get_local_schedule(group)

        if local_result is not None:
            return Schedule(**local_result)

        remote_result = await self.__get_remote_schedule(group)
        if remote_result['status'] != 'ok':
            raise ScheduleError(remote_result['message'])

        await self.local_repository.add_one(
            key=f'{self.label}:{group}',
            value=json.dumps(remote_result),
            expire_secs=settings.SCHEDULE_EXPIRE_SECS,
        )
        return Schedule(**remote_result)
