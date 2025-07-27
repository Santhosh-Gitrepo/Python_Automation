"""
Creates a timestamped log file
Saves it in a folder named Test_Output/
Configures logging to both file and console
Can be imported and reused in any test script
"""

import logging
import os
from datetime import datetime


def logger_setup(name: str = "test_logger") -> logging.Logger:
    """Creates a logger with a timestamped file in Test_Output."""

    # Simple relative path to go up one level and into Test_Output/Logs
    logs_dir = "../Test_Output/Logs"
    os.makedirs(logs_dir, exist_ok=True)

    # Create timestamped log file
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(logs_dir, f"test_log_{timestamp}.log")

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid adding handlers multiple times
    if not logger.handlers:
        # File handler
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
