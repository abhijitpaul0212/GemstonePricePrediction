# training_pipeline.py

from src.GemstonePricePrediction.components.data_ingestion import DataIngestion
from src.GemstonePricePrediction.components.data_transformation import DataTransformation
from src.GemstonePricePrediction.components.model_trainer import ModelTrainer
from dataclasses import dataclass


@dataclass
class TrainingPipeline:
    
    def start(self):
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        data_transformation = DataTransformation()
        train_arr, test_arr = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

        model_trainer = ModelTrainer()
        model_trainer.initate_model_training(train_arr, test_arr)
