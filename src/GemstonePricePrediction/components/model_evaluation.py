# model_evaluation.py

import os
import sys

import mlflow
import mlflow.sklearn
import numpy as np

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from urllib.parse import urlparse
from dataclasses import dataclass

from src.GemstonePricePrediction.utils.utils import load_object, CustomException

@dataclass
class ModelEvaluation:

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def initiate_model_evaluation(self, train_array, test_array):
        try:
            X_test, y_test = (test_array.iloc[:, :-1], test_array.iloc[:, -1])
            model_path = os.path.join("artifacts", "model.pkl")
            model = load_object(model_path)

            """
            If MLFLOW_TRACKING_URI, MLFLOW_TRACKING_USERNAME & MLFLOW_TRACKING_PASSWORD are set correctly, 
            then tracking_url_type = https  --> DagsHub MLFlow
            else tracking_url_type = file --> Local MLFLow
            """
            mlflow.set_registry_uri("https://dagshub.com/abhijitpaul0212/GemstonePricePrediction.mlflow")
            tracking_url_type = urlparse(mlflow.get_tracking_uri()).scheme
            print(tracking_url_type)

            with mlflow.start_run():
                predicted_qualities = model.predict(X_test)

                (rmse, mae, r2) = self.eval_metrics(actual=y_test, pred=predicted_qualities)

                mlflow.log_metric("rmse", rmse)
                mlflow.log_metric("mae", mae)
                mlflow.log_metric("r2", r2)

                if tracking_url_type != "file":
                    mlflow.sklearn.log_model(model, "model", registered_model_name="ml_model")
                else:
                    mlflow.sklearn.log_model(model, "model")
        except Exception as e:
            raise CustomException(e, sys)
