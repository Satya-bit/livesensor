#To read the schema.yaml
#In utils folder there is general code for the project. Tjis code can be used anywhere
import yaml
import os
import pandas
import numpy
import dill
import sys
from sensor.exception import SensorException

def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise SensorException(e,sys)
    
    
def write_yaml_file(file_path: str, content: object, replace: bool = False): #If there any no error i.e. it is false then it will create the file
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file_obj:
            yaml.dump(content, file_obj)
    except Exception as e:
        raise SensorException(e, sys)