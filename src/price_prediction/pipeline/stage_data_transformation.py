from src.price_prediction import logger
from src.price_prediction.entity.config_entity import DataTransformationConfig
from src.price_prediction.components.data_transformation import DataTransformation
from src.price_prediction.config.configuration import Configuration

STAGE_NAME = "Data Transformation STAGE"

class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = Configuration()
            logger.info(f"Starting {STAGE_NAME}...")
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config)
            df = data_transformation.handling_missing_values()
            d= data_transformation.date_time_conversion(df)
            data_transformation.train_test_split(d)
            logger.info(f"{STAGE_NAME} completed.")
        except Exception as e:
            raise e