"""
Test module for ECapability enumeration.
"""

import unittest

from src.sonoff_ewelink_cube_client_api.ts.enum.ECapability import ECapability


class ECapabilityTest(unittest.TestCase):
    """
    Test cases for ECapability enumeration.
    """

    # Define expected values as a list of (expected_value, enum_value) tuples
    expected_values = [
        ("power", ECapability.POWER),
        ("rssi", ECapability.RSSI),
        ("ota", ECapability.OTA),
        ("detect", ECapability.DETECT),
        ("battery", ECapability.BATTERY),
        ("toggle", ECapability.TOGGLE),
        ("percentage", ECapability.PERCENTAGE),
        ("motor-control", ECapability.MOTOR_CONTROL),
        ("motor-reverse", ECapability.MOTOR_REVERSE),
        ("motor-clb", ECapability.MOTOR_CLB),
        ("temperature", ECapability.TEMPERATURE),
        ("humidity", ECapability.HUMIDITY),
        ("press", ECapability.PRESS),
        ("color-rgb", ECapability.COLOR_RGB),
        ("color-temperature", ECapability.COLOR_TEMPERATURE),
        ("brightness", ECapability.BRIGHTNESS),
        ("camera-stream", ECapability.CAMERA_STREAM),
        ("startup", ECapability.STARTUP)
    ]

    def test_enum_values(self):
        """
        Test that the enumeration values have the expected string representation.
        """
        self.assertEqual(len(self.expected_values), len(ECapability))

        for expected_value in self.expected_values:
            expected_str, enum_value = expected_value
            self.assertEqual(str(enum_value), expected_str)

    def test_enum_parameters(self):
        """
        Test that all expected parameters exist in the enumeration.
        """
        self.assertEqual(len(self.expected_values), len(ECapability))

        for parameter in ECapability:
            self.assertIn(parameter, [enum_value for _, enum_value in self.expected_values])

if __name__ == "__main__":
    unittest.main()
