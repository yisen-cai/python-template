import logging

logging.basicConfig(filename='logs/basic.log', encoding='utf-8', filemode='w' level=logging.INFO)

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')