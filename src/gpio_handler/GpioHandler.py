from src.config.enums import GpioConf
from src.logger.Logger import MyLogger


class GpioHandler:
    """
    Handles the relevant GPIOs
    """
    def __init__(self):
        """Init the attributes"""
        self._logger = MyLogger()
        self._logger.info('Init GPOIHandler class')

    def toggle_gpio_pin(self, gpio: GpioConf, to_turn_on: bool):
        """Toggle gpio pin"""
        self._logger.info(f'Turn {"on" if to_turn_on else "off"} gpio pin - {gpio.name}')
        gpio.on() if to_turn_on else gpio.off()

