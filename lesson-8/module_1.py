'''Logs using ial_logger'''


import logging_ial

logging_ial.set_level('debug', __name__)

def do_sum(x, y):
    logging_ial.log('summing {} and {}'.format(x, y), 'debug', __name__)
    return x + y

def do_prod(x, y):
    logging_ial.log('multipling {} by {}'.format(x, y), 'info', __name__)
    return x * y

