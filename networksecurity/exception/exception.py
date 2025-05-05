import sys
from networksecurity.logging import logger



class NetworkSecurityException(Exception):

    def __init__(self, error_message  , error_details:sys):# error_message is a string, error_details is a sys object
        self.error_message = error_message
        _,_,exc_tb=error_details.exc_info()  # unpacking the exception details

        self.lineno= exc_tb.tb_lineno
        self.filename= exc_tb.tb_frame.f_code.co_filename 

    
    def __str__(self):
        return "Error occured in script name[{0}] at line no [{1}] with error message [{2}]".format(
            self.filename, self.lineno, str(self.error_message)
        )
    

if __name__=="__main__":
    try:
        logger.logging.info("Enter the try Bloc")
        a=1/0
    except Exception as e:
        raise NetworkSecurityException(e, sys)