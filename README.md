# python-pip.sonoff-ewelink-cube-client-api

SONOFF eWelink CUBE API communication library (unofficial)


⚠️ The project is still under active development.


Supported devices:
- SONOFF iHost
- SONOFF NSPanel Pro (untested)

Features:
- Request objects for validated params usage.
- Response objects for parsing response as object, json or text.


### What is eWeLink CUBE?

eWeLink CUBE is a Smart Home Platform for local small-scale computing platforms, tailored and optimized from the eWeLink Smart Home Cloud Platform and hardware-adapted.
More information: https://ewelink.cc/ewelink-cube/


---
## Usage

Install pip package:
```sh
pip3 install sonoff-ewelink-cube-client-api
```

Example:
```sh
"""
Simple bootstrap example, see more in examples directory.
"""

import asyncio
import json

from sonoff_ewelink_cube_client_api import EWelinkCube

# Set None for disable formatting JSON output
PRINT_JSON_INDENT = 4


async def main():
    # Create an instance of the API
    ewelink_cube = EWelinkCube()
    api_rest = ewelink_cube.create_api('iHost', ip='ihost.local')

    # Get iHost access token method:
    # After calling the [Access Token] interface, the iHost Web console page global
    # pop-up box prompts the user to confirm the acquisition of the interface call credentials.
    print(f'- Access token process: press link button on iHost device!')
    access_token = await api_rest.getBridgeAT()
    print(f'- Access token request: {access_token}')

    # iHost info
    api_bridge_info = await api_rest.getBridgeInfo()
    if api_bridge_info and not api_bridge_info["error"]:
        print(f'- Bridge info: {json.dumps(api_bridge_info, indent=PRINT_JSON_INDENT)}')

    # Devices list with some info
    api_devices_list = await api_rest.getDeviceList()
    if api_devices_list and not api_devices_list["error"]:
        print(f'- Devices list: {json.dumps(api_devices_list, indent=PRINT_JSON_INDENT)}')


# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
```

See more in the [examples](https://github.com/sm4rth0m3/python-pip.sonoff-ewelink-cube-client-api/tree/main/examples) directory.


---
## Development and testing

```sh
# Start docker container (or use virtualenv)
docker run -rm -it -v "$(pwd)":/app -w /app python:3.11-slim /bin/bash

# Install packages and repository
pip3 install -r requirements-dev.txt
pip3 install .

# Pylint checks
pylint --recursive=y ./setup.py ./src ./examples

# Try examples
export LOG_LEVEL=DEBUG
export IHOST_BRIDGE_HOST_ADDRESS="192.168.1.110"     # Use IP instead of ihost.local
export IHOST_BRIDGE_ACCES_TOKEN="uuid4-access-token" # Optional, see example codes

python3 examples/example_api.py
python3 examples/example_events.py
```

Tested devices:
- iHost - Firmware 1.6.1


---
## Roadmap

✓ Ready:
- Integrated an API source from [npm](https://www.npmjs.com/package/node-red-contrib-ewelink-cube) into Python
- Git pre-hooks, code quality tools


🔧 In-progress:
- Create objects interfaces / enums by API documentation (payload, beep, etc...)


🚀 Fantastic features in the future: ;-)
- Create additional API methods (non Open API, ex.: docker)
- Create test suites (unit / mock)
- CI/CD (ex.: Github or Travis)
- Errors handling

---
## More informations

- https://ewelink.cc/ewelink-cube/
- https://ewelink.cc/ewelink-cube/open-api/
- https://sonoff.tech/ihost-user-guides/api/
- https://www.npmjs.com/package/node-red-contrib-ewelink-cube
- https://appcms.coolkit.cn/feed
- https://appcms.coolkit.cn/ai-bridge/changelog-aibridge/feed
- https://github.com/CoolKit-Technologies/cc.ewelink.smart.home.addon/tree/main/web/src/api
