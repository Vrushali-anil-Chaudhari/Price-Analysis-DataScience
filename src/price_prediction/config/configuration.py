from src.price_prediction.constants import *
from src.price_prediction.utils.common import read_yaml, create_directories ,   save_json
from price_prediction.entity.config_entity import DataIngestionConfig, DataValidationConfig,DataTransformationConfig, ModelTrainerConfig, ModelEvaluateConfig
class Configuration:
    def __init__(self, 
    config_filepath = CONFIG_FILE_PATH,
    params_filepath = PARAMS_FILE_PATH,
    schema_filepath = SCHEMA_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])
        
     
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])
        data_transformation_config = DataTransformationConfig(
            root_dir = Path(config.root_dir),
            data_path = Path(config.data_path)
        )
        return data_transformation_config
    

    def get_model_trainer_config(self):
        config = self.config.model_trainer
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])
        return ModelTrainerConfig(
            root_dir = config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            target_column = str(list(schema.keys())[0])
        )
    
    def get_model_evaluation_config(self):
        config = self.config.model_evaluation
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])
        return ModelEvaluateConfig(
            root_dir = Path(config.root_dir),
            test_data_path = Path(config.test_data_path),
            model_path = Path(config.model_path),
            metric_file_name = Path(config.metric_file_name),
            target_column = str(list(schema.keys())[0]),
            mlflow_uri = config.mlflow_uri
        )