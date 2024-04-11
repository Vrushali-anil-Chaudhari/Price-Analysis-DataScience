from src.price_prediction.config.configuration import Configuration
from src.price_prediction.components.model_training import ModelTraining
from src.price_prediction import logger

STAGE_NAME = "Model Training STAGE"
class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        try:
            logger.info(f"Starting {STAGE_NAME}...")
            config = Configuration()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTraining(model_trainer_config)
            model_trainer.train()
            logger.info(f"{STAGE_NAME} completed.")
        except Exception as e:
            logger.error(f"{STAGE_NAME} failed.")
            raise e
        
