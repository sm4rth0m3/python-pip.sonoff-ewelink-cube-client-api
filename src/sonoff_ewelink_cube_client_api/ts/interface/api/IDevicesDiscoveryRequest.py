"""
Module: IDevice

This module defines the Device classes.

Documentation:
  3.3 Device Management Function
  https://ewelink.cc/ewelink-cube/open-api/

Class:
    IDevicesDiscoveryRequest: Represents the device discovery configuration.
"""
#pylint: disable-msg=too-few-public-methods

from .. import BaseInterface
from ...enum.EDiscoveryDevices import EDiscoveryDevicesType


class IDevicesDiscoveryRequest(BaseInterface):
    """
    Represents the device discovery configuration.

    Request parameters:
        - enable (bool): Flag to enable or disable device discovery.
        - type (str): Searching type.

    Raises:
        ValueError: If the enable parameter is not boolean.
        ValueError: If the type parameter is not provided.

    Notes:
        Note: Only supports searching for Zigbee sub-devices now.
        Note: Zigbee sub-devices will be added automatically after searching.
              Do not need to use the "Manually Add Sub-devices" interface
    """

    def __init__(self, enable: bool, device_type: EDiscoveryDevicesType):
        """
        Initialize a new IDevicesDiscoveryRequest instance.

        Args:
            enable (bool): Flag to enable or disable device discovery.
            device_type (str): Searching type.

        Raises:
            ValueError: If the enable parameter is not boolean.
            ValueError: If the type parameter is not provided.
        """
        self.enable = self._validate_enable(enable)
        self.device_type = self._validate_device_type(device_type)

    def _validate_enable(self, enable: bool) -> bool:
        """
        Validate the enable flag.

        Args:
            enable (bool): Flag to enable or disable device discovery.

        Returns:
            bool: The validated enable flag.

        Raises:
            ValueError: If the enable parameter is not boolean.
        """
        if not isinstance(enable, bool):
            raise ValueError("Enable parameter must be a boolean value.")
        return enable

    def _validate_device_type(self, device_type: str) -> str:
        """
        Validate the device type.

        Args:
            device_type (str): Searching type.

        Returns:
            str: The validated device type.

        Raises:
            ValueError: If the type parameter is not provided.
            ValueError: If the type parameter is not valid.
        """
        if not device_type:
            raise ValueError("Device type must be provided.")

        device_type = (str(device_type)).strip()

        valid_device_types = [device.value for device in EDiscoveryDevicesType]
        if device_type not in valid_device_types:
            raise ValueError(f"Invalid device type: {device_type}")

        return device_type
