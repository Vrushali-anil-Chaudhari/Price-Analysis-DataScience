from src.price_prediction import logger
from src.price_prediction.pipeline.stage_data_ingestion import DataIngestionTrainingPipeline
from src.price_prediction.pipeline.stage_data_validation import DataValidationTrainingPipeline
from src.price_prediction.pipeline.stage_data_transformation import DataTransformationTrainingPipeline
from src.price_prediction.pipeline.stage_model_training import ModelTrainingPipeline
from src.price_prediction.pipeline.stage_model_evaluation import ModelEvaluationPipeline
data_ingestion_pipeline = DataIngestionTrainingPipeline()
data_ingestion_pipeline.main()
data_validation_pipeline = DataValidationTrainingPipeline()
data_validation_pipeline.main()
data_transformation_pipeline = DataTransformationTrainingPipeline()
data_transformation_pipeline.main()
model_training_pipeline = ModelTrainingPipeline()
model_training_pipeline.main()
model_evaluation_pipeline = ModelEvaluationPipeline()
model_evaluation_pipeline.main()