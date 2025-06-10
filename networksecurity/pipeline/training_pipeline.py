import os
import sys

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import(
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
)

from networksecurity.entity.artifact_entity import(
    DataIngestionArtifact,
    DataValidationArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact,
)


class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self):
        try:
            self.data_ingestion_config=DataIngestionConfig(self.training_pipeline_config)
            logging.info("Initiating data ingestion")
            data_ingestion=DataIngestion(self.data_ingestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact} ")
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact):
        try:
            data_validation_config=DataValidationConfig(self.training_pipeline_config)
            data_validation=DataValidation(data_ingestion_artifact ,data_validation_config)
            logging.info("Initiating data validation")
            data_validation_artifact=data_validation.initiate_data_validation()
            return data_validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        
    def start_data_transformation(self, data_validation_artifact: DataValidationArtifact):
        try:
            data_transformation_config=DataTransformationConfig(self.training_pipeline_config)
            data_transformation=DataTransformation( data_validation_artifact,data_transformation_config)
            logging.info("Initiating data transformation")
            data_transformation_artifact=data_transformation.initiate_data_transformation()
            logging.info("Data transformation completed")
            return data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        
    def start_model_trainer(self, data_transformation_artifact: DataTransformationArtifact):
        try:
            model_trainer_config=ModelTrainerConfig(self.training_pipeline_config)
            model_trainer=ModelTrainer(model_trainer_config, data_transformation_artifact)
            logging.info("Initiating model training")
            model_trainer_artifact=model_trainer.initiate_model_trainer()
            logging.info("Model training completed ") 
            return model_trainer_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        

    
    
    def run_pipeline(self):
        try:
            logging.info(" Training pipeline started")  # Add this
            print(" Training pipeline started")
            data_ingestion_artifact = self.start_data_ingestion()
            logging.info(" Data ingestion completed")
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact)
            logging.info("Data validation completed")
            data_transformation_artifact = self.start_data_transformation(data_validation_artifact)
            logging.info("Data transformation completed")
            model_trainer_artifact = self.start_model_trainer(data_transformation_artifact)
            logging.info("Model training completed")
            
            return model_trainer_artifact
        
        except Exception as e:
            logging.error(f" Pipeline failed: {e}")
            raise NetworkSecurityException(e, sys) from e
    
