"""
Module: EDiscoveryDevices

This module defines an enumeration class representing sub-devices.

Classes:
    EDiscoveryDevicesType: Enum class representing types of discovery devices.
    ESubDevicesError: Enum class representing sub-devices errors.
"""

from . import BaseEnum


class EDiscoveryDevicesType(BaseEnum):
    """
    Enum class representing types of discovery devices.
    """
    TYPE_ZIGBEE = "zigbee"
