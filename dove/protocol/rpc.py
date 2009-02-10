'''
A set of things to ease in the development of Dove Services.
'''

class DoveService(object):
    '''
    A generic base class for all Dove RPC Services to inherit from
    '''
    def __init__(self):
        """docstring for __init__"""
        pass

def ServiceMethod(fn):
    '''
    A decorator for all Dove service methods. (To mark a specific method as
    a public instead of just a private method
    '''
    fn.IsServiceMethod = True
    return fn    
