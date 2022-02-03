import shutil, os

from src.config.settings import files_conf
from src.logger.Logger import MyLogger

logger = MyLogger()


def move_files_from_cam_ro_rpi():
    """Move pictures from camera to the RPi"""
    logger.info('Moving pictures from camera to RPi storage')
    files = os.listdir(files_conf['camera_pics_path'])
    for curr_file in files:
        logger.info('Moving {} from camera to RPi'.format(curr_file))
        shutil.move(files_conf['camera_pics_path'] + curr_file, files_conf['RPi_pics_path'])


def delete_pictures_from_rpi():
    """Delete the pictures from RPi storage"""
    folder = files_conf['RPi_pics_path']

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            logger.error('Failed to delete %s. Reason: %s' % (file_path, e))
    logger.info('Deleted all pictures from RPi storage')
