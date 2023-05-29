"""
Interface module: IConfig

This module defines the IConfig class, which represents a configuration object.

Classes:

    IConfig: Configuration class with properties for IP address, access token, MAC address, and debug mode.
"""
#pylint: disable-msg=too-few-public-methods

import aiohttp


class IConfig:
    """
    Represents a configuration object.

    Attributes:
        ip (str): The IP address associated with the configuration.
        at (str): The access token associated with the configuration.
        mac (str): The MAC address associated with the configuration.
        debug (bool): The debug mode setting of the configuration.
    """

    def __init__(self, ip: str, at: str, mac: str, debug: bool, session: aiohttp.ClientSession):
        self.ip = ip
        self.at = at
        self.mac = mac
        self.debug = debug
        self.session = session
