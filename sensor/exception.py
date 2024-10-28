import sys
import os # These two libraries are used for system level like Operating system. We will get to know errors form os.

def error_message_detail(error,error_detail:sys): #To capture the line number, file address and error message
    _,_,exc_tb=error_detail.exc_info() #exc_tb is used to get the line number. We are only interested in exc_tb that's why we kept only exc_tb and put two dashes because we donot want that two from the tuple.
    filename=exc_tb.tb_frame.f_code.co_filename #co_filename is used to get the file name
    
    error_message="error occured and the file name is [{0}] and the line number is [{1}] and the error is [{2}]".format(
    filename,exc_tb.tb_lineno,str(error))
    
    return error_message
    
class SensorException(Exception): #Exception is superclass. All exception handling things are under this and it handles the exception. The class is inherited.
    def __init__(self,error_message,error_detail:sys): #constructor and self is written which depicts that this is the constructor of this class. 
                                                       #error detail is passed as sys to detect error is in which line and file. Error_message is done by exception handling
        
        super().__init__(error_message)     #super is used to call the constructor of the parent class. Any class which is inherited, to use that class we use super function.
        
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
        
    def __str__(self): #str is used to return the error message in string format
        return self.error_message
        
#Note we get error form Exception class and to get detail we used sys library