from enum import Enum, auto

from gpiozero import LED

from src.config.settings import gpio_conf, debug_gpio_conf


class CloudsTypes(Enum):
    GOOGLE = auto()
    DROPBOX = auto()


class GpioConf(Enum):
    POWER_SUPPLY_PIN = LED(gpio_conf['power_supply_pin'], initial_value=None)
    CAMERA_PIN = LED(gpio_conf['camera_pin'])
    USB_SOCKET_PIN = LED(gpio_conf['usb_socket_pin'])
    RESET_CAMERA_PIN = LED(gpio_conf['reset_camera_pin'])
    STARTUP_PIN = LED(debug_gpio_conf['startup_pin'])
    FILE_TRANSFER_PIN = LED(debug_gpio_conf['file_transfer_pin'])
    CLOUD_TRANSFER_PIN = LED(debug_gpio_conf['cloud_upload_pin'])


