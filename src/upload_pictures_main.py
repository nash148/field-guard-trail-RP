from src.control_manager.ControlManager import ControlManager
from src.cloud_handler.DropboxHandler import DropboxHandler
from src.logger.Logger import MyLogger

logger = MyLogger("upload")


def main():
    logger.info('#################################')
    logger.info('##  Starting pictures main...  ##')
    logger.info('#################################')

    cloud_handler = DropboxHandler()
    control_manager = ControlManager()
    control_manager.upload_camera_pictures(cloud_handler)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error(str(e))
