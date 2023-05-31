"""
Test module for EPath enumeration.
"""

import unittest

from src.sonoff_ewelink_cube_client_api.ts.enum.EPath import EPath


class TestEPath(unittest.TestCase):
    """
    Unit tests for the EPath enumeration.
    """

    # Define expected values as a list of (expected_path, enum_value) tuples
    expected_values = [
        ("/open-api", EPath.ROOT),  # Root API path
        ("/v1/rest", EPath.V1),  # API v1 path
        ("/v1/sse/bridge", EPath.SSE),  # SSE API path for bridge
        ("/bridge", EPath.BRIDGE),  # Bridge API path
        ("/bridge/access_token", EPath.BRIDGE_TOKEN),  # Bridge access token API path
        ("/bridge/runtime", EPath.BRIDGE_RUNTIME),  # Bridge runtime API path
        ("/bridge/config", EPath.BRIDGE_CONFIG),  # Bridge configuration API path
        ("/hardware/reboot", EPath.HARDWARE_REBOOT),  # Hardware reboot API path
        ("/hardware/speaker", EPath.HARDWARE_SPEAKER),  # Hardware speaker API path
        ("/devices/discovery", EPath.DEVICE_DISCOVERY),  # Device discovery API path
        ("/devices", EPath.DEVICE),  # Device API path
        ("/thirdparty/event", EPath.THIRD_PARTY),  # Third-party event API path
        ("/thirdparty/debug-log", EPath.DEBUG_LOG)  # Debug log API path
    ]

    def test_enum_values(self):
        """
        Test that the enumeration values have the expected string representation.
        """
        self.assertEqual(len(self.expected_values), len(EPath))

        for expected_value in self.expected_values:
            expected_path, enum_value = expected_value
            self.assertEqual(str(enum_value), expected_path)

    def test_enum_parameters(self):
        """
        Test that all expected parameters exist in the enumeration.
        """
        self.assertEqual(len(self.expected_values), len(EPath))

        for parameter in EPath:
            self.assertIn(parameter, [enum_value for _, enum_value in self.expected_values])

if __name__ == "__main__":
    unittest.main()
