#!/usr/bin/env python

import sys
sys.path.append('.')
sys.path.append('..')

from dove.db import *

if __name__ == '__main__':
    print User.query.all()
