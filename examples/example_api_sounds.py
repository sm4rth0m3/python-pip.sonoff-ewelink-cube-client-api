"""
Example module for handling Open API from Sonoff eWeLink Cube API.
"""
# pylint: disable=duplicate-code

import os
import asyncio

from sonoff_ewelink_cube_client_api import EWelinkCube
from sonoff_ewelink_cube_client_api.ts.enum.EHardware import ESpeakerTypes
from sonoff_ewelink_cube_client_api.ts.interface.IResponse import IResponse
from sonoff_ewelink_cube_client_api.ts.interface.api.IHardware import IBeepObject, ISoundObject

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

    # Set system volume (0 - 100)
    set_volume = 0
    api_volume: IResponse = await api_rest.updateBridgeConfig(volume=set_volume)

    if api_volume and not api_volume["error"]:
        print(f'- System volume set: {set_volume}%')
    else:
        print(f'- System volume set error: [{api_volume["error"]}] {api_volume["message"]}')
    await asyncio.sleep(2)


    ### SOUND
    print(f'Supported SOUNDS: {ISoundObject.SUPPORTED_SOUNDS}')

    # Use enums and interfaces for secure and validated params.
    play_type: ESpeakerTypes = ESpeakerTypes.PLAY_SOUND
    play_object: ISoundObject = ISoundObject(name="alert1", volume=set_volume, countdown=2)
    print("- PLAY_SOUND", await api_rest.controlSpeaker(play_type=play_type, sound=play_object))
    await asyncio.sleep(2)

    # Or use simple payload object, but it's unsecured and unvalidated (raw).
    play_type = "play_sound"
    play_object = {"name": "doorbell1", "volume": set_volume}
    print("- PLAY_BEEP", await api_rest.controlSpeaker(play_type=play_type, beep=play_object))
    await asyncio.sleep(2)


    ### BEEP
    print(f'Supported BEEPS: {IBeepObject.SUPPORTED_BEEPS}')

    # Good bye! :-)
    play_type: ESpeakerTypes = ESpeakerTypes.PLAY_BEEP
    play_object: IBeepObject = IBeepObject(name="systemShutdown", volume=set_volume)
    print("- PLAY_BEEP", await api_rest.controlSpeaker(play_type=play_type, beep=play_object))
    await asyncio.sleep(2)


if __name__ == "__main__":
    # Run the main function
    asyncio.run(main())
