"""
Module: config/__init__.py

This module defines the config Store class for managing configurations.
"""

from ..ts.interface.IConfig import IConfig


class Store:
    """
    Class representing a configuration store.

    Attributes:
        config (IConfig): Configuration object.
    """

    ip = None
    at = None
    mac = None

    def __init__(self):
        """
        Initialize a new instance of the Store class.
        """
        self.config: IConfig

    def setConfig(self, debug: bool = None):
        """
        Set the configuration debug flag.

        Args:
            debug (bool): Debug flag value.
        """
        if debug is not None:
            self.config.debug = debug

    def setIp(self, ip: str):
        """
        Set the configuration IP address.

        Args:
            ip (str): IP address value.
        """
        self.config.ip = ip

    def setAT(self, at: str):
        """
        Set the configuration access token.

        Args:
            at (str): Access token value.
        """
        self.config.at = at

    def setMac(self, mac: str):
        """
        Set the configuration MAC address.

        Args:
            mac (str): MAC address value.
        """
        self.config.mac = mac
