import logging
from pathlib import Path

_LOGGER = None

def get_logger(name: str = "ml_project"):
    global _LOGGER
    if _LOGGER is not None:
        return _LOGGER

    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fh = logging.FileHandler(log_dir / "app.log")
        ch = logging.StreamHandler()

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

    _LOGGER = logger
    return logger
