#This file contains the information of constants used in training
#All capital values are constants
import os
TARGET_COLUMN = "class"
PIPELINE_NAME = "sensor"
ARTIFACT_DIR = "artifact"
FILE_NAME = "sensor.csv"

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



