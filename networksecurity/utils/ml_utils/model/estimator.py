from networksecurity.constant.training_pipeline import SAVED_MODEL_DIR , MODEL_FILE_NAME
import os
import sys
from networksecurity.exception.exception import NetworkSecurityException    
from networksecurity.logging.logger import logging


class NetworkModel:
    def __init__(self, model, preprocessor):
        try:
            self.model = model
            self.preprocessor = preprocessor
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        


    def predict(self, X):
        try:
            x_transform=self.preprocessor.transform(X)
            y_pred =self.model.predict(x_transform)
            return y_pred
        except Exception as e:  
            raise NetworkSecurityException(e, sys) from e