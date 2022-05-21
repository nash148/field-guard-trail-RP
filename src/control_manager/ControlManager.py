from time import sleep
import logging
from src.logger.Logger import MyLogger
from src.cloud_handler.CloudHandlerProtocol import CloudHandlerProtocol
from src.gpio_handler.GpioHandler import GpioHandler
from src.files_handler.FilesHandler import FilesHandler


class ControlManager:
    """
    The bug manager
    """
    def __init__(self):
        """Initial the attributes"""
        self._logger = MyLogger()
        self._gpio_handler = GpioHandler()
        self._files_handler = FilesHandler(self._gpio_handler)
        self._logger.info('Init ControlManager class')

    def upload_camera_pictures(self, cloud_handler: CloudHandlerProtocol, shutdown: bool = False):
        """Upload the pictures from the camera to the cloud"""
        try:
            self._gpio_handler.open_startup_led()

            # Delete pictures from RPi storage
            self._files_handler.delete_images_from_rpi()

            # Move the images from the camera to the RPi
            self._gpio_handler.open_files_transfer_led()
            self._files_handler.move_files_from_cam_to_rpi()
            self._gpio_handler.close_files_transfer_led()

            # Upload the pictures to the cloud
            self._gpio_handler.open_cloud_upload_led()
            self._files_handler.upload_images_to_cloud(cloud_handler)
            self._gpio_handler.close_cloud_upload_led()

            self._gpio_handler.reset_camera()

            self._logger.info('Done!!')

            if shutdown:
                self._logger.info('Shutting down')
                logging.shutdown()
                self._gpio_handler.stop_power_supply()
        except Exception as e:
            self._logger.error(str(e))

    def start_power_supply(self, time_to_supply: int = None):
        """Start power supply"""
        self._gpio_handler.start_power_supply()
        
        if time_to_supply is not None:
            sleep(time_to_supply)
            self._gpio_handler.stop_power_supply()
        else:  # Run forever
            while True:
                sleep(1)
