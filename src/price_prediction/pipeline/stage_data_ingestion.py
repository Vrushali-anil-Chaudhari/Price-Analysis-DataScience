from src.price_prediction import logger
from src.price_prediction.entity.config_entity import DataIngestionConfig
from src.price_prediction.components.data_ingestion import DataIngestion
from src.price_prediction.config.configuration import Configuration

STAGE_NAME = "Data Ingestion STAGE"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            logger.info(f"Starting {STAGE_NAME}...")
            config = Configuration()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            logger.info(f"{STAGE_NAME} completed.")
        except Exception as e:
            logger.exception(f"Failed to complete {STAGE_NAME} due to the following error: {e}")
            raise e