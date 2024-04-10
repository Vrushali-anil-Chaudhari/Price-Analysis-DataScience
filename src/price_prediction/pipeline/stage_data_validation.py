from src.price_prediction.config.configuration import Configuration
from src.price_prediction import logger
from src.price_prediction.components.data_validation import DataValiadtion

STAGE_NAME = "Data Validation STAGE"
class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            logger.info(f"Starting {STAGE_NAME}....")
            config = Configuration()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValiadtion(config=data_validation_config)
            data_validation.validate_all_columns()
            logger.info(f"{STAGE_NAME} completed.")
        except Exception as e:
            raise e