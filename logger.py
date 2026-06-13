import os
import logging
from logging import Logger


LOGS_FILE = 'logs/app.log'

os.makedirs(os.path.dirname(LOGS_FILE), exist_ok=True)


def get_logger(name: str) -> Logger:
    """
    The function defines a logger that returns output to a file on the terminal screen.

    Args:
        name: The name of the file in which the logger is imported and its use
    
    Rerurns: 
        Logger object
    """
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(LOGS_FILE)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(message)s | %(name)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger