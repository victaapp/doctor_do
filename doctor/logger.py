# logger.py
import os
import logging

def create_logger(filename, logger_name):
    # Get the absolute path to the logs folder in the root directory
    logs_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
    log_filename = os.path.join(logs_folder_path, filename)

    # Configure a new logger and handler
    new_logger = logging.getLogger(logger_name)
    new_logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(log_filename)
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    new_logger.addHandler(handler)

    return new_logger
