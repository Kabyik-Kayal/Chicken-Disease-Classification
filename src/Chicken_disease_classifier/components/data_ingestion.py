import os
import urllib.request as request
import zipfile
from Chicken_disease_classifier import logger
from Chicken_disease_classifier.utils.common import get_size
from Chicken_disease_classifier.config.configuration import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"Downloaded file: {filename} with following info: {headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        This function Extracts the zip file into the data directory
        Args:
            zip_file_path: str
        Returns: None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)