import argparse
import logging.config
from example.utils import hello
from spiders.portal import Portal

# module-level logger
logging.config.fileConfig(
    'logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    portal = Portal()
    portal.run()
