"""
Example module for handling Open API from Sonoff eWeLink Cube API.
"""
# pylint: disable=duplicate-code

import os
import asyncio

from sonoff_ewelink_cube_client_api import EWelinkCube
from sonoff_ewelink_cube_client_api.ts.interface.IResponse import IResponse

from .example_helpers import load_access_token, save_access_token

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

    # Get public info of the Bridge device
    bridge_public_info: IResponse = await api_rest.getBridgeInfo()
    print(f'- Bridge public info: {bridge_public_info}')

    access_token: str = api_rest.getAt()
    print(f'- Access token initialized: {access_token}')

    # Get iHost access token method:
    # After calling the [Access Token] interface, the iHost Web console page global
    # pop-up box prompts the user to confirm the acquisition of the interface call credentials.
    #
    # Note:
    # If you open more than one iHost web console page, the confirmation pop-up box will
    # appear on multiple web console pages together, and the pop-up box of other web console
    # pages will be closed after clicking the confirmation on one of the web console pages.
    if not access_token:
        print('- Access token process: press link button on iHost device!')
        await api_rest.getBridgeAT()

        access_token = api_rest.getAt()
        print(f'- Access token received: {access_token}')

        file_path = save_access_token(IHOST_BRIDGE_HOST_ADDRESS, access_token)
        print(f'- Access token saved into {file_path}')


if __name__ == "__main__":
    # Run the main function
    asyncio.run(main())
