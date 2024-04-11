from src.price_prediction import logger
from src.price_prediction.entity.config_entity import ModelTrainerConfig
import pandas as pd
import joblib
import os
from price_prediction import logger
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import GradientBoostingRegressor

class ModelTraining:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
        X_train = train_data.drop(columns = [self.config.target_column])
        y_train = train_data[self.config.target_column]
        X_test = test_data.drop(columns = [self.config.target_column])
        y_test = test_data[self.config.target_column]
        numerical_features = X_train.select_dtypes(include=['int64', 'float64']).columns.tolist()
        categorical_features = X_train.select_dtypes(include=['object']).columns.tolist()
        preprocessor = ColumnTransformer(
                transformers=[
                    ('num', StandardScaler(), numerical_features),
                    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
                ])
        model = Pipeline(
            steps = [
                ('preprocessor', preprocessor),
                ('regressor', GradientBoostingRegressor(random_state=42))
            ]
        )

        model.fit(X_train, y_train)
        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))
