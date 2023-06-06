"""
Example module for handling Open API from Sonoff eWeLink Cube API.

UNTESTTED!
"""
# pylint: disable=duplicate-code

import os
import asyncio

from sonoff_ewelink_cube_client_api import EWelinkCube

#pylint: disable-msg=unused-import
from sonoff_ewelink_cube_client_api.ts.interface.IResponse import IResponse
from sonoff_ewelink_cube_client_api.ts.interface.IDebugLog import IDebugLog

from .example_helpers import load_access_token

# iHost example settings
IHOST_BRIDGE_HOST_ADDRESS = os.getenv("IHOST_BRIDGE_HOST_ADDRESS", "ihost.local")
IHOST_BRIDGE_ACCESS_TOKEN = os.getenv("IHOST_BRIDGE_ACCESS_TOKEN", load_access_token(IHOST_BRIDGE_HOST_ADDRESS))


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

    # I don't use actually third-party devices
    # Untested, I got empty [] response for local device
    device_debug_log = await api_rest.getDebugLog("84ba20ffxxxxxxx", {
        "type": "directive_log", # or event_log
        "limit": 10,
        "from_index": 0,
        "start_time": 1685570400000,
        "end_time": 1686088799999,
    })
    print(device_debug_log)


if __name__ == "__main__":
    # Run the main function
    asyncio.run(main())
