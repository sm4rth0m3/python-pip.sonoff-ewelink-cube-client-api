"""
Module for defining custom exceptions related to API access and responses.
"""

class AccessTokenRequestError(Exception):
    """
    Exception raised for errors that occur during access token requests.
    """


class AccessTokenUnauthorized(Exception):
    """
    Exception raised when an access token is unauthorized.
    """
