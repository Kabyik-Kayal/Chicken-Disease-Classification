import os
import logging
import sys
from datetime import datetime

LOG_DIR = "logs"
LOG_FILEPATH = os.path.join(LOG_DIR, f"running_logs_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log")

os.makedirs(LOG_DIR, exist_ok=True)

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(LOG_FILEPATH),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("ChickenDiseaseClassifierLogger")
