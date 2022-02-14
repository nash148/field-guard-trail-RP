import os
import re
import shutil

from src.config.settings import files_conf
from src.logger.Logger import MyLogger

logger = MyLogger()


def get_cam_drive_device_name() -> str:
    devices = os.listdir('/dev/')

    # Search for devices which start with sd and end with 1
    r = re.compile('sd[a-z]1')
    drive_devices = list(filter(r.match, devices))

    if len(drive_devices) > 1:
        raise Exception('More then one drive are connected')

    if len(drive_devices) < 1:
        raise Exception('Cannot find any drive device')

    logger.info(f'Found drive device named {drive_devices[0]}')
    return "/dev/" + drive_devices[0]


def move_files_from_dir_to_dir(src_path: str, dst_path: str):
    """Move files from dir to dir"""
    logger.info(f'Move files from \'{src_path}\' to \'{dst_path}\'')
    for curr_file in src_path:
        logger.info(f'Moving {curr_file}')
        shutil.move(src_path + curr_file, dst_path)


def delete_files_from_dir(dir_path):
    """Delete all files from a directory"""
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            raise Exception('Failed to delete %s. Reason: %s' % (file_path, e))
