from time import sleep
from gpiozero import LED

from src.logger.Logger import MyLogger
from src.config.settings import gpio_conf, debug_gpio_conf


RESET_CAMERA_SLEEP_SEC = 1


class GpioHandler:
    """
    Handles the relevant GPIOs
    """
    def __init__(self):
        """Init the attributes"""
        self._logger = MyLogger()
        self._power_supply_pin = None
        self._camera_pin = LED(gpio_conf['camera_pin'])
        self._usb_socket_pin = LED(gpio_conf['usb_socket_pin'])
        self._reset_camera_pin = LED(gpio_conf['reset_camera_pin'])

        # Debug pins
        self._startup_pin = LED(debug_gpio_conf['startup_pin'])
        self._files_transfer_pin = LED(debug_gpio_conf['file_transfer_pin'])
        self.cloud_upload_pin = LED(debug_gpio_conf['cloud_upload_pin'])
        self._logger.info('Init GPOIHandler class')

    def start_power_supply(self):
        """Turn on the pin witch supplies the power to the RPi"""
        self._power_supply_pin = LED(gpio_conf['power_supply_pin'])
        self._power_supply_pin.on()
        self._logger.info('Turned on the power supply pin')

    def stop_power_supply(self):
        """Turn off the pin witch supplies the power to the RPi"""
        self._power_supply_pin = LED(gpio_conf['power_supply_pin'])
        self._power_supply_pin.off()
        self._logger.info('Turned off the power supply pin')

    def start_shooting(self, time_to_shoot_sec: int):
        """
        Turns on the camera pin for the given time
        :param time_to_shoot_sec: Time to pules
        :return: void
        """
        self._camera_pin.on()
        self._logger.info('Turned on the camera pin')
        sleep(time_to_shoot_sec)
        self._camera_pin.off()
        self._logger.info('Turned off the camera pin')

    def open_usb_socket(self):
        """Turns on the usb socket pin"""
        self._usb_socket_pin.on()
        self._logger.info('Turned on the usb socket pin')

    def close_usb_socket(self):
        """Tuns off the usb socket pin"""
        self._usb_socket_pin.off()
        self._logger.info('Turned off the usb socket pin')

    def reset_camera(self):
        """Reset the camera"""
        self._reset_camera_pin.on()
        self._logger.info('Turn on reset camera pin')
        sleep(RESET_CAMERA_SLEEP_SEC)
        self._reset_camera_pin.off()
        self._logger.info('Turn off reset camera pin')

    def open_startup_led(self):
        """Open startup led"""
        self._logger.info('Turn on startup led')
        self._startup_pin.on()

    def close_startup_led(self):
        """Turn off startup led"""
        self._logger.info('Turn off startup led')
        self._startup_pin.off()

    def open_files_transfer_led(self):
        """Open files transfer led"""
        self._logger.info('Turn on files transfer led')
        self._files_transfer_pin.on()

    def close_files_transfer_led(self):
        """Turn off files transfer led"""
        self._logger.info('Turn off files transfer led')
        self._files_transfer_pin.off()

    def open_cloud_upload_led(self):
        """Open cloud upload led"""
        self._logger.info('Turn on cloud upload led')
        self.cloud_upload_pin.on()

    def close_cloud_upload_led(self):
        """Turn off cloud upload led"""
        self._logger.info('Turn off cloud upload led')
        self.cloud_upload_pin.off()
