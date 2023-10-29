# logger.py

import logging
import os
from datetime import datetime

# Log filename: date--hr--mm-ss.log
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

LOG_PATH = os.path.join(os.getcwd(), "logs")

os.makedirs(LOG_PATH, exist_ok=True)

LOG_FILEPATH = os.path.join(LOG_PATH, LOG_FILE)

logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
                    )


if __name__ == '__main__':
    logging.info("i have just tested the things")
