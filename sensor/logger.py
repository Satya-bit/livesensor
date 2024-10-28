#This file is use to log the error and to see at which point our code is working. During production we can see the logger file when we deploy instead of opening the console every time.
import logging 
import os
import sys
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  #This is the name of the file which is time.

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #Used to join the relative path with path. os.getcwd() is used to get the current working directory where the error is present. logs is the name of the folder and LOG_FILE is the name of the file.

os.makedirs(logs_path,exist_ok=True) #This is used to create the directory(FOLDER) if it doesn't exist. exist_ok=True means if the directory already exists, it will not create the directory again.

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) #MAKES THE PATH FOR THE LOG FILE.


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  #Here the name is the name of teh logger. The lineno is the line number of the code. level is INFO and message is error. s is for string and d is for digit.
    level=logging.INFO # There are five levels of logging. INFO, DEBUG, WARNING, ERROR, CRITICAL
)