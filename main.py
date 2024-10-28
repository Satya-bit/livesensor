from sensor.exception import SensorException
import os
import sys
from sensor.logger import logging

def test_exception():
    try:
        logging.info("error of division by zero please check the code")
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)
        # raise e
if __name__ == "__main__":  #module control. It prevents execution or import of the module. It will only throw error for this file. The variables donot run in this file when we use import.
    try:
        test_exception()
    except Exception as e:
        print(e)