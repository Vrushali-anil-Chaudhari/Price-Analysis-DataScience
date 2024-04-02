from src.price_prediction import logger
from src.price_prediction.pipeline.stage_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion STAGE"

data_ingestion_pipeline = DataIngestionTrainingPipeline()
data_ingestion_pipeline.main()
