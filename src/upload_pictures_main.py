import sys
import os

# Set the working directory as PYTHONPATH
sys.path.append(os.getcwd())

from src.control_manager.ControlManager import ControlManager
from src.cloud_handler.DropboxHandler import DropboxHandler
from src.utils.rpi_utils import shutdown_rpi
from src.logger.Logger import MyLogger

logger = MyLogger("upload")


def main():
    logger.info('#################################')
    logger.info('##  Starting pictures main...  ##')
    logger.info('#################################')

    cloud_handler = DropboxHandler()
    control_manager = ControlManager()
    control_manager.upload_camera_pictures(cloud_handler, True)


if __name__ == '__main__':
    main()
