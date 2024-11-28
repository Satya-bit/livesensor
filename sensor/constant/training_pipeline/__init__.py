#This file contains the information of constants used in DIFFERENT COMPONENTS
#All capital values are constants
import os
TARGET_COLUMN = "class"
PIPELINE_NAME = "sensor"
ARTIFACT_DIR = "artifact"
FILE_NAME = "sensor.csv"

SAVED_MODEL_DIR = os.path.join("saved_models")
TRAINING_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"

SCHEMA_FILE_PATH = os.path.join("config","schema.yaml")

SCHEMA_DROP_COLS = "drop_columns"

"""
Data ingestion related constants for easy configuration and code maintenance.
These constants help in standardizing the naming and paths used throughout the data ingestion process.
"""

# Name of the collection or table in the database where sensor data is stored.
DATA_INGESTION_COLLECTION_NAME: str = "sensor"

# Name of the directory where data ingestion operations and outputs are stored.
DATA_INGESTION_DIR_NAME: str = "data_ingestion"

# Directory for storing processed features that are used in model training or prediction.
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

# Directory where ingested data is saved after being processed.
DATA_INGESTION_INGESTED_DIR_NAME: str = "ingested"

# Ratio for splitting the dataset into training and testing sets. 0.2 means 20% test data, 80% training data.
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2


"""
data validation related constant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"


"""
Data Transformation ralated constant start with DATA_TRANSFORMATION VAR NAME
"""

DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"


"""
Model Trainer ralated constant start with MODE TRAINER VAR NAME
"""

MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
# MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD: float = 0.05
MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD: float = 0.5


"""
Model Trainer ralated constant start with MODE TRAINER VAR NAME
"""
MODEL_EVALUATION_DIR_NAME: str = "model_evaluation"
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_EVALUATION_REPORT_NAME= "report.yaml"

MODEL_PUSHER_DIR_NAME = "model_pusher"
MODEL_PUSHER_SAVED_MODEL_DIR=SAVED_MODEL_DIR




