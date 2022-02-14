import datetime
import os
from time import sleep
from typing import Union

from src.logger.Logger import MyLogger
from src.cloud_handler.CloudHandlerProtocol import CloudHandlerProtocol
from src.gpio_handler.GpioHandler import GpioHandler
from src.files_handler.FilesHandler import FilesHandler
from src.utils.rpi_utils import shutdown_rpi


class ControlManager:
    """
    The bug manager
    """
    def __init__(self):
        """Initial the attributes"""
        self._logger = MyLogger()
        self._gpio_handler = GpioHandler()
        self._files_handler = FilesHandler()
        self._logger.info('Init ControlManager class')

    def upload_camera_pictures(self, cloud_handler: CloudHandlerProtocol, shutdown: bool = False):
        """Upload the pictures from the camera to the cloud"""

        # Move the images from the camera to the RPi
        self._files_handler.move_files_from_cam_to_rpi()

        # Reset camera
        self._gpio_handler.reset_camera()

        # Upload the pictures to the cloud
        self._files_handler.upload_images_to_cloud(cloud_handler)

        # Delete pictures from RPi storage
        self._files_handler.delete_images_from_rpi()

        if shutdown:
            # Shutdown the RPi
            shutdown_rpi()

    def start_power_supply(self, time_to_supply: int = None):
        """Start power supply"""
        self._gpio_handler.start_power_supply()
        
        if time_to_supply is not None:
            sleep(time_to_supply)
            self._gpio_handler.stop_power_supply()
        else:  # Run forever
            while True:
                sleep(1)
