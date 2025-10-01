import logging
from config.config import Config

def setup_logger(name="pipeline_logger"):
    """Configure un logger pour le pipeline."""
    logger = logging.getLogger(name)
    logger.setLevel(Config.LOG_LEVEL)

    # Format du log
    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] %(name)s: %(message)s'
    )

    # Console handler
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File handler
    fh = logging.FileHandler("pipeline.log")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
