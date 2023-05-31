"""
Module: EHardware

This enumeration defines different Hardware devices.

Enumerations:
    ESpeakerTypes: Enumeration of speaker types.
"""

from . import BaseEnum


class ESpeakerTypes(BaseEnum):
    """
    Enumeration of speaker types.

    Enumerations:
        PLAY_BEEP: Play the beep.
        PLAY_SOUND: Play the sound.
    """

    PLAY_BEEP = "play_beep"
    PLAY_SOUND = "play_sound"
