"""
Module: IDebugLog

This module defines the IDebugLog class.

Classes:
    IDebugLog: Represents a debug log with its associated attributes.
"""
#pylint: disable-msg=too-few-public-methods

class IDebugLog:
    """
    Represents a debug log.

    Attributes:
        serial_number (str): The serial number associated with the debug log.
        type (str): The type of the debug log.
        from_index (int): The starting index of the debug log.
        start_time (int): The start time of the debug log.
        end_time (int): The end time of the debug log.
        limit (int): The limit of the debug log.
        order (str): The order of the debug log.
    """

    def __init__(
        self,
        serial_number: str,
        log_type: str,
        from_index: int = None,
        start_time: int = None,
        end_time: int = None,
        limit: int = None,
        order: str = None,
    ):
        self.serial_number = serial_number
        self.type = log_type
        self.from_index = from_index
        self.start_time = start_time
        self.end_time = end_time
        self.limit = limit
        self.order = order
