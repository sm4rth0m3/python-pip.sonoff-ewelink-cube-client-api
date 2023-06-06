"""
Module: baseClass

This module provides the BaseClassBridge API.

Classes:
    BaseClassBridge: Represents the BaseClassBridge API.

Usage:
    from .baseClassBridge import BaseClassBridge
"""

from typing import Any, Awaitable, Dict, Tuple

import logging

import asyncio

from ..config import Store
from ..ts.enum.EMethod import EMethod
from ..ts.enum.EPath import EPath
from ..ts.interface.IResponse import IResponse
from ..utils.httpUtils import httpUtils

from ..errors import AccessTokenRequestError, AccessTokenUnauthorized

_LOGGER = logging.getLogger(__name__)


class BaseClassBridge(Store, httpUtils):
    """
    BaseClassBridge API.

    Attributes:
        interval (int): Interval for event subscription.
        timeout (int): Timeout for getting the bridge access token.

    Methods:
        getBridgeAT(timeout: int = 120000, interval: int = 2000) -> Dict[str, Any]: Gets the bridge access token.
        getBridgeInfo() -> Dict[str, Any]: Gets the gateway information.
        updateBridgeConfig(volume: int) -> Dict[str, Any]: Updates the gateway configuration.
    """
    interval = None
    timeout = None

    async def getBridgeAT(self, timeout: int = 120000, interval: int = 2000) -> IResponse:
        """
        Gets the bridge access token.

        Args:
            timeout (int): Timeout in milliseconds (default: 120000).
            interval (int): Interval between attempts in milliseconds (default: 2000).

        Returns:
            Dict[str, Any]: Dictionary containing the response data.
        """
        async def verifyAccessToken() -> bool:
            """
            Verify the access token with an endpoint check.
            """
            resp = await self.httpRequest(
                path=EPath.DEVICE.value,
                method=EMethod.GET,
            )

            if not resp['error']:
                if resp['data'] and 'device_list' in resp['data']:
                    return True
            return False

        async def getBridgeATHandler() -> Awaitable[Tuple[Dict[str, Any], Dict[str, Any]]]:
            """
            Internal function to handle getting the bridge access token.

            Returns:
                Dict[str, Any]: Dictionary containing the response data.
            """
            resp = await self.httpRequest(
                path=EPath.BRIDGE_TOKEN.value,
                method=EMethod.GET,
                isNeedAT=False
            )

            # Waiting...
            if resp["error"] == 401 or resp["message"] == "link button not pressed":
                return

            # We got the access token?
            if resp['error'] == 0 and 'token' in resp['data']:
                self.setAT(resp['data']['token'])
            else:
                raise AccessTokenRequestError("Failed to request the access token.")

            # Access token is work?
            if await verifyAccessToken():
                _LOGGER.info("Authentication successful!")
            else:
                raise AccessTokenUnauthorized("Failed to request the access token.")

            return resp

        async def intervalFunc() -> Dict[str, Any]:
            """
            Internal function to handle interval-based attempts to get the bridge access token.
            """
            while True:
                resp = await getBridgeATHandler()
                if resp:
                    return resp
                await asyncio.sleep(interval / 1000)

        # Get access token and validate
        return await asyncio.wait_for(asyncio.gather(getBridgeATHandler(), intervalFunc()), timeout / 1000)

    async def getBridgeInfo(self) -> IResponse:
        """
        Gets the gateway information.

        Returns:
            Dict[str, Any]: Dictionary containing the response data.
        """
        return await self.httpRequest(
           path=EPath.BRIDGE.value,
           method=EMethod.GET,
           isNeedAT=False
        )

    async def updateBridgeConfig(self, volume: int) -> IResponse:
        """
        Updates the gateway configuration.

        Args:
            volume (int): System Volume value to be updated. [0-100]

        Returns:
            Dict[str, Any]: Dictionary containing the response data.
        """
        return await self.httpRequest(
            path=EPath.BRIDGE_CONFIG.value,
            method=EMethod.PUT,
            params={'volume': volume}
        )
