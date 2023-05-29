"""
Interface module: IResponse

This module defines the IResponse class.

Classes:
    IResponse: Represents a response object with properties for error code, message, and data.
"""
#pylint: disable-msg=too-few-public-methods

class IResponse:
    """
    Represents a response object.

    Attributes:
        error (int): The error code of the response.
        msg (str): The message of the response.
        data (any): The data of the response.
    """

    def __init__(self, error: int, msg: str, data: any):
        self.error = error
        self.msg = msg
        self.data = data
