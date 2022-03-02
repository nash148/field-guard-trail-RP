from time import sleep
from src.logger.Logger import MyLogger
from src.cloud_handler.CloudHandlerProtocol import CloudHandlerProtocol
from src.gpio_handler.GpioHandler import GpioHandler
from src.files_handler.FilesHandler import FilesHandler
from src.config.enums import GpioConf

RESET_CAMERA_SLEEP_SEC = 1


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
            self._gpio_handler.toggle_gpio_pin(GpioConf.STARTUP_PIN, to_turn_on=True)

            # Delete pictures from RPi storage
            self._files_handler.delete_images_from_rpi()

            # Move the images from the camera to the RPi
            self._move_images_from_camera()

            # Upload the pictures to the cloud
            self._upload_images(cloud_handler)

            # Reset the camera
            self._reset_camera()

            self._logger.info('Done!!')

            if shutdown:
                self._logger.info('Shutting down')
                self._gpio_handler.toggle_gpio_pin(GpioConf.POWER_SUPPLY_PIN, to_turn_on=False)
        except Exception as e:
            self._logger.error(str(e))

    def start_power_supply(self, time_to_supply: int = None):
        """Start power supply"""
        self._gpio_handler.toggle_gpio_pin(GpioConf.POWER_SUPPLY_PIN, to_turn_on=True)

        if time_to_supply is not None:
            sleep(time_to_supply)
            self._gpio_handler.toggle_gpio_pin(GpioConf.POWER_SUPPLY_PIN, to_turn_on=False)
        else:  # Run forever
            while True:
                sleep(1)

    def _move_images_from_camera(self):
        self._gpio_handler.toggle_gpio_pin(GpioConf.FILE_TRANSFER_PIN, to_turn_on=True)
        self._files_handler.move_files_from_cam_to_rpi()
        self._gpio_handler.toggle_gpio_pin(GpioConf.FILE_TRANSFER_PIN, to_turn_on=False)

    def _upload_images(self, cloud_handler: CloudHandlerProtocol):
        self._gpio_handler.toggle_gpio_pin(GpioConf.CLOUD_TRANSFER_PIN, to_turn_on=True)
        self._files_handler.upload_images_to_cloud(cloud_handler)
        self._gpio_handler.toggle_gpio_pin(GpioConf.CLOUD_TRANSFER_PIN, to_turn_on=False)

    def _reset_camera(self):
        """Reset the camera"""
        self._logger.info('Reset camera')
        self._gpio_handler.toggle_gpio_pin(GpioConf.RESET_CAMERA_PIN, to_turn_on=True)
        sleep(RESET_CAMERA_SLEEP_SEC)
        self._gpio_handler.toggle_gpio_pin(GpioConf.RESET_CAMERA_PIN, to_turn_on=False)

