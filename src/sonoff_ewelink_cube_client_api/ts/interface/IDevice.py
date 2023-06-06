"""
Interface module: IDevice

This module defines the IDevice class and ICapability class.

Classes:
    ICapability: Represents a capability with its permission and optional name.
    IDevice: Represents a device with its properties.
"""
#pylint: disable-msg=too-few-public-methods
#pylint: disable-msg=too-many-arguments
#pylint: disable-msg=too-many-instance-attributes

from typing import Optional, List

from ..enum.ECapability import ECapability
from ..enum.ECategory import ECategory

#pylint: disable-msg=unused-import
from .api.IDevicesDiscoveryRequest import IDevicesDiscoveryRequest, EDiscoveryDevicesType



class ICapability:
    """
    Represents a capability.

    Attributes:
        capability (ECapability): The capability value.
        permission (str): The permission associated with the capability.
        name (Optional[str]): The optional name of the capability.
    """

    def __init__(
        self,
        capability: ECapability,
        permission: str,
        name: Optional[str] = None
    ):
        self.capability = capability
        self.permission = permission
        self.name = name


class IDevice:
    """
    Represents a device.

    Attributes:
        serial_number (str): The serial number of the device.
        name (str): The name of the device.
        manufacturer (str): The manufacturer of the device.
        model (str): The model of the device.
        firmware_version (str): The firmware version of the device.
        display_category (ECategory): The display category of the device.
        link_layer_type (Optional[str]): The optional link layer type of the device.
        capabilities (List[ICapability]): The list of capabilities associated with the device.
        state (Optional[any]): The optional state of the device.
        online (bool): The online status of the device.
        tags (Optional[any]): The optional tags associated with the device.
    """

    def __init__(
        self,
        serial_number: str,
        name: str,
        manufacturer: str,
        model: str,
        firmware_version: str,
        display_category: ECategory,
        link_layer_type: Optional[str] = None,
        capabilities: List[ICapability] = None,
        state: Optional[any] = None,
        online: bool = None,
        tags: Optional[any] = None
    ):
        self.serial_number = serial_number
        self.name = name
        self.manufacturer = manufacturer
        self.model = model
        self.firmware_version = firmware_version
        self.display_category = display_category
        self.link_layer_type = link_layer_type
        self.capabilities = capabilities or []
        self.state = state
        self.online = online
        self.tags = tags
