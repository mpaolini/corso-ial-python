''' IAL Logger (second try) with OOP


Usage:

>>> import logging_ial_2
>>> logger = logging_ial_2.Logger()
>>> logger.set_level('debug')
>>> logger.log('network error', 'debug')
network error



To log to file do:

>>> import logging_ial_2
>>> logger = logging_ial_2.FileLogger('log.txt')
>>> logger.set_level('debug')
>>> logger.log('network error', 'debug')
>>> open('log.txt').read()
'network error\\n'
'''

from logging_ial import normalize


class Logger(object):

    def __init__(self):
        self.level = normalize('info')

    def set_level(self, level):
        self.level = normalize(level)

    def log(self, message, level):
        level_norm = normalize(level)
        if level_norm >= self.level:
            print message


class FileLogger(Logger):

    def __init__(self, filename):
        self.filename = filename
        super(FileLogger, self).__init__()

    def log(self, message, level):
        level_norm = normalize(level)
        if level_norm >= self.level:
            log_file = open(self.filename, 'a+b')
            log_file.write(message)
            log_file.write('\n')
