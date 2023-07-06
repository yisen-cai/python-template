# Python logs



## Configs

~~~conf
# -------------------------------------------- Logger collection ------------------------------------------------------
[loggers]
keys=root

[logger_root]
handlers=consoleHandler,debugHandler,infoHandler,errorHandler



# -------------------------------------------- Handler collection -----------------------------------------------------
[handlers]
keys=consoleHandler,infoHandler,errorHandler,debugHandler

# console handler
[handler_consoleHandler]
class=StreamHandler
formatter=consoleFormatter
args=(sys.stdout,)

# file handler
[handler_infoHandler]
class=handlers.RotatingFileHandler
formatter=simpleFormatter
interval=midnight
backupCount=2
args=('logs/info.log','a', 5*1024*1024, 2, 'utf-8')


[handler_debugHandler]
level=DEBUG
class=handlers.RotatingFileHandler
formatter=simpleFormatter
interval=midnight
backupCount=2
args=('logs/debug.log','a', 5*1024*1024, 2, 'utf-8')


# file handler
[handler_errorHandler]
level=ERROR
# class=handlers.TimedRotatingFileHandler
class=handlers.RotatingFileHandler
formatter=simpleFormatter
interval=midnight
backupCount=2
args=('logs/error.log','a', 5*1024*1024, 2, 'utf-8')



# ------------------------------------------- Formatter collection ----------------------------------------------------
[formatters]
keys=simpleFormatter,cleanFormatter,consoleFormatter


[formatter_simpleFormatter]
format=%(asctime)s %(levelname)8s ---- %(filename)6s:%(lineno)s %(message)s

[formatter_consoleFormatter]
format=%(asctime)s %(levelname)8s ---- %(filename)6s:%(lineno)s %(message)s


# log pattern define
[formatter_cleanFormatter]
format=%(message)s
~~~

~~~bash
# shows like
2023-07-06 15:34:22,329     INFO ---- main.py:18 info log
2023-07-06 15:34:22,330    ERROR ---- main.py:19 error log
2023-07-06 15:34:22,330  WARNING ---- main.py:20 warning log
2023-07-06 15:34:22,330 CRITICAL ---- main.py:21 critical log
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





