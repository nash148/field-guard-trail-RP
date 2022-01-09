from time import sleep
from gpiozero import LED

from src.logger.Logger import MyLogger
from src.config.settings import gpio_conf


class GPIOHandler:
    """
    Handles the relevant GPIOs
    """
    def __init__(self):
        """Init the attributes"""
        self._logger = MyLogger()
        self._power_supply_pin = LED(gpio_conf['power_supply_pin'])
        self._camera_pin = LED(gpio_conf['camera_pin'])
        self._usb_socket_pin = LED(gpio_conf['usb_socket_pin'])
        self._logger.info('Init GPOIHandler class')

    def start_power_supply(self):
        """Turn on the pin witch supplies the power to the RPi"""
        self._power_supply_pin.on()
        self._logger.info('Turned on the power supply pin')

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
