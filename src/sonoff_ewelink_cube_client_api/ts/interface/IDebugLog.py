"""
Module: IDebugLog

This module defines the IDebugLog class.

Classes:
    IDebugLog: Represents a debug log with its associated attributes.
"""
#pylint: disable-msg=too-few-public-methods

import datetime

class IDebugLog:
    """
    Represents a debug log request.

    Request parameters:
        - log_type (str): Log type. Possible values: 'event_log' for third-party report request log,
          'directive_log' for the directive log sent by the gateway.
        - from_index (int, optional): Start sequence number. Default is 0. Range: 0-3000.
        - start_time (str, optional): Start timestamp to query specific time. Default is 1 minute ago.
        - end_time (str, optional): End timestamp to query specific time. Default is current time.
        - limit (int, optional): Limit the number of messages to be pulled. Range: 1-50. Default is 50.
        - order (str, optional): Sort order by time range. Possible values: 'DESC' for descending order,
          'ASC' for ascending order. Default is 'DESC'.
    """

    def __init__(self, log_type: str, from_index: int = 0, start_time: str = None, end_time: str = None,
                 limit: int = None, order: str = None) -> None:
        """
        Initialize a new IDebugRequest instance.

        Args:
            log_type (str): The log type. Possible values: 'event_log', 'directive_log'.
            from_index (int, optional): The start sequence number. Default is 0.
            start_time (str, optional): The start timestamp. Default is 1 minute ago.
            end_time (str, optional): The end timestamp. Default is current time.
            limit (int, optional): The limit of messages to be pulled. Default is 50.
            order (str, optional): The sort order. Default is 'DESC'.

        Raises:
            ValueError: If any of the parameters are invalid.
        """
        self.type = self._validate_type(log_type)
        self.from_index = self._validate_from_index(from_index)
        self.start_time = self._validate_start_time(start_time)
        self.end_time = self._validate_end_time(end_time)
        self.limit = self._validate_limit(limit)
        self.order = self._validate_order(order)

    def _validate_type(self, log_type: str) -> str:
        """
        Validate the log type.

        Args:
            log_type (str): The log type.

        Returns:
            str: The validated log type.

        Raises:
            ValueError: If the log type is invalid.
        """
        if not isinstance(log_type, str):
            raise ValueError("Type must be a string.")
        return log_type

    def _validate_from_index(self, from_index: int) -> int:
        """
        Validate the from_index parameter.

        Args:
            from_index (int): The start sequence number.

        Returns:
            int: The validated start sequence number.

        Raises:
            ValueError: If the from_index is invalid.
        """
        if not isinstance(from_index, int):
            raise ValueError("from_index must be an integer.")
        return from_index

    def _validate_start_time(self, start_time: str) -> datetime.datetime:
        """
        Validate the start_time parameter.

        Args:
            start_time (str): The start timestamp.

        Returns:
            datetime.datetime: The validated start timestamp.

        Raises:
            ValueError: If the start_time is invalid.
        """
        if start_time is None:
            start_time = datetime.datetime.now() - datetime.timedelta(minutes=1)
        else:
            try:
                start_time = datetime.datetime.fromisoformat(start_time)
            except ValueError as e:
                raise ValueError("Invalid start_time value. It should be a valid timestamp.") from e
        return start_time

    def _validate_end_time(self, end_time: str) -> datetime.datetime:
        """
        Validate the end_time parameter.

        Args:
            end_time (str): The end timestamp.

        Returns:
            datetime.datetime: The validated end timestamp.

        Raises:
            ValueError: If the end_time is invalid.
        """
        if end_time is None:
            end_time = datetime.datetime.now()
        else:
            try:
                end_time = datetime.datetime.fromisoformat(end_time)
            except ValueError as e:
                raise ValueError("Invalid end_time value. It should be a valid timestamp.") from e
        return end_time

    def _validate_limit(self, limit: int) -> int:
        """
        Validate the limit parameter.

        Args:
            limit (int): The limit of messages to be pulled.

        Returns:
            int: The validated limit.

        Raises:
            ValueError: If the limit is invalid.
        """
        if limit is None:
            limit = 50
        elif not isinstance(limit, int) or limit < 1 or limit > 50:
            raise ValueError("Invalid limit value. It should be an integer between 1 and 50.")
        return limit

    def _validate_order(self, order: str) -> str:
        """
        Validate the order parameter.

        Args:
            order (str): The sort order.

        Returns:
            str: The validated sort order.

        Raises:
            ValueError: If the order is invalid.
        """
        if order is None:
            order = 'DESC'
        elif order not in ['ASC', 'DESC']:
            raise ValueError("Invalid order value. It should be 'ASC' or 'DESC'.")
        return order
