import logging.config

from spiders.portal import Portal

# module-level logger
logging.config.fileConfig(
    'logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    Portal().run()

