import datetime
import os

from src.logger.Logger import MyLogger
from src.cloud_handler.CloudHandlerProtocol import CloudHandlerProtocol
from src.RPi_handler.RPHandler import GPIOHandler
from src.config.settings import camera_conf, files_conf
from src.utils.files_utils import move_files_from_cam_ro_rpi, delete_pictures_from_rpi
from src.utils.rpi_utils import shutdown_rpi


class ControlManager:
    """
    The bug manager
    """
    def __init__(self, cloud_handler: CloudHandlerProtocol):
        """Initial the attributes"""
        self._cloud_handler = cloud_handler
        self._logger = MyLogger()
        self._rpi_handler = GPIOHandler()
        self._logger.info('Init ControlManager class')

    def run(self):
        """Run the whole program flow"""

        now = datetime.datetime.now()
        timestamp = now.strftime("%d-%m-%Y_%H-%M-%S")

        # Start supplying power to the RPi
        self._rpi_handler.start_power_supply()

        # Start shooting for time_to_shoot seconds
        self._rpi_handler.start_shooting(camera_conf['time_to_shoot'])

        # Open usb socket
        self._rpi_handler.open_usb_socket()

        # Move the pictures from camera to the RPi
        move_files_from_cam_ro_rpi()

        # Close usb socket
        self._rpi_handler.close_usb_socket()

        # Upload the pictures to the cloud
        self._upload_pics_to_cloud(timestamp)

        # Delete pictures from RPi storage
        delete_pictures_from_rpi()

        # Shutdown the RPi
        shutdown_rpi()

    def _upload_pics_to_cloud(self, start_timestamp: str):
        """Upload every picture in the pictures folder"""

        # Create new folder in the cloud
        self._cloud_handler.create_folder(files_conf['remote_pics_path'] + start_timestamp)

        rpi_pics_path = files_conf['RPi_pics_path']

        # Run over every file in the pictures folder
        for curr_file in os.listdir(files_conf['RPi_pics_path']):
            self._cloud_handler.upload_file(
                rpi_pics_path + '/' + curr_file,
                files_conf['remote_pics_path'] + start_timestamp + '/' + curr_file)
