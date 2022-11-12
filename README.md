# Python logs



## Configs

~~~conf
# loggers
[loggers]
keys=root

[logger_root]
level=DEBUG
handlers=consoleHandler,infoHandler


# define what kind output it does, file, log level, console output etc.
[handlers]
[handlers]
keys=consoleHandler,infoHandler
# console handler
[handler_consoleHandler]
class=StreamHandler
formatter=simpleFormatter
args=(sys.stdout,)

# file handler
[handler_infoHandler]
level=INFO
# class=handlers.TimedRotatingFileHandler
class=handlers.RotatingFileHandler
formatter=simpleFormatter
interval=midnight
backupCount=5
args=('logs/info.log','a')


# setting the output log format
[formatters]
keys=simpleFormatter

# log pattern define, the number after double bracket is the format length
[formatter_simpleFormatter]
format=%(asctime)s %(name)20s %(levelname)8s: %(message)s


# shows like
2022-11-12 13:16:11,553             __main__     INFO: info log
2022-11-12 13:16:11,554             __main__    ERROR: error log
2022-11-12 13:16:11,555             __main__  WARNING: warning log
2022-11-12 13:16:11,555             __main__ CRITICAL: critical log
2022-11-12 13:16:11,556        example.utils    DEBUG: hello world
2022-11-12 13:16:11,556             __main__    DEBUG: debug log
2022-11-12 13:16:11,557             __main__    DEBUG: debug log
~~~





## Package

If a file named `__init__.py` is present in a package directory, it is invoked when the package or a module in the package is imported. This can be used for execution of package initialization code, such as initialization of package-level data.



## Log level

### Main module init

~~~python
import logging
import logging.config

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# module-level logger
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    pass
~~~



### Package init

~~~python
# __init__.py
import logging.config

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# module-level logger
logger = logging.getLogger(__name__)
~~~



### Global log level

~~~
$ python main.py -log=INFO
~~~





