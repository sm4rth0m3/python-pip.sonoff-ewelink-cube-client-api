"""
Module: EHardware

This module defines the EHardware classes.

Enumerations:
    - ESpeakerTypes: Enumeration of speaker types.
"""

from enum import Enum


class ESpeakerTypes(Enum):
    """
    Enumeration of speaker types.

    Enumerations:
        PLAY_BEEP: Play the beep.
        PLAY_SOUND: Play the sound.
    """
    PLAY_BEEP = "play_beep"
    PLAY_SOUND = "play_sound"

    def __str__(self):
        return self.value
