# data_transformation.py

import os
import sys
import pandas as pd
import numpy as np

from dataclasses import dataclass
from src.GemstonePricePrediction.exception import CustomException
from src.GemstonePricePrediction.logger import logging

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

from src.GemstonePricePrediction.utils.utils import save_object


@dataclass
class DataTransformationConfig:
    """
    This is configuration class for Data Transformation
    """
    preprocessor_obj_file_path: str = os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    """
    This class handles Data Transformation
    """
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def transform_data(self):
        try:
            logging.info('Data Transformation initiated')
            
            # Define which columns should be ordinal-encoded and which should be scaled
            categorical_cols = ['cut', 'color', 'clarity']
            numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']
            
            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
            
            logging.info('Pipeline Initiated')
            
            # Numerical Pipeline
            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )
            
            # Categorigal Pipeline
            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('ordinalencoder', OrdinalEncoder(categories=[cut_categories, color_categories, clarity_categories])),
                    ('scaler', StandardScaler())
                ]
            )
            
            preprocessor = ColumnTransformer([
                ('num_pipeline', num_pipeline, numerical_cols),
                ('cat_pipeline', cat_pipeline, categorical_cols)
            ])
            
            return preprocessor
        
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")
            raise CustomException(e, sys)   # type: ignore
            
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head : \n{test_df.head().to_string()}')
            
            preprocessing_obj = self.transform_data()
            
            target_column_name = 'price'
            drop_columns = [target_column_name, 'id']
            
            input_feature_train_df = train_df.drop(columns=drop_columns, axis=1)
            target_feature_train_df = train_df[target_column_name]
               
            input_feature_test_df = test_df.drop(columns=drop_columns, axis=1)
            target_feature_test_df = test_df[target_column_name]
            
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            input_feature_train_arr_df = pd.DataFrame(input_feature_train_arr, columns=input_feature_train_df.columns)
            input_feature_test_arr_df = pd.DataFrame(input_feature_test_arr, columns=input_feature_test_df.columns)

            logging.info("Applying preprocessing object on training and testing datasets")
            
            # Using numpy.C_ to concatenate transformed features with target feature
            # train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            # test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            train_df = pd.concat([input_feature_train_arr_df, target_feature_train_df], axis=1)
            test_df = pd.concat([input_feature_test_arr_df, target_feature_test_df], axis=1)

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            
            logging.info("preprocessing pickle file saved")
            
            return (
                train_df,
                test_df
            )
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise CustomException(e, sys)   # type: ignore
