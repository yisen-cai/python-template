import logging

logger = logging.getLogger(__name__)

def hello():
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("hello world")