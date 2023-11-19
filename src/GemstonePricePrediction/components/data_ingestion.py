# data_ingestion.py

import os
import sys
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path  # Handles naming of both LinuxPath and WindowsPath

from src.GemstonePricePrediction.logger import logging
from src.GemstonePricePrediction.exception import CustomException
from src.GemstonePricePrediction.utils.utils import load_dataframe


@dataclass
class DataIngestionConfig:
    """
    This is configuration class for Data Ingestion
    """
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")


class DataIngestion:
    """
    This class handles Data Ingestion
    """
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
       
    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")
       
        try:
            data = load_dataframe("notebooks/data", "gemstone.csv")
            logging.info("Dataset loaded into dataframe")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)), exist_ok=True)
            
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw dataset is saved in artifacts folder")
            
            train_data, test_data = train_test_split(data, test_size=0.25)
            logging.info("Dataset is splitted into Train & Test data")
            
            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Train & Test dataset are saved in artifacts folder")

            logging.info("Data ingestion completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
     
        except Exception as e:
            logging.info("exception during occured at data ingestion stage")
            raise CustomException(e, sys)  # type: ignore
