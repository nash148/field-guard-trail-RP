from src.control_manager.ControlManager import ControlManager
from src.cloud_handler.DropboxHandler import DropboxHandler
from src.logger.Logger import MyLogger

logger = MyLogger("power")


def main():
    logger.info('#################################')
    logger.info('##   Starting power main...    ##')
    logger.info('#################################')

    control_manager = ControlManager()
    control_manager.start_power_supply()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error(str(e))
