''' Main logger module

Usage:

>>> import logging_ial

>>> logging_ial.set_level('debug',
...                       'module_name')
>>> logging_ial.log('network is down',
...                 'debug',
...                 'module_name')

To store your logs into a file use:
>>> logging_ial.log('network is down',
...                 'debug',
...                 'module_name',
...                 filename='log.txt')

You can use both numbers and strings for log_level param:

 - debug 0
 - info 1
 - warning 2
 - error 3

'''


def normalize(level):
    '''Returns an int'''
    if level in ('debug', 0):
        return 0
    if level in ('info', 1):
        return 1
    if level in ('warning', 2):
        return 2
    if level in ('error', 3):
        return 3
    raise ValueError('bad level: {}'.format(level))

# Dict mapping module_name -> level
LEVEL_CURRENT = {}
LEVEL_DEFAULT = normalize('info')

def set_level(level, module_name):
    global LEVEL_CURRENT
    level_norm = normalize(level)
    LEVEL_CURRENT[module_name] = level_norm

def log(message, level, module_name,
        filename=None):
    level_norm = normalize(level)
    level_current = LEVEL_CURRENT.get(module_name, LEVEL_DEFAULT)
    if level_norm >= level_current:
        if filename is None:
            print message
        else:
            log_file = open(filename, 'a+b')
            log_file.write(message)
            log_file.write('\n')
