import argparse
import logging.config
from example.utils import hello

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# module-level logger
logger = logging.getLogger(__name__)
parser = argparse.ArgumentParser()
parser.add_argument("-log", "--log", nargs='+', help="Provide logging level. Example --log debug'")
log_level = parser.parse_args().log
log_level = log_level[0] if log_level is not None and len(log_level) > 0 else logging.INFO
logger.setLevel(log_level)


if __name__ == '__main__':
    logger.info("info log")
    logger.error("error log")
    logger.warning("warning log")
    logger.critical("critical log")
    hello()
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("debug log")
