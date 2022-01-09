from subprocess import call

from src.logger.Logger import MyLogger

logger = MyLogger()


def shutdown_rpi():
    """Shut down the RPi"""
    logger.info('Shutting down the RPi')
    try:
        call("sudo shutdown -h now", shell=True)
    except Exception as e:
        logger.error(str(e))
