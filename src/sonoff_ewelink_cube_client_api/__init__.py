"""
Module: ewelink_cube

This module provides classes for interacting with eWeLink Cube APIs.

Classes:
    EWelinkCube: The main class for creating eWeLink Cube APIs.
"""
#pylint: disable-msg=too-few-public-methods

import logging
import os

from .api.ihostClass import IHostClass
from .api.nspanelproClass import NSPanelProClass

# Set logger level
if 'LOG_LEVEL' in os.environ:
    log_level = os.environ['LOG_LEVEL']
else:
    log_level = logging.INFO
logging.basicConfig(level=log_level)


class EWelinkCube:
    """
    The main class for creating eWeLink Cube APIs.
    """

    def create_api(self, api_name, **args):
        """
        Create an instance of the specified API.

        Args:
            api_name (str): The name of the API.
            **args: Additional arguments to be passed to the API constructor.

        Returns:
            object: An instance of the specified API.

        Raises:
            ValueError: If the API name is invalid.
        """
        if api_name == 'iHost':
            return IHostClass(**args)

        if api_name == 'nsPanelPro':
            return NSPanelProClass(**args)

        raise ValueError("Invalid API name")
