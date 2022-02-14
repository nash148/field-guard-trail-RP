import urllib.request as url_request
import urllib.error as url_error

from src.logger.Logger import MyLogger

logger = MyLogger()


def wait_for_internet_connection(timeout: int):
    """Wait fot internet connection"""
    logger.info('Check internet connection')
    for i in range(timeout):
        try:
            url_request.urlopen('https://google.com', timeout=1)
            logger.info('Internet is available')
        except url_error.URLError:
            logger.info('There is no internet connection')


