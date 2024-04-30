import argparse
import logging.config

from spiders.portal import Portal

# module-level logger
logging.config.fileConfig(
    'logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def add_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-log", "--log", default='INFO', help="Provide logging level. Example --log INFO")
    log_level = parser.parse_args().log
    print(log_level)
    return log_level


if __name__ == '__main__':
    add_arguments()
