"""
Example module for handling SSE events from Sonoff eWeLink Cube API.
"""
# pylint: disable=duplicate-code

import os
import asyncio

from sonoff_ewelink_cube_client_api import EWelinkCube

from .example_helpers import load_access_token

# iHost example settings
IHOST_BRIDGE_HOST_ADDRESS = os.getenv("IHOST_BRIDGE_HOST_ADDRESS", "ihost.local")
IHOST_BRIDGE_ACCESS_TOKEN = os.getenv("IHOST_BRIDGE_ACCESS_TOKEN", load_access_token(IHOST_BRIDGE_HOST_ADDRESS))


class MySseEventHandler:
    """Event handler for SSE events.

    This class provides methods to handle various SSE events.

    Args:
        event_data (dict): Event data received from the SSE stream.
    """

    async def onAddDevice(self, event_data):
        """
        Handle the 'addDevice' event.

        Args:
            event_data (dict): Event data received from the SSE stream.
        """
        print("Received 'addDevice' event:", event_data)

    async def onUpdateDeviceState(self, event_data):
        """
        Handle the 'updateDeviceState' event.

        Args:
            event_data (dict): Event data received from the SSE stream.
        """
        print("Received 'updateDeviceState' event:", event_data)

    async def onUpdateDeviceInfo(self, event_data):
        """
        Handle the 'updateDeviceInfo' event.

        Args:
            event_data (dict): Event data received from the SSE stream.
        """
        print("Received 'updateDeviceInfo' event:", event_data)

    async def onUpdateDeviceOnline(self, event_data):
        """
        Handle the 'updateDeviceOnline' event.

        Args:
            event_data (dict): Event data received from the SSE stream.
        """
        print("Received 'updateDeviceOnline' event:", event_data)

    async def onDeleteDevice(self, event_data):
        """
        Handle the 'deleteDevice' event.

        Args:
            event_data (dict): Event data received from the SSE stream.
        """
        print("Received 'deleteDevice' event:", event_data)


async def main():
    """
    The main function for handling SSE events.
    """
    print(f"Host address: {IHOST_BRIDGE_HOST_ADDRESS}")
    print(f"Access token: {IHOST_BRIDGE_ACCESS_TOKEN}")
    print("---")

    # Create an instance of the BaseSseClass
    ewelink_cube = EWelinkCube()
    sse = ewelink_cube.create_api(
        api_name='iHost',
        ip=IHOST_BRIDGE_HOST_ADDRESS,
        at=IHOST_BRIDGE_ACCESS_TOKEN
    )

    # Initialize the SSE connection
    sse_connect = await sse.init_sse()
    if not sse_connect:
        raise ValueError(f'SSE connection error: {sse_connect}')

    # Create an instance of the event handler
    event_handler = MySseEventHandler()

    # Mount the SSE function and register event listeners
    sse.mount_sse_func(event_handler)

    # Start SSE
    try:
        while True:
            # Add your own logic here or use asyncio.sleep() to pause execution
            await asyncio.sleep(1)

    except KeyboardInterrupt:
        # Program interrupted, clean up and exit
        print("Program interrupted. Exiting...")

    finally:
        # Cancel all tasks and gather them
        sse.unmount_sse_func()


if __name__ == "__main__":
    # Run the main function
    asyncio.run(main())
