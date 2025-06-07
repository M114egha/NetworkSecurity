import os
import  sys

import certifi
ca= certifi.where()

from dotenv import load_dotenv
load_dotenv()
monogo_db_url = os.getenv("MONGO_DB_URL")
print(monogo_db_url)


import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline

from fastapi import FastAPI ,File, UploadFile, Request
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run  as app_run
from starlette.responses import RedirectResponse
import pandas as pd
from threading import Thread


from networksecurity.utils.main_utils.utils import  load_object

client = pymongo.MongoClient(monogo_db_url, tlsCAFile=ca)

from networksecurity.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from networksecurity.constant.training_pipeline import DATA_INGESTION_DATABASE_NAME

api=FastAPI()
origin = ["*"]
api.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.get("/", tags=['authentication'])
async def index():
    return RedirectResponse(url="/docs")

def run_training_pipeline():
    training_pipeline = TrainingPipeline()
    training_pipeline.run_pipeline()


@api.get("/train")
async def train():
    try:
        thread = Thread(target=run_training_pipeline)
        thread.start()
        return {"message": "Training started in the background"}
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e


if __name__ == "__main__":
    app_run(api, host="localhost" , port=8000)
