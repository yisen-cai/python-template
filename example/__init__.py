import logging.config

from custom import CustomFormatter

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)


# module-level logger
logger = logging.getLogger(__name__)

# ch = logging.StreamHandler()
# ch.setFormatter(CustomFormatter())
# logger.addHandler(ch)
