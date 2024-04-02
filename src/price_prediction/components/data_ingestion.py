import os
import urllib.request as request
import zipfile
from src.price_prediction import logger
from src.price_prediction.utils.common import get_size
import gdown
import subprocess
from src.price_prediction.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            command = f"gdown {self.config.source_URL} -O {self.config.local_data_file}"
            subprocess.run(command, shell=True)
            logger.info(f" download! ")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")



    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(r"artificats\data_ingestion\data.zip", 'r') as zip_ref:
            zip_ref.extractall(unzip_path)