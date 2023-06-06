"""
Module: EDiscoveryDevice

This enumeration defines different devices discovery error codes.

Enumerations:
    EDiscoveryDevice: Enumeration of error codes.
"""
from ..enum import BaseEnum

class EDiscoveryDeviceError(BaseEnum):
    """
    Enum class representing sub-devices errors.
    """
    SUBDEVICE_NOT_EXIST = 110000
    GATEWAY_DISCOVERING_ZIGBEE_DEVICES = 110001
    GROUP_DEVICES_NO_COMMON_CAPABILITY = 110002
    INCORRECT_NUMBER_OF_DEVICES = 110003
    INCORRECT_NUMBER_OF_GROUPS = 110004
    DEVICE_OFFLINE = 110005
    FAILED_UPDATE_DEVICE_STATUS = 110006
    FAILED_UPDATE_GROUP_STATUS = 110007
    MAXIMUM_GROUPS_REACHED = 110008
    CAMERA_DEVICE_INCORRECT_IP_ADDRESS = 110009
    CAMERA_DEVICE_AUTHORIZATION_ERROR = 110010
    CAMERA_DEVICE_STREAM_ADDRESS_ERROR = 110011
    CAMERA_DEVICE_UNSUPPORTED_VIDEO_ENCODING = 110012
    DEVICE_ALREADY_EXISTS = 110013
    CAMERA_UNSUPPORTED_OFFLINE_OPERATION = 110014
    RTSP_ADDRESS_PASSWORD_INCONSISTENCY = 110015
    GATEWAY_DISCOVERING_ONVIF_CAMERAS = 110016
    MAXIMUM_CAMERAS_ADDED_EXCEEDED = 110017
    ESP_CAMERA_PATH_ERROR = 110018

    @staticmethod
    def get_error_message(error_code: int) -> str:
        """
        Get the error message for the given error code.

        Args:
            error_code (int): The error code.

        Returns:
            str: The corresponding error message.

        Raises:
            KeyError: If the error code is not found in the error messages.
        """

        __error_messages = {
            110000: "The sub-device/group corresponding to the id does not exist",
            110001: "The gateway is in the state of discovering zigbee devices",
            110002: "Devices in a group do not have a common capability",
            110003: "Incorrect number of devices",
            110004: "Incorrect number of groups",
            110005: "Device Offline",
            110006: "Failed to update device status",
            110007: "Failed to update group status",
            110008: "The maximum number of groups has been reached. Create up to 50 groups",
            110009: "The IP address of the camera device is incorrect",
            110010: "Camera Device Access Authorization Error",
            110011: "Camera device stream address error",
            110012: "Camera device video encoding is not supported",
            110013: "Device already exists",
            110014: "Camera does not support offline operation",
            110015: "The account password is inconsistent with the account password in the RTSP stream address",
            110016: "The gateway is in the state of discovering onvif cameras",
            110017: "Exceeded the maximum number of cameras added",
            110018: "The path of the ESP camera is wrong"
        }

        return __error_messages[error_code]
