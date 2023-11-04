# model_trainer.py

import os
import sys

from dataclasses import dataclass
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet

from src.GemstonePricePrediction.logger import logging
from src.GemstonePricePrediction.exception import CustomException
from src.GemstonePricePrediction.utils.utils import save_object
from src.GemstonePricePrediction.utils.utils import evaluate_model
from explainerdashboard import RegressionExplainer, ExplainerDashboard


@dataclass
class ModelTrainerConfig:
    """
    This is configuration class for Model Trainer
    """
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')
    dashboard_file_path = os.path.join('artifacts', 'dashboard.yaml')
    explainer_file = os.path.join('explainer.joblib')


class ModelTrainer:
    """
    This class handles Model Training
    """
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initate_model_training(self, train_array, test_array):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')
            X_train, y_train, X_test, y_test = (
                train_array.iloc[:, :-1],
                train_array.iloc[:, -1],
                test_array.iloc[:, :-1],
                test_array.iloc[:, -1]
            )

            models = {
                'LinearRegression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'Elasticnet': ElasticNet()
            }
            
            model_report: dict = evaluate_model(X_train, y_train, X_test, y_test, models)
            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')

            # To get best model score from dictionary 
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            
            explainer = RegressionExplainer(best_model, X_test, y_test)
            db = ExplainerDashboard(explainer, title="Gemstone Explainer Dashboard", shap_interaction=False)
            db.to_yaml(
                self.model_trainer_config.dashboard_file_path, 
                explainerfile=self.model_trainer_config.explainer_file,
                dump_explainer=True)

            save_object(
                 file_path=self.model_trainer_config.trained_model_file_path,
                 obj=best_model
            )
          
        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise CustomException(e, sys)
