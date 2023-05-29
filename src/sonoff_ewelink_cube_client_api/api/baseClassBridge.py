"""
Module: baseClass

This module provides the BaseClassBridge API.

Classes:
    BaseClassBridge: Represents the BaseClassBridge API.

Usage:
    from .baseClassBridge import BaseClassBridge
"""

from typing import Any, Awaitable, Dict, Tuple

import asyncio

from ..ts.enum.EMethod import EMethod
from ..ts.enum.EPath import EPath
from ..config import Store
from ..utils.httpUtils import httpUtils


class BaseClassBridge(Store, httpUtils):
    """
    BaseClassBridge API.

    Attributes:
        interval (int): Interval for event subscription.
        timeout (int): Timeout for getting the bridge access token.

    Methods:
        getBridgeAT(timeout: int = 120000, interval: int = 2000) -> Dict[str, Any]: Gets the bridge access token.
        updateBridgeConfig(volume: int) -> Dict[str, Any]: Updates the gateway configuration.
        getBridgeInfo() -> Dict[str, Any]: Gets the gateway information.
    """
    interval = None
    timeout = None

    async def getBridgeAT(self, timeout: int = 120000, interval: int = 2000) -> Dict[str, Any]:
        """
        Gets the bridge access token.

        Args:
            timeout (int): Timeout in milliseconds (default: 120000).
            interval (int): Interval between attempts in milliseconds (default: 2000).

        Returns:
            Dict[str, Any]: Dictionary containing the response data.
        """

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

            # Set access token
            if resp['error'] == 0:
                if 'token' in resp['data']:
                    self.setAT(resp['data']['token'])
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

        return await asyncio.wait_for(asyncio.gather(getBridgeATHandler(), intervalFunc()), timeout / 1000)


    async def updateBridgeConfig(self, volume: int) -> Dict[str, Any]:
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

    async def getBridgeInfo(self) -> Dict[str, Any]:
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
