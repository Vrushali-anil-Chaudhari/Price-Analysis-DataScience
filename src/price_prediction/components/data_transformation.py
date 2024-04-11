import os
from src.price_prediction import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.price_prediction.entity.config_entity import DataTransformationConfig
class DataTransformation:
    def __init__(self, config : DataTransformationConfig):
        self.config = config
        self.data = pd.read_csv(self.config.data_path)

    def handling_missing_values(self):
        
        df = self.data.drop(columns=["vin"])
        logger.info("vin column dropped")
        data = df.dropna()
        logger.info("Missing values handled")
        print(data)
        return data
    
    def date_time_conversion(self ,df):
        saledate = df['saledate'].str.split(expand=True)[[1,2,3,4,5]]
        df['Datetime'] = pd.to_datetime(saledate[1] + ' ' + saledate[2].astype(str) + ' ' + saledate[3].astype(str) + ' ' + saledate[4] + ' ' + saledate[5], utc=True)
        # Get only the date part
        df['Datetime'] = df['Datetime'].dt.date
        df.drop(columns=['saledate'], inplace=True)
        return df
    
    def train_test_split(self, df):
        train, test = train_test_split(df)
        train.to_csv(os.path.join(self.config.root_dir , 'train.csv'), index=False)   
        test.to_csv(os.path.join(self.config.root_dir , 'test.csv'), index=False)
        logger.info("train and test data saved")

    
   

    
    

    
    