"""
Module: baseClassHardware

This module provides the BaseClassHardware API.

Classes:
    BaseClassHardware: Represents the BaseClassHardware API.

Usage:
    from .baseClassHardware import BaseClassHardware
"""

from typing import Dict, Any

from ..ts.enum.EMethod import EMethod
from ..ts.enum.EPath import EPath
from ..utils.httpUtils import httpUtils


class BaseClassHardware(httpUtils):
    """
    Represents the BaseClassHardware API.

    Methods:
        rebootBridge() -> Dict[str, Any]: Reboots the gateway.
        setSpeaker(volume: int) -> Dict[str, Any]: Controls the speaker.
    """

    async def rebootBridge(self) -> Dict[str, Any]:
        """
        Reboots the gateway.

        Returns:
            Dict[str, Any]: Dictionary containing the response data.
        """
        return await self.httpRequest(
            path=EPath.HARDWARE_REBOOT.value,
            method=EMethod.POST,
        )

    async def setSpeaker(self, play_type: str, sound: any, beep: any) -> Dict[str, Any]:
        """
        Controls the speaker.

        Args:
            play_type (str): Play sound or beep.
            sound (any): SoundObject.
            beep (any): BeepObject.

        Returns:
            Dict[str, Any]: Dictionary containing the response data.
        """
        return await self.httpRequest(
            path=EPath.HARDWARE_SPEAKER.value,
            method=EMethod.POST,
            params={'type': play_type, 'sound': sound, 'beep': beep}
        )
