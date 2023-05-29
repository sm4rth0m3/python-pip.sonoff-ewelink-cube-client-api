"""
Interface module: IThirdParty

This module defines the IHeader class.
This module defines the IEndpoint class.
This module defines the IThirdRequest class.

Classes:
    IHeader: Represents a header object with properties for name, message ID, and version.
    IEndpoint: Represents an endpoint object with properties for serial number and third serial number.
    IThirdRequest: Represents a third request object with an event dictionary.
"""
#pylint: disable-msg=too-few-public-methods

class IHeader:
    """
    Represents a header object.

    Attributes:
        name (str): The name of the header.
        message_id (str): The message ID of the header.
        version (str): The version of the header.
    """

    def __init__(self, name: str, message_id: str, version: str):
        self.name = name
        self.message_id = message_id
        self.version = version


class IEndpoint:
    """
    Represents an endpoint object.

    Attributes:
        serial_number (str): The serial number of the endpoint.
        third_serial_number (str): The third serial number of the endpoint.
    """

    def __init__(self, serial_number: str, third_serial_number: str):
        self.serial_number = serial_number
        self.third_serial_number = third_serial_number


class IThirdRequest:
    """
    Represents a third request object.

    Attributes:
        event (dict): The event dictionary of the third request.
    """

    def __init__(self, event: dict):
        self.event = event
