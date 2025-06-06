import logging
import os
import time
from  datetime import datetime

LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"# log file name with timestamp

logs_path=os.path.join(os.getcwd(), "logs", LOG_FILE)# logs directory path
os.makedirs(logs_path, exist_ok=True)# create logs directory if it doesn't exist

LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE)# full path to the log file


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "[%(asctime)s]  %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
'''
import logging
import os
from datetime import datetime

# Create logs directory if not exists
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Log filename with timestamp to avoid overwriting
LOG_FILE = os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Configure logging to file
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(name)s - %(message)s',
    filemode='w'  # Overwrite file each run; use 'a' to append
)

# Optional: create a logger instance for importing
logger = logging.getLogger(__name__)
'''