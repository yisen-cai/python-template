import argparse
import logging

parser = argparse.ArgumentParser()
parser.add_argument("-log", "--log", nargs='+', help="Provide logging level. Example --log debug'")
log_level = parser.parse_args().log
log_level = log_level[0] if log_level is not None and len(log_level) > 0 else logging.INFO
