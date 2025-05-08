import os
import sys
import pandas as pd
import numpy as np


'''
Defining constant avar for traing pipeline'''
TARGET_COLUMN ="Result"
PIPELINE_NAME :str ="NetworkSecurity"
ARTIFACT_DIR :str = "Artifacts"
FILE_NAME :str="phishingData.csv"

TRAIN_FILE_NAME :str= "train.csv"
TEST_FILE_NAME :str= "test_csv"








'''
Dta ingestion related constant 
'''
DATA_INGESTION_COLLECTION_NAME: str="NetworkData"
DATA_INGESTION_DATABASE_NAME :str ="MeghanaAI"
DATA_INGESTION_DIR_NAME :str= "data_ingestion"
DATA_INGESTION_FEATURE_STOTRE_DIR :str= "feature_store"
DATA_INGESTION_INGESTED_DIR :str ="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO :str= 0.2
