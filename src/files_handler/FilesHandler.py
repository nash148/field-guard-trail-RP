import os
import datetime
from time import sleep

from src.config.settings import files_conf
from src.cloud_handler.CloudHandlerProtocol import CloudHandlerProtocol
from src.gpio_handler.GpioHandler import GpioHandler
from src.logger.Logger import MyLogger
from src.utils.files_utils import get_cam_drive_device_name, move_files_from_dir_to_dir, delete_files_from_dir
from src.utils.connection import wait_for_internet_connection


TIME_TO_WAIT_BEFORE_MOUNT = 7
TIME_TO_WAIT_AFTER_MOUNT = 2
INTERNET_CONNECTION_TIMEOUT = 90


class FilesHandler:
    """Handles everything related to files"""
    def __init__(self, gpio_handler: GpioHandler):
        self._gpio_handler = gpio_handler
        self._logger = MyLogger()
        self._camera_device_name = None

        # Init config attributes
        self._camera_images_path = files_conf['camera_pics_path']
        self._rpi_tmp_path = files_conf['RPi_pics_path']
        self._cloud_images_path = files_conf['remote_pics_path']
        self._mount_point_path = files_conf['mount_point_path']

    def move_files_from_cam_to_rpi(self):
        """Moves the images from the camera to the rpi temp dir"""

        self._logger.info("Move files from camera to RPi")

        # Open the usb socket
        self._gpio_handler.open_usb_socket()

        sleep(TIME_TO_WAIT_BEFORE_MOUNT)
        self._mount_camera_drive()
        sleep(TIME_TO_WAIT_AFTER_MOUNT)

        # Move the pictures from camera to the RPi
        move_files_from_dir_to_dir(self._camera_images_path, self._rpi_tmp_path)

        self._umount_camera_drive()

        # Close usb socket
        self._gpio_handler.close_usb_socket()

    def upload_images_to_cloud(self, cloud_handler: CloudHandlerProtocol):
        """Upload the images to the cloud"""
        self._logger.info('Upload images to the cloud')

        wait_for_internet_connection(INTERNET_CONNECTION_TIMEOUT)

        cloud_dir_path = self._get_cloud_dir_path()

        cloud_handler.create_folder(cloud_dir_path)

        for curr_file in os.listdir(self._rpi_tmp_path):
            cloud_handler.upload_file(
                self._rpi_tmp_path + '/' + curr_file,
                cloud_dir_path + '/' + curr_file)

    def delete_images_from_rpi(self):
        """Delete the images from the temp dir"""
        self._logger.info('Delete all images from RPi temp directory')
        delete_files_from_dir(self._rpi_tmp_path)

    def _get_cloud_dir_path(self):
        """Returns the cloud dir name"""
        now = datetime.datetime.now()
        timestamp = now.strftime("%d-%m-%Y_%H-%M-%S")
        return self._cloud_images_path + timestamp

    def _mount_camera_drive(self):
        """Mount the camera drive into mount point path"""
        self._camera_device_name = get_cam_drive_device_name()

        self._logger.info(f'Try to mount {self._camera_device_name}')

        cmd = f'mount -t vfat -o umask=0022,gid=1000,uid=1000 {self._camera_device_name} {self._mount_point_path}'
        res = os.system(cmd)

        if res != 0:
            raise Exception('Cannot mount camera drive')

        self._logger.info('Camera drive has mounted successfully')

    def _umount_camera_drive(self):
        """Umount the camera drive"""

        self._logger.info('Umount camera device')
        if self._camera_device_name is None:
            raise Exception('Try umount None device name')

        cmd = f'sudo umount {self._camera_device_name}'
        res = os.system(cmd)

        if res != 0:
            raise Exception('Error while umount camera device')
