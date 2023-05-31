"""
Enumerations Modules for SONOFF eWelink CUBE.

This module defines the BaseEnum class, which is a base class for creating enumerations.
"""

from enum import Enum

class BaseEnum(Enum):
    """
    Base class for creating enumerations.

    This class extends the Enum class from the enum module and provides a custom string representation
    by overriding the __str__() method.

    Attributes:
        (No attributes)

    Methods:
        __str__(): Returns the string representation of the enumeration value.
    """

    def __str__(self):
        """
        Returns the string representation of the enumeration value.

        Returns:
            str: The string representation of the enumeration value.
        """
        return self.value
