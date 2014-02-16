from __future__ import (division, print_function, unicode_literals)
from future.builtins import *

import socket
import contextlib


@contextlib.contextmanager
def my_socket(*args):
    sock = socket.socket()
    sock.bind(*args)
    sock.listen(1)
    yield sock
    sock.close()


def serve(host, port, filename):
    with my_socket((host, port)) as sock, open(filename, 'ab+') as outf:
        while True:
            remote_sock, remote_addr = sock.accept()
            print('Accepted connection from {}'.format(remote_addr))
            message = remote_sock.recv(1024)
            print('Got message: {}'.format(message))
            chunks = message.split(' ')
            if len(chunks) != 2 or not chunks[0] or not chunks[1]:
                remote_sock.send(b'ERR')
            else:
                remote_sock.send(b'OK\n')
            remote_sock.close()
            outf.write(chunks)
            outf.write('\n'.encode('utf8'))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=u'Email fetch server')
    parser.add_argument('--host', type=str, default=u'localhost')
    parser.add_argument('--port', type=int, default=9000)
    parser.add_argument('--file', default='out.txt')
    args = parser.parse_args()
    serve(args.host, args.port, args.file)
