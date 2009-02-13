#!/usr/bin/env python

import sys
sys.path.append('.')
sys.path.append('..')

from dove.protocol.transport import Transport, SocketHandler

if __name__ == '__main__':
    # TODO: Bug b20
    address = ('0.0.0.0', 4644)
    t = Transport(address, SocketHandler)
    t.debug = True
    t.serve_forever()
