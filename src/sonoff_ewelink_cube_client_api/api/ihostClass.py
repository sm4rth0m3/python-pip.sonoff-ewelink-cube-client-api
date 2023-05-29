"""
API Module: ihostClass

This module provides the IHostClass API.

Classes:
    IHostClass: Represents the IHostClass API.

Usage:
    from .ihostClass import IHostClass
"""

from .baseClass import BaseClass


class IHostClass(BaseClass):
    """
    Represents the IHostClass API.

    Inherits:
        BaseClass: Base class for the API.

    Methods:
        __init__(ip: str, at: str = None, debug: bool = False): Initializes the IHostClass object.
    """

    def __init__(self, ip: str, at: str = None, debug: bool = False):
        """
        Initializes the IHostClass object.

        Parameters:
            ip (str): The IP address of the host.
            at (str): The access token.
            debug (bool): Whether to enable debug mode.

        """
        super().__init__(ip=ip, at=at, debug=debug)
