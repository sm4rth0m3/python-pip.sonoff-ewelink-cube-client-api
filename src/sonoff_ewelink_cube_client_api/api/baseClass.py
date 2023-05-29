"""
Module: baseClass

This module provides the BaseClass API.

Classes:
    BaseClass: Represents the BaseClass API.

Usage:
    from .baseClass import BaseClass
"""

from typing import Dict, Any

import logging

from ..ts.enum.EMethod import EMethod
from ..ts.enum.EPath import EPath

from .baseClassBridge import BaseClassBridge
from .baseClassDevice import BaseClassDevice
from .baseClassHardware import BaseClassHardware
from .baseClassSse import BaseClassSse

_LOGGER = logging.getLogger(__name__)


class BaseClass(BaseClassBridge, BaseClassDevice, BaseClassHardware, BaseClassSse):
    """
    Represents the BaseClass API.

    Inherits:
        BaseClassSse: Base class for APIs that support Server-Sent Events (SSE).

    Attributes:
        ip (str): IP address of the device.
        at (str): Access token for the gateway.
        debug (bool): Debug mode flag.

    Methods:
        __init__(ip: str, at: str = '', debug: bool = False): Initializes the BaseClass object.
        setIp(ip: str): Sets the IP address of the device.
        getIp() -> str: Gets the IP address of the device.
        setAT(at: str): Sets the access token for the gateway.
        getAt() -> str: Gets the access token for the gateway.
        sendCommandToDevice(deviceId: str, command: Dict[str, Any]) -> Dict[str, Any]: Sends a command to a device.
        getDebugLog() -> Dict[str, Any]: Gets the debug log interface.
    """

    def __init__(self, ip: str, at: str = '', debug: bool = False):
        """
        Initializes the BaseClass object.

        Parameters:
            ip (str): IP address of the device.
            at (str): Access token for the gateway.
            debug (bool): Debug mode flag.
        """
        super().__init__()
        self.ip: str = ip
        self.at: str = at
        self.debug: bool = debug

    def setIp(self, ip: str):
        """
        Sets the IP address of the device.

        Parameters:
            ip (str): IP address of the device.
        """
        self.ip = ip

    def getIp(self) -> str:
        """
        Gets the IP address of the device.

        Returns:
            str: IP address of the device.
        """
        return self.ip

    def setAT(self, at: str):
        """
        Sets the access token for the gateway.

        Parameters:
            at (str): Access token for the gateway.
        """
        self.at = at

    def getAt(self) -> str:
        """
        Gets the access token for the gateway.

        Returns:
            str: Access token for the gateway.
        """
        return self.at

    async def sendCommandToDevice(self, deviceId: str, command: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates specific device information or state.

        Args:
            deviceId (str): ID of the device to send the command to.
            command (Dict[str, Any]): Command to be sent to the device.

        Returns:
            Dict[str, Any]: Dictionary containing the response data.
        """
        return await self.httpRequest(
            path=EPath.DEVICE.value,
            method=EMethod.PUT,
            params={'deviceId': deviceId, 'command': command}
        )

    async def getDebugLog(self) -> Dict[str, Any]:
        """
        Gets the debug log interface.

        Returns:
            Dict[str, Any]: Dictionary containing the response data.
        """
        return await self.httpRequest(
            path=EPath.DEBUG_LOG.value,
            method=EMethod.GET
        )
