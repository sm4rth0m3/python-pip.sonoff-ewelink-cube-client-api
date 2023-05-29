"""
API Module: nspanelproClass

This module provides the NSPanelProClass API.

Classes:
    NSPanelProClass: Represents the NSPanelProClass API.

Usage:
    from .nspanelproClass import NSPanelProClass
"""

from .baseClass import BaseClass


class NSPanelProClass(BaseClass):
    """
    Represents the NSPanelProClass API.

    Inherits:
        BaseClass: Base class for the API.

    Methods:
        __init__(ip: str, at: str = None, debug: bool = False): Initializes the NSPanelProClass object.
    """

    def __init__(self, ip: str, at: str = None, debug: bool = False):
        """
        Initializes the NSPanelProClass object.

        Parameters:
            ip (str): The IP address of the host.
            at (str): The access token.
            debug (bool): Whether to enable debug mode.

        """
        super().__init__(ip=ip, at=at, debug=debug)
