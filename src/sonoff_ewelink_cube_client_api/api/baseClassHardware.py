"""
Module: baseClassHardware

This module provides the BaseClassHardware API.

Classes:
    BaseClassHardware: Represents the BaseClassHardware API.

Usage:
    from .baseClassHardware import BaseClassHardware
"""

from typing import Optional, Union

from ..ts.enum.EHardware import ESpeakerTypes
from ..ts.enum.EMethod import EMethod
from ..ts.enum.EPath import EPath
from ..ts.interface.api.IHardware import IBeepObject, ISoundObject
from ..ts.interface.IResponse import IResponse
from ..utils.httpUtils import httpUtils


class BaseClassHardware(httpUtils):
    """
    Represents the BaseClassHardware API.

    Methods:
        rebootBridge() -> Dict[str, Any]: Reboots the gateway.
        setSpeaker(volume: int) -> Dict[str, Any]: Controls the speaker.
    """

    async def rebootBridge(
            self
    ) -> IResponse:
        """
        Reboot the gateway.

        Returns:
            IResponse: IResponse object containing the response data.
        """
        return await self.httpRequest(
            path=EPath.HARDWARE_REBOOT.value,
            method=EMethod.POST,
        )

    async def controlSpeaker(
            self,
            play_type: Union[ESpeakerTypes, str],
            sound: Optional[ISoundObject] = None,
            beep: Optional[IBeepObject] = None
    ) -> IResponse:
        """
        Controls the speaker.

        Args:
            play_type (Union[ESpeakerTypes, str]): Specifies the playback type as ESpeakerTypes value or string.
            sound (Optional[ISoundObject]): The sound object to play. Required if the play_type is 'PLAY_SOUND'.
            beep (Optional[IBeepObject]): The beep object to play. Required if the play_type is 'PLAY_BEEP'.

        Returns:
            IResponse: IResponse object containing the response data.

        Raises:
            ValueError: If the play_type is invalid.
            ValueError: If the sound parameter is missing for 'PLAY_SOUND'.
            ValueError: If the beep parameter is missing for 'PLAY_BEEP'.
        """
        play_type = str(play_type)

        # Validate input
        if play_type not in [speaker_type.value for speaker_type in ESpeakerTypes]:
            raise ValueError(f"Invalid play_type value: {play_type}")
        if play_type == ESpeakerTypes.PLAY_SOUND.value and sound is None:
            raise ValueError("Sound parameter is required for PLAY_SOUND.")
        if play_type == ESpeakerTypes.PLAY_BEEP.value and beep is None:
            raise ValueError("Beep parameter is required for PLAY_BEEP.")

        # Prepare parameters
        params = {'type': str(play_type)}
        if play_type == ESpeakerTypes.PLAY_SOUND.value:
            params["sound"] = sound.__dict__ if isinstance(sound, ISoundObject) else sound
        if play_type == ESpeakerTypes.PLAY_BEEP.value:
            params["beep"] = beep.__dict__ if isinstance(beep, IBeepObject) else beep

        return await self.httpRequest(
            path=EPath.HARDWARE_SPEAKER.value,
            method=EMethod.POST,
            params=params
        )
