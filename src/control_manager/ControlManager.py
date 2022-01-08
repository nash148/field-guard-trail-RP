
from src.logger.Logger import MyLogger
from src.cloud_handler.CloudHandlerProtocol import CloudHandlerProtocol


class ControlManager:
    """
    The bug manager
    """
    def __init__(self, cloud_handler: CloudHandlerProtocol):
        """Initial the attributes"""
        self.cloud_handler = cloud_handler
        self.logger = MyLogger()
        self.RP_handler = None

    def run(self):
        pass
