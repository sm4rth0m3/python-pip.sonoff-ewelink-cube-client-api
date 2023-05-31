"""
Test module for EResponseErrorCode enumeration.
"""

import unittest

from src.sonoff_ewelink_cube_client_api.ts.enum.EResponse import EResponseErrorCode


class TestEResponseErrorCode(unittest.TestCase):
    """
    Test cases for EResponseErrorCode enumeration.
    """

    def test_error_custom(self):
        """
        Test case for ERROR_CUSTOM error code.
        """
        self.assertEqual(EResponseErrorCode.ERROR_CUSTOM.value, -1)

    def test_error_success(self):
        """
        Test case for ERROR_SUCCESS error code.
        """
        self.assertEqual(EResponseErrorCode.ERROR_SUCCESS.value, 0)

    def test_error_parameter(self):
        """
        Test case for ERROR_PARAMETER error code.
        """
        self.assertEqual(EResponseErrorCode.ERROR_PARAMETER.value, 400)

    def test_error_authentication(self):
        """
        Test case for ERROR_AUTHENTICATION error code.
        """
        self.assertEqual(EResponseErrorCode.ERROR_AUTHENTICATION.value, 401)

    def test_error_server_exception(self):
        """
        Test case for ERROR_SERVER_EXCEPTION error code.
        """
        self.assertEqual(EResponseErrorCode.ERROR_SERVER_EXCEPTION.value, 500)

    def test_error_invalid_code(self):
        """
        Test case for invalid error code.
        """
        self.assertRaises(AttributeError)

if __name__ == '__main__':
    unittest.main()
