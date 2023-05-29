"""
Module: BaseClassSse

This module provides a base class for handling Server-Sent Events (SSE) connections.

Classes:
    BaseClassSse: Represents a base class for SSE connections.
"""
#pylint: disable-msg=broad-exception-caught

from typing import Dict, Any, Optional, Callable

import logging
import json
import asyncio
import aiohttp

from ..config import Store
from ..ts.enum.EPath import EPath
from ..ts.interface.ISseEvent import ISseEvent

_LOGGER = logging.getLogger(__name__)


class BaseClassSse(Store):
    """
    Represents a base class for SSE connections.
    """

    event_listeners = None
    session = None

    async def init_sse(self, session: aiohttp.ClientSession = None):
        """
        Initialize SSE connection.

        Returns:
            Optional dictionary containing the response data.
        """
        # Check for necessary parameters
        if not self.ip:
            error_msg = {"error": 1000, "msg": "ip is needed", "data": {}}
            _LOGGER.error(error_msg)
            return error_msg
        if not self.at:
            error_msg = {"error": 1000, "msg": "at is needed", "data": {}}
            _LOGGER.error(error_msg)
            return error_msg

        _LOGGER.debug('Initialize SSE session.')

        # Set session
        self.session = session if session is not None else aiohttp.ClientSession()

        # Set SSE event listeners
        self.event_listeners = {}

        # Create SSE connection URL
        url = f"http://{self.ip}{EPath.ROOT.value}{EPath.SSE.value}?access_token={self.at}"
        _LOGGER.debug(f'SSE Init: {url}')

        try:
            # Start SSE connection in a separate task
            asyncio.create_task(self.handle_sse(url))
            return True
        except Exception as error:
            # Handle exception in case of error
            _LOGGER.error(f'SSE Error: {url}')
            _LOGGER.error(f'SSE Error: {error}')

        return False

    async def handle_sse(self, url: str) -> None:
        """
        Handle SSE connection.

        Args:
            url (str): The SSE connection URL.
        """
        while True:
            try:
                if 'onopen' in self.event_listeners:
                    await self.event_listeners["onopen"]()
                else:
                    _LOGGER.debug('Connected to SSE server.')

                async with self.session.get(url) as response:
                    event_name = None
                    async for line in response.content:
                        event = line.decode().strip()
                        if event.startswith("event:"):
                            event_name = event[6:].strip()
                        elif event.startswith("data:") and event_name:
                            event_data = event[5:]
                            if event_data.strip() != "":
                                await self.handle_event(event_name, event_data)
                                event_name = None

            except asyncio.TimeoutError:
                if 'onerror' in self.event_listeners:
                    _LOGGER.debug('SSE time-out error, reconnecting.')
                    await self.event_listeners["onerror"](asyncio.TimeoutError)
                else:
                    _LOGGER.warning('SSE time-out error, reconnecting.')
                await self.close()
                await self.init_sse()

            except Exception as e:
                if 'onerror' in self.event_listeners:
                    await self.event_listeners["onerror"](e)
                else:
                    _LOGGER.error(f'SSE connection error: {e}')

    async def handle_event(self, event_name: str, event_data: any) -> None:
        """
        Handle SSE event.

        Args:
            event_name (str): The name of the SSE event.
            event_data (any): The data associated with the SSE event.
        """
        try:
            data = json.loads(event_data)
            _LOGGER.debug(f'Event detected: {event_name}, Data: {data}')
            if event_name and event_name in self.event_listeners:
                _LOGGER.debug(f'Event callback: {event_name}, Data: {data}')
                handler = self.event_listeners[event_name]
                await handler(data)

        except json.JSONDecodeError as error:
            _LOGGER.debug(f'Event error: {error}')
            if 'onerror' in self.event_listeners:
                await self.event_listeners["onerror"](error)

    def mount_sse_func(self, handler: ISseEvent) -> Optional[Dict[str, Any]]:
        """
        Mount SSE function.

        Args:
            handler: Handler for the SSE function.

        Returns:
            Optional dictionary containing the response data.
        """
        _LOGGER.debug('Mount SSE functions.')
        if self.event_listeners is None:
            return {'error': 1000, 'msg': 'must invoke initSSE first', 'data': {}}

        if hasattr(handler, 'onopen') and callable(handler.onopen):
            self.event_listeners.onOpen = handler.onopen

        if hasattr(handler, 'onerror') and callable(handler.onerror):
            self.event_listeners.onError = handler.onerror

        if hasattr(handler, 'onAddDevice') and callable(handler.onAddDevice):
            self.register_event_listener('device#v1#addDevice', handler.onAddDevice)

        if hasattr(handler, 'onUpdateDeviceState') and callable(handler.onUpdateDeviceState):
            self.register_event_listener('device#v1#updateDeviceState', handler.onUpdateDeviceState)

        if hasattr(handler, 'updateDeviceInfo') and callable(handler.updateDeviceInfo):
            self.register_event_listener('device#v1#updateDeviceInfo', handler.onUpdateDeviceInfo)

        if hasattr(handler, 'onUpdateDeviceOnline') and callable(handler.onUpdateDeviceOnline):
            self.register_event_listener('device#v1#updateDeviceOnline', handler.onUpdateDeviceOnline)

        if hasattr(handler, 'onDeleteDevice') and callable(handler.onDeleteDevice):
            self.register_event_listener('device#v1#deleteDevice', handler.onDeleteDevice)

        return None

    def unmount_sse_func(self) -> None:
        """
        Unmount SSE function.
        """
        if self.event_listeners:
            self.remove_event_listener('device#v1#addDevice')
            self.remove_event_listener('device#v1#updateDeviceState')
            self.remove_event_listener('device#v1#updateDeviceInfo')
            self.remove_event_listener('device#v1#updateDeviceOnline')
            self.remove_event_listener('device#v1#deleteDevice')
            self.close()

    def register_event_listener(self, event_type: str, handler: Callable) -> None:
        """
        Registers an event listener for the specified event type.

        Args:
            event_type (str): The type of the event.
            handler (Callable): The handler function to be called when the event occurs.
        """
        self.event_listeners[event_type] = handler

    def remove_event_listener(self, event_type: str) -> None:
        """
        Removes the event listener for the specified event type.

        Args:
            event_type (str): The type of the event.
        """
        if event_type in self.event_listeners:
            del self.event_listeners[event_type]

    async def close(self) -> None:
        """
        Closes the SSE session connection and releases any associated resources.
        """
        await self.session.close()
