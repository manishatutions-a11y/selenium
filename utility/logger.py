import logging

def get_logger():
    logger = logging.getLogger(__name__)          # fixed getlogger → getLogger
    logger.setLevel(logging.INFO)                  # fixed setlevel → setLevel
    if not logger.handlers:                        # avoid duplicate handlers
        handler = logging.FileHandler("file.log")
        formatter = logging.Formatter("%(asctime)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)                 # use addHandler instead of setHandler
    return logger