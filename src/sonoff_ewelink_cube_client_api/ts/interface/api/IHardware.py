"""
Module: IHardware

This module defines the hardware API endpoint objects.

Documentation:
  3.2 Hardware Function
  https://ewelink.cc/ewelink-cube/open-api/

Class:
    IBeepObject: Represents a beep object with supported beep names.
    ISoundObject: Represents a sound object with supported sound names.
"""
#pylint: disable-msg=too-few-public-methods


class IBeepObject:
    """
    Represents a beep object.

    Attributes:
        SUPPORTED_BEEPS (list): List of supported beep names.

    Supported beep options:
    - 'bootComplete': System startup completed
    - 'networkConnected': Network connected
    - 'networkDisconnected': Network disconnected
    - 'systemShutdown': System shutdown
    - 'deviceDiscovered': Discover device
    - 'systemArmed': System armed enable
    - 'systemDisarmed': System armed disable
    - 'factoryReset': Reset device
    """

    SUPPORTED_BEEPS = [
        'bootComplete', 'networkConnected', 'networkDisconnected',
        'systemShutdown', 'deviceDiscovered', 'systemArmed',
        'systemDisarmed', 'factoryReset'
    ]

    def __init__(self, name: str, volume: int):
        self.name = self._validate_name(name)
        self.volume = self._validate_volume(volume)

    def _validate_name(self, name: str) -> str:
        if name not in self.SUPPORTED_BEEPS:
            raise ValueError("Unsupported beep name.")
        return name

    def _validate_volume(self, volume: int) -> int:
        if not 0 <= volume <= 100:
            raise ValueError("Volume must be in the range of 0-100.")
        return volume


class ISoundObject:
    """
    Represents a sound object.

    Attributes:
        SUPPORTED_SOUNDS (list): List of supported sound names.

    Supported sound options:
    - 'alert1': Alarm Sound 1
    - 'alert2': Alarm Sound 2
    - 'alert3': Alarm Sound 3
    - 'alert4': Alarm Sound 4
    - 'alert5': Alarm Sound 5
    - 'doorbell1': Doorbell Sound 1
    - 'doorbell2': Doorbell Sound 2
    - 'doorbell3': Doorbell Sound 3
    - 'doorbell4': Doorbell Sound 4
    - 'doorbell5': Doorbell Sound 5
    - 'alarm1': Alarm Sound 1
    - 'alarm2': Alarm Sound 2
    - 'alarm3': Alarm Sound 3
    - 'alarm4': Alarm Sound 4
    - 'alarm5': Alarm Sound 5
    """

    SUPPORTED_SOUNDS = [
        'alert1', 'alert2', 'alert3', 'alert4', 'alert5',
        'doorbell1', 'doorbell2', 'doorbell3', 'doorbell4', 'doorbell5',
        'alarm1', 'alarm2', 'alarm3', 'alarm4', 'alarm5'
    ]

    def __init__(self, name: str, volume: int, countdown: int):
        """
        Initialize a SoundObject instance.

        Args:
            name (str): The name of the sound.
            volume (int): The volume of the sound.
            countdown (int): The countdown of the sound.
        """
        self.name = self._validate_name(name)
        self.volume = self._validate_volume(volume)
        self.countdown = self._validate_countdown(countdown)

    def _validate_name(self, name: str) -> str:
        """
        Validate the name of the sound.

        Args:
            name (str): The name of the sound.

        Returns:
            str: The validated name of the sound.

        Raises:
            ValueError: If the name is not in the list of supported sounds.
        """
        if name not in self.SUPPORTED_SOUNDS:
            raise ValueError("Unsupported sound name.")
        return name

    def _validate_volume(self, volume: int) -> int:
        """
        Validate the volume of the sound.

        Args:
            volume (int): The volume of the sound.

        Returns:
            int: The validated volume of the sound.

        Raises:
            ValueError: If the volume is not in the range of 0-100.
        """
        if not 0 <= volume <= 100:
            raise ValueError("Volume must be in the range of 0-100.")
        return volume

    def _validate_countdown(self, countdown: int) -> int:
        """
        Validate the countdown of the sound.

        Args:
            countdown (int): The countdown of the sound.

        Returns:
            int: The validated countdown of the sound.

        Raises:
            ValueError: If the countdown is not in the range of 0-1799.
        """
        if not 0 <= countdown <= 1799:
            raise ValueError("Countdown must be in the range of 0-1799.")
        return countdown
