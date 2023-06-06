"""
Module: baseClassDevice

This module provides the BaseClassDevice API.

Classes:
    BaseClassDevice: Represents the BaseClassDevice API.

Usage:
    from .baseClassDevice import BaseClassDevice
"""

from typing import Dict, Any, Union

from ..ts.enum.EMethod import EMethod
from ..ts.enum.EPath import EPath
from ..ts.interface.IResponse import IResponse
from ..ts.interface.api.IDevicesDiscoveryRequest import IDevicesDiscoveryRequest
from ..utils.httpUtils import httpUtils


class BaseClassDevice(httpUtils):
    """
    Represents the BaseClassDevice API.

    Methods:
        discoverySubDevices(params: Dict[str, Any]) -> Dict[str, Any]:
            Searches for sub-devices.
        manualAddSubDevice(params: Dict[str, Any]) -> Dict[str, Any]:
            Manually adds a sub-device.
        getDeviceList() -> Dict[str, Any]:
            Gets the device list.
        updateDeviceState(serial_number: str, updateParams: Dict[str, Any]) -> Dict[str, Any]:
            Updates the status of a specified device.
        deleteDevice(serial_number: str) -> Dict[str, Any]:
            Deletes a device.
    """

    async def discoverySubDevices(self, params: Union[IDevicesDiscoveryRequest, Dict[str, Any]]) -> IResponse:
        """
        Searches for sub-devices.

        Args:
            params (Dict[str, Any]): Parameters for the request.

        Returns:
            IResponse: IResponse object containing the response data.
        """
        if isinstance(params, IDevicesDiscoveryRequest):
            params = {
                'enable': params.enable,
                'type': params.device_type
            }

        return await self.httpRequest(
            path=EPath.DEVICE_DISCOVERY.value,
            method=EMethod.PUT,
            params=params
        )

    async def manualAddSubDevice(self, params: Dict[str, Any]) -> IResponse:
        """
        Manually adds a sub-device (currently only supports adding RTSP cameras and ESP32 cameras).

        Args:
            params (Dict[str, Any]): Parameters for the request.

        Returns:
            IResponse: IResponse object containing the response data.
        """
        return await self.httpRequest(
            path=EPath.DEVICE.value,
            method=EMethod.POST,
            params=params
        )

    async def getDeviceList(self) -> IResponse:
        """
        Gets the device list.

        Returns:
            IResponse: IResponse object containing the response data.
        """
        return await self.httpRequest(
            path=EPath.DEVICE.value,
            method=EMethod.GET,
        )

    async def updateDeviceState(self, serial_number: str, updateParams: Dict[str, Any]) -> IResponse:
        """
        Updates the information or status of a specified device.

        Args:
            serial_number (str): Serial number of the device.
            updateParams (Dict[str, Any]): Parameters for updating the device.

        Returns:
            IResponse: IResponse object containing the response data.
        """
        return await self.httpRequest(
            path=f"{EPath.DEVICE.value}/{serial_number}",
            method=EMethod.PUT,
            params=updateParams
        )

    async def deleteDevice(self, serial_number: str) -> IResponse:
        """
        Deletes a device.

        Args:
            serial_number (str): Serial number of the device to be deleted.

        Returns:
            IResponse: IResponse object containing the response data.
        """
        return await self.httpRequest(
            path=f"{EPath.DEVICE.value}/{serial_number}",
            method=EMethod.DELETE
        )
