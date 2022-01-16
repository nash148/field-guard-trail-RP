from control_manager.ControlManager import ControlManager
from cloud_handler.DropboxHandler import DropboxHandler
from logger.Logger import MyLogger

logger = MyLogger()


def main():
    logger.info('################################')
    logger.info('##          Starting...       ##')
    logger.info('################################')

    cloud_handler = DropboxHandler()
    control_manager = ControlManager(cloud_handler)
    control_manager.run()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error(str(e))
