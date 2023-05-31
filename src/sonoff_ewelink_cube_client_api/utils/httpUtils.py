"""
Module: httpUtils

This module provides utility functions for making HTTP requests.

Classes:
    httpUtils: Contains functions for making HTTP requests.
"""
#pylint: disable-msg=too-few-public-methods

from typing import Dict, Any, Optional

import logging
import json
import aiohttp

from ..ts.enum.EMethod import EMethod
from ..ts.enum.EPath import EPath
from ..ts.interface.IConfig import IConfig
from ..ts.interface.IResponse import IResponse

_LOGGER = logging.getLogger(__name__)


class httpUtils(IConfig):
    """
    Contains functions for making HTTP requests.
    """
    session = None

    async def httpRequest(
        self,
        path: str,
        method: EMethod,
        params: Optional[Dict[str, Any]] = None,
        isNeedAT: bool = True
    ) -> IResponse:
        """
        Makes an HTTP request.

        Args:
            path (str): API path.
            method (EMethod): HTTP method.
            params (Optional[Dict[str, Any]]): Request parameters (default: None).
            isNeedAT (bool): Flag to indicate if access token is required (default: True).

        Returns:
            IResponse: Dictionary containing the response data.
        """
        url = f"http://{self.ip}{EPath.ROOT.value}{EPath.V1.value}{path}"
        _LOGGER.debug(f'httpRequest {method}: {url}')

        headers = {'Content-Type': 'application/json'}
        if isNeedAT and self.at:
            headers['Authorization'] = f'Bearer {self.at}'
        _LOGGER.debug(f'httpRequest headers: {headers}')

        response: str = None
        async with aiohttp.ClientSession(headers=headers) as session:
            if method == EMethod.GET:
                async with session.get(url, params=params) as resp:
                    response = await resp.text()
            elif method == EMethod.POST:
                params = {} if not params else params
                async with session.post(url, data=json.dumps(params)) as resp:
                    response = await resp.text()
            elif method == EMethod.PUT:
                async with session.put(url, data=json.dumps(params)) as resp:
                    response = await resp.text()
            elif method == EMethod.DELETE:
                async with session.delete(url, params=params) as resp:
                    response = await resp.text()

        try:
            _LOGGER.debug(f'httpRequest response: {response}')
            if response is None:
                return IResponse(
                    error=-1,
                    message='Empty response.',
                    data={}
                )

            response_data = json.loads(response)
            return IResponse(
                error=response_data["error"],
                message=response_data["message"],
                data=response_data["data"]
            )

        except json.JSONDecodeError:
            _LOGGER.error(f'httpRequest response: {response}')
            return IResponse(
                error=-1,
                message='Invalid JSON response.',
                data={}
            )
