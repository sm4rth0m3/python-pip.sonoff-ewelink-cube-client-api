"""
Example module for handling Open API from Sonoff eWeLink Cube API.
"""
# pylint: disable=duplicate-code

import os
import asyncio

from sonoff_ewelink_cube_client_api import EWelinkCube
from sonoff_ewelink_cube_client_api.ts.interface.IResponse import IResponse
from sonoff_ewelink_cube_client_api.ts.interface.IDevice import IDevicesDiscoveryRequest, EDiscoveryDevicesType

from .example_helpers import load_access_token

# iHost example settings
IHOST_BRIDGE_HOST_ADDRESS = os.getenv("IHOST_BRIDGE_HOST_ADDRESS", "ihost.local")
IHOST_BRIDGE_ACCESS_TOKEN = os.getenv("IHOST_BRIDGE_ACCESS_TOKEN", load_access_token(IHOST_BRIDGE_HOST_ADDRESS))

# Set None for disabling JSON output formatting
PRINT_JSON_INDENT = 4


async def main():
    """
    The main function of the example.
    """
    # Create an instance of the API
    ewelink_cube = EWelinkCube()
    api_rest = ewelink_cube.create_api(
        api_name='iHost',
        ip=IHOST_BRIDGE_HOST_ADDRESS,
        at=IHOST_BRIDGE_ACCESS_TOKEN,
    )

    # Enable Zigbee devices searching
    params = IDevicesDiscoveryRequest(
        enable=True,
        device_type=EDiscoveryDevicesType.TYPE_ZIGBEE
    )
    discovery_response: IResponse = await api_rest.discoverySubDevices(params=params)
    print("- Ziggbee devices discovery", discovery_response)


if __name__ == "__main__":
    # Run the main function
    asyncio.run(main())
