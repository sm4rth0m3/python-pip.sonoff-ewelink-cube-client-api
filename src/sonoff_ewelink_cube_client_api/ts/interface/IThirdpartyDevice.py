"""
Interface module: IThirdpartyDevice

This module defines the IThirdpartyDevice class.

Classes:
    IThirdpartyDevice: Represents a third-party device with its properties such as third serial number, name,
        display category, capabilities, state, manufacturer, model, firmware version, service address, and tags.
"""
#pylint: disable-msg=too-few-public-methods
#pylint: disable-msg=too-many-arguments
#pylint: disable-msg=too-many-instance-attributes

from typing import Optional, List

from ..enum.ECategory import ECategory
from .IDevice import ICapability


class IThirdpartyDevice:
    """
    Represents a third-party device.

    Attributes:
        third_serial_number (str): The third serial number of the device.
        name (str): The name of the device.
        display_category (ECategory): The display category of the device.
        capabilities (List[ICapability]): The list of capabilities associated with the device.
        state (any): The state of the device.
        manufacturer (str): The manufacturer of the device.
        model (str): The model of the device.
        firmware_version (str): The firmware version of the device.
        service_address (str): The service address of the device.
        tags (Optional[any]): The optional tags associated with the device.
    """

    def __init__(
        self,
        third_serial_number: str,
        name: str,
        display_category: ECategory,
        capabilities: List[ICapability],
        state: any,
        manufacturer: str,
        model: str,
        firmware_version: str,
        service_address: str,
        tags: Optional[any] = None,
    ):
        self.third_serial_number = third_serial_number
        self.name = name
        self.display_category = display_category
        self.capabilities = capabilities
        self.state = state
        self.manufacturer = manufacturer
        self.model = model
        self.firmware_version = firmware_version
        self.service_address = service_address
        self.tags = tags
