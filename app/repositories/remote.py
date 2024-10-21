"""Module with repository for working with remote data."""

import logging
from abc import ABC, abstractmethod
from typing import Any, AnyStr, Dict
from urllib.parse import urlencode

from aiohttp import ClientConnectorError, ClientSession, ClientTimeout

from app.exceptions.api_error import APIError


class IRemoteRepository(ABC):
    """Abstract base class for remote repositories."""

    @abstractmethod
    async def request(
        self,
        method: AnyStr,
        http_method: AnyStr,
        parameters: Dict[AnyStr, Any] = None,
        data: Dict[AnyStr, Any] = None,
        timeout: int = 3,
    ):
        """Abstract method for making requests to the remote server."""
        raise NotImplementedError

    @abstractmethod
    async def get(
        self,
        method: AnyStr,
        parameters: Dict[AnyStr, Any] = None,
        timeout: int = 3,
    ):
        """Abstract method for making get requests to the remote server."""
        raise NotImplementedError

    @abstractmethod
    async def post(
        self, method: AnyStr, data: Dict[AnyStr, Any] = None, timeout: int = 3
    ):
        """Abstract method for making post requests to the remote server."""
        raise NotImplementedError


class RemoteRepository(IRemoteRepository, ABC):
    """Repository for getting remote data."""

    def __init__(self, base_url: str = None):
        """
        Initialize remote repository.

        :param base_url:
        """
        self.base_url = base_url

    async def request(
        self,
        method: AnyStr,
        http_method: AnyStr,
        parameters: Dict[AnyStr, Any] = None,
        data: Dict[AnyStr, Any] = None,
        timeout: int = 10,
    ) -> Any | None:
        """
        Request to remote repository.

        :param method: API method name.
        :param http_method: HTTP method name.
        :param parameters: API data for GET request.
        :param data: API data for POST request.
        :param timeout: Timeout in seconds.
        :return: Response content.
        """
        parameters_url = urlencode(parameters) if parameters else ''
        url = f'{self.base_url}/{method}?{parameters_url}'
        headers = {
            'User-Agent': 'mozilla/5.0 (windows; u; windows nt 6.3) '
            'applewebkit/531.1.2 (khtml, like gecko) '
            'chrome/30.0.838.0 safari/531.1.2',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'X-Requested-With': 'XMLHttpRequest',
            'Sec-GPC': '1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'credentials': 'include',
            'referer': 'https://rasp.dmami.ru/',
        }
        logging.debug(f"Url: {url}")
        try:
            async with ClientSession(
                timeout=ClientTimeout(timeout)
            ) as session:
                async with session.request(
                    method=http_method, url=url, headers=headers
                ) as request:
                    if request.status != 200:
                        raise APIError(request.content, request.status)
                    return await request.json()
        except ClientConnectorError:
            raise Exception

    async def get(
        self,
        method: AnyStr,
        parameters: Dict[AnyStr, Any] = None,
        timeout: int = 3,
    ) -> Dict[str, Any]:
        """
        Get request to remote repository.

        :param method: API method name.
        :param parameters: API data.
        :param timeout: Timeout in seconds.
        :return: Response content.
        """
        return await self.request(
            method=method,
            http_method='GET',
            parameters=parameters,
            timeout=timeout,
        )

    async def post(
        self, method: AnyStr, data: Dict[AnyStr, Any] = None, timeout: int = 3
    ) -> Dict[str, Any]:
        """
        Post request to remote repository.

        :param method: API method name.
        :param data: API data.
        :param timeout: Timeout in seconds.
        :return: Response content.
        """
        return await self.request(
            method=method, http_method='POST', data=data, timeout=timeout
        )
