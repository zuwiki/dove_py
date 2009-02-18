#!/usr/bin/env python

import sys
sys.path.append('.')
sys.path.append('..')

from dove.logger import Logger
from dove.protocol.transport import Transport, SocketHandler

if __name__ == '__main__':

    # TODO: Bug 908
    logger = Logger()

    # TODO: Bug b20
    address = ('0.0.0.0', 4644)
    t = Transport(address, SocketHandler, logger=logger)
    t.debug = True
    t.serve_forever()
