from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os , sys
from sensor.logger import logging


from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.utils.main_utils import load_object
from sensor.ml.model.estimator import ModelResolver,TargetValueMapping
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
from sensor.pipeline import training_pipeline
from sensor.pipeline.training_pipeline import TrainPipeline
import os
from sensor.utils.main_utils import read_yaml_file
from sensor.constant.training_pipeline import SAVED_MODEL_DIR

import numpy as np
from  fastapi import FastAPI
from sensor.constant.application import APP_HOST, APP_PORT
from starlette.responses import RedirectResponse
from uvicorn import run as app_run
from fastapi.responses import Response
from sensor.ml.model.estimator import ModelResolver,TargetValueMapping
from sensor.utils.main_utils import load_object
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi import FastAPI, File, UploadFile, Response
import pandas as pd
from sensor.utils2 import dump_csv_file_to_mongodb_collection

# def test_exception():
#     try:
#         logging.info("ki yaha p bhaiaa ek error ayegi diveision by zero wali error ")
#         a=1/0
#     except Exception as e:
#        raise SensorException(e,sys) 
app=FastAPI()


origins = ["*"]
#Cross-Origin Resource Sharing (CORS) 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/",tags=["authentication"]) #For connection
async def index():  #Asyn function because we don't need to wait for one response to get input. All vcan run parellelly, so less time
    return RedirectResponse(url="/docs")




@app.get("/train") #For training
async def train():
    try:
        training_pipeline = TrainPipeline()
        if training_pipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")
            
        training_pipeline.run_pipeline()
        return Response("Training successfully completed!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")
        



@app.get("/predict")  # For prediction
async def predict():
    try:
        # Load the test CSV file into a DataFrame
        df = pd.read_csv("test.csv")
        
        # Check if DataFrame is loaded correctly
        if df is None or df.empty:
            return Response("Error: Test data is empty or not loaded correctly.")

        # Replace 'na' with np.nan
        df.replace("na", np.nan, inplace=True)

        # Drop specified columns
        columns_to_drop = ['br_000', 'bq_000', 'bp_000', 'ab_000', 'cr_000', 'bo_000', 'bn_000']
        df.drop(columns=columns_to_drop, errors='ignore', inplace=True)  # Ignore if columns don't exist

        # Check if the model exists and fetch the best model
        Model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not Model_resolver.is_model_exists():
            return Response("Model is not available.")
        
        best_model_path = Model_resolver.get_best_model_path()
        model = load_object(file_path=best_model_path)

        # Ensure the features match the model's input
        if hasattr(model, 'feature_names_in_'):
            df = df[model.feature_names_in_]  # Align test data with model's training features

        # Make predictions
        y_pred = model.predict(df)
        df['predicted_column'] = y_pred

        # Replace the predicted values with meaningful labels
        df['predicted_column'].replace(TargetValueMapping().reverse_mapping(), inplace=True)

        # Save the predictions to a file (optional)
        output_path = "predictions.csv"
        df.to_csv(output_path, index=False)

        return Response(f"Prediction successful! Output saved to {output_path}")
    
    except Exception as e:
        return Response(f"Error Occurred! {e}")




def main():
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)

if __name__ == "__main__":

    # file_path="C:/Users/satya/Documents/data_science_roadmap/Machine_Learning/SENSORLIVE/aps_failure_training_set1.csv"
    # database_name="APS"
    # collection_name ="sensor"
    # dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)
    app_run(app,host=APP_HOST,port=APP_PORT)
    










  












    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)