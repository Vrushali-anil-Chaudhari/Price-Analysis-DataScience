from src.price_prediction.config.configuration import Configuration
from src.price_prediction.components.model_evaluation import ModelEvaluation
from src.price_prediction import logger

STAGE_NAME = "Model Evaluation STAGE"

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            logger.info(f"Starting {STAGE_NAME}...")
            config = Configuration()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(model_evaluation_config)
            model_evaluation.log_into_mlflow()
            logger.info(f"{STAGE_NAME} completed.")
        except Exception as e:
            logger.error(f"{STAGE_NAME} failed.")
            raise Exception(f"Failed to log metrics into mlflow: {e}")