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
