from dropbox import Dropbox
import dropbox.files as drpfiles

from src.logger.Logger import MyLogger
from src.config.settings import cloud_conf


class DropboxHandler:
    def __init__(self):
        """Initial the attributes"""
        self.dbx = Dropbox(cloud_conf['access_token'])
        self.logger = MyLogger()
        self.logger.info('Init Dropbox class')

    def create_folder(self, path):
        """
        Create a folder in Dropbox
        :param path: The path to create the folder
        :return: void
        """
        try:
            self.dbx.files_create_folder_v2(path)
            self.logger.info('Created new folder in Dropbox - {}'.format(path))
        except Exception as e:
            self.logger.error(str(e))

    def upload_file(self, path: str, dst_path: str):
        """
        Upload the given path file to Dropbox, only file not a folder
        :param path: The path to the file
        :param dst_path: The path to save in Dropbox
        :return: bool
        """
        try:
            with open(path, 'rb') as f:
                self.dbx.files_upload(f.read(), dst_path, drpfiles.WriteMode.overwrite)
                self.logger.info('Uploaded file {} to {}'.format(path, dst_path))
        except Exception as e:
            self.logger.error(str(e))
