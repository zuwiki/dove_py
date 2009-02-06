class DoveService(object):
    def __init__(self):
        """docstring for __init__"""
        pass

def ServiceMethod(fn):
    fn.IsServiceMethod = True
    return fn
    