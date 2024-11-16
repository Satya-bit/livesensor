from dataclasses import dataclass 
import os
import pymongo

@dataclass #It is used to store data

class EnvironmentVariable:
    mongo_db_url:str=os.getenv("MONGO_DB_URL") #mongo db url is object. Top read the url from .env it used .getenv from init file
    

env_var=EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)