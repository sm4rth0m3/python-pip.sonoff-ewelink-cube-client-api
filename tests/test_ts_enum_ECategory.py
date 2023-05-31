"""
Test module for ECategory enumeration.
"""

import unittest

from src.sonoff_ewelink_cube_client_api.ts.enum.ECategory import ECategory


class TestECategory(unittest.TestCase):
    """
    Test cases for ECategory enumeration.
    """

    # Define expected values as a list of (expected_value, enum_value) tuples
    expected_values = [
        ("plug", ECategory.PLUG),
        ("switch", ECategory.SWITCH),
        ("light", ECategory.LIGHT),
        ("curtain", ECategory.CURTAIN),
        ("contactSensor", ECategory.CONTACT_SENSOR),
        ("motionSensor", ECategory.MOTION_SENSOR),
        ("temperatureSensor", ECategory.TEMPERATURE_SENSOR),
        ("humiditySensor", ECategory.HUMIDITY_SENSOR),
        ("temperatureAndHumiditySensor", ECategory.TEMPERATURE_HUMIDITY_SENSOR),
        ("waterLeakDetector", ECategory.WATER_LEAK_DETECTOR),
        ("smokeDetector", ECategory.SMOKE_DETECTOR),
        ("button", ECategory.BUTTON)
    ]

    def test_enum_values(self):
        """
        Test that the enumeration values have the expected string representation.
        """
        self.assertEqual(len(self.expected_values), len(ECategory))

        for expected_value in self.expected_values:
            expected_str, enum_value = expected_value
            self.assertEqual(str(enum_value), expected_str)

    def test_enum_parameters(self):
        """
        Test that all expected parameters exist in the enumeration.
        """
        self.assertEqual(len(self.expected_values), len(ECategory))

        for parameter in ECategory:
            self.assertIn(parameter, [enum_value for _, enum_value in self.expected_values])

if __name__ == "__main__":
    unittest.main()
