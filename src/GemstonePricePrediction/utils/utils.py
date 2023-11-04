# utils.py

import os
import sys
import pickle
import pandas as pd
from pathlib import Path

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from src.GemstonePricePrediction.logger import logging
from src.GemstonePricePrediction.exception import CustomException


def load_dataframe(path: str, filename: str):
    return pd.read_csv(Path(os.path.join(path, filename)))


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info("Object is saved at {}".format(file_path))

    except Exception as e:
        logging.info('Exception occured while saving object')
        raise CustomException(e, sys)


def evaluate_model(X_train, y_train, X_test, y_test, models: dict) -> dict:
    try:
        report = {}
        
        for key in models:
            logging.info("{} model is getting evaluated".format(key))
            model = models.get(key)

            # Train model
            model.fit(X_train, y_train)

            # Predict Testing data
            y_test_pred = model.predict(X_test)

            # Get R2 scores for train and test data
            # train_model_score = r2_score(ytrain,y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[key] = test_model_score

        return report

    except Exception as e:
        logging.info('Exception occured during model training')
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            logging.info("Object read and loaded from {}".format(file_path))
            return pickle.load(file_obj)
        
    except Exception as e:
        logging.info('Exception occured while loading object')
        raise CustomException(e, sys)
