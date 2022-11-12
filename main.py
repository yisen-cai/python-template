from custom import CustomFormatter
from example.utils import hello
import logging

import logging.config


logging.config.fileConfig('logging.conf', disable_existing_loggers=False)


# module-level logger
logger = logging.getLogger(__name__)

# ch = logging.StreamHandler()
# ch.setFormatter(CustomFormatter())
# logger.addHandler(ch)

# set logger level
# logger.setLevel(logging.INFO)


if __name__ == '__main__':
    logger.info("info log")
    logger.error("error log")
    logger.warning("warning log")
    logger.critical("critical log")
    hello()
    # still output
    logger.debug("debug log")
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("debug log")