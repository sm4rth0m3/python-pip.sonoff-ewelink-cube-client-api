"""
Interfaces Modules for SONOFF eWelink CUBE.
"""

from typing import Any

class BaseInterface:
    """
    Base class for creating interfaces.
    """

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
