"""
Test module for BaseEnum enumeration.
"""

import unittest

from src.sonoff_ewelink_cube_client_api.ts.enum import BaseEnum


class BaseEnumTest(unittest.TestCase):
    """
    Test cases for BaseEnumTest enumeration.
    """

    def test_str_representation(self):
        """Test string representation of enumeration values"""
        class MyEnum(BaseEnum):
            """Test class"""
            VALUE1 = "First Value"
            VALUE2 = "Second Value"

        self.assertEqual(str(MyEnum.VALUE1), "First Value")
        self.assertEqual(str(MyEnum.VALUE2), "Second Value")

    def test_enum_uniqueness(self):
        """Test uniqueness of enumeration values"""
        class MyEnum(BaseEnum):
            """Test class"""
            VALUE1 = "First Value"
            VALUE2 = "Second Value"

        unique_values = set(member.value for member in MyEnum)
        self.assertEqual(len(unique_values), len(MyEnum))

    def test_enum_iteration(self):
        """
        Test iteration over enumeration values
        """
        class MyEnum(BaseEnum):
            """Test class"""
            VALUE1 = "First Value"
            VALUE2 = "Second Value"

        enum_values = [member.value for member in MyEnum]
        self.assertListEqual(enum_values, ["First Value", "Second Value"])

if __name__ == "__main__":
    unittest.main()
