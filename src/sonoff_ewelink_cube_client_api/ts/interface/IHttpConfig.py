"""
Interface module: IHttpConfig

This module defines the IHttpConfig class.

Classes:
    IHttpConfig: Represents an HTTP configuration with properties.
"""
#pylint: disable-msg=too-few-public-methods

from typing import Optional

from ..enum.EMethod import EMethod


class IHttpConfig:
    """
    Represents an HTTP configuration.

    Attributes:
        path (str): The path of the HTTP request.
        method (EMethod): The HTTP method.
        params (Optional[any]): The optional parameters of the HTTP request.
        isNeedAT (bool): Indicates if authentication token is required.
    """

    def __init__(
        self,
        path: str,
        method: EMethod,
        params: Optional[any] = None,
        isNeedAT: bool = False
    ):
        self.path = path
        self.method = method
        self.params = params
        self.isNeedAT = isNeedAT
