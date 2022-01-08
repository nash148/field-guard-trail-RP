from dropbox import Dropbox
import dropbox.files as drpfiles

from src.logger.Logger import MyLogger


class DropboxHandler:
    def __init__(self):
        """Initial the attributes"""
        self.dbx = None
        self.logger = MyLogger()
        self.logger.info('Init Dropbox class')

    def auth(self, access_token: str):
        """
        Initial the Dropbox object with the given access token
        :param access_token:
        :return:
        """
        self.dbx = Dropbox(access_token)
        self.logger.info('Auth by access token')

    def create_folder(self, path):
        """
        Create a folder in Dropbox
        :param path: The path to create the folder
        :return: void
        """
        try:
            self.dbx.files_create_folder_v2(path)
            self.logger.info('Created new folder {}'.format(path))
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
