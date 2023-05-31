"""
Test module for EMethod enumeration.
"""

import unittest

from src.sonoff_ewelink_cube_client_api.ts.enum.EMethod import EMethod


class TestEMethod(unittest.TestCase):
    """
    Unit tests for the EMethod enumeration.
    """

    # Define expected values as a list of (expected_value, enum_value) tuples
    expected_values = [
        ("get", EMethod.GET),  # GET method
        ("put", EMethod.PUT),  # PUT method
        ("post", EMethod.POST),  # POST method
        ("delete", EMethod.DELETE)  # DELETE method
    ]

    def test_enum_values(self):
        """
        Test that the enumeration values have the expected string representation.
        """
        self.assertEqual(len(self.expected_values), len(EMethod))

        for expected_value in self.expected_values:
            expected_str, enum_value = expected_value
            self.assertEqual(str(enum_value), expected_str)

    def test_enum_parameters(self):
        """
        Test that all expected parameters exist in the enumeration.
        """
        self.assertEqual(len(self.expected_values), len(EMethod))

        for parameter in EMethod:
            self.assertIn(parameter, [enum_value for _, enum_value in self.expected_values])

if __name__ == "__main__":
    unittest.main()
