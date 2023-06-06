"""
Module: IBridge

This module defines the Bridge classes.

Documentation:
  3.1 Bridge Function
  https://ewelink.cc/ewelink-cube/open-api/

Class:
    IBridgeConfig: Represents the bridge configuration.
"""
#pylint: disable-msg=too-few-public-methods

class IBridgeConfig:
    """
    Represents the bridge configuration.

    Request parameters:
        - volume (int, optional): System volume. Valid range is 0 to 100.
    """

    def __init__(self, volume=None):
        """
        Initialize a new IBridgeConfig instance.

        Args:
            volume (int, optional): The system volume. Default is None.
        """
        self.volume = self._validate_volume(volume)

    def _validate_volume(self, volume):
        """
        Validate the system volume.

        Args:
            volume (int): The system volume.

        Returns:
            int: The validated system volume.

        Raises:
            ValueError: If the volume is not in the range of 0-100.
        """
        if not 0 <= volume <= 100:
            raise ValueError("Volume must be in the range of 0-100.")
        return volume
