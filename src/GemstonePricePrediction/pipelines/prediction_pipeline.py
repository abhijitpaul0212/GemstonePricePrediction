# prediction_pipeline.py

import os
import sys
import pandas as pd
from dataclasses import dataclass

from src.GemstonePricePrediction.logger import logging
from src.GemstonePricePrediction.exception import CustomException
from src.GemstonePricePrediction.utils.utils import load_object


@dataclass
class PredictPipeline:

    def predict(self, features):
        try:
            logging.info('Prediction Pipeline initiated')
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            model_path = os.path.join("artifacts", "model.pkl")

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            # preprocessed and scaled data
            scaled_data = preprocessor.transform(features)

            pred = model.predict(scaled_data)
            logging.info('Predicted value: {}'.format(pred))
            
            return pred

        except Exception as e:
            raise CustomException(e, sys)
  

class CustomData:
    def __init__(self,
                 carat: float,
                 depth: float,
                 table: float,
                 x: float,
                 y: float,
                 z: float,
                 cut: str,
                 color: str,
                 clarity: str):
        
        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity
                
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat': [self.carat],
                'depth': [self.depth],
                'table': [self.table],
                'x': [self.x],
                'y': [self.y],
                'z': [self.z],
                'cut': [self.cut],
                'color': [self.color],
                'clarity': [self.clarity]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Custom input is converted to Dataframe: \n{}'.format(df.head()))
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e, sys)
