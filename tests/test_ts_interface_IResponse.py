"""
Test module for IResponse interface.
"""

import unittest

from src.sonoff_ewelink_cube_client_api.ts.enum.EResponse import EResponseErrorCode
from src.sonoff_ewelink_cube_client_api.ts.interface.IResponse import IResponse

class TestIResponse(unittest.TestCase):
    """
    Test cases for IResponse class.
    """

    def test_valid_response(self):
        """
        Test case for a valid response.
        """
        # Arrange
        error_code = EResponseErrorCode.ERROR_SUCCESS.value
        data = {"token": "376310da-7adf-4521-b18c-5e0752cfff8d"}
        message = "success"

        # Act
        response = IResponse(error_code, message, data)

        # Assert
        self.assertEqual(response.error, error_code)
        self.assertEqual(response.data, data)
        self.assertEqual(response.message, message)

    def test_invalid_response_error_code(self):
        """
        Test case for an invalid response error code.
        """
        # Arrange
        error_code = 999
        data = {}
        message = "invalid error code"

        # Act & Assert
        with self.assertRaises(ValueError):
            IResponse(error_code, message, data)

    def test_invalid_response_message(self):
        """
        Test case for an invalid response message.
        """
        # Arrange
        error_code = EResponseErrorCode.ERROR_SUCCESS.value
        data = {}
        message = ""

        # Act & Assert
        with self.assertRaises(ValueError):
            IResponse(error_code, message, data)

    def test_inconsistent_success_message(self):
        """
        Test case for an inconsistent success message.
        """
        # Arrange
        error_code = EResponseErrorCode.ERROR_SUCCESS.value
        data = {}
        message = "Invalid success message"

        # Act & Assert
        with self.assertRaises(ValueError):
            IResponse(error_code, message, data)

    def test_string_representation(self):
        """
        Test case for string representation of IResponse.
        """
        # Arrange
        error_code = EResponseErrorCode.ERROR_SUCCESS.value
        data = {"key": "value"}
        message = "success"
        response = IResponse(error_code, message, data)

        # Act
        result = str(response)

        # Assert
        self.assertEqual(result, "{'error': 0, 'message': 'success', 'data': {'key': 'value'}}")

    def test_attribute_access(self):
        """
        Test case for attribute access of IResponse.
        """
        # Arrange
        error_code = EResponseErrorCode.ERROR_SUCCESS.value
        data = {"key": "value"}
        message = "success"
        response = IResponse(error_code, message, data)

        # Act
        error = response.error
        message = response.message
        data = response.data

        # Assert
        self.assertEqual(error, 0)
        self.assertEqual(message, "success")
        self.assertEqual(data, {"key": "value"})


if __name__ == '__main__':
    unittest.main()
