import logging
import os

# Ensure the log directory and file are created securely
log_file = "weather.log"

if not os.path.exists(log_file):
    open(log_file, 'a').close()
    os.chmod(log_file, 0o600)  # Owner can read/write

logger = logging.getLogger("WeatherAppLogger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(log_file)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
