# utils.py

import os
import sys
import pickle
import pandas as pd
import numpy as np
import seaborn as sns
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
            logging.info("-----"*5)
            logging.info("{} model is getting evaluated".format(key))
            model = models.get(key)

            # Train model
            model.fit(X_train, y_train)

            # Predict Testing data
            y_test_pred = model.predict(X_test)

            # Get R2 scores for train and test data
            r2_model_train_score = r2_score(y_true=y_train,y_pred=model.predict(X_train))
            r2_model_test_score = r2_score(y_true=y_test, y_pred=y_test_pred)
            mae = mean_absolute_error(y_true=y_test, y_pred=y_test_pred)
            mse = mean_squared_error(y_true=y_test, y_pred=y_test_pred)
            
            logging.info("R Squared on Train Data: {}".format(r2_model_train_score))
            logging.info("R Squared on Test Data: {}".format(r2_model_test_score))
            logging.info("Mean Absolute Error: {}".format(mae))
            logging.info("Mean Squared Error: {}".format(mse))
            logging.info("Root Mean Squared Error: {}".format(np.sqrt(mse)))

            report[key] = r2_model_test_score

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
