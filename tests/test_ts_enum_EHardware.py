"""
Test module for EHardware enumerations.
"""

import unittest

from src.sonoff_ewelink_cube_client_api.ts.enum.EHardware import ESpeakerTypes


class TestESpeakerTypes(unittest.TestCase):
    """
    Test cases for ESpeakerTypes enumeration.
    """

    # Define expected values as a list of (expected_value, enum_value) tuples
    expected_values = [
        ("play_beep", ESpeakerTypes.PLAY_BEEP),
        ("play_sound", ESpeakerTypes.PLAY_SOUND)
    ]

    def test_enum_values(self):
        """
        Test that the enumeration values have the expected string representation.
        """
        self.assertEqual(len(self.expected_values), len(ESpeakerTypes))

        for expected_value in self.expected_values:
            expected_str, enum_value = expected_value
            self.assertEqual(str(enum_value), expected_str)

    def test_enum_parameters(self):
        """
        Test that all expected parameters exist in the enumeration.
        """
        self.assertEqual(len(self.expected_values), len(ESpeakerTypes))

        for parameter in ESpeakerTypes:
            self.assertIn(parameter, [enum_value for _, enum_value in self.expected_values])

if __name__ == '__main__':
    unittest.main()
