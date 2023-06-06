"""
Module: IResponse

This module defines the IResponse class representing a response object.

Classes:
    IResponse: Represents a response object with properties for error code, message, and data.
"""

from typing import Any

from ..enum.EResponse import EResponseErrorCode
from . import BaseInterface

from ..error.EDiscoveryDevice import EDiscoveryDeviceError

class IResponse(BaseInterface):
    """
    Represents a response object.

    Attributes:
        error (int): The error code of the response.
        message (str): The message of the response.
        data (any): The data of the response.
    """

    VALID_ERROR_CODES = {
        EResponseErrorCode: [device.value for device in EResponseErrorCode],
        EDiscoveryDeviceError: [device.value for device in EDiscoveryDeviceError],
    }

    def __init__(self, error: int, message: str, data: Any):
        """
        Initializes a new instance of the IResponse class.

        Args:
            error (int): The error code of the response.
            message (str): The message of the response.
            data (Any): The data of the response.
        Raises:
            ValueError: If the error code or message is invalid.
        """
        self.error = self._validate_error(error)
        self.message = self._validate_message(message)
        self.data = data

    def _validate_error(self, error: int) -> int:
        """
        Validates the error code.

        Args:
            error (int): The error code to validate.

        Returns:
            int: The validated error code.

        Raises:
            ValueError: If the error code is invalid.
        """
        if not isinstance(error, int):
            raise ValueError("Error code must be an integer.")

        for error_codes in self.VALID_ERROR_CODES:
            if error in [code.value for code in error_codes]:
                return error

        raise ValueError(f"Invalid error code: {error}")

    def _validate_message(self, message: str) -> str:
        """
        Validate the message.

        Args:
            message (str): The message to validate.

        Returns:
            str: The validated message.

        Raises:
            ValueError: If the message is empty.
            ValueError: If the message is not a string.
            ValueError: If the message is inconsistent with the error code.
        """
        if not message:
            for error_codes in self.VALID_ERROR_CODES:
                if self.error in [code.value for code in error_codes]:
                    error_code = self.error
                    error_message = error_codes.get_error_message(error_code=self.error)
                    raise ValueError(f'Error {error_code}: {error_message}')

            raise ValueError("Message cannot be empty.")

        if not isinstance(message, str):
            raise ValueError("Message must be a string.")

        if self.error == EResponseErrorCode.ERROR_SUCCESS.value:
            if message != 'success':
                raise ValueError("Inconsistent success message and error code.")

        return message

    def __str__(self) -> str:
        """
        Returns a string representation of the IResponse object.

        Returns:
            str: The string representation of the IResponse object.
        """
        return str(self.__dict__)

    def __getitem__(self, key: str) -> Any:
        """
        Enables indexing to access object attributes.

        Args:
            key (str): The attribute key to access.

        Returns:
            Any: The value of the specified attribute.

        Raises:
            KeyError: If the specified attribute does not exist.
        """
        return self.__dict__[key]

    def __getattr__(self, key: str) -> Any:
        """
        Enables attribute access to object attributes.

        Args:
            key (str): The attribute key to access.

        Returns:
            Any: The value of the specified attribute.

        Raises:
            AttributeError: If the specified attribute does not exist.
        """
        return self.__dict__[key]
