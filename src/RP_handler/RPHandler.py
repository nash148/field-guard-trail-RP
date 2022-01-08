
from src.logger.Logger import MyLogger


class GPIOHandler:
    """
    Handles the relevant GPIOs
    """
    def __init__(self):
        """Init the attributes"""
        self.logger = MyLogger()
        self.logger.info('Init GPOIHandler class')

    def start_shoot(self, time_to_shoot: int):
        """"""
        pass
