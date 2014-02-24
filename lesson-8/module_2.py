
'''Logs using ial_logger'''


import logging_ial

logging_ial.set_level('info', __name__)

def do_diff(x, y):
    logging_ial.log('take away {} from {}'.format(y, x), 'info', __name__)
    return x - y


