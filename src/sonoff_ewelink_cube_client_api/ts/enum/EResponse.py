"""
Module: EResponce

This enumeration defines different API Response error codes.

Classes:
  EResponseErrorCode: Enumeration of API error codes.
"""
from . import BaseEnum


class EResponseErrorCode(BaseEnum):
    """
    Enum class representing error codes for response objects.

    Attributes:
        ERROR_CUSTOM (int): Custom error code (-1), unofficial option.
        ERROR_SUCCESS (int): Success error code (0).
        ERROR_PARAMETER (int): Parameter error code (400).
        ERROR_AUTHENTICATION (int): Authentication failed error code (401).
        ERROR_SERVER_EXCEPTION (int): Server exception error code (500).
    """
    ERROR_CUSTOM = -1
    ERROR_SUCCESS = 0
    ERROR_PARAMETER = 400
    ERROR_AUTHENTICATION = 401
    ERROR_SERVER_EXCEPTION = 500

    @staticmethod
    def get_error_message(error_code: int) -> str:
        """
        Get the error message for the given error code.

        Args:
            error_code (int): The error code.

        Returns:
            str: The corresponding error message.

        Raises:
            KeyError: If the error code is not found in the error messages.
        """
        __error_messages = {
             -1: "Custom error message",
              0: "success",
            400: "Invalid parameter",
            401: "Authentication failed",
            500: "Internal server error"
        }

        return __error_messages[error_code]
