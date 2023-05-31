"""
Enumeration: EPath

This enumeration defines different API paths.

Enumerations:
    EPath: Represents various API paths.
"""

from . import BaseEnum


class EPath(BaseEnum):
    """
    Represents various API paths.

    Enumerations:
        ROOT: Root API path.
        V1: API v1 path.
        SSE: Server-Sent Events (SSE) API path for bridge.
        BRIDGE: Bridge API path.
        BRIDGE_TOKEN: Bridge access token API path.
        BRIDGE_RUNTIME: Bridge runtime API path.
        BRIDGE_CONFIG: Bridge configuration API path.
        HARDWARE_REBOOT: Hardware reboot API path.
        HARDWARE_SPEAKER: Hardware speaker API path.
        DEVICE_DISCOVERY: Device discovery API path.
        DEVICE: Device API path.
        THIRD_PARTY: Third-party event API path.
        DEBUG_LOG: Debug log API path.
    """
    ROOT = "/open-api"
    V1 = "/v1/rest"
    SSE = "/v1/sse/bridge"
    BRIDGE = "/bridge"
    BRIDGE_TOKEN = "/bridge/access_token"
    BRIDGE_RUNTIME = "/bridge/runtime"
    BRIDGE_CONFIG = "/bridge/config"
    HARDWARE_REBOOT = "/hardware/reboot"
    HARDWARE_SPEAKER = "/hardware/speaker"
    DEVICE_DISCOVERY = "/devices/discovery"
    DEVICE = "/devices"
    THIRD_PARTY = "/thirdparty/event"
    DEBUG_LOG = "/thirdparty/debug-log"
