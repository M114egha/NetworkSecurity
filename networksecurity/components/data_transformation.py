import sys,os
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from networksecurity.constant.training_pipeline import TARGET_COLUMN
from networksecurity.constant.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS

from networksecurity.entity.artifact_entity import(
    DataTransformationArtifact,
    DataValidationArtifact
)

from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils.utils import save_numpy_array_data , save_object


class DataTransformation:
    def __init__(self , data_validation_artifact:DataValidationArtifact,
                 data_transformation_config :DataTransformationConfig):
        try:
            self.data_validation_artifact:DataValidationArtifact=data_validation_artifact
            self.data_transformation_config:DataTransformationConfig = data_transformation_config
        except Exception as e:
            raise NetworkSecurityException(e , sys) from e 

    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        
    def get_data_transfomer_object(cls)->Pipeline:
        "It initaielixees  knn imputer onbject with the params specfied in the traing_pipeline.py and returns a "
        "Pipeline object with the knnimputer onbject as the first step"

        logging.info("Enter  get_data_transfomer_object  of DataTrsnformationClass")
        try:
            imputer : KNNImputer=KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            logging.info(f"Initialize Knnimputer with {DATA_TRANSFORMATION_IMPUTER_PARAMS}")
            processor:Pipeline =Pipeline([("imputer" , imputer)])
            return processor
        except Exception as e:
            raise Exception 
    

    def initiate_data_transformation(self)->DataTransformationArtifact:
        logging.info("Entered initiate data transformation method of Data Transformation ") 
        try:
            logging.info("Starting Data Transformation")
            train_df= DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df=DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)



            #INput_feature dataframe
            input_feature_train_df=train_df.drop(columns=[TARGET_COLUMN] , axis=1)
            target_feature_train_df= train_df[TARGET_COLUMN]
            target_feature_train_df=target_feature_train_df.replace(-1 , 0)

            input_feature_test_df=test_df.drop(columns=[TARGET_COLUMN] , axis=1)
            target_feature_test_df= test_df[TARGET_COLUMN]
            target_feature_test_df=target_feature_test_df.replace(-1 , 0)

            preprocessor=self.get_data_transfomer_object()
            preprocessor_object= preprocessor.fit(input_feature_train_df)
            transformed_input_train_feature=preprocessor_object.transform(input_feature_train_df)
            transformed_input_test_feature=preprocessor_object.transform(input_feature_test_df)

            #Combining both the arrays
            train_arr = np.c_[transformed_input_train_feature , np.array(target_feature_train_df)]
            test_arr = np.c_[transformed_input_test_feature , np.array(target_feature_test_df)]


            #Save numpy array data
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path , array=train_arr ,)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path , array=test_arr ,)
            save_object(self.data_transformation_config.transformed_object_file_path , preprocessor_object ,)
            save_object("final_model/preprocessor.pkl" , preprocessor_object)


            #Preparing artifacts
            data_transformation_artifact=DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )
            return data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e , sys) from e