"""
Enumeration: ECategory

This enumeration defines different device categories.

Enumerations:
    ECategory: Represents various device categories.
"""

from . import BaseEnum


class ECategory(BaseEnum):
    """
    Represents various device categories.

    Enumerations:
        PLUG: Plug category.
        SWITCH: Switch category.
        LIGHT: Light category.
        CURTAIN: Curtain category.
        CONTACT_SENSOR: Contact sensor category.
        MOTION_SENSOR: Motion sensor category.
        TEMPERATURE_SENSOR: Temperature sensor category.
        HUMIDITY_SENSOR: Humidity sensor category.
        TEMPERATURE_HUMIDITY_SENSOR: Temperature and humidity sensor category.
        WATER_LEAK_DETECTOR: Water leak detector category.
        SMOKE_DETECTOR: Smoke detector category.
        BUTTON: Button category.
    """
    PLUG = "plug"
    SWITCH = "switch"
    LIGHT = "light"
    CURTAIN = "curtain"
    CONTACT_SENSOR = "contactSensor"
    MOTION_SENSOR = "motionSensor"
    TEMPERATURE_SENSOR = "temperatureSensor"
    HUMIDITY_SENSOR = "humiditySensor"
    TEMPERATURE_HUMIDITY_SENSOR = "temperatureAndHumiditySensor"
    WATER_LEAK_DETECTOR = "waterLeakDetector"
    SMOKE_DETECTOR = "smokeDetector"
    BUTTON = "button"
