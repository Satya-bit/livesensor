from sensor.exception import SensorException
import os
import sys

def test_exception():
    try:
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)
if __name__ == "__main__":  #module control. It prevents execution or import of the module. It will only throw error for this file. The variables donot run in this file when we use import.
    try:
        test_exception()
    except Exception as e:
        print(e)