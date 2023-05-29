"""
Interface module: ISseEvent

This module defines the ISseEvent class.

Classes:
    ISseEvent: Represents an SSE event object with optional callbacks for various events.
"""
#pylint: disable-msg=too-few-public-methods

from typing import Optional


class ISseEvent:
    """
    Represents an SSE event object.

    Attributes:
        onopen (Optional[callable]): The callback function for the 'onopen' event.
        onerror (Optional[callable]): The callback function for the 'onerror' event.
        onAddDevice (Optional[callable]): The callback function for the 'onAddDevice' event.
        onUpdateDeviceState (Optional[callable]): The callback function for the 'onUpdateDeviceState' event.
        onUpdateDeviceInfo (Optional[callable]): The callback function for the 'onUpdateDeviceInfo' event.
        onUpdateDeviceOnline (Optional[callable]): The callback function for the 'onUpdateDeviceOnline' event.
        onDeleteDevice (Optional[callable]): The callback function for the 'onDeleteDevice' event.
    """

    def __init__(
        self,
        onopen: Optional[callable] = None,
        onerror: Optional[callable] = None,
        onAddDevice: Optional[callable] = None,
        onUpdateDeviceState: Optional[callable] = None,
        onUpdateDeviceInfo: Optional[callable] = None,
        onUpdateDeviceOnline: Optional[callable] = None,
        onDeleteDevice: Optional[callable] = None,
    ):
        self.onopen = onopen
        self.onerror = onerror
        self.onAddDevice = onAddDevice
        self.onUpdateDeviceState = onUpdateDeviceState
        self.onUpdateDeviceInfo = onUpdateDeviceInfo
        self.onUpdateDeviceOnline = onUpdateDeviceOnline
        self.onDeleteDevice = onDeleteDevice
