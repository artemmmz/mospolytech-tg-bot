import logging

from aiohttp import ClientSession, ClientConnectorError

from abc import ABC, abstractmethod
from enum import Enum

from typing import AnyStr, Dict, Any


class IRemoteRepository(ABC):
    @abstractmethod
    async def request(
            self,
            method: AnyStr,
            http_method: AnyStr,
            parameters: Dict[AnyStr, Any] = None,
            data: Dict[AnyStr, Any] = None,
            timeout: int = 3
    ):
        raise NotImplementedError

    @abstractmethod
    async def get(
            self,
            method: AnyStr,
            parameters: Dict[AnyStr, Any] = None,
            timeout: int = 3
    ):
        raise NotImplementedError

    @abstractmethod
    async def post(
            self,
            method: AnyStr,
            data: Dict[AnyStr, Any] = None,
            timeout: int = 3
    ):
        raise NotImplementedError


class RemoteRepository(IRemoteRepository, ABC):
    def __init__(self, base_url: str = None):
        self.base_url = base_url

    async def request(
            self,
            method: AnyStr,
            http_method: AnyStr,
            parameters: Dict[AnyStr, Any] = None,
            data: Dict[AnyStr, Any] = None,
            timeout: int = 3
    ) -> Dict[AnyStr, Any]:
        url = f'{self.base_url}/{method}?'
        headers = {
            'User-Agent': 'mozilla/5.0 (windows; u; windows nt 6.3) '
                          'applewebkit/531.1.2 (khtml, like gecko) '
                          'chrome/30.0.838.0 safari/531.1.2'
        }
        try:
            async with ClientSession(timeout=timeout) as session:
                async with session.request(
                        method=http_method, url=url,
                        params=parameters, headers=headers
                ) as request:
                    return await request.json()
        except ClientConnectorError:
            raise Exception

    async def get(
            self,
            method: AnyStr,
            parameters: Dict[AnyStr, Any] = None,
            timeout: int = 3
    ) -> Dict[str, Any]:
        return await self.request(
            method=method,
            http_method='GET',
            parameters=parameters,
            timeout=timeout
        )

    async def post(
            self,
            method: AnyStr,
            data: Dict[AnyStr, Any] = None,
            timeout: int = 3
    ) -> Dict[str, Any]:
        return await self.request(
            method=method,
            http_method='POST',
            data=data,
            timeout=timeout
        )
