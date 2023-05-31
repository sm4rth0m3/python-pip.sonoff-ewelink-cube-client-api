"""
Enumeration: ECapability

This enumeration defines different capabilities.

Enumerations:
    ECapability: Represents various capabilities.
"""

from . import BaseEnum


class ECapability(BaseEnum):
    """
    Represents various capabilities.

    Enumerations:
        POWER: Power capability.
        RSSI: RSSI (Received Signal Strength Indication) capability.
        OTA: OTA (Over-the-Air) capability.
        DETECT: Detection capability.
        BATTERY: Battery capability.
        TOGGLE: Toggle capability.
        PERCENTAGE: Percentage capability.
        MOTOR_CONTROL: Motor control capability.
        MOTOR_REVERSE: Motor reverse capability.
        MOTOR_CLB: Motor calibration capability.
        TEMPERATURE: Temperature capability.
        HUMIDITY: Humidity capability.
        PRESS: Pressure capability.
        COLOR_RGB: RGB color capability.
        COLOR_TEMPERATURE: Color temperature capability.
        BRIGHTNESS: Brightness capability.
        CAMERA_STREAM: Camera stream capability.
        STARTUP: Startup capability.
    """
    POWER = "power"
    RSSI = "rssi"
    OTA = "ota"
    DETECT = "detect"
    BATTERY = "battery"
    TOGGLE = "toggle"
    PERCENTAGE = "percentage"
    MOTOR_CONTROL = "motor-control"
    MOTOR_REVERSE = "motor-reverse"
    MOTOR_CLB = "motor-clb"
    TEMPERATURE = "temperature"
    HUMIDITY = "humidity"
    PRESS = "press"
    COLOR_RGB = "color-rgb"
    COLOR_TEMPERATURE = "color-temperature"
    BRIGHTNESS = "brightness"
    CAMERA_STREAM = "camera-stream"
    STARTUP = "startup"
