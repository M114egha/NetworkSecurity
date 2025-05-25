from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from  networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from  networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("INtitiate data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed")
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact , data_validation_config)
        print(dataingestionartifact)
        logging.info("INtitiate data validation")
        datavalidationartifact=data_validation.initiate_data_validation()
        logging.info("Data validation completed")
        print(datavalidationartifact)

        
       
        

    except Exception  as e:
        raise NetworkSecurityException(e, sys)