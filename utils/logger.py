"""Logging configuration for the simulator."""

import logging

def setup_logger(log_level: int = logging.INFO) -> logging.Logger:
    """Setup and return a configured logger."""
    logger = logging.getLogger('thermosim')
    logger.setLevel(log_level)
    
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger 