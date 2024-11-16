# This file is to push the data to mongodb read by the config file
import pandas as pd
import numpy as np
import logging
import json
from sensor.config import mongo_client
def dump_csv_file_to_mongodb_collection(file_path:str,database_name:str,collection_name:str)->None:
    try:
        df=pd.read_csv(file_path)
        df.reset_index(drop=True,inplace=True) #keeps the index and donot add any new index
        json_records=list(json.loads(df.T.to_json()).values())#converts the dataframe to list of dictionaries and make sure to do Transpose or else it will store in bad order for JSON 
        mongo_client[database_name][collection_name].insert_many(json_records)
    except Exception as e:
        print(e)
    