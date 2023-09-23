import logging
import os

logger = logging.getLogger(__name__)


def hello():
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("hello world")


def walks_dir(base_dir):
    for root, dirs, files in os.walk(base_dir, topdown=False):
        for name in files:
            print(os.path.join(root, name))
