"""
Enumeration: EMethod

This enumeration defines different HTTP methods.

Enumerations:
    EMethod: Represents various HTTP methods.
"""

from enum import Enum


class EMethod(Enum):
    """
    Represents various HTTP methods.

    Enumerations:
        GET: HTTP GET method.
        PUT: HTTP PUT method.
        POST: HTTP POST method.
        DELETE: HTTP DELETE method.
    """
    GET = "get"
    PUT = "put"
    POST = "post"
    DELETE = "delete"
